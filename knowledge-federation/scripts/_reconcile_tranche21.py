#!/usr/bin/env python3
"""Reconcile tranche 21 across manifest, MOC, review registry and status docs.

Every replacement is asserted: a missing pattern aborts the script instead of
silently leaving a stale count in the editorial documents. The script is
idempotent: re-running it skips blocks and pairs already applied.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KF = ROOT / "knowledge-federation"
SCRIPTS = KF / "scripts"
BATCH_ID = "software-testes-2000-0001"
REPORT_NAME = "ai-review-software-testes-2000-0001-tranche-21.md"
RECON_NAME = "batch-reconciliation-software-testes-2000-0001-tranche-21.md"
DATE = "2026-10-03"


def load_builder():
    spec = importlib.util.spec_from_file_location("b21", SCRIPTS / "_build_tranche21.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_groups(b21):
    groups = []
    for path in sorted(b21.DATA_DIR.glob("*.txt")):
        context, rows = b21.parse_group(path)
        groups.append((context, rows))
    return groups


def manifest_section(groups) -> str:
    lines = ["## Tranche 21 — executores de navegador e de unidade, asserções, dublês, cassetes HTTP, mutação e fuzzing (100 notas; revisão factual por IA registrada)", ""]
    for context, rows in groups:
        lines.append(f"### {context['group']}")
        lines.append("")
        for index, row in enumerate(rows):
            number = int(context["first"]) + index
            lines.append(
                f"{number}. [{row['title']}](../../domains/software-0007/software/testes/{row['slug']}.md)"
            )
        lines.append("")
    return "\n".join(lines) + "\n"


def moc_section(groups) -> str:
    lines = ["## Tranche 21 — executores de navegador e de unidade, asserções, dublês, cassetes HTTP, mutação e fuzzing", ""]
    for context, rows in groups:
        lines.append(f"### {context['group']}")
        lines.append("")
        for index, row in enumerate(rows):
            number = int(context["first"]) + index
            lines.append(f"{number}. [[{row['slug']}]] — {row['summary']}")
        lines.append("")
    return "\n".join(lines) + "\n"


def review_rows(groups) -> str:
    lines = []
    for context, rows in groups:
        for index, row in enumerate(rows):
            number = int(context["first"]) + index
            position = 1500 + (number - 1460)
            lines.append(
                f"| {position} | `{BATCH_ID}` | [{row['title']}](../../domains/software-0007/software/testes/{row['slug']}.md) "
                f"| APROVADA POR IA | IA: Arena.ai Agent Mode | Revisão factual por IA registrada em {DATE} no relatório "
                f"`{REPORT_NAME}` (nota {number}); não é aprovação humana. |"
            )
    return "\n".join(lines) + "\n"


def apply(path: Path, pairs: list[tuple[str, str]]) -> None:
    text = path.read_text(encoding="utf-8")
    original = text
    for old, new in pairs:
        if new in text:
            # Already applied (covers pairs whose old text is a prefix of the new text).
            continue
        count = text.count(old)
        if count == 0:
            raise SystemExit(f"{path.relative_to(ROOT)}: padrão não encontrado: {old[:140]}")
        if count != 1:
            raise SystemExit(f"{path.relative_to(ROOT)}: padrão encontrado {count} vezes: {old[:140]}")
        text = text.replace(old, new)
    if text == original:
        print(f"já reconciliado {path.relative_to(ROOT)}")
        return
    path.write_text(text, encoding="utf-8")
    print(f"ok {path.relative_to(ROOT)}")


def insert_before(path: Path, anchor: str, block: str, marker: str | None = None) -> None:
    text = path.read_text(encoding="utf-8")
    marker = marker if marker is not None else block.splitlines()[0]
    if marker in text:
        print(f"já presente {path.relative_to(ROOT)}")
        return
    if text.count(anchor) != 1:
        raise SystemExit(f"{path.relative_to(ROOT)}: âncora encontrada {text.count(anchor)} vezes: {anchor}")
    text = text.replace(anchor, block + anchor, 1)
    path.write_text(text, encoding="utf-8")
    print(f"ok inserção {path.relative_to(ROOT)}")


def main() -> None:
    b21 = load_builder()
    groups = load_groups(b21)
    total = sum(len(rows) for _, rows in groups)
    if total != 100 or int(groups[0][0]["first"]) != 1460 or int(groups[-1][0]["first"]) != 1550:
        raise SystemExit(f"dados inesperados: {total} notas, primeiro grupo em {groups[0][0]['first']}")

    manifest = KF / "exports" / "batches" / f"{BATCH_ID}.md"
    moc = KF / "00-home-vault" / "MOCs" / "MOC-Testes-Software-0007.md"
    queue = KF / "exports" / "reports" / "human-review-queue.md"

    insert_before(manifest, "## Critérios e próximo passo", manifest_section(groups))
    insert_before(moc, "## Estado editorial", moc_section(groups))
    queue_block = review_rows(groups)
    insert_before(queue, "## Regra de contagem", queue_block)

    # --- Manifest ---
    apply(manifest, [
        ("- Notas efetivamente redigidas até agora: **1459 / 2.000 (72,95%)**",
         "- Notas efetivamente redigidas até agora: **1559 / 2.000 (77,95%)**"),
        ("- Gate automatizado: **1459/1459 aprovadas**", "- Gate automatizado: **1559/1559 aprovadas**"),
        ("reexecutado após a tranche 20)", "reexecutado após a tranche 21)"),
        ("- Revisão factual humana: **9/1459**", "- Revisão factual humana: **9/1559**"),
        ("- Revisão factual por IA: **1450/1459**", "- Revisão factual por IA: **1550/1559**"),
        ("Contabilizadas como válidas: **1459/1459**", "Contabilizadas como válidas: **1559/1559**"),
        ("- Revisor das 1450 notas aprovadas por IA", "- Revisor das 1550 notas aprovadas por IA"),
        ("tranches 2–20 (1450 notas, IDs 10–1459) foram conferidas factualmente por IA",
         "tranches 2–21 (1550 notas, IDs 10–1559) foram conferidas factualmente por IA"),
        ("[`tranche 20`](../reports/ai-review-software-testes-2000-0001-tranche-20.md)",
         "[`tranche 20`](../reports/ai-review-software-testes-2000-0001-tranche-20.md), [`tranche 21`](../reports/ai-review-software-testes-2000-0001-tranche-21.md)"),
        (f"[`batch-reconciliation-software-testes-2000-0001-tranche-20.md`](../reports/batch-reconciliation-software-testes-2000-0001-tranche-20.md)",
         f"[`{RECON_NAME}`](../reports/{RECON_NAME})"),
        ("Existem 1459 notas materiais listadas abaixo; não há IDs reservados, placeholders ou registros virtuais para as 541 restantes.",
         "Existem 1559 notas materiais listadas abaixo; não há IDs reservados, placeholders ou registros virtuais para as 441 restantes."),
        ("as 1450 notas 10–1459 das tranches 2–20 têm revisão factual por IA registrada nos relatórios vinculados",
         "as 1550 notas 10–1559 das tranches 2–21 têm revisão factual por IA registrada nos relatórios vinculados"),
        ("são 1459/2.000 notas válidas, restando 541 notas materiais",
         "são 1559/2.000 notas válidas, restando 441 notas materiais"),
    ])

    # --- MOC ---
    apply(moc, [
        ("Índice das 1459 notas substantivas redigidas até agora no lote `software-testes-2000-0001`, cuja meta é 2.000. As 1459 passaram pelo gate automatizado e têm revisão factual registrada: nove aprovadas pelo usuário e 1450 aprovadas por IA",
         "Índice das 1559 notas substantivas redigidas até agora no lote `software-testes-2000-0001`, cuja meta é 2.000. As 1559 passaram pelo gate automatizado e têm revisão factual registrada: nove aprovadas pelo usuário e 1550 aprovadas por IA"),
        ("O gate automatizado foi aprovado por 1459/1459 notas e as 1459 contam como válidas pelo protocolo atualizado: nove têm aprovação humana histórica e 1450 têm revisão factual por IA registrada separadamente. O lote de 2.000 continua `in_progress` (1459 notas substantivas; 541 ainda não produzidas).",
         "O gate automatizado foi aprovado por 1559/1559 notas e as 1559 contam como válidas pelo protocolo atualizado: nove têm aprovação humana histórica e 1550 têm revisão factual por IA registrada separadamente. O lote de 2.000 continua `in_progress` (1559 notas substantivas; 441 ainda não produzidas)."),
        ("[reconciliação mais recente do manifesto/fila](../../exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-20.md)",
         f"[reconciliação mais recente do manifesto/fila](../../exports/reports/{RECON_NAME})"),
        (", [19](../../exports/reports/ai-review-software-testes-2000-0001-tranche-19.md) e [20](../../exports/reports/ai-review-software-testes-2000-0001-tranche-20.md).",
         ", [19](../../exports/reports/ai-review-software-testes-2000-0001-tranche-19.md), [20](../../exports/reports/ai-review-software-testes-2000-0001-tranche-20.md) e [21](../../exports/reports/ai-review-software-testes-2000-0001-tranche-21.md)."),
    ])

    # --- Review queue ---
    apply(queue, [
        ("distingue 1450 revisões factuais realizadas por IA no lote `software-testes-2000-0001`",
         "distingue 1550 revisões factuais realizadas por IA no lote `software-testes-2000-0001`"),
        ("- Aprovações por IA registradas separadamente: **1450**.",
         "- Aprovações por IA registradas separadamente: **1550**."),
        ("- Notas válidas contabilizadas (gate + revisão humana ou IA): **1499**.",
         "- Notas válidas contabilizadas (gate + revisão humana ou IA): **1599**."),
        ("As 1450 linhas `APROVADA POR IA` (nº 50–1499) correspondem às notas 10–1459 e às revisões documentadas nos relatórios das tranches 2–20",
         "As 1550 linhas `APROVADA POR IA` (nº 50–1599) correspondem às notas 10–1559 e às revisões documentadas nos relatórios das tranches 2–21"),
    ])

    # --- Root README ---
    apply(ROOT / "README.md", [
        ("| Notas válidas contabilizadas | 1499 / 1.000.000 (0,1499%) | 49 com aprovação humana histórica + 1450 com revisão factual por IA |",
         "| Notas válidas contabilizadas | 1599 / 1.000.000 (0,1599%) | 49 com aprovação humana histórica + 1550 com revisão factual por IA |"),
        ("| Notas com revisão factual por IA registrada | 1450 |", "| Notas com revisão factual por IA registrada | 1550 |"),
        ("| Primeiro lote `software-testes-2000-0001` | 1459 / 2.000 (72,95%) | 9 aprovadas por humano + 1450 por IA; faltam 541 notas substantivas |",
         "| Primeiro lote `software-testes-2000-0001` | 1559 / 2.000 (77,95%) | 9 aprovadas por humano + 1550 por IA; faltam 441 notas substantivas |"),
        ("| Arquivos Markdown ativos em `knowledge-federation/domains/` | 1599 | 100 notas legadas com pendências + 1499 notas autorais substantivas |",
         "| Arquivos Markdown ativos em `knowledge-federation/domains/` | 1699 | 100 notas legadas com pendências + 1599 notas autorais substantivas |"),
        ("é `software-testes-2000-0001`: 1459 notas materiais já passaram pelo gate e revisão factual (9 humanas + 1450 IA)",
         "é `software-testes-2000-0001`: 1559 notas materiais já passaram pelo gate e revisão factual (9 humanas + 1550 IA)"),
        (", [19](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-19.md) e [20](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-20.md))",
         ", [19](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-19.md), [20](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-20.md) e [21](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-21.md))"),
        ("além da [reconciliação da tranche 20](knowledge-federation/exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-20.md)",
         f"além da [reconciliação da tranche 21](knowledge-federation/exports/reports/{RECON_NAME})"),
    ])

    # --- Knowledge-federation README ---
    apply(KF / "README.md", [
        ("- Arquivos Markdown ativos: **1599** (100 notas legadas com pendências + 1499 notas autorais substantivas).",
         "- Arquivos Markdown ativos: **1699** (100 notas legadas com pendências + 1599 notas autorais substantivas)."),
        ("- Notas válidas pelo protocolo atual: **1499** (49 aprovações humanas históricas + 1450 revisões factuais por IA).",
         "- Notas válidas pelo protocolo atual: **1599** (49 aprovações humanas históricas + 1550 revisões factuais por IA)."),
        ("- Progresso: **1499 / 1.000.000 (0,1499%)**; faltam 998.501 notas válidas.",
         "- Progresso: **1599 / 1.000.000 (0,1599%)**; faltam 998.401 notas válidas."),
        ("- Lote em andamento `software-testes-2000-0001`: **1459 / 2.000** notas válidas (72,95%); 9 humanas e 1450 por IA; faltam 541 notas materiais.",
         "- Lote em andamento `software-testes-2000-0001`: **1559 / 2.000** notas válidas (77,95%); 9 humanas e 1550 por IA; faltam 441 notas materiais."),
        (", [19](exports/reports/ai-review-software-testes-2000-0001-tranche-19.md) e [20](exports/reports/ai-review-software-testes-2000-0001-tranche-20.md); veja também a [reconciliação da tranche 20](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-20.md).",
         ", [19](exports/reports/ai-review-software-testes-2000-0001-tranche-19.md), [20](exports/reports/ai-review-software-testes-2000-0001-tranche-20.md) e [21](exports/reports/ai-review-software-testes-2000-0001-tranche-21.md); veja também a [reconciliação da tranche 21](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-21.md)."),
    ])

    # --- README-1M ---
    apply(KF / "README-1M.md", [
        ("tem 1499 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 1450 revisões factuais por IA registradas separadamente). O diretório ativo tem 1599 arquivos Markdown, incluindo 100 notas legadas com pendências, ainda excluídas da contagem. O lote `software-testes-2000-0001` tem 1459/2.000 notas válidas e segue em andamento; as notas 1359–1459 estão no [relatório factual por IA da tranche 20](exports/reports/ai-review-software-testes-2000-0001-tranche-20.md) e na [reconciliação da tranche 20](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-20.md); as notas 1258–1358 ficam no [relatório da tranche 19](exports/reports/ai-review-software-testes-2000-0001-tranche-19.md);",
         "tem 1599 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 1550 revisões factuais por IA registradas separadamente). O diretório ativo tem 1699 arquivos Markdown, incluindo 100 notas legadas com pendências, ainda excluídas da contagem. O lote `software-testes-2000-0001` tem 1559/2.000 notas válidas e segue em andamento; as notas 1460–1559 estão no [relatório factual por IA da tranche 21](exports/reports/ai-review-software-testes-2000-0001-tranche-21.md) e na [reconciliação da tranche 21](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-21.md); as notas 1359–1459 ficam no [relatório da tranche 20](exports/reports/ai-review-software-testes-2000-0001-tranche-20.md);"),
    ])

    # --- STATUS ---
    apply(KF / "STATUS-CONSOLIDACAO-1M.md", [
        ("A auditoria encontrou 1599 arquivos Markdown ativos: 1499 notas substantivas passaram pelo gate e receberam revisão factual registrada (49 humanas históricas + 1450 por IA)",
         "A auditoria encontrou 1699 arquivos Markdown ativos: 1599 notas substantivas passaram pelo gate e receberam revisão factual registrada (49 humanas históricas + 1550 por IA)"),
        ("| Progresso válido global | 1499 / 1.000.000 (0,1499%) | 49 revisões humanas históricas + 1450 revisões por IA registradas separadamente |",
         "| Progresso válido global | 1599 / 1.000.000 (0,1599%) | 49 revisões humanas históricas + 1550 revisões por IA registradas separadamente |"),
        ("| Revisões factuais por IA registradas | 1450 | Relatórios das tranches 2–20",
         "| Revisões factuais por IA registradas | 1550 | Relatórios das tranches 2–21"),
        ("| Primeiro lote | 1459 / 2.000 (72,95%) | 9 humanas + 1450 IA; faltam 541 notas substantivas |",
         "| Primeiro lote | 1559 / 2.000 (77,95%) | 9 humanas + 1550 IA; faltam 441 notas substantivas |"),
        ("| Candidatas que passaram pelo gate automatizado | 1499 |", "| Candidatas que passaram pelo gate automatizado | 1599 |"),
        ("Revisadas factualmente por IA as notas 10–1459 do lote (1450 no total)",
         "Revisadas factualmente por IA as notas 10–1559 do lote (1550 no total)"),
        (", [19](exports/reports/ai-review-software-testes-2000-0001-tranche-19.md) e [20](exports/reports/ai-review-software-testes-2000-0001-tranche-20.md).",
         ", [19](exports/reports/ai-review-software-testes-2000-0001-tranche-19.md), [20](exports/reports/ai-review-software-testes-2000-0001-tranche-20.md) e [21](exports/reports/ai-review-software-testes-2000-0001-tranche-21.md)."),
        ("4. Resultado parcial do primeiro lote: 1459/1459 aprovadas pelo gate; nove revisões humanas e 1450 revisões por IA no total após a tranche 20, incluindo as 101 novas revisões das notas 1359–1459.",
         "4. Resultado parcial do primeiro lote: 1559/1559 aprovadas pelo gate; nove revisões humanas e 1550 revisões por IA no total após a tranche 21, incluindo as 100 novas revisões das notas 1460–1559."),
        ("Relatórios atualizados: [reconciliação da tranche 20](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-20.md)",
         f"Relatórios atualizados: [reconciliação da tranche 21](exports/reports/{RECON_NAME})"),
        ("faltam 541 notas para o tamanho configurado de 2.000",
         "faltam 441 notas para o tamanho configurado de 2.000"),
    ])

    # --- PLANO ---
    apply(KF / "PLANO-CONTINUO-1M.md", [
        ("- Notas válidas globais: **1499** (49 aprovações humanas históricas + 1450 revisões factuais por IA).",
         "- Notas válidas globais: **1599** (49 aprovações humanas históricas + 1550 revisões factuais por IA)."),
        ("- Progresso: **1499 / 1.000.000 (0,1499%)**; faltam **998.501** notas válidas.",
         "- Progresso: **1599 / 1.000.000 (0,1599%)**; faltam **998.401** notas válidas."),
        ("- Lote atual `software-testes-2000-0001`: **1459 / 2.000 (72,95%)** notas válidas (9 humanas + 1450 IA); faltam **541** notas substantivas.",
         "- Lote atual `software-testes-2000-0001`: **1559 / 2.000 (77,95%)** notas válidas (9 humanas + 1550 IA); faltam **441** notas substantivas."),
        ("- Arquivos Markdown ativos: **1599**; 100 com pendências de qualidade, excluídos da contagem.",
         "- Arquivos Markdown ativos: **1699**; 100 com pendências de qualidade, excluídos da contagem."),
        ("| 4 | Conferir factual e registrar notas 10–1459 do primeiro lote | **Concluído até a tranche 20** | 1450 revisões por IA em relatórios das tranches 2–20, além das 9 aprovações humanas. |",
         "| 4 | Conferir factual e registrar notas 10–1559 do primeiro lote | **Concluído até a tranche 21** | 1550 revisões por IA em relatórios das tranches 2–21, além das 9 aprovações humanas. |"),
        ("| 5 | Rodar gate, testes, auditorias e diff | **Concluído para o estado atual** | Lote: 1459/1459 no gate, 9 humanas, 1450 IA. Global: 1599 arquivos, 1499 válidas, 100 com pendências legadas; veja a [reconciliação da tranche 20](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-20.md). |",
         f"| 5 | Rodar gate, testes, auditorias e diff | **Concluído para o estado atual** | Lote: 1559/1559 no gate, 9 humanas, 1550 IA. Global: 1699 arquivos, 1599 válidas, 100 com pendências legadas; veja a [reconciliação da tranche 21](exports/reports/{RECON_NAME}). |"),
        ("| 7 | Completar o lote `software-testes-2000-0001` até 2.000 notas | **Em andamento** | 1459/2.000; faltam 541 notas;",
         "| 7 | Completar o lote `software-testes-2000-0001` até 2.000 notas | **Em andamento** | 1559/2.000; faltam 441 notas;"),
        ("Progresso atual: 1499 notas válidas, 0/500 lotes completos.",
         "Progresso atual: 1599 notas válidas, 0/500 lotes completos."),
    ])

    # --- RECOVERY ---
    apply(KF / "RECOVERY-AND-SCALE-NOTE.md", [
        ("há 1599 arquivos: 100 legados com pendências e 1499 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 1450 revisões por IA). O lote `software-testes-2000-0001` tem 1459/2.000 notas válidas (9 humanas + 1450 IA), com status `in_progress` e 541 notas qualificadas restantes. As notas 1359–1459 passaram pelo gate e têm revisão factual por IA registrada na [tranche 20](exports/reports/ai-review-software-testes-2000-0001-tranche-20.md), com [reconciliação](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-20.md);",
         "há 1699 arquivos: 100 legados com pendências e 1599 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 1550 revisões por IA). O lote `software-testes-2000-0001` tem 1559/2.000 notas válidas (9 humanas + 1550 IA), com status `in_progress` e 441 notas qualificadas restantes. As notas 1460–1559 passaram pelo gate e têm revisão factual por IA registrada na [tranche 21](exports/reports/ai-review-software-testes-2000-0001-tranche-21.md), com [reconciliação](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-21.md);"),
        ("1. Continuar o lote atual em tranches de conteúdo real; faltam 541 notas qualificadas para completar as 2.000 configuradas.",
         "1. Continuar o lote atual em tranches de conteúdo real; faltam 441 notas qualificadas para completar as 2.000 configuradas."),
    ])

    # --- Home ---
    apply(KF / "00-home-vault" / "Home.md", [
        ("[[MOC-Testes-Software-0007]] — 1459 notas do lote de escala (meta: 2.000); nove têm aprovação humana histórica e 1450 revisões factuais por IA.",
         "[[MOC-Testes-Software-0007]] — 1559 notas do lote de escala (meta: 2.000); nove têm aprovação humana histórica e 1550 revisões factuais por IA."),
        ("[[human-review-queue|Registro de revisões factuais]] — 49 aprovações humanas e 1450 aprovações por IA, identificadas separadamente.",
         "[[human-review-queue|Registro de revisões factuais]] — 49 aprovações humanas e 1550 aprovações por IA, identificadas separadamente."),
        ("[[note-quality-audit|Auditoria de qualidade]] — 1499 notas válidas pelo protocolo atual (49 humanas + 1450 IA) e 100 notas legadas com falhas.",
         "[[note-quality-audit|Auditoria de qualidade]] — 1599 notas válidas pelo protocolo atual (49 humanas + 1550 IA) e 100 notas legadas com falhas."),
    ])

    # --- Indice-Global ---
    apply(KF / "00-home-vault" / "Indice-Global.md", [
        ("- Arquivos Markdown em `domains/`: **1599** (100 sementes legadas + 1499 notas autorais substantivas).",
         "- Arquivos Markdown em `domains/`: **1699** (100 sementes legadas + 1599 notas autorais substantivas)."),
        ("- Candidatas aprovadas no gate automatizado: **1499**; revisões humanas registradas: **49**; revisões factuais por IA: **1450**; 100 sementes legadas mantêm pendências.",
         "- Candidatas aprovadas no gate automatizado: **1599**; revisões humanas registradas: **49**; revisões factuais por IA: **1550**; 100 sementes legadas mantêm pendências."),
        ("- Os lotes atuais totalizam 1499 notas válidas pelo protocolo; o lote `software-testes-2000-0001` tem 1459/2.000, incluindo as notas 1359–1459 revisadas por IA na [tranche 20](../exports/reports/ai-review-software-testes-2000-0001-tranche-20.md) e na [reconciliação da tranche 20](../exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-20.md), as notas 1258–1358 na [tranche 19](../exports/reports/ai-review-software-testes-2000-0001-tranche-19.md),",
         "- Os lotes atuais totalizam 1599 notas válidas pelo protocolo; o lote `software-testes-2000-0001` tem 1559/2.000, incluindo as notas 1460–1559 revisadas por IA na [tranche 21](../exports/reports/ai-review-software-testes-2000-0001-tranche-21.md) e na [reconciliação da tranche 21](../exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-21.md), as notas 1359–1459 na [tranche 20](../exports/reports/ai-review-software-testes-2000-0001-tranche-20.md),"),
    ])

    print("reconciliação concluída")


if __name__ == "__main__":
    main()
