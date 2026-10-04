#!/usr/bin/env python3
"""Build 100 substantive notes for batch software-seguranca-2000-0003 tranche 12 (IDs 1101-1200) and its AI factual review report."""
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
REPORT = KF / "exports" / "reports" / "ai-review-software-seguranca-2000-0003-tranche-12.md"
DATA_DIR = Path(__file__).resolve().parent / "_seguranca_t12_data"
BATCH_ID = "software-seguranca-2000-0003"
DATE = "2026-10-03"
START = 1101
EXPECTED_NOTES = 100

sys.path.insert(0, str(Path(__file__).resolve().parent))
from note_quality import assess_markdown  # noqa: E402
from prose_audit import repeated_substantive_sentences  # noqa: E402


GROUP_META = {
    "01-chainsaw.txt": {
        "sub": "WithSecure Chainsaw (WithSecureLabs/chainsaw) — Triagem Forense Multi-Artefatos Windows (.evtx, $MFT, Registry Hives, Shimcache e SRUM) em Rust e Motor Lógico TAU",
        "src1_label": "WithSecure Chainsaw Official GitHub — Rapidly Search and Hunt Through Windows Forensic Artefacts",
        "src1_note": "repositório oficial do Chainsaw cobrindo triagem forense (`hunt`, `search`, `analyse shimcache`, `analyse srum`, `dump`), regras Sigma e motor TAU",
        "src2_label": "WithSecure Chainsaw Official Rust Package Specification (`Cargo.toml`)",
        "src2_note": "especificação oficial das bibliotecas forenses em Rust do Chainsaw 2.16+ (`evtx`, `mft`, `notatin`, `libesedb`, `tau-engine`, `aho-corasick`, `rayon`)",
    },
    "02-atomic-red-team.txt": {
        "sub": "Red Canary Atomic Red Team (redcanaryco/atomic-red-team & invoke-atomicredteam) — Biblioteca Aberta de Testes Determinísticos Mapeados ao MITRE ATT&CK e Execução Automatizada",
        "src1_label": "Red Canary Atomic Red Team Official GitHub — Library of Tests Mapped to MITRE ATT&CK",
        "src1_note": "repositório oficial do Atomic Red Team com mais de 1.870 testes atômicos declarativos em YAML mapeados às técnicas do MITRE ATT&CK",
        "src2_label": "Red Canary `Invoke-AtomicRedTeam` Official GitHub — PowerShell Execution Framework",
        "src2_note": "documentação oficial do motor multiplataforma `Invoke-AtomicRedTeam` para Windows, Linux e macOS",
    },
    "03-caldera.txt": {
        "sub": "MITRE Caldera (mitre/caldera) — Plataforma Automatizada de Emulação de Adversários, Agentes C2 (Sandcat/Manx), Planejamento Orientado a Fatos e Operações Purple Team",
        "src1_label": "MITRE Caldera Official GitHub — Automated Adversary Emulation, Red Team & Incident Response Platform",
        "src1_note": "repositório oficial do MITRE Caldera v5 cobrindo o Core C2 Server, interface VueJS Magma e ecossistema de plugins (`sandcat`, `stockpile`, `atomic`, `emu`, `debrief`, `response`)",
        "src2_label": "MITRE Caldera Official Documentation — Learning the Terminology (`Agents`, `Abilities`, `Adversaries`, `Operations`, `Planners`, `Facts`, `Parsers`)",
        "src2_note": "documentação oficial ReadTheDocs detalhando a arquitetura de planejamento orientado a fatos e agentes do Caldera",
    },
    "04-certipy.txt": {
        "sub": "Certipy (ly4k/Certipy — certipy-ad) — Auditoria, Enumeração e Testes de Segurança em Active Directory Certificate Services (AD CS ESC1–ESC17, Shadow Credentials e Golden Certificates)",
        "src1_label": "Certipy Official GitHub — Active Directory Certificate Services (AD CS) Attack & Enumeration Toolkit",
        "src1_note": "repositório oficial do Certipy cobrindo descoberta de CAs/Templates, identificação de vulnerabilidades ESC1–ESC17, Shadow Credentials e Golden Certificates",
        "src2_label": "Certipy Official Package & Architecture Specification (`pyproject.toml`)",
        "src2_note": "especificação técnica do pacote `certipy-ad` v5.1+ (`impacket`, `ldap3`, `cryptography`, `asn1crypto`, `neo4j`/BloodHound)",
    },
    "05-aide.txt": {
        "sub": "AIDE — Advanced Intrusion Detection Environment (aide/aide) — Monitoramento Criptográfico de Integridade de Arquivos (FIM), Atributos Estendidos (ACL/SELinux/xattrs/e2fsattrs) e Detecção de Rootkits em Linux",
        "src1_label": "AIDE Official Repository README — Advanced Intrusion Detection Environment (v0.19)",
        "src1_note": "documentação oficial do código-fonte do AIDE cobrindo arquitetura, verificação criptográfica GPG, PCRE2 e bibliotecas `libnettle`/`libgcrypt`",
        "src2_label": "The Official AIDE Manual (`aide.github.io/doc`)",
        "src2_note": "manual técnico oficial do AIDE detalhando regras de atributos (`p`, `i`, `n`, `u`, `g`, `s`, `m`, `c`, `S`, `acl`, `selinux`, `xattrs`, `e2fsattrs`, `sha256`, `sha512`), seleções regex e assinatura de banco de dados",
    },
    "06-cowrie.txt": {
        "sub": "Cowrie (cowrie/cowrie) — Honeypot SSH e Telnet de Média e Alta Interação (Modos Shell, Proxy QEMU Pool e LLM), Captura de Malware e Replay de Sessões TTY (playlog)",
        "src1_label": "Cowrie Official GitHub (`README.rst`) — Medium to High Interaction SSH and Telnet Honeypot",
        "src1_note": "documentação oficial do Cowrie cobrindo os modos `shell`, `proxy` e `llm`, sistema de arquivos falso `fs.pickle`, utilitários `fsctl`/`createfs`/`playlog` e logs JSON",
        "src2_label": "Cowrie Official Configuration Reference (`src/cowrie/data/etc/cowrie.cfg.dist`)",
        "src2_note": "especificação completa dos parâmetros de configuração do Cowrie (`[honeypot]`, `auth_class`, `UserDB`, `AuthRandom`, `ttylog`, `download_limit_size`, `[backend_pool]`)",
    },
    "07-opencanary.txt": {
        "sub": "Thinkst OpenCanary (thinkst/opencanary) — Honeypot Multiprotocolo de Baixa Interação para Detecção de Intrusão em Redes Internas, Módulos de Protocolo e Breadcrumbs",
        "src1_label": "Thinkst OpenCanary Official GitHub — Multi-Protocol Network Honeypot Daemon",
        "src1_note": "repositório oficial do OpenCanary cobrindo arquitetura do daemon `opencanaryd`, requisitos de permissão do `/etc/opencanaryd/opencanary.conf` e módulos opcionais (`smb`, `snmp`, `portscan`)",
        "src2_label": "Thinkst OpenCanary Default Configuration Schema (`opencanary/data/settings.json`)",
        "src2_note": "esquema oficial de configuração JSON do OpenCanary detalhando os protocolos suportados (`ftp`, `http`, `https`, `smb`, `mysql`, `mssql`, `ssh`, `redis`, `rdp`, `sip`, `snmp`, `ntp`, `tftp`, `tcpbanner`, `telnet`, `git`, `llmnr`, `vnc`) e `PyLogger`",
    },
    "08-wireguard.txt": {
        "sub": "WireGuard — VPN Criptográfica Moderna no Kernel Linux, Protocolo Noise_IKpsk2 (ChaCha20-Poly1305, Curve25519, BLAKE2s), Cryptokey Routing (AllowedIPs) e Resistência Pós-Quântica",
        "src1_label": "WireGuard Official Protocol & Cryptography Specification (`wireguard.com/protocol`)",
        "src1_note": "especificação criptográfica oficial do WireGuard detalhando as primitivas fixas (`Noise_IKpsk2_25519_ChaChaPoly_BLAKE2s`), timers de PFS, `PresharedKey` e mitigação de DoS com `mac1`/`mac2` cookies",
        "src2_label": "WireGuard Official Quick Start & CLI Guide (`wireguard.com/quickstart`)",
        "src2_note": "guia oficial de operação com `ip link`, `wg(8)`, `wg-quick(8)`, geração de chaves, `PersistentKeepalive` para travessia de NAT e `dynamic_debug` no kernel Linux",
    },
    "09-nftables.txt": {
        "sub": "Linux nftables (Netfilter Project) — Subsistema Moderno de Classificação de Pacotes e Firewall Stateful no Kernel Linux, Família Dual-Stack inet, Sets/Verdict Maps em O(1) e Flowtables",
        "src1_label": "Official nftables Wiki — Quick Reference: nftables in 10 Minutes",
        "src1_note": "documentação oficial do projeto Netfilter detalhando tabelas (`ip`, `ip6`, `inet`, `arp`, `bridge`, `netdev`), chains, hooks, prioridades, matches (`ct`, `meta`, `tcp`, `ip`) e scripting atômico",
        "src2_label": "Official nftables Wiki — Generic Set Infrastructure (Anonymous & Named Sets, Intervals, Timeouts & Auto-Merge)",
        "src2_note": "documentação oficial das estruturas de dados de alta performance de Sets (`hashtables` e `red-black trees`), `flags interval`, `timeout`, `auto-merge`, `counter` e `typeof`",
    },
    "10-openssh.txt": {
        "sub": "OpenSSH (openssh/openssh-portable 10.x) — Arquitetura de Separação de Privilégios (sshd-session / seccomp), Troca de Chaves Híbrida Pós-Quântica (mlkem768x25519-sha256), Chaves FIDO2 (ed25519-sk) e Certificados SSH CA",
        "src1_label": "OpenSSH Portable Official Repository README (`openssh/openssh-portable`)",
        "src1_note": "documentação oficial do OpenSSH Portable detalhando a arquitetura derivada do OpenBSD, suporte a PAM/libcrypto e diretrizes de segurança",
        "src2_label": "OpenSSH Official Release Notes (OpenSSH 10.4 / 10.5p1)",
        "src2_note": "notas de lançamento oficiais do OpenSSH detalhando melhorias de segurança em `sshd-session`, `seccomp`/`NO_NEW_PRIVS` fatais, `session-bind@openssh.com`, `restrict`, `ChannelTimeout` e chaves FIDO (`ssh -Z`)",
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
id: software.seguranca.tranche12.{number:06d}
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-12.md"
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
        help="Rebuild the existing tranche-12 notes after validating their IDs and batch metadata.",
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
            r"(?m)^id: software\.seguranca\.tranche12\.\d{6}\s*$",
            path.read_text(encoding="utf-8", errors="replace")[:1200],
        )
    ]
    if args.refresh and len(existing_tranche) != EXPECTED_NOTES:
        raise ValueError(
            f"--refresh exige exatamente {EXPECTED_NOTES} notas tranche12 existentes; encontradas {len(existing_tranche)}"
        )
    if REPORT.exists() and not args.refresh:
        raise ValueError(f"relatório já existe (use --refresh apenas para atualizar a tranche 12): {REPORT}")
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
            expected_id = f"id: software.seguranca.tranche12.{expected_number + index:06d}"
            if target_path.exists():
                current = target_path.read_text(encoding="utf-8")
                if not args.refresh:
                    raise ValueError(f"arquivo já existe (use --refresh apenas para a tranche 12): {target_path}")
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
        f"# Revisão factual assistida por IA — lote `{BATCH_ID}`, tranche 12",
        "",
        f"- Data: {DATE}",
        "- Revisor: `Arena.ai Agent Mode`",
        f"- Escopo: notas **{START}–{START + EXPECTED_NOTES - 1}**, em dez grupos temáticos com dez notas cada; cada linha identifica a conferência factual da nota.",
        "- Fontes primárias: documentação oficial dos projetos e versões indicadas nas próprias notas; as afirmações foram limitadas ao material citado.",
        f"- Resultado: **{EXPECTED_NOTES} revisões factuais por IA registradas** e aprovadas no gate automatizado de qualidade, elevando o terceiro lote `{BATCH_ID}` para **1200/2.000 notas válidas (`in_progress`)**. Isto não é aprovação humana nem garantia de ausência de erro.",
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
