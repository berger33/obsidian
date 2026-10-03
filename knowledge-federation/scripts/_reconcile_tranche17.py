#!/usr/bin/env python3
"""Reconcile tranche 17 across manifest, MOC, review registry and status docs.

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
REPORT_NAME = "ai-review-software-testes-2000-0001-tranche-17.md"
RECON_NAME = "batch-reconciliation-software-testes-2000-0001-tranche-17.md"
DATE = "2026-10-03"


def load_builder():
    spec = importlib.util.spec_from_file_location("b17", SCRIPTS / "_build_tranche17.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_groups(b17):
    groups = []
    for path in sorted(b17.DATA_DIR.glob("*.txt")):
        context, rows = b17.parse_group(path)
        groups.append((context, rows))
    return groups


def manifest_section(groups) -> str:
    lines = ["## Tranche 17 — automação de navegador e dispositivos, simulação HTTP e contratos (101 notas; revisão factual por IA registrada)", ""]
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
    lines = ["## Tranche 17 — automação de navegador e dispositivos, simulação HTTP e contratos", ""]
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
            position = 1096 + (number - 1056)
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
    b17 = load_builder()
    groups = load_groups(b17)
    total = sum(len(rows) for _, rows in groups)
    if total != 101 or int(groups[0][0]["first"]) != 1056 or int(groups[-1][0]["first"]) != 1146:
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
        marker="| 1096 | `software-testes-2000-0001` | [Gatling: organizar a simulação como código]",
    )

    # --- Manifest ---
    apply(manifest, [
        ("- Notas efetivamente redigidas até agora: **1055 / 2.000 (52,75%)**",
         "- Notas efetivamente redigidas até agora: **1156 / 2.000 (57,80%)**"),
        ("- Gate automatizado: **1055/1055 aprovadas**", "- Gate automatizado: **1156/1156 aprovadas**"),
        ("reexecutado após a tranche 16)", "reexecutado após a tranche 17)"),
        ("- Revisão factual humana: **9/1055**", "- Revisão factual humana: **9/1156**"),
        ("- Revisão factual por IA: **1046/1055**", "- Revisão factual por IA: **1147/1156**"),
        ("Contabilizadas como válidas: **1055/1055**", "Contabilizadas como válidas: **1156/1156**"),
        ("- Revisor das 1046 notas aprovadas por IA", "- Revisor das 1147 notas aprovadas por IA"),
        ("tranches 2–16 (1046 notas, IDs 10–1055) foram conferidas factualmente por IA",
         "tranches 2–17 (1147 notas, IDs 10–1156) foram conferidas factualmente por IA"),
        ("[`tranche 16`](../reports/ai-review-software-testes-2000-0001-tranche-16.md)",
         "[`tranche 16`](../reports/ai-review-software-testes-2000-0001-tranche-16.md), [`tranche 17`](../reports/ai-review-software-testes-2000-0001-tranche-17.md)"),
        ("[`batch-reconciliation-software-testes-2000-0001-tranche-16.md`](../reports/batch-reconciliation-software-testes-2000-0001-tranche-16.md)",
         "[`batch-reconciliation-software-testes-2000-0001-tranche-17.md`](../reports/batch-reconciliation-software-testes-2000-0001-tranche-17.md)"),
        ("Existem 1055 notas materiais listadas abaixo; não há IDs reservados, placeholders ou registros virtuais para as 945 restantes.",
         "Existem 1156 notas materiais listadas abaixo; não há IDs reservados, placeholders ou registros virtuais para as 844 restantes."),
        ("as 1046 notas 10–1055 das tranches 2–16 têm revisão factual por IA",
         "as 1147 notas 10–1156 das tranches 2–17 têm revisão factual por IA"),
        ("são 1055/2.000 notas válidas, restando 945 notas materiais",
         "são 1156/2.000 notas válidas, restando 844 notas materiais"),
    ])

    # --- MOC ---
    apply(moc, [
        ("Índice das 1055 notas substantivas redigidas até agora no lote `software-testes-2000-0001`, cuja meta é 2.000. As 1055 passaram pelo gate automatizado e têm revisão factual registrada: nove aprovadas pelo usuário e 1046 aprovadas por IA",
         "Índice das 1156 notas substantivas redigidas até agora no lote `software-testes-2000-0001`, cuja meta é 2.000. As 1156 passaram pelo gate automatizado e têm revisão factual registrada: nove aprovadas pelo usuário e 1147 aprovadas por IA"),
        ("O gate automatizado foi aprovado por 1055/1055 notas e as 1055 contam como válidas pelo protocolo atualizado: nove têm aprovação humana histórica e 1046 têm revisão factual por IA registrada separadamente. O lote de 2.000 continua `in_progress` (1055 notas substantivas; 945 ainda não produzidas).",
         "O gate automatizado foi aprovado por 1156/1156 notas e as 1156 contam como válidas pelo protocolo atualizado: nove têm aprovação humana histórica e 1147 têm revisão factual por IA registrada separadamente. O lote de 2.000 continua `in_progress` (1156 notas substantivas; 844 ainda não produzidas)."),
        ("[15](../../exports/reports/ai-review-software-testes-2000-0001-tranche-15.md) e [16](../../exports/reports/ai-review-software-testes-2000-0001-tranche-16.md).",
         "[15](../../exports/reports/ai-review-software-testes-2000-0001-tranche-15.md), [16](../../exports/reports/ai-review-software-testes-2000-0001-tranche-16.md) e [17](../../exports/reports/ai-review-software-testes-2000-0001-tranche-17.md)."),
        ("reconciliação mais recente do manifesto/fila](../../exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-16.md)",
         "reconciliação mais recente do manifesto/fila](../../exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-17.md)"),
    ])

    # --- Review queue ---
    apply(queue, [
        ("distingue 1046 revisões factuais realizadas por IA no lote `software-testes-2000-0001`",
         "distingue 1147 revisões factuais realizadas por IA no lote `software-testes-2000-0001`"),
        ("- Aprovações por IA registradas separadamente: **1046**.",
         "- Aprovações por IA registradas separadamente: **1147**."),
        ("- Notas válidas contabilizadas (gate + revisão humana ou IA): **1095**.",
         "- Notas válidas contabilizadas (gate + revisão humana ou IA): **1196**."),
        ("As 1046 linhas `APROVADA POR IA` (nº 50–1095) correspondem às notas 10–1055 e às revisões documentadas nos relatórios das tranches 2–16",
         "As 1147 linhas `APROVADA POR IA` (nº 50–1196) correspondem às notas 10–1156 e às revisões documentadas nos relatórios das tranches 2–17"),
    ])

    # --- Root README ---
    apply(ROOT / "README.md", [
        ("| Notas válidas contabilizadas | 1095 / 1.000.000 (0,1095%) | 49 com aprovação humana histórica + 1046 com revisão factual por IA |",
         "| Notas válidas contabilizadas | 1196 / 1.000.000 (0,1196%) | 49 com aprovação humana histórica + 1147 com revisão factual por IA |"),
        ("| Notas com revisão factual por IA registrada | 1046 |", "| Notas com revisão factual por IA registrada | 1147 |"),
        ("| Primeiro lote `software-testes-2000-0001` | 1055 / 2.000 (52,75%) | 9 aprovadas por humano + 1046 por IA; faltam 945 notas substantivas |",
         "| Primeiro lote `software-testes-2000-0001` | 1156 / 2.000 (57,80%) | 9 aprovadas por humano + 1147 por IA; faltam 844 notas substantivas |"),
        ("| Arquivos Markdown ativos em `knowledge-federation/domains/` | 1195 | 100 notas legadas com pendências + 1095 notas autorais substantivas |",
         "| Arquivos Markdown ativos em `knowledge-federation/domains/` | 1296 | 100 notas legadas com pendências + 1196 notas autorais substantivas |"),
        ("é `software-testes-2000-0001`: 1055 notas materiais já passaram pelo gate e revisão factual (9 humanas + 1046 IA)",
         "é `software-testes-2000-0001`: 1156 notas materiais já passaram pelo gate e revisão factual (9 humanas + 1147 IA)"),
        ("[15](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md) e [16](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-16.md))",
         "[15](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md), [16](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-16.md) e [17](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-17.md))"),
        ("além da [reconciliação da tranche 16](knowledge-federation/exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-16.md)",
         "além da [reconciliação da tranche 17](knowledge-federation/exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-17.md)"),
    ])

    # --- Knowledge-federation README ---
    apply(KF / "README.md", [
        ("- Arquivos Markdown ativos: **1195** (100 notas legadas com pendências + 1095 notas autorais substantivas).",
         "- Arquivos Markdown ativos: **1296** (100 notas legadas com pendências + 1196 notas autorais substantivas)."),
        ("- Notas válidas pelo protocolo atual: **1095** (49 aprovações humanas históricas + 1046 revisões factuais por IA).",
         "- Notas válidas pelo protocolo atual: **1196** (49 aprovações humanas históricas + 1147 revisões factuais por IA)."),
        ("- Progresso: **1095 / 1.000.000 (0,1095%)**; faltam 998.905 notas válidas.",
         "- Progresso: **1196 / 1.000.000 (0,1196%)**; faltam 998.804 notas válidas."),
        ("- Lote em andamento `software-testes-2000-0001`: **1055 / 2.000** notas válidas (52,75%); 9 humanas e 1046 por IA; faltam 945 notas materiais.",
         "- Lote em andamento `software-testes-2000-0001`: **1156 / 2.000** notas válidas (57,80%); 9 humanas e 1147 por IA; faltam 844 notas materiais."),
        ("[13](exports/reports/ai-review-software-testes-2000-0001-tranche-13.md), [14](exports/reports/ai-review-software-testes-2000-0001-tranche-14.md), [15](exports/reports/ai-review-software-testes-2000-0001-tranche-15.md) e [16](exports/reports/ai-review-software-testes-2000-0001-tranche-16.md); veja também a [reconciliação da tranche 16](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-16.md).",
         "[13](exports/reports/ai-review-software-testes-2000-0001-tranche-13.md), [14](exports/reports/ai-review-software-testes-2000-0001-tranche-14.md), [15](exports/reports/ai-review-software-testes-2000-0001-tranche-15.md), [16](exports/reports/ai-review-software-testes-2000-0001-tranche-16.md) e [17](exports/reports/ai-review-software-testes-2000-0001-tranche-17.md); veja também a [reconciliação da tranche 17](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-17.md)."),
    ])

    # --- README-1M ---
    apply(KF / "README-1M.md", [
        ("tem 1095 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 1046 revisões factuais por IA registradas separadamente). O diretório ativo tem 1195 arquivos Markdown, incluindo 100 notas legadas com pendências, ainda excluídas da contagem. O lote `software-testes-2000-0001` tem 1055/2.000 notas válidas e segue em andamento; as notas 950–1055 estão no [relatório factual por IA da tranche 16](exports/reports/ai-review-software-testes-2000-0001-tranche-16.md) e na [reconciliação da tranche 16](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-16.md);",
         "tem 1196 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 1147 revisões factuais por IA registradas separadamente). O diretório ativo tem 1296 arquivos Markdown, incluindo 100 notas legadas com pendências, ainda excluídas da contagem. O lote `software-testes-2000-0001` tem 1156/2.000 notas válidas e segue em andamento; as notas 1056–1156 estão no [relatório factual por IA da tranche 17](exports/reports/ai-review-software-testes-2000-0001-tranche-17.md) e na [reconciliação da tranche 17](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-17.md); as notas 950–1055 ficam no [relatório da tranche 16](exports/reports/ai-review-software-testes-2000-0001-tranche-16.md);"),
    ])

    # --- STATUS ---
    apply(KF / "STATUS-CONSOLIDACAO-1M.md", [
        ("A auditoria encontrou 1195 arquivos Markdown ativos: 1095 notas substantivas passaram pelo gate e receberam revisão factual registrada (49 humanas históricas + 1046 por IA)",
         "A auditoria encontrou 1296 arquivos Markdown ativos: 1196 notas substantivas passaram pelo gate e receberam revisão factual registrada (49 humanas históricas + 1147 por IA)"),
        ("| Progresso válido global | 1095 / 1.000.000 (0,1095%) | 49 revisões humanas históricas + 1046 revisões por IA registradas separadamente |",
         "| Progresso válido global | 1196 / 1.000.000 (0,1196%) | 49 revisões humanas históricas + 1147 revisões por IA registradas separadamente |"),
        ("| Revisões factuais por IA registradas | 1046 | Relatórios das tranches 2–16",
         "| Revisões factuais por IA registradas | 1147 | Relatórios das tranches 2–17"),
        ("| Primeiro lote | 1055 / 2.000 (52,75%) | 9 humanas + 1046 IA; faltam 945 notas substantivas |",
         "| Primeiro lote | 1156 / 2.000 (57,80%) | 9 humanas + 1147 IA; faltam 844 notas substantivas |"),
        ("| Candidatas que passaram pelo gate automatizado | 1095 |", "| Candidatas que passaram pelo gate automatizado | 1196 |"),
        ("Revisadas factualmente por IA as notas 10–1055 do lote (1046 no total)",
         "Revisadas factualmente por IA as notas 10–1156 do lote (1147 no total)"),
        ("[15](exports/reports/ai-review-software-testes-2000-0001-tranche-15.md) e [16](exports/reports/ai-review-software-testes-2000-0001-tranche-16.md).",
         "[15](exports/reports/ai-review-software-testes-2000-0001-tranche-15.md), [16](exports/reports/ai-review-software-testes-2000-0001-tranche-16.md) e [17](exports/reports/ai-review-software-testes-2000-0001-tranche-17.md)."),
        ("4. Resultado parcial do primeiro lote: 1055/1055 aprovadas pelo gate; nove revisões humanas e 1046 revisões por IA no total após a tranche 16, incluindo as 106 novas revisões das notas 950–1055.",
         "4. Resultado parcial do primeiro lote: 1156/1156 aprovadas pelo gate; nove revisões humanas e 1147 revisões por IA no total após a tranche 17, incluindo as 101 novas revisões das notas 1056–1156."),
        ("Relatórios atualizados: [reconciliação da tranche 16](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-16.md)",
         "Relatórios atualizados: [reconciliação da tranche 17](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-17.md)"),
        ("faltam 945 notas para o tamanho configurado de 2.000", "faltam 844 notas para o tamanho configurado de 2.000"),
    ])

    # --- PLANO ---
    apply(KF / "PLANO-CONTINUO-1M.md", [
        ("- Notas válidas globais: **1095** (49 aprovações humanas históricas + 1046 revisões factuais por IA).",
         "- Notas válidas globais: **1196** (49 aprovações humanas históricas + 1147 revisões factuais por IA)."),
        ("- Progresso: **1095 / 1.000.000 (0,1095%)**; faltam **998.905** notas válidas.",
         "- Progresso: **1196 / 1.000.000 (0,1196%)**; faltam **998.804** notas válidas."),
        ("- Lote atual `software-testes-2000-0001`: **1055 / 2.000 (52,75%)** notas válidas (9 humanas + 1046 IA); faltam **945** notas substantivas.",
         "- Lote atual `software-testes-2000-0001`: **1156 / 2.000 (57,80%)** notas válidas (9 humanas + 1147 IA); faltam **844** notas substantivas."),
        ("- Arquivos Markdown ativos: **1195**; 100 com pendências de qualidade, excluídos da contagem.",
         "- Arquivos Markdown ativos: **1296**; 100 com pendências de qualidade, excluídos da contagem."),
        ("| 4 | Conferir factual e registrar notas 10–1055 do primeiro lote | **Concluído até a tranche 16** | 1046 revisões por IA em relatórios das tranches 2–16, além das 9 aprovações humanas. |",
         "| 4 | Conferir factual e registrar notas 10–1156 do primeiro lote | **Concluído até a tranche 17** | 1147 revisões por IA em relatórios das tranches 2–17, além das 9 aprovações humanas. |"),
        ("| 5 | Rodar gate, testes, auditorias e diff | **Concluído para o estado atual** | Lote: 1055/1055 no gate, 9 humanas, 1046 IA. Global: 1195 arquivos, 1095 válidas, 100 com pendências legadas; veja a [reconciliação da tranche 16](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-16.md). |",
         "| 5 | Rodar gate, testes, auditorias e diff | **Concluído para o estado atual** | Lote: 1156/1156 no gate, 9 humanas, 1147 IA. Global: 1296 arquivos, 1196 válidas, 100 com pendências legadas; veja a [reconciliação da tranche 17](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-17.md). |"),
        ("| 7 | Completar o lote `software-testes-2000-0001` até 2.000 notas | **Em andamento** | 1055/2.000; faltam 945 notas;",
         "| 7 | Completar o lote `software-testes-2000-0001` até 2.000 notas | **Em andamento** | 1156/2.000; faltam 844 notas;"),
        ("Progresso atual: 1095 notas válidas, 0/500 lotes completos.",
         "Progresso atual: 1196 notas válidas, 0/500 lotes completos."),
    ])

    # --- RECOVERY ---
    apply(KF / "RECOVERY-AND-SCALE-NOTE.md", [
        ("há 1195 arquivos: 100 legados com pendências e 1095 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 1046 revisões por IA). O lote `software-testes-2000-0001` tem 1055/2.000 notas válidas (9 humanas + 1046 IA), com status `in_progress` e 945 notas qualificadas restantes. As notas 950–1055 passaram pelo gate e têm revisão factual por IA registrada na [tranche 16](exports/reports/ai-review-software-testes-2000-0001-tranche-16.md), com [reconciliação](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-16.md);",
         "há 1296 arquivos: 100 legados com pendências e 1196 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 1147 revisões por IA). O lote `software-testes-2000-0001` tem 1156/2.000 notas válidas (9 humanas + 1147 IA), com status `in_progress` e 844 notas qualificadas restantes. As notas 1056–1156 passaram pelo gate e têm revisão factual por IA registrada na [tranche 17](exports/reports/ai-review-software-testes-2000-0001-tranche-17.md), com [reconciliação](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-17.md);"),
        ("1. Continuar o lote atual em tranches de conteúdo real; faltam 945 notas qualificadas para completar as 2.000 configuradas.",
         "1. Continuar o lote atual em tranches de conteúdo real; faltam 844 notas qualificadas para completar as 2.000 configuradas."),
    ])

    # --- Home ---
    apply(KF / "00-home-vault" / "Home.md", [
        ("[[MOC-Testes-Software-0007]] — 1055 notas do lote de escala (meta: 2.000); nove têm aprovação humana histórica e 1046 revisões factuais por IA.",
         "[[MOC-Testes-Software-0007]] — 1156 notas do lote de escala (meta: 2.000); nove têm aprovação humana histórica e 1147 revisões factuais por IA."),
        ("[[human-review-queue|Registro de revisões factuais]] — 49 aprovações humanas e 1046 aprovações por IA, identificadas separadamente.",
         "[[human-review-queue|Registro de revisões factuais]] — 49 aprovações humanas e 1147 aprovações por IA, identificadas separadamente."),
        ("[[note-quality-audit|Auditoria de qualidade]] — 1095 notas válidas pelo protocolo atual (49 humanas + 1046 IA) e 100 notas legadas com falhas.",
         "[[note-quality-audit|Auditoria de qualidade]] — 1196 notas válidas pelo protocolo atual (49 humanas + 1147 IA) e 100 notas legadas com falhas."),
    ])

    # --- Indice-Global ---
    apply(KF / "00-home-vault" / "Indice-Global.md", [
        ("- Arquivos Markdown em `domains/`: **1195** (100 sementes legadas + 1095 notas autorais substantivas).",
         "- Arquivos Markdown em `domains/`: **1296** (100 sementes legadas + 1196 notas autorais substantivas)."),
        ("- Candidatas aprovadas no gate automatizado: **1095**; revisões humanas registradas: **49**; revisões factuais por IA: **1046**; 100 sementes legadas mantêm pendências.",
         "- Candidatas aprovadas no gate automatizado: **1196**; revisões humanas registradas: **49**; revisões factuais por IA: **1147**; 100 sementes legadas mantêm pendências."),
        ("- Os lotes atuais totalizam 1095 notas válidas pelo protocolo; o lote `software-testes-2000-0001` tem 1055/2.000, incluindo as notas 950–1055 revisadas por IA na [tranche 16](../exports/reports/ai-review-software-testes-2000-0001-tranche-16.md) e na [reconciliação da tranche 16](../exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-16.md),",
         "- Os lotes atuais totalizam 1196 notas válidas pelo protocolo; o lote `software-testes-2000-0001` tem 1156/2.000, incluindo as notas 1056–1156 revisadas por IA na [tranche 17](../exports/reports/ai-review-software-testes-2000-0001-tranche-17.md) e na [reconciliação da tranche 17](../exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-17.md), as notas 950–1055 na [tranche 16](../exports/reports/ai-review-software-testes-2000-0001-tranche-16.md),"),
    ])

    print("reconciliação concluída")


if __name__ == "__main__":
    main()
