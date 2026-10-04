#!/usr/bin/env python3
"""Reconcile batch software-seguranca-2000-0003 tranche 16 (IDs 1501-1600, advancing batch 3 to 1600/2000 [80%]) across manifest, MOC, review registry and status docs."""
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
REPORT_T12 = "ai-review-software-seguranca-2000-0003-tranche-12.md"
REPORT_T13 = "ai-review-software-seguranca-2000-0003-tranche-13.md"
REPORT_T14 = "ai-review-software-seguranca-2000-0003-tranche-14.md"
REPORT_T15 = "ai-review-software-seguranca-2000-0003-tranche-15.md"
REPORT_NAME = "ai-review-software-seguranca-2000-0003-tranche-16.md"
RECON_NAME = "batch-reconciliation-software-seguranca-2000-0003-tranche-16.md"
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
    groups_t13,
    groups_t14,
    groups_t15,
    groups_t16,
) -> str:
    lines = [
        f"# Lote `{BATCH_ID}` — Engenharia de Segurança de Software, AppSec, DevSecOps e IAM",
        "",
        f"Manifesto auditável do terceiro lote de escala (`{BATCH_ID}`), focado em segurança de aplicações (AppSec & Mobile MobSF/`mobsfscan`/Objection/JADX/Apktool), SAST/DAST/IaC/Proxies e Simulação de Phishing (Gophish/GitHub CodeQL/Checkmarx KICS/Wapiti/Nikto/WPScan/Arjun/Feroxbuster/`jwt_tool`/`mitmproxy`/ZAP/Nuclei/Gobuster/`ffuf`/`sqlmap`/Dalfox), WAF/NSM, Full Packet Capture, Síntese/Captura BPF, WIDS/Auditoria Sem Fio 802.11, Caça a Beacons e Firewalls/VPNs de Kernel (Scapy/`tcpdump` & `libpcap`/Kismet WIDS/Aircrack-ng/Cisco Snort 3/Arkime FPC/RITA Zeek Hunting/OWASP ModSecurity v3 `libmodsecurity`/strongSwan IPsec IKEv2/Linux `nftables`/WireGuard/OpenSSH/Coraza/CRS v4/Suricata/Zeek), segurança em runtime, Application Whitelisting `fanotify`, Sandboxing & pós-exploração de containers/Kubernetes (`fapolicyd`/Firejail/CDK/Peirates/eBPF/LSMs AppArmor & SELinux/Bubblewrap/KubeArmor/Tracee), DFIR/Threat Intelligence, Super Timelines, Análise de Malware, Detecção Sigma, Emulação de Adversários C2, Pivoting L3/L4, Honeypots, Fuzzing Guiado por Cobertura, Instrumentação Binária Dinâmica & Binary Exploitation (AFL++/Valgrind `Memcheck` & `Helgrind`/Sliver C2/Ligolo-ng `TUN`+`gVisor`/Chisel/Plaso `log2timeline`/Mandiant `capa`/Mandiant `FLOSS`/WithSecure Chainsaw/Atomic Red Team/MITRE Caldera/Cowrie/OpenCanary/SigmaHQ/Hayabusa/`angr`/Pwndbg/Ropper/TheHive/Cortex/OpenCTI/Timesketch/Volatility 3/CAPEv2/Wireshark/Ghidra/Radare2/Frida/MISP/Velociraptor/auditd), criptografia moderna, Raiz de Confiança em Hardware TPM 2.0, Atestação Remota Keylime, Tokens FIDO2/PIV YubiKey, Auditoria de Senhas Offline/Online, Cofres Zero-Knowledge, FDE/NBDE & PKI/TLS (THC-Hydra/Keylime/YubiKey `ykman` & `pam-u2f`/John the Ripper Jumbo/Rustls/TPM 2.0 `tpm2-tools` & `tpm2-tss`/Vaultwarden/OpenSSL 3.x/KeePassXC/`tlsx`/GnuPG/VeraCrypt/Cryptsetup LUKS2/Clevis & Tang/`testssl.sh`/Certbot ACME/Hashcat/`age`), EASM, Gerenciamento de Vulnerabilidades Enterprise (GVM/OpenVAS) & varredura de rede/DNS em escala (Greenbone GVM & OpenVAS/Naabu/`dnsx`/`tlsx`/OWASP Amass/Masscan/RustScan/ZMap & ZGrab2/Subfinder/`httpx`/Katana), postura multi-cloud CSPM, Conformidade SCAP, grafos de ataque, pentest cloud, containers, autenticação PAM e integridade de host (OpenSCAP & ComplianceAsCode/Linux-PAM `pam_faillock`/AIDE/CNCF Cartography/Scout Suite/Pacu/Steampipe & Powerpipe/CloudQuery/Clair v4/Fail2ban/Sudo/Lynis/USBGuard/Prowler/osquery), segurança da cadeia de suprimentos de software, Reachable SCA e prevenção de vazamento de segredos (OWASP Dependency-Check/`pip-audit` & PyPA Advisory DB/Go `govulncheck` & `vuln.go.dev`/Yelp `detect-secrets`/Talisman/`git-secrets`/Gitleaks/TruffleHog/in-toto/GUAC/Sigstore Rekor & Fulcio/OSV-Scanner/Dependency-Track/Scorecard) e auditoria/identidade Active Directory, FreeIPA, SSSD, IdM, PAM & Acesso Zero-Trust (SSSD/Gravitational Teleport/FreeIPA/authentik/Kanidm/Certipy/Bettercap/Responder/Impacket/NetExec/BloodHound CE/Paralus/OpenZiti/Hydra/Kratos/Authelia/Dex/Pomerium/OpenFGA/SpiceDB/Cerbos).",
        "",
        "## Resumo do estado atual",
        "",
        "- Domínio / subdomínio: `software` / `seguranca` (`knowledge-federation/domains/software-0009/software/seguranca/`)",
        "- Meta do lote: **2.000 notas substantivas**",
        "- Notas efetivamente redigidas até agora: **1600 / 2.000 (80,00%)**",
        "- Gate automatizado: **1600/1600 aprovadas** (conteúdo mínimo, seções, fontes específicas e wikilinks; reexecutado após a tranche 16)",
        "- Revisão factual humana: **0/1600**",
        "- Revisão factual por IA: **1600/1600**",
        "- Contabilizadas como válidas: **1600/1600**",
        "- Revisor das 1600 notas aprovadas por IA: `Arena.ai Agent Mode`, com relatórios específicos; não são aprovações humanas",
        "- Status do lote maior: `in_progress`; tranches 1–16 (1600 notas, IDs 1–1600) foram conferidas factualmente por IA e aprovadas sob o protocolo atualizado",
        "- MOC do lote: [`MOC-Seguranca-Software-0009.md`](../../00-home-vault/MOCs/MOC-Seguranca-Software-0009.md)",
        "- Relatório de qualidade do lote: [`note-quality-software-seguranca-2000-0003.md`](../reports/note-quality-software-seguranca-2000-0003.md)",
        f"- Reconciliação estrutural mais recente do manifesto/fila: [`{RECON_NAME}`](../reports/{RECON_NAME})",
        f"- Relatórios factuais por IA: [`tranche 1`](../reports/{REPORT_T01}), [`tranche 2`](../reports/{REPORT_T02}), [`tranche 3`](../reports/{REPORT_T03}), [`tranche 4`](../reports/{REPORT_T04}), [`tranche 5`](../reports/{REPORT_T05}), [`tranche 6`](../reports/{REPORT_T06}), [`tranche 7`](../reports/{REPORT_T07}), [`tranche 8`](../reports/{REPORT_T08}), [`tranche 9`](../reports/{REPORT_T09}), [`tranche 10`](../reports/{REPORT_T10}), [`tranche 11`](../reports/{REPORT_T11}), [`tranche 12`](../reports/{REPORT_T12}), [`tranche 13`](../reports/{REPORT_T13}), [`tranche 14`](../reports/{REPORT_T14}), [`tranche 15`](../reports/{REPORT_T15}), [`tranche 16`](../reports/{REPORT_NAME})",
        "",
        "Existem 1600 notas materiais listadas abaixo; não há IDs reservados, placeholders ou registros virtuais para as 400 restantes.",
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
        (
            "## Tranche 13 — KeePassXC (`keepassxc-cli`), Plaso (`log2timeline` / `psort`), Mandiant `capa`, Mandiant FLOSS (`flare-floss`), Gophish, OWASP ModSecurity v3 (`libmodsecurity`), strongSwan IPsec/IKEv2 (`swanctl`), Firejail Sandbox, Linux-PAM (`pam_faillock`) e OpenSSL 3.x (100 notas; revisão factual por IA registrada)",
            groups_t13,
        ),
        (
            "## Tranche 14 — authentik (`goauthentik`), Kanidm (`kanidmd` / `kanidm-unixd`), Vaultwarden (`dani-garcia/vaultwarden`), Rustls (`rustls` / `aws-lc-rs`), Cisco Snort 3 (`Snort++`), Arkime Full Packet Capture, RITA (`activecm/rita`), Gravitational Teleport, FreeIPA (`Red Hat IdM`) e TPM 2.0 (`tpm2-tools` & `tpm2-tss`) (100 notas; revisão factual por IA registrada)",
            groups_t14,
        ),
        (
            "## Tranche 15 — SSSD (`System Security Services Daemon`), Keylime (`keylime` / `rust-keylime`), OpenSCAP & ComplianceAsCode (`oscap`), `fapolicyd` (`fanotify`), YubiKey (`ykman` & `pam-u2f`), John the Ripper Jumbo, Aircrack-ng Suite, Kismet Wireless WIDS, Scapy e `tcpdump` & `libpcap` (100 notas; revisão factual por IA registrada)",
            groups_t15,
        ),
        (
            "## Tranche 16 — Greenbone GVM & OpenVAS (`gvmd` / `openvas-scanner`), OWASP Dependency-Check, AFL++ (`AFLplusplus`), Valgrind (`Memcheck` / `Helgrind` / `DRD`), Sliver C2, Chisel, Ligolo-ng (`TUN` + `gVisor`), THC-Hydra, `pip-audit` (`pypa/advisory-database`) e Go `govulncheck` (`vuln.go.dev`) (100 notas; revisão factual por IA registrada)",
            groups_t16,
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
    groups_t13,
    groups_t14,
    groups_t15,
    groups_t16,
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
        f"Mapa de conteúdo das **1600 notas substantivas (Tranches 1–16, IDs `1–1600`)** do lote [`{BATCH_ID}`](../../exports/batches/{BATCH_ID}.md) em `knowledge-federation/domains/software-0009/software/seguranca/`.",
        "",
        "## Estado do lote",
        "",
        "- Progresso atual: **1600 / 2.000 notas válidas (80,00%)** (`status: in_progress`)",
        "- Revisão factual humana: **0 / 1600**",
        "- Revisão factual por IA (`Arena.ai Agent Mode`): **1600 / 1600** ([Tranche 1](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-01.md), [Tranche 2](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-02.md), [Tranche 3](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-03.md), [Tranche 4](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-04.md), [Tranche 5](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-05.md), [Tranche 6](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-06.md), [Tranche 7](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-07.md), [Tranche 8](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-08.md), [Tranche 9](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-09.md), [Tranche 10](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-10.md), [Tranche 11](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-11.md), [Tranche 12](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-12.md), [Tranche 13](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-13.md), [Tranche 14](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-14.md), [Tranche 15](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-15.md), [Tranche 16](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-16.md))",
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
        ("Tranche 13 (IDs 1201–1300)", groups_t13),
        ("Tranche 14 (IDs 1301–1400)", groups_t14),
        ("Tranche 15 (IDs 1401–1500)", groups_t15),
        ("Tranche 16 (IDs 1501–1600)", groups_t16),
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


def review_rows(groups_t16) -> str:
    lines = []
    for context, rows in groups_t16:
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
    bs13 = load_module("bs13", "_build_seguranca_t13.py")
    bs14 = load_module("bs14", "_build_seguranca_t14.py")
    bs15 = load_module("bs15", "_build_seguranca_t15.py")
    bs16 = load_module("bs16", "_build_seguranca_t16.py")

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
    g13 = load_groups(bs13)
    g14 = load_groups(bs14)
    g15 = load_groups(bs15)
    g16 = load_groups(bs16)

    manifest_path = KF / "exports" / "batches" / f"{BATCH_ID}.md"
    manifest_path.write_text(
        render_manifest(g01, g02, g03, g04, g05, g06, g07, g08, g09, g10, g11, g12, g13, g14, g15, g16),
        encoding="utf-8",
    )
    print(f"ok {manifest_path.relative_to(ROOT)}")

    moc_path = KF / "00-home-vault" / "MOCs" / "MOC-Seguranca-Software-0009.md"
    moc_path.write_text(
        render_moc(g01, g02, g03, g04, g05, g06, g07, g08, g09, g10, g11, g12, g13, g14, g15, g16),
        encoding="utf-8",
    )
    print(f"ok {moc_path.relative_to(ROOT)}")

    queue_path = KF / "exports" / "reports" / "human-review-queue.md"
    insert_before(
        queue_path,
        "## Regra de contagem",
        review_rows(g16),
        marker="| 5541 | `software-seguranca-2000-0003` |",
    )

    apply(
        queue_path,
        [
            (
                "distingue 5491 revisões factuais realizadas por IA nos lotes `software-testes-2000-0001` (1991), `software-devops-2000-0002` (2000) e `software-seguranca-2000-0003` (1500)",
                "distingue 5591 revisões factuais realizadas por IA nos lotes `software-testes-2000-0001` (1991), `software-devops-2000-0002` (2000) e `software-seguranca-2000-0003` (1600)",
            ),
            (
                "- Aprovações por IA registradas separadamente: **5491**.",
                "- Aprovações por IA registradas separadamente: **5591**.",
            ),
            (
                "- Notas válidas contabilizadas (gate + revisão humana ou IA): **5540**.",
                "- Notas válidas contabilizadas (gate + revisão humana ou IA): **5640**.",
            ),
            (
                "As 5491 linhas `APROVADA POR IA` (nº 50–5540) correspondem às 1991 notas 10–2000 das tranches 2–26 do lote `software-testes-2000-0001`, às 2000 notas 1–2000 das tranches 1–20 do lote `software-devops-2000-0002` e às 1500 notas 1–1500 das tranches 1–15 do lote `software-seguranca-2000-0003`",
                "As 5591 linhas `APROVADA POR IA` (nº 50–5640) correspondem às 1991 notas 10–2000 das tranches 2–26 do lote `software-testes-2000-0001`, às 2000 notas 1–2000 das tranches 1–20 do lote `software-devops-2000-0002` e às 1600 notas 1–1600 das tranches 1–16 do lote `software-seguranca-2000-0003`",
            ),
        ],
    )

    apply(
        ROOT / "README.md",
        [
            (
                "| Notas válidas contabilizadas | 5540 / 1.000.000 (0,5540%) | 49 com aprovação humana histórica + 5491 com revisão factual por IA |",
                "| Notas válidas contabilizadas | 5640 / 1.000.000 (0,5640%) | 49 com aprovação humana histórica + 5591 com revisão factual por IA |",
            ),
            (
                "| Notas com revisão factual por IA registrada | 5491 | Revisões dos lotes de escala (1991 no lote 1 + 2000 no lote 2 + 1500 no lote 3), com relatórios por tranche; não são humanas |",
                "| Notas com revisão factual por IA registrada | 5591 | Revisões dos lotes de escala (1991 no lote 1 + 2000 no lote 2 + 1600 no lote 3), com relatórios por tranche; não são humanas |",
            ),
            (
                "| Terceiro lote `software-seguranca-2000-0003` | 1500 / 2.000 (75,00%) | 1500 aprovadas por IA nas tranches 1–15; faltam 500 notas substantivas |",
                "| Terceiro lote `software-seguranca-2000-0003` | 1600 / 2.000 (80,00%) | 1600 aprovadas por IA nas tranches 1–16; faltam 400 notas substantivas |",
            ),
            (
                "| Arquivos Markdown ativos em `knowledge-federation/domains/` | 5640 | 100 notas legadas com pendências + 5540 notas autorais substantivas |",
                "| Arquivos Markdown ativos em `knowledge-federation/domains/` | 5740 | 100 notas legadas com pendências + 5640 notas autorais substantivas |",
            ),
            (
                "e o terceiro lote em andamento é [`software-seguranca-2000-0003`](knowledge-federation/exports/batches/software-seguranca-2000-0003.md): 1500 notas materiais já passaram pelo gate e revisão factual por IA até a [tranche 15](knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-15.md) ([reconciliação](knowledge-federation/exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-15.md), [auditoria do lote](knowledge-federation/exports/reports/note-quality-software-seguranca-2000-0003.md) e [MOC de Segurança](knowledge-federation/00-home-vault/MOCs/MOC-Seguranca-Software-0009.md)), com meta de 2.000.",
                "e o terceiro lote em andamento é [`software-seguranca-2000-0003`](knowledge-federation/exports/batches/software-seguranca-2000-0003.md): 1600 notas materiais já passaram pelo gate e revisão factual por IA até a [tranche 16](knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-16.md) ([reconciliação](knowledge-federation/exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-16.md), [auditoria do lote](knowledge-federation/exports/reports/note-quality-software-seguranca-2000-0003.md) e [MOC de Segurança](knowledge-federation/00-home-vault/MOCs/MOC-Seguranca-Software-0009.md)), com meta de 2.000.",
            ),
        ],
    )

    apply(
        KF / "README.md",
        [
            (
                "- Arquivos Markdown ativos: **5640** (100 notas legadas com pendências + 5540 notas autorais substantivas).",
                "- Arquivos Markdown ativos: **5740** (100 notas legadas com pendências + 5640 notas autorais substantivas).",
            ),
            (
                "- Notas válidas pelo protocolo atual: **5540** (49 aprovações humanas históricas + 5491 revisões factuais por IA).",
                "- Notas válidas pelo protocolo atual: **5640** (49 aprovações humanas históricas + 5591 revisões factuais por IA).",
            ),
            (
                "- Progresso: **5540 / 1.000.000 (0,5540%)**; faltam 994.460 notas válidas.",
                "- Progresso: **5640 / 1.000.000 (0,5640%)**; faltam 994.360 notas válidas.",
            ),
            (
                "- Terceiro lote em andamento `software-seguranca-2000-0003`: **1500 / 2.000** notas válidas (75,00%); 1500 por IA ([tranche 15](exports/reports/ai-review-software-seguranca-2000-0003-tranche-15.md) e [reconciliação](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-15.md)); faltam 500 notas materiais.",
                "- Terceiro lote em andamento `software-seguranca-2000-0003`: **1600 / 2.000** notas válidas (80,00%); 1600 por IA ([tranche 16](exports/reports/ai-review-software-seguranca-2000-0003-tranche-16.md) e [reconciliação](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-16.md)); faltam 400 notas materiais.",
            ),
        ],
    )

    apply(
        KF / "README-1M.md",
        [
            (
                "tem 5540 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 5491 revisões factuais por IA registradas separadamente). O diretório ativo tem 5640 arquivos Markdown, incluindo 100 notas legadas com pendências, ainda excluídas da contagem. O terceiro lote [`software-seguranca-2000-0003`](exports/batches/software-seguranca-2000-0003.md) está em andamento com 1500/2.000 notas válidas ([relatório factual por IA da tranche 15](exports/reports/ai-review-software-seguranca-2000-0003-tranche-15.md) e [reconciliação da tranche 15](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-15.md)),",
                "tem 5640 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 5591 revisões factuais por IA registradas separadamente). O diretório ativo tem 5740 arquivos Markdown, incluindo 100 notas legadas com pendências, ainda excluídas da contagem. O terceiro lote [`software-seguranca-2000-0003`](exports/batches/software-seguranca-2000-0003.md) está em andamento com 1600/2.000 notas válidas ([relatório factual por IA da tranche 16](exports/reports/ai-review-software-seguranca-2000-0003-tranche-16.md) e [reconciliação da tranche 16](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-16.md)),",
            ),
        ],
    )

    apply(
        KF / "STATUS-CONSOLIDACAO-1M.md",
        [
            (
                "A auditoria encontrou 5640 arquivos Markdown ativos: 5540 notas substantivas passaram pelo gate e receberam revisão factual registrada (49 humanas históricas + 5491 por IA)",
                "A auditoria encontrou 5740 arquivos Markdown ativos: 5640 notas substantivas passaram pelo gate e receberam revisão factual registrada (49 humanas históricas + 5591 por IA)",
            ),
            (
                "| Progresso válido global | 5540 / 1.000.000 (0,5540%) | 49 revisões humanas históricas + 5491 revisões por IA registradas separadamente |",
                "| Progresso válido global | 5640 / 1.000.000 (0,5640%) | 49 revisões humanas históricas + 5591 revisões por IA registradas separadamente |",
            ),
            (
                "| Revisões factuais por IA registradas | 5491 | Relatórios das tranches 2–26 (`software-testes-2000-0001`), tranches 1–20 (`software-devops-2000-0002`) e tranches 1–15 (`software-seguranca-2000-0003`); não são humanas |",
                "| Revisões factuais por IA registradas | 5591 | Relatórios das tranches 2–26 (`software-testes-2000-0001`), tranches 1–20 (`software-devops-2000-0002`) e tranches 1–16 (`software-seguranca-2000-0003`); não são humanas |",
            ),
            (
                "| Terceiro lote (`software-seguranca-2000-0003`) | 1500 / 2.000 (75,00%) | 1500 IA nas tranches 1–15 ([tranche 15](exports/reports/ai-review-software-seguranca-2000-0003-tranche-15.md)); faltam 500 notas substantivas |",
                "| Terceiro lote (`software-seguranca-2000-0003`) | 1600 / 2.000 (80,00%) | 1600 IA nas tranches 1–16 ([tranche 16](exports/reports/ai-review-software-seguranca-2000-0003-tranche-16.md)); faltam 400 notas substantivas |",
            ),
            (
                "| Candidatas que passaram pelo gate automatizado | 5540 |",
                "| Candidatas que passaram pelo gate automatizado | 5640 |",
            ),
            (
                "e o terceiro lote [`software-seguranca-2000-0003`](exports/batches/software-seguranca-2000-0003.md) está em 1500/2.000 notas válidas após a [tranche 15](exports/reports/ai-review-software-seguranca-2000-0003-tranche-15.md) ([reconciliação](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-15.md)).",
                "e o terceiro lote [`software-seguranca-2000-0003`](exports/batches/software-seguranca-2000-0003.md) está em 1600/2.000 notas válidas após a [tranche 16](exports/reports/ai-review-software-seguranca-2000-0003-tranche-16.md) ([reconciliação](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-16.md)).",
            ),
            (
                "3. Continuar o terceiro lote `software-seguranca-2000-0003` (atualmente em 1500/2.000; faltam 500 notas substantivas) e os 497 lotes subsequentes,",
                "3. Continuar o terceiro lote `software-seguranca-2000-0003` (atualmente em 1600/2.000; faltam 400 notas substantivas) e os 497 lotes subsequentes,",
            ),
        ],
    )

    apply(
        KF / "PLANO-CONTINUO-1M.md",
        [
            (
                "- Notas válidas globais: **5540** (49 aprovações humanas históricas + 5491 revisões factuais por IA).",
                "- Notas válidas globais: **5640** (49 aprovações humanas históricas + 5591 revisões factuais por IA).",
            ),
            (
                "- Progresso: **5540 / 1.000.000 (0,5540%)**; faltam **994.460** notas válidas.",
                "- Progresso: **5640 / 1.000.000 (0,5640%)**; faltam **994.360** notas válidas.",
            ),
            (
                "- Terceiro lote atual `software-seguranca-2000-0003`: **1500 / 2.000 (75,00%)** notas válidas (1500 IA nas tranches 1–15); faltam **500** notas substantivas.",
                "- Terceiro lote atual `software-seguranca-2000-0003`: **1600 / 2.000 (80,00%)** notas válidas (1600 IA nas tranches 1–16); faltam **400** notas substantivas.",
            ),
            (
                "- Arquivos Markdown ativos: **5640**; 100 com pendências de qualidade, excluídos da contagem.",
                "- Arquivos Markdown ativos: **5740**; 100 com pendências de qualidade, excluídos da contagem.",
            ),
            (
                "| 5 | Rodar gate, testes, auditorias e diff | **Concluído para o estado atual** | Lote 1: 2000/2000 (`complete`). Lote 2: 2000/2000 (`complete`). Lote 3 (`software-seguranca-2000-0003`): 1500/1500 no gate (1500 IA). Global: 5640 arquivos, 5540 válidas, 100 com pendências legadas; veja a [reconciliação da tranche 15 do lote 3](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-15.md). |",
                "| 5 | Rodar gate, testes, auditorias e diff | **Concluído para o estado atual** | Lote 1: 2000/2000 (`complete`). Lote 2: 2000/2000 (`complete`). Lote 3 (`software-seguranca-2000-0003`): 1600/1600 no gate (1600 IA). Global: 5740 arquivos, 5640 válidas, 100 com pendências legadas; veja a [reconciliação da tranche 16 do lote 3](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-16.md). |",
            ),
            (
                "| 8 | Abrir lotes subsequentes de 2.000 notas | **Em andamento (lote 3 em 75%)** | Terceiro lote `software-seguranca-2000-0003` em 1500/2.000 notas válidas nas tranches 1–15; restam 500 notas neste lote e 497 lotes subsequentes. |",
                "| 8 | Abrir lotes subsequentes de 2.000 notas | **Em andamento (lote 3 em 80%)** | Terceiro lote `software-seguranca-2000-0003` em 1600/2.000 notas válidas nas tranches 1–16; restam 400 notas neste lote e 497 lotes subsequentes. |",
            ),
            (
                "Progresso atual: 5540 notas válidas, 2/500 lotes completos.",
                "Progresso atual: 5640 notas válidas, 2/500 lotes completos.",
            ),
        ],
    )

    apply(
        KF / "RECOVERY-AND-SCALE-NOTE.md",
        [
            (
                "há 5640 arquivos: 100 legados com pendências e 5540 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 5491 revisões por IA). O primeiro lote `software-testes-2000-0001` atingiu 2000/2.000 notas válidas (9 humanas + 1991 IA, `complete`); o segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) atingiu 2000/2.000 notas válidas (`complete`, [tranche 20](exports/reports/ai-review-software-devops-2000-0002-tranche-20.md)); e o terceiro lote [`software-seguranca-2000-0003`](exports/batches/software-seguranca-2000-0003.md) está em andamento (`in_progress`) com 1500/2.000 notas válidas revisadas por IA até a [tranche 15](exports/reports/ai-review-software-seguranca-2000-0003-tranche-15.md), com [reconciliação](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-15.md);",
                "há 5740 arquivos: 100 legados com pendências e 5640 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 5591 revisões por IA). O primeiro lote `software-testes-2000-0001` atingiu 2000/2.000 notas válidas (9 humanas + 1991 IA, `complete`); o segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) atingiu 2000/2.000 notas válidas (`complete`, [tranche 20](exports/reports/ai-review-software-devops-2000-0002-tranche-20.md)); e o terceiro lote [`software-seguranca-2000-0003`](exports/batches/software-seguranca-2000-0003.md) está em andamento (`in_progress`) com 1600/2.000 notas válidas revisadas por IA até a [tranche 16](exports/reports/ai-review-software-seguranca-2000-0003-tranche-16.md), com [reconciliação](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-16.md);",
            ),
            (
                "4. Continuar o terceiro lote `software-seguranca-2000-0003` (1500/2.000; faltam 500 notas qualificadas) até 2.000 antes de abrir os 497 lotes seguintes.",
                "4. Continuar o terceiro lote `software-seguranca-2000-0003` (1600/2.000; faltam 400 notas qualificadas) até 2.000 antes de abrir os 497 lotes seguintes.",
            ),
        ],
    )

    apply(
        KF / "00-home-vault" / "Home.md",
        [
            (
                "- [[MOC-Seguranca-Software-0009]] — 1500 notas do terceiro lote de escala `software-seguranca-2000-0003` (meta: 2.000); 1500 revisões factuais por IA.",
                "- [[MOC-Seguranca-Software-0009]] — 1600 notas do terceiro lote de escala `software-seguranca-2000-0003` (meta: 2.000); 1600 revisões factuais por IA.",
            ),
            (
                "[[human-review-queue|Registro de revisões factuais]] — 49 aprovações humanas e 5491 aprovações por IA, identificadas separadamente.",
                "[[human-review-queue|Registro de revisões factuais]] — 49 aprovações humanas e 5591 aprovações por IA, identificadas separadamente.",
            ),
            (
                "[[note-quality-audit|Auditoria de qualidade]] — 5540 notas válidas pelo protocolo atual (49 humanas + 5491 IA) e 100 notas legadas com falhas.",
                "[[note-quality-audit|Auditoria de qualidade]] — 5640 notas válidas pelo protocolo atual (49 humanas + 5591 IA) e 100 notas legadas com falhas.",
            ),
        ],
    )

    apply(
        KF / "00-home-vault" / "Indice-Global.md",
        [
            (
                "- Arquivos Markdown em `domains/`: **5640** (100 sementes legadas + 5540 notas autorais substantivas).",
                "- Arquivos Markdown em `domains/`: **5740** (100 sementes legadas + 5640 notas autorais substantivas).",
            ),
            (
                "- Candidatas aprovadas no gate automatizado: **5540**; revisões humanas registradas: **49**; revisões factuais por IA: **5491**; 100 sementes legadas mantêm pendências.",
                "- Candidatas aprovadas no gate automatizado: **5640**; revisões humanas registradas: **49**; revisões factuais por IA: **5591**; 100 sementes legadas mantêm pendências.",
            ),
            (
                "- Os lotes atuais totalizam 5540 notas válidas pelo protocolo; o terceiro lote [`software-seguranca-2000-0003`](../exports/batches/software-seguranca-2000-0003.md) tem 1500/2.000 ([tranche 15](../exports/reports/ai-review-software-seguranca-2000-0003-tranche-15.md), [reconciliação da tranche 15](../exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-15.md) e [[MOC-Seguranca-Software-0009]]),",
                "- Os lotes atuais totalizam 5640 notas válidas pelo protocolo; o terceiro lote [`software-seguranca-2000-0003`](../exports/batches/software-seguranca-2000-0003.md) tem 1600/2.000 ([tranche 16](../exports/reports/ai-review-software-seguranca-2000-0003-tranche-16.md), [reconciliação da tranche 16](../exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-16.md) e [[MOC-Seguranca-Software-0009]]),",
            ),
        ],
    )
    print("reconciliação concluída")


if __name__ == "__main__":
    main()
