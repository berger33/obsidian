#!/usr/bin/env python3
"""Reconcile batch software-seguranca-2000-0003 tranche 11 (IDs 1001-1100, advancing batch 3 to 1100/2000 [55%]) across manifest, MOC, review registry and status docs."""
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
REPORT_NAME = "ai-review-software-seguranca-2000-0003-tranche-11.md"
RECON_NAME = "batch-reconciliation-software-seguranca-2000-0003-tranche-11.md"
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
) -> str:
    lines = [
        f"# Lote `{BATCH_ID}` — Engenharia de Segurança de Software, AppSec, DevSecOps e IAM",
        "",
        f"Manifesto auditável do terceiro lote de escala (`{BATCH_ID}`), focado em segurança de aplicações (AppSec & Mobile MobSF/`mobsfscan`/Objection/JADX/Apktool), SAST/DAST/IaC/Proxies (GitHub CodeQL/Checkmarx KICS/Wapiti/Nikto/WPScan/Arjun/Feroxbuster/`jwt_tool`/`mitmproxy`/ZAP/Nuclei/Gobuster/`ffuf`/`sqlmap`/Dalfox), WAF/NSM (Coraza/CRS v4/Suricata/Zeek), segurança em runtime & pós-exploração de containers/Kubernetes (CDK/Peirates/eBPF/LSMs AppArmor & SELinux/Bubblewrap/KubeArmor/Tracee), DFIR/Threat Intelligence, Detecção Sigma, Engenharia Reversa & Binary Exploitation (SigmaHQ/Hayabusa/`angr`/Pwndbg/Ropper/TheHive/Cortex/OpenCTI/Timesketch/Volatility 3/CAPEv2/Wireshark/Ghidra/Radare2/Frida/MISP/Velociraptor/auditd), criptografia moderna, FDE/NBDE & PKI/TLS (`tlsx`/GnuPG/VeraCrypt/Cryptsetup LUKS2/Clevis & Tang/`testssl.sh`/Certbot ACME/Hashcat/`age`), EASM & varredura de rede/DNS em escala (Naabu/`dnsx`/`tlsx`/OWASP Amass/Masscan/RustScan/ZMap & ZGrab2/Subfinder/`httpx`/Katana), postura multi-cloud CSPM, grafos de ataque, pentest cloud, containers e de host (CNCF Cartography/Scout Suite/Pacu/Steampipe & Powerpipe/CloudQuery/Clair v4/Fail2ban/Sudo/Lynis/USBGuard/Prowler/osquery), segurança da cadeia de suprimentos de software e prevenção de vazamento de segredos (Yelp `detect-secrets`/Talisman/`git-secrets`/Gitleaks/TruffleHog/in-toto/GUAC/Sigstore Rekor & Fulcio/OSV-Scanner/Dependency-Track/Scorecard) e auditoria/identidade Active Directory & Zero-Trust (Bettercap/Responder/Impacket/NetExec/BloodHound CE/Paralus/OpenZiti/Hydra/Kratos/Authelia/Dex/Pomerium/OpenFGA/SpiceDB/Cerbos).",
        "",
        "## Resumo do estado atual",
        "",
        "- Domínio / subdomínio: `software` / `seguranca` (`knowledge-federation/domains/software-0009/software/seguranca/`)",
        "- Meta do lote: **2.000 notas substantivas**",
        "- Notas efetivamente redigidas até agora: **1100 / 2.000 (55,00%)**",
        "- Gate automatizado: **1100/1100 aprovadas** (conteúdo mínimo, seções, fontes específicas e wikilinks; reexecutado após a tranche 11)",
        "- Revisão factual humana: **0/1100**",
        "- Revisão factual por IA: **1100/1100**",
        "- Contabilizadas como válidas: **1100/1100**",
        "- Revisor das 1100 notas aprovadas por IA: `Arena.ai Agent Mode`, com relatórios específicos; não são aprovações humanas",
        "- Status do lote maior: `in_progress`; tranches 1–11 (1100 notas, IDs 1–1100) foram conferidas factualmente por IA e aprovadas sob o protocolo atualizado",
        "- MOC do lote: [`MOC-Seguranca-Software-0009.md`](../../00-home-vault/MOCs/MOC-Seguranca-Software-0009.md)",
        "- Relatório de qualidade do lote: [`note-quality-software-seguranca-2000-0003.md`](../reports/note-quality-software-seguranca-2000-0003.md)",
        f"- Reconciliação estrutural mais recente do manifesto/fila: [`{RECON_NAME}`](../reports/{RECON_NAME})",
        f"- Relatórios factuais por IA: [`tranche 1`](../reports/{REPORT_T01}), [`tranche 2`](../reports/{REPORT_T02}), [`tranche 3`](../reports/{REPORT_T03}), [`tranche 4`](../reports/{REPORT_T04}), [`tranche 5`](../reports/{REPORT_T05}), [`tranche 6`](../reports/{REPORT_T06}), [`tranche 7`](../reports/{REPORT_T07}), [`tranche 8`](../reports/{REPORT_T08}), [`tranche 9`](../reports/{REPORT_T09}), [`tranche 10`](../reports/{REPORT_T10}), [`tranche 11`](../reports/{REPORT_NAME})",
        "",
        "Existem 1100 notas materiais listadas abaixo; não há IDs reservados, placeholders ou registros virtuais para as 900 restantes.",
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
            "## Tranche 6 — TheHive & Cortex, Filigran OpenCTI, Google Timesketch & Plaso, Volatility 3 & `dwarf2json`, CAPEv2 Sandbox, Wireshark & `tshark`, Bettercap, Responder, Fortra Impacket e NetExec (`nxc`) (100 notas; revisão factual por IA registrada)",
            "",
        ]
    )
    for context, rows in groups_t06:
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
            "## Tranche 7 — `testssl.sh`, EFF Certbot (ACME), Hashcat, NSA Ghidra, Radare2 (`r2`), Frida, Fail2ban, Sudo (`sudo` & `sudo_logsrvd`), Bubblewrap (`bwrap`) e Project Quay Clair v4 (`ClairCore`) (100 notas; revisão factual por IA registrada)",
            "",
        ]
    )
    for context, rows in groups_t07:
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
            "## Tranche 8 — GnuPG (`gpg`), VeraCrypt, Linux Cryptsetup & LUKS2, Clevis & Tang (NBDE), `mitmproxy`, Gobuster, OWASP Amass (OAM), Masscan, RustScan e ZMap & ZGrab 2.0 (100 notas; revisão factual por IA registrada)",
            "",
        ]
    )
    for context, rows in groups_t08:
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
            "## Tranche 9 — Checkmarx KICS, ProjectDiscovery Naabu, ProjectDiscovery `dnsx`, ProjectDiscovery `tlsx`, WPScan, Nikto, Wapiti, Arjun, `jwt_tool` (RFC 8725) e Feroxbuster (100 notas; revisão factual por IA registrada)",
            "",
        ]
    )
    for context, rows in groups_t09:
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
            "## Tranche 10 — Turbot Steampipe & Powerpipe, CloudQuery, JADX, Apktool, Pwndbg, Ropper, Thoughtworks Talisman, awslabs `git-secrets`, CDK (Container Penetration Toolkit) e Peirates (100 notas; revisão factual por IA registrada)",
            "",
        ]
    )
    for context, rows in groups_t10:
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
            "## Tranche 11 — CNCF Cartography, NCC Group Scout Suite, Rhino Security Labs Pacu, MobSF & `mobsfscan`, SensePost Objection, `angr`, Yelp `detect-secrets`, GitHub CodeQL, SigmaHQ e Yamato Security Hayabusa (100 notas; revisão factual por IA registrada)",
            "",
        ]
    )
    for context, rows in groups_t11:
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
            "As 1100 notas 1–1100 das tranches 1–11 têm revisão factual por IA registrada nos relatórios vinculados. O lote continua incompleto: são 1100/2.000 notas válidas, restando 900 notas materiais.",
            "",
        ]
    )
    return "\n".join(lines)


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
) -> str:
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
        f"Índice das 1100 notas substantivas redigidas até agora no lote `{BATCH_ID}`, cuja meta é 2.000. As 1100 passaram pelo gate automatizado e receberam revisão factual por IA registrada separadamente (nenhuma delas é aprovação humana).",
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
            "## Tranche 6 — TheHive & Cortex, Filigran OpenCTI, Google Timesketch & Plaso, Volatility 3 & `dwarf2json`, CAPEv2 Sandbox, Wireshark & `tshark`, Bettercap, Responder, Fortra Impacket e NetExec (`nxc`)",
            "",
        ]
    )
    for context, rows in groups_t06:
        lines.append(f"### {context['group_title']}")
        lines.append("")
        for index, row in enumerate(rows):
            number = int(context["first"]) + index
            lines.append(f"{number}. [[{row['slug']}]] — {row['summary']}")
        lines.append("")

    lines.extend(
        [
            "## Tranche 7 — `testssl.sh`, EFF Certbot (ACME), Hashcat, NSA Ghidra, Radare2 (`r2`), Frida, Fail2ban, Sudo (`sudo` & `sudo_logsrvd`), Bubblewrap (`bwrap`) e Project Quay Clair v4 (`ClairCore`)",
            "",
        ]
    )
    for context, rows in groups_t07:
        lines.append(f"### {context['group_title']}")
        lines.append("")
        for index, row in enumerate(rows):
            number = int(context["first"]) + index
            lines.append(f"{number}. [[{row['slug']}]] — {row['summary']}")
        lines.append("")

    lines.extend(
        [
            "## Tranche 8 — GnuPG (`gpg`), VeraCrypt, Linux Cryptsetup & LUKS2, Clevis & Tang (NBDE), `mitmproxy`, Gobuster, OWASP Amass (OAM), Masscan, RustScan e ZMap & ZGrab 2.0",
            "",
        ]
    )
    for context, rows in groups_t08:
        lines.append(f"### {context['group_title']}")
        lines.append("")
        for index, row in enumerate(rows):
            number = int(context["first"]) + index
            lines.append(f"{number}. [[{row['slug']}]] — {row['summary']}")
        lines.append("")

    lines.extend(
        [
            "## Tranche 9 — Checkmarx KICS, ProjectDiscovery Naabu, ProjectDiscovery `dnsx`, ProjectDiscovery `tlsx`, WPScan, Nikto, Wapiti, Arjun, `jwt_tool` (RFC 8725) e Feroxbuster",
            "",
        ]
    )
    for context, rows in groups_t09:
        lines.append(f"### {context['group_title']}")
        lines.append("")
        for index, row in enumerate(rows):
            number = int(context["first"]) + index
            lines.append(f"{number}. [[{row['slug']}]] — {row['summary']}")
        lines.append("")

    lines.extend(
        [
            "## Tranche 10 — Turbot Steampipe & Powerpipe, CloudQuery, JADX, Apktool, Pwndbg, Ropper, Thoughtworks Talisman, awslabs `git-secrets`, CDK (Container Penetration Toolkit) e Peirates",
            "",
        ]
    )
    for context, rows in groups_t10:
        lines.append(f"### {context['group_title']}")
        lines.append("")
        for index, row in enumerate(rows):
            number = int(context["first"]) + index
            lines.append(f"{number}. [[{row['slug']}]] — {row['summary']}")
        lines.append("")

    lines.extend(
        [
            "## Tranche 11 — CNCF Cartography, NCC Group Scout Suite, Rhino Security Labs Pacu, MobSF & `mobsfscan`, SensePost Objection, `angr`, Yelp `detect-secrets`, GitHub CodeQL, SigmaHQ e Yamato Security Hayabusa",
            "",
        ]
    )
    for context, rows in groups_t11:
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
            f"O gate automatizado foi aprovado por 1100/1100 notas e as 1100 contam como válidas pelo protocolo atualizado, com revisão factual por IA registrada separadamente. O lote de 2.000 continua `in_progress` (1100 notas substantivas; 900 ainda não produzidas). Consulte o [manifesto](../../exports/batches/{BATCH_ID}.md), a [auditoria de qualidade](../../exports/reports/note-quality-{BATCH_ID}.md) e a [reconciliação mais recente do manifesto/fila](../../exports/reports/{RECON_NAME}). Os relatórios factuais por IA são [tranche 1](../../exports/reports/{REPORT_T01}), [tranche 2](../../exports/reports/{REPORT_T02}), [tranche 3](../../exports/reports/{REPORT_T03}), [tranche 4](../../exports/reports/{REPORT_T04}), [tranche 5](../../exports/reports/{REPORT_T05}), [tranche 6](../../exports/reports/{REPORT_T06}), [tranche 7](../../exports/reports/{REPORT_T07}), [tranche 8](../../exports/reports/{REPORT_T08}), [tranche 9](../../exports/reports/{REPORT_T09}), [tranche 10](../../exports/reports/{REPORT_T10}) e [tranche 11](../../exports/reports/{REPORT_NAME}).",
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


def review_rows(groups_t11) -> str:
    lines = []
    for context, rows in groups_t11:
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
    groups_t01 = load_groups(bs01)
    groups_t02 = load_groups(bs02)
    groups_t03 = load_groups(bs03)
    groups_t04 = load_groups(bs04)
    groups_t05 = load_groups(bs05)
    groups_t06 = load_groups(bs06)
    groups_t07 = load_groups(bs07)
    groups_t08 = load_groups(bs08)
    groups_t09 = load_groups(bs09)
    groups_t10 = load_groups(bs10)
    groups_t11 = load_groups(bs11)
    total_t11 = sum(len(rows) for _, rows in groups_t11)
    if total_t11 != 100 or int(groups_t11[0][0]["first"]) != 1001 or int(groups_t11[-1][0]["first"]) != 1091:
        raise SystemExit(f"dados inesperados: {total_t11} notas, primeiro grupo em {groups_t11[0][0]['first']}")

    manifest = KF / "exports" / "batches" / f"{BATCH_ID}.md"
    moc = KF / "00-home-vault" / "MOCs" / "MOC-Seguranca-Software-0009.md"
    queue = KF / "exports" / "reports" / "human-review-queue.md"

    manifest.write_text(
        render_manifest(
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
        ),
        encoding="utf-8",
    )
    print(f"ok {manifest.relative_to(ROOT)}")
    moc.write_text(
        render_moc(
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
        ),
        encoding="utf-8",
    )
    print(f"ok {moc.relative_to(ROOT)}")

    insert_before(queue, "## Regra de contagem", review_rows(groups_t11), marker="| 5041 | `software-seguranca-2000-0003` |")

    apply(
        queue,
        [
            (
                "distingue 4991 revisões factuais realizadas por IA nos lotes `software-testes-2000-0001` (1991), `software-devops-2000-0002` (2000) e `software-seguranca-2000-0003` (1000)",
                "distingue 5091 revisões factuais realizadas por IA nos lotes `software-testes-2000-0001` (1991), `software-devops-2000-0002` (2000) e `software-seguranca-2000-0003` (1100)",
            ),
            (
                "- Aprovações por IA registradas separadamente: **4991**.",
                "- Aprovações por IA registradas separadamente: **5091**.",
            ),
            (
                "- Notas válidas contabilizadas (gate + revisão humana ou IA): **5040**.",
                "- Notas válidas contabilizadas (gate + revisão humana ou IA): **5140**.",
            ),
            (
                "As 4991 linhas `APROVADA POR IA` (nº 50–5040) correspondem às 1991 notas 10–2000 das tranches 2–26 do lote `software-testes-2000-0001`, às 2000 notas 1–2000 das tranches 1–20 do lote `software-devops-2000-0002` e às 1000 notas 1–1000 das tranches 1–10 do lote `software-seguranca-2000-0003`",
                "As 5091 linhas `APROVADA POR IA` (nº 50–5140) correspondem às 1991 notas 10–2000 das tranches 2–26 do lote `software-testes-2000-0001`, às 2000 notas 1–2000 das tranches 1–20 do lote `software-devops-2000-0002` e às 1100 notas 1–1100 das tranches 1–11 do lote `software-seguranca-2000-0003`",
            ),
        ],
    )

    apply(
        ROOT / "README.md",
        [
            (
                "| Notas válidas contabilizadas | 5040 / 1.000.000 (0,5040%) | 49 com aprovação humana histórica + 4991 com revisão factual por IA |",
                "| Notas válidas contabilizadas | 5140 / 1.000.000 (0,5140%) | 49 com aprovação humana histórica + 5091 com revisão factual por IA |",
            ),
            (
                "| Notas com revisão factual por IA registrada | 4991 | Revisões dos lotes de escala (1991 no lote 1 + 2000 no lote 2 + 1000 no lote 3), com relatórios por tranche; não são humanas |",
                "| Notas com revisão factual por IA registrada | 5091 | Revisões dos lotes de escala (1991 no lote 1 + 2000 no lote 2 + 1100 no lote 3), com relatórios por tranche; não são humanas |",
            ),
            (
                "| Terceiro lote `software-seguranca-2000-0003` | 1000 / 2.000 (50,00%) | 1000 aprovadas por IA nas tranches 1–10; faltam 1.000 notas substantivas |",
                "| Terceiro lote `software-seguranca-2000-0003` | 1100 / 2.000 (55,00%) | 1100 aprovadas por IA nas tranches 1–11; faltam 900 notas substantivas |",
            ),
            (
                "| Arquivos Markdown ativos em `knowledge-federation/domains/` | 5140 | 100 notas legadas com pendências + 5040 notas autorais substantivas |",
                "| Arquivos Markdown ativos em `knowledge-federation/domains/` | 5240 | 100 notas legadas com pendências + 5140 notas autorais substantivas |",
            ),
            (
                "e o terceiro lote em andamento é [`software-seguranca-2000-0003`](knowledge-federation/exports/batches/software-seguranca-2000-0003.md): 1000 notas materiais já passaram pelo gate e revisão factual por IA até a [tranche 10](knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-10.md) ([reconciliação](knowledge-federation/exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-10.md), [auditoria do lote](knowledge-federation/exports/reports/note-quality-software-seguranca-2000-0003.md) e [MOC de Segurança](knowledge-federation/00-home-vault/MOCs/MOC-Seguranca-Software-0009.md)), com meta de 2.000.",
                "e o terceiro lote em andamento é [`software-seguranca-2000-0003`](knowledge-federation/exports/batches/software-seguranca-2000-0003.md): 1100 notas materiais já passaram pelo gate e revisão factual por IA até a [tranche 11](knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-11.md) ([reconciliação](knowledge-federation/exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-11.md), [auditoria do lote](knowledge-federation/exports/reports/note-quality-software-seguranca-2000-0003.md) e [MOC de Segurança](knowledge-federation/00-home-vault/MOCs/MOC-Seguranca-Software-0009.md)), com meta de 2.000.",
            ),
        ],
    )

    apply(
        KF / "README.md",
        [
            (
                "- Arquivos Markdown ativos: **5140** (100 notas legadas com pendências + 5040 notas autorais substantivas).",
                "- Arquivos Markdown ativos: **5240** (100 notas legadas com pendências + 5140 notas autorais substantivas).",
            ),
            (
                "- Notas válidas pelo protocolo atual: **5040** (49 aprovações humanas históricas + 4991 revisões factuais por IA).",
                "- Notas válidas pelo protocolo atual: **5140** (49 aprovações humanas históricas + 5091 revisões factuais por IA).",
            ),
            (
                "- Progresso: **5040 / 1.000.000 (0,5040%)**; faltam 994.960 notas válidas.",
                "- Progresso: **5140 / 1.000.000 (0,5140%)**; faltam 994.860 notas válidas.",
            ),
            (
                "- Terceiro lote em andamento `software-seguranca-2000-0003`: **1000 / 2.000** notas válidas (50,00%); 1000 por IA ([tranche 10](exports/reports/ai-review-software-seguranca-2000-0003-tranche-10.md) e [reconciliação](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-10.md)); faltam 1.000 notas materiais.",
                "- Terceiro lote em andamento `software-seguranca-2000-0003`: **1100 / 2.000** notas válidas (55,00%); 1100 por IA ([tranche 11](exports/reports/ai-review-software-seguranca-2000-0003-tranche-11.md) e [reconciliação](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-11.md)); faltam 900 notas materiais.",
            ),
        ],
    )

    apply(
        KF / "README-1M.md",
        [
            (
                "tem 5040 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 4991 revisões factuais por IA registradas separadamente). O diretório ativo tem 5140 arquivos Markdown, incluindo 100 notas legadas com pendências, ainda excluídas da contagem. O terceiro lote [`software-seguranca-2000-0003`](exports/batches/software-seguranca-2000-0003.md) está em andamento com 1000/2.000 notas válidas ([relatório factual por IA da tranche 10](exports/reports/ai-review-software-seguranca-2000-0003-tranche-10.md) e [reconciliação da tranche 10](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-10.md)),",
                "tem 5140 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 5091 revisões factuais por IA registradas separadamente). O diretório ativo tem 5240 arquivos Markdown, incluindo 100 notas legadas com pendências, ainda excluídas da contagem. O terceiro lote [`software-seguranca-2000-0003`](exports/batches/software-seguranca-2000-0003.md) está em andamento com 1100/2.000 notas válidas ([relatório factual por IA da tranche 11](exports/reports/ai-review-software-seguranca-2000-0003-tranche-11.md) e [reconciliação da tranche 11](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-11.md)),",
            ),
        ],
    )

    apply(
        KF / "STATUS-CONSOLIDACAO-1M.md",
        [
            (
                "A auditoria encontrou 5140 arquivos Markdown ativos: 5040 notas substantivas passaram pelo gate e receberam revisão factual registrada (49 humanas históricas + 4991 por IA)",
                "A auditoria encontrou 5240 arquivos Markdown ativos: 5140 notas substantivas passaram pelo gate e receberam revisão factual registrada (49 humanas históricas + 5091 por IA)",
            ),
            (
                "| Progresso válido global | 5040 / 1.000.000 (0,5040%) | 49 revisões humanas históricas + 4991 revisões por IA registradas separadamente |",
                "| Progresso válido global | 5140 / 1.000.000 (0,5140%) | 49 revisões humanas históricas + 5091 revisões por IA registradas separadamente |",
            ),
            (
                "| Revisões factuais por IA registradas | 4991 | Relatórios das tranches 2–26 (`software-testes-2000-0001`), tranches 1–20 (`software-devops-2000-0002`) e tranches 1–10 (`software-seguranca-2000-0003`); não são humanas |",
                "| Revisões factuais por IA registradas | 5091 | Relatórios das tranches 2–26 (`software-testes-2000-0001`), tranches 1–20 (`software-devops-2000-0002`) e tranches 1–11 (`software-seguranca-2000-0003`); não são humanas |",
            ),
            (
                "| Terceiro lote (`software-seguranca-2000-0003`) | 1000 / 2.000 (50,00%) | 1000 IA nas tranches 1–10 ([tranche 10](exports/reports/ai-review-software-seguranca-2000-0003-tranche-10.md)); faltam 1.000 notas substantivas |",
                "| Terceiro lote (`software-seguranca-2000-0003`) | 1100 / 2.000 (55,00%) | 1100 IA nas tranches 1–11 ([tranche 11](exports/reports/ai-review-software-seguranca-2000-0003-tranche-11.md)); faltam 900 notas substantivas |",
            ),
            (
                "| Candidatas que passaram pelo gate automatizado | 5040 |",
                "| Candidatas que passaram pelo gate automatizado | 5140 |",
            ),
            (
                "e o terceiro lote [`software-seguranca-2000-0003`](exports/batches/software-seguranca-2000-0003.md) está em 1000/2.000 notas válidas após a [tranche 10](exports/reports/ai-review-software-seguranca-2000-0003-tranche-10.md) ([reconciliação](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-10.md)).",
                "e o terceiro lote [`software-seguranca-2000-0003`](exports/batches/software-seguranca-2000-0003.md) está em 1100/2.000 notas válidas após a [tranche 11](exports/reports/ai-review-software-seguranca-2000-0003-tranche-11.md) ([reconciliação](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-11.md)).",
            ),
            (
                "3. Continuar o terceiro lote `software-seguranca-2000-0003` (atualmente em 1000/2.000; faltam 1.000 notas substantivas) e os 497 lotes subsequentes,",
                "3. Continuar o terceiro lote `software-seguranca-2000-0003` (atualmente em 1100/2.000; faltam 900 notas substantivas) e os 497 lotes subsequentes,",
            ),
        ],
    )

    apply(
        KF / "PLANO-CONTINUO-1M.md",
        [
            (
                "- Notas válidas globais: **5040** (49 aprovações humanas históricas + 4991 revisões factuais por IA).",
                "- Notas válidas globais: **5140** (49 aprovações humanas históricas + 5091 revisões factuais por IA).",
            ),
            (
                "- Progresso: **5040 / 1.000.000 (0,5040%)**; faltam **994.960** notas válidas.",
                "- Progresso: **5140 / 1.000.000 (0,5140%)**; faltam **994.860** notas válidas.",
            ),
            (
                "- Terceiro lote atual `software-seguranca-2000-0003`: **1000 / 2.000 (50,00%)** notas válidas (1000 IA nas tranches 1–10); faltam **1.000** notas substantivas.",
                "- Terceiro lote atual `software-seguranca-2000-0003`: **1100 / 2.000 (55,00%)** notas válidas (1100 IA nas tranches 1–11); faltam **900** notas substantivas.",
            ),
            (
                "- Arquivos Markdown ativos: **5140**; 100 com pendências de qualidade, excluídos da contagem.",
                "- Arquivos Markdown ativos: **5240**; 100 com pendências de qualidade, excluídos da contagem.",
            ),
            (
                "| 5 | Rodar gate, testes, auditorias e diff | **Concluído para o estado atual** | Lote 1: 2000/2000 (`complete`). Lote 2: 2000/2000 (`complete`). Lote 3 (`software-seguranca-2000-0003`): 1000/1000 no gate (1000 IA). Global: 5140 arquivos, 5040 válidas, 100 com pendências legadas; veja a [reconciliação da tranche 10 do lote 3](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-10.md). |",
                "| 5 | Rodar gate, testes, auditorias e diff | **Concluído para o estado atual** | Lote 1: 2000/2000 (`complete`). Lote 2: 2000/2000 (`complete`). Lote 3 (`software-seguranca-2000-0003`): 1100/1100 no gate (1100 IA). Global: 5240 arquivos, 5140 válidas, 100 com pendências legadas; veja a [reconciliação da tranche 11 do lote 3](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-11.md). |",
            ),
            (
                "| 8 | Abrir lotes subsequentes de 2.000 notas | **Em andamento (lote 3 em 50%)** | Terceiro lote `software-seguranca-2000-0003` em 1000/2.000 notas válidas nas tranches 1–10; restam 1.000 notas neste lote e 497 lotes subsequentes. |",
                "| 8 | Abrir lotes subsequentes de 2.000 notas | **Em andamento (lote 3 em 55%)** | Terceiro lote `software-seguranca-2000-0003` em 1100/2.000 notas válidas nas tranches 1–11; restam 900 notas neste lote e 497 lotes subsequentes. |",
            ),
            (
                "Progresso atual: 5040 notas válidas, 2/500 lotes completos.",
                "Progresso atual: 5140 notas válidas, 2/500 lotes completos.",
            ),
        ],
    )

    apply(
        KF / "RECOVERY-AND-SCALE-NOTE.md",
        [
            (
                "há 5140 arquivos: 100 legados com pendências e 5040 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 4991 revisões por IA). O primeiro lote `software-testes-2000-0001` atingiu 2000/2.000 notas válidas (9 humanas + 1991 IA, `complete`); o segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) atingiu 2000/2.000 notas válidas (`complete`, [tranche 20](exports/reports/ai-review-software-devops-2000-0002-tranche-20.md)); e o terceiro lote [`software-seguranca-2000-0003`](exports/batches/software-seguranca-2000-0003.md) está em andamento (`in_progress`) com 1000/2.000 notas válidas revisadas por IA até a [tranche 10](exports/reports/ai-review-software-seguranca-2000-0003-tranche-10.md), com [reconciliação](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-10.md);",
                "há 5240 arquivos: 100 legados com pendências e 5140 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 5091 revisões por IA). O primeiro lote `software-testes-2000-0001` atingiu 2000/2.000 notas válidas (9 humanas + 1991 IA, `complete`); o segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) atingiu 2000/2.000 notas válidas (`complete`, [tranche 20](exports/reports/ai-review-software-devops-2000-0002-tranche-20.md)); e o terceiro lote [`software-seguranca-2000-0003`](exports/batches/software-seguranca-2000-0003.md) está em andamento (`in_progress`) com 1100/2.000 notas válidas revisadas por IA até a [tranche 11](exports/reports/ai-review-software-seguranca-2000-0003-tranche-11.md), com [reconciliação](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-11.md);",
            ),
            (
                "4. Continuar o terceiro lote `software-seguranca-2000-0003` (1000/2.000; faltam 1.000 notas qualificadas) até 2.000 antes de abrir os 497 lotes seguintes.",
                "4. Continuar o terceiro lote `software-seguranca-2000-0003` (1100/2.000; faltam 900 notas qualificadas) até 2.000 antes de abrir os 497 lotes seguintes.",
            ),
        ],
    )

    apply(
        KF / "00-home-vault" / "Home.md",
        [
            (
                "- [[MOC-Seguranca-Software-0009]] — 1000 notas do terceiro lote de escala `software-seguranca-2000-0003` (meta: 2.000); 1000 revisões factuais por IA.",
                "- [[MOC-Seguranca-Software-0009]] — 1100 notas do terceiro lote de escala `software-seguranca-2000-0003` (meta: 2.000); 1100 revisões factuais por IA.",
            ),
            (
                "[[human-review-queue|Registro de revisões factuais]] — 49 aprovações humanas e 4991 aprovações por IA, identificadas separadamente.",
                "[[human-review-queue|Registro de revisões factuais]] — 49 aprovações humanas e 5091 aprovações por IA, identificadas separadamente.",
            ),
            (
                "[[note-quality-audit|Auditoria de qualidade]] — 5040 notas válidas pelo protocolo atual (49 humanas + 4991 IA) e 100 notas legadas com falhas.",
                "[[note-quality-audit|Auditoria de qualidade]] — 5140 notas válidas pelo protocolo atual (49 humanas + 5091 IA) e 100 notas legadas com falhas.",
            ),
        ],
    )

    apply(
        KF / "00-home-vault" / "Indice-Global.md",
        [
            (
                "- Arquivos Markdown em `domains/`: **5140** (100 sementes legadas + 5040 notas autorais substantivas).",
                "- Arquivos Markdown em `domains/`: **5240** (100 sementes legadas + 5140 notas autorais substantivas).",
            ),
            (
                "- Candidatas aprovadas no gate automatizado: **5040**; revisões humanas registradas: **49**; revisões factuais por IA: **4991**; 100 sementes legadas mantêm pendências.",
                "- Candidatas aprovadas no gate automatizado: **5140**; revisões humanas registradas: **49**; revisões factuais por IA: **5091**; 100 sementes legadas mantêm pendências.",
            ),
            (
                "- Os lotes atuais totalizam 5040 notas válidas pelo protocolo; o terceiro lote [`software-seguranca-2000-0003`](../exports/batches/software-seguranca-2000-0003.md) tem 1000/2.000 ([tranche 10](../exports/reports/ai-review-software-seguranca-2000-0003-tranche-10.md), [reconciliação da tranche 10](../exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-10.md) e [[MOC-Seguranca-Software-0009]]),",
                "- Os lotes atuais totalizam 5140 notas válidas pelo protocolo; o terceiro lote [`software-seguranca-2000-0003`](../exports/batches/software-seguranca-2000-0003.md) tem 1100/2.000 ([tranche 11](../exports/reports/ai-review-software-seguranca-2000-0003-tranche-11.md), [reconciliação da tranche 11](../exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-11.md) e [[MOC-Seguranca-Software-0009]]),",
            ),
        ],
    )
    print("reconciliação concluída")


if __name__ == "__main__":
    main()
