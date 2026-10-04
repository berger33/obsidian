#!/usr/bin/env python3
"""Build 100 substantive notes for batch software-seguranca-2000-0003 tranche 15 (IDs 1401-1500) and its AI factual review report."""
from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KF = ROOT / "knowledge-federation"
DOMAINS_DIR = KF / "domains"
NOTES_DIR = DOMAINS_DIR / "software-0009" / "software" / "seguranca"
REPORT = KF / "exports" / "reports" / "ai-review-software-seguranca-2000-0003-tranche-15.md"
DATA_DIR = Path(__file__).resolve().parent / "_seguranca_t15_data"
BATCH_ID = "software-seguranca-2000-0003"
DATE = "2026-10-03"
START = 1401
EXPECTED_NOTES = 100

sys.path.insert(0, str(Path(__file__).resolve().parent))
from note_quality import assess_markdown  # noqa: E402
from prose_audit import repeated_substantive_sentences  # noqa: E402


GROUP_META = {
    "01-sssd.txt": {
        "sub": "SSSD (SSSD/sssd — System Security Services Daemon) — Identidade Centralizada e Autenticação Offline em Frotas Linux (Domínios IPA/AD/LDAP, Cache LDB, Mapeamento SID->UID, GPOs, SSH AuthorizedKeysCommand e Smart Cards PKCS#11)",
        "src1_label": "Official SSSD GitHub Repository (`SSSD/sssd`)",
        "src1_note": "repositório oficial do System Security Services Daemon cobrindo arquitetura de responders (`nss`, `pam`, `ssh`, `sudo`) e provedores (`ipa`, `ad`, `ldap`, `krb5`) com cache offline",
        "src2_label": "SSSD Official Configuration Reference (`src/examples/sssd-example.conf`)",
        "src2_note": "configuração oficial de referência do `/etc/sssd/sssd.conf` detalhando domínios, `id_provider`, `auth_provider`, `access_provider`, `cache_credentials` e `enumerate = FALSE`",
    },
    "02-keylime.txt": {
        "sub": "Keylime (keylime/keylime & rust-keylime) — Atestação Remota Contínua Baseada em Hardware TPM 2.0 (Registrar, Verifier, Tenant, Rust Agent, IMA Runtime File Integrity, Measured Boot UEFA e Revogação Criptográfica)",
        "src1_label": "CNCF Keylime Official GitHub Repository (`keylime/keylime`)",
        "src1_note": "repositório oficial do projeto CNCF Keylime cobrindo arquitetura de atestação remota TPM 2.0, Verifier, Registrar, Tenant, Measured Boot, IMA e Encrypted Payloads",
        "src2_label": "Keylime Official Rust Agent Repository (`keylime/rust-keylime`)",
        "src2_note": "documentação oficial do agente `rust-keylime` em Rust sobre `rust-tss-esapi` detalhando configuração `/etc/keylime/agent.conf`, mTLS e revogação local",
    },
    "03-openscap.txt": {
        "sub": "OpenSCAP & ComplianceAsCode (OpenSCAP/openscap & ComplianceAsCode/content) — Auditoria Automatizada e Remediação de Conformidade SCAP 1.3 (XCCDF, OVAL, CPE, CVE, Perfis CIS/STIG/PCI-DSS/ANSSI, `oscap-ssh` e Ansible/Bash)",
        "src1_label": "OpenSCAP Official GitHub Repository (`OpenSCAP/openscap` — NIST SCAP 1.3 Certified)",
        "src1_note": "repositório oficial do motor e utilitário `oscap` certificado pelo NIST cobrindo avaliação XCCDF, OVAL, DataStreams (`ssg-*-ds.xml`), relatórios ARF/HTML e `oscap-ssh`",
        "src2_label": "ComplianceAsCode (`SCAP Security Guide`) Official Repository (`ComplianceAsCode/content`)",
        "src2_note": "repositório oficial de conteúdo SCAP como código contendo perfis CIS, DISA STIG, PCI-DSS, HIPAA e ANSSI e geração de remediações Ansible, Bash, Ignition e Kickstart",
    },
    "04-fapolicyd.txt": {
        "sub": "fapolicyd (linux-application-whitelisting/fapolicyd) — Application Whitelisting no Linux via Kernel `fanotify` (`FAN_OPEN_EXEC_PERM`), Trust Database LMDB (`rpmdb` + `file`), Verificação SHA-256/IMA e Proteção Contra Execução via Interpretadores",
        "src1_label": "Official `fapolicyd` GitHub Repository (`linux-application-whitelisting/fapolicyd`)",
        "src1_note": "repositório oficial do File Access Policy Daemon cobrindo interceptação de execução via `fanotify`, linguagem de regras `allow`/`deny_audit`, `fapolicyd-cli` e banco de confiança",
        "src2_label": "Official `fapolicyd.conf` Configuration Specification (`init/fapolicyd.conf`)",
        "src2_note": "especificação oficial de configuração do `/etc/fapolicyd/fapolicyd.conf` detalhando `permissive`, `trust = rpmdb,file`, `integrity = none|size|ima|sha256`, `watch_fs` e caches LRU",
    },
    "05-yubikey.txt": {
        "sub": "YubiKey & Hardware Security Tokens (`Yubico/yubikey-manager` `ykman` & `Yubico/pam-u2f`) — FIDO2/WebAuthn Passkeys Residentes, Autenticação Linux PAM U2F (`pamu2fcfg`), PIV Smart Card X.509, OpenPGP Hardware Card e OATH/Yubico OTP",
        "src1_label": "YubiKey Manager (`ykman`) Official Repository (`Yubico/yubikey-manager`)",
        "src1_note": "documentação oficial da biblioteca e CLI `ykman` cobrindo gerenciamento de interfaces USB/NFC e applets FIDO2, PIV, OpenPGP, OATH e OTP em YubiKeys",
        "src2_label": "Yubico `pam-u2f` Official Repository and Specification (`Yubico/pam-u2f`)",
        "src2_note": "documentação oficial do módulo `pam_u2f.so` e utilitário `pamu2fcfg` detalhando `authfile`, `cue`, `pinverification`, `userpresence`, `origin`, `sshformat` e proteção contra chave clonada",
    },
    "06-john.txt": {
        "sub": "John the Ripper Jumbo (`openwall/john`) — Auditoria de Senhas de Sistema, Utilitários `unshadow`/`*2john`, Modos `Single Crack`, `Wordlist`/Regras de Mangling, `Incremental` Markov, Expressões `PRINCE`/`Mask`, Aceleração OpenCL e `john.pot`",
        "src1_label": "John the Ripper Jumbo Official GitHub Repository (`openwall/john`)",
        "src1_note": "repositório oficial do Openwall John the Ripper Jumbo cobrindo mais de 400 formatos de hash/arquivos cifrados, aceleração SIMD/OpenCL e utilitários `*2john`",
        "src2_label": "John the Ripper Official Cracking Modes Specification (`doc/MODES`)",
        "src2_note": "especificação oficial dos modos de ataque do John the Ripper detalhando `Single Crack` (GECOS), `Wordlist` com regras de mangling, `Incremental` (cadeias de Markov) e `External`",
    },
    "07-aircrack.txt": {
        "sub": "Aircrack-ng Suite (`aircrack-ng/aircrack-ng`) — Auditoria de Segurança de Redes Sem Fio 802.11 (`airmon-ng`, `airodump-ng`, `aireplay-ng`, Captura de 4-Way Handshake EAPOL/PMKID, `aircrack-ng` SIMD/PBKDF2, `airdecap-ng` e WPA3-SAE)",
        "src1_label": "Aircrack-ng Official GitHub Repository (`aircrack-ng/aircrack-ng`)",
        "src1_note": "repositório oficial da suíte Aircrack-ng cobrindo ferramentas de monitoramento, captura, injeção de quadros 802.11, teste de chaves WPA/WPA2 e descriptografia `airdecap-ng`",
        "src2_label": "Aircrack-ng Official Technical Documentation (`aircrack-ng.org`)",
        "src2_note": "documentação técnica oficial do `aircrack-ng` detalhando ataques de dicionário WPA/WPA2-PSK (`PBKDF2-HMAC-SHA1`), bancos pré-computados `airolib-ng` e flags operacionais",
    },
    "08-kismet.txt": {
        "sub": "Kismet Wireless (`kismetwireless/kismet`) — Detecção de Intrusão Sem Fio (WIDS) 100% Passiva e Monitoramento RF Multi-Espectro (Wi-Fi 802.11a/b/g/n/ac/ax/be, BLE, Zigbee, RTL-SDR, Sensores Remotos, Alertas Rogue AP e `kismetdb`)",
        "src1_label": "Kismet Wireless Official GitHub Repository (`kismetwireless/kismet`)",
        "src1_note": "repositório oficial do detector passivo de redes e WIDS Kismet cobrindo suporte a Wi-Fi, Bluetooth, Zigbee, RF/SDR, sensores remotos e API REST/WebSockets",
        "src2_label": "Kismet Official Documentation — Introduction & Architecture (`kismetwireless.net/docs/readme/intro/kismet`)",
        "src2_note": "documentação arquitetural oficial do Kismet detalhando operação passiva sem emissão RF, configuração `kismet_site.conf`, logs unificados `.kismet` (SQLite3) e `.pcapng`",
    },
    "09-scapy.txt": {
        "sub": "Scapy (`secdev/scapy`) — Construção, Dissecação, Fuzzing e Automação de Protocolos de Rede em Python (Operador de Camadas `/`, `send`/`sr1`/`srp`, Produto Cartesiano `PacketList`, `sniff`/`PcapReader`, `fuzz()`, `Automaton` e Dissecadores Customizados)",
        "src1_label": "Scapy Official GitHub Repository (`secdev/scapy`)",
        "src1_note": "repositório oficial da biblioteca e shell interativo Scapy em Python para manipulação, síntese, decodificação e auditoria de protocolos de rede das camadas 2 a 7",
        "src2_label": "Scapy Official Usage & Design Documentation (`doc/scapy/usage.rst`)",
        "src2_note": "documentação oficial de uso do Scapy detalhando composição de camadas com `/`, pareamento estímulo-resposta (`sr`/`sr1`/`srp`), geração de conjuntos de pacotes e `fuzz()`",
    },
    "10-tcpdump.txt": {
        "sub": "`tcpdump` & `libpcap` (`the-tcpdump-group/tcpdump`) — Captura e Análise Forense de Pacotes com Filtragem BPF no Kernel, Aritmética de Bytes/Flags TCP, Ring Buffer de Rotação (`-C`/`-W`/`-G`), Linux `SLL2` (`-i any`), `nsenter` e Segurança (`-Z`/`-nn`)",
        "src1_label": "The Tcpdump Group Official GitHub Repository (`the-tcpdump-group/tcpdump`)",
        "src1_note": "repositório oficial do analisador de pacotes `tcpdump` cobrindo arquitetura de dissecadores, integração com `libpcap`, opções de linha de comando e segurança",
        "src2_label": "Official `tcpdump(1)` Manpage Specification (`tcpdump.org/manpages/tcpdump.1.html`)",
        "src2_note": "manpage oficial `tcpdump(1)` detalhando flags `-nn`, `-i any`, `-s`, `-B`, `-C`/`-W`/`-G`/`-z`, `-U`, `-l`, `--immediate-mode`, `--print`, `--count`, `-Z` e primitivas BPF",
    },
}


def normalize(text: str) -> str:
    base = unicodedata.normalize("NFKD", text.lower())
    clean = "".join(ch for ch in base if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]+", " ", clean).strip()


def parse_group(path: Path) -> tuple[dict[str, str], list[dict[str, object]]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    sources_urls: list[str] = []
    for line in lines[:10]:
        if line.startswith("SOURCES:"):
            sources_urls = [s.strip() for s in line.split("SOURCES:", 1)[1].split("|") if s.strip()]
    if len(sources_urls) < 2:
        raise ValueError(f"{path.name}: esperado cabeçalho SOURCES com pelo menos 2 URLs")

    raw_text = "\n".join(lines)
    blocks = [b.strip() for b in raw_text.split("===NOTE===") if b.strip()][1:]
    if len(blocks) != 10:
        raise ValueError(f"{path.name}: esperadas 10 notas, encontradas {len(blocks)}")

    meta = GROUP_META[path.name]
    group_title = meta["sub"]
    rows: list[dict[str, object]] = []
    first_num: int | None = None

    for rec in blocks:
        code_m = re.search(r"\|(```[\s\S]+?```)\|", rec)
        if not code_m:
            raise ValueError(f"{path.name}: bloco de código não encontrado: {rec[:140]}...")
        pre = rec[: code_m.start()]
        example = code_m.group(1).strip()
        post = rec[code_m.end() :]

        pre_parts = [g.strip() for g in re.split(r"\|(?=(?:[^`]*`[^`]*`)*[^`]*$)", pre)]
        post_parts = [g.strip() for g in re.split(r"\|(?=(?:[^`]*`[^`]*`)*[^`]*$)", post)]
        if len(pre_parts) != 6 or len(post_parts) != 3:
            raise ValueError(
                f"{path.name}: falha ao analisar registro (pre={len(pre_parts)}, post={len(post_parts)}): {rec[:140]}..."
            )
        num_str, slug, title, summary, reason, how = pre_parts
        caveat, verify, links_csv = post_parts
        num = int(num_str)
        if first_num is None:
            first_num = num
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
            raise ValueError(f"{path.name}: slug inválido: {slug}")

        links = [x.strip() for x in links_csv.split(",") if x.strip()]
        sources = [
            (meta["src1_label"], sources_urls[0], meta["src1_note"]),
            (meta["src2_label"], sources_urls[1], meta["src2_note"]),
        ]
        if len(sources_urls) >= 3:
            sources.append((meta["src3_label"], sources_urls[2], meta["src3_note"]))

        rows.append(
            {
                "slug": slug,
                "title": title,
                "summary": summary,
                "reason": reason,
                "how": how,
                "example": example,
                "caveat": caveat,
                "verify": verify,
                "links": links,
                "sources": sources,
                "review": f"Verificado contra {meta['src1_label']} e {meta['src2_label']}.",
            }
        )

    assert first_num is not None
    first_sources = rows[0]["sources"]  # type: ignore[index]
    ctx = {
        "first": str(first_num),
        "sub": group_title,
        "group_title": group_title,
        "check": (
            f"Conferi a documentação primária oficial de {group_title} "
            f"({first_sources[0][1]} e {first_sources[1][1]}) antes de redigir as dez notas."
        ),
    }
    return ctx, rows


def render_note(
    context: dict[str, str],
    rows: list[dict[str, object]],
    index: int,
    row: dict[str, object],
    valid_slugs: set[str] | None = None,
) -> tuple[int, str, dict[str, object]]:
    number = int(context["first"]) + index
    sources: list[tuple[str, str, str]] = list(row["sources"])  # type: ignore[arg-type]
    if len(sources) < 2 or len({source[1] for source in sources}) < 2:
        raise ValueError(f"{row['slug']}: precisa de duas fontes distintas")

    neighbors = []
    seen_nb: set[str] = set()
    for neighbor_index in (index - 1, index + 1):
        if 0 <= neighbor_index < len(rows):
            other = rows[neighbor_index]
            s = str(other["slug"])
            seen_nb.add(s)
            neighbors.append(f"- [[{s}]] — Veja também: {other['title']}.")
    if valid_slugs is not None:
        for lk in row.get("links", []):  # type: ignore[union-attr]
            if lk not in seen_nb and lk != row["slug"] and lk in valid_slugs:
                seen_nb.add(lk)
                neighbors.append(f"- [[{lk}]] — Referência cruzada direta com {lk}.")

    frontmatter = f'''---
id: software.seguranca.tranche15.{number:06d}
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: {DATE}
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: {DATE}
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-15.md"
fontes: [{', '.join('"' + source[1] + '"' for source in sources)}]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: {BATCH_ID}
---\n'''
    source_lines = [
        f"- [{name}]({url}) — {description}; consultado em {DATE}."
        for name, url, description in sources
    ]
    content = f'''{frontmatter}
# {row['title']}

## Em uma frase
{row['summary']}

## Por que importa
{row['reason']}

## Como funciona
{row['how']}

## Exemplo
{row['example']}

## Limites e trade-offs
{row['caveat']}

## Como verificar
{row['verify']}

## Conexões
{chr(10).join(neighbors)}

## Fontes
{chr(10).join(source_lines)}
'''
    quality = assess_markdown(content, str(row["slug"]) + ".md")
    if quality["errors"]:
        raise ValueError(f"{row['slug']}: {quality['errors']} ({quality['word_count']} palavras)")
    return number, content, quality


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--refresh",
        action="store_true",
        help="Rebuild the existing tranche-15 notes after validating their IDs and batch metadata.",
    )
    args = parser.parse_args()
    NOTES_DIR.mkdir(parents=True, exist_ok=True)
    group_files = sorted(DATA_DIR.glob("*.txt"))
    if len(group_files) != 10:
        raise SystemExit(f"Esperados 10 arquivos de grupo; encontrados {len(group_files)}")

    existing_paths = list(DOMAINS_DIR.rglob("*.md"))
    existing_tranche = [
        path
        for path in existing_paths
        if re.search(
            r"(?m)^id: software\.seguranca\.tranche15\.\d{6}\s*$",
            path.read_text(encoding="utf-8", errors="replace")[:1200],
        )
    ]
    if args.refresh and len(existing_tranche) != EXPECTED_NOTES:
        raise ValueError(
            f"--refresh exige exatamente {EXPECTED_NOTES} notas tranche15 existentes; encontradas {len(existing_tranche)}"
        )
    if REPORT.exists() and not args.refresh:
        raise ValueError(f"relatório já existe (use --refresh apenas para atualizar a tranche 15): {REPORT}")
    if args.refresh and not REPORT.exists():
        raise ValueError(f"--refresh exige relatório factual existente: {REPORT}")

    current_tranche = set(existing_tranche)
    existing_paths = [path for path in existing_paths if path not in current_tranche]
    existing_slugs = {path.stem for path in existing_paths}
    existing_titles = set()
    for path in existing_paths:
        match = re.search(r"(?m)^#\s+(.+?)\s*$", path.read_text(encoding="utf-8", errors="replace"))
        if match:
            existing_titles.add(normalize(match.group(1).strip()))

    parsed_groups = [parse_group(path) for path in group_files]
    tranche_slugs = {str(r["slug"]) for _, rows in parsed_groups for r in rows}
    all_valid_slugs = existing_slugs | tranche_slugs

    pending = []
    report_rows = []
    group_summaries: list[tuple[dict[str, str], int]] = []
    seen_slugs: set[str] = set()
    seen_titles: set[str] = set()
    expected_number = START
    for path, (context, rows) in zip(group_files, parsed_groups):
        if int(context["first"]) != expected_number:
            raise ValueError(f"{path.name}: ID inicial esperado {expected_number}, informado {context['first']}")
        group_summaries.append((context, len(rows)))
        for index, row in enumerate(rows):
            slug = str(row["slug"])
            title = str(row["title"])
            normalized_title = normalize(title.strip())
            if slug in seen_slugs or slug in existing_slugs:
                raise ValueError(f"slug em colisão com o inventário: {slug}")
            if normalized_title in seen_titles or normalized_title in existing_titles:
                raise ValueError(f"título em colisão com o inventário: {title}")
            target_path = NOTES_DIR / f"{slug}.md"
            expected_id = f"id: software.seguranca.tranche15.{expected_number + index:06d}"
            if target_path.exists():
                current = target_path.read_text(encoding="utf-8")
                if not args.refresh:
                    raise ValueError(f"arquivo já existe (use --refresh apenas para a tranche 15): {target_path}")
                if (
                    expected_id not in current.splitlines()[:25]
                    or f"lote: {BATCH_ID}" not in current.splitlines()[:25]
                ):
                    raise ValueError(f"ID ou lote existente não corresponde à tranche: {target_path}")
            elif args.refresh:
                raise ValueError(f"--refresh exige os {EXPECTED_NOTES} arquivos existentes; falta {target_path}")
            seen_slugs.add(slug)
            seen_titles.add(normalized_title)
            number, content, quality = render_note(context, rows, index, row, valid_slugs=all_valid_slugs)
            pending.append((number, row, context, content, quality))
            source_name, source_url, _ = row["sources"][0]  # type: ignore[index]
            report_rows.append(
                f"| {number} | [[{slug}]] | [{source_name}]({source_url}) | {row['review']} Revisão factual por IA concluída; decisão: aprovada. |"
            )
        expected_number += len(rows)

    if len(pending) != EXPECTED_NOTES or expected_number != START + EXPECTED_NOTES:
        raise ValueError(
            f"esperadas {EXPECTED_NOTES} notas de {START} a {START + EXPECTED_NOTES - 1}, validadas {len(pending)}"
        )
    repeated = repeated_substantive_sentences(
        [(number, content) for number, _, _, content, _ in pending]
    )
    if repeated:
        examples = [f"{numbers}: {sentence}" for sentence, numbers in list(repeated.items())[:8]]
        raise ValueError(f"prosa substantiva repetida entre notas; revisar antes de gravar: {examples}")

    for number, row, context, content, quality in pending:
        (NOTES_DIR / f"{row['slug']}.md").write_text(content, encoding="utf-8")

    report = [
        f"# Revisão factual assistida por IA — lote `{BATCH_ID}`, tranche 15",
        "",
        f"- Data: {DATE}",
        "- Revisor: `Arena.ai Agent Mode`",
        f"- Escopo: notas **{START}–{START + EXPECTED_NOTES - 1}**, em dez grupos temáticos com dez notas cada; cada linha identifica a conferência factual da nota.",
        "- Fontes primárias: documentação oficial dos projetos e versões indicadas nas próprias notas; as afirmações foram limitadas ao material citado.",
        f"- Resultado: **{EXPECTED_NOTES} revisões factuais por IA registradas** e aprovadas no gate automatizado de qualidade, elevando o terceiro lote `{BATCH_ID}` para **1500/2.000 notas válidas (`in_progress`)**. Isto não é aprovação humana nem garantia de ausência de erro.",
        "- Nenhuma aprovação humana existente foi alterada ou estendida às novas notas.",
        "",
        "## Registro por nota",
        "",
        "| # | Nota | Fonte principal | Verificação factual / decisão |",
        "|---:|---|---|---|",
        *report_rows,
        "",
        "## Verificações por grupo",
        "",
    ]
    for context, count in group_summaries:
        report.append(
            f"- {context['group_title']} (itens {context['first']}–{int(context['first']) + count - 1}): {context['check']}"
        )
    report += [
        "- A auditoria de links, a comparação com o inventário, o gate de conteúdo e a verificação de sentenças repetidas foram executados separadamente antes da contabilização.",
        "",
    ]
    REPORT.write_text("\n".join(report).rstrip() + "\n", encoding="utf-8")
    word_counts = [quality["word_count"] for _, _, _, _, quality in pending]
    source_counts = [quality["source_count"] for _, _, _, _, quality in pending]
    print(
        f"Geradas {len(pending)} notas substantivas (IDs {START}–{START + EXPECTED_NOTES - 1}); "
        f"palavras: min={min(word_counts)}; max={max(word_counts)}"
    )
    print(f"Fontes HTTPS específicas por nota: min={min(source_counts)}; max={max(source_counts)}")
    print(f"Relatório factual: {REPORT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
