#!/usr/bin/env python3
"""Reconcile batch software-devops-2000-0002 tranche 12 (IDs 1101-1200) across manifest, MOC, review registry and status docs."""
from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KF = ROOT / "knowledge-federation"
SCRIPTS = KF / "scripts"
BATCH_ID = "software-devops-2000-0002"
REPORT_NAME = "ai-review-software-devops-2000-0002-tranche-12.md"
RECON_NAME = "batch-reconciliation-software-devops-2000-0002-tranche-12.md"
DATE = "2026-10-03"


def load_builder():
    spec = importlib.util.spec_from_file_location("bd12", SCRIPTS / "_build_devops_t12.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_groups(bd12):
    groups = []
    for path in sorted(bd12.DATA_DIR.glob("*.txt")):
        context, rows = bd12.parse_group(path)
        groups.append((context, rows))
    return groups


def manifest_section(groups) -> str:
    lines = [
        "## Tranche 12 — Kratix, Score, Jetify Devbox, direnv, Fairwinds Nova, Fairwinds RBAC Manager, Robusta, Botkube, Kured e just (100 notas; revisão factual por IA registrada)",
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
        "## Tranche 12 — Kratix, Score, Jetify Devbox, direnv, Fairwinds Nova, Fairwinds RBAC Manager, Robusta, Botkube, Kured e just",
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
    bd12 = load_builder()
    groups = load_groups(bd12)
    total = sum(len(rows) for _, rows in groups)
    if total != 100 or int(groups[0][0]["first"]) != 1101 or int(groups[-1][0]["first"]) != 1191:
        raise SystemExit(f"dados inesperados: {total} notas, primeiro grupo em {groups[0][0]['first']}")

    manifest = KF / "exports" / "batches" / f"{BATCH_ID}.md"
    moc = KF / "00-home-vault" / "MOCs" / "MOC-DevOps-Software-0008.md"
    queue = KF / "exports" / "reports" / "human-review-queue.md"

    insert_before(manifest, "## Critérios e próximo passo", manifest_section(groups))
    insert_before(moc, "## Estado editorial", moc_section(groups))
    insert_before(queue, "## Regra de contagem", review_rows(groups))

    apply(manifest, [
        ('- Notas efetivamente redigidas até agora: **1100 / 2.000 (55,00%)**',
         '- Notas efetivamente redigidas até agora: **1200 / 2.000 (60,00%)**'),
        ('- Gate automatizado: **1100/1100 aprovadas** (conteúdo mínimo, seções, fontes específicas e wikilinks; reexecutado após a tranche 11)',
         '- Gate automatizado: **1200/1200 aprovadas** (conteúdo mínimo, seções, fontes específicas e wikilinks; reexecutado após a tranche 12)'),
        ('- Revisão factual humana: **0/1100**',
         '- Revisão factual humana: **0/1200**'),
        ('- Revisão factual por IA: **1100/1100**',
         '- Revisão factual por IA: **1200/1200**'),
        ('- Contabilizadas como válidas: **1100/1100**',
         '- Contabilizadas como válidas: **1200/1200**'),
        ('- Revisor das 1100 notas aprovadas por IA: `Arena.ai Agent Mode`, com relatórios específicos; não são aprovações humanas',
         '- Revisor das 1200 notas aprovadas por IA: `Arena.ai Agent Mode`, com relatórios específicos; não são aprovações humanas'),
        ('- Status do lote maior: `in_progress`; tranches 1–11 (1100 notas, IDs 1–1100) foram conferidas factualmente por IA e aprovadas sob o protocolo atualizado',
         '- Status do lote maior: `in_progress`; tranches 1–12 (1200 notas, IDs 1–1200) foram conferidas factualmente por IA e aprovadas sob o protocolo atualizado'),
        ('- Reconciliação estrutural mais recente do manifesto/fila: [`batch-reconciliation-software-devops-2000-0002-tranche-11.md`](../reports/batch-reconciliation-software-devops-2000-0002-tranche-11.md)',
         '- Reconciliação estrutural mais recente do manifesto/fila: [`batch-reconciliation-software-devops-2000-0002-tranche-12.md`](../reports/batch-reconciliation-software-devops-2000-0002-tranche-12.md)'),
        ('- Relatórios factuais por IA: [`tranche 1`](../reports/ai-review-software-devops-2000-0002-tranche-01.md), [`tranche 2`](../reports/ai-review-software-devops-2000-0002-tranche-02.md), [`tranche 3`](../reports/ai-review-software-devops-2000-0002-tranche-03.md), [`tranche 4`](../reports/ai-review-software-devops-2000-0002-tranche-04.md), [`tranche 5`](../reports/ai-review-software-devops-2000-0002-tranche-05.md), [`tranche 6`](../reports/ai-review-software-devops-2000-0002-tranche-06.md), [`tranche 7`](../reports/ai-review-software-devops-2000-0002-tranche-07.md), [`tranche 8`](../reports/ai-review-software-devops-2000-0002-tranche-08.md), [`tranche 9`](../reports/ai-review-software-devops-2000-0002-tranche-09.md), [`tranche 10`](../reports/ai-review-software-devops-2000-0002-tranche-10.md), [`tranche 11`](../reports/ai-review-software-devops-2000-0002-tranche-11.md)',
         '- Relatórios factuais por IA: [`tranche 1`](../reports/ai-review-software-devops-2000-0002-tranche-01.md), [`tranche 2`](../reports/ai-review-software-devops-2000-0002-tranche-02.md), [`tranche 3`](../reports/ai-review-software-devops-2000-0002-tranche-03.md), [`tranche 4`](../reports/ai-review-software-devops-2000-0002-tranche-04.md), [`tranche 5`](../reports/ai-review-software-devops-2000-0002-tranche-05.md), [`tranche 6`](../reports/ai-review-software-devops-2000-0002-tranche-06.md), [`tranche 7`](../reports/ai-review-software-devops-2000-0002-tranche-07.md), [`tranche 8`](../reports/ai-review-software-devops-2000-0002-tranche-08.md), [`tranche 9`](../reports/ai-review-software-devops-2000-0002-tranche-09.md), [`tranche 10`](../reports/ai-review-software-devops-2000-0002-tranche-10.md), [`tranche 11`](../reports/ai-review-software-devops-2000-0002-tranche-11.md), [`tranche 12`](../reports/ai-review-software-devops-2000-0002-tranche-12.md)'),
        ('Existem 1100 notas materiais listadas abaixo; não há IDs reservados, placeholders ou registros virtuais para as 900 restantes.',
         'Existem 1200 notas materiais listadas abaixo; não há IDs reservados, placeholders ou registros virtuais para as 800 restantes.'),
        ('As 1100 notas 1–1100 das tranches 1–11 têm revisão factual por IA registrada nos relatórios vinculados. O lote continua incompleto: são 1100/2.000 notas válidas, restando 900 notas materiais.',
         'As 1200 notas 1–1200 das tranches 1–12 têm revisão factual por IA registrada nos relatórios vinculados. O lote continua incompleto: são 1200/2.000 notas válidas, restando 800 notas materiais.'),
    ])

    apply(moc, [
        ('Índice das 1100 notas substantivas redigidas até agora no lote `software-devops-2000-0002`, cuja meta é 2.000. As 1100 passaram pelo gate automatizado',
         'Índice das 1200 notas substantivas redigidas até agora no lote `software-devops-2000-0002`, cuja meta é 2.000. As 1200 passaram pelo gate automatizado'),
        ('O gate automatizado foi aprovado por 1100/1100 notas e as 1100 contam como válidas pelo protocolo atualizado, com revisão factual por IA registrada separadamente. O lote de 2.000 continua `in_progress` (1100 notas substantivas; 900 ainda não produzidas). Consulte o [manifesto](../../exports/batches/software-devops-2000-0002.md), a [auditoria de qualidade](../../exports/reports/note-quality-software-devops-2000-0002.md) e a [reconciliação mais recente do manifesto/fila](../../exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-11.md). Os relatórios factuais por IA são [tranche 1](../../exports/reports/ai-review-software-devops-2000-0002-tranche-01.md), [tranche 2](../../exports/reports/ai-review-software-devops-2000-0002-tranche-02.md), [tranche 3](../../exports/reports/ai-review-software-devops-2000-0002-tranche-03.md), [tranche 4](../../exports/reports/ai-review-software-devops-2000-0002-tranche-04.md), [tranche 5](../../exports/reports/ai-review-software-devops-2000-0002-tranche-05.md), [tranche 6](../../exports/reports/ai-review-software-devops-2000-0002-tranche-06.md), [tranche 7](../../exports/reports/ai-review-software-devops-2000-0002-tranche-07.md), [tranche 8](../../exports/reports/ai-review-software-devops-2000-0002-tranche-08.md), [tranche 9](../../exports/reports/ai-review-software-devops-2000-0002-tranche-09.md), [tranche 10](../../exports/reports/ai-review-software-devops-2000-0002-tranche-10.md) e [tranche 11](../../exports/reports/ai-review-software-devops-2000-0002-tranche-11.md).',
         'O gate automatizado foi aprovado por 1200/1200 notas e as 1200 contam como válidas pelo protocolo atualizado, com revisão factual por IA registrada separadamente. O lote de 2.000 continua `in_progress` (1200 notas substantivas; 800 ainda não produzidas). Consulte o [manifesto](../../exports/batches/software-devops-2000-0002.md), a [auditoria de qualidade](../../exports/reports/note-quality-software-devops-2000-0002.md) e a [reconciliação mais recente do manifesto/fila](../../exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-12.md). Os relatórios factuais por IA são [tranche 1](../../exports/reports/ai-review-software-devops-2000-0002-tranche-01.md), [tranche 2](../../exports/reports/ai-review-software-devops-2000-0002-tranche-02.md), [tranche 3](../../exports/reports/ai-review-software-devops-2000-0002-tranche-03.md), [tranche 4](../../exports/reports/ai-review-software-devops-2000-0002-tranche-04.md), [tranche 5](../../exports/reports/ai-review-software-devops-2000-0002-tranche-05.md), [tranche 6](../../exports/reports/ai-review-software-devops-2000-0002-tranche-06.md), [tranche 7](../../exports/reports/ai-review-software-devops-2000-0002-tranche-07.md), [tranche 8](../../exports/reports/ai-review-software-devops-2000-0002-tranche-08.md), [tranche 9](../../exports/reports/ai-review-software-devops-2000-0002-tranche-09.md), [tranche 10](../../exports/reports/ai-review-software-devops-2000-0002-tranche-10.md), [tranche 11](../../exports/reports/ai-review-software-devops-2000-0002-tranche-11.md) e [tranche 12](../../exports/reports/ai-review-software-devops-2000-0002-tranche-12.md).'),
    ])

    apply(queue, [
        ('distingue 3091 revisões factuais realizadas por IA nos lotes `software-testes-2000-0001` (1991) e `software-devops-2000-0002` (1100)',
         'distingue 3191 revisões factuais realizadas por IA nos lotes `software-testes-2000-0001` (1991) e `software-devops-2000-0002` (1200)'),
        ('- Aprovações por IA registradas separadamente: **3091**.',
         '- Aprovações por IA registradas separadamente: **3191**.'),
        ('- Notas válidas contabilizadas (gate + revisão humana ou IA): **3140**.',
         '- Notas válidas contabilizadas (gate + revisão humana ou IA): **3240**.'),
        ('As 3091 linhas `APROVADA POR IA` (nº 50–3140) correspondem às 1991 notas 10–2000 das tranches 2–26 do lote `software-testes-2000-0001` e às 1100 notas 1–1100 das tranches 1–11 do lote `software-devops-2000-0002`',
         'As 3191 linhas `APROVADA POR IA` (nº 50–3240) correspondem às 1991 notas 10–2000 das tranches 2–26 do lote `software-testes-2000-0001` e às 1200 notas 1–1200 das tranches 1–12 do lote `software-devops-2000-0002`'),
    ])

    apply(ROOT / 'README.md', [
        ('| Notas válidas contabilizadas | 3140 / 1.000.000 (0,3140%) | 49 com aprovação humana histórica + 3091 com revisão factual por IA |',
         '| Notas válidas contabilizadas | 3240 / 1.000.000 (0,3240%) | 49 com aprovação humana histórica + 3191 com revisão factual por IA |'),
        ('| Notas com revisão factual por IA registrada | 3091 | Revisões dos lotes de escala (1991 no lote 1 + 1100 no lote 2), com relatórios por tranche; não são humanas |',
         '| Notas com revisão factual por IA registrada | 3191 | Revisões dos lotes de escala (1991 no lote 1 + 1200 no lote 2), com relatórios por tranche; não são humanas |'),
        ('| Segundo lote `software-devops-2000-0002` | 1100 / 2.000 (55,00%) | 1100 aprovadas por IA nas tranches 1–11; faltam 900 notas substantivas |',
         '| Segundo lote `software-devops-2000-0002` | 1200 / 2.000 (60,00%) | 1200 aprovadas por IA nas tranches 1–12; faltam 800 notas substantivas |'),
        ('| Arquivos Markdown ativos em `knowledge-federation/domains/` | 3240 | 100 notas legadas com pendências + 3140 notas autorais substantivas |',
         '| Arquivos Markdown ativos em `knowledge-federation/domains/` | 3340 | 100 notas legadas com pendências + 3240 notas autorais substantivas |'),
        ('1100 notas materiais já passaram pelo gate e revisão factual por IA até a [tranche 11](knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-11.md) ([reconciliação](knowledge-federation/exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-11.md), [auditoria do lote](knowledge-federation/exports/reports/note-quality-software-devops-2000-0002.md) e [MOC de DevOps](knowledge-federation/00-home-vault/MOCs/MOC-DevOps-Software-0008.md)), com meta de 2.000.',
         '1200 notas materiais já passaram pelo gate e revisão factual por IA até a [tranche 12](knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-12.md) ([reconciliação](knowledge-federation/exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-12.md), [auditoria do lote](knowledge-federation/exports/reports/note-quality-software-devops-2000-0002.md) e [MOC de DevOps](knowledge-federation/00-home-vault/MOCs/MOC-DevOps-Software-0008.md)), com meta de 2.000.'),
    ])

    apply(KF / 'README.md', [
        ('- Arquivos Markdown ativos: **3240** (100 notas legadas com pendências + 3140 notas autorais substantivas).',
         '- Arquivos Markdown ativos: **3340** (100 notas legadas com pendências + 3240 notas autorais substantivas).'),
        ('- Notas válidas pelo protocolo atual: **3140** (49 aprovações humanas históricas + 3091 revisões factuais por IA).',
         '- Notas válidas pelo protocolo atual: **3240** (49 aprovações humanas históricas + 3191 revisões factuais por IA).'),
        ('- Progresso: **3140 / 1.000.000 (0,3140%)**; faltam 996.860 notas válidas.',
         '- Progresso: **3240 / 1.000.000 (0,3240%)**; faltam 996.760 notas válidas.'),
        ('- Segundo lote em andamento `software-devops-2000-0002`: **1100 / 2.000** notas válidas (55,00%); 1100 por IA ([tranche 11](exports/reports/ai-review-software-devops-2000-0002-tranche-11.md) e [reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-11.md)); faltam 900 notas materiais.',
         '- Segundo lote em andamento `software-devops-2000-0002`: **1200 / 2.000** notas válidas (60,00%); 1200 por IA ([tranche 12](exports/reports/ai-review-software-devops-2000-0002-tranche-12.md) e [reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-12.md)); faltam 800 notas materiais.'),
    ])

    apply(KF / 'README-1M.md', [
        ('tem 3140 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 3091 revisões factuais por IA registradas separadamente). O diretório ativo tem 3240 arquivos Markdown, incluindo 100 notas legadas com pendências, ainda excluídas da contagem. O segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) está em andamento com 1100/2.000 notas válidas ([relatório factual por IA da tranche 11](exports/reports/ai-review-software-devops-2000-0002-tranche-11.md) e [reconciliação da tranche 11](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-11.md)),',
         'tem 3240 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 3191 revisões factuais por IA registradas separadamente). O diretório ativo tem 3340 arquivos Markdown, incluindo 100 notas legadas com pendências, ainda excluídas da contagem. O segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) está em andamento com 1200/2.000 notas válidas ([relatório factual por IA da tranche 12](exports/reports/ai-review-software-devops-2000-0002-tranche-12.md) e [reconciliação da tranche 12](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-12.md)),'),
    ])

    apply(KF / 'STATUS-CONSOLIDACAO-1M.md', [
        ('A auditoria encontrou 3240 arquivos Markdown ativos: 3140 notas substantivas passaram pelo gate e receberam revisão factual registrada (49 humanas históricas + 3091 por IA)',
         'A auditoria encontrou 3340 arquivos Markdown ativos: 3240 notas substantivas passaram pelo gate e receberam revisão factual registrada (49 humanas históricas + 3191 por IA)'),
        ('| Progresso válido global | 3140 / 1.000.000 (0,3140%) | 49 revisões humanas históricas + 3091 revisões por IA registradas separadamente |',
         '| Progresso válido global | 3240 / 1.000.000 (0,3240%) | 49 revisões humanas históricas + 3191 revisões por IA registradas separadamente |'),
        ('| Revisões factuais por IA registradas | 3091 | Relatórios das tranches 2–26 (`software-testes-2000-0001`) e tranches 1–11 (`software-devops-2000-0002`); não são humanas |',
         '| Revisões factuais por IA registradas | 3191 | Relatórios das tranches 2–26 (`software-testes-2000-0001`) e tranches 1–12 (`software-devops-2000-0002`); não são humanas |'),
        ('| Segundo lote (`software-devops-2000-0002`) | 1100 / 2.000 (55,00%) | 1100 IA nas tranches 1–11 ([tranche 11](exports/reports/ai-review-software-devops-2000-0002-tranche-11.md)); faltam 900 notas substantivas |',
         '| Segundo lote (`software-devops-2000-0002`) | 1200 / 2.000 (60,00%) | 1200 IA nas tranches 1–12 ([tranche 12](exports/reports/ai-review-software-devops-2000-0002-tranche-12.md)); faltam 800 notas substantivas |'),
        ('| Candidatas que passaram pelo gate automatizado | 3140 |',
         '| Candidatas que passaram pelo gate automatizado | 3240 |'),
        ('O segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) está em 1100/2.000 notas válidas após a [tranche 11](exports/reports/ai-review-software-devops-2000-0002-tranche-11.md) ([reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-11.md)).',
         'O segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) está em 1200/2.000 notas válidas após a [tranche 12](exports/reports/ai-review-software-devops-2000-0002-tranche-12.md) ([reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-12.md)).'),
        ('3. Continuar o segundo lote `software-devops-2000-0002` (atualmente em 1100/2.000; faltam 900 notas substantivas) e os 498 lotes subsequentes,',
         '3. Continuar o segundo lote `software-devops-2000-0002` (atualmente em 1200/2.000; faltam 800 notas substantivas) e os 498 lotes subsequentes,'),
    ])

    apply(KF / 'PLANO-CONTINUO-1M.md', [
        ('- Notas válidas globais: **3140** (49 aprovações humanas históricas + 3091 revisões factuais por IA).',
         '- Notas válidas globais: **3240** (49 aprovações humanas históricas + 3191 revisões factuais por IA).'),
        ('- Progresso: **3140 / 1.000.000 (0,3140%)**; faltam **996.860** notas válidas.',
         '- Progresso: **3240 / 1.000.000 (0,3240%)**; faltam **996.760** notas válidas.'),
        ('- Segundo lote atual `software-devops-2000-0002`: **1100 / 2.000 (55,00%)** notas válidas (1100 IA nas tranches 1–11); faltam **900** notas substantivas.',
         '- Segundo lote atual `software-devops-2000-0002`: **1200 / 2.000 (60,00%)** notas válidas (1200 IA nas tranches 1–12); faltam **800** notas substantivas.'),
        ('- Arquivos Markdown ativos: **3240**; 100 com pendências de qualidade, excluídos da contagem.',
         '- Arquivos Markdown ativos: **3340**; 100 com pendências de qualidade, excluídos da contagem.'),
        ('| 5 | Rodar gate, testes, auditorias e diff | **Concluído para o estado atual** | Lote 1: 2000/2000 (`complete`). Lote 2 (`software-devops-2000-0002`): 1100/1100 no gate (1100 IA). Global: 3240 arquivos, 3140 válidas, 100 com pendências legadas; veja a [reconciliação da tranche 11 do lote 2](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-11.md). |',
         '| 5 | Rodar gate, testes, auditorias e diff | **Concluído para o estado atual** | Lote 1: 2000/2000 (`complete`). Lote 2 (`software-devops-2000-0002`): 1200/1200 no gate (1200 IA). Global: 3340 arquivos, 3240 válidas, 100 com pendências legadas; veja a [reconciliação da tranche 12 do lote 2](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-12.md). |'),
        ('| 8 | Abrir lotes subsequentes de 2.000 notas | **Em andamento (lote 2 em 55%)** | Segundo lote `software-devops-2000-0002` com 1100/2.000 notas válidas nas tranches 1–11; restam 900 notas neste lote e 498 lotes subsequentes. |',
         '| 8 | Abrir lotes subsequentes de 2.000 notas | **Em andamento (lote 2 em 60%)** | Segundo lote `software-devops-2000-0002` com 1200/2.000 notas válidas nas tranches 1–12; restam 800 notas neste lote e 498 lotes subsequentes. |'),
        ('Progresso atual: 3140 notas válidas, 1/500 lotes completos.',
         'Progresso atual: 3240 notas válidas, 1/500 lotes completos.'),
    ])

    apply(KF / 'RECOVERY-AND-SCALE-NOTE.md', [
        ('há 3240 arquivos: 100 legados com pendências e 3140 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 3091 revisões por IA). O primeiro lote `software-testes-2000-0001` atingiu 2000/2.000 notas válidas (9 humanas + 1991 IA), com status `complete` ([tranche 26](exports/reports/ai-review-software-testes-2000-0001-tranche-26.md) e [reconciliação](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-26.md)); o segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) está em andamento (`in_progress`) com 1100/2.000 notas válidas revisadas por IA até a [tranche 11](exports/reports/ai-review-software-devops-2000-0002-tranche-11.md), com [reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-11.md);',
         'há 3340 arquivos: 100 legados com pendências e 3240 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 3191 revisões por IA). O primeiro lote `software-testes-2000-0001` atingiu 2000/2.000 notas válidas (9 humanas + 1991 IA), com status `complete` ([tranche 26](exports/reports/ai-review-software-testes-2000-0001-tranche-26.md) e [reconciliação](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-26.md)); o segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) está em andamento (`in_progress`) com 1200/2.000 notas válidas revisadas por IA até a [tranche 12](exports/reports/ai-review-software-devops-2000-0002-tranche-12.md), com [reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-12.md);'),
        ('4. Continuar o segundo lote `software-devops-2000-0002` (1100/2.000; faltam 900 notas qualificadas) até 2.000 antes de abrir os 498 lotes seguintes.',
         '4. Continuar o segundo lote `software-devops-2000-0002` (1200/2.000; faltam 800 notas qualificadas) até 2.000 antes de abrir os 498 lotes seguintes.'),
    ])

    apply(KF / '00-home-vault' / 'Home.md', [
        ('- [[MOC-DevOps-Software-0008]] — 1100 notas do segundo lote de escala `software-devops-2000-0002` (meta: 2.000); 1100 revisões factuais por IA.',
         '- [[MOC-DevOps-Software-0008]] — 1200 notas do segundo lote de escala `software-devops-2000-0002` (meta: 2.000); 1200 revisões factuais por IA.'),
        ('[[human-review-queue|Registro de revisões factuais]] — 49 aprovações humanas e 3091 aprovações por IA, identificadas separadamente.',
         '[[human-review-queue|Registro de revisões factuais]] — 49 aprovações humanas e 3191 aprovações por IA, identificadas separadamente.'),
        ('[[note-quality-audit|Auditoria de qualidade]] — 3140 notas válidas pelo protocolo atual (49 humanas + 3091 IA) e 100 notas legadas com falhas.',
         '[[note-quality-audit|Auditoria de qualidade]] — 3240 notas válidas pelo protocolo atual (49 humanas + 3191 IA) e 100 notas legadas com falhas.'),
    ])

    apply(KF / '00-home-vault' / 'Indice-Global.md', [
        ('- Arquivos Markdown em `domains/`: **3240** (100 sementes legadas + 3140 notas autorais substantivas).',
         '- Arquivos Markdown em `domains/`: **3340** (100 sementes legadas + 3240 notas autorais substantivas).'),
        ('- Candidatas aprovadas no gate automatizado: **3140**; revisões humanas registradas: **49**; revisões factuais por IA: **3091**; 100 sementes legadas mantêm pendências.',
         '- Candidatas aprovadas no gate automatizado: **3240**; revisões humanas registradas: **49**; revisões factuais por IA: **3191**; 100 sementes legadas mantêm pendências.'),
        ('- Os lotes atuais totalizam 3140 notas válidas pelo protocolo; o segundo lote [`software-devops-2000-0002`](../exports/batches/software-devops-2000-0002.md) tem 1100/2.000 ([tranche 11](../exports/reports/ai-review-software-devops-2000-0002-tranche-11.md), [reconciliação da tranche 11](../exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-11.md) e [[MOC-DevOps-Software-0008]]),',
         '- Os lotes atuais totalizam 3240 notas válidas pelo protocolo; o segundo lote [`software-devops-2000-0002`](../exports/batches/software-devops-2000-0002.md) tem 1200/2.000 ([tranche 12](../exports/reports/ai-review-software-devops-2000-0002-tranche-12.md), [reconciliação da tranche 12](../exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-12.md) e [[MOC-DevOps-Software-0008]]),'),
    ])
    print("reconciliação concluída")


if __name__ == "__main__":
    main()
