#!/usr/bin/env python3
"""Reconcile tranche 26 (final 41 notes, IDs 1960-2000) closing batch software-testes-2000-0001 at 2000/2000.

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
REPORT_NAME = "ai-review-software-testes-2000-0001-tranche-26.md"
RECON_NAME = "batch-reconciliation-software-testes-2000-0001-tranche-26.md"
DATE = "2026-10-03"


def load_builder():
    spec = importlib.util.spec_from_file_location("b26", SCRIPTS / "_build_tranche26.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_groups(b26):
    groups = []
    for path in sorted(b26.DATA_DIR.glob("*.txt")):
        context, rows = b26.parse_group(path)
        groups.append((context, rows))
    return groups


def manifest_section(groups) -> str:
    lines = ["## Tranche 26 — ESBMC, SymbiYosys, gocheck e Psalm (41 notas finais; revisão factual por IA registrada)", ""]
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
    lines = ["## Tranche 26 — ESBMC, SymbiYosys, gocheck e Psalm", ""]
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
            position = 2000 + (number - 1960)
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
    b26 = load_builder()
    groups = load_groups(b26)
    total = sum(len(rows) for _, rows in groups)
    if total != 41 or int(groups[0][0]["first"]) != 1960 or int(groups[-1][0]["first"]) != 1990:
        raise SystemExit(f"dados inesperados: {total} notas, primeiro grupo em {groups[0][0]['first']}")

    manifest = KF / "exports" / "batches" / f"{BATCH_ID}.md"
    moc = KF / "00-home-vault" / "MOCs" / "MOC-Testes-Software-0007.md"
    queue = KF / "exports" / "reports" / "human-review-queue.md"

    insert_before(manifest, "## Critérios e próximo passo", manifest_section(groups))
    insert_before(moc, "## Estado editorial", moc_section(groups))
    queue_block = review_rows(groups)
    insert_before(queue, "## Regra de contagem", queue_block)

    apply(manifest, [
        ('- Notas efetivamente redigidas até agora: **1959 / 2.000 (97,95%)**',
         '- Notas efetivamente redigidas até agora: **2000 / 2.000 (100%)**'),
        ('- Gate automatizado: **1959/1959 aprovadas**',
         '- Gate automatizado: **2000/2000 aprovadas**'),
        ('reexecutado após a tranche 25)',
         'reexecutado após a tranche 26)'),
        ('- Revisão factual humana: **9/1959**',
         '- Revisão factual humana: **9/2000**'),
        ('- Revisão factual por IA: **1950/1959**',
         '- Revisão factual por IA: **1991/2000**'),
        ('Contabilizadas como válidas: **1959/1959**',
         'Contabilizadas como válidas: **2000/2000**'),
        ('- Revisor das 1950 notas aprovadas por IA',
         '- Revisor das 1991 notas aprovadas por IA'),
        ('- Status do lote maior: `in_progress`; tranche 1 (9 notas) preserva aprovação humana; tranches 2–25 (1950 notas, IDs 10–1959) foram conferidas factualmente por IA e aprovadas sob o protocolo atualizado',
         '- Status do lote maior: `complete`; tranche 1 (9 notas) preserva aprovação humana; tranches 2–26 (1991 notas, IDs 10–2000) foram conferidas factualmente por IA e aprovadas sob o protocolo atualizado'),
        ('[`tranche 20`](../reports/ai-review-software-testes-2000-0001-tranche-20.md), [`tranche 21`](../reports/ai-review-software-testes-2000-0001-tranche-21.md), [`tranche 22`](../reports/ai-review-software-testes-2000-0001-tranche-22.md), [`tranche 23`](../reports/ai-review-software-testes-2000-0001-tranche-23.md), [`tranche 24`](../reports/ai-review-software-testes-2000-0001-tranche-24.md) e [`tranche 25`](../reports/ai-review-software-testes-2000-0001-tranche-25.md)',
         '[`tranche 20`](../reports/ai-review-software-testes-2000-0001-tranche-20.md), [`tranche 21`](../reports/ai-review-software-testes-2000-0001-tranche-21.md), [`tranche 22`](../reports/ai-review-software-testes-2000-0001-tranche-22.md), [`tranche 23`](../reports/ai-review-software-testes-2000-0001-tranche-23.md), [`tranche 24`](../reports/ai-review-software-testes-2000-0001-tranche-24.md), [`tranche 25`](../reports/ai-review-software-testes-2000-0001-tranche-25.md) e [`tranche 26`](../reports/ai-review-software-testes-2000-0001-tranche-26.md)'),
        ('[`batch-reconciliation-software-testes-2000-0001-tranche-25.md`](../reports/batch-reconciliation-software-testes-2000-0001-tranche-25.md)',
         '[`batch-reconciliation-software-testes-2000-0001-tranche-26.md`](../reports/batch-reconciliation-software-testes-2000-0001-tranche-26.md)'),
        ('> **Contagem literal:** 2.000 é a meta deste lote, não a quantidade já criada. Existem 1959 notas materiais listadas abaixo; não há IDs reservados, placeholders ou registros virtuais para as 41 restantes.',
         '> **Contagem literal:** 2.000 é a meta deste lote e todas as 2000 notas materiais já estão criadas e listadas abaixo; não há IDs reservados, placeholders ou registros virtuais.'),
        ('as 1950 notas 10–1959 das tranches 2–25 têm revisão factual por IA registrada nos relatórios vinculados. O lote continua incompleto: são 1959/2.000 notas válidas, restando 41 notas materiais.',
         'as 1991 notas 10–2000 das tranches 2–26 têm revisão factual por IA registrada nos relatórios vinculados. O lote está concluído (`complete`): são 2000/2.000 notas válidas, restando 0 notas materiais neste lote.'),
    ])

    apply(moc, [
        ('Índice das 1959 notas substantivas redigidas até agora no lote `software-testes-2000-0001`, cuja meta é 2.000. As 1959 passaram pelo gate automatizado e têm revisão factual registrada: nove aprovadas pelo usuário e 1950 aprovadas por IA',
         'Índice das 2000 notas substantivas redigidas no lote `software-testes-2000-0001` (meta de 2.000 concluída). As 2000 passaram pelo gate automatizado e têm revisão factual registrada: nove aprovadas pelo usuário e 1991 aprovadas por IA'),
        ('O gate automatizado foi aprovado por 1959/1959 notas e as 1959 contam como válidas pelo protocolo atualizado: nove têm aprovação humana histórica e 1950 têm revisão factual por IA registrada separadamente. O lote de 2.000 continua `in_progress` (1959 notas substantivas; 41 ainda não produzidas).',
         'O gate automatizado foi aprovado por 2000/2000 notas e as 2000 contam como válidas pelo protocolo atualizado: nove têm aprovação humana histórica e 1991 têm revisão factual por IA registrada separadamente. O lote de 2.000 está `complete` (2000 notas substantivas; 0 pendentes).'),
        ('[reconciliação mais recente do manifesto/fila](../../exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-25.md)',
         '[reconciliação mais recente do manifesto/fila](../../exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-26.md)'),
        (', [19](../../exports/reports/ai-review-software-testes-2000-0001-tranche-19.md), [20](../../exports/reports/ai-review-software-testes-2000-0001-tranche-20.md), [21](../../exports/reports/ai-review-software-testes-2000-0001-tranche-21.md), [22](../../exports/reports/ai-review-software-testes-2000-0001-tranche-22.md), [23](../../exports/reports/ai-review-software-testes-2000-0001-tranche-23.md), [24](../../exports/reports/ai-review-software-testes-2000-0001-tranche-24.md) e [25](../../exports/reports/ai-review-software-testes-2000-0001-tranche-25.md).',
         ', [19](../../exports/reports/ai-review-software-testes-2000-0001-tranche-19.md), [20](../../exports/reports/ai-review-software-testes-2000-0001-tranche-20.md), [21](../../exports/reports/ai-review-software-testes-2000-0001-tranche-21.md), [22](../../exports/reports/ai-review-software-testes-2000-0001-tranche-22.md), [23](../../exports/reports/ai-review-software-testes-2000-0001-tranche-23.md), [24](../../exports/reports/ai-review-software-testes-2000-0001-tranche-24.md), [25](../../exports/reports/ai-review-software-testes-2000-0001-tranche-25.md) e [26](../../exports/reports/ai-review-software-testes-2000-0001-tranche-26.md).'),
    ])

    apply(queue, [
        ('distingue 1950 revisões factuais realizadas por IA no lote `software-testes-2000-0001`',
         'distingue 1991 revisões factuais realizadas por IA no lote `software-testes-2000-0001`'),
        ('- Aprovações por IA registradas separadamente: **1950**.',
         '- Aprovações por IA registradas separadamente: **1991**.'),
        ('- Notas válidas contabilizadas (gate + revisão humana ou IA): **1999**.',
         '- Notas válidas contabilizadas (gate + revisão humana ou IA): **2040**.'),
        ('As 1950 linhas `APROVADA POR IA` (nº 50–1999) correspondem às notas 10–1959 e às revisões documentadas nos relatórios das tranches 2–25',
         'As 1991 linhas `APROVADA POR IA` (nº 50–2040) correspondem às notas 10–2000 e às revisões documentadas nos relatórios das tranches 2–26'),
    ])

    apply(ROOT / 'README.md', [
        ('| Lotes completos | 0 / 500 | O primeiro lote ainda está em andamento |',
         '| Lotes completos | 1 / 500 | Primeiro lote (`software-testes-2000-0001`) concluído com 2.000 notas válidas |'),
        ('| Notas válidas contabilizadas | 1999 / 1.000.000 (0,1999%) | 49 com aprovação humana histórica + 1950 com revisão factual por IA |',
         '| Notas válidas contabilizadas | 2040 / 1.000.000 (0,2040%) | 49 com aprovação humana histórica + 1991 com revisão factual por IA |'),
        ('| Notas com revisão factual por IA registrada | 1950 |',
         '| Notas com revisão factual por IA registrada | 1991 |'),
        ('| Primeiro lote `software-testes-2000-0001` | 1959 / 2.000 (97,95%) | 9 aprovadas por humano + 1950 por IA; faltam 41 notas substantivas |',
         '| Primeiro lote `software-testes-2000-0001` | 2000 / 2.000 (100%) | 9 aprovadas por humano + 1991 por IA; lote concluído (`complete`) |'),
        ('| Arquivos Markdown ativos em `knowledge-federation/domains/` | 2099 | 100 notas legadas com pendências + 1999 notas autorais substantivas |',
         '| Arquivos Markdown ativos em `knowledge-federation/domains/` | 2140 | 100 notas legadas com pendências + 2040 notas autorais substantivas |'),
        ('O lote em andamento é `software-testes-2000-0001`: 1959 notas materiais já passaram pelo gate e revisão factual (9 humanas + 1950 IA), com meta de 2.000.',
         'O primeiro lote concluído é `software-testes-2000-0001`: 2000 notas materiais passaram pelo gate e revisão factual (9 humanas + 1991 IA), atingindo 2.000/2.000 (100%).'),
        (', [19](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-19.md), [20](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-20.md), [21](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-21.md), [22](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-22.md), [23](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-23.md), [24](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-24.md) e [25](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-25.md))',
         ', [19](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-19.md), [20](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-20.md), [21](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-21.md), [22](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-22.md), [23](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-23.md), [24](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-24.md), [25](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-25.md) e [26](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-26.md))'),
        ('além da [reconciliação da tranche 25](knowledge-federation/exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-25.md)',
         'além da [reconciliação da tranche 26](knowledge-federation/exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-26.md)'),
    ])

    apply(KF / 'README.md', [
        ('- Arquivos Markdown ativos: **2099** (100 notas legadas com pendências + 1999 notas autorais substantivas).',
         '- Arquivos Markdown ativos: **2140** (100 notas legadas com pendências + 2040 notas autorais substantivas).'),
        ('- Notas válidas pelo protocolo atual: **1999** (49 aprovações humanas históricas + 1950 revisões factuais por IA).',
         '- Notas válidas pelo protocolo atual: **2040** (49 aprovações humanas históricas + 1991 revisões factuais por IA).'),
        ('- Progresso: **1999 / 1.000.000 (0,1999%)**; faltam 998.001 notas válidas.',
         '- Progresso: **2040 / 1.000.000 (0,2040%)**; faltam 997.960 notas válidas.'),
        ('- Lotes completos: **0 / 500**.',
         '- Lotes completos: **1 / 500** (`software-testes-2000-0001`).'),
        ('- Lote em andamento `software-testes-2000-0001`: **1959 / 2.000** notas válidas (97,95%); 9 humanas e 1950 por IA; faltam 41 notas materiais.',
         '- Primeiro lote concluído `software-testes-2000-0001`: **2000 / 2.000** notas válidas (100%); 9 humanas e 1991 por IA; status `complete`.'),
        (', [19](exports/reports/ai-review-software-testes-2000-0001-tranche-19.md), [20](exports/reports/ai-review-software-testes-2000-0001-tranche-20.md), [21](exports/reports/ai-review-software-testes-2000-0001-tranche-21.md), [22](exports/reports/ai-review-software-testes-2000-0001-tranche-22.md), [23](exports/reports/ai-review-software-testes-2000-0001-tranche-23.md), [24](exports/reports/ai-review-software-testes-2000-0001-tranche-24.md) e [25](exports/reports/ai-review-software-testes-2000-0001-tranche-25.md); veja também a [reconciliação da tranche 25](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-25.md).',
         ', [19](exports/reports/ai-review-software-testes-2000-0001-tranche-19.md), [20](exports/reports/ai-review-software-testes-2000-0001-tranche-20.md), [21](exports/reports/ai-review-software-testes-2000-0001-tranche-21.md), [22](exports/reports/ai-review-software-testes-2000-0001-tranche-22.md), [23](exports/reports/ai-review-software-testes-2000-0001-tranche-23.md), [24](exports/reports/ai-review-software-testes-2000-0001-tranche-24.md), [25](exports/reports/ai-review-software-testes-2000-0001-tranche-25.md) e [26](exports/reports/ai-review-software-testes-2000-0001-tranche-26.md); veja também a [reconciliação da tranche 26](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-26.md).'),
    ])

    apply(KF / 'README-1M.md', [
        ('tem 1999 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 1950 revisões factuais por IA registradas separadamente). O diretório ativo tem 2099 arquivos Markdown, incluindo 100 notas legadas com pendências, ainda excluídas da contagem. O lote `software-testes-2000-0001` tem 1959/2.000 notas válidas e segue em andamento; as notas 1860–1959 estão no [relatório factual por IA da tranche 25](exports/reports/ai-review-software-testes-2000-0001-tranche-25.md) e na [reconciliação da tranche 25](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-25.md); as notas 1760–1859 ficam no [relatório da tranche 24](exports/reports/ai-review-software-testes-2000-0001-tranche-24.md);',
         'tem 2040 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 1991 revisões factuais por IA registradas separadamente). O diretório ativo tem 2140 arquivos Markdown, incluindo 100 notas legadas com pendências, ainda excluídas da contagem. O lote `software-testes-2000-0001` atingiu 2000/2.000 notas válidas (`complete`); as notas 1960–2000 estão no [relatório factual por IA da tranche 26](exports/reports/ai-review-software-testes-2000-0001-tranche-26.md) e na [reconciliação da tranche 26](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-26.md); as notas 1860–1959 ficam no [relatório da tranche 25](exports/reports/ai-review-software-testes-2000-0001-tranche-25.md);'),
    ])

    apply(KF / 'STATUS-CONSOLIDACAO-1M.md', [
        ('A auditoria encontrou 2099 arquivos Markdown ativos: 1999 notas substantivas passaram pelo gate e receberam revisão factual registrada (49 humanas históricas + 1950 por IA)',
         'A auditoria encontrou 2140 arquivos Markdown ativos: 2040 notas substantivas passaram pelo gate e receberam revisão factual registrada (49 humanas históricas + 1991 por IA)'),
        ('O lote parcial não está completo; placeholders, IDs e materialização de arquivos não contam.',
         'O primeiro lote (`software-testes-2000-0001`) está completo com 2.000 notas substantivas; placeholders, IDs e materialização de arquivos não contam.'),
        ('| Lotes completos | 0 / 500 | O primeiro lote ainda não tem 2.000 notas |',
         '| Lotes completos | 1 / 500 | Primeiro lote (`software-testes-2000-0001`) concluído com 2.000 notas |'),
        ('| Progresso válido global | 1999 / 1.000.000 (0,1999%) | 49 revisões humanas históricas + 1950 revisões por IA registradas separadamente |',
         '| Progresso válido global | 2040 / 1.000.000 (0,2040%) | 49 revisões humanas históricas + 1991 revisões por IA registradas separadamente |'),
        ('| Revisões factuais por IA registradas | 1950 | Relatórios das tranches 2–25',
         '| Revisões factuais por IA registradas | 1991 | Relatórios das tranches 2–26'),
        ('| Primeiro lote | 1959 / 2.000 (97,95%) | 9 humanas + 1950 IA; faltam 41 notas substantivas |',
         '| Primeiro lote | 2000 / 2.000 (100%) | 9 humanas + 1991 IA; lote concluído (`complete`) |'),
        ('| Candidatas que passaram pelo gate automatizado | 1999 |',
         '| Candidatas que passaram pelo gate automatizado | 2040 |'),
        ('Revisadas factualmente por IA as notas 10–1959 do lote (1950 no total)',
         'Revisadas factualmente por IA as notas 10–2000 do lote (1991 no total)'),
        (', [19](exports/reports/ai-review-software-testes-2000-0001-tranche-19.md), [20](exports/reports/ai-review-software-testes-2000-0001-tranche-20.md), [21](exports/reports/ai-review-software-testes-2000-0001-tranche-21.md), [22](exports/reports/ai-review-software-testes-2000-0001-tranche-22.md), [23](exports/reports/ai-review-software-testes-2000-0001-tranche-23.md), [24](exports/reports/ai-review-software-testes-2000-0001-tranche-24.md) e [25](exports/reports/ai-review-software-testes-2000-0001-tranche-25.md).',
         ', [19](exports/reports/ai-review-software-testes-2000-0001-tranche-19.md), [20](exports/reports/ai-review-software-testes-2000-0001-tranche-20.md), [21](exports/reports/ai-review-software-testes-2000-0001-tranche-21.md), [22](exports/reports/ai-review-software-testes-2000-0001-tranche-22.md), [23](exports/reports/ai-review-software-testes-2000-0001-tranche-23.md), [24](exports/reports/ai-review-software-testes-2000-0001-tranche-24.md), [25](exports/reports/ai-review-software-testes-2000-0001-tranche-25.md) e [26](exports/reports/ai-review-software-testes-2000-0001-tranche-26.md).'),
        ('4. Resultado parcial do primeiro lote: 1959/1959 aprovadas pelo gate; nove revisões humanas e 1950 revisões por IA no total após a tranche 25, incluindo as 100 novas revisões das notas 1860–1959. O lote continua `in_progress`, com alvo de 2.000.',
         '4. Resultado final do primeiro lote: 2000/2000 aprovadas pelo gate; nove revisões humanas e 1991 revisões por IA no total após a tranche 26, incluindo as 41 novas revisões das notas 1960–2000. O lote atingiu o alvo de 2.000 e passa ao estado `complete`.'),
        ('Relatórios atualizados: [reconciliação da tranche 25](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-25.md)',
         'Relatórios atualizados: [reconciliação da tranche 26](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-26.md)'),
        ('1. Continuar o lote atual com conteúdo real, fontes verificadas e revisão factual por tranche; faltam 41 notas para o tamanho configurado de 2.000.',
         '1. Primeiro lote (`software-testes-2000-0001`) concluído com 2.000/2.000 notas substantivas, fontes verificadas e revisão factual por tranche.'),
    ])

    apply(KF / 'PLANO-CONTINUO-1M.md', [
        ('- Notas válidas globais: **1999** (49 aprovações humanas históricas + 1950 revisões factuais por IA).',
         '- Notas válidas globais: **2040** (49 aprovações humanas históricas + 1991 revisões factuais por IA).'),
        ('- Progresso: **1999 / 1.000.000 (0,1999%)**; faltam **998.001** notas válidas.',
         '- Progresso: **2040 / 1.000.000 (0,2040%)**; faltam **997.960** notas válidas.'),
        ('- Lotes completos: **0 / 500**.',
         '- Lotes completos: **1 / 500** (`software-testes-2000-0001`).'),
        ('- Lote atual `software-testes-2000-0001`: **1959 / 2.000 (97,95%)** notas válidas (9 humanas + 1950 IA); faltam **41** notas substantivas.',
         '- Primeiro lote `software-testes-2000-0001`: **2000 / 2.000 (100%)** notas válidas (9 humanas + 1991 IA); concluído (`complete`).'),
        ('- Arquivos Markdown ativos: **2099**; 100 com pendências de qualidade, excluídos da contagem.',
         '- Arquivos Markdown ativos: **2140**; 100 com pendências de qualidade, excluídos da contagem.'),
        ('| 4 | Conferir factual e registrar notas 10–1959 do primeiro lote | **Concluído até a tranche 25** | 1950 revisões por IA em relatórios das tranches 2–25, além das 9 aprovações humanas. |',
         '| 4 | Conferir factual e registrar notas 10–2000 do primeiro lote | **Concluído (tranches 2–26)** | 1991 revisões por IA em relatórios das tranches 2–26, além das 9 aprovações humanas. |'),
        ('| 5 | Rodar gate, testes, auditorias e diff | **Concluído para o estado atual** | Lote: 1959/1959 no gate, 9 humanas, 1950 IA. Global: 2099 arquivos, 1999 válidas, 100 com pendências legadas; veja a [reconciliação da tranche 25](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-25.md). |',
         '| 5 | Rodar gate, testes, auditorias e diff | **Concluído para o estado atual** | Lote: 2000/2000 no gate, 9 humanas, 1991 IA. Global: 2140 arquivos, 2040 válidas, 100 com pendências legadas; veja a [reconciliação da tranche 26](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-26.md). |'),
        ('| 7 | Completar o lote `software-testes-2000-0001` até 2.000 notas | **Em andamento** | 1959/2.000; faltam 41 notas; continuar com conteúdo substantivo e fontes verificadas. Não marcar como completo antes do padrão definido. |',
         '| 7 | Completar o lote `software-testes-2000-0001` até 2.000 notas | **Concluído** | 2000/2.000 (100%); todas as 2.000 notas substantivas contam com gate aprovado, fontes verificadas e revisão factual registrada (`complete`). |'),
        ('Progresso atual: 1999 notas válidas, 0/500 lotes completos.',
         'Progresso atual: 2040 notas válidas, 1/500 lotes completos.'),
    ])

    apply(KF / 'RECOVERY-AND-SCALE-NOTE.md', [
        ('há 2099 arquivos: 100 legados com pendências e 1999 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 1950 revisões por IA). O lote `software-testes-2000-0001` tem 1959/2.000 notas válidas (9 humanas + 1950 IA), com status `in_progress` e 41 notas qualificadas restantes. As notas 1860–1959 passaram pelo gate e têm revisão factual por IA registrada na [tranche 25](exports/reports/ai-review-software-testes-2000-0001-tranche-25.md), com [reconciliação](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-25.md);',
         'há 2140 arquivos: 100 legados com pendências e 2040 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 1991 revisões por IA). O lote `software-testes-2000-0001` atingiu 2000/2.000 notas válidas (9 humanas + 1991 IA), com status `complete`. As notas 1960–2000 passaram pelo gate e têm revisão factual por IA registrada na [tranche 26](exports/reports/ai-review-software-testes-2000-0001-tranche-26.md), com [reconciliação](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-26.md);'),
        ('1. Continuar o lote atual em tranches de conteúdo real; faltam 41 notas qualificadas para completar as 2.000 configuradas.',
         '1. Primeiro lote (`software-testes-2000-0001`) concluído com 2.000/2.000 notas qualificadas em tranches de conteúdo real.'),
    ])

    apply(KF / '00-home-vault' / 'Home.md', [
        ('[[MOC-Testes-Software-0007]] — 1959 notas do lote de escala (meta: 2.000); nove têm aprovação humana histórica e 1950 revisões factuais por IA.',
         '[[MOC-Testes-Software-0007]] — 2000 notas do lote de escala (meta de 2.000 concluída); nove têm aprovação humana histórica e 1991 revisões factuais por IA.'),
        ('[[human-review-queue|Registro de revisões factuais]] — 49 aprovações humanas e 1950 aprovações por IA, identificadas separadamente.',
         '[[human-review-queue|Registro de revisões factuais]] — 49 aprovações humanas e 1991 aprovações por IA, identificadas separadamente.'),
        ('[[note-quality-audit|Auditoria de qualidade]] — 1999 notas válidas pelo protocolo atual (49 humanas + 1950 IA) e 100 notas legadas com falhas.',
         '[[note-quality-audit|Auditoria de qualidade]] — 2040 notas válidas pelo protocolo atual (49 humanas + 1991 IA) e 100 notas legadas com falhas.'),
    ])

    apply(KF / '00-home-vault' / 'Indice-Global.md', [
        ('- Arquivos Markdown em `domains/`: **2099** (100 sementes legadas + 1999 notas autorais substantivas).',
         '- Arquivos Markdown em `domains/`: **2140** (100 sementes legadas + 2040 notas autorais substantivas).'),
        ('- Candidatas aprovadas no gate automatizado: **1999**; revisões humanas registradas: **49**; revisões factuais por IA: **1950**; 100 sementes legadas mantêm pendências.',
         '- Candidatas aprovadas no gate automatizado: **2040**; revisões humanas registradas: **49**; revisões factuais por IA: **1991**; 100 sementes legadas mantêm pendências.'),
        ('- Os lotes atuais totalizam 1999 notas válidas pelo protocolo; o lote `software-testes-2000-0001` tem 1959/2.000, incluindo as notas 1860–1959 revisadas por IA na [tranche 25](../exports/reports/ai-review-software-testes-2000-0001-tranche-25.md) e na [reconciliação da tranche 25](../exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-25.md), as notas 1760–1859 na [tranche 24](../exports/reports/ai-review-software-testes-2000-0001-tranche-24.md),',
         '- Os lotes atuais totalizam 2040 notas válidas pelo protocolo; o lote `software-testes-2000-0001` atingiu 2000/2.000 (`complete`), incluindo as notas 1960–2000 revisadas por IA na [tranche 26](../exports/reports/ai-review-software-testes-2000-0001-tranche-26.md) e na [reconciliação da tranche 26](../exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-26.md), as notas 1860–1959 na [tranche 25](../exports/reports/ai-review-software-testes-2000-0001-tranche-25.md),'),
    ])
    print("reconciliação concluída")


if __name__ == "__main__":
    main()
