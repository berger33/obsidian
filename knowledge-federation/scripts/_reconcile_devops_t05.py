#!/usr/bin/env python3
"""Reconcile batch software-devops-2000-0002 tranche 5 (IDs 401-500) across manifest, MOC, review registry and status docs."""
from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KF = ROOT / "knowledge-federation"
SCRIPTS = KF / "scripts"
BATCH_ID = "software-devops-2000-0002"
REPORT_NAME = "ai-review-software-devops-2000-0002-tranche-05.md"
RECON_NAME = "batch-reconciliation-software-devops-2000-0002-tranche-05.md"
DATE = "2026-10-03"


def load_builder():
    spec = importlib.util.spec_from_file_location("bd05", SCRIPTS / "_build_devops_t05.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_groups(bd05):
    groups = []
    for path in sorted(bd05.DATA_DIR.glob("*.txt")):
        context, rows = bd05.parse_group(path)
        groups.append((context, rows))
    return groups


def manifest_section(groups) -> str:
    lines = [
        "## Tranche 5 — Grafana Tempo, VictoriaMetrics, Backstage, KubeVirt, MetalLB, Strimzi, Knative Serving, SPIFFE/SPIRE, Dapr e OpenFeature (100 notas; revisão factual por IA registrada)",
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
        "## Tranche 5 — Grafana Tempo, VictoriaMetrics, Backstage, KubeVirt, MetalLB, Strimzi, Knative Serving, SPIFFE/SPIRE, Dapr e OpenFeature",
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
    bd05 = load_builder()
    groups = load_groups(bd05)
    total = sum(len(rows) for _, rows in groups)
    if total != 100 or int(groups[0][0]["first"]) != 401 or int(groups[-1][0]["first"]) != 491:
        raise SystemExit(f"dados inesperados: {total} notas, primeiro grupo em {groups[0][0]['first']}")

    manifest = KF / "exports" / "batches" / f"{BATCH_ID}.md"
    moc = KF / "00-home-vault" / "MOCs" / "MOC-DevOps-Software-0008.md"
    queue = KF / "exports" / "reports" / "human-review-queue.md"

    insert_before(manifest, "## Critérios e próximo passo", manifest_section(groups))
    insert_before(moc, "## Estado editorial", moc_section(groups))
    insert_before(queue, "## Regra de contagem", review_rows(groups))

    apply(manifest, [
        ('- Notas efetivamente redigidas até agora: **400 / 2.000 (20,00%)**',
         '- Notas efetivamente redigidas até agora: **500 / 2.000 (25,00%)**'),
        ('- Gate automatizado: **400/400 aprovadas** (conteúdo mínimo, seções, fontes específicas e wikilinks; reexecutado após a tranche 4)',
         '- Gate automatizado: **500/500 aprovadas** (conteúdo mínimo, seções, fontes específicas e wikilinks; reexecutado após a tranche 5)'),
        ('- Revisão factual humana: **0/400**',
         '- Revisão factual humana: **0/500**'),
        ('- Revisão factual por IA: **400/400**',
         '- Revisão factual por IA: **500/500**'),
        ('- Contabilizadas como válidas: **400/400**',
         '- Contabilizadas como válidas: **500/500**'),
        ('- Revisor das 400 notas aprovadas por IA: `Arena.ai Agent Mode`, com relatórios específicos; não são aprovações humanas',
         '- Revisor das 500 notas aprovadas por IA: `Arena.ai Agent Mode`, com relatórios específicos; não são aprovações humanas'),
        ('- Status do lote maior: `in_progress`; tranches 1–4 (400 notas, IDs 1–400) foram conferidas factualmente por IA e aprovadas sob o protocolo atualizado',
         '- Status do lote maior: `in_progress`; tranches 1–5 (500 notas, IDs 1–500) foram conferidas factualmente por IA e aprovadas sob o protocolo atualizado'),
        ('- Reconciliação estrutural mais recente do manifesto/fila: [`batch-reconciliation-software-devops-2000-0002-tranche-04.md`](../reports/batch-reconciliation-software-devops-2000-0002-tranche-04.md)',
         '- Reconciliação estrutural mais recente do manifesto/fila: [`batch-reconciliation-software-devops-2000-0002-tranche-05.md`](../reports/batch-reconciliation-software-devops-2000-0002-tranche-05.md)'),
        ('- Relatórios factuais por IA: [`tranche 1`](../reports/ai-review-software-devops-2000-0002-tranche-01.md), [`tranche 2`](../reports/ai-review-software-devops-2000-0002-tranche-02.md), [`tranche 3`](../reports/ai-review-software-devops-2000-0002-tranche-03.md), [`tranche 4`](../reports/ai-review-software-devops-2000-0002-tranche-04.md)',
         '- Relatórios factuais por IA: [`tranche 1`](../reports/ai-review-software-devops-2000-0002-tranche-01.md), [`tranche 2`](../reports/ai-review-software-devops-2000-0002-tranche-02.md), [`tranche 3`](../reports/ai-review-software-devops-2000-0002-tranche-03.md), [`tranche 4`](../reports/ai-review-software-devops-2000-0002-tranche-04.md), [`tranche 5`](../reports/ai-review-software-devops-2000-0002-tranche-05.md)'),
        ('Existem 400 notas materiais listadas abaixo; não há IDs reservados, placeholders ou registros virtuais para as 1600 restantes.',
         'Existem 500 notas materiais listadas abaixo; não há IDs reservados, placeholders ou registros virtuais para as 1500 restantes.'),
        ('As 400 notas 1–400 das tranches 1–4 têm revisão factual por IA registrada nos relatórios vinculados. O lote continua incompleto: são 400/2.000 notas válidas, restando 1600 notas materiais.',
         'As 500 notas 1–500 das tranches 1–5 têm revisão factual por IA registrada nos relatórios vinculados. O lote continua incompleto: são 500/2.000 notas válidas, restando 1500 notas materiais.'),
    ])

    apply(moc, [
        ('Índice das 400 notas substantivas redigidas até agora no lote `software-devops-2000-0002`, cuja meta é 2.000. As 400 passaram pelo gate automatizado',
         'Índice das 500 notas substantivas redigidas até agora no lote `software-devops-2000-0002`, cuja meta é 2.000. As 500 passaram pelo gate automatizado'),
        ('O gate automatizado foi aprovado por 400/400 notas e as 400 contam como válidas pelo protocolo atualizado, com revisão factual por IA registrada separadamente. O lote de 2.000 continua `in_progress` (400 notas substantivas; 1600 ainda não produzidas). Consulte o [manifesto](../../exports/batches/software-devops-2000-0002.md), a [auditoria de qualidade](../../exports/reports/note-quality-software-devops-2000-0002.md) e a [reconciliação mais recente do manifesto/fila](../../exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-04.md). Os relatórios factuais por IA são [tranche 1](../../exports/reports/ai-review-software-devops-2000-0002-tranche-01.md), [tranche 2](../../exports/reports/ai-review-software-devops-2000-0002-tranche-02.md), [tranche 3](../../exports/reports/ai-review-software-devops-2000-0002-tranche-03.md) e [tranche 4](../../exports/reports/ai-review-software-devops-2000-0002-tranche-04.md).',
         'O gate automatizado foi aprovado por 500/500 notas e as 500 contam como válidas pelo protocolo atualizado, com revisão factual por IA registrada separadamente. O lote de 2.000 continua `in_progress` (500 notas substantivas; 1500 ainda não produzidas). Consulte o [manifesto](../../exports/batches/software-devops-2000-0002.md), a [auditoria de qualidade](../../exports/reports/note-quality-software-devops-2000-0002.md) e a [reconciliação mais recente do manifesto/fila](../../exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-05.md). Os relatórios factuais por IA são [tranche 1](../../exports/reports/ai-review-software-devops-2000-0002-tranche-01.md), [tranche 2](../../exports/reports/ai-review-software-devops-2000-0002-tranche-02.md), [tranche 3](../../exports/reports/ai-review-software-devops-2000-0002-tranche-03.md), [tranche 4](../../exports/reports/ai-review-software-devops-2000-0002-tranche-04.md) e [tranche 5](../../exports/reports/ai-review-software-devops-2000-0002-tranche-05.md).'),
    ])

    apply(queue, [
        ('distingue 2391 revisões factuais realizadas por IA nos lotes `software-testes-2000-0001` (1991) e `software-devops-2000-0002` (400)',
         'distingue 2491 revisões factuais realizadas por IA nos lotes `software-testes-2000-0001` (1991) e `software-devops-2000-0002` (500)'),
        ('- Aprovações por IA registradas separadamente: **2391**.',
         '- Aprovações por IA registradas separadamente: **2491**.'),
        ('- Notas válidas contabilizadas (gate + revisão humana ou IA): **2440**.',
         '- Notas válidas contabilizadas (gate + revisão humana ou IA): **2540**.'),
        ('As 2391 linhas `APROVADA POR IA` (nº 50–2440) correspondem às 1991 notas 10–2000 das tranches 2–26 do lote `software-testes-2000-0001` e às 400 notas 1–400 das tranches 1–4 do lote `software-devops-2000-0002`',
         'As 2491 linhas `APROVADA POR IA` (nº 50–2540) correspondem às 1991 notas 10–2000 das tranches 2–26 do lote `software-testes-2000-0001` e às 500 notas 1–500 das tranches 1–5 do lote `software-devops-2000-0002`'),
    ])

    apply(ROOT / 'README.md', [
        ('| Notas válidas contabilizadas | 2440 / 1.000.000 (0,2440%) | 49 com aprovação humana histórica + 2391 com revisão factual por IA |',
         '| Notas válidas contabilizadas | 2540 / 1.000.000 (0,2540%) | 49 com aprovação humana histórica + 2491 com revisão factual por IA |'),
        ('| Notas com revisão factual por IA registrada | 2391 | Revisões dos lotes de escala (1991 no lote 1 + 400 no lote 2), com relatórios por tranche; não são humanas |',
         '| Notas com revisão factual por IA registrada | 2491 | Revisões dos lotes de escala (1991 no lote 1 + 500 no lote 2), com relatórios por tranche; não são humanas |'),
        ('| Segundo lote `software-devops-2000-0002` | 400 / 2.000 (20,00%) | 400 aprovadas por IA nas tranches 1–4; faltam 1600 notas substantivas |',
         '| Segundo lote `software-devops-2000-0002` | 500 / 2.000 (25,00%) | 500 aprovadas por IA nas tranches 1–5; faltam 1500 notas substantivas |'),
        ('| Arquivos Markdown ativos em `knowledge-federation/domains/` | 2540 | 100 notas legadas com pendências + 2440 notas autorais substantivas |',
         '| Arquivos Markdown ativos em `knowledge-federation/domains/` | 2640 | 100 notas legadas com pendências + 2540 notas autorais substantivas |'),
        ('400 notas materiais já passaram pelo gate e revisão factual por IA até a [tranche 4](knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-04.md) ([reconciliação](knowledge-federation/exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-04.md), [auditoria do lote](knowledge-federation/exports/reports/note-quality-software-devops-2000-0002.md) e [MOC de DevOps](knowledge-federation/00-home-vault/MOCs/MOC-DevOps-Software-0008.md)), com meta de 2.000.',
         '500 notas materiais já passaram pelo gate e revisão factual por IA até a [tranche 5](knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-05.md) ([reconciliação](knowledge-federation/exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-05.md), [auditoria do lote](knowledge-federation/exports/reports/note-quality-software-devops-2000-0002.md) e [MOC de DevOps](knowledge-federation/00-home-vault/MOCs/MOC-DevOps-Software-0008.md)), com meta de 2.000.'),
    ])

    apply(KF / 'README.md', [
        ('- Arquivos Markdown ativos: **2540** (100 notas legadas com pendências + 2440 notas autorais substantivas).',
         '- Arquivos Markdown ativos: **2640** (100 notas legadas com pendências + 2540 notas autorais substantivas).'),
        ('- Notas válidas pelo protocolo atual: **2440** (49 aprovações humanas históricas + 2391 revisões factuais por IA).',
         '- Notas válidas pelo protocolo atual: **2540** (49 aprovações humanas históricas + 2491 revisões factuais por IA).'),
        ('- Progresso: **2440 / 1.000.000 (0,2440%)**; faltam 997.560 notas válidas.',
         '- Progresso: **2540 / 1.000.000 (0,2540%)**; faltam 997.460 notas válidas.'),
        ('- Segundo lote em andamento `software-devops-2000-0002`: **400 / 2.000** notas válidas (20,00%); 400 por IA ([tranche 4](exports/reports/ai-review-software-devops-2000-0002-tranche-04.md) e [reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-04.md)); faltam 1600 notas materiais.',
         '- Segundo lote em andamento `software-devops-2000-0002`: **500 / 2.000** notas válidas (25,00%); 500 por IA ([tranche 5](exports/reports/ai-review-software-devops-2000-0002-tranche-05.md) e [reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-05.md)); faltam 1500 notas materiais.'),
    ])

    apply(KF / 'README-1M.md', [
        ('tem 2440 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 2391 revisões factuais por IA registradas separadamente). O diretório ativo tem 2540 arquivos Markdown, incluindo 100 notas legadas com pendências, ainda excluídas da contagem. O segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) está em andamento com 400/2.000 notas válidas ([relatório factual por IA da tranche 4](exports/reports/ai-review-software-devops-2000-0002-tranche-04.md) e [reconciliação da tranche 4](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-04.md)),',
         'tem 2540 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 2491 revisões factuais por IA registradas separadamente). O diretório ativo tem 2640 arquivos Markdown, incluindo 100 notas legadas com pendências, ainda excluídas da contagem. O segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) está em andamento com 500/2.000 notas válidas ([relatório factual por IA da tranche 5](exports/reports/ai-review-software-devops-2000-0002-tranche-05.md) e [reconciliação da tranche 5](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-05.md)),'),
    ])

    apply(KF / 'STATUS-CONSOLIDACAO-1M.md', [
        ('A auditoria encontrou 2540 arquivos Markdown ativos: 2440 notas substantivas passaram pelo gate e receberam revisão factual registrada (49 humanas históricas + 2391 por IA)',
         'A auditoria encontrou 2640 arquivos Markdown ativos: 2540 notas substantivas passaram pelo gate e receberam revisão factual registrada (49 humanas históricas + 2491 por IA)'),
        ('| Progresso válido global | 2440 / 1.000.000 (0,2440%) | 49 revisões humanas históricas + 2391 revisões por IA registradas separadamente |',
         '| Progresso válido global | 2540 / 1.000.000 (0,2540%) | 49 revisões humanas históricas + 2491 revisões por IA registradas separadamente |'),
        ('| Revisões factuais por IA registradas | 2391 | Relatórios das tranches 2–26 (`software-testes-2000-0001`) e tranches 1–4 (`software-devops-2000-0002`); não são humanas |',
         '| Revisões factuais por IA registradas | 2491 | Relatórios das tranches 2–26 (`software-testes-2000-0001`) e tranches 1–5 (`software-devops-2000-0002`); não são humanas |'),
        ('| Segundo lote (`software-devops-2000-0002`) | 400 / 2.000 (20,00%) | 400 IA nas tranches 1–4 ([tranche 4](exports/reports/ai-review-software-devops-2000-0002-tranche-04.md)); faltam 1600 notas substantivas |',
         '| Segundo lote (`software-devops-2000-0002`) | 500 / 2.000 (25,00%) | 500 IA nas tranches 1–5 ([tranche 5](exports/reports/ai-review-software-devops-2000-0002-tranche-05.md)); faltam 1500 notas substantivas |'),
        ('| Candidatas que passaram pelo gate automatizado | 2440 |',
         '| Candidatas que passaram pelo gate automatizado | 2540 |'),
        ('O segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) está em 400/2.000 notas válidas após a [tranche 4](exports/reports/ai-review-software-devops-2000-0002-tranche-04.md) ([reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-04.md)).',
         'O segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) está em 500/2.000 notas válidas após a [tranche 5](exports/reports/ai-review-software-devops-2000-0002-tranche-05.md) ([reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-05.md)).'),
        ('3. Continuar o segundo lote `software-devops-2000-0002` (atualmente em 400/2.000; faltam 1600 notas substantivas) e os 498 lotes subsequentes,',
         '3. Continuar o segundo lote `software-devops-2000-0002` (atualmente em 500/2.000; faltam 1500 notas substantivas) e os 498 lotes subsequentes,'),
    ])

    apply(KF / 'PLANO-CONTINUO-1M.md', [
        ('- Notas válidas globais: **2440** (49 aprovações humanas históricas + 2391 revisões factuais por IA).',
         '- Notas válidas globais: **2540** (49 aprovações humanas históricas + 2491 revisões factuais por IA).'),
        ('- Progresso: **2440 / 1.000.000 (0,2440%)**; faltam **997.560** notas válidas.',
         '- Progresso: **2540 / 1.000.000 (0,2540%)**; faltam **997.460** notas válidas.'),
        ('- Segundo lote atual `software-devops-2000-0002`: **400 / 2.000 (20,00%)** notas válidas (400 IA nas tranches 1–4); faltam **1600** notas substantivas.',
         '- Segundo lote atual `software-devops-2000-0002`: **500 / 2.000 (25,00%)** notas válidas (500 IA nas tranches 1–5); faltam **1500** notas substantivas.'),
        ('- Arquivos Markdown ativos: **2540**; 100 com pendências de qualidade, excluídos da contagem.',
         '- Arquivos Markdown ativos: **2640**; 100 com pendências de qualidade, excluídos da contagem.'),
        ('| 5 | Rodar gate, testes, auditorias e diff | **Concluído para o estado atual** | Lote 1: 2000/2000 (`complete`). Lote 2 (`software-devops-2000-0002`): 400/400 no gate (400 IA). Global: 2540 arquivos, 2440 válidas, 100 com pendências legadas; veja a [reconciliação da tranche 4 do lote 2](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-04.md). |',
         '| 5 | Rodar gate, testes, auditorias e diff | **Concluído para o estado atual** | Lote 1: 2000/2000 (`complete`). Lote 2 (`software-devops-2000-0002`): 500/500 no gate (500 IA). Global: 2640 arquivos, 2540 válidas, 100 com pendências legadas; veja a [reconciliação da tranche 5 do lote 2](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-05.md). |'),
        ('| 8 | Abrir lotes subsequentes de 2.000 notas | **Em andamento (lote 2 em 20%)** | Segundo lote `software-devops-2000-0002` com 400/2.000 notas válidas nas tranches 1–4; restam 1600 notas neste lote e 498 lotes subsequentes. |',
         '| 8 | Abrir lotes subsequentes de 2.000 notas | **Em andamento (lote 2 em 25%)** | Segundo lote `software-devops-2000-0002` com 500/2.000 notas válidas nas tranches 1–5; restam 1500 notas neste lote e 498 lotes subsequentes. |'),
        ('Progresso atual: 2440 notas válidas, 1/500 lotes completos.',
         'Progresso atual: 2540 notas válidas, 1/500 lotes completos.'),
    ])

    apply(KF / 'RECOVERY-AND-SCALE-NOTE.md', [
        ('há 2540 arquivos: 100 legados com pendências e 2440 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 2391 revisões por IA). O primeiro lote `software-testes-2000-0001` atingiu 2000/2.000 notas válidas (9 humanas + 1991 IA), com status `complete` ([tranche 26](exports/reports/ai-review-software-testes-2000-0001-tranche-26.md) e [reconciliação](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-26.md)); o segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) está em andamento (`in_progress`) com 400/2.000 notas válidas revisadas por IA até a [tranche 4](exports/reports/ai-review-software-devops-2000-0002-tranche-04.md), com [reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-04.md);',
         'há 2640 arquivos: 100 legados com pendências e 2540 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 2491 revisões por IA). O primeiro lote `software-testes-2000-0001` atingiu 2000/2.000 notas válidas (9 humanas + 1991 IA), com status `complete` ([tranche 26](exports/reports/ai-review-software-testes-2000-0001-tranche-26.md) e [reconciliação](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-26.md)); o segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) está em andamento (`in_progress`) com 500/2.000 notas válidas revisadas por IA até a [tranche 5](exports/reports/ai-review-software-devops-2000-0002-tranche-05.md), com [reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-05.md);'),
        ('4. Continuar o segundo lote `software-devops-2000-0002` (400/2.000; faltam 1600 notas qualificadas) até 2.000 antes de abrir os 498 lotes seguintes.',
         '4. Continuar o segundo lote `software-devops-2000-0002` (500/2.000; faltam 1500 notas qualificadas) até 2.000 antes de abrir os 498 lotes seguintes.'),
    ])

    apply(KF / '00-home-vault' / 'Home.md', [
        ('- [[MOC-DevOps-Software-0008]] — 400 notas do segundo lote de escala `software-devops-2000-0002` (meta: 2.000); 400 revisões factuais por IA.',
         '- [[MOC-DevOps-Software-0008]] — 500 notas do segundo lote de escala `software-devops-2000-0002` (meta: 2.000); 500 revisões factuais por IA.'),
        ('[[human-review-queue|Registro de revisões factuais]] — 49 aprovações humanas e 2391 aprovações por IA, identificadas separadamente.',
         '[[human-review-queue|Registro de revisões factuais]] — 49 aprovações humanas e 2491 aprovações por IA, identificadas separadamente.'),
        ('[[note-quality-audit|Auditoria de qualidade]] — 2440 notas válidas pelo protocolo atual (49 humanas + 2391 IA) e 100 notas legadas com falhas.',
         '[[note-quality-audit|Auditoria de qualidade]] — 2540 notas válidas pelo protocolo atual (49 humanas + 2491 IA) e 100 notas legadas com falhas.'),
    ])

    apply(KF / '00-home-vault' / 'Indice-Global.md', [
        ('- Arquivos Markdown em `domains/`: **2540** (100 sementes legadas + 2440 notas autorais substantivas).',
         '- Arquivos Markdown em `domains/`: **2640** (100 sementes legadas + 2540 notas autorais substantivas).'),
        ('- Candidatas aprovadas no gate automatizado: **2440**; revisões humanas registradas: **49**; revisões factuais por IA: **2391**; 100 sementes legadas mantêm pendências.',
         '- Candidatas aprovadas no gate automatizado: **2540**; revisões humanas registradas: **49**; revisões factuais por IA: **2491**; 100 sementes legadas mantêm pendências.'),
        ('- Os lotes atuais totalizam 2440 notas válidas pelo protocolo; o segundo lote [`software-devops-2000-0002`](../exports/batches/software-devops-2000-0002.md) tem 400/2.000 ([tranche 4](../exports/reports/ai-review-software-devops-2000-0002-tranche-04.md), [reconciliação da tranche 4](../exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-04.md) e [[MOC-DevOps-Software-0008]]),',
         '- Os lotes atuais totalizam 2540 notas válidas pelo protocolo; o segundo lote [`software-devops-2000-0002`](../exports/batches/software-devops-2000-0002.md) tem 500/2.000 ([tranche 5](../exports/reports/ai-review-software-devops-2000-0002-tranche-05.md), [reconciliação da tranche 5](../exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-05.md) e [[MOC-DevOps-Software-0008]]),'),
    ])
    print("reconciliação concluída")


if __name__ == "__main__":
    main()
