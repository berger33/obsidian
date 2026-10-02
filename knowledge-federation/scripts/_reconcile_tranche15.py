#!/usr/bin/env python3
"""Reconcile tranche 15 across manifest, MOC, review registry and status docs.

Every replacement is asserted: a missing pattern aborts the script instead of
silently leaving a stale count in the editorial documents.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
KF = ROOT / "knowledge-federation"
SCRIPTS = KF / "scripts"
BATCH_ID = "software-testes-2000-0001"
REPORT_NAME = "ai-review-software-testes-2000-0001-tranche-15.md"
RECON_NAME = "batch-reconciliation-software-testes-2000-0001-tranche-15.md"
DATE = "2026-10-02"


def load_builder():
    spec = importlib.util.spec_from_file_location("b15", SCRIPTS / "_build_tranche15.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_groups(b15):
    groups = []
    for path in sorted(b15.DATA_DIR.glob("*.txt")):
        context, rows = b15.parse_group(path)
        groups.append((context, rows))
    return groups


def manifest_section(groups) -> str:
    lines = [f"## Tranche 15 — frameworks, mocks, cobertura e automação móvel (100 notas; revisão factual por IA registrada)", ""]
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
    lines = ["## Tranche 15 — frameworks, mocks, cobertura e automação móvel", ""]
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
            position = 890 + (number - 850)
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
            raise SystemExit(f"{path.relative_to(ROOT)}: padrão não encontrado: {old[:120]}")
        text = text.replace(old, new)
    if text == original:
        raise SystemExit(f"{path.relative_to(ROOT)}: nenhuma mudança aplicada")
    path.write_text(text, encoding="utf-8")
    print(f"ok {path.relative_to(ROOT)}")


def insert_before(path: Path, anchor: str, block: str) -> None:
    text = path.read_text(encoding="utf-8")
    marker = block.splitlines()[0]
    if marker in text:
        print(f"já presente {path.relative_to(ROOT)}")
        return
    if text.count(anchor) != 1:
        raise SystemExit(f"{path.relative_to(ROOT)}: âncora encontrada {text.count(anchor)} vezes: {anchor}")
    text = text.replace(anchor, block + anchor, 1)
    path.write_text(text, encoding="utf-8")
    print(f"ok inserção {path.relative_to(ROOT)}")


def main() -> None:
    b15 = load_builder()
    groups = load_groups(b15)
    total = sum(len(rows) for _, rows in groups)
    if total != 100 or int(groups[0][0]["first"]) != 850 or int(groups[-1][0]["first"]) != 940:
        raise SystemExit(f"dados inesperados: {total} notas, primeiro grupo em {groups[0][0]['first']}")

    manifest = KF / "exports" / "batches" / f"{BATCH_ID}.md"
    moc = KF / "00-home-vault" / "MOCs" / "MOC-Testes-Software-0007.md"
    queue = KF / "exports" / "reports" / "human-review-queue.md"

    insert_before(manifest, "## Critérios e próximo passo", manifest_section(groups))
    insert_before(moc, "## Estado editorial", moc_section(groups))
    insert_before(queue, "## Regra de contagem", review_rows(groups))

    # --- Manifest ---
    apply(manifest, [
        ("- Notas efetivamente redigidas até agora: **849 / 2.000 (42,45%)**",
         "- Notas efetivamente redigidas até agora: **949 / 2.000 (47,45%)**"),
        ("- Gate automatizado: **849/849 aprovadas**",
         "- Gate automatizado: **949/949 aprovadas**"),
        ("- Revisão factual humana: **9/849**", "- Revisão factual humana: **9/949**"),
        ("- Revisão factual por IA: **840/849**", "- Revisão factual por IA: **940/949**"),
        ("- Contabilizadas como válidas: **849/849**", "- Contabilizadas como válidas: **949/949**"),
        ("- Revisor das 840 notas aprovadas por IA", "- Revisor das 940 notas aprovadas por IA"),
        ("tranches 2–14 (840 notas, IDs 10–849) foram conferidas factualmente por IA",
         "tranches 2–15 (940 notas, IDs 10–949) foram conferidas factualmente por IA"),
        ("[`tranche 13`](../reports/ai-review-software-testes-2000-0001-tranche-13.md), [`tranche 14`](../reports/ai-review-software-testes-2000-0001-tranche-14.md)",
         "[`tranche 13`](../reports/ai-review-software-testes-2000-0001-tranche-13.md), [`tranche 14`](../reports/ai-review-software-testes-2000-0001-tranche-14.md), [`tranche 15`](../reports/ai-review-software-testes-2000-0001-tranche-15.md)"),
        ("[`batch-reconciliation-software-testes-2000-0001-tranche-14.md`](../reports/batch-reconciliation-software-testes-2000-0001-tranche-14.md)",
         "[`batch-reconciliation-software-testes-2000-0001-tranche-15.md`](../reports/batch-reconciliation-software-testes-2000-0001-tranche-15.md)"),
        ("Existem 849 notas materiais listadas abaixo; não há IDs reservados, placeholders ou registros virtuais para as 1.151 restantes.",
         "Existem 949 notas materiais listadas abaixo; não há IDs reservados, placeholders ou registros virtuais para as 1.051 restantes."),
        ("As nove notas da tranche 1 preservam aprovação humana; as 840 notas 10–849 das tranches 2–14",
         "As nove notas da tranche 1 preservam aprovação humana; as 940 notas 10–949 das tranches 2–15"),
        ("O lote continua incompleto: são 849/2.000 notas válidas, restando 1.151 notas materiais.",
         "O lote continua incompleto: são 949/2.000 notas válidas, restando 1.051 notas materiais."),
    ])

    # --- MOC ---
    apply(moc, [
        ("Índice das 849 notas substantivas redigidas até agora no lote `software-testes-2000-0001`, cuja meta é 2.000. As 849 passaram pelo gate automatizado e têm revisão factual registrada: nove aprovadas pelo usuário e 840 aprovadas por IA",
         "Índice das 949 notas substantivas redigidas até agora no lote `software-testes-2000-0001`, cuja meta é 2.000. As 949 passaram pelo gate automatizado e têm revisão factual registrada: nove aprovadas pelo usuário e 940 aprovadas por IA"),
        ("O gate automatizado foi aprovado por 849/849 notas e as 849 contam como válidas pelo protocolo atualizado: nove têm aprovação humana histórica e 840 têm revisão factual por IA registrada separadamente. O lote de 2.000 continua `in_progress` (849 notas substantivas; 1.151 ainda não produzidas).",
         "O gate automatizado foi aprovado por 949/949 notas e as 949 contam como válidas pelo protocolo atualizado: nove têm aprovação humana histórica e 940 têm revisão factual por IA registrada separadamente. O lote de 2.000 continua `in_progress` (949 notas substantivas; 1.051 ainda não produzidas)."),
        ("[13](../../exports/reports/ai-review-software-testes-2000-0001-tranche-13.md) e [14](../../exports/reports/ai-review-software-testes-2000-0001-tranche-14.md). Consulte também o [registro de revisão humana e IA](../../exports/reports/human-review-queue.md).",
         "[13](../../exports/reports/ai-review-software-testes-2000-0001-tranche-13.md), [14](../../exports/reports/ai-review-software-testes-2000-0001-tranche-14.md) e [15](../../exports/reports/ai-review-software-testes-2000-0001-tranche-15.md). Consulte também o [registro de revisão humana e IA](../../exports/reports/human-review-queue.md)."),
        ("[reconciliação mais recente do manifesto/fila](../../exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-14.md)",
         "[reconciliação mais recente do manifesto/fila](../../exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-15.md)"),
    ])

    # --- Review queue ---
    apply(queue, [
        ("distingue 840 revisões factuais realizadas por IA no lote `software-testes-2000-0001`",
         "distingue 940 revisões factuais realizadas por IA no lote `software-testes-2000-0001`"),
        ("- Aprovações por IA registradas separadamente: **840**.",
         "- Aprovações por IA registradas separadamente: **940**."),
        ("- Notas válidas contabilizadas (gate + revisão humana ou IA): **889**.",
         "- Notas válidas contabilizadas (gate + revisão humana ou IA): **989**."),
        ("As 840 linhas `APROVADA POR IA` (nº 50–889) correspondem às notas 10–849 e às revisões documentadas nos relatórios das tranches 2–14",
         "As 940 linhas `APROVADA POR IA` (nº 50–989) correspondem às notas 10–949 e às revisões documentadas nos relatórios das tranches 2–15"),
    ])

    # --- Root README ---
    apply(ROOT / "README.md", [
        ("| Notas válidas contabilizadas | 889 / 1.000.000 (0,0889%) | 49 com aprovação humana histórica + 840 com revisão factual por IA |",
         "| Notas válidas contabilizadas | 989 / 1.000.000 (0,0989%) | 49 com aprovação humana histórica + 940 com revisão factual por IA |"),
        ("| Notas com revisão factual por IA registrada | 840 |", "| Notas com revisão factual por IA registrada | 940 |"),
        ("| Primeiro lote `software-testes-2000-0001` | 849 / 2.000 (42,45%) | 9 aprovadas por humano + 840 por IA; faltam 1.151 notas substantivas |",
         "| Primeiro lote `software-testes-2000-0001` | 949 / 2.000 (47,45%) | 9 aprovadas por humano + 940 por IA; faltam 1.051 notas substantivas |"),
        ("| Arquivos Markdown ativos em `knowledge-federation/domains/` | 989 | 100 notas legadas com pendências + 889 notas autorais substantivas |",
         "| Arquivos Markdown ativos em `knowledge-federation/domains/` | 1089 | 100 notas legadas com pendências + 989 notas autorais substantivas |"),
        ("O lote em andamento é `software-testes-2000-0001`: 849 notas materiais já passaram pelo gate e revisão factual (9 humanas + 840 IA), com meta de 2.000.",
         "O lote em andamento é `software-testes-2000-0001`: 949 notas materiais já passaram pelo gate e revisão factual (9 humanas + 940 IA), com meta de 2.000."),
        ("[14](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-14.md))",
         "[14](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-14.md) e [15](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md))"),
        ("além da [reconciliação da tranche 14](knowledge-federation/exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-14.md)",
         "além da [reconciliação da tranche 15](knowledge-federation/exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-15.md)"),
    ])

    # --- Knowledge-federation README ---
    apply(KF / "README.md", [
        ("- Arquivos Markdown ativos: **989** (100 notas legadas com pendências + 889 notas autorais substantivas).",
         "- Arquivos Markdown ativos: **1089** (100 notas legadas com pendências + 989 notas autorais substantivas)."),
        ("- Notas válidas pelo protocolo atual: **889** (49 aprovações humanas históricas + 840 revisões factuais por IA).",
         "- Notas válidas pelo protocolo atual: **989** (49 aprovações humanas históricas + 940 revisões factuais por IA)."),
        ("- Progresso: **889 / 1.000.000 (0,0889%)**; faltam 999.111 notas válidas.",
         "- Progresso: **989 / 1.000.000 (0,0989%)**; faltam 999.011 notas válidas."),
        ("- Lote em andamento `software-testes-2000-0001`: **849 / 2.000** notas válidas (42,45%); 9 humanas e 840 por IA; faltam 1.151 notas materiais.",
         "- Lote em andamento `software-testes-2000-0001`: **949 / 2.000** notas válidas (47,45%); 9 humanas e 940 por IA; faltam 1.051 notas materiais."),
        ("[13](exports/reports/ai-review-software-testes-2000-0001-tranche-13.md) e [14](exports/reports/ai-review-software-testes-2000-0001-tranche-14.md); veja também a [reconciliação da tranche 14](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-14.md).",
         "[13](exports/reports/ai-review-software-testes-2000-0001-tranche-13.md), [14](exports/reports/ai-review-software-testes-2000-0001-tranche-14.md) e [15](exports/reports/ai-review-software-testes-2000-0001-tranche-15.md); veja também a [reconciliação da tranche 15](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-15.md)."),
    ])

    # --- README-1M ---
    apply(KF / "README-1M.md", [
        ("Na atualização de 2026-10-02, o repositório tem 889 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 840 revisões factuais por IA registradas separadamente). O diretório ativo tem 989 arquivos Markdown, incluindo 100 notas legadas com pendências, ainda excluídas da contagem. O lote `software-testes-2000-0001` tem 849/2.000 notas válidas e segue em andamento; as notas 750–849 estão no [relatório factual por IA da tranche 14](exports/reports/ai-review-software-testes-2000-0001-tranche-14.md) e na [reconciliação da tranche 14](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-14.md);",
         "Na atualização de 2026-10-02, o repositório tem 989 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 940 revisões factuais por IA registradas separadamente). O diretório ativo tem 1089 arquivos Markdown, incluindo 100 notas legadas com pendências, ainda excluídas da contagem. O lote `software-testes-2000-0001` tem 949/2.000 notas válidas e segue em andamento; as notas 850–949 estão no [relatório factual por IA da tranche 15](exports/reports/ai-review-software-testes-2000-0001-tranche-15.md) e na [reconciliação da tranche 15](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-15.md); as notas 750–849 ficam no [relatório da tranche 14](exports/reports/ai-review-software-testes-2000-0001-tranche-14.md);"),
    ])

    # --- STATUS ---
    apply(KF / "STATUS-CONSOLIDACAO-1M.md", [
        ("A auditoria encontrou 989 arquivos Markdown ativos: 889 notas substantivas passaram pelo gate e receberam revisão factual registrada (49 humanas históricas + 840 por IA); outras 100 mantêm pendências e continuam fora da contagem.",
         "A auditoria encontrou 1089 arquivos Markdown ativos: 989 notas substantivas passaram pelo gate e receberam revisão factual registrada (49 humanas históricas + 940 por IA); outras 100 mantêm pendências e continuam fora da contagem."),
        ("| Progresso válido global | 889 / 1.000.000 (0,0889%) | 49 revisões humanas históricas + 840 revisões por IA registradas separadamente |",
         "| Progresso válido global | 989 / 1.000.000 (0,0989%) | 49 revisões humanas históricas + 940 revisões por IA registradas separadamente |"),
        ("| Revisões factuais por IA registradas | 840 | Relatórios das tranches 2–14",
         "| Revisões factuais por IA registradas | 940 | Relatórios das tranches 2–15"),
        ("| Primeiro lote | 849 / 2.000 (42,45%) | 9 humanas + 840 IA; faltam 1.151 notas substantivas |",
         "| Primeiro lote | 949 / 2.000 (47,45%) | 9 humanas + 940 IA; faltam 1.051 notas substantivas |"),
        ("| Candidatas que passaram pelo gate automatizado | 889 |", "| Candidatas que passaram pelo gate automatizado | 989 |"),
        ("Revisadas factualmente por IA as notas 10–849 do lote (840 no total)",
         "Revisadas factualmente por IA as notas 10–949 do lote (940 no total)"),
        ("e [13](exports/reports/ai-review-software-testes-2000-0001-tranche-13.md) e [14](exports/reports/ai-review-software-testes-2000-0001-tranche-14.md).",
         "[13](exports/reports/ai-review-software-testes-2000-0001-tranche-13.md), [14](exports/reports/ai-review-software-testes-2000-0001-tranche-14.md) e [15](exports/reports/ai-review-software-testes-2000-0001-tranche-15.md)."),
        ("4. Resultado parcial do primeiro lote: 849/849 aprovadas pelo gate; nove revisões humanas e 840 revisões por IA no total após a tranche 14, incluindo as 100 novas revisões das notas 750–849.",
         "4. Resultado parcial do primeiro lote: 949/949 aprovadas pelo gate; nove revisões humanas e 940 revisões por IA no total após a tranche 15, incluindo as 100 novas revisões das notas 850–949."),
        ("Relatórios atualizados: [reconciliação da tranche 14](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-14.md)",
         "Relatórios atualizados: [reconciliação da tranche 15](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-15.md)"),
        ("faltam 1.151 notas para o tamanho configurado de 2.000", "faltam 1.051 notas para o tamanho configurado de 2.000"),
    ])

    # --- PLANO ---
    apply(KF / "PLANO-CONTINUO-1M.md", [
        ("- Notas válidas globais: **889** (49 aprovações humanas históricas + 840 revisões factuais por IA).",
         "- Notas válidas globais: **989** (49 aprovações humanas históricas + 940 revisões factuais por IA)."),
        ("- Progresso: **889 / 1.000.000 (0,0889%)**; faltam **999.111** notas válidas.",
         "- Progresso: **989 / 1.000.000 (0,0989%)**; faltam **999.011** notas válidas."),
        ("- Lote atual `software-testes-2000-0001`: **849 / 2.000 (42,45%)** notas válidas (9 humanas + 840 IA); faltam **1.151** notas substantivas.",
         "- Lote atual `software-testes-2000-0001`: **949 / 2.000 (47,45%)** notas válidas (9 humanas + 940 IA); faltam **1.051** notas substantivas."),
        ("- Arquivos Markdown ativos: **989**; 100 com pendências de qualidade, excluídos da contagem.",
         "- Arquivos Markdown ativos: **1089**; 100 com pendências de qualidade, excluídos da contagem."),
        ("| 4 | Conferir factual e registrar notas 10–849 do primeiro lote | **Concluído nesta tranche** | 840 revisões por IA em relatórios das tranches 2–14, além das 9 aprovações humanas. |",
         "| 4 | Conferir factual e registrar notas 10–949 do primeiro lote | **Concluído até a tranche 15** | 940 revisões por IA em relatórios das tranches 2–15, além das 9 aprovações humanas. |"),
        ("| 5 | Rodar gate, testes, auditorias e diff | **Concluído para o estado atual** | Lote: 849/849 no gate, 9 humanas, 840 IA. Global: 989 arquivos, 889 válidas, 100 com pendências legadas; veja a [reconciliação da tranche 14](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-14.md). |",
         "| 5 | Rodar gate, testes, auditorias e diff | **Concluído para o estado atual** | Lote: 949/949 no gate, 9 humanas, 940 IA. Global: 1089 arquivos, 989 válidas, 100 com pendências legadas; veja a [reconciliação da tranche 15](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-15.md). |"),
        ("| 7 | Completar o lote `software-testes-2000-0001` até 2.000 notas | **Em andamento** | 849/2.000; faltam 1.151 notas;",
         "| 7 | Completar o lote `software-testes-2000-0001` até 2.000 notas | **Em andamento** | 949/2.000; faltam 1.051 notas;"),
        ("Progresso atual: 889 notas válidas, 0/500 lotes completos.", "Progresso atual: 989 notas válidas, 0/500 lotes completos."),
    ])

    # --- RECOVERY ---
    apply(KF / "RECOVERY-AND-SCALE-NOTE.md", [
        ("No diretório ativo `knowledge-federation/domains/` há 989 arquivos: 100 legados com pendências e 889 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 840 revisões por IA). O lote `software-testes-2000-0001` tem 849/2.000 notas válidas (9 humanas + 840 IA), com status `in_progress` e 1.151 notas qualificadas restantes. As notas 750–849 passaram pelo gate e têm revisão factual por IA registrada na [tranche 14](exports/reports/ai-review-software-testes-2000-0001-tranche-14.md), com [reconciliação](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-14.md);",
         "No diretório ativo `knowledge-federation/domains/` há 1089 arquivos: 100 legados com pendências e 989 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 940 revisões por IA). O lote `software-testes-2000-0001` tem 949/2.000 notas válidas (9 humanas + 940 IA), com status `in_progress` e 1.051 notas qualificadas restantes. As notas 850–949 passaram pelo gate e têm revisão factual por IA registrada na [tranche 15](exports/reports/ai-review-software-testes-2000-0001-tranche-15.md), com [reconciliação](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-15.md);"),
        ("1. Continuar o lote atual em tranches de conteúdo real; faltam 1.151 notas qualificadas para completar as 2.000 configuradas.",
         "1. Continuar o lote atual em tranches de conteúdo real; faltam 1.051 notas qualificadas para completar as 2.000 configuradas."),
    ])

    # --- Home ---
    apply(KF / "00-home-vault" / "Home.md", [
        ("[[MOC-Testes-Software-0007]] — 849 notas do lote de escala (meta: 2.000); nove têm aprovação humana histórica e 840 revisões factuais por IA.",
         "[[MOC-Testes-Software-0007]] — 949 notas do lote de escala (meta: 2.000); nove têm aprovação humana histórica e 940 revisões factuais por IA."),
        ("[[human-review-queue|Registro de revisões factuais]] — 49 aprovações humanas e 840 aprovações por IA, identificadas separadamente.",
         "[[human-review-queue|Registro de revisões factuais]] — 49 aprovações humanas e 940 aprovações por IA, identificadas separadamente."),
        ("[[note-quality-audit|Auditoria de qualidade]] — 889 notas válidas pelo protocolo atual (49 humanas + 840 IA) e 100 notas legadas com falhas.",
         "[[note-quality-audit|Auditoria de qualidade]] — 989 notas válidas pelo protocolo atual (49 humanas + 940 IA) e 100 notas legadas com falhas."),
    ])

    # --- Indice-Global ---
    apply(KF / "00-home-vault" / "Indice-Global.md", [
        ("- Arquivos Markdown em `domains/`: **989** (100 sementes legadas + 889 notas autorais substantivas).",
         "- Arquivos Markdown em `domains/`: **1089** (100 sementes legadas + 989 notas autorais substantivas)."),
        ("- Candidatas aprovadas no gate automatizado: **889**; revisões humanas registradas: **49**; revisões factuais por IA: **840**; 100 sementes legadas mantêm pendências.",
         "- Candidatas aprovadas no gate automatizado: **989**; revisões humanas registradas: **49**; revisões factuais por IA: **940**; 100 sementes legadas mantêm pendências."),
        ("- Os lotes atuais totalizam 889 notas válidas pelo protocolo; o lote `software-testes-2000-0001` tem 849/2.000, incluindo as notas 750–849 revisadas por IA na [tranche 14](../exports/reports/ai-review-software-testes-2000-0001-tranche-14.md) e na [reconciliação da tranche 14](../exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-14.md),",
         "- Os lotes atuais totalizam 989 notas válidas pelo protocolo; o lote `software-testes-2000-0001` tem 949/2.000, incluindo as notas 850–949 revisadas por IA na [tranche 15](../exports/reports/ai-review-software-testes-2000-0001-tranche-15.md) e na [reconciliação da tranche 15](../exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-15.md), as notas 750–849 na [tranche 14](../exports/reports/ai-review-software-testes-2000-0001-tranche-14.md),"),
    ])

    print("reconciliação concluída")


if __name__ == "__main__":
    main()
