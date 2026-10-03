#!/usr/bin/env python3
"""Reconcile batch software-seguranca-2000-0003 tranche 01 (IDs 1-100, opening batch 3 at 100/2000) across manifest, MOC, review registry and status docs."""
from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KF = ROOT / "knowledge-federation"
SCRIPTS = KF / "scripts"
BATCH_ID = "software-seguranca-2000-0003"
REPORT_NAME = "ai-review-software-seguranca-2000-0003-tranche-01.md"
RECON_NAME = "batch-reconciliation-software-seguranca-2000-0003-tranche-01.md"
DATE = "2026-10-03"


def load_builder():
    spec = importlib.util.spec_from_file_location("bs01", SCRIPTS / "_build_seguranca_t01.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_groups(bs01):
    groups = []
    for path in sorted(bs01.DATA_DIR.glob("*.txt")):
        context, rows = bs01.parse_group(path)
        groups.append((context, rows))
    return groups


def render_manifest(groups) -> str:
    lines = [
        f"# Lote `{BATCH_ID}` — Engenharia de Segurança de Software, AppSec, DevSecOps e IAM",
        "",
        f"Manifesto auditável do terceiro lote de escala (`{BATCH_ID}`), focado em segurança de aplicações (AppSec), segurança da cadeia de suprimentos de software (SBOM/VEX/SCA/SLSA/Scorecard), varredura de segredos, DAST e motores de autorização fina (ReBAC/ABAC/PBAC).",
        "",
        "## Resumo do estado atual",
        "",
        "- Domínio / subdomínio: `software` / `seguranca` (`knowledge-federation/domains/software-0009/software/seguranca/`)",
        "- Meta do lote: **2.000 notas substantivas**",
        "- Notas efetivamente redigidas até agora: **100 / 2.000 (5,00%)**",
        "- Gate automatizado: **100/100 aprovadas** (conteúdo mínimo, seções, fontes específicas e wikilinks; reexecutado após a tranche 1)",
        "- Revisão factual humana: **0/100**",
        "- Revisão factual por IA: **100/100**",
        "- Contabilizadas como válidas: **100/100**",
        "- Revisor das 100 notas aprovadas por IA: `Arena.ai Agent Mode`, com relatórios específicos; não são aprovações humanas",
        "- Status do lote maior: `in_progress`; tranche 1 (100 notas, IDs 1–100) foi conferida factualmente por IA e aprovada sob o protocolo atualizado",
        "- MOC do lote: [`MOC-Seguranca-Software-0009.md`](../../00-home-vault/MOCs/MOC-Seguranca-Software-0009.md)",
        "- Relatório de qualidade do lote: [`note-quality-software-seguranca-2000-0003.md`](../reports/note-quality-software-seguranca-2000-0003.md)",
        f"- Reconciliação estrutural mais recente do manifesto/fila: [`{RECON_NAME}`](../reports/{RECON_NAME})",
        f"- Relatórios factuais por IA: [`tranche 1`](../reports/{REPORT_NAME})",
        "",
        "Existem 100 notas materiais listadas abaixo; não há IDs reservados, placeholders ou registros virtuais para as 1.900 restantes.",
        "",
        "## Tranche 1 — Gitleaks, TruffleHog, Google OSV-Scanner V2, OWASP Dependency-Track, OWASP ZAP, ProjectDiscovery Nuclei, OpenFGA, AuthZed SpiceDB, Cerbos e OpenSSF Scorecard (100 notas; revisão factual por IA registrada)",
        "",
    ]
    for context, rows in groups:
        lines.append(f"### {context['group_title']}")
        lines.append("")
        for index, row in enumerate(rows):
            number = int(context["first"]) + index
            lines.append(
                f"{number}. [{row['title']}](../../domains/software-0009/software/seguranca/{row['slug']}.md)"
            )
        lines.append("")
    lines.extend(
        [
            "## Critérios e próximo passo",
            "",
            "As 100 notas 1–100 da tranche 1 têm revisão factual por IA registrada no relatório vinculado. O lote continua incompleto: são 100/2.000 notas válidas, restando 1.900 notas materiais.",
            "",
        ]
    )
    return "\n".join(lines)


def render_moc(groups) -> str:
    lines = [
        "---",
        "tipo: moc-lote",
        f"lote: {BATCH_ID}",
        "dominio: software",
        "subdominio: seguranca",
        f"ultima_verificacao: {DATE}",
        "tags: [moc, software, seguranca, appsec, devsecops, iam, supply-chain]",
        'aliases: ["MOC Segurança de Software 0009"]',
        "---",
        "# MOC — Segurança de Software, AppSec, DevSecOps e Autorização (`software-0009`)",
        "",
        f"Índice das 100 notas substantivas redigidas até agora no lote `{BATCH_ID}`, cuja meta é 2.000. As 100 passaram pelo gate automatizado e receberam revisão factual por IA registrada separadamente (nenhuma delas é aprovação humana).",
        "",
        "## Tranche 1 — Gitleaks, TruffleHog, Google OSV-Scanner V2, OWASP Dependency-Track, OWASP ZAP, ProjectDiscovery Nuclei, OpenFGA, AuthZed SpiceDB, Cerbos e OpenSSF Scorecard",
        "",
    ]
    for context, rows in groups:
        lines.append(f"### {context['group_title']}")
        lines.append("")
        for index, row in enumerate(rows):
            number = int(context["first"]) + index
            lines.append(f"{number}. [[{row['slug']}]] — {row['summary']}")
        lines.append("")
    lines.extend(
        [
            "## Estado editorial",
            "",
            f"O gate automatizado foi aprovado por 100/100 notas e as 100 contam como válidas pelo protocolo atualizado, com revisão factual por IA registrada separadamente. O lote de 2.000 continua `in_progress` (100 notas substantivas; 1.900 ainda não produzidas). Consulte o [manifesto](../../exports/batches/{BATCH_ID}.md), a [auditoria de qualidade](../../exports/reports/note-quality-{BATCH_ID}.md) e a [reconciliação mais recente do manifesto/fila](../../exports/reports/{RECON_NAME}). Os relatórios factuais por IA são [tranche 1](../../exports/reports/{REPORT_NAME}).",
            "",
            "## Conexões com o restante do vault",
            "",
            "- [[MOC-software]]",
            "- [[MOC-Seguranca-Web-e-APIs]]",
            "- [[MOC-Operacao-e-Seguranca-Kubernetes]]",
            "- [[MOC-Testes-Software-0007]]",
            "- [[MOC-DevOps-Software-0008]]",
            "",
        ]
    )
    return "\n".join(lines)


def review_rows(groups) -> str:
    lines = []
    for context, rows in groups:
        for index, row in enumerate(rows):
            number = int(context["first"]) + index
            position = 4041 + (number - 1)
            lines.append(
                f"| {position} | `{BATCH_ID}` | [{row['title']}](../../domains/software-0009/software/seguranca/{row['slug']}.md) "
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
    bs01 = load_builder()
    groups = load_groups(bs01)
    total = sum(len(rows) for _, rows in groups)
    if total != 100 or int(groups[0][0]["first"]) != 1 or int(groups[-1][0]["first"]) != 91:
        raise SystemExit(f"dados inesperados: {total} notas, primeiro grupo em {groups[0][0]['first']}")

    manifest = KF / "exports" / "batches" / f"{BATCH_ID}.md"
    moc = KF / "00-home-vault" / "MOCs" / "MOC-Seguranca-Software-0009.md"
    queue = KF / "exports" / "reports" / "human-review-queue.md"
    moc_software = KF / "00-home-vault" / "MOCs" / "MOC-software.md"

    manifest.parent.mkdir(parents=True, exist_ok=True)
    moc.parent.mkdir(parents=True, exist_ok=True)
    manifest.write_text(render_manifest(groups), encoding="utf-8")
    print(f"ok {manifest.relative_to(ROOT)}")
    moc.write_text(render_moc(groups), encoding="utf-8")
    print(f"ok {moc.relative_to(ROOT)}")

    insert_before(queue, "## Regra de contagem", review_rows(groups), marker="| 4041 | `software-seguranca-2000-0003` |")

    apply(
        queue,
        [
            (
                "distingue 3991 revisões factuais realizadas por IA nos lotes `software-testes-2000-0001` (1991) e `software-devops-2000-0002` (2000)",
                "distingue 4091 revisões factuais realizadas por IA nos lotes `software-testes-2000-0001` (1991), `software-devops-2000-0002` (2000) e `software-seguranca-2000-0003` (100)",
            ),
            (
                "- Aprovações por IA registradas separadamente: **3991**.",
                "- Aprovações por IA registradas separadamente: **4091**.",
            ),
            (
                "- Notas válidas contabilizadas (gate + revisão humana ou IA): **4040**.",
                "- Notas válidas contabilizadas (gate + revisão humana ou IA): **4140**.",
            ),
            (
                "As 3991 linhas `APROVADA POR IA` (nº 50–4040) correspondem às 1991 notas 10–2000 das tranches 2–26 do lote `software-testes-2000-0001` e às 2000 notas 1–2000 das tranches 1–20 do lote `software-devops-2000-0002`",
                "As 4091 linhas `APROVADA POR IA` (nº 50–4140) correspondem às 1991 notas 10–2000 das tranches 2–26 do lote `software-testes-2000-0001`, às 2000 notas 1–2000 das tranches 1–20 do lote `software-devops-2000-0002` e às 100 notas 1–100 da tranche 1 do lote `software-seguranca-2000-0003`",
            ),
        ],
    )

    apply(
        ROOT / "README.md",
        [
            (
                "| Notas válidas contabilizadas | 4040 / 1.000.000 (0,4040%) | 49 com aprovação humana histórica + 3991 com revisão factual por IA |",
                "| Notas válidas contabilizadas | 4140 / 1.000.000 (0,4140%) | 49 com aprovação humana histórica + 4091 com revisão factual por IA |",
            ),
            (
                "| Notas com revisão factual por IA registrada | 3991 | Revisões dos lotes de escala (1991 no lote 1 + 2000 no lote 2), com relatórios por tranche; não são humanas |",
                "| Notas com revisão factual por IA registrada | 4091 | Revisões dos lotes de escala (1991 no lote 1 + 2000 no lote 2 + 100 no lote 3), com relatórios por tranche; não são humanas |",
            ),
            (
                "| Segundo lote `software-devops-2000-0002` | 2000 / 2.000 (100,00%) | 2000 aprovadas por IA nas tranches 1–20; lote concluído (`complete`) |",
                "| Segundo lote `software-devops-2000-0002` | 2000 / 2.000 (100,00%) | 2000 aprovadas por IA nas tranches 1–20; lote concluído (`complete`) |\n| Terceiro lote `software-seguranca-2000-0003` | 100 / 2.000 (5,00%) | 100 aprovadas por IA na tranche 1; faltam 1.900 notas substantivas |",
            ),
            (
                "| Arquivos Markdown ativos em `knowledge-federation/domains/` | 4140 | 100 notas legadas com pendências + 4040 notas autorais substantivas |",
                "| Arquivos Markdown ativos em `knowledge-federation/domains/` | 4240 | 100 notas legadas com pendências + 4140 notas autorais substantivas |",
            ),
            (
                "e o segundo lote concluído é [`software-devops-2000-0002`](knowledge-federation/exports/batches/software-devops-2000-0002.md) (2000/2.000, `complete`): todas as 2000 notas materiais passaram pelo gate e revisão factual por IA até a [tranche 20](knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-20.md) ([reconciliação](knowledge-federation/exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-20.md), [auditoria do lote](knowledge-federation/exports/reports/note-quality-software-devops-2000-0002.md) e [MOC de DevOps](knowledge-federation/00-home-vault/MOCs/MOC-DevOps-Software-0008.md)).",
                "o segundo lote concluído é [`software-devops-2000-0002`](knowledge-federation/exports/batches/software-devops-2000-0002.md) (2000/2.000, `complete`, [tranche 20](knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-20.md), [reconciliação](knowledge-federation/exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-20.md), [auditoria do lote](knowledge-federation/exports/reports/note-quality-software-devops-2000-0002.md) e [MOC de DevOps](knowledge-federation/00-home-vault/MOCs/MOC-DevOps-Software-0008.md)), e o terceiro lote em andamento é [`software-seguranca-2000-0003`](knowledge-federation/exports/batches/software-seguranca-2000-0003.md): 100 notas materiais já passaram pelo gate e revisão factual por IA na [tranche 1](knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-01.md) ([reconciliação](knowledge-federation/exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-01.md), [auditoria do lote](knowledge-federation/exports/reports/note-quality-software-seguranca-2000-0003.md) e [MOC de Segurança](knowledge-federation/00-home-vault/MOCs/MOC-Seguranca-Software-0009.md)), com meta de 2.000.",
            ),
        ],
    )

    apply(
        KF / "README.md",
        [
            (
                "- Arquivos Markdown ativos: **4140** (100 notas legadas com pendências + 4040 notas autorais substantivas).",
                "- Arquivos Markdown ativos: **4240** (100 notas legadas com pendências + 4140 notas autorais substantivas).",
            ),
            (
                "- Notas válidas pelo protocolo atual: **4040** (49 aprovações humanas históricas + 3991 revisões factuais por IA).",
                "- Notas válidas pelo protocolo atual: **4140** (49 aprovações humanas históricas + 4091 revisões factuais por IA).",
            ),
            (
                "- Progresso: **4040 / 1.000.000 (0,4040%)**; faltam 995.960 notas válidas.",
                "- Progresso: **4140 / 1.000.000 (0,4140%)**; faltam 995.860 notas válidas.",
            ),
            (
                "- Segundo lote concluído `software-devops-2000-0002`: **2000 / 2.000** notas válidas (100,00%); 2000 por IA ([tranche 20](exports/reports/ai-review-software-devops-2000-0002-tranche-20.md) e [reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-20.md)); status `complete`.",
                "- Segundo lote concluído `software-devops-2000-0002`: **2000 / 2.000** notas válidas (100,00%); 2000 por IA ([tranche 20](exports/reports/ai-review-software-devops-2000-0002-tranche-20.md) e [reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-20.md)); status `complete`.\n- Terceiro lote em andamento `software-seguranca-2000-0003`: **100 / 2.000** notas válidas (5,00%); 100 por IA ([tranche 1](exports/reports/ai-review-software-seguranca-2000-0003-tranche-01.md) e [reconciliação](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-01.md)); faltam 1.900 notas materiais.",
            ),
        ],
    )

    apply(
        KF / "README-1M.md",
        [
            (
                "tem 4040 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 3991 revisões factuais por IA registradas separadamente). O diretório ativo tem 4140 arquivos Markdown, incluindo 100 notas legadas com pendências, ainda excluídas da contagem. O segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) está concluído (`complete`) com 2000/2.000 notas válidas ([relatório factual por IA da tranche 20](exports/reports/ai-review-software-devops-2000-0002-tranche-20.md) e [reconciliação da tranche 20](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-20.md)),",
                "tem 4140 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 4091 revisões factuais por IA registradas separadamente). O diretório ativo tem 4240 arquivos Markdown, incluindo 100 notas legadas com pendências, ainda excluídas da contagem. O terceiro lote [`software-seguranca-2000-0003`](exports/batches/software-seguranca-2000-0003.md) está em andamento com 100/2.000 notas válidas ([relatório factual por IA da tranche 1](exports/reports/ai-review-software-seguranca-2000-0003-tranche-01.md) e [reconciliação da tranche 1](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-01.md)), após o segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) atingir 2000/2.000 (`complete`),",
            ),
        ],
    )

    apply(
        KF / "STATUS-CONSOLIDACAO-1M.md",
        [
            (
                "A auditoria encontrou 4140 arquivos Markdown ativos: 4040 notas substantivas passaram pelo gate e receberam revisão factual registrada (49 humanas históricas + 3991 por IA)",
                "A auditoria encontrou 4240 arquivos Markdown ativos: 4140 notas substantivas passaram pelo gate e receberam revisão factual registrada (49 humanas históricas + 4091 por IA)",
            ),
            (
                "| Progresso válido global | 4040 / 1.000.000 (0,4040%) | 49 revisões humanas históricas + 3991 revisões por IA registradas separadamente |",
                "| Progresso válido global | 4140 / 1.000.000 (0,4140%) | 49 revisões humanas históricas + 4091 revisões por IA registradas separadamente |",
            ),
            (
                "| Revisões factuais por IA registradas | 3991 | Relatórios das tranches 2–26 (`software-testes-2000-0001`) e tranches 1–20 (`software-devops-2000-0002`); não são humanas |",
                "| Revisões factuais por IA registradas | 4091 | Relatórios das tranches 2–26 (`software-testes-2000-0001`), tranches 1–20 (`software-devops-2000-0002`) e tranche 1 (`software-seguranca-2000-0003`); não são humanas |",
            ),
            (
                "| Segundo lote (`software-devops-2000-0002`) | 2000 / 2.000 (100,00%) | 2000 IA nas tranches 1–20 ([tranche 20](exports/reports/ai-review-software-devops-2000-0002-tranche-20.md)); lote concluído (`complete`) |",
                "| Segundo lote (`software-devops-2000-0002`) | 2000 / 2.000 (100,00%) | 2000 IA nas tranches 1–20 ([tranche 20](exports/reports/ai-review-software-devops-2000-0002-tranche-20.md)); lote concluído (`complete`) |\n| Terceiro lote (`software-seguranca-2000-0003`) | 100 / 2.000 (5,00%) | 100 IA na tranche 1 ([tranche 1](exports/reports/ai-review-software-seguranca-2000-0003-tranche-01.md)); faltam 1.900 notas substantivas |",
            ),
            (
                "| Candidatas que passaram pelo gate automatizado | 4040 |",
                "| Candidatas que passaram pelo gate automatizado | 4140 |",
            ),
            (
                "O segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) atingiu 2000/2.000 notas válidas (`complete`) após a [tranche 20](exports/reports/ai-review-software-devops-2000-0002-tranche-20.md) ([reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-20.md)).",
                "O segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) atingiu 2000/2.000 notas válidas (`complete`) após a [tranche 20](exports/reports/ai-review-software-devops-2000-0002-tranche-20.md) ([reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-20.md)), e o terceiro lote [`software-seguranca-2000-0003`](exports/batches/software-seguranca-2000-0003.md) está em 100/2.000 notas válidas após a [tranche 1](exports/reports/ai-review-software-seguranca-2000-0003-tranche-01.md) ([reconciliação](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-01.md)).",
            ),
            (
                "3. Segundo lote `software-devops-2000-0002` concluído em 2000/2.000 (`complete`); abrir e avançar os 498 lotes subsequentes,",
                "3. Continuar o terceiro lote `software-seguranca-2000-0003` (atualmente em 100/2.000; faltam 1.900 notas substantivas) e os 497 lotes subsequentes,",
            ),
        ],
    )

    apply(
        KF / "PLANO-CONTINUO-1M.md",
        [
            (
                "- Notas válidas globais: **4040** (49 aprovações humanas históricas + 3991 revisões factuais por IA).",
                "- Notas válidas globais: **4140** (49 aprovações humanas históricas + 4091 revisões factuais por IA).",
            ),
            (
                "- Progresso: **4040 / 1.000.000 (0,4040%)**; faltam **995.960** notas válidas.",
                "- Progresso: **4140 / 1.000.000 (0,4140%)**; faltam **995.860** notas válidas.",
            ),
            (
                "- Segundo lote `software-devops-2000-0002`: **2000 / 2.000 (100,00%)** notas válidas (2000 IA nas tranches 1–20); concluído (`complete`).",
                "- Segundo lote `software-devops-2000-0002`: **2000 / 2.000 (100,00%)** notas válidas (2000 IA nas tranches 1–20); concluído (`complete`).\n- Terceiro lote atual `software-seguranca-2000-0003`: **100 / 2.000 (5,00%)** notas válidas (100 IA na tranche 1); faltam **1.900** notas substantivas.",
            ),
            (
                "- Arquivos Markdown ativos: **4140**; 100 com pendências de qualidade, excluídos da contagem.",
                "- Arquivos Markdown ativos: **4240**; 100 com pendências de qualidade, excluídos da contagem.",
            ),
            (
                "| 5 | Rodar gate, testes, auditorias e diff | **Concluído para o estado atual** | Lote 1: 2000/2000 (`complete`). Lote 2 (`software-devops-2000-0002`): 2000/2000 no gate (2000 IA, `complete`). Global: 4140 arquivos, 4040 válidas, 100 com pendências legadas; veja a [reconciliação da tranche 20 do lote 2](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-20.md). |",
                "| 5 | Rodar gate, testes, auditorias e diff | **Concluído para o estado atual** | Lote 1: 2000/2000 (`complete`). Lote 2: 2000/2000 (`complete`). Lote 3 (`software-seguranca-2000-0003`): 100/100 no gate (100 IA). Global: 4240 arquivos, 4140 válidas, 100 com pendências legadas; veja a [reconciliação da tranche 1 do lote 3](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-01.md). |",
            ),
            (
                "| 8 | Abrir lotes subsequentes de 2.000 notas | **Lote 2 concluído (100%); 498 lotes restantes** | Segundo lote `software-devops-2000-0002` concluído (`complete`) com 2000/2.000 notas válidas nas tranches 1–20; restam 498 lotes subsequentes. |",
                "| 8 | Abrir lotes subsequentes de 2.000 notas | **Em andamento (lote 3 em 5%)** | Terceiro lote `software-seguranca-2000-0003` aberto com 100/2.000 notas válidas na tranche 1; restam 1.900 notas neste lote e 497 lotes subsequentes. |",
            ),
            (
                "Progresso atual: 4040 notas válidas, 2/500 lotes completos.",
                "Progresso atual: 4140 notas válidas, 2/500 lotes completos.",
            ),
        ],
    )

    apply(
        KF / "RECOVERY-AND-SCALE-NOTE.md",
        [
            (
                "há 4140 arquivos: 100 legados com pendências e 4040 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 3991 revisões por IA). O primeiro lote `software-testes-2000-0001` atingiu 2000/2.000 notas válidas (9 humanas + 1991 IA), com status `complete` ([tranche 26](exports/reports/ai-review-software-testes-2000-0001-tranche-26.md) e [reconciliação](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-26.md)); o segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) atingiu 2000/2.000 notas válidas (`complete`) revisadas por IA até a [tranche 20](exports/reports/ai-review-software-devops-2000-0002-tranche-20.md), com [reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-20.md);",
                "há 4240 arquivos: 100 legados com pendências e 4140 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 4091 revisões por IA). O primeiro lote `software-testes-2000-0001` atingiu 2000/2.000 notas válidas (9 humanas + 1991 IA, `complete`); o segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) atingiu 2000/2.000 notas válidas (`complete`, [tranche 20](exports/reports/ai-review-software-devops-2000-0002-tranche-20.md)); e o terceiro lote [`software-seguranca-2000-0003`](exports/batches/software-seguranca-2000-0003.md) está em andamento (`in_progress`) com 100/2.000 notas válidas revisadas por IA na [tranche 1](exports/reports/ai-review-software-seguranca-2000-0003-tranche-01.md), com [reconciliação](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-01.md);",
            ),
            (
                "4. Segundo lote `software-devops-2000-0002` concluído com 2000/2.000 notas qualificadas (`complete`); abrir os 498 lotes seguintes.",
                "4. Continuar o terceiro lote `software-seguranca-2000-0003` (100/2.000; faltam 1.900 notas qualificadas) até 2.000 antes de abrir os 497 lotes seguintes.",
            ),
        ],
    )

    apply(
        KF / "00-home-vault" / "Home.md",
        [
            (
                "- [[MOC-DevOps-Software-0008]] — 2000 notas do segundo lote de escala `software-devops-2000-0002` (meta de 2.000 concluída, `complete`); 2000 revisões factuais por IA.",
                "- [[MOC-DevOps-Software-0008]] — 2000 notas do segundo lote de escala `software-devops-2000-0002` (meta de 2.000 concluída, `complete`); 2000 revisões factuais por IA.\n- [[MOC-Seguranca-Software-0009]] — 100 notas do terceiro lote de escala `software-seguranca-2000-0003` (meta: 2.000); 100 revisões factuais por IA.",
            ),
            (
                "[[human-review-queue|Registro de revisões factuais]] — 49 aprovações humanas e 3991 aprovações por IA, identificadas separadamente.",
                "[[human-review-queue|Registro de revisões factuais]] — 49 aprovações humanas e 4091 aprovações por IA, identificadas separadamente.",
            ),
            (
                "[[note-quality-audit|Auditoria de qualidade]] — 4040 notas válidas pelo protocolo atual (49 humanas + 3991 IA) e 100 notas legadas com falhas.",
                "[[note-quality-audit|Auditoria de qualidade]] — 4140 notas válidas pelo protocolo atual (49 humanas + 4091 IA) e 100 notas legadas com falhas.",
            ),
        ],
    )

    apply(
        KF / "00-home-vault" / "Indice-Global.md",
        [
            (
                "- Arquivos Markdown em `domains/`: **4140** (100 sementes legadas + 4040 notas autorais substantivas).",
                "- Arquivos Markdown em `domains/`: **4240** (100 sementes legadas + 4140 notas autorais substantivas).",
            ),
            (
                "- Candidatas aprovadas no gate automatizado: **4040**; revisões humanas registradas: **49**; revisões factuais por IA: **3991**; 100 sementes legadas mantêm pendências.",
                "- Candidatas aprovadas no gate automatizado: **4140**; revisões humanas registradas: **49**; revisões factuais por IA: **4091**; 100 sementes legadas mantêm pendências.",
            ),
            (
                "- Os lotes atuais totalizam 4040 notas válidas pelo protocolo; o segundo lote [`software-devops-2000-0002`](../exports/batches/software-devops-2000-0002.md) atingiu 2000/2.000 (`complete`, [tranche 20](../exports/reports/ai-review-software-devops-2000-0002-tranche-20.md), [reconciliação da tranche 20](../exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-20.md) e [[MOC-DevOps-Software-0008]]),",
                "- Os lotes atuais totalizam 4140 notas válidas pelo protocolo; o terceiro lote [`software-seguranca-2000-0003`](../exports/batches/software-seguranca-2000-0003.md) tem 100/2.000 ([tranche 1](../exports/reports/ai-review-software-seguranca-2000-0003-tranche-01.md), [reconciliação da tranche 1](../exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-01.md) e [[MOC-Seguranca-Software-0009]]), o segundo lote [`software-devops-2000-0002`](../exports/batches/software-devops-2000-0002.md) atingiu 2000/2.000 (`complete`, [tranche 20](../exports/reports/ai-review-software-devops-2000-0002-tranche-20.md), [reconciliação da tranche 20](../exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-20.md) e [[MOC-DevOps-Software-0008]]),",
            ),
        ],
    )
    print("reconciliação concluída")


if __name__ == "__main__":
    main()
