#!/usr/bin/env python3
"""Reconcile batch software-devops-2000-0002 tranche 3 (IDs 201-300) across manifest, MOC, review registry and status docs."""
from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KF = ROOT / "knowledge-federation"
SCRIPTS = KF / "scripts"
BATCH_ID = "software-devops-2000-0002"
REPORT_NAME = "ai-review-software-devops-2000-0002-tranche-03.md"
RECON_NAME = "batch-reconciliation-software-devops-2000-0002-tranche-03.md"
DATE = "2026-10-03"


def load_builder():
    spec = importlib.util.spec_from_file_location("bd03", SCRIPTS / "_build_devops_t03.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_groups(bd03):
    groups = []
    for path in sorted(bd03.DATA_DIR.glob("*.txt")):
        context, rows = bd03.parse_group(path)
        groups.append((context, rows))
    return groups


def manifest_section(groups) -> str:
    lines = ["## Tranche 3 — cert-manager, ExternalDNS, Kyverno, OPA Gatekeeper, Falco, KEDA, Karpenter, Envoy Proxy, CoreDNS e etcd (100 notas; revisão factual por IA registrada)", ""]
    for context, rows in groups:
        lines.append(f"### {context['group']}")
        lines.append("")
        for index, row in enumerate(rows):
            number = int(context["first"]) + index
            lines.append(
                f"{number}. [{row['title']}](../../domains/software-0008/software/devops/{row['slug']}.md)"
            )
        lines.append("")
    return "\n".join(lines) + "\n"


def moc_section(groups) -> str:
    lines = ["## Tranche 3 — cert-manager, ExternalDNS, Kyverno, OPA Gatekeeper, Falco, KEDA, Karpenter, Envoy Proxy, CoreDNS e etcd", ""]
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
    bd03 = load_builder()
    groups = load_groups(bd03)
    total = sum(len(rows) for _, rows in groups)
    if total != 100 or int(groups[0][0]["first"]) != 201 or int(groups[-1][0]["first"]) != 291:
        raise SystemExit(f"dados inesperados: {total} notas, primeiro grupo em {groups[0][0]['first']}")

    manifest = KF / "exports" / "batches" / f"{BATCH_ID}.md"
    moc = KF / "00-home-vault" / "MOCs" / "MOC-DevOps-Software-0008.md"
    queue = KF / "exports" / "reports" / "human-review-queue.md"

    insert_before(manifest, "## Critérios e próximo passo", manifest_section(groups))
    insert_before(moc, "## Estado editorial", moc_section(groups))
    insert_before(queue, "## Regra de contagem", review_rows(groups))

    apply(manifest, [
        ('- Notas efetivamente redigidas até agora: **200 / 2.000 (10,00%)**',
         '- Notas efetivamente redigidas até agora: **300 / 2.000 (15,00%)**'),
        ('- Gate automatizado: **200/200 aprovadas** (conteúdo mínimo, seções, fontes específicas e wikilinks; reexecutado após a tranche 2)',
         '- Gate automatizado: **300/300 aprovadas** (conteúdo mínimo, seções, fontes específicas e wikilinks; reexecutado após a tranche 3)'),
        ('- Revisão factual humana: **0/200**',
         '- Revisão factual humana: **0/300**'),
        ('- Revisão factual por IA: **200/200**',
         '- Revisão factual por IA: **300/300**'),
        ('- Contabilizadas como válidas: **200/200**',
         '- Contabilizadas como válidas: **300/300**'),
        ('- Revisor das 200 notas aprovadas por IA: `Arena.ai Agent Mode`, com relatórios específicos; não são aprovações humanas',
         '- Revisor das 300 notas aprovadas por IA: `Arena.ai Agent Mode`, com relatórios específicos; não são aprovações humanas'),
        ('- Status do lote maior: `in_progress`; tranches 1–2 (200 notas, IDs 1–200) foram conferidas factualmente por IA e aprovadas sob o protocolo atualizado',
         '- Status do lote maior: `in_progress`; tranches 1–3 (300 notas, IDs 1–300) foram conferidas factualmente por IA e aprovadas sob o protocolo atualizado'),
        ('- Reconciliação estrutural mais recente do manifesto/fila: [`batch-reconciliation-software-devops-2000-0002-tranche-02.md`](../reports/batch-reconciliation-software-devops-2000-0002-tranche-02.md)',
         '- Reconciliação estrutural mais recente do manifesto/fila: [`batch-reconciliation-software-devops-2000-0002-tranche-03.md`](../reports/batch-reconciliation-software-devops-2000-0002-tranche-03.md)'),
        ('- Relatórios factuais por IA: [`tranche 1`](../reports/ai-review-software-devops-2000-0002-tranche-01.md), [`tranche 2`](../reports/ai-review-software-devops-2000-0002-tranche-02.md)',
         '- Relatórios factuais por IA: [`tranche 1`](../reports/ai-review-software-devops-2000-0002-tranche-01.md), [`tranche 2`](../reports/ai-review-software-devops-2000-0002-tranche-02.md), [`tranche 3`](../reports/ai-review-software-devops-2000-0002-tranche-03.md)'),
        ('Existem 200 notas materiais listadas abaixo; não há IDs reservados, placeholders ou registros virtuais para as 1800 restantes.',
         'Existem 300 notas materiais listadas abaixo; não há IDs reservados, placeholders ou registros virtuais para as 1700 restantes.'),
        ('As 200 notas 1–200 das tranches 1–2 têm revisão factual por IA registrada nos relatórios vinculados. O lote continua incompleto: são 200/2.000 notas válidas, restando 1800 notas materiais.',
         'As 300 notas 1–300 das tranches 1–3 têm revisão factual por IA registrada nos relatórios vinculados. O lote continua incompleto: são 300/2.000 notas válidas, restando 1700 notas materiais.'),
    ])

    apply(moc, [
        ('Índice das 200 notas substantivas redigidas até agora no lote `software-devops-2000-0002`, cuja meta é 2.000. As 200 passaram pelo gate automatizado',
         'Índice das 300 notas substantivas redigidas até agora no lote `software-devops-2000-0002`, cuja meta é 2.000. As 300 passaram pelo gate automatizado'),
        ('O gate automatizado foi aprovado por 200/200 notas e as 200 contam como válidas pelo protocolo atualizado, com revisão factual por IA registrada separadamente. O lote de 2.000 continua `in_progress` (200 notas substantivas; 1800 ainda não produzidas). Consulte o [manifesto](../../exports/batches/software-devops-2000-0002.md), a [auditoria de qualidade](../../exports/reports/note-quality-software-devops-2000-0002.md) e a [reconciliação mais recente do manifesto/fila](../../exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-02.md). Os relatórios factuais por IA são [tranche 1](../../exports/reports/ai-review-software-devops-2000-0002-tranche-01.md) e [tranche 2](../../exports/reports/ai-review-software-devops-2000-0002-tranche-02.md).',
         'O gate automatizado foi aprovado por 300/300 notas e as 300 contam como válidas pelo protocolo atualizado, com revisão factual por IA registrada separadamente. O lote de 2.000 continua `in_progress` (300 notas substantivas; 1700 ainda não produzidas). Consulte o [manifesto](../../exports/batches/software-devops-2000-0002.md), a [auditoria de qualidade](../../exports/reports/note-quality-software-devops-2000-0002.md) e a [reconciliação mais recente do manifesto/fila](../../exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-03.md). Os relatórios factuais por IA são [tranche 1](../../exports/reports/ai-review-software-devops-2000-0002-tranche-01.md), [tranche 2](../../exports/reports/ai-review-software-devops-2000-0002-tranche-02.md) e [tranche 3](../../exports/reports/ai-review-software-devops-2000-0002-tranche-03.md).'),
    ])

    apply(queue, [
        ('distingue 2191 revisões factuais realizadas por IA nos lotes `software-testes-2000-0001` (1991) e `software-devops-2000-0002` (200)',
         'distingue 2291 revisões factuais realizadas por IA nos lotes `software-testes-2000-0001` (1991) e `software-devops-2000-0002` (300)'),
        ('- Aprovações por IA registradas separadamente: **2191**.',
         '- Aprovações por IA registradas separadamente: **2291**.'),
        ('- Notas válidas contabilizadas (gate + revisão humana ou IA): **2240**.',
         '- Notas válidas contabilizadas (gate + revisão humana ou IA): **2340**.'),
        ('As 2191 linhas `APROVADA POR IA` (nº 50–2240) correspondem às 1991 notas 10–2000 das tranches 2–26 do lote `software-testes-2000-0001` e às 200 notas 1–200 das tranches 1–2 do lote `software-devops-2000-0002`',
         'As 2291 linhas `APROVADA POR IA` (nº 50–2340) correspondem às 1991 notas 10–2000 das tranches 2–26 do lote `software-testes-2000-0001` e às 300 notas 1–300 das tranches 1–3 do lote `software-devops-2000-0002`'),
    ])

    apply(ROOT / 'README.md', [
        ('| Notas válidas contabilizadas | 2240 / 1.000.000 (0,2240%) | 49 com aprovação humana histórica + 2191 com revisão factual por IA |',
         '| Notas válidas contabilizadas | 2340 / 1.000.000 (0,2340%) | 49 com aprovação humana histórica + 2291 com revisão factual por IA |'),
        ('| Notas com revisão factual por IA registrada | 2191 | Revisões dos lotes de escala (1991 no lote 1 + 200 no lote 2), com relatórios por tranche; não são humanas |',
         '| Notas com revisão factual por IA registrada | 2291 | Revisões dos lotes de escala (1991 no lote 1 + 300 no lote 2), com relatórios por tranche; não são humanas |'),
        ('| Segundo lote `software-devops-2000-0002` | 200 / 2.000 (10,00%) | 200 aprovadas por IA nas tranches 1–2; faltam 1800 notas substantivas |',
         '| Segundo lote `software-devops-2000-0002` | 300 / 2.000 (15,00%) | 300 aprovadas por IA nas tranches 1–3; faltam 1700 notas substantivas |'),
        ('| Arquivos Markdown ativos em `knowledge-federation/domains/` | 2340 | 100 notas legadas com pendências + 2240 notas autorais substantivas |',
         '| Arquivos Markdown ativos em `knowledge-federation/domains/` | 2440 | 100 notas legadas com pendências + 2340 notas autorais substantivas |'),
        ('200 notas materiais já passaram pelo gate e revisão factual por IA até a [tranche 2](knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-02.md) ([reconciliação](knowledge-federation/exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-02.md), [auditoria do lote](knowledge-federation/exports/reports/note-quality-software-devops-2000-0002.md) e [MOC de DevOps](knowledge-federation/00-home-vault/MOCs/MOC-DevOps-Software-0008.md)), com meta de 2.000.',
         '300 notas materiais já passaram pelo gate e revisão factual por IA até a [tranche 3](knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-03.md) ([reconciliação](knowledge-federation/exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-03.md), [auditoria do lote](knowledge-federation/exports/reports/note-quality-software-devops-2000-0002.md) e [MOC de DevOps](knowledge-federation/00-home-vault/MOCs/MOC-DevOps-Software-0008.md)), com meta de 2.000.'),
    ])

    apply(KF / 'README.md', [
        ('- Arquivos Markdown ativos: **2340** (100 notas legadas com pendências + 2240 notas autorais substantivas).',
         '- Arquivos Markdown ativos: **2440** (100 notas legadas com pendências + 2340 notas autorais substantivas).'),
        ('- Notas válidas pelo protocolo atual: **2240** (49 aprovações humanas históricas + 2191 revisões factuais por IA).',
         '- Notas válidas pelo protocolo atual: **2340** (49 aprovações humanas históricas + 2291 revisões factuais por IA).'),
        ('- Progresso: **2240 / 1.000.000 (0,2240%)**; faltam 997.760 notas válidas.',
         '- Progresso: **2340 / 1.000.000 (0,2340%)**; faltam 997.660 notas válidas.'),
        ('- Segundo lote em andamento `software-devops-2000-0002`: **200 / 2.000** notas válidas (10,00%); 200 por IA ([tranche 2](exports/reports/ai-review-software-devops-2000-0002-tranche-02.md) e [reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-02.md)); faltam 1800 notas materiais.',
         '- Segundo lote em andamento `software-devops-2000-0002`: **300 / 2.000** notas válidas (15,00%); 300 por IA ([tranche 3](exports/reports/ai-review-software-devops-2000-0002-tranche-03.md) e [reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-03.md)); faltam 1700 notas materiais.'),
    ])

    apply(KF / 'README-1M.md', [
        ('tem 2240 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 2191 revisões factuais por IA registradas separadamente). O diretório ativo tem 2340 arquivos Markdown, incluindo 100 notas legadas com pendências, ainda excluídas da contagem. O segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) está em andamento com 200/2.000 notas válidas ([relatório factual por IA da tranche 2](exports/reports/ai-review-software-devops-2000-0002-tranche-02.md) e [reconciliação da tranche 2](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-02.md)),',
         'tem 2340 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 2291 revisões factuais por IA registradas separadamente). O diretório ativo tem 2440 arquivos Markdown, incluindo 100 notas legadas com pendências, ainda excluídas da contagem. O segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) está em andamento com 300/2.000 notas válidas ([relatório factual por IA da tranche 3](exports/reports/ai-review-software-devops-2000-0002-tranche-03.md) e [reconciliação da tranche 3](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-03.md)),'),
    ])

    apply(KF / 'STATUS-CONSOLIDACAO-1M.md', [
        ('A auditoria encontrou 2340 arquivos Markdown ativos: 2240 notas substantivas passaram pelo gate e receberam revisão factual registrada (49 humanas históricas + 2191 por IA)',
         'A auditoria encontrou 2440 arquivos Markdown ativos: 2340 notas substantivas passaram pelo gate e receberam revisão factual registrada (49 humanas históricas + 2291 por IA)'),
        ('| Progresso válido global | 2240 / 1.000.000 (0,2240%) | 49 revisões humanas históricas + 2191 revisões por IA registradas separadamente |',
         '| Progresso válido global | 2340 / 1.000.000 (0,2340%) | 49 revisões humanas históricas + 2291 revisões por IA registradas separadamente |'),
        ('| Revisões factuais por IA registradas | 2191 | Relatórios das tranches 2–26 (`software-testes-2000-0001`) e tranches 1–2 (`software-devops-2000-0002`); não são humanas |',
         '| Revisões factuais por IA registradas | 2291 | Relatórios das tranches 2–26 (`software-testes-2000-0001`) e tranches 1–3 (`software-devops-2000-0002`); não são humanas |'),
        ('| Segundo lote (`software-devops-2000-0002`) | 200 / 2.000 (10,00%) | 200 IA nas tranches 1–2 ([tranche 2](exports/reports/ai-review-software-devops-2000-0002-tranche-02.md)); faltam 1800 notas substantivas |',
         '| Segundo lote (`software-devops-2000-0002`) | 300 / 2.000 (15,00%) | 300 IA nas tranches 1–3 ([tranche 3](exports/reports/ai-review-software-devops-2000-0002-tranche-03.md)); faltam 1700 notas substantivas |'),
        ('| Candidatas que passaram pelo gate automatizado | 2240 |',
         '| Candidatas que passaram pelo gate automatizado | 2340 |'),
        ('O segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) está em 200/2.000 notas válidas após a [tranche 2](exports/reports/ai-review-software-devops-2000-0002-tranche-02.md) ([reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-02.md)).',
         'O segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) está em 300/2.000 notas válidas após a [tranche 3](exports/reports/ai-review-software-devops-2000-0002-tranche-03.md) ([reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-03.md)).'),
        ('3. Continuar o segundo lote `software-devops-2000-0002` (atualmente em 200/2.000; faltam 1800 notas substantivas) e os 498 lotes subsequentes,',
         '3. Continuar o segundo lote `software-devops-2000-0002` (atualmente em 300/2.000; faltam 1700 notas substantivas) e os 498 lotes subsequentes,'),
    ])

    apply(KF / 'PLANO-CONTINUO-1M.md', [
        ('- Notas válidas globais: **2240** (49 aprovações humanas históricas + 2191 revisões factuais por IA).',
         '- Notas válidas globais: **2340** (49 aprovações humanas históricas + 2291 revisões factuais por IA).'),
        ('- Progresso: **2240 / 1.000.000 (0,2240%)**; faltam **997.760** notas válidas.',
         '- Progresso: **2340 / 1.000.000 (0,2340%)**; faltam **997.660** notas válidas.'),
        ('- Segundo lote atual `software-devops-2000-0002`: **200 / 2.000 (10,00%)** notas válidas (200 IA nas tranches 1–2); faltam **1800** notas substantivas.',
         '- Segundo lote atual `software-devops-2000-0002`: **300 / 2.000 (15,00%)** notas válidas (300 IA nas tranches 1–3); faltam **1700** notas substantivas.'),
        ('- Arquivos Markdown ativos: **2340**; 100 com pendências de qualidade, excluídos da contagem.',
         '- Arquivos Markdown ativos: **2440**; 100 com pendências de qualidade, excluídos da contagem.'),
        ('| 5 | Rodar gate, testes, auditorias e diff | **Concluído para o estado atual** | Lote 1: 2000/2000 (`complete`). Lote 2 (`software-devops-2000-0002`): 200/200 no gate (200 IA). Global: 2340 arquivos, 2240 válidas, 100 com pendências legadas; veja a [reconciliação da tranche 2 do lote 2](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-02.md). |',
         '| 5 | Rodar gate, testes, auditorias e diff | **Concluído para o estado atual** | Lote 1: 2000/2000 (`complete`). Lote 2 (`software-devops-2000-0002`): 300/300 no gate (300 IA). Global: 2440 arquivos, 2340 válidas, 100 com pendências legadas; veja a [reconciliação da tranche 3 do lote 2](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-03.md). |'),
        ('| 8 | Abrir lotes subsequentes de 2.000 notas | **Em andamento (lote 2 em 10%)** | Segundo lote `software-devops-2000-0002` com 200/2.000 notas válidas nas tranches 1–2; restam 1800 notas neste lote e 498 lotes subsequentes. |',
         '| 8 | Abrir lotes subsequentes de 2.000 notas | **Em andamento (lote 2 em 15%)** | Segundo lote `software-devops-2000-0002` com 300/2.000 notas válidas nas tranches 1–3; restam 1700 notas neste lote e 498 lotes subsequentes. |'),
        ('Progresso atual: 2240 notas válidas, 1/500 lotes completos.',
         'Progresso atual: 2340 notas válidas, 1/500 lotes completos.'),
    ])

    apply(KF / 'RECOVERY-AND-SCALE-NOTE.md', [
        ('há 2340 arquivos: 100 legados com pendências e 2240 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 2191 revisões por IA). O primeiro lote `software-testes-2000-0001` atingiu 2000/2.000 notas válidas (9 humanas + 1991 IA), com status `complete` ([tranche 26](exports/reports/ai-review-software-testes-2000-0001-tranche-26.md) e [reconciliação](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-26.md)); o segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) está em andamento (`in_progress`) com 200/2.000 notas válidas revisadas por IA até a [tranche 2](exports/reports/ai-review-software-devops-2000-0002-tranche-02.md), com [reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-02.md);',
         'há 2440 arquivos: 100 legados com pendências e 2340 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 2291 revisões por IA). O primeiro lote `software-testes-2000-0001` atingiu 2000/2.000 notas válidas (9 humanas + 1991 IA), com status `complete` ([tranche 26](exports/reports/ai-review-software-testes-2000-0001-tranche-26.md) e [reconciliação](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-26.md)); o segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) está em andamento (`in_progress`) com 300/2.000 notas válidas revisadas por IA até a [tranche 3](exports/reports/ai-review-software-devops-2000-0002-tranche-03.md), com [reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-03.md);'),
        ('4. Continuar o segundo lote `software-devops-2000-0002` (200/2.000; faltam 1800 notas qualificadas) até 2.000 antes de abrir os 498 lotes seguintes.',
         '4. Continuar o segundo lote `software-devops-2000-0002` (300/2.000; faltam 1700 notas qualificadas) até 2.000 antes de abrir os 498 lotes seguintes.'),
    ])

    apply(KF / '00-home-vault' / 'Home.md', [
        ('- [[MOC-DevOps-Software-0008]] — 200 notas do segundo lote de escala `software-devops-2000-0002` (meta: 2.000); 200 revisões factuais por IA.',
         '- [[MOC-DevOps-Software-0008]] — 300 notas do segundo lote de escala `software-devops-2000-0002` (meta: 2.000); 300 revisões factuais por IA.'),
        ('[[human-review-queue|Registro de revisões factuais]] — 49 aprovações humanas e 2191 aprovações por IA, identificadas separadamente.',
         '[[human-review-queue|Registro de revisões factuais]] — 49 aprovações humanas e 2291 aprovações por IA, identificadas separadamente.'),
        ('[[note-quality-audit|Auditoria de qualidade]] — 2240 notas válidas pelo protocolo atual (49 humanas + 2191 IA) e 100 notas legadas com falhas.',
         '[[note-quality-audit|Auditoria de qualidade]] — 2340 notas válidas pelo protocolo atual (49 humanas + 2291 IA) e 100 notas legadas com falhas.'),
    ])

    apply(KF / '00-home-vault' / 'Indice-Global.md', [
        ('- Arquivos Markdown em `domains/`: **2340** (100 sementes legadas + 2240 notas autorais substantivas).',
         '- Arquivos Markdown em `domains/`: **2440** (100 sementes legadas + 2340 notas autorais substantivas).'),
        ('- Candidatas aprovadas no gate automatizado: **2240**; revisões humanas registradas: **49**; revisões factuais por IA: **2191**; 100 sementes legadas mantêm pendências.',
         '- Candidatas aprovadas no gate automatizado: **2340**; revisões humanas registradas: **49**; revisões factuais por IA: **2291**; 100 sementes legadas mantêm pendências.'),
        ('- Os lotes atuais totalizam 2240 notas válidas pelo protocolo; o segundo lote [`software-devops-2000-0002`](../exports/batches/software-devops-2000-0002.md) tem 200/2.000 ([tranche 2](../exports/reports/ai-review-software-devops-2000-0002-tranche-02.md), [reconciliação da tranche 2](../exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-02.md) e [[MOC-DevOps-Software-0008]]),',
         '- Os lotes atuais totalizam 2340 notas válidas pelo protocolo; o segundo lote [`software-devops-2000-0002`](../exports/batches/software-devops-2000-0002.md) tem 300/2.000 ([tranche 3](../exports/reports/ai-review-software-devops-2000-0002-tranche-03.md), [reconciliação da tranche 3](../exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-03.md) e [[MOC-DevOps-Software-0008]]),'),
    ])
    print("reconciliação concluída")


if __name__ == "__main__":
    main()
