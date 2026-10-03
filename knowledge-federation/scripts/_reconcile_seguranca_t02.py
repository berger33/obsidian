#!/usr/bin/env python3
"""Reconcile batch software-seguranca-2000-0003 tranche 02 (IDs 101-200, advancing batch 3 to 200/2000) across manifest, MOC, review registry and status docs."""
from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KF = ROOT / "knowledge-federation"
SCRIPTS = KF / "scripts"
BATCH_ID = "software-seguranca-2000-0003"
REPORT_T01 = "ai-review-software-seguranca-2000-0003-tranche-01.md"
REPORT_NAME = "ai-review-software-seguranca-2000-0003-tranche-02.md"
RECON_NAME = "batch-reconciliation-software-seguranca-2000-0003-tranche-02.md"
DATE = "2026-10-03"


def load_module(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_groups(mod):
    groups = []
    for path in sorted(mod.DATA_DIR.glob("*.txt")):
        context, rows = mod.parse_group(path)
        groups.append((context, rows))
    return groups


def render_manifest(groups_t01, groups_t02) -> str:
    lines = [
        f"# Lote `{BATCH_ID}` — Engenharia de Segurança de Software, AppSec, DevSecOps e IAM",
        "",
        f"Manifesto auditável do terceiro lote de escala (`{BATCH_ID}`), focado em segurança de aplicações (AppSec), WAF/NSM, criptografia moderna, postura multi-cloud (CSPM/ASPM), segurança da cadeia de suprimentos de software (SBOM/VEX/SCA/SLSA/Scorecard), varredura de segredos, DAST e identidade/autorização (OAuth2/OIDC/ReBAC/ABAC/PBAC).",
        "",
        "## Resumo do estado atual",
        "",
        "- Domínio / subdomínio: `software` / `seguranca` (`knowledge-federation/domains/software-0009/software/seguranca/`)",
        "- Meta do lote: **2.000 notas substantivas**",
        "- Notas efetivamente redigidas até agora: **200 / 2.000 (10,00%)**",
        "- Gate automatizado: **200/200 aprovadas** (conteúdo mínimo, seções, fontes específicas e wikilinks; reexecutado após a tranche 2)",
        "- Revisão factual humana: **0/200**",
        "- Revisão factual por IA: **200/200**",
        "- Contabilizadas como válidas: **200/200**",
        "- Revisor das 200 notas aprovadas por IA: `Arena.ai Agent Mode`, com relatórios específicos; não são aprovações humanas",
        "- Status do lote maior: `in_progress`; tranches 1–2 (200 notas, IDs 1–200) foram conferidas factualmente por IA e aprovadas sob o protocolo atualizado",
        "- MOC do lote: [`MOC-Seguranca-Software-0009.md`](../../00-home-vault/MOCs/MOC-Seguranca-Software-0009.md)",
        "- Relatório de qualidade do lote: [`note-quality-software-seguranca-2000-0003.md`](../reports/note-quality-software-seguranca-2000-0003.md)",
        f"- Reconciliação estrutural mais recente do manifesto/fila: [`{RECON_NAME}`](../reports/{RECON_NAME})",
        f"- Relatórios factuais por IA: [`tranche 1`](../reports/{REPORT_T01}), [`tranche 2`](../reports/{REPORT_NAME})",
        "",
        "Existem 200 notas materiais listadas abaixo; não há IDs reservados, placeholders ou registros virtuais para as 1.800 restantes.",
        "",
        "## Tranche 1 — Gitleaks, TruffleHog, Google OSV-Scanner V2, OWASP Dependency-Track, OWASP ZAP, ProjectDiscovery Nuclei, OpenFGA, AuthZed SpiceDB, Cerbos e OpenSSF Scorecard (100 notas; revisão factual por IA registrada)",
        "",
    ]
    for context, rows in groups_t01:
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
            "## Tranche 2 — OWASP Coraza WAF, OWASP Core Rule Set (CRS v4), Ory Hydra, Ory Kratos, Authelia, FiloSottile `age`, OWASP DefectDojo, Prowler, osquery e OISF Suricata (100 notas; revisão factual por IA registrada)",
            "",
        ]
    )
    for context, rows in groups_t02:
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
            "As 200 notas 1–200 das tranches 1–2 têm revisão factual por IA registrada nos relatórios vinculados. O lote continua incompleto: são 200/2.000 notas válidas, restando 1.800 notas materiais.",
            "",
        ]
    )
    return "\n".join(lines)


def render_moc(groups_t01, groups_t02) -> str:
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
        f"Índice das 200 notas substantivas redigidas até agora no lote `{BATCH_ID}`, cuja meta é 2.000. As 200 passaram pelo gate automatizado e receberam revisão factual por IA registrada separadamente (nenhuma delas é aprovação humana).",
        "",
        "## Tranche 1 — Gitleaks, TruffleHog, Google OSV-Scanner V2, OWASP Dependency-Track, OWASP ZAP, ProjectDiscovery Nuclei, OpenFGA, AuthZed SpiceDB, Cerbos e OpenSSF Scorecard",
        "",
    ]
    for context, rows in groups_t01:
        lines.append(f"### {context['group_title']}")
        lines.append("")
        for index, row in enumerate(rows):
            number = int(context["first"]) + index
            lines.append(f"{number}. [[{row['slug']}]] — {row['summary']}")
        lines.append("")

    lines.extend(
        [
            "## Tranche 2 — OWASP Coraza WAF, OWASP Core Rule Set (CRS v4), Ory Hydra, Ory Kratos, Authelia, FiloSottile `age`, OWASP DefectDojo, Prowler, osquery e OISF Suricata",
            "",
        ]
    )
    for context, rows in groups_t02:
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
            f"O gate automatizado foi aprovado por 200/200 notas e as 200 contam como válidas pelo protocolo atualizado, com revisão factual por IA registrada separadamente. O lote de 2.000 continua `in_progress` (200 notas substantivas; 1.800 ainda não produzidas). Consulte o [manifesto](../../exports/batches/{BATCH_ID}.md), a [auditoria de qualidade](../../exports/reports/note-quality-{BATCH_ID}.md) e a [reconciliação mais recente do manifesto/fila](../../exports/reports/{RECON_NAME}). Os relatórios factuais por IA são [tranche 1](../../exports/reports/{REPORT_T01}) e [tranche 2](../../exports/reports/{REPORT_NAME}).",
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


def review_rows(groups_t02) -> str:
    lines = []
    for context, rows in groups_t02:
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
    bs01 = load_module("bs01", "_build_seguranca_t01.py")
    bs02 = load_module("bs02", "_build_seguranca_t02.py")
    groups_t01 = load_groups(bs01)
    groups_t02 = load_groups(bs02)
    total_t02 = sum(len(rows) for _, rows in groups_t02)
    if total_t02 != 100 or int(groups_t02[0][0]["first"]) != 101 or int(groups_t02[-1][0]["first"]) != 191:
        raise SystemExit(f"dados inesperados: {total_t02} notas, primeiro grupo em {groups_t02[0][0]['first']}")

    manifest = KF / "exports" / "batches" / f"{BATCH_ID}.md"
    moc = KF / "00-home-vault" / "MOCs" / "MOC-Seguranca-Software-0009.md"
    queue = KF / "exports" / "reports" / "human-review-queue.md"

    manifest.write_text(render_manifest(groups_t01, groups_t02), encoding="utf-8")
    print(f"ok {manifest.relative_to(ROOT)}")
    moc.write_text(render_moc(groups_t01, groups_t02), encoding="utf-8")
    print(f"ok {moc.relative_to(ROOT)}")

    insert_before(queue, "## Regra de contagem", review_rows(groups_t02), marker="| 4141 | `software-seguranca-2000-0003` |")

    apply(
        queue,
        [
            (
                "distingue 4091 revisões factuais realizadas por IA nos lotes `software-testes-2000-0001` (1991), `software-devops-2000-0002` (2000) e `software-seguranca-2000-0003` (100)",
                "distingue 4191 revisões factuais realizadas por IA nos lotes `software-testes-2000-0001` (1991), `software-devops-2000-0002` (2000) e `software-seguranca-2000-0003` (200)",
            ),
            (
                "- Aprovações por IA registradas separadamente: **4091**.",
                "- Aprovações por IA registradas separadamente: **4191**.",
            ),
            (
                "- Notas válidas contabilizadas (gate + revisão humana ou IA): **4140**.",
                "- Notas válidas contabilizadas (gate + revisão humana ou IA): **4240**.",
            ),
            (
                "As 4091 linhas `APROVADA POR IA` (nº 50–4140) correspondem às 1991 notas 10–2000 das tranches 2–26 do lote `software-testes-2000-0001`, às 2000 notas 1–2000 das tranches 1–20 do lote `software-devops-2000-0002` e às 100 notas 1–100 da tranche 1 do lote `software-seguranca-2000-0003`",
                "As 4191 linhas `APROVADA POR IA` (nº 50–4240) correspondem às 1991 notas 10–2000 das tranches 2–26 do lote `software-testes-2000-0001`, às 2000 notas 1–2000 das tranches 1–20 do lote `software-devops-2000-0002` e às 200 notas 1–200 das tranches 1–2 do lote `software-seguranca-2000-0003`",
            ),
        ],
    )

    apply(
        ROOT / "README.md",
        [
            (
                "| Notas válidas contabilizadas | 4140 / 1.000.000 (0,4140%) | 49 com aprovação humana histórica + 4091 com revisão factual por IA |",
                "| Notas válidas contabilizadas | 4240 / 1.000.000 (0,4240%) | 49 com aprovação humana histórica + 4191 com revisão factual por IA |",
            ),
            (
                "| Notas com revisão factual por IA registrada | 4091 | Revisões dos lotes de escala (1991 no lote 1 + 2000 no lote 2 + 100 no lote 3), com relatórios por tranche; não são humanas |",
                "| Notas com revisão factual por IA registrada | 4191 | Revisões dos lotes de escala (1991 no lote 1 + 2000 no lote 2 + 200 no lote 3), com relatórios por tranche; não são humanas |",
            ),
            (
                "| Terceiro lote `software-seguranca-2000-0003` | 100 / 2.000 (5,00%) | 100 aprovadas por IA na tranche 1; faltam 1.900 notas substantivas |",
                "| Terceiro lote `software-seguranca-2000-0003` | 200 / 2.000 (10,00%) | 200 aprovadas por IA nas tranches 1–2; faltam 1.800 notas substantivas |",
            ),
            (
                "| Arquivos Markdown ativos em `knowledge-federation/domains/` | 4240 | 100 notas legadas com pendências + 4140 notas autorais substantivas |",
                "| Arquivos Markdown ativos em `knowledge-federation/domains/` | 4340 | 100 notas legadas com pendências + 4240 notas autorais substantivas |",
            ),
            (
                "e o terceiro lote em andamento é [`software-seguranca-2000-0003`](knowledge-federation/exports/batches/software-seguranca-2000-0003.md): 100 notas materiais já passaram pelo gate e revisão factual por IA na [tranche 1](knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-01.md) ([reconciliação](knowledge-federation/exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-01.md), [auditoria do lote](knowledge-federation/exports/reports/note-quality-software-seguranca-2000-0003.md) e [MOC de Segurança](knowledge-federation/00-home-vault/MOCs/MOC-Seguranca-Software-0009.md)), com meta de 2.000.",
                "e o terceiro lote em andamento é [`software-seguranca-2000-0003`](knowledge-federation/exports/batches/software-seguranca-2000-0003.md): 200 notas materiais já passaram pelo gate e revisão factual por IA até a [tranche 2](knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-02.md) ([reconciliação](knowledge-federation/exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-02.md), [auditoria do lote](knowledge-federation/exports/reports/note-quality-software-seguranca-2000-0003.md) e [MOC de Segurança](knowledge-federation/00-home-vault/MOCs/MOC-Seguranca-Software-0009.md)), com meta de 2.000.",
            ),
        ],
    )

    apply(
        KF / "README.md",
        [
            (
                "- Arquivos Markdown ativos: **4240** (100 notas legadas com pendências + 4140 notas autorais substantivas).",
                "- Arquivos Markdown ativos: **4340** (100 notas legadas com pendências + 4240 notas autorais substantivas).",
            ),
            (
                "- Notas válidas pelo protocolo atual: **4140** (49 aprovações humanas históricas + 4091 revisões factuais por IA).",
                "- Notas válidas pelo protocolo atual: **4240** (49 aprovações humanas históricas + 4191 revisões factuais por IA).",
            ),
            (
                "- Progresso: **4140 / 1.000.000 (0,4140%)**; faltam 995.860 notas válidas.",
                "- Progresso: **4240 / 1.000.000 (0,4240%)**; faltam 995.760 notas válidas.",
            ),
            (
                "- Terceiro lote em andamento `software-seguranca-2000-0003`: **100 / 2.000** notas válidas (5,00%); 100 por IA ([tranche 1](exports/reports/ai-review-software-seguranca-2000-0003-tranche-01.md) e [reconciliação](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-01.md)); faltam 1.900 notas materiais.",
                "- Terceiro lote em andamento `software-seguranca-2000-0003`: **200 / 2.000** notas válidas (10,00%); 200 por IA ([tranche 2](exports/reports/ai-review-software-seguranca-2000-0003-tranche-02.md) e [reconciliação](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-02.md)); faltam 1.800 notas materiais.",
            ),
        ],
    )

    apply(
        KF / "README-1M.md",
        [
            (
                "tem 4140 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 4091 revisões factuais por IA registradas separadamente). O diretório ativo tem 4240 arquivos Markdown, incluindo 100 notas legadas com pendências, ainda excluídas da contagem. O terceiro lote [`software-seguranca-2000-0003`](exports/batches/software-seguranca-2000-0003.md) está em andamento com 100/2.000 notas válidas ([relatório factual por IA da tranche 1](exports/reports/ai-review-software-seguranca-2000-0003-tranche-01.md) e [reconciliação da tranche 1](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-01.md)),",
                "tem 4240 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 4191 revisões factuais por IA registradas separadamente). O diretório ativo tem 4340 arquivos Markdown, incluindo 100 notas legadas com pendências, ainda excluídas da contagem. O terceiro lote [`software-seguranca-2000-0003`](exports/batches/software-seguranca-2000-0003.md) está em andamento com 200/2.000 notas válidas ([relatório factual por IA da tranche 2](exports/reports/ai-review-software-seguranca-2000-0003-tranche-02.md) e [reconciliação da tranche 2](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-02.md)),",
            ),
        ],
    )

    apply(
        KF / "STATUS-CONSOLIDACAO-1M.md",
        [
            (
                "A auditoria encontrou 4240 arquivos Markdown ativos: 4140 notas substantivas passaram pelo gate e receberam revisão factual registrada (49 humanas históricas + 4091 por IA)",
                "A auditoria encontrou 4340 arquivos Markdown ativos: 4240 notas substantivas passaram pelo gate e receberam revisão factual registrada (49 humanas históricas + 4191 por IA)",
            ),
            (
                "| Progresso válido global | 4140 / 1.000.000 (0,4140%) | 49 revisões humanas históricas + 4091 revisões por IA registradas separadamente |",
                "| Progresso válido global | 4240 / 1.000.000 (0,4240%) | 49 revisões humanas históricas + 4191 revisões por IA registradas separadamente |",
            ),
            (
                "| Revisões factuais por IA registradas | 4091 | Relatórios das tranches 2–26 (`software-testes-2000-0001`), tranches 1–20 (`software-devops-2000-0002`) e tranche 1 (`software-seguranca-2000-0003`); não são humanas |",
                "| Revisões factuais por IA registradas | 4191 | Relatórios das tranches 2–26 (`software-testes-2000-0001`), tranches 1–20 (`software-devops-2000-0002`) e tranches 1–2 (`software-seguranca-2000-0003`); não são humanas |",
            ),
            (
                "| Terceiro lote (`software-seguranca-2000-0003`) | 100 / 2.000 (5,00%) | 100 IA na tranche 1 ([tranche 1](exports/reports/ai-review-software-seguranca-2000-0003-tranche-01.md)); faltam 1.900 notas substantivas |",
                "| Terceiro lote (`software-seguranca-2000-0003`) | 200 / 2.000 (10,00%) | 200 IA nas tranches 1–2 ([tranche 2](exports/reports/ai-review-software-seguranca-2000-0003-tranche-02.md)); faltam 1.800 notas substantivas |",
            ),
            (
                "| Candidatas que passaram pelo gate automatizado | 4140 |",
                "| Candidatas que passaram pelo gate automatizado | 4240 |",
            ),
            (
                "e o terceiro lote [`software-seguranca-2000-0003`](exports/batches/software-seguranca-2000-0003.md) está em 100/2.000 notas válidas após a [tranche 1](exports/reports/ai-review-software-seguranca-2000-0003-tranche-01.md) ([reconciliação](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-01.md)).",
                "e o terceiro lote [`software-seguranca-2000-0003`](exports/batches/software-seguranca-2000-0003.md) está em 200/2.000 notas válidas após a [tranche 2](exports/reports/ai-review-software-seguranca-2000-0003-tranche-02.md) ([reconciliação](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-02.md)).",
            ),
            (
                "3. Continuar o terceiro lote `software-seguranca-2000-0003` (atualmente em 100/2.000; faltam 1.900 notas substantivas) e os 497 lotes subsequentes,",
                "3. Continuar o terceiro lote `software-seguranca-2000-0003` (atualmente em 200/2.000; faltam 1.800 notas substantivas) e os 497 lotes subsequentes,",
            ),
        ],
    )

    apply(
        KF / "PLANO-CONTINUO-1M.md",
        [
            (
                "- Notas válidas globais: **4140** (49 aprovações humanas históricas + 4091 revisões factuais por IA).",
                "- Notas válidas globais: **4240** (49 aprovações humanas históricas + 4191 revisões factuais por IA).",
            ),
            (
                "- Progresso: **4140 / 1.000.000 (0,4140%)**; faltam **995.860** notas válidas.",
                "- Progresso: **4240 / 1.000.000 (0,4240%)**; faltam **995.760** notas válidas.",
            ),
            (
                "- Terceiro lote atual `software-seguranca-2000-0003`: **100 / 2.000 (5,00%)** notas válidas (100 IA na tranche 1); faltam **1.900** notas substantivas.",
                "- Terceiro lote atual `software-seguranca-2000-0003`: **200 / 2.000 (10,00%)** notas válidas (200 IA nas tranches 1–2); faltam **1.800** notas substantivas.",
            ),
            (
                "- Arquivos Markdown ativos: **4240**; 100 com pendências de qualidade, excluídos da contagem.",
                "- Arquivos Markdown ativos: **4340**; 100 com pendências de qualidade, excluídos da contagem.",
            ),
            (
                "| 5 | Rodar gate, testes, auditorias e diff | **Concluído para o estado atual** | Lote 1: 2000/2000 (`complete`). Lote 2: 2000/2000 (`complete`). Lote 3 (`software-seguranca-2000-0003`): 100/100 no gate (100 IA). Global: 4240 arquivos, 4140 válidas, 100 com pendências legadas; veja a [reconciliação da tranche 1 do lote 3](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-01.md). |",
                "| 5 | Rodar gate, testes, auditorias e diff | **Concluído para o estado atual** | Lote 1: 2000/2000 (`complete`). Lote 2: 2000/2000 (`complete`). Lote 3 (`software-seguranca-2000-0003`): 200/200 no gate (200 IA). Global: 4340 arquivos, 4240 válidas, 100 com pendências legadas; veja a [reconciliação da tranche 2 do lote 3](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-02.md). |",
            ),
            (
                "| 8 | Abrir lotes subsequentes de 2.000 notas | **Em andamento (lote 3 em 5%)** | Terceiro lote `software-seguranca-2000-0003` aberto com 100/2.000 notas válidas na tranche 1; restam 1.900 notas neste lote e 497 lotes subsequentes. |",
                "| 8 | Abrir lotes subsequentes de 2.000 notas | **Em andamento (lote 3 em 10%)** | Terceiro lote `software-seguranca-2000-0003` em 200/2.000 notas válidas nas tranches 1–2; restam 1.800 notas neste lote e 497 lotes subsequentes. |",
            ),
            (
                "Progresso atual: 4140 notas válidas, 2/500 lotes completos.",
                "Progresso atual: 4240 notas válidas, 2/500 lotes completos.",
            ),
        ],
    )

    apply(
        KF / "RECOVERY-AND-SCALE-NOTE.md",
        [
            (
                "há 4240 arquivos: 100 legados com pendências e 4140 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 4091 revisões por IA). O primeiro lote `software-testes-2000-0001` atingiu 2000/2.000 notas válidas (9 humanas + 1991 IA, `complete`); o segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) atingiu 2000/2.000 notas válidas (`complete`, [tranche 20](exports/reports/ai-review-software-devops-2000-0002-tranche-20.md)); e o terceiro lote [`software-seguranca-2000-0003`](exports/batches/software-seguranca-2000-0003.md) está em andamento (`in_progress`) com 100/2.000 notas válidas revisadas por IA na [tranche 1](exports/reports/ai-review-software-seguranca-2000-0003-tranche-01.md), com [reconciliação](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-01.md);",
                "há 4340 arquivos: 100 legados com pendências e 4240 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 4191 revisões por IA). O primeiro lote `software-testes-2000-0001` atingiu 2000/2.000 notas válidas (9 humanas + 1991 IA, `complete`); o segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) atingiu 2000/2.000 notas válidas (`complete`, [tranche 20](exports/reports/ai-review-software-devops-2000-0002-tranche-20.md)); e o terceiro lote [`software-seguranca-2000-0003`](exports/batches/software-seguranca-2000-0003.md) está em andamento (`in_progress`) com 200/2.000 notas válidas revisadas por IA até a [tranche 2](exports/reports/ai-review-software-seguranca-2000-0003-tranche-02.md), com [reconciliação](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-02.md);",
            ),
            (
                "4. Continuar o terceiro lote `software-seguranca-2000-0003` (100/2.000; faltam 1.900 notas qualificadas) até 2.000 antes de abrir os 497 lotes seguintes.",
                "4. Continuar o terceiro lote `software-seguranca-2000-0003` (200/2.000; faltam 1.800 notas qualificadas) até 2.000 antes de abrir os 497 lotes seguintes.",
            ),
        ],
    )

    apply(
        KF / "00-home-vault" / "Home.md",
        [
            (
                "- [[MOC-Seguranca-Software-0009]] — 100 notas do terceiro lote de escala `software-seguranca-2000-0003` (meta: 2.000); 100 revisões factuais por IA.",
                "- [[MOC-Seguranca-Software-0009]] — 200 notas do terceiro lote de escala `software-seguranca-2000-0003` (meta: 2.000); 200 revisões factuais por IA.",
            ),
            (
                "[[human-review-queue|Registro de revisões factuais]] — 49 aprovações humanas e 4091 aprovações por IA, identificadas separadamente.",
                "[[human-review-queue|Registro de revisões factuais]] — 49 aprovações humanas e 4191 aprovações por IA, identificadas separadamente.",
            ),
            (
                "[[note-quality-audit|Auditoria de qualidade]] — 4140 notas válidas pelo protocolo atual (49 humanas + 4091 IA) e 100 notas legadas com falhas.",
                "[[note-quality-audit|Auditoria de qualidade]] — 4240 notas válidas pelo protocolo atual (49 humanas + 4191 IA) e 100 notas legadas com falhas.",
            ),
        ],
    )

    apply(
        KF / "00-home-vault" / "Indice-Global.md",
        [
            (
                "- Arquivos Markdown em `domains/`: **4240** (100 sementes legadas + 4140 notas autorais substantivas).",
                "- Arquivos Markdown em `domains/`: **4340** (100 sementes legadas + 4240 notas autorais substantivas).",
            ),
            (
                "- Candidatas aprovadas no gate automatizado: **4140**; revisões humanas registradas: **49**; revisões factuais por IA: **4091**; 100 sementes legadas mantêm pendências.",
                "- Candidatas aprovadas no gate automatizado: **4240**; revisões humanas registradas: **49**; revisões factuais por IA: **4191**; 100 sementes legadas mantêm pendências.",
            ),
            (
                "- Os lotes atuais totalizam 4140 notas válidas pelo protocolo; o terceiro lote [`software-seguranca-2000-0003`](../exports/batches/software-seguranca-2000-0003.md) tem 100/2.000 ([tranche 1](../exports/reports/ai-review-software-seguranca-2000-0003-tranche-01.md), [reconciliação da tranche 1](../exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-01.md) e [[MOC-Seguranca-Software-0009]]),",
                "- Os lotes atuais totalizam 4240 notas válidas pelo protocolo; o terceiro lote [`software-seguranca-2000-0003`](../exports/batches/software-seguranca-2000-0003.md) tem 200/2.000 ([tranche 2](../exports/reports/ai-review-software-seguranca-2000-0003-tranche-02.md), [reconciliação da tranche 2](../exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-02.md) e [[MOC-Seguranca-Software-0009]]),",
            ),
        ],
    )
    print("reconciliação concluída")


if __name__ == "__main__":
    main()
