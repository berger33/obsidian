#!/usr/bin/env python3
"""Reconcile batch software-devops-2000-0002 tranche 8 (IDs 701-800) across manifest, MOC, review registry and status docs."""
from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KF = ROOT / "knowledge-federation"
SCRIPTS = KF / "scripts"
BATCH_ID = "software-devops-2000-0002"
REPORT_NAME = "ai-review-software-devops-2000-0002-tranche-08.md"
RECON_NAME = "batch-reconciliation-software-devops-2000-0002-tranche-08.md"
DATE = "2026-10-03"


def load_builder():
    spec = importlib.util.spec_from_file_location("bd08", SCRIPTS / "_build_devops_t08.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_groups(bd08):
    groups = []
    for path in sorted(bd08.DATA_DIR.glob("*.txt")):
        context, rows = bd08.parse_group(path)
        groups.append((context, rows))
    return groups


def manifest_section(groups) -> str:
    lines = [
        "## Tranche 8 — Kata Containers, AWS Firecracker, Google gVisor, Youki, Liquibase, Redgate Flyway, Ariga Atlas, Bytebase, Nix e Earthly (100 notas; revisão factual por IA registrada)",
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
        "## Tranche 8 — Kata Containers, AWS Firecracker, Google gVisor, Youki, Liquibase, Redgate Flyway, Ariga Atlas, Bytebase, Nix e Earthly",
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
    bd08 = load_builder()
    groups = load_groups(bd08)
    total = sum(len(rows) for _, rows in groups)
    if total != 100 or int(groups[0][0]["first"]) != 701 or int(groups[-1][0]["first"]) != 791:
        raise SystemExit(f"dados inesperados: {total} notas, primeiro grupo em {groups[0][0]['first']}")

    manifest = KF / "exports" / "batches" / f"{BATCH_ID}.md"
    moc = KF / "00-home-vault" / "MOCs" / "MOC-DevOps-Software-0008.md"
    queue = KF / "exports" / "reports" / "human-review-queue.md"

    insert_before(manifest, "## Critérios e próximo passo", manifest_section(groups))
    insert_before(moc, "## Estado editorial", moc_section(groups))
    insert_before(queue, "## Regra de contagem", review_rows(groups))

    apply(manifest, [
        ('- Notas efetivamente redigidas até agora: **700 / 2.000 (35,00%)**',
         '- Notas efetivamente redigidas até agora: **800 / 2.000 (40,00%)**'),
        ('- Gate automatizado: **700/700 aprovadas** (conteúdo mínimo, seções, fontes específicas e wikilinks; reexecutado após a tranche 7)',
         '- Gate automatizado: **800/800 aprovadas** (conteúdo mínimo, seções, fontes específicas e wikilinks; reexecutado após a tranche 8)'),
        ('- Revisão factual humana: **0/700**',
         '- Revisão factual humana: **0/800**'),
        ('- Revisão factual por IA: **700/700**',
         '- Revisão factual por IA: **800/800**'),
        ('- Contabilizadas como válidas: **700/700**',
         '- Contabilizadas como válidas: **800/800**'),
        ('- Revisor das 700 notas aprovadas por IA: `Arena.ai Agent Mode`, com relatórios específicos; não são aprovações humanas',
         '- Revisor das 800 notas aprovadas por IA: `Arena.ai Agent Mode`, com relatórios específicos; não são aprovações humanas'),
        ('- Status do lote maior: `in_progress`; tranches 1–7 (700 notas, IDs 1–700) foram conferidas factualmente por IA e aprovadas sob o protocolo atualizado',
         '- Status do lote maior: `in_progress`; tranches 1–8 (800 notas, IDs 1–800) foram conferidas factualmente por IA e aprovadas sob o protocolo atualizado'),
        ('- Reconciliação estrutural mais recente do manifesto/fila: [`batch-reconciliation-software-devops-2000-0002-tranche-07.md`](../reports/batch-reconciliation-software-devops-2000-0002-tranche-07.md)',
         '- Reconciliação estrutural mais recente do manifesto/fila: [`batch-reconciliation-software-devops-2000-0002-tranche-08.md`](../reports/batch-reconciliation-software-devops-2000-0002-tranche-08.md)'),
        ('- Relatórios factuais por IA: [`tranche 1`](../reports/ai-review-software-devops-2000-0002-tranche-01.md), [`tranche 2`](../reports/ai-review-software-devops-2000-0002-tranche-02.md), [`tranche 3`](../reports/ai-review-software-devops-2000-0002-tranche-03.md), [`tranche 4`](../reports/ai-review-software-devops-2000-0002-tranche-04.md), [`tranche 5`](../reports/ai-review-software-devops-2000-0002-tranche-05.md), [`tranche 6`](../reports/ai-review-software-devops-2000-0002-tranche-06.md), [`tranche 7`](../reports/ai-review-software-devops-2000-0002-tranche-07.md)',
         '- Relatórios factuais por IA: [`tranche 1`](../reports/ai-review-software-devops-2000-0002-tranche-01.md), [`tranche 2`](../reports/ai-review-software-devops-2000-0002-tranche-02.md), [`tranche 3`](../reports/ai-review-software-devops-2000-0002-tranche-03.md), [`tranche 4`](../reports/ai-review-software-devops-2000-0002-tranche-04.md), [`tranche 5`](../reports/ai-review-software-devops-2000-0002-tranche-05.md), [`tranche 6`](../reports/ai-review-software-devops-2000-0002-tranche-06.md), [`tranche 7`](../reports/ai-review-software-devops-2000-0002-tranche-07.md), [`tranche 8`](../reports/ai-review-software-devops-2000-0002-tranche-08.md)'),
        ('Existem 700 notas materiais listadas abaixo; não há IDs reservados, placeholders ou registros virtuais para as 1300 restantes.',
         'Existem 800 notas materiais listadas abaixo; não há IDs reservados, placeholders ou registros virtuais para as 1200 restantes.'),
        ('As 700 notas 1–700 das tranches 1–7 têm revisão factual por IA registrada nos relatórios vinculados. O lote continua incompleto: são 700/2.000 notas válidas, restando 1300 notas materiais.',
         'As 800 notas 1–800 das tranches 1–8 têm revisão factual por IA registrada nos relatórios vinculados. O lote continua incompleto: são 800/2.000 notas válidas, restando 1200 notas materiais.'),
    ])

    apply(moc, [
        ('Índice das 700 notas substantivas redigidas até agora no lote `software-devops-2000-0002`, cuja meta é 2.000. As 700 passaram pelo gate automatizado',
         'Índice das 800 notas substantivas redigidas até agora no lote `software-devops-2000-0002`, cuja meta é 2.000. As 800 passaram pelo gate automatizado'),
        ('O gate automatizado foi aprovado por 700/700 notas e as 700 contam como válidas pelo protocolo atualizado, com revisão factual por IA registrada separadamente. O lote de 2.000 continua `in_progress` (700 notas substantivas; 1300 ainda não produzidas). Consulte o [manifesto](../../exports/batches/software-devops-2000-0002.md), a [auditoria de qualidade](../../exports/reports/note-quality-software-devops-2000-0002.md) e a [reconciliação mais recente do manifesto/fila](../../exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-07.md). Os relatórios factuais por IA são [tranche 1](../../exports/reports/ai-review-software-devops-2000-0002-tranche-01.md), [tranche 2](../../exports/reports/ai-review-software-devops-2000-0002-tranche-02.md), [tranche 3](../../exports/reports/ai-review-software-devops-2000-0002-tranche-03.md), [tranche 4](../../exports/reports/ai-review-software-devops-2000-0002-tranche-04.md), [tranche 5](../../exports/reports/ai-review-software-devops-2000-0002-tranche-05.md), [tranche 6](../../exports/reports/ai-review-software-devops-2000-0002-tranche-06.md) e [tranche 7](../../exports/reports/ai-review-software-devops-2000-0002-tranche-07.md).',
         'O gate automatizado foi aprovado por 800/800 notas e as 800 contam como válidas pelo protocolo atualizado, com revisão factual por IA registrada separadamente. O lote de 2.000 continua `in_progress` (800 notas substantivas; 1200 ainda não produzidas). Consulte o [manifesto](../../exports/batches/software-devops-2000-0002.md), a [auditoria de qualidade](../../exports/reports/note-quality-software-devops-2000-0002.md) e a [reconciliação mais recente do manifesto/fila](../../exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-08.md). Os relatórios factuais por IA são [tranche 1](../../exports/reports/ai-review-software-devops-2000-0002-tranche-01.md), [tranche 2](../../exports/reports/ai-review-software-devops-2000-0002-tranche-02.md), [tranche 3](../../exports/reports/ai-review-software-devops-2000-0002-tranche-03.md), [tranche 4](../../exports/reports/ai-review-software-devops-2000-0002-tranche-04.md), [tranche 5](../../exports/reports/ai-review-software-devops-2000-0002-tranche-05.md), [tranche 6](../../exports/reports/ai-review-software-devops-2000-0002-tranche-06.md), [tranche 7](../../exports/reports/ai-review-software-devops-2000-0002-tranche-07.md) e [tranche 8](../../exports/reports/ai-review-software-devops-2000-0002-tranche-08.md).'),
    ])

    apply(queue, [
        ('distingue 2691 revisões factuais realizadas por IA nos lotes `software-testes-2000-0001` (1991) e `software-devops-2000-0002` (700)',
         'distingue 2791 revisões factuais realizadas por IA nos lotes `software-testes-2000-0001` (1991) e `software-devops-2000-0002` (800)'),
        ('- Aprovações por IA registradas separadamente: **2691**.',
         '- Aprovações por IA registradas separadamente: **2791**.'),
        ('- Notas válidas contabilizadas (gate + revisão humana ou IA): **2740**.',
         '- Notas válidas contabilizadas (gate + revisão humana ou IA): **2840**.'),
        ('As 2691 linhas `APROVADA POR IA` (nº 50–2740) correspondem às 1991 notas 10–2000 das tranches 2–26 do lote `software-testes-2000-0001` e às 700 notas 1–700 das tranches 1–7 do lote `software-devops-2000-0002`',
         'As 2791 linhas `APROVADA POR IA` (nº 50–2840) correspondem às 1991 notas 10–2000 das tranches 2–26 do lote `software-testes-2000-0001` e às 800 notas 1–800 das tranches 1–8 do lote `software-devops-2000-0002`'),
    ])

    apply(ROOT / 'README.md', [
        ('| Notas válidas contabilizadas | 2740 / 1.000.000 (0,2740%) | 49 com aprovação humana histórica + 2691 com revisão factual por IA |',
         '| Notas válidas contabilizadas | 2840 / 1.000.000 (0,2840%) | 49 com aprovação humana histórica + 2791 com revisão factual por IA |'),
        ('| Notas com revisão factual por IA registrada | 2691 | Revisões dos lotes de escala (1991 no lote 1 + 700 no lote 2), com relatórios por tranche; não são humanas |',
         '| Notas com revisão factual por IA registrada | 2791 | Revisões dos lotes de escala (1991 no lote 1 + 800 no lote 2), com relatórios por tranche; não são humanas |'),
        ('| Segundo lote `software-devops-2000-0002` | 700 / 2.000 (35,00%) | 700 aprovadas por IA nas tranches 1–7; faltam 1300 notas substantivas |',
         '| Segundo lote `software-devops-2000-0002` | 800 / 2.000 (40,00%) | 800 aprovadas por IA nas tranches 1–8; faltam 1200 notas substantivas |'),
        ('| Arquivos Markdown ativos em `knowledge-federation/domains/` | 2840 | 100 notas legadas com pendências + 2740 notas autorais substantivas |',
         '| Arquivos Markdown ativos em `knowledge-federation/domains/` | 2940 | 100 notas legadas com pendências + 2840 notas autorais substantivas |'),
        ('700 notas materiais já passaram pelo gate e revisão factual por IA até a [tranche 7](knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-07.md) ([reconciliação](knowledge-federation/exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-07.md), [auditoria do lote](knowledge-federation/exports/reports/note-quality-software-devops-2000-0002.md) e [MOC de DevOps](knowledge-federation/00-home-vault/MOCs/MOC-DevOps-Software-0008.md)), com meta de 2.000.',
         '800 notas materiais já passaram pelo gate e revisão factual por IA até a [tranche 8](knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-08.md) ([reconciliação](knowledge-federation/exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-08.md), [auditoria do lote](knowledge-federation/exports/reports/note-quality-software-devops-2000-0002.md) e [MOC de DevOps](knowledge-federation/00-home-vault/MOCs/MOC-DevOps-Software-0008.md)), com meta de 2.000.'),
    ])

    apply(KF / 'README.md', [
        ('- Arquivos Markdown ativos: **2840** (100 notas legadas com pendências + 2740 notas autorais substantivas).',
         '- Arquivos Markdown ativos: **2940** (100 notas legadas com pendências + 2840 notas autorais substantivas).'),
        ('- Notas válidas pelo protocolo atual: **2740** (49 aprovações humanas históricas + 2691 revisões factuais por IA).',
         '- Notas válidas pelo protocolo atual: **2840** (49 aprovações humanas históricas + 2791 revisões factuais por IA).'),
        ('- Progresso: **2740 / 1.000.000 (0,2740%)**; faltam 997.260 notas válidas.',
         '- Progresso: **2840 / 1.000.000 (0,2840%)**; faltam 997.160 notas válidas.'),
        ('- Segundo lote em andamento `software-devops-2000-0002`: **700 / 2.000** notas válidas (35,00%); 700 por IA ([tranche 7](exports/reports/ai-review-software-devops-2000-0002-tranche-07.md) e [reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-07.md)); faltam 1300 notas materiais.',
         '- Segundo lote em andamento `software-devops-2000-0002`: **800 / 2.000** notas válidas (40,00%); 800 por IA ([tranche 8](exports/reports/ai-review-software-devops-2000-0002-tranche-08.md) e [reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-08.md)); faltam 1200 notas materiais.'),
    ])

    apply(KF / 'README-1M.md', [
        ('tem 2740 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 2691 revisões factuais por IA registradas separadamente). O diretório ativo tem 2840 arquivos Markdown, incluindo 100 notas legadas com pendências, ainda excluídas da contagem. O segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) está em andamento com 700/2.000 notas válidas ([relatório factual por IA da tranche 7](exports/reports/ai-review-software-devops-2000-0002-tranche-07.md) e [reconciliação da tranche 7](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-07.md)),',
         'tem 2840 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 2791 revisões factuais por IA registradas separadamente). O diretório ativo tem 2940 arquivos Markdown, incluindo 100 notas legadas com pendências, ainda excluídas da contagem. O segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) está em andamento com 800/2.000 notas válidas ([relatório factual por IA da tranche 8](exports/reports/ai-review-software-devops-2000-0002-tranche-08.md) e [reconciliação da tranche 8](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-08.md)),'),
    ])

    apply(KF / 'STATUS-CONSOLIDACAO-1M.md', [
        ('A auditoria encontrou 2840 arquivos Markdown ativos: 2740 notas substantivas passaram pelo gate e receberam revisão factual registrada (49 humanas históricas + 2691 por IA)',
         'A auditoria encontrou 2940 arquivos Markdown ativos: 2840 notas substantivas passaram pelo gate e receberam revisão factual registrada (49 humanas históricas + 2791 por IA)'),
        ('| Progresso válido global | 2740 / 1.000.000 (0,2740%) | 49 revisões humanas históricas + 2691 revisões por IA registradas separadamente |',
         '| Progresso válido global | 2840 / 1.000.000 (0,2840%) | 49 revisões humanas históricas + 2791 revisões por IA registradas separadamente |'),
        ('| Revisões factuais por IA registradas | 2691 | Relatórios das tranches 2–26 (`software-testes-2000-0001`) e tranches 1–7 (`software-devops-2000-0002`); não são humanas |',
         '| Revisões factuais por IA registradas | 2791 | Relatórios das tranches 2–26 (`software-testes-2000-0001`) e tranches 1–8 (`software-devops-2000-0002`); não são humanas |'),
        ('| Segundo lote (`software-devops-2000-0002`) | 700 / 2.000 (35,00%) | 700 IA nas tranches 1–7 ([tranche 7](exports/reports/ai-review-software-devops-2000-0002-tranche-07.md)); faltam 1300 notas substantivas |',
         '| Segundo lote (`software-devops-2000-0002`) | 800 / 2.000 (40,00%) | 800 IA nas tranches 1–8 ([tranche 8](exports/reports/ai-review-software-devops-2000-0002-tranche-08.md)); faltam 1200 notas substantivas |'),
        ('| Candidatas que passaram pelo gate automatizado | 2740 |',
         '| Candidatas que passaram pelo gate automatizado | 2840 |'),
        ('O segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) está em 700/2.000 notas válidas após a [tranche 7](exports/reports/ai-review-software-devops-2000-0002-tranche-07.md) ([reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-07.md)).',
         'O segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) está em 800/2.000 notas válidas após a [tranche 8](exports/reports/ai-review-software-devops-2000-0002-tranche-08.md) ([reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-08.md)).'),
        ('3. Continuar o segundo lote `software-devops-2000-0002` (atualmente em 700/2.000; faltam 1300 notas substantivas) e os 498 lotes subsequentes,',
         '3. Continuar o segundo lote `software-devops-2000-0002` (atualmente em 800/2.000; faltam 1200 notas substantivas) e os 498 lotes subsequentes,'),
    ])

    apply(KF / 'PLANO-CONTINUO-1M.md', [
        ('- Notas válidas globais: **2740** (49 aprovações humanas históricas + 2691 revisões factuais por IA).',
         '- Notas válidas globais: **2840** (49 aprovações humanas históricas + 2791 revisões factuais por IA).'),
        ('- Progresso: **2740 / 1.000.000 (0,2740%)**; faltam **997.260** notas válidas.',
         '- Progresso: **2840 / 1.000.000 (0,2840%)**; faltam **997.160** notas válidas.'),
        ('- Segundo lote atual `software-devops-2000-0002`: **700 / 2.000 (35,00%)** notas válidas (700 IA nas tranches 1–7); faltam **1300** notas substantivas.',
         '- Segundo lote atual `software-devops-2000-0002`: **800 / 2.000 (40,00%)** notas válidas (800 IA nas tranches 1–8); faltam **1200** notas substantivas.'),
        ('- Arquivos Markdown ativos: **2840**; 100 com pendências de qualidade, excluídos da contagem.',
         '- Arquivos Markdown ativos: **2940**; 100 com pendências de qualidade, excluídos da contagem.'),
        ('| 5 | Rodar gate, testes, auditorias e diff | **Concluído para o estado atual** | Lote 1: 2000/2000 (`complete`). Lote 2 (`software-devops-2000-0002`): 700/700 no gate (700 IA). Global: 2840 arquivos, 2740 válidas, 100 com pendências legadas; veja a [reconciliação da tranche 7 do lote 2](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-07.md). |',
         '| 5 | Rodar gate, testes, auditorias e diff | **Concluído para o estado atual** | Lote 1: 2000/2000 (`complete`). Lote 2 (`software-devops-2000-0002`): 800/800 no gate (800 IA). Global: 2940 arquivos, 2840 válidas, 100 com pendências legadas; veja a [reconciliação da tranche 8 do lote 2](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-08.md). |'),
        ('| 8 | Abrir lotes subsequentes de 2.000 notas | **Em andamento (lote 2 em 35%)** | Segundo lote `software-devops-2000-0002` com 700/2.000 notas válidas nas tranches 1–7; restam 1300 notas neste lote e 498 lotes subsequentes. |',
         '| 8 | Abrir lotes subsequentes de 2.000 notas | **Em andamento (lote 2 em 40%)** | Segundo lote `software-devops-2000-0002` com 800/2.000 notas válidas nas tranches 1–8; restam 1200 notas neste lote e 498 lotes subsequentes. |'),
        ('Progresso atual: 2740 notas válidas, 1/500 lotes completos.',
         'Progresso atual: 2840 notas válidas, 1/500 lotes completos.'),
    ])

    apply(KF / 'RECOVERY-AND-SCALE-NOTE.md', [
        ('há 2840 arquivos: 100 legados com pendências e 2740 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 2691 revisões por IA). O primeiro lote `software-testes-2000-0001` atingiu 2000/2.000 notas válidas (9 humanas + 1991 IA), com status `complete` ([tranche 26](exports/reports/ai-review-software-testes-2000-0001-tranche-26.md) e [reconciliação](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-26.md)); o segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) está em andamento (`in_progress`) com 700/2.000 notas válidas revisadas por IA até a [tranche 7](exports/reports/ai-review-software-devops-2000-0002-tranche-07.md), com [reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-07.md);',
         'há 2940 arquivos: 100 legados com pendências e 2840 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 2791 revisões por IA). O primeiro lote `software-testes-2000-0001` atingiu 2000/2.000 notas válidas (9 humanas + 1991 IA), com status `complete` ([tranche 26](exports/reports/ai-review-software-testes-2000-0001-tranche-26.md) e [reconciliação](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-26.md)); o segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) está em andamento (`in_progress`) com 800/2.000 notas válidas revisadas por IA até a [tranche 8](exports/reports/ai-review-software-devops-2000-0002-tranche-08.md), com [reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-08.md);'),
        ('4. Continuar o segundo lote `software-devops-2000-0002` (700/2.000; faltam 1300 notas qualificadas) até 2.000 antes de abrir os 498 lotes seguintes.',
         '4. Continuar o segundo lote `software-devops-2000-0002` (800/2.000; faltam 1200 notas qualificadas) até 2.000 antes de abrir os 498 lotes seguintes.'),
    ])

    apply(KF / '00-home-vault' / 'Home.md', [
        ('- [[MOC-DevOps-Software-0008]] — 700 notas do segundo lote de escala `software-devops-2000-0002` (meta: 2.000); 700 revisões factuais por IA.',
         '- [[MOC-DevOps-Software-0008]] — 800 notas do segundo lote de escala `software-devops-2000-0002` (meta: 2.000); 800 revisões factuais por IA.'),
        ('[[human-review-queue|Registro de revisões factuais]] — 49 aprovações humanas e 2691 aprovações por IA, identificadas separadamente.',
         '[[human-review-queue|Registro de revisões factuais]] — 49 aprovações humanas e 2791 aprovações por IA, identificadas separadamente.'),
        ('[[note-quality-audit|Auditoria de qualidade]] — 2740 notas válidas pelo protocolo atual (49 humanas + 2691 IA) e 100 notas legadas com falhas.',
         '[[note-quality-audit|Auditoria de qualidade]] — 2840 notas válidas pelo protocolo atual (49 humanas + 2791 IA) e 100 notas legadas com falhas.'),
    ])

    apply(KF / '00-home-vault' / 'Indice-Global.md', [
        ('- Arquivos Markdown em `domains/`: **2840** (100 sementes legadas + 2740 notas autorais substantivas).',
         '- Arquivos Markdown em `domains/`: **2940** (100 sementes legadas + 2840 notas autorais substantivas).'),
        ('- Candidatas aprovadas no gate automatizado: **2740**; revisões humanas registradas: **49**; revisões factuais por IA: **2691**; 100 sementes legadas mantêm pendências.',
         '- Candidatas aprovadas no gate automatizado: **2840**; revisões humanas registradas: **49**; revisões factuais por IA: **2791**; 100 sementes legadas mantêm pendências.'),
        ('- Os lotes atuais totalizam 2740 notas válidas pelo protocolo; o segundo lote [`software-devops-2000-0002`](../exports/batches/software-devops-2000-0002.md) tem 700/2.000 ([tranche 7](../exports/reports/ai-review-software-devops-2000-0002-tranche-07.md), [reconciliação da tranche 7](../exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-07.md) e [[MOC-DevOps-Software-0008]]),',
         '- Os lotes atuais totalizam 2840 notas válidas pelo protocolo; o segundo lote [`software-devops-2000-0002`](../exports/batches/software-devops-2000-0002.md) tem 800/2.000 ([tranche 8](../exports/reports/ai-review-software-devops-2000-0002-tranche-08.md), [reconciliação da tranche 8](../exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-08.md) e [[MOC-DevOps-Software-0008]]),'),
    ])
    print("reconciliação concluída")


if __name__ == "__main__":
    main()
