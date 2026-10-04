#!/usr/bin/env python3
"""Initialize and reconcile batch software-devops-2000-0002 tranche 1 (IDs 1-100) across manifest, MOC, review registry and status docs."""
from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KF = ROOT / "knowledge-federation"
SCRIPTS = KF / "scripts"
BATCH_ID = "software-devops-2000-0002"
REPORT_NAME = "ai-review-software-devops-2000-0002-tranche-01.md"
RECON_NAME = "batch-reconciliation-software-devops-2000-0002-tranche-01.md"
DATE = "2026-10-03"


def load_builder():
    spec = importlib.util.spec_from_file_location("bd01", SCRIPTS / "_build_devops_t01.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_groups(bd01):
    groups = []
    for path in sorted(bd01.DATA_DIR.glob("*.txt")):
        context, rows = bd01.parse_group(path)
        groups.append((context, rows))
    return groups


def manifest_section(groups) -> str:
    lines = ["## Tranche 1 — OpenTelemetry Collector, Argo CD, Helm, OpenTofu, Ansible, Flux v2, Kustomize, containerd, Jaeger e Tekton Pipelines (100 notas; revisão factual por IA registrada)", ""]
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
    lines = ["## Tranche 1 — OpenTelemetry Collector, Argo CD, Helm, OpenTofu, Ansible, Flux v2, Kustomize, containerd, Jaeger e Tekton Pipelines", ""]
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
    bd01 = load_builder()
    groups = load_groups(bd01)
    total = sum(len(rows) for _, rows in groups)
    if total != 100 or int(groups[0][0]["first"]) != 1 or int(groups[-1][0]["first"]) != 91:
        raise SystemExit(f"dados inesperados: {total} notas, primeiro grupo em {groups[0][0]['first']}")

    manifest = KF / "exports" / "batches" / f"{BATCH_ID}.md"
    moc = KF / "00-home-vault" / "MOCs" / "MOC-DevOps-Software-0008.md"
    queue = KF / "exports" / "reports" / "human-review-queue.md"

    manifest_content = f"""# Lote de escala {BATCH_ID}

- Data de início: {DATE}
- Última atualização: {DATE}
- Escopo: engenharia de software — DevOps, GitOps, IaC, observabilidade e runtimes cloud-native
- Tamanho-alvo solicitado: **2.000 notas substantivas**
- Notas efetivamente redigidas até agora: **100 / 2.000 (5,00%)**
- Gate automatizado: **100/100 aprovadas** (conteúdo mínimo, seções, fontes específicas e wikilinks; reexecutado após a tranche 1)
- Revisão factual humana: **0/100**
- Revisão factual por IA: **100/100**
- Contabilizadas como válidas: **100/100**
- Revisor das 100 notas aprovadas por IA: `Arena.ai Agent Mode`, com relatórios específicos; não são aprovações humanas
- Status do lote maior: `in_progress`; tranche 1 (100 notas, IDs 1–100) foi conferida factualmente por IA e aprovada sob o protocolo atualizado
- Auditoria reproduzível do gate e links: [`note-quality-software-devops-2000-0002.md`](../reports/note-quality-software-devops-2000-0002.md)
- Reconciliação estrutural mais recente do manifesto/fila: [`batch-reconciliation-software-devops-2000-0002-tranche-01.md`](../reports/batch-reconciliation-software-devops-2000-0002-tranche-01.md)
- Relatórios factuais por IA: [`tranche 1`](../reports/ai-review-software-devops-2000-0002-tranche-01.md)
- Navegação: [`MOC-DevOps-Software-0008.md`](../../00-home-vault/MOCs/MOC-DevOps-Software-0008.md)

> **Contagem literal:** 2.000 é a meta deste segundo lote de escala, não a quantidade já criada. Existem 100 notas materiais listadas abaixo; não há IDs reservados, placeholders ou registros virtuais para as 1900 restantes. A contagem válida só avança com conteúdo substantivo, fontes específicas, gate aprovado e revisão factual humana ou por IA registrada separadamente.

{manifest_section(groups)}## Critérios e próximo passo

Cada tranche é auditada antes de ser adicionada ao lote de escala. A aprovação automática verifica estrutura, conteúdo mínimo, fontes HTTPS específicas e links; não certifica a verdade das afirmações. O protocolo atualizado aceita revisão factual humana ou por IA, registradas separadamente. As 100 notas 1–100 da tranche 1 têm revisão factual por IA registrada no relatório vinculado. O lote continua incompleto: são 100/2.000 notas válidas, restando 1900 notas materiais. Continuar em tranches de conteúdo real, sem contar placeholders, IDs ou progresso parcial como conclusão; cada nota deve ter fontes conferidas e relatório de revisão factual.
"""
    manifest.write_text(manifest_content, encoding="utf-8")
    print(f"ok {manifest.relative_to(ROOT)}")

    moc_content = f"""---
tipo: moc-lote
dominio: software
subdominio: devops
lote: {BATCH_ID}
ultima_verificacao: {DATE}
tags: [moc, dominio/software, subdominio/devops, lote/{BATCH_ID}]
aliases: ["MOC — DevOps e Plataforma Cloud-Native (software-0008)"]
---
# MOC — DevOps e Plataforma Cloud-Native (`software-0008`)

Índice das 100 notas substantivas redigidas até agora no lote `{BATCH_ID}`, cuja meta é 2.000. As 100 passaram pelo gate automatizado e têm revisão factual registrada por IA, sem converter estas últimas em aprovações humanas. Este mapa é navegação, não validação factual.

{moc_section(groups)}## Estado editorial

O gate automatizado foi aprovado por 100/100 notas e as 100 contam como válidas pelo protocolo atualizado, com revisão factual por IA registrada separadamente. O lote de 2.000 continua `in_progress` (100 notas substantivas; 1900 ainda não produzidas). Consulte o [manifesto](../../exports/batches/{BATCH_ID}.md), a [auditoria de qualidade](../../exports/reports/note-quality-software-devops-2000-0002.md) e a [reconciliação mais recente do manifesto/fila](../../exports/reports/{RECON_NAME}). Os relatórios factuais por IA são [tranche 1](../../exports/reports/{REPORT_NAME}). Consulte também o [registro de revisão humana e IA](../../exports/reports/human-review-queue.md) e o [[MOC-software]].
"""
    moc.write_text(moc_content, encoding="utf-8")
    print(f"ok {moc.relative_to(ROOT)}")

    queue_block = review_rows(groups)
    insert_before(queue, "## Regra de contagem", queue_block)

    apply(queue, [
        ('distingue 1991 revisões factuais realizadas por IA no lote `software-testes-2000-0001`',
         'distingue 2091 revisões factuais realizadas por IA nos lotes `software-testes-2000-0001` (1991) e `software-devops-2000-0002` (100)'),
        ('- Aprovações por IA registradas separadamente: **1991**.',
         '- Aprovações por IA registradas separadamente: **2091**.'),
        ('- Notas válidas contabilizadas (gate + revisão humana ou IA): **2040**.',
         '- Notas válidas contabilizadas (gate + revisão humana ou IA): **2140**.'),
        ('As 1991 linhas `APROVADA POR IA` (nº 50–2040) correspondem às notas 10–2000 e às revisões documentadas nos relatórios das tranches 2–26',
         'As 2091 linhas `APROVADA POR IA` (nº 50–2140) correspondem às 1991 notas 10–2000 das tranches 2–26 do lote `software-testes-2000-0001` e às 100 notas 1–100 da tranche 1 do lote `software-devops-2000-0002`'),
    ])

    apply(ROOT / 'README.md', [
        ('| Notas válidas contabilizadas | 2040 / 1.000.000 (0,2040%) | 49 com aprovação humana histórica + 1991 com revisão factual por IA |',
         '| Notas válidas contabilizadas | 2140 / 1.000.000 (0,2140%) | 49 com aprovação humana histórica + 2091 com revisão factual por IA |'),
        ('| Notas com revisão factual por IA registrada | 1991 | Revisões do lote atual, com relatórios por tranche; não são humanas |',
         '| Notas com revisão factual por IA registrada | 2091 | Revisões dos lotes de escala (1991 no lote 1 + 100 no lote 2), com relatórios por tranche; não são humanas |'),
        ('| Primeiro lote `software-testes-2000-0001` | 2000 / 2.000 (100%) | 9 aprovadas por humano + 1991 por IA; lote concluído (`complete`) |',
         '| Primeiro lote `software-testes-2000-0001` | 2000 / 2.000 (100%) | 9 aprovadas por humano + 1991 por IA; lote concluído (`complete`) |\n| Segundo lote `software-devops-2000-0002` | 100 / 2.000 (5,00%) | 100 aprovadas por IA na tranche 1; faltam 1900 notas substantivas |'),
        ('| Arquivos Markdown ativos em `knowledge-federation/domains/` | 2140 | 100 notas legadas com pendências + 2040 notas autorais substantivas |',
         '| Arquivos Markdown ativos em `knowledge-federation/domains/` | 2240 | 100 notas legadas com pendências + 2140 notas autorais substantivas |'),
        ('O primeiro lote concluído é `software-testes-2000-0001`: 2000 notas materiais passaram pelo gate e revisão factual (9 humanas + 1991 IA), atingindo 2.000/2.000 (100%).',
         'O primeiro lote concluído é `software-testes-2000-0001` (2000/2.000, 9 humanas + 1991 IA, `complete`), e o segundo lote em andamento é [`software-devops-2000-0002`](knowledge-federation/exports/batches/software-devops-2000-0002.md): 100 notas materiais já passaram pelo gate e revisão factual por IA na [tranche 1](knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-01.md) ([reconciliação](knowledge-federation/exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-01.md), [auditoria do lote](knowledge-federation/exports/reports/note-quality-software-devops-2000-0002.md) e [MOC de DevOps](knowledge-federation/00-home-vault/MOCs/MOC-DevOps-Software-0008.md)), com meta de 2.000.'),
    ])

    apply(KF / 'README.md', [
        ('- Arquivos Markdown ativos: **2140** (100 notas legadas com pendências + 2040 notas autorais substantivas).',
         '- Arquivos Markdown ativos: **2240** (100 notas legadas com pendências + 2140 notas autorais substantivas).'),
        ('- Notas válidas pelo protocolo atual: **2040** (49 aprovações humanas históricas + 1991 revisões factuais por IA).',
         '- Notas válidas pelo protocolo atual: **2140** (49 aprovações humanas históricas + 2091 revisões factuais por IA).'),
        ('- Progresso: **2040 / 1.000.000 (0,2040%)**; faltam 997.960 notas válidas.',
         '- Progresso: **2140 / 1.000.000 (0,2140%)**; faltam 997.860 notas válidas.'),
        ('- Primeiro lote concluído `software-testes-2000-0001`: **2000 / 2.000** notas válidas (100%); 9 humanas e 1991 por IA; status `complete`.',
         '- Primeiro lote concluído `software-testes-2000-0001`: **2000 / 2.000** notas válidas (100%); 9 humanas e 1991 por IA; status `complete`.\n- Segundo lote em andamento `software-devops-2000-0002`: **100 / 2.000** notas válidas (5,00%); 100 por IA ([tranche 1](exports/reports/ai-review-software-devops-2000-0002-tranche-01.md) e [reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-01.md)); faltam 1900 notas materiais.'),
    ])

    apply(KF / 'README-1M.md', [
        ('tem 2040 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 1991 revisões factuais por IA registradas separadamente). O diretório ativo tem 2140 arquivos Markdown, incluindo 100 notas legadas com pendências, ainda excluídas da contagem. O lote `software-testes-2000-0001` atingiu 2000/2.000 notas válidas (`complete`);',
         'tem 2140 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 2091 revisões factuais por IA registradas separadamente). O diretório ativo tem 2240 arquivos Markdown, incluindo 100 notas legadas com pendências, ainda excluídas da contagem. O segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) está em andamento com 100/2.000 notas válidas ([relatório factual por IA da tranche 1](exports/reports/ai-review-software-devops-2000-0002-tranche-01.md) e [reconciliação da tranche 1](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-01.md)), após o primeiro lote `software-testes-2000-0001` atingir 2000/2.000 notas válidas (`complete`);'),
    ])

    apply(KF / 'STATUS-CONSOLIDACAO-1M.md', [
        ('A auditoria encontrou 2140 arquivos Markdown ativos: 2040 notas substantivas passaram pelo gate e receberam revisão factual registrada (49 humanas históricas + 1991 por IA)',
         'A auditoria encontrou 2240 arquivos Markdown ativos: 2140 notas substantivas passaram pelo gate e receberam revisão factual registrada (49 humanas históricas + 2091 por IA)'),
        ('| Progresso válido global | 2040 / 1.000.000 (0,2040%) | 49 revisões humanas históricas + 1991 revisões por IA registradas separadamente |',
         '| Progresso válido global | 2140 / 1.000.000 (0,2140%) | 49 revisões humanas históricas + 2091 revisões por IA registradas separadamente |'),
        ('| Revisões factuais por IA registradas | 1991 | Relatórios das tranches 2–26 no lote `software-testes-2000-0001`; não são humanas |',
         '| Revisões factuais por IA registradas | 2091 | Relatórios das tranches 2–26 (`software-testes-2000-0001`) e tranche 1 (`software-devops-2000-0002`); não são humanas |'),
        ('| Primeiro lote | 2000 / 2.000 (100%) | 9 humanas + 1991 IA; lote concluído (`complete`) |',
         '| Primeiro lote (`software-testes-2000-0001`) | 2000 / 2.000 (100%) | 9 humanas + 1991 IA; lote concluído (`complete`) |\n| Segundo lote (`software-devops-2000-0002`) | 100 / 2.000 (5,00%) | 100 IA na [tranche 1](exports/reports/ai-review-software-devops-2000-0002-tranche-01.md); faltam 1900 notas substantivas |'),
        ('| Candidatas que passaram pelo gate automatizado | 2040 |',
         '| Candidatas que passaram pelo gate automatizado | 2140 |'),
        ('4. Resultado final do primeiro lote: 2000/2000 aprovadas pelo gate; nove revisões humanas e 1991 revisões por IA no total após a tranche 26, incluindo as 41 novas revisões das notas 1960–2000. O lote atingiu o alvo de 2.000 e passa ao estado `complete`.',
         '4. Resultado final do primeiro lote: 2000/2000 aprovadas pelo gate; nove revisões humanas e 1991 revisões por IA no total após a tranche 26, incluindo as 41 novas revisões das notas 1960–2000. O lote atingiu o alvo de 2.000 e passa ao estado `complete`. Iniciado o segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) com 100/2.000 notas válidas na [tranche 1](exports/reports/ai-review-software-devops-2000-0002-tranche-01.md) ([reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-01.md)).'),
        ('3. Depois iniciar os 499 lotes restantes, preservando 2.000 notas qualificadas por lote e total ativo de 500 lotes.',
         '3. Continuar o segundo lote `software-devops-2000-0002` (atualmente em 100/2.000; faltam 1900 notas substantivas) e os 498 lotes subsequentes, preservando 2.000 notas qualificadas por lote e total ativo de 500 lotes.'),
    ])

    apply(KF / 'PLANO-CONTINUO-1M.md', [
        ('- Notas válidas globais: **2040** (49 aprovações humanas históricas + 1991 revisões factuais por IA).',
         '- Notas válidas globais: **2140** (49 aprovações humanas históricas + 2091 revisões factuais por IA).'),
        ('- Progresso: **2040 / 1.000.000 (0,2040%)**; faltam **997.960** notas válidas.',
         '- Progresso: **2140 / 1.000.000 (0,2140%)**; faltam **997.860** notas válidas.'),
        ('- Primeiro lote `software-testes-2000-0001`: **2000 / 2.000 (100%)** notas válidas (9 humanas + 1991 IA); concluído (`complete`).',
         '- Primeiro lote `software-testes-2000-0001`: **2000 / 2.000 (100%)** notas válidas (9 humanas + 1991 IA); concluído (`complete`).\n- Segundo lote atual `software-devops-2000-0002`: **100 / 2.000 (5,00%)** notas válidas (100 IA na tranche 1); faltam **1900** notas substantivas.'),
        ('- Arquivos Markdown ativos: **2140**; 100 com pendências de qualidade, excluídos da contagem.',
         '- Arquivos Markdown ativos: **2240**; 100 com pendências de qualidade, excluídos da contagem.'),
        ('| 5 | Rodar gate, testes, auditorias e diff | **Concluído para o estado atual** | Lote: 2000/2000 no gate, 9 humanas, 1991 IA. Global: 2140 arquivos, 2040 válidas, 100 com pendências legadas; veja a [reconciliação da tranche 26](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-26.md). |',
         '| 5 | Rodar gate, testes, auditorias e diff | **Concluído para o estado atual** | Lote 1: 2000/2000 (`complete`). Lote 2 (`software-devops-2000-0002`): 100/100 no gate (100 IA). Global: 2240 arquivos, 2140 válidas, 100 com pendências legadas; veja a [reconciliação da tranche 1 do lote 2](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-01.md). |'),
        ('| 8 | Abrir lotes subsequentes de 2.000 notas | **Pendente após o lote 1** | Restam 499 lotes depois do atual; ID, placeholder ou tranche parcial não conta como lote completo. |',
         '| 8 | Abrir lotes subsequentes de 2.000 notas | **Em andamento (lote 2 iniciado)** | Segundo lote `software-devops-2000-0002` aberto com 100/2.000 notas válidas na tranche 1; restam 1900 notas neste lote e 498 lotes subsequentes. |'),
        ('Progresso atual: 2040 notas válidas, 1/500 lotes completos.',
         'Progresso atual: 2140 notas válidas, 1/500 lotes completos.'),
    ])

    apply(KF / 'RECOVERY-AND-SCALE-NOTE.md', [
        ('há 2140 arquivos: 100 legados com pendências e 2040 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 1991 revisões por IA). O lote `software-testes-2000-0001` atingiu 2000/2.000 notas válidas (9 humanas + 1991 IA), com status `complete`. As notas 1960–2000 passaram pelo gate e têm revisão factual por IA registrada na [tranche 26](exports/reports/ai-review-software-testes-2000-0001-tranche-26.md), com [reconciliação](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-26.md);',
         'há 2240 arquivos: 100 legados com pendências e 2140 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 2091 revisões por IA). O primeiro lote `software-testes-2000-0001` atingiu 2000/2.000 notas válidas (9 humanas + 1991 IA), com status `complete` ([tranche 26](exports/reports/ai-review-software-testes-2000-0001-tranche-26.md) e [reconciliação](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-26.md)); o segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) está em andamento (`in_progress`) com 100/2.000 notas válidas revisadas por IA na [tranche 1](exports/reports/ai-review-software-devops-2000-0002-tranche-01.md), com [reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-01.md);'),
        ('4. Abrir os 499 lotes seguintes de 2.000 notas somente após concluir o lote atual.',
         '4. Continuar o segundo lote `software-devops-2000-0002` (100/2.000; faltam 1900 notas qualificadas) até 2.000 antes de abrir os 498 lotes seguintes.'),
    ])

    apply(KF / '00-home-vault' / 'Home.md', [
        ('- [[MOC-Testes-Software-0007]] — 2000 notas do lote de escala (meta de 2.000 concluída); nove têm aprovação humana histórica e 1991 revisões factuais por IA.',
         '- [[MOC-Testes-Software-0007]] — 2000 notas do primeiro lote de escala (meta de 2.000 concluída); nove têm aprovação humana histórica e 1991 revisões factuais por IA.\n- [[MOC-DevOps-Software-0008]] — 100 notas do segundo lote de escala `software-devops-2000-0002` (meta: 2.000); 100 revisões factuais por IA.'),
        ('[[human-review-queue|Registro de revisões factuais]] — 49 aprovações humanas e 1991 aprovações por IA, identificadas separadamente.',
         ('[[human-review-queue|Registro de revisões factuais]] — 49 aprovações humanas e 2091 aprovações por IA, identificadas separadamente.')),
        ('[[note-quality-audit|Auditoria de qualidade]] — 2040 notas válidas pelo protocolo atual (49 humanas + 1991 IA) e 100 notas legadas com falhas.',
         '[[note-quality-audit|Auditoria de qualidade]] — 2140 notas válidas pelo protocolo atual (49 humanas + 2091 IA) e 100 notas legadas com falhas.'),
    ])

    apply(KF / '00-home-vault' / 'Indice-Global.md', [
        ('- Arquivos Markdown em `domains/`: **2140** (100 sementes legadas + 2040 notas autorais substantivas).',
         '- Arquivos Markdown em `domains/`: **2240** (100 sementes legadas + 2140 notas autorais substantivas).'),
        ('- Candidatas aprovadas no gate automatizado: **2040**; revisões humanas registradas: **49**; revisões factuais por IA: **1991**; 100 sementes legadas mantêm pendências.',
         '- Candidatas aprovadas no gate automatizado: **2140**; revisões humanas registradas: **49**; revisões factuais por IA: **2091**; 100 sementes legadas mantêm pendências.'),
        ('- Os lotes atuais totalizam 2040 notas válidas pelo protocolo; o lote `software-testes-2000-0001` atingiu 2000/2.000 (`complete`),',
         '- Os lotes atuais totalizam 2140 notas válidas pelo protocolo; o segundo lote [`software-devops-2000-0002`](../exports/batches/software-devops-2000-0002.md) tem 100/2.000 ([tranche 1](../exports/reports/ai-review-software-devops-2000-0002-tranche-01.md), [reconciliação da tranche 1](../exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-01.md) e [[MOC-DevOps-Software-0008]]), e o primeiro lote `software-testes-2000-0001` atingiu 2000/2.000 (`complete`),'),
    ])
    print("reconciliação concluída")


if __name__ == "__main__":
    main()
