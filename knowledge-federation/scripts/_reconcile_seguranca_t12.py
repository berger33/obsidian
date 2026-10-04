#!/usr/bin/env python3
"""Reconcile batch software-seguranca-2000-0003 tranche 12 (IDs 1101-1200, advancing batch 3 to 1200/2000 [60%]) across manifest, MOC, review registry and status docs."""
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
REPORT_T05 = "ai-review-software-seguranca-2000-0003-tranche-05.md"
REPORT_T06 = "ai-review-software-seguranca-2000-0003-tranche-06.md"
REPORT_T07 = "ai-review-software-seguranca-2000-0003-tranche-07.md"
REPORT_T08 = "ai-review-software-seguranca-2000-0003-tranche-08.md"
REPORT_T09 = "ai-review-software-seguranca-2000-0003-tranche-09.md"
REPORT_T10 = "ai-review-software-seguranca-2000-0003-tranche-10.md"
REPORT_T11 = "ai-review-software-seguranca-2000-0003-tranche-11.md"
REPORT_NAME = "ai-review-software-seguranca-2000-0003-tranche-12.md"
RECON_NAME = "batch-reconciliation-software-seguranca-2000-0003-tranche-12.md"
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


def render_manifest(
    groups_t01,
    groups_t02,
    groups_t03,
    groups_t04,
    groups_t05,
    groups_t06,
    groups_t07,
    groups_t08,
    groups_t09,
    groups_t10,
    groups_t11,
    groups_t12,
) -> str:
    lines = [
        f"# Lote `{BATCH_ID}` — Engenharia de Segurança de Software, AppSec, DevSecOps e IAM",
        "",
        f"Manifesto auditável do terceiro lote de escala (`{BATCH_ID}`), focado em segurança de aplicações (AppSec & Mobile MobSF/`mobsfscan`/Objection/JADX/Apktool), SAST/DAST/IaC/Proxies (GitHub CodeQL/Checkmarx KICS/Wapiti/Nikto/WPScan/Arjun/Feroxbuster/`jwt_tool`/`mitmproxy`/ZAP/Nuclei/Gobuster/`ffuf`/`sqlmap`/Dalfox), WAF/NSM e Firewalls/VPNs de Kernel (Linux `nftables`/WireGuard/OpenSSH/Coraza/CRS v4/Suricata/Zeek), segurança em runtime & pós-exploração de containers/Kubernetes (CDK/Peirates/eBPF/LSMs AppArmor & SELinux/Bubblewrap/KubeArmor/Tracee), DFIR/Threat Intelligence, Detecção Sigma, Emulação de Adversários, Honeypots & Binary Exploitation (WithSecure Chainsaw/Atomic Red Team/MITRE Caldera/Cowrie/OpenCanary/SigmaHQ/Hayabusa/`angr`/Pwndbg/Ropper/TheHive/Cortex/OpenCTI/Timesketch/Volatility 3/CAPEv2/Wireshark/Ghidra/Radare2/Frida/MISP/Velociraptor/auditd), criptografia moderna, FDE/NBDE & PKI/TLS (`tlsx`/GnuPG/VeraCrypt/Cryptsetup LUKS2/Clevis & Tang/`testssl.sh`/Certbot ACME/Hashcat/`age`), EASM & varredura de rede/DNS em escala (Naabu/`dnsx`/`tlsx`/OWASP Amass/Masscan/RustScan/ZMap & ZGrab2/Subfinder/`httpx`/Katana), postura multi-cloud CSPM, grafos de ataque, pentest cloud, containers e integridade de host (AIDE/CNCF Cartography/Scout Suite/Pacu/Steampipe & Powerpipe/CloudQuery/Clair v4/Fail2ban/Sudo/Lynis/USBGuard/Prowler/osquery), segurança da cadeia de suprimentos de software e prevenção de vazamento de segredos (Yelp `detect-secrets`/Talisman/`git-secrets`/Gitleaks/TruffleHog/in-toto/GUAC/Sigstore Rekor & Fulcio/OSV-Scanner/Dependency-Track/Scorecard) e auditoria/identidade Active Directory, AD CS & Zero-Trust (Certipy/Bettercap/Responder/Impacket/NetExec/BloodHound CE/Paralus/OpenZiti/Hydra/Kratos/Authelia/Dex/Pomerium/OpenFGA/SpiceDB/Cerbos).",
        "",
        "## Resumo do estado atual",
        "",
        "- Domínio / subdomínio: `software` / `seguranca` (`knowledge-federation/domains/software-0009/software/seguranca/`)",
        "- Meta do lote: **2.000 notas substantivas**",
        "- Notas efetivamente redigidas até agora: **1200 / 2.000 (60,00%)**",
        "- Gate automatizado: **1200/1200 aprovadas** (conteúdo mínimo, seções, fontes específicas e wikilinks; reexecutado após a tranche 12)",
        "- Revisão factual humana: **0/1200**",
        "- Revisão factual por IA: **1200/1200**",
        "- Contabilizadas como válidas: **1200/1200**",
        "- Revisor das 1200 notas aprovadas por IA: `Arena.ai Agent Mode`, com relatórios específicos; não são aprovações humanas",
        "- Status do lote maior: `in_progress`; tranches 1–12 (1200 notas, IDs 1–1200) foram conferidas factualmente por IA e aprovadas sob o protocolo atualizado",
        "- MOC do lote: [`MOC-Seguranca-Software-0009.md`](../../00-home-vault/MOCs/MOC-Seguranca-Software-0009.md)",
        "- Relatório de qualidade do lote: [`note-quality-software-seguranca-2000-0003.md`](../reports/note-quality-software-seguranca-2000-0003.md)",
        f"- Reconciliação estrutural mais recente do manifesto/fila: [`{RECON_NAME}`](../reports/{RECON_NAME})",
        f"- Relatórios factuais por IA: [`tranche 1`](../reports/{REPORT_T01}), [`tranche 2`](../reports/{REPORT_T02}), [`tranche 3`](../reports/{REPORT_T03}), [`tranche 4`](../reports/{REPORT_T04}), [`tranche 5`](../reports/{REPORT_T05}), [`tranche 6`](../reports/{REPORT_T06}), [`tranche 7`](../reports/{REPORT_T07}), [`tranche 8`](../reports/{REPORT_T08}), [`tranche 9`](../reports/{REPORT_T09}), [`tranche 10`](../reports/{REPORT_T10}), [`tranche 11`](../reports/{REPORT_T11}), [`tranche 12`](../reports/{REPORT_NAME})",
        "",
        "Existem 1200 notas materiais listadas abaixo; não há IDs reservados, placeholders ou registros virtuais para as 800 restantes.",
        "",
    ]

    tranches = [
        (
            "## Tranche 1 — Gitleaks, TruffleHog, Google OSV-Scanner V2, OWASP Dependency-Track, OWASP ZAP, ProjectDiscovery Nuclei, OpenFGA, AuthZed SpiceDB, Cerbos e OpenSSF Scorecard (100 notas; revisão factual por IA registrada)",
            groups_t01,
        ),
        (
            "## Tranche 2 — OWASP Coraza WAF, OWASP Core Rule Set (CRS v4), Ory Hydra, Ory Kratos, Authelia, FiloSottile `age`, OWASP DefectDojo, Prowler, osquery e OISF Suricata (100 notas; revisão factual por IA registrada)",
            groups_t02,
        ),
        (
            "## Tranche 3 — Zeek Network Security Monitor, CNCF KubeArmor, Aqua Security Tracee, CNCF Dex, Pomerium, CNCF in-toto, PyCQA Bandit, Securego `gosec`, VirusTotal YARA / YARA-X e Rapid7 Velociraptor (100 notas; revisão factual por IA registrada)",
            groups_t03,
        ),
        (
            "## Tranche 4 — OpenZiti, Cisco ClamAV, Brakeman, `ffuf`, ProjectDiscovery Subfinder, ProjectDiscovery `httpx`, ProjectDiscovery Katana, OpenSSF GUAC, Sigstore Rekor e Sigstore Fulcio (100 notas; revisão factual por IA registrada)",
            groups_t04,
        ),
        (
            "## Tranche 5 — `sqlmap`, Dalfox, MISP / PyMISP, BloodHound CE, CNCF Paralus, CISOfy Lynis, Linux Audit (`auditd`), USBGuard, AppArmor LSM e SELinux (100 notas; revisão factual por IA registrada)",
            groups_t05,
        ),
        (
            "## Tranche 6 — `mitmproxy`, Ghidra, Radare2 / Rizin, Frida, Hashcat, `testssl.sh`, Certbot / ACME, Gobuster, Impacket e NetExec (`nxc`) (100 notas; revisão factual por IA registrada)",
            groups_t06,
        ),
        (
            "## Tranche 7 — Wireshark / `tshark`, Volatility 3, CAPEv2 Malware Sandbox, TheHive / Cortex, OpenCTI, Google Timesketch, Masscan, RustScan, ZMap / ZGrab2 e OWASP Amass (100 notas; revisão factual por IA registrada)",
            groups_t07,
        ),
        (
            "## Tranche 8 — Cryptsetup / LUKS2, Clevis & Tang (NBDE), VeraCrypt, GnuPG (GPG), Sudo / `sudoers`, Fail2ban, Bubblewrap (`bwrap`), Responder, Bettercap e Clair v4 (100 notas; revisão factual por IA registrada)",
            groups_t08,
        ),
        (
            "## Tranche 9 — Checkmarx KICS, Wapiti, Nikto, WPScan, Arjun, Feroxbuster, `jwt_tool`, JADX, Apktool e Pwndbg (100 notas; revisão factual por IA registrada)",
            groups_t09,
        ),
        (
            "## Tranche 10 — Ropper, ProjectDiscovery Naabu, ProjectDiscovery `dnsx`, ProjectDiscovery `tlsx`, CloudQuery, Steampipe & Powerpipe, Container Penetration Toolkit (`CDK`), Peirates, Talisman e AWS `git-secrets` (100 notas; revisão factual por IA registrada)",
            groups_t10,
        ),
        (
            "## Tranche 11 — CNCF Cartography, NCC Group Scout Suite, Rhino Security Labs Pacu, MobSF / `mobsfscan`, SensePost `objection`, `angr`, Yelp `detect-secrets`, GitHub CodeQL, Sigma (`SigmaHQ`) e Yamato Security Hayabusa (100 notas; revisão factual por IA registrada)",
            groups_t11,
        ),
        (
            "## Tranche 12 — WithSecure Chainsaw, Red Canary Atomic Red Team (`Invoke-AtomicRedTeam`), MITRE Caldera, Certipy (`certipy-ad`), AIDE (Advanced Intrusion Detection Environment), Cowrie Honeypot, Thinkst OpenCanary, WireGuard VPN, Linux `nftables` e OpenSSH (`openssh-portable` 10.x) (100 notas; revisão factual por IA registrada)",
            groups_t12,
        ),
    ]

    for heading, groups in tranches:
        lines.append(heading)
        lines.append("")
        for context, rows in groups:
            lines.append(f"### {context['group_title']}")
            lines.append("")
            for index, row in enumerate(rows):
                number = int(context["first"]) + index
                lines.append(
                    f"{number}. [{row['title']}](../../domains/software-0009/software/seguranca/{row['slug']}.md)"
                )
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def render_moc(
    groups_t01,
    groups_t02,
    groups_t03,
    groups_t04,
    groups_t05,
    groups_t06,
    groups_t07,
    groups_t08,
    groups_t09,
    groups_t10,
    groups_t11,
    groups_t12,
) -> str:
    lines = [
        "---",
        "id: moc-seguranca-software-0009",
        'titulo: "MOC — Engenharia de Segurança de Software, AppSec, DevSecOps e IAM"',
        "dominio: software",
        "subdominio: seguranca",
        f"lote: {BATCH_ID}",
        "tipo_nota: moc",
        f"created: {DATE}",
        f"updated: {DATE}",
        "---",
        "",
        "# MOC — Engenharia de Segurança de Software, AppSec, DevSecOps e IAM (`software-0009`)",
        "",
        f"Mapa de conteúdo das **1200 notas substantivas (Tranches 1–12, IDs `1–1200`)** do lote [`{BATCH_ID}`](../../exports/batches/{BATCH_ID}.md) em `knowledge-federation/domains/software-0009/software/seguranca/`.",
        "",
        "## Estado do lote",
        "",
        "- Progresso atual: **1200 / 2.000 notas válidas (60,00%)** (`status: in_progress`)",
        "- Revisão factual humana: **0 / 1200**",
        "- Revisão factual por IA (`Arena.ai Agent Mode`): **1200 / 1200** ([Tranche 1](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-01.md), [Tranche 2](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-02.md), [Tranche 3](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-03.md), [Tranche 4](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-04.md), [Tranche 5](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-05.md), [Tranche 6](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-06.md), [Tranche 7](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-07.md), [Tranche 8](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-08.md), [Tranche 9](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-09.md), [Tranche 10](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-10.md), [Tranche 11](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-11.md), [Tranche 12](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-12.md))",
        "- Auditoria de qualidade do lote: [`note-quality-software-seguranca-2000-0003.md`](../../exports/reports/note-quality-software-seguranca-2000-0003.md)",
        "",
    ]

    all_tranches = [
        ("Tranche 1 (IDs 1–100)", groups_t01),
        ("Tranche 2 (IDs 101–200)", groups_t02),
        ("Tranche 3 (IDs 201–300)", groups_t03),
        ("Tranche 4 (IDs 301–400)", groups_t04),
        ("Tranche 5 (IDs 401–500)", groups_t05),
        ("Tranche 6 (IDs 501–600)", groups_t06),
        ("Tranche 7 (IDs 601–700)", groups_t07),
        ("Tranche 8 (IDs 701–800)", groups_t08),
        ("Tranche 9 (IDs 801–900)", groups_t09),
        ("Tranche 10 (IDs 901–1000)", groups_t10),
        ("Tranche 11 (IDs 1001–1100)", groups_t11),
        ("Tranche 12 (IDs 1101–1200)", groups_t12),
    ]

    for label, groups in all_tranches:
        lines.append(f"## {label}")
        lines.append("")
        for context, rows in groups:
            lines.append(f"### {context['group_title']}")
            lines.append("")
            for row in rows:
                lines.append(f"- [[{row['slug']}]] — {row['title']}")
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def review_rows(groups_t12) -> str:
    lines = []
    for context, rows in groups_t12:
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
    bs06 = load_module("bs06", "_build_seguranca_t06.py")
    bs07 = load_module("bs07", "_build_seguranca_t07.py")
    bs08 = load_module("bs08", "_build_seguranca_t08.py")
    bs09 = load_module("bs09", "_build_seguranca_t09.py")
    bs10 = load_module("bs10", "_build_seguranca_t10.py")
    bs11 = load_module("bs11", "_build_seguranca_t11.py")
    bs12 = load_module("bs12", "_build_seguranca_t12.py")

    g01 = load_groups(bs01)
    g02 = load_groups(bs02)
    g03 = load_groups(bs03)
    g04 = load_groups(bs04)
    g05 = load_groups(bs05)
    g06 = load_groups(bs06)
    g07 = load_groups(bs07)
    g08 = load_groups(bs08)
    g09 = load_groups(bs09)
    g10 = load_groups(bs10)
    g11 = load_groups(bs11)
    g12 = load_groups(bs12)

    manifest_path = KF / "exports" / "batches" / f"{BATCH_ID}.md"
    manifest_path.write_text(
        render_manifest(g01, g02, g03, g04, g05, g06, g07, g08, g09, g10, g11, g12),
        encoding="utf-8",
    )
    print(f"ok {manifest_path.relative_to(ROOT)}")

    moc_path = KF / "00-home-vault" / "MOCs" / "MOC-Seguranca-Software-0009.md"
    moc_path.write_text(
        render_moc(g01, g02, g03, g04, g05, g06, g07, g08, g09, g10, g11, g12),
        encoding="utf-8",
    )
    print(f"ok {moc_path.relative_to(ROOT)}")

    queue_path = KF / "exports" / "reports" / "human-review-queue.md"
    insert_before(
        queue_path,
        "## Regra de contagem",
        review_rows(g12),
        marker="| 5141 | `software-seguranca-2000-0003` |",
    )

    apply(
        queue_path,
        [
            (
                "distingue 5091 revisões factuais realizadas por IA nos lotes `software-testes-2000-0001` (1991), `software-devops-2000-0002` (2000) e `software-seguranca-2000-0003` (1100)",
                "distingue 5191 revisões factuais realizadas por IA nos lotes `software-testes-2000-0001` (1991), `software-devops-2000-0002` (2000) e `software-seguranca-2000-0003` (1200)",
            ),
            (
                "- Aprovações por IA registradas separadamente: **5091**.",
                "- Aprovações por IA registradas separadamente: **5191**.",
            ),
            (
                "- Notas válidas contabilizadas (gate + revisão humana ou IA): **5140**.",
                "- Notas válidas contabilizadas (gate + revisão humana ou IA): **5240**.",
            ),
            (
                "As 5091 linhas `APROVADA POR IA` (nº 50–5140) correspondem às 1991 notas 10–2000 das tranches 2–26 do lote `software-testes-2000-0001`, às 2000 notas 1–2000 das tranches 1–20 do lote `software-devops-2000-0002` e às 1100 notas 1–1100 das tranches 1–11 do lote `software-seguranca-2000-0003`",
                "As 5191 linhas `APROVADA POR IA` (nº 50–5240) correspondem às 1991 notas 10–2000 das tranches 2–26 do lote `software-testes-2000-0001`, às 2000 notas 1–2000 das tranches 1–20 do lote `software-devops-2000-0002` e às 1200 notas 1–1200 das tranches 1–12 do lote `software-seguranca-2000-0003`",
            ),
        ],
    )

    apply(
        ROOT / "README.md",
        [
            (
                "| Notas válidas contabilizadas | 5140 / 1.000.000 (0,5140%) | 49 com aprovação humana histórica + 5091 com revisão factual por IA |",
                "| Notas válidas contabilizadas | 5240 / 1.000.000 (0,5240%) | 49 com aprovação humana histórica + 5191 com revisão factual por IA |",
            ),
            (
                "| Notas com revisão factual por IA registrada | 5091 | Revisões dos lotes de escala (1991 no lote 1 + 2000 no lote 2 + 1100 no lote 3), com relatórios por tranche; não são humanas |",
                "| Notas com revisão factual por IA registrada | 5191 | Revisões dos lotes de escala (1991 no lote 1 + 2000 no lote 2 + 1200 no lote 3), com relatórios por tranche; não são humanas |",
            ),
            (
                "| Terceiro lote `software-seguranca-2000-0003` | 1100 / 2.000 (55,00%) | 1100 aprovadas por IA nas tranches 1–11; faltam 900 notas substantivas |",
                "| Terceiro lote `software-seguranca-2000-0003` | 1200 / 2.000 (60,00%) | 1200 aprovadas por IA nas tranches 1–12; faltam 800 notas substantivas |",
            ),
            (
                "| Arquivos Markdown ativos em `knowledge-federation/domains/` | 5240 | 100 notas legadas com pendências + 5140 notas autorais substantivas |",
                "| Arquivos Markdown ativos em `knowledge-federation/domains/` | 5340 | 100 notas legadas com pendências + 5240 notas autorais substantivas |",
            ),
            (
                "e o terceiro lote em andamento é [`software-seguranca-2000-0003`](knowledge-federation/exports/batches/software-seguranca-2000-0003.md): 1100 notas materiais já passaram pelo gate e revisão factual por IA até a [tranche 11](knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-11.md) ([reconciliação](knowledge-federation/exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-11.md), [auditoria do lote](knowledge-federation/exports/reports/note-quality-software-seguranca-2000-0003.md) e [MOC de Segurança](knowledge-federation/00-home-vault/MOCs/MOC-Seguranca-Software-0009.md)), com meta de 2.000.",
                "e o terceiro lote em andamento é [`software-seguranca-2000-0003`](knowledge-federation/exports/batches/software-seguranca-2000-0003.md): 1200 notas materiais já passaram pelo gate e revisão factual por IA até a [tranche 12](knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-12.md) ([reconciliação](knowledge-federation/exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-12.md), [auditoria do lote](knowledge-federation/exports/reports/note-quality-software-seguranca-2000-0003.md) e [MOC de Segurança](knowledge-federation/00-home-vault/MOCs/MOC-Seguranca-Software-0009.md)), com meta de 2.000.",
            ),
        ],
    )

    apply(
        KF / "README.md",
        [
            (
                "- Arquivos Markdown ativos: **5240** (100 notas legadas com pendências + 5140 notas autorais substantivas).",
                "- Arquivos Markdown ativos: **5340** (100 notas legadas com pendências + 5240 notas autorais substantivas).",
            ),
            (
                "- Notas válidas pelo protocolo atual: **5140** (49 aprovações humanas históricas + 5091 revisões factuais por IA).",
                "- Notas válidas pelo protocolo atual: **5240** (49 aprovações humanas históricas + 5191 revisões factuais por IA).",
            ),
            (
                "- Progresso: **5140 / 1.000.000 (0,5140%)**; faltam 994.860 notas válidas.",
                "- Progresso: **5240 / 1.000.000 (0,5240%)**; faltam 994.760 notas válidas.",
            ),
            (
                "- Terceiro lote em andamento `software-seguranca-2000-0003`: **1100 / 2.000** notas válidas (55,00%); 1100 por IA ([tranche 11](exports/reports/ai-review-software-seguranca-2000-0003-tranche-11.md) e [reconciliação](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-11.md)); faltam 900 notas materiais.",
                "- Terceiro lote em andamento `software-seguranca-2000-0003`: **1200 / 2.000** notas válidas (60,00%); 1200 por IA ([tranche 12](exports/reports/ai-review-software-seguranca-2000-0003-tranche-12.md) e [reconciliação](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-12.md)); faltam 800 notas materiais.",
            ),
        ],
    )

    apply(
        KF / "README-1M.md",
        [
            (
                "tem 5140 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 5091 revisões factuais por IA registradas separadamente). O diretório ativo tem 5240 arquivos Markdown, incluindo 100 notas legadas com pendências, ainda excluídas da contagem. O terceiro lote [`software-seguranca-2000-0003`](exports/batches/software-seguranca-2000-0003.md) está em andamento com 1100/2.000 notas válidas ([relatório factual por IA da tranche 11](exports/reports/ai-review-software-seguranca-2000-0003-tranche-11.md) e [reconciliação da tranche 11](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-11.md)),",
                "tem 5240 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 5191 revisões factuais por IA registradas separadamente). O diretório ativo tem 5340 arquivos Markdown, incluindo 100 notas legadas com pendências, ainda excluídas da contagem. O terceiro lote [`software-seguranca-2000-0003`](exports/batches/software-seguranca-2000-0003.md) está em andamento com 1200/2.000 notas válidas ([relatório factual por IA da tranche 12](exports/reports/ai-review-software-seguranca-2000-0003-tranche-12.md) e [reconciliação da tranche 12](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-12.md)),",
            ),
        ],
    )

    apply(
        KF / "STATUS-CONSOLIDACAO-1M.md",
        [
            (
                "A auditoria encontrou 5240 arquivos Markdown ativos: 5140 notas substantivas passaram pelo gate e receberam revisão factual registrada (49 humanas históricas + 5091 por IA)",
                "A auditoria encontrou 5340 arquivos Markdown ativos: 5240 notas substantivas passaram pelo gate e receberam revisão factual registrada (49 humanas históricas + 5191 por IA)",
            ),
            (
                "| Progresso válido global | 5140 / 1.000.000 (0,5140%) | 49 revisões humanas históricas + 5091 revisões por IA registradas separadamente |",
                "| Progresso válido global | 5240 / 1.000.000 (0,5240%) | 49 revisões humanas históricas + 5191 revisões por IA registradas separadamente |",
            ),
            (
                "| Revisões factuais por IA registradas | 5091 | Relatórios das tranches 2–26 (`software-testes-2000-0001`), tranches 1–20 (`software-devops-2000-0002`) e tranches 1–11 (`software-seguranca-2000-0003`); não são humanas |",
                "| Revisões factuais por IA registradas | 5191 | Relatórios das tranches 2–26 (`software-testes-2000-0001`), tranches 1–20 (`software-devops-2000-0002`) e tranches 1–12 (`software-seguranca-2000-0003`); não são humanas |",
            ),
            (
                "| Terceiro lote (`software-seguranca-2000-0003`) | 1100 / 2.000 (55,00%) | 1100 IA nas tranches 1–11 ([tranche 11](exports/reports/ai-review-software-seguranca-2000-0003-tranche-11.md)); faltam 900 notas substantivas |",
                "| Terceiro lote (`software-seguranca-2000-0003`) | 1200 / 2.000 (60,00%) | 1200 IA nas tranches 1–12 ([tranche 12](exports/reports/ai-review-software-seguranca-2000-0003-tranche-12.md)); faltam 800 notas substantivas |",
            ),
            (
                "| Candidatas que passaram pelo gate automatizado | 5140 |",
                "| Candidatas que passaram pelo gate automatizado | 5240 |",
            ),
            (
                "e o terceiro lote [`software-seguranca-2000-0003`](exports/batches/software-seguranca-2000-0003.md) está em 1100/2.000 notas válidas após a [tranche 11](exports/reports/ai-review-software-seguranca-2000-0003-tranche-11.md) ([reconciliação](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-11.md)).",
                "e o terceiro lote [`software-seguranca-2000-0003`](exports/batches/software-seguranca-2000-0003.md) está em 1200/2.000 notas válidas após a [tranche 12](exports/reports/ai-review-software-seguranca-2000-0003-tranche-12.md) ([reconciliação](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-12.md)).",
            ),
            (
                "3. Continuar o terceiro lote `software-seguranca-2000-0003` (atualmente em 1100/2.000; faltam 900 notas substantivas) e os 497 lotes subsequentes,",
                "3. Continuar o terceiro lote `software-seguranca-2000-0003` (atualmente em 1200/2.000; faltam 800 notas substantivas) e os 497 lotes subsequentes,",
            ),
        ],
    )

    apply(
        KF / "PLANO-CONTINUO-1M.md",
        [
            (
                "- Notas válidas globais: **5140** (49 aprovações humanas históricas + 5091 revisões factuais por IA).",
                "- Notas válidas globais: **5240** (49 aprovações humanas históricas + 5191 revisões factuais por IA).",
            ),
            (
                "- Progresso: **5140 / 1.000.000 (0,5140%)**; faltam **994.860** notas válidas.",
                "- Progresso: **5240 / 1.000.000 (0,5240%)**; faltam **994.760** notas válidas.",
            ),
            (
                "- Terceiro lote atual `software-seguranca-2000-0003`: **1100 / 2.000 (55,00%)** notas válidas (1100 IA nas tranches 1–11); faltam **900** notas substantivas.",
                "- Terceiro lote atual `software-seguranca-2000-0003`: **1200 / 2.000 (60,00%)** notas válidas (1200 IA nas tranches 1–12); faltam **800** notas substantivas.",
            ),
            (
                "- Arquivos Markdown ativos: **5240**; 100 com pendências de qualidade, excluídos da contagem.",
                "- Arquivos Markdown ativos: **5340**; 100 com pendências de qualidade, excluídos da contagem.",
            ),
            (
                "| 5 | Rodar gate, testes, auditorias e diff | **Concluído para o estado atual** | Lote 1: 2000/2000 (`complete`). Lote 2: 2000/2000 (`complete`). Lote 3 (`software-seguranca-2000-0003`): 1100/1100 no gate (1100 IA). Global: 5240 arquivos, 5140 válidas, 100 com pendências legadas; veja a [reconciliação da tranche 11 do lote 3](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-11.md). |",
                "| 5 | Rodar gate, testes, auditorias e diff | **Concluído para o estado atual** | Lote 1: 2000/2000 (`complete`). Lote 2: 2000/2000 (`complete`). Lote 3 (`software-seguranca-2000-0003`): 1200/1200 no gate (1200 IA). Global: 5340 arquivos, 5240 válidas, 100 com pendências legadas; veja a [reconciliação da tranche 12 do lote 3](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-12.md). |",
            ),
            (
                "| 8 | Abrir lotes subsequentes de 2.000 notas | **Em andamento (lote 3 em 55%)** | Terceiro lote `software-seguranca-2000-0003` em 1100/2.000 notas válidas nas tranches 1–11; restam 900 notas neste lote e 497 lotes subsequentes. |",
                "| 8 | Abrir lotes subsequentes de 2.000 notas | **Em andamento (lote 3 em 60%)** | Terceiro lote `software-seguranca-2000-0003` em 1200/2.000 notas válidas nas tranches 1–12; restam 800 notas neste lote e 497 lotes subsequentes. |",
            ),
            (
                "Progresso atual: 5140 notas válidas, 2/500 lotes completos.",
                "Progresso atual: 5240 notas válidas, 2/500 lotes completos.",
            ),
        ],
    )

    apply(
        KF / "RECOVERY-AND-SCALE-NOTE.md",
        [
            (
                "há 5240 arquivos: 100 legados com pendências e 5140 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 5091 revisões por IA). O primeiro lote `software-testes-2000-0001` atingiu 2000/2.000 notas válidas (9 humanas + 1991 IA, `complete`); o segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) atingiu 2000/2.000 notas válidas (`complete`, [tranche 20](exports/reports/ai-review-software-devops-2000-0002-tranche-20.md)); e o terceiro lote [`software-seguranca-2000-0003`](exports/batches/software-seguranca-2000-0003.md) está em andamento (`in_progress`) com 1100/2.000 notas válidas revisadas por IA até a [tranche 11](exports/reports/ai-review-software-seguranca-2000-0003-tranche-11.md), com [reconciliação](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-11.md);",
                "há 5340 arquivos: 100 legados com pendências e 5240 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 5191 revisões por IA). O primeiro lote `software-testes-2000-0001` atingiu 2000/2.000 notas válidas (9 humanas + 1991 IA, `complete`); o segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) atingiu 2000/2.000 notas válidas (`complete`, [tranche 20](exports/reports/ai-review-software-devops-2000-0002-tranche-20.md)); e o terceiro lote [`software-seguranca-2000-0003`](exports/batches/software-seguranca-2000-0003.md) está em andamento (`in_progress`) com 1200/2.000 notas válidas revisadas por IA até a [tranche 12](exports/reports/ai-review-software-seguranca-2000-0003-tranche-12.md), com [reconciliação](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-12.md);",
            ),
            (
                "4. Continuar o terceiro lote `software-seguranca-2000-0003` (1100/2.000; faltam 900 notas qualificadas) até 2.000 antes de abrir os 497 lotes seguintes.",
                "4. Continuar o terceiro lote `software-seguranca-2000-0003` (1200/2.000; faltam 800 notas qualificadas) até 2.000 antes de abrir os 497 lotes seguintes.",
            ),
        ],
    )

    apply(
        KF / "00-home-vault" / "Home.md",
        [
            (
                "- [[MOC-Seguranca-Software-0009]] — 1100 notas do terceiro lote de escala `software-seguranca-2000-0003` (meta: 2.000); 1100 revisões factuais por IA.",
                "- [[MOC-Seguranca-Software-0009]] — 1200 notas do terceiro lote de escala `software-seguranca-2000-0003` (meta: 2.000); 1200 revisões factuais por IA.",
            ),
            (
                "[[human-review-queue|Registro de revisões factuais]] — 49 aprovações humanas e 5091 aprovações por IA, identificadas separadamente.",
                "[[human-review-queue|Registro de revisões factuais]] — 49 aprovações humanas e 5191 aprovações por IA, identificadas separadamente.",
            ),
            (
                "[[note-quality-audit|Auditoria de qualidade]] — 5140 notas válidas pelo protocolo atual (49 humanas + 5091 IA) e 100 notas legadas com falhas.",
                "[[note-quality-audit|Auditoria de qualidade]] — 5240 notas válidas pelo protocolo atual (49 humanas + 5191 IA) e 100 notas legadas com falhas.",
            ),
        ],
    )

    apply(
        KF / "00-home-vault" / "Indice-Global.md",
        [
            (
                "- Arquivos Markdown em `domains/`: **5240** (100 sementes legadas + 5140 notas autorais substantivas).",
                "- Arquivos Markdown em `domains/`: **5340** (100 sementes legadas + 5240 notas autorais substantivas).",
            ),
            (
                "- Candidatas aprovadas no gate automatizado: **5140**; revisões humanas registradas: **49**; revisões factuais por IA: **5091**; 100 sementes legadas mantêm pendências.",
                "- Candidatas aprovadas no gate automatizado: **5240**; revisões humanas registradas: **49**; revisões factuais por IA: **5191**; 100 sementes legadas mantêm pendências.",
            ),
            (
                "- Os lotes atuais totalizam 5140 notas válidas pelo protocolo; o terceiro lote [`software-seguranca-2000-0003`](../exports/batches/software-seguranca-2000-0003.md) tem 1100/2.000 ([tranche 11](../exports/reports/ai-review-software-seguranca-2000-0003-tranche-11.md), [reconciliação da tranche 11](../exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-11.md) e [[MOC-Seguranca-Software-0009]]),",
                "- Os lotes atuais totalizam 5240 notas válidas pelo protocolo; o terceiro lote [`software-seguranca-2000-0003`](../exports/batches/software-seguranca-2000-0003.md) tem 1200/2.000 ([tranche 12](../exports/reports/ai-review-software-seguranca-2000-0003-tranche-12.md), [reconciliação da tranche 12](../exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-12.md) e [[MOC-Seguranca-Software-0009]]),",
            ),
        ],
    )
    print("reconciliação concluída")


if __name__ == "__main__":
    main()
