#!/usr/bin/env python3
"""Reconcile tranche 16 across manifest, MOC, review registry and status docs.

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
REPORT_NAME = "ai-review-software-testes-2000-0001-tranche-16.md"
RECON_NAME = "batch-reconciliation-software-testes-2000-0001-tranche-16.md"
DATE = "2026-10-03"


def load_builder():
    spec = importlib.util.spec_from_file_location("b16", SCRIPTS / "_build_tranche16.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_groups(b16):
    groups = []
    for path in sorted(b16.DATA_DIR.glob("*.txt")):
        context, rows = b16.parse_group(path)
        groups.append((context, rows))
    return groups


def manifest_section(groups) -> str:
    lines = ["## Tranche 16 — desempenho, cobertura, acessibilidade e contratos (106 notas; revisão factual por IA registrada)", ""]
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
    lines = ["## Tranche 16 — desempenho, cobertura, acessibilidade e contratos", ""]
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
            position = 990 + (number - 950)
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
        count = text.count(old)
        if count == 0:
            if new in text:
                continue
            raise SystemExit(f"{path.relative_to(ROOT)}: padrão não encontrado: {old[:140]}")
        if new in text:
            # Already applied (covers pairs whose old text is a prefix of the new text).
            continue
        if count != 1:
            raise SystemExit(f"{path.relative_to(ROOT)}: padrão encontrado {count} vezes: {old[:140]}")
        text = text.replace(old, new)
    if text == original:
        print(f"já reconciliado {path.relative_to(ROOT)}")
        return
    path.write_text(text, encoding="utf-8")
    print(f"ok {path.relative_to(ROOT)}")


def replace_all(path: Path, old: str, new: str, expected: int) -> None:
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count == 0:
        if new in text:
            print(f"já aplicado {path.relative_to(ROOT)}")
            return
        raise SystemExit(f"{path.relative_to(ROOT)}: padrão não encontrado: {old[:140]}")
    if count != expected:
        raise SystemExit(f"{path.relative_to(ROOT)}: esperadas {expected} ocorrências, encontradas {count}: {old[:140]}")
    path.write_text(text.replace(old, new), encoding="utf-8")
    print(f"ok {count}x {path.relative_to(ROOT)}")


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
    b16 = load_builder()
    groups = load_groups(b16)
    total = sum(len(rows) for _, rows in groups)
    if total != 106 or int(groups[0][0]["first"]) != 950 or int(groups[-1][0]["first"]) != 1045:
        raise SystemExit(f"dados inesperados: {total} notas, primeiro grupo em {groups[0][0]['first']}")

    manifest = KF / "exports" / "batches" / f"{BATCH_ID}.md"
    moc = KF / "00-home-vault" / "MOCs" / "MOC-Testes-Software-0007.md"
    queue = KF / "exports" / "reports" / "human-review-queue.md"

    insert_before(manifest, "## Critérios e próximo passo", manifest_section(groups))
    insert_before(moc, "## Estado editorial", moc_section(groups))
    insert_before(
        queue,
        "## Regra de contagem",
        review_rows(groups),
        marker="| 990 | `software-testes-2000-0001` | [Detox: confiar na sincronização com operações pendentes]",
    )

    # --- Manifest ---
    apply(manifest, [
        ("- Notas efetivamente redigidas até agora: **949 / 2.000 (47,45%)**",
         "- Notas efetivamente redigidas até agora: **1055 / 2.000 (52,75%)**"),
        ("- Gate automatizado: **949/949 aprovadas**",
         "- Gate automatizado: **1055/1055 aprovadas**"),
        ("- Revisão factual humana: **9/949**", "- Revisão factual humana: **9/1055**"),
        ("- Revisão factual por IA: **940/949**", "- Revisão factual por IA: **1046/1055**"),
        ("- Contabilizadas como válidas: **949/949**", "- Contabilizadas como válidas: **1055/1055**"),
        ("- Revisor das 940 notas aprovadas por IA", "- Revisor das 1046 notas aprovadas por IA"),
        ("tranches 2–15 (940 notas, IDs 10–949) foram conferidas factualmente por IA",
         "tranches 2–16 (1046 notas, IDs 10–1055) foram conferidas factualmente por IA"),
        ("[`tranche 13`](../reports/ai-review-software-testes-2000-0001-tranche-13.md), [`tranche 14`](../reports/ai-review-software-testes-2000-0001-tranche-14.md), [`tranche 15`](../reports/ai-review-software-testes-2000-0001-tranche-15.md)",
         "[`tranche 13`](../reports/ai-review-software-testes-2000-0001-tranche-13.md), [`tranche 14`](../reports/ai-review-software-testes-2000-0001-tranche-14.md), [`tranche 15`](../reports/ai-review-software-testes-2000-0001-tranche-15.md), [`tranche 16`](../reports/ai-review-software-testes-2000-0001-tranche-16.md)"),
        ("[`batch-reconciliation-software-testes-2000-0001-tranche-15.md`](../reports/batch-reconciliation-software-testes-2000-0001-tranche-15.md)",
         "[`batch-reconciliation-software-testes-2000-0001-tranche-16.md`](../reports/batch-reconciliation-software-testes-2000-0001-tranche-16.md)"),
        ("wikilinks; reexecutado após a tranche 15)", "wikilinks; reexecutado após a tranche 16)"),
        ("Existem 949 notas materiais listadas abaixo; não há IDs reservados, placeholders ou registros virtuais para as 1.051 restantes.",
         "Existem 1055 notas materiais listadas abaixo; não há IDs reservados, placeholders ou registros virtuais para as 945 restantes."),
        ("As nove notas da tranche 1 preservam aprovação humana; as 940 notas 10–949 das tranches 2–15",
         "As nove notas da tranche 1 preservam aprovação humana; as 1046 notas 10–1055 das tranches 2–16"),
        ("O lote continua incompleto: são 949/2.000 notas válidas, restando 1.051 notas materiais.",
         "O lote continua incompleto: são 1055/2.000 notas válidas, restando 945 notas materiais."),
    ])

    # --- MOC ---
    apply(moc, [
        ("Índice das 949 notas substantivas redigidas até agora no lote `software-testes-2000-0001`, cuja meta é 2.000. As 949 passaram pelo gate automatizado e têm revisão factual registrada: nove aprovadas pelo usuário e 940 aprovadas por IA",
         "Índice das 1055 notas substantivas redigidas até agora no lote `software-testes-2000-0001`, cuja meta é 2.000. As 1055 passaram pelo gate automatizado e têm revisão factual registrada: nove aprovadas pelo usuário e 1046 aprovadas por IA"),
        ("O gate automatizado foi aprovado por 949/949 notas e as 949 contam como válidas pelo protocolo atualizado: nove têm aprovação humana histórica e 940 têm revisão factual por IA registrada separadamente. O lote de 2.000 continua `in_progress` (949 notas substantivas; 1.051 ainda não produzidas).",
         "O gate automatizado foi aprovado por 1055/1055 notas e as 1055 contam como válidas pelo protocolo atualizado: nove têm aprovação humana histórica e 1046 têm revisão factual por IA registrada separadamente. O lote de 2.000 continua `in_progress` (1055 notas substantivas; 945 ainda não produzidas)."),
        ("[13](../../exports/reports/ai-review-software-testes-2000-0001-tranche-13.md), [14](../../exports/reports/ai-review-software-testes-2000-0001-tranche-14.md) e [15](../../exports/reports/ai-review-software-testes-2000-0001-tranche-15.md). Consulte também o [registro de revisão humana e IA](../../exports/reports/human-review-queue.md).",
         "[13](../../exports/reports/ai-review-software-testes-2000-0001-tranche-13.md), [14](../../exports/reports/ai-review-software-testes-2000-0001-tranche-14.md), [15](../../exports/reports/ai-review-software-testes-2000-0001-tranche-15.md) e [16](../../exports/reports/ai-review-software-testes-2000-0001-tranche-16.md). Consulte também o [registro de revisão humana e IA](../../exports/reports/human-review-queue.md)."),
        ("[reconciliação mais recente do manifesto/fila](../../exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-15.md)",
         "[reconciliação mais recente do manifesto/fila](../../exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-16.md)"),
    ])

    # --- Review queue ---
    apply(queue, [
        ("distingue 940 revisões factuais realizadas por IA no lote `software-testes-2000-0001`",
         "distingue 1046 revisões factuais realizadas por IA no lote `software-testes-2000-0001`"),
        ("- Aprovações por IA registradas separadamente: **940**.",
         "- Aprovações por IA registradas separadamente: **1046**."),
        ("- Notas válidas contabilizadas (gate + revisão humana ou IA): **989**.",
         "- Notas válidas contabilizadas (gate + revisão humana ou IA): **1095**."),
        ("As 940 linhas `APROVADA POR IA` (nº 50–989) correspondem às notas 10–949 e às revisões documentadas nos relatórios das tranches 2–15",
         "As 1046 linhas `APROVADA POR IA` (nº 50–1095) correspondem às notas 10–1055 e às revisões documentadas nos relatórios das tranches 2–16"),
    ])

    # --- Root README ---
    apply(ROOT / "README.md", [
        ("| Notas válidas contabilizadas | 989 / 1.000.000 (0,0989%) | 49 com aprovação humana histórica + 940 com revisão factual por IA |",
         "| Notas válidas contabilizadas | 1095 / 1.000.000 (0,1095%) | 49 com aprovação humana histórica + 1046 com revisão factual por IA |"),
        ("| Notas com revisão factual por IA registrada | 940 |",
         "| Notas com revisão factual por IA registrada | 1046 |"),
        ("| Primeiro lote `software-testes-2000-0001` | 949 / 2.000 (47,45%) | 9 aprovadas por humano + 940 por IA; faltam 1.051 notas substantivas |",
         "| Primeiro lote `software-testes-2000-0001` | 1055 / 2.000 (52,75%) | 9 aprovadas por humano + 1046 por IA; faltam 945 notas substantivas |"),
        ("| Arquivos Markdown ativos em `knowledge-federation/domains/` | 1089 | 100 notas legadas com pendências + 989 notas autorais substantivas |",
         "| Arquivos Markdown ativos em `knowledge-federation/domains/` | 1195 | 100 notas legadas com pendências + 1095 notas autorais substantivas |"),
        ("O lote em andamento é `software-testes-2000-0001`: 949 notas materiais já passaram pelo gate e revisão factual (9 humanas + 940 IA), com meta de 2.000.",
         "O lote em andamento é `software-testes-2000-0001`: 1055 notas materiais já passaram pelo gate e revisão factual (9 humanas + 1046 IA), com meta de 2.000."),
        ("[14](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-14.md) e [15](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md))",
         "[14](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-14.md), [15](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md) e [16](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-16.md))"),
        ("além da [reconciliação da tranche 15](knowledge-federation/exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-15.md)",
         "além da [reconciliação da tranche 16](knowledge-federation/exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-16.md)"),
    ])

    # --- Knowledge-federation README ---
    apply(KF / "README.md", [
        ("- Arquivos Markdown ativos: **1089** (100 notas legadas com pendências + 989 notas autorais substantivas).",
         "- Arquivos Markdown ativos: **1195** (100 notas legadas com pendências + 1095 notas autorais substantivas)."),
        ("- Notas válidas pelo protocolo atual: **989** (49 aprovações humanas históricas + 940 revisões factuais por IA).",
         "- Notas válidas pelo protocolo atual: **1095** (49 aprovações humanas históricas + 1046 revisões factuais por IA)."),
        ("- Progresso: **989 / 1.000.000 (0,0989%)**; faltam 999.011 notas válidas.",
         "- Progresso: **1095 / 1.000.000 (0,1095%)**; faltam 998.905 notas válidas."),
        ("- Lote em andamento `software-testes-2000-0001`: **949 / 2.000** notas válidas (47,45%); 9 humanas e 940 por IA; faltam 1.051 notas materiais.",
         "- Lote em andamento `software-testes-2000-0001`: **1055 / 2.000** notas válidas (52,75%); 9 humanas e 1046 por IA; faltam 945 notas materiais."),
        ("[13](exports/reports/ai-review-software-testes-2000-0001-tranche-13.md), [14](exports/reports/ai-review-software-testes-2000-0001-tranche-14.md) e [15](exports/reports/ai-review-software-testes-2000-0001-tranche-15.md); veja também a [reconciliação da tranche 15](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-15.md).",
         "[13](exports/reports/ai-review-software-testes-2000-0001-tranche-13.md), [14](exports/reports/ai-review-software-testes-2000-0001-tranche-14.md), [15](exports/reports/ai-review-software-testes-2000-0001-tranche-15.md) e [16](exports/reports/ai-review-software-testes-2000-0001-tranche-16.md); veja também a [reconciliação da tranche 16](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-16.md)."),
    ])

    # --- README-1M ---
    apply(KF / "README-1M.md", [
        ("Na atualização de 2026-10-02, o repositório tem 989 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 940 revisões factuais por IA registradas separadamente). O diretório ativo tem 1089 arquivos Markdown, incluindo 100 notas legadas com pendências, ainda excluídas da contagem. O lote `software-testes-2000-0001` tem 949/2.000 notas válidas e segue em andamento; as notas 850–949 estão no [relatório factual por IA da tranche 15](exports/reports/ai-review-software-testes-2000-0001-tranche-15.md) e na [reconciliação da tranche 15](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-15.md); as notas 750–849 ficam no [relatório da tranche 14](exports/reports/ai-review-software-testes-2000-0001-tranche-14.md);",
         "Na atualização de 2026-10-03, o repositório tem 1095 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 1046 revisões factuais por IA registradas separadamente). O diretório ativo tem 1195 arquivos Markdown, incluindo 100 notas legadas com pendências, ainda excluídas da contagem. O lote `software-testes-2000-0001` tem 1055/2.000 notas válidas e segue em andamento; as notas 950–1055 estão no [relatório factual por IA da tranche 16](exports/reports/ai-review-software-testes-2000-0001-tranche-16.md) e na [reconciliação da tranche 16](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-16.md); as notas 850–949 ficam no [relatório da tranche 15](exports/reports/ai-review-software-testes-2000-0001-tranche-15.md);"),
    ])

    # --- STATUS ---
    apply(KF / "STATUS-CONSOLIDACAO-1M.md", [
        ("A auditoria encontrou 1089 arquivos Markdown ativos: 989 notas substantivas passaram pelo gate e receberam revisão factual registrada (49 humanas históricas + 940 por IA); outras 100 mantêm pendências e continuam fora da contagem.",
         "A auditoria encontrou 1195 arquivos Markdown ativos: 1095 notas substantivas passaram pelo gate e receberam revisão factual registrada (49 humanas históricas + 1046 por IA); outras 100 mantêm pendências e continuam fora da contagem."),
        ("| Progresso válido global | 989 / 1.000.000 (0,0989%) | 49 revisões humanas históricas + 940 revisões por IA registradas separadamente |",
         "| Progresso válido global | 1095 / 1.000.000 (0,1095%) | 49 revisões humanas históricas + 1046 revisões por IA registradas separadamente |"),
        ("| Revisões factuais por IA registradas | 940 | Relatórios das tranches 2–15",
         "| Revisões factuais por IA registradas | 1046 | Relatórios das tranches 2–16"),
        ("| Primeiro lote | 949 / 2.000 (47,45%) | 9 humanas + 940 IA; faltam 1.051 notas substantivas |",
         "| Primeiro lote | 1055 / 2.000 (52,75%) | 9 humanas + 1046 IA; faltam 945 notas substantivas |"),
        ("| Candidatas que passaram pelo gate automatizado | 989 |",
         "| Candidatas que passaram pelo gate automatizado | 1095 |"),
        ("Revisadas factualmente por IA as notas 10–949 do lote (940 no total)",
         "Revisadas factualmente por IA as notas 10–1055 do lote (1046 no total)"),
        ("[13](exports/reports/ai-review-software-testes-2000-0001-tranche-13.md), [14](exports/reports/ai-review-software-testes-2000-0001-tranche-14.md) e [15](exports/reports/ai-review-software-testes-2000-0001-tranche-15.md).",
         "[13](exports/reports/ai-review-software-testes-2000-0001-tranche-13.md), [14](exports/reports/ai-review-software-testes-2000-0001-tranche-14.md), [15](exports/reports/ai-review-software-testes-2000-0001-tranche-15.md) e [16](exports/reports/ai-review-software-testes-2000-0001-tranche-16.md)."),
        ("4. Resultado parcial do primeiro lote: 949/949 aprovadas pelo gate; nove revisões humanas e 940 revisões por IA no total após a tranche 15, incluindo as 100 novas revisões das notas 850–949.",
         "4. Resultado parcial do primeiro lote: 1055/1055 aprovadas pelo gate; nove revisões humanas e 1046 revisões por IA no total após a tranche 16, incluindo as 106 novas revisões das notas 950–1055."),
        ("Relatórios atualizados: [reconciliação da tranche 15](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-15.md)",
         "Relatórios atualizados: [reconciliação da tranche 16](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-16.md)"),
        ("faltam 1.051 notas para o tamanho configurado de 2.000",
         "faltam 945 notas para o tamanho configurado de 2.000"),
    ])

    # --- PLANO ---
    apply(KF / "PLANO-CONTINUO-1M.md", [
        ("- Notas válidas globais: **989** (49 aprovações humanas históricas + 940 revisões factuais por IA).",
         "- Notas válidas globais: **1095** (49 aprovações humanas históricas + 1046 revisões factuais por IA)."),
        ("- Progresso: **989 / 1.000.000 (0,0989%)**; faltam **999.011** notas válidas.",
         "- Progresso: **1095 / 1.000.000 (0,1095%)**; faltam **998.905** notas válidas."),
        ("- Lote atual `software-testes-2000-0001`: **949 / 2.000 (47,45%)** notas válidas (9 humanas + 940 IA); faltam **1.051** notas substantivas.",
         "- Lote atual `software-testes-2000-0001`: **1055 / 2.000 (52,75%)** notas válidas (9 humanas + 1046 IA); faltam **945** notas substantivas."),
        ("- Arquivos Markdown ativos: **1089**; 100 com pendências de qualidade, excluídos da contagem.",
         "- Arquivos Markdown ativos: **1195**; 100 com pendências de qualidade, excluídos da contagem."),
        ("| 4 | Conferir factual e registrar notas 10–949 do primeiro lote | **Concluído até a tranche 15** | 940 revisões por IA em relatórios das tranches 2–15, além das 9 aprovações humanas. |",
         "| 4 | Conferir factual e registrar notas 10–1055 do primeiro lote | **Concluído até a tranche 16** | 1046 revisões por IA em relatórios das tranches 2–16, além das 9 aprovações humanas. |"),
        ("| 5 | Rodar gate, testes, auditorias e diff | **Concluído para o estado atual** | Lote: 949/949 no gate, 9 humanas, 940 IA. Global: 1089 arquivos, 989 válidas, 100 com pendências legadas; veja a [reconciliação da tranche 15](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-15.md). |",
         "| 5 | Rodar gate, testes, auditorias e diff | **Concluído para o estado atual** | Lote: 1055/1055 no gate, 9 humanas, 1046 IA. Global: 1195 arquivos, 1095 válidas, 100 com pendências legadas; veja a [reconciliação da tranche 16](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-16.md). |"),
        ("| 7 | Completar o lote `software-testes-2000-0001` até 2.000 notas | **Em andamento** | 949/2.000; faltam 1.051 notas;",
         "| 7 | Completar o lote `software-testes-2000-0001` até 2.000 notas | **Em andamento** | 1055/2.000; faltam 945 notas;"),
        ("Progresso atual: 989 notas válidas, 0/500 lotes completos.",
         "Progresso atual: 1095 notas válidas, 0/500 lotes completos."),
    ])

    # --- RECOVERY ---
    apply(KF / "RECOVERY-AND-SCALE-NOTE.md", [
        ("No diretório ativo `knowledge-federation/domains/` há 1089 arquivos: 100 legados com pendências e 989 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 940 revisões por IA). O lote `software-testes-2000-0001` tem 949/2.000 notas válidas (9 humanas + 940 IA), com status `in_progress` e 1.051 notas qualificadas restantes. As notas 850–949 passaram pelo gate e têm revisão factual por IA registrada na [tranche 15](exports/reports/ai-review-software-testes-2000-0001-tranche-15.md), com [reconciliação](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-15.md);",
         "No diretório ativo `knowledge-federation/domains/` há 1195 arquivos: 100 legados com pendências e 1095 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 1046 revisões por IA). O lote `software-testes-2000-0001` tem 1055/2.000 notas válidas (9 humanas + 1046 IA), com status `in_progress` e 945 notas qualificadas restantes. As notas 950–1055 passaram pelo gate e têm revisão factual por IA registrada na [tranche 16](exports/reports/ai-review-software-testes-2000-0001-tranche-16.md), com [reconciliação](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-16.md);"),
        ("1. Continuar o lote atual em tranches de conteúdo real; faltam 1.051 notas qualificadas para completar as 2.000 configuradas.",
         "1. Continuar o lote atual em tranches de conteúdo real; faltam 945 notas qualificadas para completar as 2.000 configuradas."),
    ])

    # --- Home ---
    apply(KF / "00-home-vault" / "Home.md", [
        ("[[MOC-Testes-Software-0007]] — 949 notas do lote de escala (meta: 2.000); nove têm aprovação humana histórica e 940 revisões factuais por IA.",
         "[[MOC-Testes-Software-0007]] — 1055 notas do lote de escala (meta: 2.000); nove têm aprovação humana histórica e 1046 revisões factuais por IA."),
        ("[[human-review-queue|Registro de revisões factuais]] — 49 aprovações humanas e 940 aprovações por IA, identificadas separadamente.",
         "[[human-review-queue|Registro de revisões factuais]] — 49 aprovações humanas e 1046 aprovações por IA, identificadas separadamente."),
        ("[[note-quality-audit|Auditoria de qualidade]] — 989 notas válidas pelo protocolo atual (49 humanas + 940 IA) e 100 notas legadas com falhas.",
         "[[note-quality-audit|Auditoria de qualidade]] — 1095 notas válidas pelo protocolo atual (49 humanas + 1046 IA) e 100 notas legadas com falhas."),
    ])

    # --- Indice-Global ---
    apply(KF / "00-home-vault" / "Indice-Global.md", [
        ("- Arquivos Markdown em `domains/`: **1089** (100 sementes legadas + 989 notas autorais substantivas).",
         "- Arquivos Markdown em `domains/`: **1195** (100 sementes legadas + 1095 notas autorais substantivas)."),
        ("- Candidatas aprovadas no gate automatizado: **989**; revisões humanas registradas: **49**; revisões factuais por IA: **940**; 100 sementes legadas mantêm pendências.",
         "- Candidatas aprovadas no gate automatizado: **1095**; revisões humanas registradas: **49**; revisões factuais por IA: **1046**; 100 sementes legadas mantêm pendências."),
        ("- Os lotes atuais totalizam 989 notas válidas pelo protocolo; o lote `software-testes-2000-0001` tem 949/2.000, incluindo as notas 850–949 revisadas por IA na [tranche 15](../exports/reports/ai-review-software-testes-2000-0001-tranche-15.md) e na [reconciliação da tranche 15](../exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-15.md), as notas 750–849 na [tranche 14](../exports/reports/ai-review-software-testes-2000-0001-tranche-14.md),",
         "- Os lotes atuais totalizam 1095 notas válidas pelo protocolo; o lote `software-testes-2000-0001` tem 1055/2.000, incluindo as notas 950–1055 revisadas por IA na [tranche 16](../exports/reports/ai-review-software-testes-2000-0001-tranche-16.md) e na [reconciliação da tranche 16](../exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-16.md), as notas 850–949 na [tranche 15](../exports/reports/ai-review-software-testes-2000-0001-tranche-15.md), as notas 750–849 na [tranche 14](../exports/reports/ai-review-software-testes-2000-0001-tranche-14.md),"),
    ])

    # --- datas do estado atual (a tranche 16 foi produzida em 2026-10-03) ---
    apply(KF / "STATUS-CONSOLIDACAO-1M.md", [
        ("Data do status: 2026-10-02.", "Data do status: 2026-10-03."),
        ("## Progresso auditado em 2026-10-02", "## Progresso auditado em 2026-10-03"),
    ])
    apply(KF / "PLANO-CONTINUO-1M.md", [
        ("Atualizado em 2026-10-02. O nome `PLANO-CONTINUO-1M.md`", "Atualizado em 2026-10-03. O nome `PLANO-CONTINUO-1M.md`"),
    ])
    apply(KF / "RECOVERY-AND-SCALE-NOTE.md", [
        ("Atualizado em 2026-10-02. A meta ativa é", "Atualizado em 2026-10-03. A meta ativa é"),
    ])
    apply(KF / "README-1M.md", [
        ("Na atualização de 2026-10-02, o repositório tem 1095 notas", "Na atualização de 2026-10-03, o repositório tem 1095 notas"),
    ])
    apply(KF / "00-home-vault" / "Home.md", [
        ("ultima_verificacao: 2026-10-02", "ultima_verificacao: 2026-10-03"),
    ])
    apply(KF / "00-home-vault" / "Indice-Global.md", [
        ("ultima_verificacao: 2026-10-02", "ultima_verificacao: 2026-10-03"),
        ("Atualizado em: 2026-10-02", "Atualizado em: 2026-10-03"),
    ])
    apply(manifest, [
        ("- Última atualização: 2026-10-02", "- Última atualização: 2026-10-03"),
    ])
    apply(queue, [
        ("Atualizado em 2026-10-02. O registro preserva 49 aprovações", "Atualizado em 2026-10-03. O registro preserva 49 aprovações"),
    ])
    replace_all(queue, "registrada em 2026-10-02 no relatório `ai-review-software-testes-2000-0001-tranche-16.md`",
                "registrada em 2026-10-03 no relatório `ai-review-software-testes-2000-0001-tranche-16.md`", 106)

    print("reconciliação concluída")


if __name__ == "__main__":
    main()
