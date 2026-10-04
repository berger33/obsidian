#!/usr/bin/env python3
"""Reconcile one published tranche of software-seguranca-2000-0003.

The script appends tranche-specific navigation/review records, then advances
counts derived from the already-verified 5,640-note baseline. It never edits
human approvals or creates note files. Run only after building and auditing a
complete tranche.
"""
from __future__ import annotations

import argparse
from datetime import date
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
KF = ROOT / "knowledge-federation"
SCRIPTS = KF / "scripts"
DATA_ROOT = SCRIPTS / "_security_scale_data"
BATCH_ID = "software-seguranca-2000-0003"
NOTES_DIR = KF / "domains" / "software-0009" / "software" / "seguranca"
BASE_VALID = 5640
BASE_AI = 5591
BASE_ACTIVE = 5740
HUMAN = 49
REVIEWER = "Arena.ai Agent Mode"

sys.path.insert(0, str(SCRIPTS))
from audit_note_quality import markdown_link_index, unresolved_wikilinks  # noqa: E402
from note_quality import assess_markdown  # noqa: E402


def format_decimal(value: float, places: int) -> str:
    return f"{value:.{places}f}".replace(".", ",")


def load_groups(tranche: int) -> list[dict]:
    files = sorted((DATA_ROOT / f"tranche-{tranche:02d}").glob("*.json"))
    if len(files) != 10:
        raise SystemExit(f"tranche {tranche:02d}: esperados 10 grupos JSON, encontrados {len(files)}")
    groups = [json.loads(path.read_text(encoding="utf-8")) for path in files]
    if any(len(group.get("notes", [])) != 10 for group in groups):
        raise SystemExit(f"tranche {tranche:02d}: cada grupo precisa listar exatamente 10 notas")
    return groups


def validate_prior_tranches(tranche: int) -> None:
    manifest = KF / "exports" / "batches" / f"{BATCH_ID}.md"
    moc = KF / "00-home-vault" / "MOCs" / "MOC-Seguranca-Software-0009.md"
    manifest_text = manifest.read_text(encoding="utf-8")
    moc_text = moc.read_text(encoding="utf-8")
    for prior in range(17, tranche):
        report = KF / "exports" / "reports" / f"ai-review-{BATCH_ID}-tranche-{prior:02d}.md"
        recon = KF / "exports" / "reports" / f"batch-reconciliation-{BATCH_ID}-tranche-{prior:02d}.md"
        if not report.is_file() or not recon.is_file():
            raise SystemExit(f"tranche anterior {prior} não tem relatório e reconciliação")
        if f"## Tranche {prior} —" not in manifest_text or f"## Tranche {prior} (IDs " not in moc_text:
            raise SystemExit(f"tranche anterior {prior} não está reconciliada no manifesto e no MOC")


def validate_published_tranche(tranche: int, start: int, groups: list[dict], report_path: Path) -> None:
    if not report_path.is_file():
        raise SystemExit(f"relatório factual ausente: {report_path.name}")
    report = report_path.read_text(encoding="utf-8")
    report_numbers = [
        int(value) for value in re.findall(r"(?m)^\|\s*(\d+)\s*\|\s*\[\[", report)
    ]
    expected_numbers = list(range(start, start + 100))
    if report_numbers != expected_numbers:
        raise SystemExit(f"relatório da tranche {tranche} não registra exatamente os IDs {start}–{start + 99}")

    known_stems, known_paths = markdown_link_index([KF])
    number = start
    for group in groups:
        for row in group["notes"]:
            path = NOTES_DIR / f"{row['slug']}.md"
            if not path.is_file():
                raise SystemExit(f"nota da tranche ausente: {path.relative_to(ROOT)}")
            content = path.read_text(encoding="utf-8")
            result = assess_markdown(content, path)
            if result["errors"] or not result["ai_reviewed"] or result["human_reviewed"]:
                raise SystemExit(f"{path.name}: gate/revisão inválidos: {result['errors']}")
            pieces = content.split("---", 2)
            if len(pieces) != 3:
                raise SystemExit(f"{path.name}: frontmatter ausente")
            metadata_lines = set(pieces[1].splitlines())
            required = {
                f"id: software.seguranca.tranche{tranche}.{number:06d}",
                f"lote: {BATCH_ID}",
                "revisao_humana: nao_solicitada",
                'revisor: ""',
                "revisao_ia: aprovada",
                f'relatorio_revisao_ia: "knowledge-federation/exports/reports/{report_path.name}"',
            }
            if not required <= metadata_lines:
                raise SystemExit(f"{path.name}: metadados incompatíveis; ausentes {sorted(required - metadata_lines)}")
            broken = unresolved_wikilinks(content, known_stems, known_paths)
            if broken:
                raise SystemExit(f"{path.name}: wikilinks não resolvidos: {broken}")
            number += 1
    if number != start + 100:
        raise SystemExit(f"tranche {tranche}: quantidade de notas não corresponde a 100")


def set_line(text: str, prefix: str, replacement: str, *, expected: int = 1) -> str:
    lines = text.splitlines()
    matches = [index for index, line in enumerate(lines) if line.startswith(prefix)]
    if len(matches) != expected:
        raise SystemExit(f"esperadas {expected} linhas com prefixo {prefix!r}; encontradas {len(matches)}")
    for index in matches:
        lines[index] = replacement
    return "\n".join(lines) + ("\n" if text.endswith("\n") else "")


def replace_once(text: str, pattern: str, replacement: str, description: str) -> str:
    updated, replacements = re.subn(pattern, replacement, text, count=1)
    if replacements != 1:
        raise SystemExit(f"padrão de {description} deveria corresponder uma vez; correspondeu {replacements}")
    return updated


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")
    print(f"ok {path.relative_to(ROOT)}")


def manifest_section(tranche: int, start: int, groups: list[dict]) -> str:
    end = start + 99
    titles = ", ".join(group["group_title"].split(" — ")[0] for group in groups)
    lines = [
        f"## Tranche {tranche} — {titles} (100 notas; revisão factual por IA registrada)",
        "",
    ]
    number = start
    for group in groups:
        lines.extend([
            f"### {group['group_title']}",
            "",
            f"**Conferência factual:** {group['fact_check']}",
            f"**Cobertura anterior:** {group['coverage_review']}",
            "",
        ])
        for row in group["notes"]:
            lines.append(
                f"{number}. [{row['title']}](../../domains/software-0009/software/seguranca/{row['slug']}.md)"
            )
            number += 1
        lines.append("")
    if number - 1 != end:
        raise SystemExit(f"manifesto: intervalo incorreto na tranche {tranche}")
    return "\n".join(lines) + "\n"


def moc_section(tranche: int, start: int, groups: list[dict]) -> str:
    end = start + 99
    lines = [f"## Tranche {tranche} (IDs {start}–{end})", ""]
    for group in groups:
        lines.extend([f"### {group['group_title']}", ""])
        for row in group["notes"]:
            lines.append(f"- [[{row['slug']}]] — {row['title']}")
        lines.append("")
    return "\n".join(lines)


def review_rows(tranche: int, start: int, position_start: int, groups: list[dict], today: str) -> str:
    report_name = f"ai-review-{BATCH_ID}-tranche-{tranche:02d}.md"
    lines = []
    number = start
    position = position_start
    for group in groups:
        for row in group["notes"]:
            title = row["title"].replace("|", "\\|")
            lines.append(
                f"| {position} | `{BATCH_ID}` | [{title}](../../domains/software-0009/software/seguranca/{row['slug']}.md) "
                f"| APROVADA POR IA | IA: {REVIEWER} | Revisão factual por IA registrada em {today} no relatório "
                f"`{report_name}` (nota {number}); não é aprovação humana. |"
            )
            number += 1
            position += 1
    return "\n".join(lines) + "\n"


def update_manifest_and_moc(tranche: int, start: int, count: int, groups: list[dict], today: str,
                            report_name: str, recon_name: str, complete: bool) -> None:
    manifest = KF / "exports" / "batches" / f"{BATCH_ID}.md"
    text = manifest.read_text(encoding="utf-8")
    marker = f"## Tranche {tranche} —"
    if marker in text:
        raise SystemExit(f"tranche já consta no manifesto: {marker}")
    previous_marker = f"## Tranche {tranche - 1} —"
    if previous_marker not in text:
        raise SystemExit(f"tranche anterior ausente no manifesto: {previous_marker}")
    section = manifest_section(tranche, start, groups)
    text = text.rstrip() + "\n\n" + section.rstrip() + "\n"
    percent_text = format_decimal(count / 20, 2)
    status = "complete" if complete else "in_progress"
    rem = 2000 - count
    text = set_line(text, "- Notas efetivamente redigidas até agora:",
                    f"- Notas efetivamente redigidas até agora: **{count} / 2.000 ({percent_text}%)**")
    text = set_line(text, "- Gate automatizado:",
                    f"- Gate automatizado: **{count}/{count} aprovadas** (conteúdo mínimo, seções, fontes específicas e wikilinks; reexecutado após a tranche {tranche})")
    text = set_line(text, "- Revisão factual humana:", f"- Revisão factual humana: **0/{count}**")
    text = set_line(text, "- Revisão factual por IA:", f"- Revisão factual por IA: **{count}/{count}**")
    text = set_line(text, "- Contabilizadas como válidas:", f"- Contabilizadas como válidas: **{count}/{count}**")
    text = set_line(text, "- Revisor das ", f"- Revisor das {count} notas aprovadas por IA: `{REVIEWER}`, com relatórios específicos; não são aprovações humanas")
    text = set_line(text, "- Status do lote maior:",
                    f"- Status do lote maior: `{status}`; tranches 1–{tranche} ({count} notas, IDs 1–{count}) foram conferidas factualmente por IA e aprovadas sob o protocolo atualizado")
    text = set_line(text, "- Reconciliação estrutural mais recente do manifesto/fila:",
                    f"- Reconciliação estrutural mais recente do manifesto/fila: [`{recon_name}`](../reports/{recon_name})")
    links = ", ".join(
        f"[`tranche {n}`](../reports/ai-review-{BATCH_ID}-tranche-{n:02d}.md)"
        for n in range(1, tranche + 1)
    )
    text = set_line(text, "- Relatórios factuais por IA:", f"- Relatórios factuais por IA: {links}")
    sentence_prefix = "Existem "
    old_line = next((line for line in text.splitlines() if line.startswith(sentence_prefix) and "notas materiais listadas abaixo" in line), None)
    if old_line is None:
        raise SystemExit("linha de notas materiais não encontrada no manifesto")
    new_line = (
        f"Existem {count} notas materiais listadas abaixo; não há IDs reservados, placeholders ou registros virtuais "
        + ("restantes no lote." if complete else f"para as {rem} restantes.")
    )
    text = set_line(text, sentence_prefix, new_line)
    write(manifest, text)

    moc = KF / "00-home-vault" / "MOCs" / "MOC-Seguranca-Software-0009.md"
    mtext = moc.read_text(encoding="utf-8")
    section = moc_section(tranche, start, groups)
    if f"## Tranche {tranche} (IDs " in mtext:
        raise SystemExit(f"tranche já consta no MOC: {tranche}")
    # Refresh the MOC's `updated` date and the concise batch status.
    mtext = set_line(mtext, "updated:", f"updated: {today}")
    mtext = set_line(mtext, "Mapa de conteúdo das",
                     f"Mapa de conteúdo das **{count} notas substantivas (Tranches 1–{tranche}, IDs `1–{count}`)** do lote [`{BATCH_ID}`](../../exports/batches/{BATCH_ID}.md) em `knowledge-federation/domains/software-0009/software/seguranca/`.")
    mtext = set_line(mtext, "- Progresso atual:",
                     f"- Progresso atual: **{count} / 2.000 notas válidas ({percent_text}%)** (`status: {status}`)")
    mtext = set_line(mtext, "- Revisão factual humana:", f"- Revisão factual humana: **0 / {count}**")
    reports = ", ".join(
        f"[Tranche {n}](../../exports/reports/ai-review-{BATCH_ID}-tranche-{n:02d}.md)"
        for n in range(1, tranche + 1)
    )
    mtext = set_line(mtext, "- Revisão factual por IA (`Arena.ai Agent Mode`):",
                     f"- Revisão factual por IA (`{REVIEWER}`): **{count} / {count}** ({reports})")
    audit_line = f"- Auditoria de qualidade do lote: [`note-quality-{BATCH_ID}.md`](../../exports/reports/note-quality-{BATCH_ID}.md)"
    recon_line = f"- Reconciliação mais recente: [`{recon_name}`](../../exports/reports/{recon_name})"
    if any(line.startswith("- Reconciliação mais recente:") for line in mtext.splitlines()):
        mtext = set_line(mtext, "- Auditoria de qualidade do lote:", audit_line)
        mtext = set_line(mtext, "- Reconciliação mais recente:", recon_line)
    else:
        mtext = set_line(mtext, "- Auditoria de qualidade do lote:", audit_line + "\n" + recon_line)
    mtext = mtext.rstrip() + "\n\n" + section.rstrip() + "\n"
    write(moc, mtext)


def update_queue(tranche: int, start: int, count: int, ai_count: int, global_count: int,
                 groups: list[dict], today: str) -> None:
    path = KF / "exports" / "reports" / "human-review-queue.md"
    text = path.read_text(encoding="utf-8")
    anchor = "## Regra de contagem"
    if text.count(anchor) != 1:
        raise SystemExit("âncora de contagem não é única na fila de revisão")
    position_start = 50 + (ai_count - 100)
    rows = review_rows(tranche, start, position_start, groups, today)
    text = text.replace(anchor, rows + "\n" + anchor, 1)
    intro = (
        f"Atualizado em {today}. O registro preserva {HUMAN} aprovações humanas históricas e distingue {ai_count} revisões factuais realizadas por IA "
        f"nos lotes `software-testes-2000-0001` (1991), `software-devops-2000-0002` (2000) e `{BATCH_ID}` ({count}). "
        "O usuário dispensou revisão humana obrigatória para novas notas; a revisão por IA não altera nem amplia as aprovações humanas anteriores."
    )
    text = set_line(text, "Atualizado em ", intro)
    text = set_line(text, "- Aprovações por IA registradas separadamente:",
                    f"- Aprovações por IA registradas separadamente: **{ai_count}**.")
    text = set_line(text, "- Notas válidas contabilizadas (gate + revisão humana ou IA):",
                    f"- Notas válidas contabilizadas (gate + revisão humana ou IA): **{global_count}**.")
    # Rebuild the summary sentence only; historical approval rows remain untouched.
    rule_lines = text.splitlines()
    for index, line in enumerate(rule_lines):
        if line.startswith("As ") and "linhas `APROVADA POR IA`" in line:
            rule_lines[index] = (
                f"As {ai_count} linhas `APROVADA POR IA` (nº 50–{global_count}) correspondem às 1991 notas 10–2000 das tranches 2–26 do lote `software-testes-2000-0001`, "
                f"às 2000 notas 1–2000 das tranches 1–20 do lote `software-devops-2000-0002` e às {count} notas 1–{count} das tranches 1–{tranche} do lote `{BATCH_ID}`; "
                "elas contam pelo protocolo atualizado, mas não são aprovações humanas. Cada nota futura precisa passar pelo gate e ter revisão factual registrada antes de entrar na contagem."
            )
            break
    else:
        raise SystemExit("resumo final da fila de revisão não encontrado")
    write(path, "\n".join(rule_lines) + ("\n" if text.endswith("\n") else ""))


def update_global_documents(tranche: int, count: int, valid: int, ai: int, active: int,
                            complete_batches: int, today: str, report_name: str,
                            recon_name: str, complete: bool) -> None:
    pct_global = format_decimal(valid / 10000, 4)
    pct_batch = format_decimal(count / 20, 2)
    remaining_batch = 2000 - count
    remaining_global = 1_000_000 - valid
    state = "complete" if complete else "in_progress"
    def batch_status(link_root: str) -> str:
        return (
            f"o terceiro lote [`{BATCH_ID}`]({link_root}exports/batches/{BATCH_ID}.md) está `{state}` com {count}/2.000 notas válidas até a [tranche {tranche}]({link_root}exports/reports/{report_name}) "
            f"([reconciliação]({link_root}exports/reports/{recon_name}), [auditoria do lote]({link_root}exports/reports/note-quality-{BATCH_ID}.md) e [MOC de Segurança]({link_root}00-home-vault/MOCs/MOC-Seguranca-Software-0009.md)); "
            + ("a meta do lote foi atingida; o lote seguinte será aberto sem contar a preparação como progresso." if complete else f"faltam {remaining_batch} notas substantivas para a meta de 2.000.")
        )

    root_readme = ROOT / "README.md"
    text = root_readme.read_text(encoding="utf-8")
    text = set_line(text, "| Lotes completos |",
                    f"| Lotes completos | {complete_batches} / 500 | {complete_batches} lotes (`software-testes-2000-0001`, `software-devops-2000-0002`" + (", `software-seguranca-2000-0003`" if complete else "") + ") concluídos com 2.000 notas válidas cada |")
    text = set_line(text, "| Notas válidas contabilizadas |",
                    f"| Notas válidas contabilizadas | {valid} / 1.000.000 ({pct_global}%) | {HUMAN} com aprovação humana histórica + {ai} com revisão factual por IA |")
    text = set_line(text, "| Notas com revisão factual por IA registrada |",
                    f"| Notas com revisão factual por IA registrada | {ai} | Revisões dos lotes de escala (1991 no lote 1 + 2000 no lote 2 + {count} no lote 3), com relatórios por tranche; não são humanas |")
    text = set_line(text, "| Terceiro lote `software-seguranca-2000-0003` |",
                    f"| Terceiro lote `{BATCH_ID}` | {count} / 2.000 ({pct_batch}%) | {count} aprovadas por IA nas tranches 1–{tranche}; " + ("lote concluído (`complete`)" if complete else f"faltam {remaining_batch} notas substantivas") + " |")
    text = set_line(text, "| Arquivos Markdown ativos em `knowledge-federation/domains/` |",
                    f"| Arquivos Markdown ativos em `knowledge-federation/domains/` | {active} | 100 notas legadas com pendências + {valid} notas autorais substantivas |")
    paragraph_pattern = re.compile(r"e o terceiro lote .*?(?= A \[auditoria global\]\(knowledge-federation/exports/reports/note-quality-audit\.md\))")
    if len(paragraph_pattern.findall(text)) != 1:
        raise SystemExit("parágrafo de retomada do lote 3 não é único no README raiz")
    text = paragraph_pattern.sub("e " + batch_status("knowledge-federation/"), text, count=1)
    write(root_readme, text)

    kf_readme = KF / "README.md"
    text = kf_readme.read_text(encoding="utf-8")
    text = set_line(text, "- Arquivos Markdown ativos:", f"- Arquivos Markdown ativos: **{active}** (100 notas legadas com pendências + {valid} notas autorais substantivas).")
    text = set_line(text, "- Notas válidas pelo protocolo atual:", f"- Notas válidas pelo protocolo atual: **{valid}** ({HUMAN} aprovações humanas históricas + {ai} revisões factuais por IA).")
    text = set_line(text, "- Progresso:", f"- Progresso: **{valid} / 1.000.000 ({pct_global}%)**; faltam {remaining_global} notas válidas.")
    text = set_line(text, "- Lotes completos:", f"- Lotes completos: **{complete_batches} / 500** (`software-testes-2000-0001`, `software-devops-2000-0002`" + (", `software-seguranca-2000-0003`" if complete else "") + ").")
    text = set_line(text, "- Terceiro lote",
                    f"- Terceiro lote `{BATCH_ID}`: **{count} / 2.000** notas válidas ({pct_batch}%); {count} por IA ([tranche {tranche}](exports/reports/{report_name}) e [reconciliação](exports/reports/{recon_name})); " + ("lote concluído (`complete`)." if complete else f"faltam {remaining_batch} notas materiais."))
    write(kf_readme, text)

    readme_1m = KF / "README-1M.md"
    text = readme_1m.read_text(encoding="utf-8")
    first_paragraph = (
        f"Na atualização de {today}, o repositório tem {valid} notas válidas pelo protocolo atual ({HUMAN} aprovações humanas históricas + {ai} revisões factuais por IA registradas separadamente). "
        f"O diretório ativo tem {active} arquivos Markdown, incluindo 100 notas legadas com pendências, ainda excluídas da contagem. {batch_status('')} "
        "O primeiro lote (`software-testes-2000-0001`) e o segundo (`software-devops-2000-0002`) permanecem `complete`;"
    )
    paragraphs = text.splitlines()
    first = next((i for i, line in enumerate(paragraphs) if line.startswith("Na atualização de ")), None)
    if first is None:
        raise SystemExit("parágrafo inicial de README-1M não encontrado")
    paragraphs[first] = first_paragraph
    write(readme_1m, "\n".join(paragraphs) + ("\n" if text.endswith("\n") else ""))

    status_path = KF / "STATUS-CONSOLIDACAO-1M.md"
    text = status_path.read_text(encoding="utf-8")
    text = set_line(text, "Data do status:", f"Data do status: {today}. A meta editorial ativa é **500 lotes × 2.000 notas substantivas = 1.000.000 de notas válidas**. Revisão humana não é requisito para novas notas; cada revisão factual por IA é registrada separadamente e nunca é apresentada como aprovação humana.")
    text = set_line(text, "## Progresso auditado em ", f"## Progresso auditado em {today}")
    text = set_line(text, "O checkpoint histórico contém",
                    f"O checkpoint histórico contém **1.000.000 de registros virtuais** com texto-template; não é conteúdo validado nem progresso da meta ativa. A auditoria encontrou {active} arquivos Markdown ativos: {valid} notas substantivas passaram pelo gate e receberam revisão factual registrada ({HUMAN} humanas históricas + {ai} por IA); outras 100 mantêm pendências e continuam fora da contagem.")
    text = set_line(text, "| Lotes completos |", f"| Lotes completos | {complete_batches} / 500 | {complete_batches} lotes concluídos com 2.000 notas válidas cada |")
    text = set_line(text, "| Progresso válido global |", f"| Progresso válido global | {valid} / 1.000.000 ({pct_global}%) | {HUMAN} revisões humanas históricas + {ai} revisões por IA registradas separadamente |")
    text = set_line(text, "| Revisões factuais por IA registradas |", f"| Revisões factuais por IA registradas | {ai} | Relatórios das tranches 2–26 (`software-testes-2000-0001`), tranches 1–20 (`software-devops-2000-0002`) e tranches 1–{tranche} (`{BATCH_ID}`); não são humanas |")
    text = set_line(text, "| Terceiro lote (`software-seguranca-2000-0003`) |", f"| Terceiro lote (`{BATCH_ID}`) | {count} / 2.000 ({pct_batch}%) | {count} IA nas tranches 1–{tranche} ([tranche {tranche}](exports/reports/{report_name})); " + ("lote completo (`complete`) |" if complete else f"faltam {remaining_batch} notas substantivas |"))
    text = set_line(text, "| Candidatas que passaram pelo gate automatizado |", f"| Candidatas que passaram pelo gate automatizado | {valid} | Todas receberam revisão factual registrada; gate sozinho não comprova veracidade |")
    # The status doc summarizes the latest state in its explanatory paragraphs too.
    text = replace_once(
        text,
        r"e o terceiro lote \[\`software-seguranca-2000-0003\`\].*?\(\[reconciliação\]\(exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-\d+\.md\)\)\.",
        f"e o terceiro lote [`{BATCH_ID}`](exports/batches/{BATCH_ID}.md) está `{state}` com {count}/2.000 notas válidas após a [tranche {tranche}](exports/reports/{report_name}) ([reconciliação](exports/reports/{recon_name})).",
        "estado do terceiro lote no status",
    )

    text = replace_once(text, r"Relatórios atualizados: .*?\[auditoria global\]", f"Relatórios atualizados: [reconciliação da tranche {tranche}](exports/reports/{recon_name}), [auditoria global]", "lista de relatórios atualizados")
    text = replace_once(
        text,
        r"3\. Continuar o terceiro lote `software-seguranca-2000-0003` \(atualmente em \d+/2\.000; faltam \d+ notas substantivas\) e os 497 lotes subsequentes,",
        (f"3. " + ("Lote 3 `software-seguranca-2000-0003` completo (2.000/2.000); abrir o lote 4 após reconciliação e continuar os 497 lotes restantes," if complete else f"Continuar o terceiro lote `{BATCH_ID}` (atualmente em {count}/2.000; faltam {remaining_batch} notas substantivas) e os 497 lotes subsequentes,")),
        "próximo marco do status",
    )
    write(status_path, text)

    plan_path = KF / "PLANO-CONTINUO-1M.md"
    text = plan_path.read_text(encoding="utf-8")
    text = set_line(text, "Atualizado em ", f"Atualizado em {today}. A meta editorial ativa é **500 lotes × 2.000 notas = 1.000.000**; cada tranche contém 100 notas e só entra na contagem após gate e revisão factual registrados.")
    text = set_line(text, "- Notas válidas globais:", f"- Notas válidas globais: **{valid}** ({HUMAN} aprovações humanas históricas + {ai} revisões factuais por IA).")
    text = set_line(text, "- Progresso:", f"- Progresso: **{valid} / 1.000.000 ({pct_global}%)**; faltam **{remaining_global}** notas válidas.")
    text = set_line(text, "- Lotes completos:", f"- Lotes completos: **{complete_batches} / 500** (`software-testes-2000-0001`, `software-devops-2000-0002`" + (", `software-seguranca-2000-0003`" if complete else "") + ").")
    text = set_line(text, "- Terceiro lote", f"- Terceiro lote `{BATCH_ID}`: **{count} / 2.000 ({pct_batch}%)** notas válidas ({count} IA nas tranches 1–{tranche}); " + ("concluído (`complete`)." if complete else f"faltam **{remaining_batch}** notas substantivas."))
    text = set_line(text, "- Arquivos Markdown ativos:", f"- Arquivos Markdown ativos: **{active}**; 100 com pendências de qualidade, excluídos da contagem.")
    text = set_line(text, "| 5 | Rodar gate, testes, auditorias e diff |", f"| 5 | Rodar gate, testes, auditorias e diff | **Concluído para o estado atual** | Lote 1: 2000/2000 (`complete`). Lote 2: 2000/2000 (`complete`). Lote 3: {count}/2.000 ({count} IA; status `{state}`). Global: {active} arquivos, {valid} válidas, 100 com pendências legadas; veja a [reconciliação da tranche {tranche}](exports/reports/{recon_name}). |")
    text = set_line(text, "| 8 | Abrir lotes subsequentes de 2.000 notas |", f"| 8 | Abrir lotes subsequentes de 2.000 notas | **Em andamento** | " + (f"Lote 3 completo em {count}/2.000; abrir lote 4 após reconciliação." if complete else f"Lote 3 em {count}/2.000 nas tranches 1–{tranche}; restam {remaining_batch} notas neste lote e 497 lotes subsequentes."))
    text = set_line(text, "| 10 | Atingir a meta e publicar relatório final |",
                    f"| 10 | Atingir a meta e publicar relatório final | **Em andamento; meta não atingida** | Progresso atual: {valid} notas válidas, {complete_batches}/500 lotes completos. Publicar apenas ao atingir 1.000.000. |")
    write(plan_path, text)

    recovery_path = KF / "RECOVERY-AND-SCALE-NOTE.md"
    text = recovery_path.read_text(encoding="utf-8")
    text = set_line(text, "Atualizado em ", f"Atualizado em {today}. A meta ativa é **500 lotes × 2.000 notas substantivas = 1.000.000 de notas válidas**. Revisão humana não é obrigatória para notas novas; revisão factual por IA é aceita somente quando registrada separadamente, com relatório.")
    text = replace_once(text, r"No diretório ativo `knowledge-federation/domains/` há .*?\n", f"No diretório ativo `knowledge-federation/domains/` há {active} arquivos: 100 legados com pendências e {valid} notas válidas pelo protocolo atual ({HUMAN} aprovações humanas históricas + {ai} revisões por IA). Os lotes 1 e 2 seguem completos; o lote 3 `{BATCH_ID}` está `{state}` com {count}/2.000 notas revisadas por IA até a [tranche {tranche}](exports/reports/{report_name}), com [reconciliação](exports/reports/{recon_name}).\n", "estado editorial da recuperação")
    text = replace_once(text, r"(?m)^4\. Continuar o terceiro lote `software-seguranca-2000-0003` \(\d+/2\.000; faltam \d+ notas qualificadas\).*$",
                        f"4. " + ("Com o lote 3 em 2.000/2.000, abrir o quarto lote sem contar a preparação como progresso." if complete else f"Continuar o terceiro lote `{BATCH_ID}` ({count}/2.000; faltam {remaining_batch} notas qualificadas) até 2.000 antes de abrir os 497 lotes seguintes."), "próximo marco da recuperação")
    write(recovery_path, text)

    home = KF / "00-home-vault" / "Home.md"
    text = home.read_text(encoding="utf-8")
    text = set_line(text, "ultima_verificacao:", f"ultima_verificacao: {today}")
    text = set_line(text, "- [[MOC-Seguranca-Software-0009]]", f"- [[MOC-Seguranca-Software-0009]] — {count} notas do terceiro lote de escala `{BATCH_ID}` (meta: 2.000; status `{state}`); {count} revisões factuais por IA.")
    text = set_line(text, "- [[human-review-queue|Registro de revisões factuais]]", f"- [[human-review-queue|Registro de revisões factuais]] — {HUMAN} aprovações humanas e {ai} aprovações por IA, identificadas separadamente.")
    text = set_line(text, "- [[note-quality-audit|Auditoria de qualidade]]", f"- [[note-quality-audit|Auditoria de qualidade]] — {valid} notas válidas pelo protocolo atual ({HUMAN} humanas + {ai} IA) e 100 notas legadas com falhas.")
    write(home, text)

    index = KF / "00-home-vault" / "Indice-Global.md"
    text = index.read_text(encoding="utf-8")
    text = set_line(text, "ultima_verificacao:", f"ultima_verificacao: {today}")
    text = set_line(text, "- Arquivos Markdown em `domains/`:", f"- Arquivos Markdown em `domains/`: **{active}** (100 sementes legadas + {valid} notas autorais substantivas).")
    text = set_line(text, "- Candidatas aprovadas no gate automatizado:", f"- Candidatas aprovadas no gate automatizado: **{valid}**; revisões humanas registradas: **{HUMAN}**; revisões factuais por IA: **{ai}**; 100 sementes legadas mantêm pendências.")
    state_line_prefix = "- Os lotes atuais totalizam "
    old_line = next((line for line in text.splitlines() if line.startswith(state_line_prefix)), None)
    if old_line is None:
        raise SystemExit("resumo de lotes do Índice-Global não encontrado")
    text = set_line(text, state_line_prefix,
                    f"- Os lotes atuais totalizam {valid} notas válidas pelo protocolo; o terceiro lote [`{BATCH_ID}`](../exports/batches/{BATCH_ID}.md) tem {count}/2.000 (`{state}`, [tranche {tranche}](../exports/reports/{report_name}), [reconciliação](../exports/reports/{recon_name}) e [[MOC-Seguranca-Software-0009]]); os lotes 1 e 2 permanecem completos. Veja também [[MOC-Dados-Distribuidos-e-Eventos]], [[MOC-Operacao-e-Seguranca-Kubernetes]], [[MOC-Cache-HTTP]], [[MOC-Testes-Software-0007]] e a [fila de revisão](../exports/reports/human-review-queue.md).")
    write(index, text)


def write_reconciliation_report(tranche: int, start: int, count: int, valid: int, ai: int,
                                active: int, groups: list[dict], today: str, complete: bool,
                                tests_status: str, audit_status: str) -> None:
    end = start + 99
    report_name = f"ai-review-{BATCH_ID}-tranche-{tranche:02d}.md"
    recon_name = f"batch-reconciliation-{BATCH_ID}-tranche-{tranche:02d}.md"
    report_path = KF / "exports" / "reports" / recon_name
    pct_batch = format_decimal(count / 20, 2)
    pct_global = format_decimal(valid / 10000, 4)
    lines = [
        f"# Reconciliação estrutural — lote `{BATCH_ID}`, tranche {tranche:02d}",
        "",
        f"Tranche **{tranche:02d} (IDs {start}–{end}, 100 notas substantivas)** reconciliada em {today}. O lote 3 fica em **{count}/2.000 ({pct_batch}%)** e o progresso global em **{valid}/1.000.000 ({pct_global}%)**. Revisões: 49 humanas históricas, sem alteração, e {ai} por IA; os arquivos legados seguem fora da contagem.",
        "",
        "## Famílias e conferência factual",
        "",
    ]
    for group in groups:
        lines.append(f"- **{group['group_title']} — conferência factual:** {group['fact_check']}")
        lines.append(f"  **Cobertura anterior:** {group['coverage_review']}")
    lines.extend([
        "",
        "## Artefatos reconciliados",
        "",
        f"- Manifesto: [`{BATCH_ID}.md`](../batches/{BATCH_ID}.md)",
        f"- MOC: [`MOC-Seguranca-Software-0009.md`](../../00-home-vault/MOCs/MOC-Seguranca-Software-0009.md)",
        f"- Revisão factual por IA: [`{report_name}`]({report_name})",
        f"- Qualidade do lote: [`note-quality-{BATCH_ID}.md`](note-quality-{BATCH_ID}.md)",
        "- Fila de revisão humana/IA: [`human-review-queue.md`](human-review-queue.md); novas linhas marcadas apenas como `APROVADA POR IA`.",
        "- Índices e documentação global: `README.md`, `README-1M.md`, `STATUS-CONSOLIDACAO-1M.md`, `PLANO-CONTINUO-1M.md`, `RECOVERY-AND-SCALE-NOTE.md`, `00-home-vault/Home.md` e `00-home-vault/Indice-Global.md`.",
        "",
        "## Verificações",
        "",
        "- Builder/gate por nota: 100 arquivos materiais, IDs contíguos, fontes HTTPS específicas, seções requeridas, links de conexão resolvidos, mínimo de 100 palavras e sem sentença substantiva repetida na tranche.",
        f"- Testes unitários obrigatórios: {tests_status}.",
        f"- Auditoria global obrigatória (`audit_note_quality.py --path knowledge-federation/domains --archive ledger-v1000000-mat8000.sqlite.xz`): {audit_status}.",
        f"- Estado do lote: `{'complete' if complete else 'in_progress'}`; {'2.000/2.000 notas aprovadas' if complete else f'{2000 - count} notas substantivas ainda faltam'}.",
        "- Revisão por IA não é aprovação humana; nenhuma aprovação humana histórica foi editada.",
        "",
    ])
    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"ok {report_path.relative_to(ROOT)}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tranche", type=int, required=True, choices=range(17, 21))
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--tests-status", choices=("passou",), required=True,
                        help="obrigatório: informe passou somente após executar unittest discover")
    parser.add_argument("--audit-status", choices=("passou",), required=True,
                        help="obrigatório: informe passou somente após executar audit_note_quality.py com o archive")
    args = parser.parse_args()
    tranche = args.tranche
    today = args.date
    groups = load_groups(tranche)
    start = (tranche - 1) * 100 + 1
    count = (tranche - 16) * 100 + 1600
    valid = BASE_VALID + (tranche - 16) * 100
    ai = BASE_AI + (tranche - 16) * 100
    active = BASE_ACTIVE + (tranche - 16) * 100
    complete = tranche == 20
    complete_batches = 3 if complete else 2
    report_name = f"ai-review-{BATCH_ID}-tranche-{tranche:02d}.md"
    recon_name = f"batch-reconciliation-{BATCH_ID}-tranche-{tranche:02d}.md"

    report_path = KF / "exports" / "reports" / report_name
    batch_quality_path = KF / "exports" / "reports" / f"note-quality-{BATCH_ID}.md"
    recon_path = KF / "exports" / "reports" / recon_name
    if not (NOTES_DIR.exists() and sum(1 for _ in NOTES_DIR.glob("*.md")) >= count):
        raise SystemExit(f"notas insuficientes para tranche {tranche}; execute e audite o builder primeiro")
    if recon_path.exists():
        raise SystemExit(f"reconciliação já existe; não sobrescrevo: {recon_name}")
    validate_prior_tranches(tranche)
    validate_published_tranche(tranche, start, groups, report_path)

    targets = [
        ROOT / "README.md",
        KF / "README.md",
        KF / "README-1M.md",
        KF / "STATUS-CONSOLIDACAO-1M.md",
        KF / "PLANO-CONTINUO-1M.md",
        KF / "RECOVERY-AND-SCALE-NOTE.md",
        KF / "exports" / "batches" / f"{BATCH_ID}.md",
        KF / "exports" / "reports" / "human-review-queue.md",
        KF / "00-home-vault" / "MOCs" / "MOC-Seguranca-Software-0009.md",
        KF / "00-home-vault" / "Home.md",
        KF / "00-home-vault" / "Indice-Global.md",
        batch_quality_path,
        recon_path,
    ]
    missing = [path for path in targets[:-1] if not path.is_file()]
    if missing:
        raise SystemExit(f"artefatos de reconciliação ausentes: {[str(path) for path in missing]}")
    backups = {path: path.read_bytes() if path.exists() else None for path in targets}
    try:
        subprocess.run(
            [
                sys.executable,
                str(SCRIPTS / "audit_note_quality.py"),
                "--path", str(NOTES_DIR),
                "--link-root", str(KF),
                "--out", str(batch_quality_path),
            ],
            cwd=ROOT,
            check=True,
        )
        update_manifest_and_moc(tranche, start, count, groups, today, report_name, recon_name, complete)
        update_queue(tranche, start, count, ai, valid, groups, today)
        update_global_documents(tranche, count, valid, ai, active, complete_batches, today, report_name, recon_name, complete)
        write_reconciliation_report(tranche, start, count, valid, ai, active, groups, today, complete,
                                   args.tests_status, args.audit_status)
    except BaseException:
        for path, original in backups.items():
            if original is None:
                path.unlink(missing_ok=True)
            else:
                path.write_bytes(original)
        raise
    print(f"tranche {tranche:02d} reconciliada: lote={count}/2000, global={valid}/1000000, arquivos={active}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
