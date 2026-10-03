#!/usr/bin/env python3
"""Reconcile batch software-devops-2000-0002 tranche 19 (IDs 1801-1900) across manifest, MOC, review registry and status docs."""
from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KF = ROOT / "knowledge-federation"
SCRIPTS = KF / "scripts"
BATCH_ID = "software-devops-2000-0002"
REPORT_NAME = "ai-review-software-devops-2000-0002-tranche-19.md"
RECON_NAME = "batch-reconciliation-software-devops-2000-0002-tranche-19.md"
DATE = "2026-10-03"


def load_builder():
    spec = importlib.util.spec_from_file_location("bd19", SCRIPTS / "_build_devops_t19.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_groups(bd19):
    groups = []
    for path in sorted(bd19.DATA_DIR.glob("*.txt")):
        context, rows = bd19.parse_group(path)
        groups.append((context, rows))
    return groups


def manifest_section(groups) -> str:
    lines = [
        "## Tranche 19 — OpenFaaS, Fission, Nuclio, Temporal, HashiCorp Boundary, Tailscale, Headscale, NetBird, Nebula e kpack (100 notas; revisão factual por IA registrada)",
        "",
    ]
    for context, rows in groups:
        lines.append(f"### {context['group_title']}")
        lines.append("")
        for index, row in enumerate(rows):
            number = int(context["first"]) + index
            lines.append(
                f"{number}. [{row['title']}](../../domains/software-0008/software/devops/{row['slug']}.md)"
            )
        lines.append("")
    return "\n".join(lines) + "\n"


def moc_section(groups) -> str:
    lines = [
        "## Tranche 19 — OpenFaaS, Fission, Nuclio, Temporal, HashiCorp Boundary, Tailscale, Headscale, NetBird, Nebula e kpack",
        "",
    ]
    for context, rows in groups:
        lines.append(f"### {context['group_title']}")
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
            position = 2041 + (number - 1)
            lines.append(
                f"| {position} | `{BATCH_ID}` | [{row['title']}](../../domains/software-0008/software/devops/{row['slug']}.md) "
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
    bd19 = load_builder()
    groups = load_groups(bd19)
    total = sum(len(rows) for _, rows in groups)
    if total != 100 or int(groups[0][0]["first"]) != 1801 or int(groups[-1][0]["first"]) != 1891:
        raise SystemExit(f"dados inesperados: {total} notas, primeiro grupo em {groups[0][0]['first']}")

    manifest = KF / "exports" / "batches" / f"{BATCH_ID}.md"
    moc = KF / "00-home-vault" / "MOCs" / "MOC-DevOps-Software-0008.md"
    queue = KF / "exports" / "reports" / "human-review-queue.md"

    insert_before(manifest, "## Critérios e próximo passo", manifest_section(groups))
    insert_before(moc, "## Estado editorial", moc_section(groups))
    insert_before(queue, "## Regra de contagem", review_rows(groups))

    apply(manifest, [
        ('- Notas efetivamente redigidas até agora: **1800 / 2.000 (90,00%)**',
         '- Notas efetivamente redigidas até agora: **1900 / 2.000 (95,00%)**'),
        ('- Gate automatizado: **1800/1800 aprovadas** (conteúdo mínimo, seções, fontes específicas e wikilinks; reexecutado após a tranche 18)',
         '- Gate automatizado: **1900/1900 aprovadas** (conteúdo mínimo, seções, fontes específicas e wikilinks; reexecutado após a tranche 19)'),
        ('- Revisão factual humana: **0/1800**',
         '- Revisão factual humana: **0/1900**'),
        ('- Revisão factual por IA: **1800/1800**',
         '- Revisão factual por IA: **1900/1900**'),
        ('- Contabilizadas como válidas: **1800/1800**',
         '- Contabilizadas como válidas: **1900/1900**'),
        ('- Revisor das 1800 notas aprovadas por IA: `Arena.ai Agent Mode`, com relatórios específicos; não são aprovações humanas',
         '- Revisor das 1900 notas aprovadas por IA: `Arena.ai Agent Mode`, com relatórios específicos; não são aprovações humanas'),
        ('- Status do lote maior: `in_progress`; tranches 1–18 (1800 notas, IDs 1–1800) foram conferidas factualmente por IA e aprovadas sob o protocolo atualizado',
         '- Status do lote maior: `in_progress`; tranches 1–19 (1900 notas, IDs 1–1900) foram conferidas factualmente por IA e aprovadas sob o protocolo atualizado'),
        ('- Reconciliação estrutural mais recente do manifesto/fila: [`batch-reconciliation-software-devops-2000-0002-tranche-18.md`](../reports/batch-reconciliation-software-devops-2000-0002-tranche-18.md)',
         '- Reconciliação estrutural mais recente do manifesto/fila: [`batch-reconciliation-software-devops-2000-0002-tranche-19.md`](../reports/batch-reconciliation-software-devops-2000-0002-tranche-19.md)'),
        ('- Relatórios factuais por IA: [`tranche 1`](../reports/ai-review-software-devops-2000-0002-tranche-01.md), [`tranche 2`](../reports/ai-review-software-devops-2000-0002-tranche-02.md), [`tranche 3`](../reports/ai-review-software-devops-2000-0002-tranche-03.md), [`tranche 4`](../reports/ai-review-software-devops-2000-0002-tranche-04.md), [`tranche 5`](../reports/ai-review-software-devops-2000-0002-tranche-05.md), [`tranche 6`](../reports/ai-review-software-devops-2000-0002-tranche-06.md), [`tranche 7`](../reports/ai-review-software-devops-2000-0002-tranche-07.md), [`tranche 8`](../reports/ai-review-software-devops-2000-0002-tranche-08.md), [`tranche 9`](../reports/ai-review-software-devops-2000-0002-tranche-09.md), [`tranche 10`](../reports/ai-review-software-devops-2000-0002-tranche-10.md), [`tranche 11`](../reports/ai-review-software-devops-2000-0002-tranche-11.md), [`tranche 12`](../reports/ai-review-software-devops-2000-0002-tranche-12.md), [`tranche 13`](../reports/ai-review-software-devops-2000-0002-tranche-13.md), [`tranche 14`](../reports/ai-review-software-devops-2000-0002-tranche-14.md), [`tranche 15`](../reports/ai-review-software-devops-2000-0002-tranche-15.md), [`tranche 16`](../reports/ai-review-software-devops-2000-0002-tranche-16.md), [`tranche 17`](../reports/ai-review-software-devops-2000-0002-tranche-17.md), [`tranche 18`](../reports/ai-review-software-devops-2000-0002-tranche-18.md)',
         '- Relatórios factuais por IA: [`tranche 1`](../reports/ai-review-software-devops-2000-0002-tranche-01.md), [`tranche 2`](../reports/ai-review-software-devops-2000-0002-tranche-02.md), [`tranche 3`](../reports/ai-review-software-devops-2000-0002-tranche-03.md), [`tranche 4`](../reports/ai-review-software-devops-2000-0002-tranche-04.md), [`tranche 5`](../reports/ai-review-software-devops-2000-0002-tranche-05.md), [`tranche 6`](../reports/ai-review-software-devops-2000-0002-tranche-06.md), [`tranche 7`](../reports/ai-review-software-devops-2000-0002-tranche-07.md), [`tranche 8`](../reports/ai-review-software-devops-2000-0002-tranche-08.md), [`tranche 9`](../reports/ai-review-software-devops-2000-0002-tranche-09.md), [`tranche 10`](../reports/ai-review-software-devops-2000-0002-tranche-10.md), [`tranche 11`](../reports/ai-review-software-devops-2000-0002-tranche-11.md), [`tranche 12`](../reports/ai-review-software-devops-2000-0002-tranche-12.md), [`tranche 13`](../reports/ai-review-software-devops-2000-0002-tranche-13.md), [`tranche 14`](../reports/ai-review-software-devops-2000-0002-tranche-14.md), [`tranche 15`](../reports/ai-review-software-devops-2000-0002-tranche-15.md), [`tranche 16`](../reports/ai-review-software-devops-2000-0002-tranche-16.md), [`tranche 17`](../reports/ai-review-software-devops-2000-0002-tranche-17.md), [`tranche 18`](../reports/ai-review-software-devops-2000-0002-tranche-18.md), [`tranche 19`](../reports/ai-review-software-devops-2000-0002-tranche-19.md)'),
        ('Existem 1800 notas materiais listadas abaixo; não há IDs reservados, placeholders ou registros virtuais para as 200 restantes.',
         'Existem 1900 notas materiais listadas abaixo; não há IDs reservados, placeholders ou registros virtuais para as 100 restantes.'),
        ('As 1800 notas 1–1800 das tranches 1–18 têm revisão factual por IA registrada nos relatórios vinculados. O lote continua incompleto: são 1800/2.000 notas válidas, restando 200 notas materiais.',
         'As 1900 notas 1–1900 das tranches 1–19 têm revisão factual por IA registrada nos relatórios vinculados. O lote continua incompleto: são 1900/2.000 notas válidas, restando 100 notas materiais.'),
    ])

    apply(moc, [
        ('Índice das 1800 notas substantivas redigidas até agora no lote `software-devops-2000-0002`, cuja meta é 2.000. As 1800 passaram pelo gate automatizado',
         'Índice das 1900 notas substantivas redigidas até agora no lote `software-devops-2000-0002`, cuja meta é 2.000. As 1900 passaram pelo gate automatizado'),
        ('O gate automatizado foi aprovado por 1800/1800 notas e as 1800 contam como válidas pelo protocolo atualizado, com revisão factual por IA registrada separadamente. O lote de 2.000 continua `in_progress` (1800 notas substantivas; 200 ainda não produzidas). Consulte o [manifesto](../../exports/batches/software-devops-2000-0002.md), a [auditoria de qualidade](../../exports/reports/note-quality-software-devops-2000-0002.md) e a [reconciliação mais recente do manifesto/fila](../../exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-18.md). Os relatórios factuais por IA são [tranche 1](../../exports/reports/ai-review-software-devops-2000-0002-tranche-01.md), [tranche 2](../../exports/reports/ai-review-software-devops-2000-0002-tranche-02.md), [tranche 3](../../exports/reports/ai-review-software-devops-2000-0002-tranche-03.md), [tranche 4](../../exports/reports/ai-review-software-devops-2000-0002-tranche-04.md), [tranche 5](../../exports/reports/ai-review-software-devops-2000-0002-tranche-05.md), [tranche 6](../../exports/reports/ai-review-software-devops-2000-0002-tranche-06.md), [tranche 7](../../exports/reports/ai-review-software-devops-2000-0002-tranche-07.md), [tranche 8](../../exports/reports/ai-review-software-devops-2000-0002-tranche-08.md), [tranche 9](../../exports/reports/ai-review-software-devops-2000-0002-tranche-09.md), [tranche 10](../../exports/reports/ai-review-software-devops-2000-0002-tranche-10.md), [tranche 11](../../exports/reports/ai-review-software-devops-2000-0002-tranche-11.md), [tranche 12](../../exports/reports/ai-review-software-devops-2000-0002-tranche-12.md), [tranche 13](../../exports/reports/ai-review-software-devops-2000-0002-tranche-13.md), [tranche 14](../../exports/reports/ai-review-software-devops-2000-0002-tranche-14.md), [tranche 15](../../exports/reports/ai-review-software-devops-2000-0002-tranche-15.md), [tranche 16](../../exports/reports/ai-review-software-devops-2000-0002-tranche-16.md), [tranche 17](../../exports/reports/ai-review-software-devops-2000-0002-tranche-17.md) e [tranche 18](../../exports/reports/ai-review-software-devops-2000-0002-tranche-18.md).',
         'O gate automatizado foi aprovado por 1900/1900 notas e as 1900 contam como válidas pelo protocolo atualizado, com revisão factual por IA registrada separadamente. O lote de 2.000 continua `in_progress` (1900 notas substantivas; 100 ainda não produzidas). Consulte o [manifesto](../../exports/batches/software-devops-2000-0002.md), a [auditoria de qualidade](../../exports/reports/note-quality-software-devops-2000-0002.md) e a [reconciliação mais recente do manifesto/fila](../../exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-19.md). Os relatórios factuais por IA são [tranche 1](../../exports/reports/ai-review-software-devops-2000-0002-tranche-01.md), [tranche 2](../../exports/reports/ai-review-software-devops-2000-0002-tranche-02.md), [tranche 3](../../exports/reports/ai-review-software-devops-2000-0002-tranche-03.md), [tranche 4](../../exports/reports/ai-review-software-devops-2000-0002-tranche-04.md), [tranche 5](../../exports/reports/ai-review-software-devops-2000-0002-tranche-05.md), [tranche 6](../../exports/reports/ai-review-software-devops-2000-0002-tranche-06.md), [tranche 7](../../exports/reports/ai-review-software-devops-2000-0002-tranche-07.md), [tranche 8](../../exports/reports/ai-review-software-devops-2000-0002-tranche-08.md), [tranche 9](../../exports/reports/ai-review-software-devops-2000-0002-tranche-09.md), [tranche 10](../../exports/reports/ai-review-software-devops-2000-0002-tranche-10.md), [tranche 11](../../exports/reports/ai-review-software-devops-2000-0002-tranche-11.md), [tranche 12](../../exports/reports/ai-review-software-devops-2000-0002-tranche-12.md), [tranche 13](../../exports/reports/ai-review-software-devops-2000-0002-tranche-13.md), [tranche 14](../../exports/reports/ai-review-software-devops-2000-0002-tranche-14.md), [tranche 15](../../exports/reports/ai-review-software-devops-2000-0002-tranche-15.md), [tranche 16](../../exports/reports/ai-review-software-devops-2000-0002-tranche-16.md), [tranche 17](../../exports/reports/ai-review-software-devops-2000-0002-tranche-17.md), [tranche 18](../../exports/reports/ai-review-software-devops-2000-0002-tranche-18.md) e [tranche 19](../../exports/reports/ai-review-software-devops-2000-0002-tranche-19.md).'),
    ])

    apply(queue, [
        ('distingue 3791 revisões factuais realizadas por IA nos lotes `software-testes-2000-0001` (1991) e `software-devops-2000-0002` (1800)',
         'distingue 3891 revisões factuais realizadas por IA nos lotes `software-testes-2000-0001` (1991) e `software-devops-2000-0002` (1900)'),
        ('- Aprovações por IA registradas separadamente: **3791**.',
         '- Aprovações por IA registradas separadamente: **3891**.'),
        ('- Notas válidas contabilizadas (gate + revisão humana ou IA): **3840**.',
         '- Notas válidas contabilizadas (gate + revisão humana ou IA): **3940**.'),
        ('As 3791 linhas `APROVADA POR IA` (nº 50–3840) correspondem às 1991 notas 10–2000 das tranches 2–26 do lote `software-testes-2000-0001` e às 1800 notas 1–1800 das tranches 1–18 do lote `software-devops-2000-0002`',
         'As 3891 linhas `APROVADA POR IA` (nº 50–3940) correspondem às 1991 notas 10–2000 das tranches 2–26 do lote `software-testes-2000-0001` e às 1900 notas 1–1900 das tranches 1–19 do lote `software-devops-2000-0002`'),
    ])

    apply(ROOT / 'README.md', [
        ('| Notas válidas contabilizadas | 3840 / 1.000.000 (0,3840%) | 49 com aprovação humana histórica + 3791 com revisão factual por IA |',
         '| Notas válidas contabilizadas | 3940 / 1.000.000 (0,3940%) | 49 com aprovação humana histórica + 3891 com revisão factual por IA |'),
        ('| Notas com revisão factual por IA registrada | 3791 | Revisões dos lotes de escala (1991 no lote 1 + 1800 no lote 2), com relatórios por tranche; não são humanas |',
         '| Notas com revisão factual por IA registrada | 3891 | Revisões dos lotes de escala (1991 no lote 1 + 1900 no lote 2), com relatórios por tranche; não são humanas |'),
        ('| Segundo lote `software-devops-2000-0002` | 1800 / 2.000 (90,00%) | 1800 aprovadas por IA nas tranches 1–18; faltam 200 notas substantivas |',
         '| Segundo lote `software-devops-2000-0002` | 1900 / 2.000 (95,00%) | 1900 aprovadas por IA nas tranches 1–19; faltam 100 notas substantivas |'),
        ('| Arquivos Markdown ativos em `knowledge-federation/domains/` | 3940 | 100 notas legadas com pendências + 3840 notas autorais substantivas |',
         '| Arquivos Markdown ativos em `knowledge-federation/domains/` | 4040 | 100 notas legadas com pendências + 3940 notas autorais substantivas |'),
        ('1800 notas materiais já passaram pelo gate e revisão factual por IA até a [tranche 18](knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-18.md) ([reconciliação](knowledge-federation/exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-18.md), [auditoria do lote](knowledge-federation/exports/reports/note-quality-software-devops-2000-0002.md) e [MOC de DevOps](knowledge-federation/00-home-vault/MOCs/MOC-DevOps-Software-0008.md)), com meta de 2.000.',
         '1900 notas materiais já passaram pelo gate e revisão factual por IA até a [tranche 19](knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-19.md) ([reconciliação](knowledge-federation/exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-19.md), [auditoria do lote](knowledge-federation/exports/reports/note-quality-software-devops-2000-0002.md) e [MOC de DevOps](knowledge-federation/00-home-vault/MOCs/MOC-DevOps-Software-0008.md)), com meta de 2.000.'),
    ])

    apply(KF / 'README.md', [
        ('- Arquivos Markdown ativos: **3940** (100 notas legadas com pendências + 3840 notas autorais substantivas).',
         '- Arquivos Markdown ativos: **4040** (100 notas legadas com pendências + 3940 notas autorais substantivas).'),
        ('- Notas válidas pelo protocolo atual: **3840** (49 aprovações humanas históricas + 3791 revisões factuais por IA).',
         '- Notas válidas pelo protocolo atual: **3940** (49 aprovações humanas históricas + 3891 revisões factuais por IA).'),
        ('- Progresso: **3840 / 1.000.000 (0,3840%)**; faltam 996.160 notas válidas.',
         '- Progresso: **3940 / 1.000.000 (0,3940%)**; faltam 996.060 notas válidas.'),
        ('- Segundo lote em andamento `software-devops-2000-0002`: **1800 / 2.000** notas válidas (90,00%); 1800 por IA ([tranche 18](exports/reports/ai-review-software-devops-2000-0002-tranche-18.md) e [reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-18.md)); faltam 200 notas materiais.',
         '- Segundo lote em andamento `software-devops-2000-0002`: **1900 / 2.000** notas válidas (95,00%); 1900 por IA ([tranche 19](exports/reports/ai-review-software-devops-2000-0002-tranche-19.md) e [reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-19.md)); faltam 100 notas materiais.'),
    ])

    apply(KF / 'README-1M.md', [
        ('tem 3840 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 3791 revisões factuais por IA registradas separadamente). O diretório ativo tem 3940 arquivos Markdown, incluindo 100 notas legadas com pendências, ainda excluídas da contagem. O segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) está em andamento com 1800/2.000 notas válidas ([relatório factual por IA da tranche 18](exports/reports/ai-review-software-devops-2000-0002-tranche-18.md) e [reconciliação da tranche 18](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-18.md)),',
         'tem 3940 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 3891 revisões factuais por IA registradas separadamente). O diretório ativo tem 4040 arquivos Markdown, incluindo 100 notas legadas com pendências, ainda excluídas da contagem. O segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) está em andamento com 1900/2.000 notas válidas ([relatório factual por IA da tranche 19](exports/reports/ai-review-software-devops-2000-0002-tranche-19.md) e [reconciliação da tranche 19](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-19.md)),'),
    ])

    apply(KF / 'STATUS-CONSOLIDACAO-1M.md', [
        ('A auditoria encontrou 3940 arquivos Markdown ativos: 3840 notas substantivas passaram pelo gate e receberam revisão factual registrada (49 humanas históricas + 3791 por IA)',
         'A auditoria encontrou 4040 arquivos Markdown ativos: 3940 notas substantivas passaram pelo gate e receberam revisão factual registrada (49 humanas históricas + 3891 por IA)'),
        ('| Progresso válido global | 3840 / 1.000.000 (0,3840%) | 49 revisões humanas históricas + 3791 revisões por IA registradas separadamente |',
         '| Progresso válido global | 3940 / 1.000.000 (0,3940%) | 49 revisões humanas históricas + 3891 revisões por IA registradas separadamente |'),
        ('| Revisões factuais por IA registradas | 3791 | Relatórios das tranches 2–26 (`software-testes-2000-0001`) e tranches 1–18 (`software-devops-2000-0002`); não são humanas |',
         '| Revisões factuais por IA registradas | 3891 | Relatórios das tranches 2–26 (`software-testes-2000-0001`) e tranches 1–19 (`software-devops-2000-0002`); não são humanas |'),
        ('| Segundo lote (`software-devops-2000-0002`) | 1800 / 2.000 (90,00%) | 1800 IA nas tranches 1–18 ([tranche 18](exports/reports/ai-review-software-devops-2000-0002-tranche-18.md)); faltam 200 notas substantivas |',
         '| Segundo lote (`software-devops-2000-0002`) | 1900 / 2.000 (95,00%) | 1900 IA nas tranches 1–19 ([tranche 19](exports/reports/ai-review-software-devops-2000-0002-tranche-19.md)); faltam 100 notas substantivas |'),
        ('| Candidatas que passaram pelo gate automatizado | 3840 |',
         ('| Candidatas que passaram pelo gate automatizado | 3940 |')),
        ('O segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) está em 1800/2.000 notas válidas após a [tranche 18](exports/reports/ai-review-software-devops-2000-0002-tranche-18.md) ([reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-18.md)).',
         'O segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) está em 1900/2.000 notas válidas após a [tranche 19](exports/reports/ai-review-software-devops-2000-0002-tranche-19.md) ([reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-19.md)).'),
        ('3. Continuar o segundo lote `software-devops-2000-0002` (atualmente em 1800/2.000; faltam 200 notas substantivas) e os 498 lotes subsequentes,',
         '3. Continuar o segundo lote `software-devops-2000-0002` (atualmente em 1900/2.000; faltam 100 notas substantivas) e os 498 lotes subsequentes,'),
    ])

    apply(KF / 'PLANO-CONTINUO-1M.md', [
        ('- Notas válidas globais: **3840** (49 aprovações humanas históricas + 3791 revisões factuais por IA).',
         '- Notas válidas globais: **3940** (49 aprovações humanas históricas + 3891 revisões factuais por IA).'),
        ('- Progresso: **3840 / 1.000.000 (0,3840%)**; faltam **996.160** notas válidas.',
         '- Progresso: **3940 / 1.000.000 (0,3940%)**; faltam **996.060** notas válidas.'),
        ('- Segundo lote atual `software-devops-2000-0002`: **1800 / 2.000 (90,00%)** notas válidas (1800 IA nas tranches 1–18); faltam **200** notas substantivas.',
         '- Segundo lote atual `software-devops-2000-0002`: **1900 / 2.000 (95,00%)** notas válidas (1900 IA nas tranches 1–19); faltam **100** notas substantivas.'),
        ('- Arquivos Markdown ativos: **3940**; 100 com pendências de qualidade, excluídos da contagem.',
         '- Arquivos Markdown ativos: **4040**; 100 com pendências de qualidade, excluídos da contagem.'),
        ('| 5 | Rodar gate, testes, auditorias e diff | **Concluído para o estado atual** | Lote 1: 2000/2000 (`complete`). Lote 2 (`software-devops-2000-0002`): 1800/1800 no gate (1800 IA). Global: 3940 arquivos, 3840 válidas, 100 com pendências legadas; veja a [reconciliação da tranche 18 do lote 2](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-18.md). |',
         '| 5 | Rodar gate, testes, auditorias e diff | **Concluído para o estado atual** | Lote 1: 2000/2000 (`complete`). Lote 2 (`software-devops-2000-0002`): 1900/1900 no gate (1900 IA). Global: 4040 arquivos, 3940 válidas, 100 com pendências legadas; veja a [reconciliação da tranche 19 do lote 2](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-19.md). |'),
        ('| 8 | Abrir lotes subsequentes de 2.000 notas | **Em andamento (lote 2 em 90%)** | Segundo lote `software-devops-2000-0002` com 1800/2.000 notas válidas nas tranches 1–18; restam 200 notas neste lote e 498 lotes subsequentes. |',
         '| 8 | Abrir lotes subsequentes de 2.000 notas | **Em andamento (lote 2 em 95%)** | Segundo lote `software-devops-2000-0002` com 1900/2.000 notas válidas nas tranches 1–19; restam 100 notas neste lote e 498 lotes subsequentes. |'),
        ('Progresso atual: 3840 notas válidas, 1/500 lotes completos.',
         'Progresso atual: 3940 notas válidas, 1/500 lotes completos.'),
    ])

    apply(KF / 'RECOVERY-AND-SCALE-NOTE.md', [
        ('há 3940 arquivos: 100 legados com pendências e 3840 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 3791 revisões por IA). O primeiro lote `software-testes-2000-0001` atingiu 2000/2.000 notas válidas (9 humanas + 1991 IA), com status `complete` ([tranche 26](exports/reports/ai-review-software-testes-2000-0001-tranche-26.md) e [reconciliação](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-26.md)); o segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) está em andamento (`in_progress`) com 1800/2.000 notas válidas revisadas por IA até a [tranche 18](exports/reports/ai-review-software-devops-2000-0002-tranche-18.md), com [reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-18.md);',
         'há 4040 arquivos: 100 legados com pendências e 3940 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 3891 revisões por IA). O primeiro lote `software-testes-2000-0001` atingiu 2000/2.000 notas válidas (9 humanas + 1991 IA), com status `complete` ([tranche 26](exports/reports/ai-review-software-testes-2000-0001-tranche-26.md) e [reconciliação](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-26.md)); o segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) está em andamento (`in_progress`) com 1900/2.000 notas válidas revisadas por IA até a [tranche 19](exports/reports/ai-review-software-devops-2000-0002-tranche-19.md), com [reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-19.md);'),
        ('4. Continuar o segundo lote `software-devops-2000-0002` (1800/2.000; faltam 200 notas qualificadas) até 2.000 antes de abrir os 498 lotes seguintes.',
         '4. Continuar o segundo lote `software-devops-2000-0002` (1900/2.000; faltam 100 notas qualificadas) até 2.000 antes de abrir os 498 lotes seguintes.'),
    ])

    apply(KF / '00-home-vault' / 'Home.md', [
        ('- [[MOC-DevOps-Software-0008]] — 1800 notas do segundo lote de escala `software-devops-2000-0002` (meta: 2.000); 1800 revisões factuais por IA.',
         '- [[MOC-DevOps-Software-0008]] — 1900 notas do segundo lote de escala `software-devops-2000-0002` (meta: 2.000); 1900 revisões factuais por IA.'),
        ('[[human-review-queue|Registro de revisões factuais]] — 49 aprovações humanas e 3791 aprovações por IA, identificadas separadamente.',
         '[[human-review-queue|Registro de revisões factuais]] — 49 aprovações humanas e 3891 aprovações por IA, identificadas separadamente.'),
        ('[[note-quality-audit|Auditoria de qualidade]] — 3840 notas válidas pelo protocolo atual (49 humanas + 3791 IA) e 100 notas legadas com falhas.',
         '[[note-quality-audit|Auditoria de qualidade]] — 3940 notas válidas pelo protocolo atual (49 humanas + 3891 IA) e 100 notas legadas com falhas.'),
    ])

    apply(KF / '00-home-vault' / 'Indice-Global.md', [
        ('- Arquivos Markdown em `domains/`: **3940** (100 sementes legadas + 3840 notas autorais substantivas).',
         '- Arquivos Markdown em `domains/`: **4040** (100 sementes legadas + 3940 notas autorais substantivas).'),
        ('- Candidatas aprovadas no gate automatizado: **3840**; revisões humanas registradas: **49**; revisões factuais por IA: **3791**; 100 sementes legadas mantêm pendências.',
         '- Candidatas aprovadas no gate automatizado: **3940**; revisões humanas registradas: **49**; revisões factuais por IA: **3891**; 100 sementes legadas mantêm pendências.'),
        ('- Os lotes atuais totalizam 3840 notas válidas pelo protocolo; o segundo lote [`software-devops-2000-0002`](../exports/batches/software-devops-2000-0002.md) tem 1800/2.000 ([tranche 18](../exports/reports/ai-review-software-devops-2000-0002-tranche-18.md), [reconciliação da tranche 18](../exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-18.md) e [[MOC-DevOps-Software-0008]]),',
         '- Os lotes atuais totalizam 3940 notas válidas pelo protocolo; o segundo lote [`software-devops-2000-0002`](../exports/batches/software-devops-2000-0002.md) tem 1900/2.000 ([tranche 19](../exports/reports/ai-review-software-devops-2000-0002-tranche-19.md), [reconciliação da tranche 19](../exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-19.md) e [[MOC-DevOps-Software-0008]]),'),
    ])
    print("reconciliação concluída")


if __name__ == "__main__":
    main()
