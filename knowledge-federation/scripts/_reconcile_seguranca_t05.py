#!/usr/bin/env python3
"""Reconcile batch software-seguranca-2000-0003 tranche 05 (IDs 401-500, advancing batch 3 to 500/2000) across manifest, MOC, review registry and status docs."""
from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KF = ROOT / "knowledge-federation"
SCRIPTS = KF / "scripts"
BATCH_ID = "software-seguranca-2000-0003"
REPORT_T01 = "ai-review-software-seguranca-2000-0003-tranche-01.md"
REPORT_T02 = "ai-review-software-seguranca-2000-0003-tranche-02.md"
REPORT_T03 = "ai-review-software-seguranca-2000-0003-tranche-03.md"
REPORT_T04 = "ai-review-software-seguranca-2000-0003-tranche-04.md"
REPORT_NAME = "ai-review-software-seguranca-2000-0003-tranche-05.md"
RECON_NAME = "batch-reconciliation-software-seguranca-2000-0003-tranche-05.md"
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


def render_manifest(groups_t01, groups_t02, groups_t03, groups_t04, groups_t05) -> str:
    lines = [
        f"# Lote `{BATCH_ID}` — Engenharia de Segurança de Software, AppSec, DevSecOps e IAM",
        "",
        f"Manifesto auditável do terceiro lote de escala (`{BATCH_ID}`), focado em segurança de aplicações (AppSec), SAST/DAST, WAF/NSM, segurança em runtime (eBPF/LSMs AppArmor & SELinux), DFIR/Threat Intelligence (MISP/Velociraptor/auditd), criptografia moderna, postura multi-cloud e de host (Lynis/USBGuard/CSPM/ASPM), segurança da cadeia de suprimentos de software (in-toto/GUAC/Sigstore Rekor & Fulcio/SBOM/VEX/SCA/SLSA/Scorecard), varredura de segredos e identidade/autorização Zero-Trust (BloodHound CE/Paralus/OpenZiti/OAuth2/OIDC/BeyondCorp/ReBAC/ABAC/PBAC).",
        "",
        "## Resumo do estado atual",
        "",
        "- Domínio / subdomínio: `software` / `seguranca` (`knowledge-federation/domains/software-0009/software/seguranca/`)",
        "- Meta do lote: **2.000 notas substantivas**",
        "- Notas efetivamente redigidas até agora: **500 / 2.000 (25,00%)**",
        "- Gate automatizado: **500/500 aprovadas** (conteúdo mínimo, seções, fontes específicas e wikilinks; reexecutado após a tranche 5)",
        "- Revisão factual humana: **0/500**",
        "- Revisão factual por IA: **500/500**",
        "- Contabilizadas como válidas: **500/500**",
        "- Revisor das 500 notas aprovadas por IA: `Arena.ai Agent Mode`, com relatórios específicos; não são aprovações humanas",
        "- Status do lote maior: `in_progress`; tranches 1–5 (500 notas, IDs 1–500) foram conferidas factualmente por IA e aprovadas sob o protocolo atualizado",
        "- MOC do lote: [`MOC-Seguranca-Software-0009.md`](../../00-home-vault/MOCs/MOC-Seguranca-Software-0009.md)",
        "- Relatório de qualidade do lote: [`note-quality-software-seguranca-2000-0003.md`](../reports/note-quality-software-seguranca-2000-0003.md)",
        f"- Reconciliação estrutural mais recente do manifesto/fila: [`{RECON_NAME}`](../reports/{RECON_NAME})",
        f"- Relatórios factuais por IA: [`tranche 1`](../reports/{REPORT_T01}), [`tranche 2`](../reports/{REPORT_T02}), [`tranche 3`](../reports/{REPORT_T03}), [`tranche 4`](../reports/{REPORT_T04}), [`tranche 5`](../reports/{REPORT_NAME})",
        "",
        "Existem 500 notas materiais listadas abaixo; não há IDs reservados, placeholders ou registros virtuais para as 1.500 restantes.",
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
            "## Tranche 3 — Zeek Network Security Monitor, CNCF KubeArmor, Aqua Security Tracee, CNCF Dex, Pomerium, CNCF in-toto, PyCQA Bandit, Securego `gosec`, VirusTotal YARA / YARA-X e Rapid7 Velociraptor (100 notas; revisão factual por IA registrada)",
            "",
        ]
    )
    for context, rows in groups_t03:
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
            "## Tranche 4 — OpenZiti, Cisco ClamAV, Brakeman, `ffuf`, ProjectDiscovery Subfinder, ProjectDiscovery `httpx`, ProjectDiscovery Katana, OpenSSF GUAC, Sigstore Rekor e Sigstore Fulcio (100 notas; revisão factual por IA registrada)",
            "",
        ]
    )
    for context, rows in groups_t04:
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
            "## Tranche 5 — `sqlmap`, Dalfox, MISP / PyMISP, BloodHound CE, CNCF Paralus, CISOfy Lynis, Linux Audit (`auditd`), USBGuard, AppArmor LSM e SELinux (100 notas; revisão factual por IA registrada)",
            "",
        ]
    )
    for context, rows in groups_t05:
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
            "As 500 notas 1–500 das tranches 1–5 têm revisão factual por IA registrada nos relatórios vinculados. O lote continua incompleto: são 500/2.000 notas válidas, restando 1.500 notas materiais.",
            "",
        ]
    )
    return "\n".join(lines)


def render_moc(groups_t01, groups_t02, groups_t03, groups_t04, groups_t05) -> str:
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
        f"Índice das 500 notas substantivas redigidas até agora no lote `{BATCH_ID}`, cuja meta é 2.000. As 500 passaram pelo gate automatizado e receberam revisão factual por IA registrada separadamente (nenhuma delas é aprovação humana).",
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
            "## Tranche 3 — Zeek Network Security Monitor, CNCF KubeArmor, Aqua Security Tracee, CNCF Dex, Pomerium, CNCF in-toto, PyCQA Bandit, Securego `gosec`, VirusTotal YARA / YARA-X e Rapid7 Velociraptor",
            "",
        ]
    )
    for context, rows in groups_t03:
        lines.append(f"### {context['group_title']}")
        lines.append("")
        for index, row in enumerate(rows):
            number = int(context["first"]) + index
            lines.append(f"{number}. [[{row['slug']}]] — {row['summary']}")
        lines.append("")

    lines.extend(
        [
            "## Tranche 4 — OpenZiti, Cisco ClamAV, Brakeman, `ffuf`, ProjectDiscovery Subfinder, ProjectDiscovery `httpx`, ProjectDiscovery Katana, OpenSSF GUAC, Sigstore Rekor e Sigstore Fulcio",
            "",
        ]
    )
    for context, rows in groups_t04:
        lines.append(f"### {context['group_title']}")
        lines.append("")
        for index, row in enumerate(rows):
            number = int(context["first"]) + index
            lines.append(f"{number}. [[{row['slug']}]] — {row['summary']}")
        lines.append("")

    lines.extend(
        [
            "## Tranche 5 — `sqlmap`, Dalfox, MISP / PyMISP, BloodHound CE, CNCF Paralus, CISOfy Lynis, Linux Audit (`auditd`), USBGuard, AppArmor LSM e SELinux",
            "",
        ]
    )
    for context, rows in groups_t05:
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
            f"O gate automatizado foi aprovado por 500/500 notas e as 500 contam como válidas pelo protocolo atualizado, com revisão factual por IA registrada separadamente. O lote de 2.000 continua `in_progress` (500 notas substantivas; 1.500 ainda não produzidas). Consulte o [manifesto](../../exports/batches/{BATCH_ID}.md), a [auditoria de qualidade](../../exports/reports/note-quality-{BATCH_ID}.md) e a [reconciliação mais recente do manifesto/fila](../../exports/reports/{RECON_NAME}). Os relatórios factuais por IA são [tranche 1](../../exports/reports/{REPORT_T01}), [tranche 2](../../exports/reports/{REPORT_T02}), [tranche 3](../../exports/reports/{REPORT_T03}), [tranche 4](../../exports/reports/{REPORT_T04}) e [tranche 5](../../exports/reports/{REPORT_NAME}).",
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


def review_rows(groups_t05) -> str:
    lines = []
    for context, rows in groups_t05:
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
    bs03 = load_module("bs03", "_build_seguranca_t03.py")
    bs04 = load_module("bs04", "_build_seguranca_t04.py")
    bs05 = load_module("bs05", "_build_seguranca_t05.py")
    groups_t01 = load_groups(bs01)
    groups_t02 = load_groups(bs02)
    groups_t03 = load_groups(bs03)
    groups_t04 = load_groups(bs04)
    groups_t05 = load_groups(bs05)
    total_t05 = sum(len(rows) for _, rows in groups_t05)
    if total_t05 != 100 or int(groups_t05[0][0]["first"]) != 401 or int(groups_t05[-1][0]["first"]) != 491:
        raise SystemExit(f"dados inesperados: {total_t05} notas, primeiro grupo em {groups_t05[0][0]['first']}")

    manifest = KF / "exports" / "batches" / f"{BATCH_ID}.md"
    moc = KF / "00-home-vault" / "MOCs" / "MOC-Seguranca-Software-0009.md"
    queue = KF / "exports" / "reports" / "human-review-queue.md"

    manifest.write_text(render_manifest(groups_t01, groups_t02, groups_t03, groups_t04, groups_t05), encoding="utf-8")
    print(f"ok {manifest.relative_to(ROOT)}")
    moc.write_text(render_moc(groups_t01, groups_t02, groups_t03, groups_t04, groups_t05), encoding="utf-8")
    print(f"ok {moc.relative_to(ROOT)}")

    insert_before(queue, "## Regra de contagem", review_rows(groups_t05), marker="| 4441 | `software-seguranca-2000-0003` |")

    apply(
        queue,
        [
            (
                "distingue 4391 revisões factuais realizadas por IA nos lotes `software-testes-2000-0001` (1991), `software-devops-2000-0002` (2000) e `software-seguranca-2000-0003` (400)",
                "distingue 4491 revisões factuais realizadas por IA nos lotes `software-testes-2000-0001` (1991), `software-devops-2000-0002` (2000) e `software-seguranca-2000-0003` (500)",
            ),
            (
                "- Aprovações por IA registradas separadamente: **4391**.",
                "- Aprovações por IA registradas separadamente: **4491**.",
            ),
            (
                "- Notas válidas contabilizadas (gate + revisão humana ou IA): **4440**.",
                "- Notas válidas contabilizadas (gate + revisão humana ou IA): **4540**.",
            ),
            (
                "As 4391 linhas `APROVADA POR IA` (nº 50–4440) correspondem às 1991 notas 10–2000 das tranches 2–26 do lote `software-testes-2000-0001`, às 2000 notas 1–2000 das tranches 1–20 do lote `software-devops-2000-0002` e às 400 notas 1–400 das tranches 1–4 do lote `software-seguranca-2000-0003`",
                "As 4491 linhas `APROVADA POR IA` (nº 50–4540) correspondem às 1991 notas 10–2000 das tranches 2–26 do lote `software-testes-2000-0001`, às 2000 notas 1–2000 das tranches 1–20 do lote `software-devops-2000-0002` e às 500 notas 1–500 das tranches 1–5 do lote `software-seguranca-2000-0003`",
            ),
        ],
    )

    apply(
        ROOT / "README.md",
        [
            (
                "| Notas válidas contabilizadas | 4440 / 1.000.000 (0,4440%) | 49 com aprovação humana histórica + 4391 com revisão factual por IA |",
                "| Notas válidas contabilizadas | 4540 / 1.000.000 (0,4540%) | 49 com aprovação humana histórica + 4491 com revisão factual por IA |",
            ),
            (
                "| Notas com revisão factual por IA registrada | 4391 | Revisões dos lotes de escala (1991 no lote 1 + 2000 no lote 2 + 400 no lote 3), com relatórios por tranche; não são humanas |",
                "| Notas com revisão factual por IA registrada | 4491 | Revisões dos lotes de escala (1991 no lote 1 + 2000 no lote 2 + 500 no lote 3), com relatórios por tranche; não são humanas |",
            ),
            (
                "| Terceiro lote `software-seguranca-2000-0003` | 400 / 2.000 (20,00%) | 400 aprovadas por IA nas tranches 1–4; faltam 1.600 notas substantivas |",
                "| Terceiro lote `software-seguranca-2000-0003` | 500 / 2.000 (25,00%) | 500 aprovadas por IA nas tranches 1–5; faltam 1.500 notas substantivas |",
            ),
            (
                "| Arquivos Markdown ativos em `knowledge-federation/domains/` | 4540 | 100 notas legadas com pendências + 4440 notas autorais substantivas |",
                "| Arquivos Markdown ativos em `knowledge-federation/domains/` | 4640 | 100 notas legadas com pendências + 4540 notas autorais substantivas |",
            ),
            (
                "e o terceiro lote em andamento é [`software-seguranca-2000-0003`](knowledge-federation/exports/batches/software-seguranca-2000-0003.md): 400 notas materiais já passaram pelo gate e revisão factual por IA até a [tranche 4](knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-04.md) ([reconciliação](knowledge-federation/exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-04.md), [auditoria do lote](knowledge-federation/exports/reports/note-quality-software-seguranca-2000-0003.md) e [MOC de Segurança](knowledge-federation/00-home-vault/MOCs/MOC-Seguranca-Software-0009.md)), com meta de 2.000.",
                "e o terceiro lote em andamento é [`software-seguranca-2000-0003`](knowledge-federation/exports/batches/software-seguranca-2000-0003.md): 500 notas materiais já passaram pelo gate e revisão factual por IA até a [tranche 5](knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-05.md) ([reconciliação](knowledge-federation/exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-05.md), [auditoria do lote](knowledge-federation/exports/reports/note-quality-software-seguranca-2000-0003.md) e [MOC de Segurança](knowledge-federation/00-home-vault/MOCs/MOC-Seguranca-Software-0009.md)), com meta de 2.000.",
            ),
        ],
    )

    apply(
        KF / "README.md",
        [
            (
                "- Arquivos Markdown ativos: **4540** (100 notas legadas com pendências + 4440 notas autorais substantivas).",
                "- Arquivos Markdown ativos: **4640** (100 notas legadas com pendências + 4540 notas autorais substantivas).",
            ),
            (
                "- Notas válidas pelo protocolo atual: **4440** (49 aprovações humanas históricas + 4391 revisões factuais por IA).",
                "- Notas válidas pelo protocolo atual: **4540** (49 aprovações humanas históricas + 4491 revisões factuais por IA).",
            ),
            (
                "- Progresso: **4440 / 1.000.000 (0,4440%)**; faltam 995.560 notas válidas.",
                "- Progresso: **4540 / 1.000.000 (0,4540%)**; faltam 995.460 notas válidas.",
            ),
            (
                "- Terceiro lote em andamento `software-seguranca-2000-0003`: **400 / 2.000** notas válidas (20,00%); 400 por IA ([tranche 4](exports/reports/ai-review-software-seguranca-2000-0003-tranche-04.md) e [reconciliação](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-04.md)); faltam 1.600 notas materiais.",
                "- Terceiro lote em andamento `software-seguranca-2000-0003`: **500 / 2.000** notas válidas (25,00%); 500 por IA ([tranche 5](exports/reports/ai-review-software-seguranca-2000-0003-tranche-05.md) e [reconciliação](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-05.md)); faltam 1.500 notas materiais.",
            ),
        ],
    )

    apply(
        KF / "README-1M.md",
        [
            (
                "tem 4440 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 4391 revisões factuais por IA registradas separadamente). O diretório ativo tem 4540 arquivos Markdown, incluindo 100 notas legadas com pendências, ainda excluídas da contagem. O terceiro lote [`software-seguranca-2000-0003`](exports/batches/software-seguranca-2000-0003.md) está em andamento com 400/2.000 notas válidas ([relatório factual por IA da tranche 4](exports/reports/ai-review-software-seguranca-2000-0003-tranche-04.md) e [reconciliação da tranche 4](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-04.md)),",
                "tem 4540 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 4491 revisões factuais por IA registradas separadamente). O diretório ativo tem 4640 arquivos Markdown, incluindo 100 notas legadas com pendências, ainda excluídas da contagem. O terceiro lote [`software-seguranca-2000-0003`](exports/batches/software-seguranca-2000-0003.md) está em andamento com 500/2.000 notas válidas ([relatório factual por IA da tranche 5](exports/reports/ai-review-software-seguranca-2000-0003-tranche-05.md) e [reconciliação da tranche 5](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-05.md)),",
            ),
        ],
    )

    apply(
        KF / "STATUS-CONSOLIDACAO-1M.md",
        [
            (
                "A auditoria encontrou 4540 arquivos Markdown ativos: 4440 notas substantivas passaram pelo gate e receberam revisão factual registrada (49 humanas históricas + 4391 por IA)",
                "A auditoria encontrou 4640 arquivos Markdown ativos: 4540 notas substantivas passaram pelo gate e receberam revisão factual registrada (49 humanas históricas + 4491 por IA)",
            ),
            (
                "| Progresso válido global | 4440 / 1.000.000 (0,4440%) | 49 revisões humanas históricas + 4391 revisões por IA registradas separadamente |",
                "| Progresso válido global | 4540 / 1.000.000 (0,4540%) | 49 revisões humanas históricas + 4491 revisões por IA registradas separadamente |",
            ),
            (
                "| Revisões factuais por IA registradas | 4391 | Relatórios das tranches 2–26 (`software-testes-2000-0001`), tranches 1–20 (`software-devops-2000-0002`) e tranches 1–4 (`software-seguranca-2000-0003`); não são humanas |",
                "| Revisões factuais por IA registradas | 4491 | Relatórios das tranches 2–26 (`software-testes-2000-0001`), tranches 1–20 (`software-devops-2000-0002`) e tranches 1–5 (`software-seguranca-2000-0003`); não são humanas |",
            ),
            (
                "| Terceiro lote (`software-seguranca-2000-0003`) | 400 / 2.000 (20,00%) | 400 IA nas tranches 1–4 ([tranche 4](exports/reports/ai-review-software-seguranca-2000-0003-tranche-04.md)); faltam 1.600 notas substantivas |",
                "| Terceiro lote (`software-seguranca-2000-0003`) | 500 / 2.000 (25,00%) | 500 IA nas tranches 1–5 ([tranche 5](exports/reports/ai-review-software-seguranca-2000-0003-tranche-05.md)); faltam 1.500 notas substantivas |",
            ),
            (
                "| Candidatas que passaram pelo gate automatizado | 4440 |",
                "| Candidatas que passaram pelo gate automatizado | 4540 |",
            ),
            (
                "e o terceiro lote [`software-seguranca-2000-0003`](exports/batches/software-seguranca-2000-0003.md) está em 400/2.000 notas válidas após a [tranche 4](exports/reports/ai-review-software-seguranca-2000-0003-tranche-04.md) ([reconciliação](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-04.md)).",
                "e o terceiro lote [`software-seguranca-2000-0003`](exports/batches/software-seguranca-2000-0003.md) está em 500/2.000 notas válidas após a [tranche 5](exports/reports/ai-review-software-seguranca-2000-0003-tranche-05.md) ([reconciliação](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-05.md)).",
            ),
            (
                "3. Continuar o terceiro lote `software-seguranca-2000-0003` (atualmente em 400/2.000; faltam 1.600 notas substantivas) e os 497 lotes subsequentes,",
                "3. Continuar o terceiro lote `software-seguranca-2000-0003` (atualmente em 500/2.000; faltam 1.500 notas substantivas) e os 497 lotes subsequentes,",
            ),
        ],
    )

    apply(
        KF / "PLANO-CONTINUO-1M.md",
        [
            (
                "- Notas válidas globais: **4440** (49 aprovações humanas históricas + 4391 revisões factuais por IA).",
                "- Notas válidas globais: **4540** (49 aprovações humanas históricas + 4491 revisões factuais por IA).",
            ),
            (
                "- Progresso: **4440 / 1.000.000 (0,4440%)**; faltam **995.560** notas válidas.",
                "- Progresso: **4540 / 1.000.000 (0,4540%)**; faltam **995.460** notas válidas.",
            ),
            (
                "- Terceiro lote atual `software-seguranca-2000-0003`: **400 / 2.000 (20,00%)** notas válidas (400 IA nas tranches 1–4); faltam **1.600** notas substantivas.",
                "- Terceiro lote atual `software-seguranca-2000-0003`: **500 / 2.000 (25,00%)** notas válidas (500 IA nas tranches 1–5); faltam **1.500** notas substantivas.",
            ),
            (
                "- Arquivos Markdown ativos: **4540**; 100 com pendências de qualidade, excluídos da contagem.",
                "- Arquivos Markdown ativos: **4640**; 100 com pendências de qualidade, excluídos da contagem.",
            ),
            (
                "| 5 | Rodar gate, testes, auditorias e diff | **Concluído para o estado atual** | Lote 1: 2000/2000 (`complete`). Lote 2: 2000/2000 (`complete`). Lote 3 (`software-seguranca-2000-0003`): 400/400 no gate (400 IA). Global: 4540 arquivos, 4440 válidas, 100 com pendências legadas; veja a [reconciliação da tranche 4 do lote 3](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-04.md). |",
                "| 5 | Rodar gate, testes, auditorias e diff | **Concluído para o estado atual** | Lote 1: 2000/2000 (`complete`). Lote 2: 2000/2000 (`complete`). Lote 3 (`software-seguranca-2000-0003`): 500/500 no gate (500 IA). Global: 4640 arquivos, 4540 válidas, 100 com pendências legadas; veja a [reconciliação da tranche 5 do lote 3](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-05.md). |",
            ),
            (
                "| 8 | Abrir lotes subsequentes de 2.000 notas | **Em andamento (lote 3 em 20%)** | Terceiro lote `software-seguranca-2000-0003` em 400/2.000 notas válidas nas tranches 1–4; restam 1.600 notas neste lote e 497 lotes subsequentes. |",
                "| 8 | Abrir lotes subsequentes de 2.000 notas | **Em andamento (lote 3 em 25%)** | Terceiro lote `software-seguranca-2000-0003` em 500/2.000 notas válidas nas tranches 1–5; restam 1.500 notas neste lote e 497 lotes subsequentes. |",
            ),
            (
                "Progresso atual: 4440 notas válidas, 2/500 lotes completos.",
                "Progresso atual: 4540 notas válidas, 2/500 lotes completos.",
            ),
        ],
    )

    apply(
        KF / "RECOVERY-AND-SCALE-NOTE.md",
        [
            (
                "há 4540 arquivos: 100 legados com pendências e 4440 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 4391 revisões por IA). O primeiro lote `software-testes-2000-0001` atingiu 2000/2.000 notas válidas (9 humanas + 1991 IA, `complete`); o segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) atingiu 2000/2.000 notas válidas (`complete`, [tranche 20](exports/reports/ai-review-software-devops-2000-0002-tranche-20.md)); e o terceiro lote [`software-seguranca-2000-0003`](exports/batches/software-seguranca-2000-0003.md) está em andamento (`in_progress`) com 400/2.000 notas válidas revisadas por IA até a [tranche 4](exports/reports/ai-review-software-seguranca-2000-0003-tranche-04.md), com [reconciliação](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-04.md);",
                "há 4640 arquivos: 100 legados com pendências e 4540 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 4491 revisões por IA). O primeiro lote `software-testes-2000-0001` atingiu 2000/2.000 notas válidas (9 humanas + 1991 IA, `complete`); o segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) atingiu 2000/2.000 notas válidas (`complete`, [tranche 20](exports/reports/ai-review-software-devops-2000-0002-tranche-20.md)); e o terceiro lote [`software-seguranca-2000-0003`](exports/batches/software-seguranca-2000-0003.md) está em andamento (`in_progress`) com 500/2.000 notas válidas revisadas por IA até a [tranche 5](exports/reports/ai-review-software-seguranca-2000-0003-tranche-05.md), com [reconciliação](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-05.md);",
            ),
            (
                "4. Continuar o terceiro lote `software-seguranca-2000-0003` (400/2.000; faltam 1.600 notas qualificadas) até 2.000 antes de abrir os 497 lotes seguintes.",
                "4. Continuar o terceiro lote `software-seguranca-2000-0003` (500/2.000; faltam 1.500 notas qualificadas) até 2.000 antes de abrir os 497 lotes seguintes.",
            ),
        ],
    )

    apply(
        KF / "00-home-vault" / "Home.md",
        [
            (
                "- [[MOC-Seguranca-Software-0009]] — 400 notas do terceiro lote de escala `software-seguranca-2000-0003` (meta: 2.000); 400 revisões factuais por IA.",
                "- [[MOC-Seguranca-Software-0009]] — 500 notas do terceiro lote de escala `software-seguranca-2000-0003` (meta: 2.000); 500 revisões factuais por IA.",
            ),
            (
                "[[human-review-queue|Registro de revisões factuais]] — 49 aprovações humanas e 4391 aprovações por IA, identificadas separadamente.",
                "[[human-review-queue|Registro de revisões factuais]] — 49 aprovações humanas e 4491 aprovações por IA, identificadas separadamente.",
            ),
            (
                "[[note-quality-audit|Auditoria de qualidade]] — 4440 notas válidas pelo protocolo atual (49 humanas + 4391 IA) e 100 notas legadas com falhas.",
                "[[note-quality-audit|Auditoria de qualidade]] — 4540 notas válidas pelo protocolo atual (49 humanas + 4491 IA) e 100 notas legadas com falhas.",
            ),
        ],
    )

    apply(
        KF / "00-home-vault" / "Indice-Global.md",
        [
            (
                "- Arquivos Markdown em `domains/`: **4540** (100 sementes legadas + 4440 notas autorais substantivas).",
                "- Arquivos Markdown em `domains/`: **4640** (100 sementes legadas + 4540 notas autorais substantivas).",
            ),
            (
                "- Candidatas aprovadas no gate automatizado: **4440**; revisões humanas registradas: **49**; revisões factuais por IA: **4391**; 100 sementes legadas mantêm pendências.",
                "- Candidatas aprovadas no gate automatizado: **4540**; revisões humanas registradas: **49**; revisões factuais por IA: **4491**; 100 sementes legadas mantêm pendências.",
            ),
            (
                "- Os lotes atuais totalizam 4440 notas válidas pelo protocolo; o terceiro lote [`software-seguranca-2000-0003`](../exports/batches/software-seguranca-2000-0003.md) tem 400/2.000 ([tranche 4](../exports/reports/ai-review-software-seguranca-2000-0003-tranche-04.md), [reconciliação da tranche 4](../exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-04.md) e [[MOC-Seguranca-Software-0009]]),",
                "- Os lotes atuais totalizam 4540 notas válidas pelo protocolo; o terceiro lote [`software-seguranca-2000-0003`](../exports/batches/software-seguranca-2000-0003.md) tem 500/2.000 ([tranche 5](../exports/reports/ai-review-software-seguranca-2000-0003-tranche-05.md), [reconciliação da tranche 5](../exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-05.md) e [[MOC-Seguranca-Software-0009]]),",
            ),
        ],
    )
    print("reconciliação concluída")


if __name__ == "__main__":
    main()
