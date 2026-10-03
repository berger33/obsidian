#!/usr/bin/env python3
"""Reconcile batch software-devops-2000-0002 tranche 20 (IDs 1901-2000, completing batch 2 at 2000/2000) across manifest, MOC, review registry and status docs."""
from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KF = ROOT / "knowledge-federation"
SCRIPTS = KF / "scripts"
BATCH_ID = "software-devops-2000-0002"
REPORT_NAME = "ai-review-software-devops-2000-0002-tranche-20.md"
RECON_NAME = "batch-reconciliation-software-devops-2000-0002-tranche-20.md"
DATE = "2026-10-03"


def load_builder():
    spec = importlib.util.spec_from_file_location("bd20", SCRIPTS / "_build_devops_t20.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_groups(bd20):
    groups = []
    for path in sorted(bd20.DATA_DIR.glob("*.txt")):
        context, rows = bd20.parse_group(path)
        groups.append((context, rows))
    return groups


def manifest_section(groups) -> str:
    lines = [
        "## Tranche 20 — LinuxKit, cert-manager trust-manager, Cloudflare CFSSL, Smallstep step-ca, OpenBao, Infisical, Wazuh, CrowdSec, Keptn e Redpanda Connect / Benthos (100 notas; revisão factual por IA registrada)",
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
        "## Tranche 20 — LinuxKit, cert-manager trust-manager, Cloudflare CFSSL, Smallstep step-ca, OpenBao, Infisical, Wazuh, CrowdSec, Keptn e Redpanda Connect / Benthos",
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
    bd20 = load_builder()
    groups = load_groups(bd20)
    total = sum(len(rows) for _, rows in groups)
    if total != 100 or int(groups[0][0]["first"]) != 1901 or int(groups[-1][0]["first"]) != 1991:
        raise SystemExit(f"dados inesperados: {total} notas, primeiro grupo em {groups[0][0]['first']}")

    manifest = KF / "exports" / "batches" / f"{BATCH_ID}.md"
    moc = KF / "00-home-vault" / "MOCs" / "MOC-DevOps-Software-0008.md"
    queue = KF / "exports" / "reports" / "human-review-queue.md"

    insert_before(manifest, "## Critérios e próximo passo", manifest_section(groups))
    insert_before(moc, "## Estado editorial", moc_section(groups))
    insert_before(queue, "## Regra de contagem", review_rows(groups))

    apply(manifest, [
        ('- Notas efetivamente redigidas até agora: **1900 / 2.000 (95,00%)**',
         '- Notas efetivamente redigidas até agora: **2000 / 2.000 (100,00%)**'),
        ('- Gate automatizado: **1900/1900 aprovadas** (conteúdo mínimo, seções, fontes específicas e wikilinks; reexecutado após a tranche 19)',
         '- Gate automatizado: **2000/2000 aprovadas** (conteúdo mínimo, seções, fontes específicas e wikilinks; reexecutado após a tranche 20)'),
        ('- Revisão factual humana: **0/1900**',
         '- Revisão factual humana: **0/2000**'),
        ('- Revisão factual por IA: **1900/1900**',
         '- Revisão factual por IA: **2000/2000**'),
        ('- Contabilizadas como válidas: **1900/1900**',
         '- Contabilizadas como válidas: **2000/2000**'),
        ('- Revisor das 1900 notas aprovadas por IA: `Arena.ai Agent Mode`, com relatórios específicos; não são aprovações humanas',
         '- Revisor das 2000 notas aprovadas por IA: `Arena.ai Agent Mode`, com relatórios específicos; não são aprovações humanas'),
        ('- Status do lote maior: `in_progress`; tranches 1–19 (1900 notas, IDs 1–1900) foram conferidas factualmente por IA e aprovadas sob o protocolo atualizado',
         '- Status do lote maior: `complete`; tranches 1–20 (2000 notas, IDs 1–2000) foram conferidas factualmente por IA e aprovadas sob o protocolo atualizado'),
        ('- Reconciliação estrutural mais recente do manifesto/fila: [`batch-reconciliation-software-devops-2000-0002-tranche-19.md`](../reports/batch-reconciliation-software-devops-2000-0002-tranche-19.md)',
         '- Reconciliação estrutural mais recente do manifesto/fila: [`batch-reconciliation-software-devops-2000-0002-tranche-20.md`](../reports/batch-reconciliation-software-devops-2000-0002-tranche-20.md)'),
        ('- Relatórios factuais por IA: [`tranche 1`](../reports/ai-review-software-devops-2000-0002-tranche-01.md), [`tranche 2`](../reports/ai-review-software-devops-2000-0002-tranche-02.md), [`tranche 3`](../reports/ai-review-software-devops-2000-0002-tranche-03.md), [`tranche 4`](../reports/ai-review-software-devops-2000-0002-tranche-04.md), [`tranche 5`](../reports/ai-review-software-devops-2000-0002-tranche-05.md), [`tranche 6`](../reports/ai-review-software-devops-2000-0002-tranche-06.md), [`tranche 7`](../reports/ai-review-software-devops-2000-0002-tranche-07.md), [`tranche 8`](../reports/ai-review-software-devops-2000-0002-tranche-08.md), [`tranche 9`](../reports/ai-review-software-devops-2000-0002-tranche-09.md), [`tranche 10`](../reports/ai-review-software-devops-2000-0002-tranche-10.md), [`tranche 11`](../reports/ai-review-software-devops-2000-0002-tranche-11.md), [`tranche 12`](../reports/ai-review-software-devops-2000-0002-tranche-12.md), [`tranche 13`](../reports/ai-review-software-devops-2000-0002-tranche-13.md), [`tranche 14`](../reports/ai-review-software-devops-2000-0002-tranche-14.md), [`tranche 15`](../reports/ai-review-software-devops-2000-0002-tranche-15.md), [`tranche 16`](../reports/ai-review-software-devops-2000-0002-tranche-16.md), [`tranche 17`](../reports/ai-review-software-devops-2000-0002-tranche-17.md), [`tranche 18`](../reports/ai-review-software-devops-2000-0002-tranche-18.md), [`tranche 19`](../reports/ai-review-software-devops-2000-0002-tranche-19.md)',
         '- Relatórios factuais por IA: [`tranche 1`](../reports/ai-review-software-devops-2000-0002-tranche-01.md), [`tranche 2`](../reports/ai-review-software-devops-2000-0002-tranche-02.md), [`tranche 3`](../reports/ai-review-software-devops-2000-0002-tranche-03.md), [`tranche 4`](../reports/ai-review-software-devops-2000-0002-tranche-04.md), [`tranche 5`](../reports/ai-review-software-devops-2000-0002-tranche-05.md), [`tranche 6`](../reports/ai-review-software-devops-2000-0002-tranche-06.md), [`tranche 7`](../reports/ai-review-software-devops-2000-0002-tranche-07.md), [`tranche 8`](../reports/ai-review-software-devops-2000-0002-tranche-08.md), [`tranche 9`](../reports/ai-review-software-devops-2000-0002-tranche-09.md), [`tranche 10`](../reports/ai-review-software-devops-2000-0002-tranche-10.md), [`tranche 11`](../reports/ai-review-software-devops-2000-0002-tranche-11.md), [`tranche 12`](../reports/ai-review-software-devops-2000-0002-tranche-12.md), [`tranche 13`](../reports/ai-review-software-devops-2000-0002-tranche-13.md), [`tranche 14`](../reports/ai-review-software-devops-2000-0002-tranche-14.md), [`tranche 15`](../reports/ai-review-software-devops-2000-0002-tranche-15.md), [`tranche 16`](../reports/ai-review-software-devops-2000-0002-tranche-16.md), [`tranche 17`](../reports/ai-review-software-devops-2000-0002-tranche-17.md), [`tranche 18`](../reports/ai-review-software-devops-2000-0002-tranche-18.md), [`tranche 19`](../reports/ai-review-software-devops-2000-0002-tranche-19.md), [`tranche 20`](../reports/ai-review-software-devops-2000-0002-tranche-20.md)'),
        ('Existem 1900 notas materiais listadas abaixo; não há IDs reservados, placeholders ou registros virtuais para as 100 restantes.',
         'Todas as 2000 notas materiais já estão criadas e listadas abaixo; não há IDs reservados, placeholders ou registros virtuais.'),
        ('As 1900 notas 1–1900 das tranches 1–19 têm revisão factual por IA registrada nos relatórios vinculados. O lote continua incompleto: são 1900/2.000 notas válidas, restando 100 notas materiais.',
         'As 2000 notas 1–2000 das tranches 1–20 têm revisão factual por IA registrada nos relatórios vinculados. O segundo lote atingiu sua meta integral de 2000/2.000 notas válidas (`complete`).'),
    ])

    apply(moc, [
        ('Índice das 1900 notas substantivas redigidas até agora no lote `software-devops-2000-0002`, cuja meta é 2.000. As 1900 passaram pelo gate automatizado',
         'Índice das 2000 notas substantivas redigidas no lote concluído `software-devops-2000-0002`, cuja meta de 2.000 foi integralmente atingida (`complete`). As 2000 passaram pelo gate automatizado'),
        ('O gate automatizado foi aprovado por 1900/1900 notas e as 1900 contam como válidas pelo protocolo atualizado, com revisão factual por IA registrada separadamente. O lote de 2.000 continua `in_progress` (1900 notas substantivas; 100 ainda não produzidas). Consulte o [manifesto](../../exports/batches/software-devops-2000-0002.md), a [auditoria de qualidade](../../exports/reports/note-quality-software-devops-2000-0002.md) e a [reconciliação mais recente do manifesto/fila](../../exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-19.md). Os relatórios factuais por IA são [tranche 1](../../exports/reports/ai-review-software-devops-2000-0002-tranche-01.md), [tranche 2](../../exports/reports/ai-review-software-devops-2000-0002-tranche-02.md), [tranche 3](../../exports/reports/ai-review-software-devops-2000-0002-tranche-03.md), [tranche 4](../../exports/reports/ai-review-software-devops-2000-0002-tranche-04.md), [tranche 5](../../exports/reports/ai-review-software-devops-2000-0002-tranche-05.md), [tranche 6](../../exports/reports/ai-review-software-devops-2000-0002-tranche-06.md), [tranche 7](../../exports/reports/ai-review-software-devops-2000-0002-tranche-07.md), [tranche 8](../../exports/reports/ai-review-software-devops-2000-0002-tranche-08.md), [tranche 9](../../exports/reports/ai-review-software-devops-2000-0002-tranche-09.md), [tranche 10](../../exports/reports/ai-review-software-devops-2000-0002-tranche-10.md), [tranche 11](../../exports/reports/ai-review-software-devops-2000-0002-tranche-11.md), [tranche 12](../../exports/reports/ai-review-software-devops-2000-0002-tranche-12.md), [tranche 13](../../exports/reports/ai-review-software-devops-2000-0002-tranche-13.md), [tranche 14](../../exports/reports/ai-review-software-devops-2000-0002-tranche-14.md), [tranche 15](../../exports/reports/ai-review-software-devops-2000-0002-tranche-15.md), [tranche 16](../../exports/reports/ai-review-software-devops-2000-0002-tranche-16.md), [tranche 17](../../exports/reports/ai-review-software-devops-2000-0002-tranche-17.md), [tranche 18](../../exports/reports/ai-review-software-devops-2000-0002-tranche-18.md) e [tranche 19](../../exports/reports/ai-review-software-devops-2000-0002-tranche-19.md).',
         'O gate automatizado foi aprovado por 2000/2000 notas e as 2000 contam como válidas pelo protocolo atualizado, com revisão factual por IA registrada separadamente. O lote de 2.000 está concluído (`complete`, 2000/2.000 notas substantivas). Consulte o [manifesto](../../exports/batches/software-devops-2000-0002.md), a [auditoria de qualidade](../../exports/reports/note-quality-software-devops-2000-0002.md) e a [reconciliação mais recente do manifesto/fila](../../exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-20.md). Os relatórios factuais por IA são [tranche 1](../../exports/reports/ai-review-software-devops-2000-0002-tranche-01.md), [tranche 2](../../exports/reports/ai-review-software-devops-2000-0002-tranche-02.md), [tranche 3](../../exports/reports/ai-review-software-devops-2000-0002-tranche-03.md), [tranche 4](../../exports/reports/ai-review-software-devops-2000-0002-tranche-04.md), [tranche 5](../../exports/reports/ai-review-software-devops-2000-0002-tranche-05.md), [tranche 6](../../exports/reports/ai-review-software-devops-2000-0002-tranche-06.md), [tranche 7](../../exports/reports/ai-review-software-devops-2000-0002-tranche-07.md), [tranche 8](../../exports/reports/ai-review-software-devops-2000-0002-tranche-08.md), [tranche 9](../../exports/reports/ai-review-software-devops-2000-0002-tranche-09.md), [tranche 10](../../exports/reports/ai-review-software-devops-2000-0002-tranche-10.md), [tranche 11](../../exports/reports/ai-review-software-devops-2000-0002-tranche-11.md), [tranche 12](../../exports/reports/ai-review-software-devops-2000-0002-tranche-12.md), [tranche 13](../../exports/reports/ai-review-software-devops-2000-0002-tranche-13.md), [tranche 14](../../exports/reports/ai-review-software-devops-2000-0002-tranche-14.md), [tranche 15](../../exports/reports/ai-review-software-devops-2000-0002-tranche-15.md), [tranche 16](../../exports/reports/ai-review-software-devops-2000-0002-tranche-16.md), [tranche 17](../../exports/reports/ai-review-software-devops-2000-0002-tranche-17.md), [tranche 18](../../exports/reports/ai-review-software-devops-2000-0002-tranche-18.md), [tranche 19](../../exports/reports/ai-review-software-devops-2000-0002-tranche-19.md) e [tranche 20](../../exports/reports/ai-review-software-devops-2000-0002-tranche-20.md).'),
    ])

    apply(queue, [
        ('distingue 3891 revisões factuais realizadas por IA nos lotes `software-testes-2000-0001` (1991) e `software-devops-2000-0002` (1900)',
         'distingue 3991 revisões factuais realizadas por IA nos lotes `software-testes-2000-0001` (1991) e `software-devops-2000-0002` (2000)'),
        ('- Aprovações por IA registradas separadamente: **3891**.',
         '- Aprovações por IA registradas separadamente: **3991**.'),
        ('- Notas válidas contabilizadas (gate + revisão humana ou IA): **3940**.',
         '- Notas válidas contabilizadas (gate + revisão humana ou IA): **4040**.'),
        ('As 3891 linhas `APROVADA POR IA` (nº 50–3940) correspondem às 1991 notas 10–2000 das tranches 2–26 do lote `software-testes-2000-0001` e às 1900 notas 1–1900 das tranches 1–19 do lote `software-devops-2000-0002`',
         'As 3991 linhas `APROVADA POR IA` (nº 50–4040) correspondem às 1991 notas 10–2000 das tranches 2–26 do lote `software-testes-2000-0001` e às 2000 notas 1–2000 das tranches 1–20 do lote `software-devops-2000-0002`'),
    ])

    apply(ROOT / 'README.md', [
        ('| Lotes completos | 1 / 500 | Primeiro lote (`software-testes-2000-0001`) concluído com 2.000 notas válidas |',
         '| Lotes completos | 2 / 500 | Dois primeiros lotes (`software-testes-2000-0001` e `software-devops-2000-0002`) concluídos com 2.000 notas válidas cada |'),
        ('| Notas válidas contabilizadas | 3940 / 1.000.000 (0,3940%) | 49 com aprovação humana histórica + 3891 com revisão factual por IA |',
         '| Notas válidas contabilizadas | 4040 / 1.000.000 (0,4040%) | 49 com aprovação humana histórica + 3991 com revisão factual por IA |'),
        ('| Notas com revisão factual por IA registrada | 3891 | Revisões dos lotes de escala (1991 no lote 1 + 1900 no lote 2), com relatórios por tranche; não são humanas |',
         '| Notas com revisão factual por IA registrada | 3991 | Revisões dos lotes de escala (1991 no lote 1 + 2000 no lote 2), com relatórios por tranche; não são humanas |'),
        ('| Segundo lote `software-devops-2000-0002` | 1900 / 2.000 (95,00%) | 1900 aprovadas por IA nas tranches 1–19; faltam 100 notas substantivas |',
         '| Segundo lote `software-devops-2000-0002` | 2000 / 2.000 (100,00%) | 2000 aprovadas por IA nas tranches 1–20; lote concluído (`complete`) |'),
        ('| Arquivos Markdown ativos em `knowledge-federation/domains/` | 4040 | 100 notas legadas com pendências + 3940 notas autorais substantivas |',
         '| Arquivos Markdown ativos em `knowledge-federation/domains/` | 4140 | 100 notas legadas com pendências + 4040 notas autorais substantivas |'),
        ('e o segundo lote em andamento é [`software-devops-2000-0002`](knowledge-federation/exports/batches/software-devops-2000-0002.md): 1900 notas materiais já passaram pelo gate e revisão factual por IA até a [tranche 19](knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-19.md) ([reconciliação](knowledge-federation/exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-19.md), [auditoria do lote](knowledge-federation/exports/reports/note-quality-software-devops-2000-0002.md) e [MOC de DevOps](knowledge-federation/00-home-vault/MOCs/MOC-DevOps-Software-0008.md)), com meta de 2.000.',
         'e o segundo lote concluído é [`software-devops-2000-0002`](knowledge-federation/exports/batches/software-devops-2000-0002.md) (2000/2.000, `complete`): todas as 2000 notas materiais passaram pelo gate e revisão factual por IA até a [tranche 20](knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-20.md) ([reconciliação](knowledge-federation/exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-20.md), [auditoria do lote](knowledge-federation/exports/reports/note-quality-software-devops-2000-0002.md) e [MOC de DevOps](knowledge-federation/00-home-vault/MOCs/MOC-DevOps-Software-0008.md)).'),
    ])

    apply(KF / 'README.md', [
        ('- Arquivos Markdown ativos: **4040** (100 notas legadas com pendências + 3940 notas autorais substantivas).',
         '- Arquivos Markdown ativos: **4140** (100 notas legadas com pendências + 4040 notas autorais substantivas).'),
        ('- Notas válidas pelo protocolo atual: **3940** (49 aprovações humanas históricas + 3891 revisões factuais por IA).',
         '- Notas válidas pelo protocolo atual: **4040** (49 aprovações humanas históricas + 3991 revisões factuais por IA).'),
        ('- Progresso: **3940 / 1.000.000 (0,3940%)**; faltam 996.060 notas válidas.',
         '- Progresso: **4040 / 1.000.000 (0,4040%)**; faltam 995.960 notas válidas.'),
        ('- Lotes completos: **1 / 500** (`software-testes-2000-0001`).',
         '- Lotes completos: **2 / 500** (`software-testes-2000-0001` e `software-devops-2000-0002`).'),
        ('- Segundo lote em andamento `software-devops-2000-0002`: **1900 / 2.000** notas válidas (95,00%); 1900 por IA ([tranche 19](exports/reports/ai-review-software-devops-2000-0002-tranche-19.md) e [reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-19.md)); faltam 100 notas materiais.',
         '- Segundo lote concluído `software-devops-2000-0002`: **2000 / 2.000** notas válidas (100,00%); 2000 por IA ([tranche 20](exports/reports/ai-review-software-devops-2000-0002-tranche-20.md) e [reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-20.md)); status `complete`.'),
    ])

    apply(KF / 'README-1M.md', [
        ('tem 3940 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 3891 revisões factuais por IA registradas separadamente). O diretório ativo tem 4040 arquivos Markdown, incluindo 100 notas legadas com pendências, ainda excluídas da contagem. O segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) está em andamento com 1900/2.000 notas válidas ([relatório factual por IA da tranche 19](exports/reports/ai-review-software-devops-2000-0002-tranche-19.md) e [reconciliação da tranche 19](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-19.md)),',
         'tem 4040 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 3991 revisões factuais por IA registradas separadamente). O diretório ativo tem 4140 arquivos Markdown, incluindo 100 notas legadas com pendências, ainda excluídas da contagem. O segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) está concluído (`complete`) com 2000/2.000 notas válidas ([relatório factual por IA da tranche 20](exports/reports/ai-review-software-devops-2000-0002-tranche-20.md) e [reconciliação da tranche 20](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-20.md)),'),
    ])

    apply(KF / 'STATUS-CONSOLIDACAO-1M.md', [
        ('A auditoria encontrou 4040 arquivos Markdown ativos: 3940 notas substantivas passaram pelo gate e receberam revisão factual registrada (49 humanas históricas + 3891 por IA)',
         'A auditoria encontrou 4140 arquivos Markdown ativos: 4040 notas substantivas passaram pelo gate e receberam revisão factual registrada (49 humanas históricas + 3991 por IA)'),
        ('| Lotes completos | 1 / 500 | Primeiro lote (`software-testes-2000-0001`) concluído com 2.000 notas |',
         '| Lotes completos | 2 / 500 | Dois primeiros lotes (`software-testes-2000-0001` e `software-devops-2000-0002`) concluídos com 2.000 notas cada |'),
        ('| Progresso válido global | 3940 / 1.000.000 (0,3940%) | 49 revisões humanas históricas + 3891 revisões por IA registradas separadamente |',
         '| Progresso válido global | 4040 / 1.000.000 (0,4040%) | 49 revisões humanas históricas + 3991 revisões por IA registradas separadamente |'),
        ('| Revisões factuais por IA registradas | 3891 | Relatórios das tranches 2–26 (`software-testes-2000-0001`) e tranches 1–19 (`software-devops-2000-0002`); não são humanas |',
         '| Revisões factuais por IA registradas | 3991 | Relatórios das tranches 2–26 (`software-testes-2000-0001`) e tranches 1–20 (`software-devops-2000-0002`); não são humanas |'),
        ('| Segundo lote (`software-devops-2000-0002`) | 1900 / 2.000 (95,00%) | 1900 IA nas tranches 1–19 ([tranche 19](exports/reports/ai-review-software-devops-2000-0002-tranche-19.md)); faltam 100 notas substantivas |',
         '| Segundo lote (`software-devops-2000-0002`) | 2000 / 2.000 (100,00%) | 2000 IA nas tranches 1–20 ([tranche 20](exports/reports/ai-review-software-devops-2000-0002-tranche-20.md)); lote concluído (`complete`) |'),
        ('| Candidatas que passaram pelo gate automatizado | 3940 |',
         '| Candidatas que passaram pelo gate automatizado | 4040 |'),
        ('O segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) está em 1900/2.000 notas válidas após a [tranche 19](exports/reports/ai-review-software-devops-2000-0002-tranche-19.md) ([reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-19.md)).',
         'O segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) atingiu 2000/2.000 notas válidas (`complete`) após a [tranche 20](exports/reports/ai-review-software-devops-2000-0002-tranche-20.md) ([reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-20.md)).'),
        ('3. Continuar o segundo lote `software-devops-2000-0002` (atualmente em 1900/2.000; faltam 100 notas substantivas) e os 498 lotes subsequentes,',
         '3. Segundo lote `software-devops-2000-0002` concluído em 2000/2.000 (`complete`); abrir e avançar os 498 lotes subsequentes,'),
    ])

    apply(KF / 'PLANO-CONTINUO-1M.md', [
        ('- Notas válidas globais: **3940** (49 aprovações humanas históricas + 3891 revisões factuais por IA).',
         '- Notas válidas globais: **4040** (49 aprovações humanas históricas + 3991 revisões factuais por IA).'),
        ('- Progresso: **3940 / 1.000.000 (0,3940%)**; faltam **996.060** notas válidas.',
         '- Progresso: **4040 / 1.000.000 (0,4040%)**; faltam **995.960** notas válidas.'),
        ('- Lotes completos: **1 / 500** (`software-testes-2000-0001`).',
         '- Lotes completos: **2 / 500** (`software-testes-2000-0001` e `software-devops-2000-0002`).'),
        ('- Segundo lote atual `software-devops-2000-0002`: **1900 / 2.000 (95,00%)** notas válidas (1900 IA nas tranches 1–19); faltam **100** notas substantivas.',
         '- Segundo lote `software-devops-2000-0002`: **2000 / 2.000 (100,00%)** notas válidas (2000 IA nas tranches 1–20); concluído (`complete`).'),
        ('- Arquivos Markdown ativos: **4040**; 100 com pendências de qualidade, excluídos da contagem.',
         '- Arquivos Markdown ativos: **4140**; 100 com pendências de qualidade, excluídos da contagem.'),
        ('| 5 | Rodar gate, testes, auditorias e diff | **Concluído para o estado atual** | Lote 1: 2000/2000 (`complete`). Lote 2 (`software-devops-2000-0002`): 1900/1900 no gate (1900 IA). Global: 4040 arquivos, 3940 válidas, 100 com pendências legadas; veja a [reconciliação da tranche 19 do lote 2](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-19.md). |',
         '| 5 | Rodar gate, testes, auditorias e diff | **Concluído para o estado atual** | Lote 1: 2000/2000 (`complete`). Lote 2 (`software-devops-2000-0002`): 2000/2000 no gate (2000 IA, `complete`). Global: 4140 arquivos, 4040 válidas, 100 com pendências legadas; veja a [reconciliação da tranche 20 do lote 2](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-20.md). |'),
        ('| 8 | Abrir lotes subsequentes de 2.000 notas | **Em andamento (lote 2 em 95%)** | Segundo lote `software-devops-2000-0002` com 1900/2.000 notas válidas nas tranches 1–19; restam 100 notas neste lote e 498 lotes subsequentes. |',
         '| 8 | Abrir lotes subsequentes de 2.000 notas | **Lote 2 concluído (100%); 498 lotes restantes** | Segundo lote `software-devops-2000-0002` concluído (`complete`) com 2000/2.000 notas válidas nas tranches 1–20; restam 498 lotes subsequentes. |'),
        ('Progresso atual: 3940 notas válidas, 1/500 lotes completos.',
         'Progresso atual: 4040 notas válidas, 2/500 lotes completos.'),
    ])

    apply(KF / 'RECOVERY-AND-SCALE-NOTE.md', [
        ('há 4040 arquivos: 100 legados com pendências e 3940 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 3891 revisões por IA). O primeiro lote `software-testes-2000-0001` atingiu 2000/2.000 notas válidas (9 humanas + 1991 IA), com status `complete` ([tranche 26](exports/reports/ai-review-software-testes-2000-0001-tranche-26.md) e [reconciliação](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-26.md)); o segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) está em andamento (`in_progress`) com 1900/2.000 notas válidas revisadas por IA até a [tranche 19](exports/reports/ai-review-software-devops-2000-0002-tranche-19.md), com [reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-19.md);',
         'há 4140 arquivos: 100 legados com pendências e 4040 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 3991 revisões por IA). O primeiro lote `software-testes-2000-0001` atingiu 2000/2.000 notas válidas (9 humanas + 1991 IA), com status `complete` ([tranche 26](exports/reports/ai-review-software-testes-2000-0001-tranche-26.md) e [reconciliação](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-26.md)); o segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) atingiu 2000/2.000 notas válidas (`complete`) revisadas por IA até a [tranche 20](exports/reports/ai-review-software-devops-2000-0002-tranche-20.md), com [reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-20.md);'),
        ('4. Continuar o segundo lote `software-devops-2000-0002` (1900/2.000; faltam 100 notas qualificadas) até 2.000 antes de abrir os 498 lotes seguintes.',
         '4. Segundo lote `software-devops-2000-0002` concluído com 2000/2.000 notas qualificadas (`complete`); abrir os 498 lotes seguintes.'),
    ])

    apply(KF / '00-home-vault' / 'Home.md', [
        ('- [[MOC-DevOps-Software-0008]] — 1900 notas do segundo lote de escala `software-devops-2000-0002` (meta: 2.000); 1900 revisões factuais por IA.',
         '- [[MOC-DevOps-Software-0008]] — 2000 notas do segundo lote de escala `software-devops-2000-0002` (meta de 2.000 concluída, `complete`); 2000 revisões factuais por IA.'),
        ('[[human-review-queue|Registro de revisões factuais]] — 49 aprovações humanas e 3891 aprovações por IA, identificadas separadamente.',
         ('[[human-review-queue|Registro de revisões factuais]] — 49 aprovações humanas e 3991 aprovações por IA, identificadas separadamente.')),
        ('[[note-quality-audit|Auditoria de qualidade]] — 3940 notas válidas pelo protocolo atual (49 humanas + 3891 IA) e 100 notas legadas com falhas.',
         '[[note-quality-audit|Auditoria de qualidade]] — 4040 notas válidas pelo protocolo atual (49 humanas + 3991 IA) e 100 notas legadas com falhas.'),
    ])

    apply(KF / '00-home-vault' / 'Indice-Global.md', [
        ('- Arquivos Markdown em `domains/`: **4040** (100 sementes legadas + 3940 notas autorais substantivas).',
         '- Arquivos Markdown em `domains/`: **4140** (100 sementes legadas + 4040 notas autorais substantivas).'),
        ('- Candidatas aprovadas no gate automatizado: **3940**; revisões humanas registradas: **49**; revisões factuais por IA: **3891**; 100 sementes legadas mantêm pendências.',
         '- Candidatas aprovadas no gate automatizado: **4040**; revisões humanas registradas: **49**; revisões factuais por IA: **3991**; 100 sementes legadas mantêm pendências.'),
        ('- Os lotes atuais totalizam 3940 notas válidas pelo protocolo; o segundo lote [`software-devops-2000-0002`](../exports/batches/software-devops-2000-0002.md) tem 1900/2.000 ([tranche 19](../exports/reports/ai-review-software-devops-2000-0002-tranche-19.md), [reconciliação da tranche 19](../exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-19.md) e [[MOC-DevOps-Software-0008]]),',
         '- Os lotes atuais totalizam 4040 notas válidas pelo protocolo; o segundo lote [`software-devops-2000-0002`](../exports/batches/software-devops-2000-0002.md) atingiu 2000/2.000 (`complete`, [tranche 20](../exports/reports/ai-review-software-devops-2000-0002-tranche-20.md), [reconciliação da tranche 20](../exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-20.md) e [[MOC-DevOps-Software-0008]]),'),
    ])
    print("reconciliação concluída")


if __name__ == "__main__":
    main()
