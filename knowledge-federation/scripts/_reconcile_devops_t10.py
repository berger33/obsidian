#!/usr/bin/env python3
"""Reconcile batch software-devops-2000-0002 tranche 10 (IDs 901-1000) across manifest, MOC, review registry and status docs."""
from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KF = ROOT / "knowledge-federation"
SCRIPTS = KF / "scripts"
BATCH_ID = "software-devops-2000-0002"
REPORT_NAME = "ai-review-software-devops-2000-0002-tranche-10.md"
RECON_NAME = "batch-reconciliation-software-devops-2000-0002-tranche-10.md"
DATE = "2026-10-03"


def load_builder():
    spec = importlib.util.spec_from_file_location("bd10", SCRIPTS / "_build_devops_t10.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_groups(bd10):
    groups = []
    for path in sorted(bd10.DATA_DIR.glob("*.txt")):
        context, rows = bd10.parse_group(path)
        groups.append((context, rows))
    return groups


def manifest_section(groups) -> str:
    lines = [
        "## Tranche 10 — HashiCorp Vault, External Secrets Operator (ESO), Bitnami Sealed Secrets, SOPS, Atlantis, Infracost, GoReleaser, vCluster, K9s e Stern (100 notas; revisão factual por IA registrada)",
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
        "## Tranche 10 — HashiCorp Vault, External Secrets Operator (ESO), Bitnami Sealed Secrets, SOPS, Atlantis, Infracost, GoReleaser, vCluster, K9s e Stern",
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
    bd10 = load_builder()
    groups = load_groups(bd10)
    total = sum(len(rows) for _, rows in groups)
    if total != 100 or int(groups[0][0]["first"]) != 901 or int(groups[-1][0]["first"]) != 991:
        raise SystemExit(f"dados inesperados: {total} notas, primeiro grupo em {groups[0][0]['first']}")

    manifest = KF / "exports" / "batches" / f"{BATCH_ID}.md"
    moc = KF / "00-home-vault" / "MOCs" / "MOC-DevOps-Software-0008.md"
    queue = KF / "exports" / "reports" / "human-review-queue.md"

    insert_before(manifest, "## Critérios e próximo passo", manifest_section(groups))
    insert_before(moc, "## Estado editorial", moc_section(groups))
    insert_before(queue, "## Regra de contagem", review_rows(groups))

    apply(manifest, [
        ('- Notas efetivamente redigidas até agora: **900 / 2.000 (45,00%)**',
         '- Notas efetivamente redigidas até agora: **1000 / 2.000 (50,00%)**'),
        ('- Gate automatizado: **900/900 aprovadas** (conteúdo mínimo, seções, fontes específicas e wikilinks; reexecutado após a tranche 9)',
         '- Gate automatizado: **1000/1000 aprovadas** (conteúdo mínimo, seções, fontes específicas e wikilinks; reexecutado após a tranche 10)'),
        ('- Revisão factual humana: **0/900**',
         '- Revisão factual humana: **0/1000**'),
        ('- Revisão factual por IA: **900/900**',
         '- Revisão factual por IA: **1000/1000**'),
        ('- Contabilizadas como válidas: **900/900**',
         '- Contabilizadas como válidas: **1000/1000**'),
        ('- Revisor das 900 notas aprovadas por IA: `Arena.ai Agent Mode`, com relatórios específicos; não são aprovações humanas',
         '- Revisor das 1000 notas aprovadas por IA: `Arena.ai Agent Mode`, com relatórios específicos; não são aprovações humanas'),
        ('- Status do lote maior: `in_progress`; tranches 1–9 (900 notas, IDs 1–900) foram conferidas factualmente por IA e aprovadas sob o protocolo atualizado',
         '- Status do lote maior: `in_progress`; tranches 1–10 (1000 notas, IDs 1–1000) foram conferidas factualmente por IA e aprovadas sob o protocolo atualizado'),
        ('- Reconciliação estrutural mais recente do manifesto/fila: [`batch-reconciliation-software-devops-2000-0002-tranche-09.md`](../reports/batch-reconciliation-software-devops-2000-0002-tranche-09.md)',
         '- Reconciliação estrutural mais recente do manifesto/fila: [`batch-reconciliation-software-devops-2000-0002-tranche-10.md`](../reports/batch-reconciliation-software-devops-2000-0002-tranche-10.md)'),
        ('- Relatórios factuais por IA: [`tranche 1`](../reports/ai-review-software-devops-2000-0002-tranche-01.md), [`tranche 2`](../reports/ai-review-software-devops-2000-0002-tranche-02.md), [`tranche 3`](../reports/ai-review-software-devops-2000-0002-tranche-03.md), [`tranche 4`](../reports/ai-review-software-devops-2000-0002-tranche-04.md), [`tranche 5`](../reports/ai-review-software-devops-2000-0002-tranche-05.md), [`tranche 6`](../reports/ai-review-software-devops-2000-0002-tranche-06.md), [`tranche 7`](../reports/ai-review-software-devops-2000-0002-tranche-07.md), [`tranche 8`](../reports/ai-review-software-devops-2000-0002-tranche-08.md), [`tranche 9`](../reports/ai-review-software-devops-2000-0002-tranche-09.md)',
         '- Relatórios factuais por IA: [`tranche 1`](../reports/ai-review-software-devops-2000-0002-tranche-01.md), [`tranche 2`](../reports/ai-review-software-devops-2000-0002-tranche-02.md), [`tranche 3`](../reports/ai-review-software-devops-2000-0002-tranche-03.md), [`tranche 4`](../reports/ai-review-software-devops-2000-0002-tranche-04.md), [`tranche 5`](../reports/ai-review-software-devops-2000-0002-tranche-05.md), [`tranche 6`](../reports/ai-review-software-devops-2000-0002-tranche-06.md), [`tranche 7`](../reports/ai-review-software-devops-2000-0002-tranche-07.md), [`tranche 8`](../reports/ai-review-software-devops-2000-0002-tranche-08.md), [`tranche 9`](../reports/ai-review-software-devops-2000-0002-tranche-09.md), [`tranche 10`](../reports/ai-review-software-devops-2000-0002-tranche-10.md)'),
        ('Existem 900 notas materiais listadas abaixo; não há IDs reservados, placeholders ou registros virtuais para as 1100 restantes.',
         'Existem 1000 notas materiais listadas abaixo; não há IDs reservados, placeholders ou registros virtuais para as 1000 restantes.'),
        ('As 900 notas 1–900 das tranches 1–9 têm revisão factual por IA registrada nos relatórios vinculados. O lote continua incompleto: são 900/2.000 notas válidas, restando 1100 notas materiais.',
         'As 1000 notas 1–1000 das tranches 1–10 têm revisão factual por IA registrada nos relatórios vinculados. O lote continua incompleto: são 1000/2.000 notas válidas, restando 1000 notas materiais.'),
    ])

    apply(moc, [
        ('Índice das 900 notas substantivas redigidas até agora no lote `software-devops-2000-0002`, cuja meta é 2.000. As 900 passaram pelo gate automatizado',
         'Índice das 1000 notas substantivas redigidas até agora no lote `software-devops-2000-0002`, cuja meta é 2.000. As 1000 passaram pelo gate automatizado'),
        ('O gate automatizado foi aprovado por 900/900 notas e as 900 contam como válidas pelo protocolo atualizado, com revisão factual por IA registrada separadamente. O lote de 2.000 continua `in_progress` (900 notas substantivas; 1100 ainda não produzidas). Consulte o [manifesto](../../exports/batches/software-devops-2000-0002.md), a [auditoria de qualidade](../../exports/reports/note-quality-software-devops-2000-0002.md) e a [reconciliação mais recente do manifesto/fila](../../exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-09.md). Os relatórios factuais por IA são [tranche 1](../../exports/reports/ai-review-software-devops-2000-0002-tranche-01.md), [tranche 2](../../exports/reports/ai-review-software-devops-2000-0002-tranche-02.md), [tranche 3](../../exports/reports/ai-review-software-devops-2000-0002-tranche-03.md), [tranche 4](../../exports/reports/ai-review-software-devops-2000-0002-tranche-04.md), [tranche 5](../../exports/reports/ai-review-software-devops-2000-0002-tranche-05.md), [tranche 6](../../exports/reports/ai-review-software-devops-2000-0002-tranche-06.md), [tranche 7](../../exports/reports/ai-review-software-devops-2000-0002-tranche-07.md), [tranche 8](../../exports/reports/ai-review-software-devops-2000-0002-tranche-08.md) e [tranche 9](../../exports/reports/ai-review-software-devops-2000-0002-tranche-09.md).',
         'O gate automatizado foi aprovado por 1000/1000 notas e as 1000 contam como válidas pelo protocolo atualizado, com revisão factual por IA registrada separadamente. O lote de 2.000 continua `in_progress` (1000 notas substantivas; 1000 ainda não produzidas). Consulte o [manifesto](../../exports/batches/software-devops-2000-0002.md), a [auditoria de qualidade](../../exports/reports/note-quality-software-devops-2000-0002.md) e a [reconciliação mais recente do manifesto/fila](../../exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-10.md). Os relatórios factuais por IA são [tranche 1](../../exports/reports/ai-review-software-devops-2000-0002-tranche-01.md), [tranche 2](../../exports/reports/ai-review-software-devops-2000-0002-tranche-02.md), [tranche 3](../../exports/reports/ai-review-software-devops-2000-0002-tranche-03.md), [tranche 4](../../exports/reports/ai-review-software-devops-2000-0002-tranche-04.md), [tranche 5](../../exports/reports/ai-review-software-devops-2000-0002-tranche-05.md), [tranche 6](../../exports/reports/ai-review-software-devops-2000-0002-tranche-06.md), [tranche 7](../../exports/reports/ai-review-software-devops-2000-0002-tranche-07.md), [tranche 8](../../exports/reports/ai-review-software-devops-2000-0002-tranche-08.md), [tranche 9](../../exports/reports/ai-review-software-devops-2000-0002-tranche-09.md) e [tranche 10](../../exports/reports/ai-review-software-devops-2000-0002-tranche-10.md).'),
    ])

    apply(queue, [
        ('distingue 2891 revisões factuais realizadas por IA nos lotes `software-testes-2000-0001` (1991) e `software-devops-2000-0002` (900)',
         'distingue 2991 revisões factuais realizadas por IA nos lotes `software-testes-2000-0001` (1991) e `software-devops-2000-0002` (1000)'),
        ('- Aprovações por IA registradas separadamente: **2891**.',
         '- Aprovações por IA registradas separadamente: **2991**.'),
        ('- Notas válidas contabilizadas (gate + revisão humana ou IA): **2940**.',
         '- Notas válidas contabilizadas (gate + revisão humana ou IA): **3040**.'),
        ('As 2891 linhas `APROVADA POR IA` (nº 50–2940) correspondem às 1991 notas 10–2000 das tranches 2–26 do lote `software-testes-2000-0001` e às 900 notas 1–900 das tranches 1–9 do lote `software-devops-2000-0002`',
         'As 2991 linhas `APROVADA POR IA` (nº 50–3040) correspondem às 1991 notas 10–2000 das tranches 2–26 do lote `software-testes-2000-0001` e às 1000 notas 1–1000 das tranches 1–10 do lote `software-devops-2000-0002`'),
    ])

    apply(ROOT / 'README.md', [
        ('| Notas válidas contabilizadas | 2940 / 1.000.000 (0,2940%) | 49 com aprovação humana histórica + 2891 com revisão factual por IA |',
         '| Notas válidas contabilizadas | 3040 / 1.000.000 (0,3040%) | 49 com aprovação humana histórica + 2991 com revisão factual por IA |'),
        ('| Notas com revisão factual por IA registrada | 2891 | Revisões dos lotes de escala (1991 no lote 1 + 900 no lote 2), com relatórios por tranche; não são humanas |',
         '| Notas com revisão factual por IA registrada | 2991 | Revisões dos lotes de escala (1991 no lote 1 + 1000 no lote 2), com relatórios por tranche; não são humanas |'),
        ('| Segundo lote `software-devops-2000-0002` | 900 / 2.000 (45,00%) | 900 aprovadas por IA nas tranches 1–9; faltam 1100 notas substantivas |',
         '| Segundo lote `software-devops-2000-0002` | 1000 / 2.000 (50,00%) | 1000 aprovadas por IA nas tranches 1–10; faltam 1000 notas substantivas |'),
        ('| Arquivos Markdown ativos em `knowledge-federation/domains/` | 3040 | 100 notas legadas com pendências + 2940 notas autorais substantivas |',
         '| Arquivos Markdown ativos em `knowledge-federation/domains/` | 3140 | 100 notas legadas com pendências + 3040 notas autorais substantivas |'),
        ('900 notas materiais já passaram pelo gate e revisão factual por IA até a [tranche 9](knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-09.md) ([reconciliação](knowledge-federation/exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-09.md), [auditoria do lote](knowledge-federation/exports/reports/note-quality-software-devops-2000-0002.md) e [MOC de DevOps](knowledge-federation/00-home-vault/MOCs/MOC-DevOps-Software-0008.md)), com meta de 2.000.',
         '1000 notas materiais já passaram pelo gate e revisão factual por IA até a [tranche 10](knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-10.md) ([reconciliação](knowledge-federation/exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-10.md), [auditoria do lote](knowledge-federation/exports/reports/note-quality-software-devops-2000-0002.md) e [MOC de DevOps](knowledge-federation/00-home-vault/MOCs/MOC-DevOps-Software-0008.md)), com meta de 2.000.'),
    ])

    apply(KF / 'README.md', [
        ('- Arquivos Markdown ativos: **3040** (100 notas legadas com pendências + 2940 notas autorais substantivas).',
         '- Arquivos Markdown ativos: **3140** (100 notas legadas com pendências + 3040 notas autorais substantivas).'),
        ('- Notas válidas pelo protocolo atual: **2940** (49 aprovações humanas históricas + 2891 revisões factuais por IA).',
         '- Notas válidas pelo protocolo atual: **3040** (49 aprovações humanas históricas + 2991 revisões factuais por IA).'),
        ('- Progresso: **2940 / 1.000.000 (0,2940%)**; faltam 997.060 notas válidas.',
         '- Progresso: **3040 / 1.000.000 (0,3040%)**; faltam 996.960 notas válidas.'),
        ('- Segundo lote em andamento `software-devops-2000-0002`: **900 / 2.000** notas válidas (45,00%); 900 por IA ([tranche 9](exports/reports/ai-review-software-devops-2000-0002-tranche-09.md) e [reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-09.md)); faltam 1100 notas materiais.',
         '- Segundo lote em andamento `software-devops-2000-0002`: **1000 / 2.000** notas válidas (50,00%); 1000 por IA ([tranche 10](exports/reports/ai-review-software-devops-2000-0002-tranche-10.md) e [reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-10.md)); faltam 1000 notas materiais.'),
    ])

    apply(KF / 'README-1M.md', [
        ('tem 2940 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 2891 revisões factuais por IA registradas separadamente). O diretório ativo tem 3040 arquivos Markdown, incluindo 100 notas legadas com pendências, ainda excluídas da contagem. O segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) está em andamento com 900/2.000 notas válidas ([relatório factual por IA da tranche 9](exports/reports/ai-review-software-devops-2000-0002-tranche-09.md) e [reconciliação da tranche 9](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-09.md)),',
         'tem 3040 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 2991 revisões factuais por IA registradas separadamente). O diretório ativo tem 3140 arquivos Markdown, incluindo 100 notas legadas com pendências, ainda excluídas da contagem. O segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) está em andamento com 1000/2.000 notas válidas ([relatório factual por IA da tranche 10](exports/reports/ai-review-software-devops-2000-0002-tranche-10.md) e [reconciliação da tranche 10](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-10.md)),'),
    ])

    apply(KF / 'STATUS-CONSOLIDACAO-1M.md', [
        ('A auditoria encontrou 3040 arquivos Markdown ativos: 2940 notas substantivas passaram pelo gate e receberam revisão factual registrada (49 humanas históricas + 2891 por IA)',
         'A auditoria encontrou 3140 arquivos Markdown ativos: 3040 notas substantivas passaram pelo gate e receberam revisão factual registrada (49 humanas históricas + 2991 por IA)'),
        ('| Progresso válido global | 2940 / 1.000.000 (0,2940%) | 49 revisões humanas históricas + 2891 revisões por IA registradas separadamente |',
         '| Progresso válido global | 3040 / 1.000.000 (0,3040%) | 49 revisões humanas históricas + 2991 revisões por IA registradas separadamente |'),
        ('| Revisões factuais por IA registradas | 2891 | Relatórios das tranches 2–26 (`software-testes-2000-0001`) e tranches 1–9 (`software-devops-2000-0002`); não são humanas |',
         '| Revisões factuais por IA registradas | 2991 | Relatórios das tranches 2–26 (`software-testes-2000-0001`) e tranches 1–10 (`software-devops-2000-0002`); não são humanas |'),
        ('| Segundo lote (`software-devops-2000-0002`) | 900 / 2.000 (45,00%) | 900 IA nas tranches 1–9 ([tranche 9](exports/reports/ai-review-software-devops-2000-0002-tranche-09.md)); faltam 1100 notas substantivas |',
         '| Segundo lote (`software-devops-2000-0002`) | 1000 / 2.000 (50,00%) | 1000 IA nas tranches 1–10 ([tranche 10](exports/reports/ai-review-software-devops-2000-0002-tranche-10.md)); faltam 1000 notas substantivas |'),
        ('| Candidatas que passaram pelo gate automatizado | 2940 |',
         '| Candidatas que passaram pelo gate automatizado | 3040 |'),
        ('O segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) está em 900/2.000 notas válidas após a [tranche 9](exports/reports/ai-review-software-devops-2000-0002-tranche-09.md) ([reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-09.md)).',
         'O segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) está em 1000/2.000 notas válidas após a [tranche 10](exports/reports/ai-review-software-devops-2000-0002-tranche-10.md) ([reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-10.md)).'),
        ('3. Continuar o segundo lote `software-devops-2000-0002` (atualmente em 900/2.000; faltam 1100 notas substantivas) e os 498 lotes subsequentes,',
         '3. Continuar o segundo lote `software-devops-2000-0002` (atualmente em 1000/2.000; faltam 1000 notas substantivas) e os 498 lotes subsequentes,'),
    ])

    apply(KF / 'PLANO-CONTINUO-1M.md', [
        ('- Notas válidas globais: **2940** (49 aprovações humanas históricas + 2891 revisões factuais por IA).',
         '- Notas válidas globais: **3040** (49 aprovações humanas históricas + 2991 revisões factuais por IA).'),
        ('- Progresso: **2940 / 1.000.000 (0,2940%)**; faltam **997.060** notas válidas.',
         '- Progresso: **3040 / 1.000.000 (0,3040%)**; faltam **996.960** notas válidas.'),
        ('- Segundo lote atual `software-devops-2000-0002`: **900 / 2.000 (45,00%)** notas válidas (900 IA nas tranches 1–9); faltam **1100** notas substantivas.',
         '- Segundo lote atual `software-devops-2000-0002`: **1000 / 2.000 (50,00%)** notas válidas (1000 IA nas tranches 1–10); faltam **1000** notas substantivas.'),
        ('- Arquivos Markdown ativos: **3040**; 100 com pendências de qualidade, excluídos da contagem.',
         '- Arquivos Markdown ativos: **3140**; 100 com pendências de qualidade, excluídos da contagem.'),
        ('| 5 | Rodar gate, testes, auditorias e diff | **Concluído para o estado atual** | Lote 1: 2000/2000 (`complete`). Lote 2 (`software-devops-2000-0002`): 900/900 no gate (900 IA). Global: 3040 arquivos, 2940 válidas, 100 com pendências legadas; veja a [reconciliação da tranche 9 do lote 2](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-09.md). |',
         '| 5 | Rodar gate, testes, auditorias e diff | **Concluído para o estado atual** | Lote 1: 2000/2000 (`complete`). Lote 2 (`software-devops-2000-0002`): 1000/1000 no gate (1000 IA). Global: 3140 arquivos, 3040 válidas, 100 com pendências legadas; veja a [reconciliação da tranche 10 do lote 2](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-10.md). |'),
        ('| 8 | Abrir lotes subsequentes de 2.000 notas | **Em andamento (lote 2 em 45%)** | Segundo lote `software-devops-2000-0002` com 900/2.000 notas válidas nas tranches 1–9; restam 1100 notas neste lote e 498 lotes subsequentes. |',
         '| 8 | Abrir lotes subsequentes de 2.000 notas | **Em andamento (lote 2 em 50%)** | Segundo lote `software-devops-2000-0002` com 1000/2.000 notas válidas nas tranches 1–10; restam 1000 notas neste lote e 498 lotes subsequentes. |'),
        ('Progresso atual: 2940 notas válidas, 1/500 lotes completos.',
         'Progresso atual: 3040 notas válidas, 1/500 lotes completos.'),
    ])

    apply(KF / 'RECOVERY-AND-SCALE-NOTE.md', [
        ('há 3040 arquivos: 100 legados com pendências e 2940 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 2891 revisões por IA). O primeiro lote `software-testes-2000-0001` atingiu 2000/2.000 notas válidas (9 humanas + 1991 IA), com status `complete` ([tranche 26](exports/reports/ai-review-software-testes-2000-0001-tranche-26.md) e [reconciliação](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-26.md)); o segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) está em andamento (`in_progress`) com 900/2.000 notas válidas revisadas por IA até a [tranche 9](exports/reports/ai-review-software-devops-2000-0002-tranche-09.md), com [reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-09.md);',
         'há 3140 arquivos: 100 legados com pendências e 3040 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 2991 revisões por IA). O primeiro lote `software-testes-2000-0001` atingiu 2000/2.000 notas válidas (9 humanas + 1991 IA), com status `complete` ([tranche 26](exports/reports/ai-review-software-testes-2000-0001-tranche-26.md) e [reconciliação](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-26.md)); o segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) está em andamento (`in_progress`) com 1000/2.000 notas válidas revisadas por IA até a [tranche 10](exports/reports/ai-review-software-devops-2000-0002-tranche-10.md), com [reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-10.md);'),
        ('4. Continuar o segundo lote `software-devops-2000-0002` (900/2.000; faltam 1100 notas qualificadas) até 2.000 antes de abrir os 498 lotes seguintes.',
         '4. Continuar o segundo lote `software-devops-2000-0002` (1000/2.000; faltam 1000 notas qualificadas) até 2.000 antes de abrir os 498 lotes seguintes.'),
    ])

    apply(KF / '00-home-vault' / 'Home.md', [
        ('- [[MOC-DevOps-Software-0008]] — 900 notas do segundo lote de escala `software-devops-2000-0002` (meta: 2.000); 900 revisões factuais por IA.',
         '- [[MOC-DevOps-Software-0008]] — 1000 notas do segundo lote de escala `software-devops-2000-0002` (meta: 2.000); 1000 revisões factuais por IA.'),
        ('[[human-review-queue|Registro de revisões factuais]] — 49 aprovações humanas e 2891 aprovações por IA, identificadas separadamente.',
         '[[human-review-queue|Registro de revisões factuais]] — 49 aprovações humanas e 2991 aprovações por IA, identificadas separadamente.'),
        ('[[note-quality-audit|Auditoria de qualidade]] — 2940 notas válidas pelo protocolo atual (49 humanas + 2891 IA) e 100 notas legadas com falhas.',
         '[[note-quality-audit|Auditoria de qualidade]] — 3040 notas válidas pelo protocolo atual (49 humanas + 2991 IA) e 100 notas legadas com falhas.'),
    ])

    apply(KF / '00-home-vault' / 'Indice-Global.md', [
        ('- Arquivos Markdown em `domains/`: **3040** (100 sementes legadas + 2940 notas autorais substantivas).',
         '- Arquivos Markdown em `domains/`: **3140** (100 sementes legadas + 3040 notas autorais substantivas).'),
        ('- Candidatas aprovadas no gate automatizado: **2940**; revisões humanas registradas: **49**; revisões factuais por IA: **2891**; 100 sementes legadas mantêm pendências.',
         '- Candidatas aprovadas no gate automatizado: **3040**; revisões humanas registradas: **49**; revisões factuais por IA: **2991**; 100 sementes legadas mantêm pendências.'),
        ('- Os lotes atuais totalizam 2940 notas válidas pelo protocolo; o segundo lote [`software-devops-2000-0002`](../exports/batches/software-devops-2000-0002.md) tem 900/2.000 ([tranche 9](../exports/reports/ai-review-software-devops-2000-0002-tranche-09.md), [reconciliação da tranche 9](../exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-09.md) e [[MOC-DevOps-Software-0008]]),',
         '- Os lotes atuais totalizam 3040 notas válidas pelo protocolo; o segundo lote [`software-devops-2000-0002`](../exports/batches/software-devops-2000-0002.md) tem 1000/2.000 ([tranche 10](../exports/reports/ai-review-software-devops-2000-0002-tranche-10.md), [reconciliação da tranche 10](../exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-10.md) e [[MOC-DevOps-Software-0008]]),'),
    ])
    print("reconciliação concluída")


if __name__ == "__main__":
    main()
