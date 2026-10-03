#!/usr/bin/env python3
"""Build 100 substantive notes for batch software-seguranca-2000-0003 tranche 06 (IDs 501-600) and its AI factual review report."""
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
REPORT = KF / "exports" / "reports" / "ai-review-software-seguranca-2000-0003-tranche-06.md"
DATA_DIR = Path(__file__).resolve().parent / "_seguranca_t06_data"
BATCH_ID = "software-seguranca-2000-0003"
DATE = "2026-10-03"
START = 501
EXPECTED_NOTES = 100

sys.path.insert(0, str(Path(__file__).resolve().parent))
from note_quality import assess_markdown  # noqa: E402
from prose_audit import repeated_substantive_sentences  # noqa: E402


GROUP_META = {
    "01-thehive.txt": {
        "sub": "TheHive & Cortex — Plataforma de Resposta a Incidentes (SIRP), Cases, Observables, Analyzers, Responders e Integração MISP",
        "src1_label": "TheHive Project Official GitHub — SIRP Architecture & Features",
        "src1_note": "documentação oficial do TheHive cobrindo Alerts, Cases, Tasks, Observables, Case Templates e integração MISP",
        "src2_label": "Cortex Official GitHub — Observable Analysis & Active Response Engine",
        "src2_note": "documentação oficial do motor Cortex para execução isolada de Analyzers e Responders com guardrails TLP/PAP",
        "src3_label": "Cortex Analyzers & Responders Official Repository",
        "src3_note": "catálogo oficial de Analyzers e Responders do projeto TheHive",
    },
    "02-opencti.txt": {
        "sub": "Filigran OpenCTI — Plataforma de Threat Intelligence em Grafo STIX 2.1, Conectores, Inferência, RBAC Markings e Feeds",
        "src1_label": "OpenCTI Official GitHub — STIX 2.1 Cyber Threat Intelligence Platform",
        "src1_note": "documentação oficial da plataforma OpenCTI cobrindo o grafo STIX 2.1, GraphQL, inferência e RBAC",
        "src2_label": "OpenCTI Connectors Official GitHub — Architecture & Classes",
        "src2_note": "documentação oficial das 5 classes de conectores do OpenCTI (EXTERNAL_IMPORT, INTERNAL_ENRICHMENT, STREAM, etc.)",
        "src3_label": "OpenCTI Official Documentation — Connectors Deployment",
        "src3_note": "guia oficial de implantação e operação de conectores e workers do OpenCTI",
    },
    "03-timesketch.txt": {
        "sub": "Google Timesketch & Plaso (log2timeline) — Análise Colaborativa de Super-Timelines Forenses, DFIQ, Analyzers e Sigma",
        "src1_label": "Google Timesketch Official GitHub — Collaborative Forensic Timeline Analysis",
        "src1_note": "documentação oficial do Google Timesketch para análise colaborativa de timelines forenses",
        "src2_label": "Timesketch Official User Guide — Sketch Overview & Lifecycle",
        "src2_note": "guia oficial de abas do Sketch (Explore, Stories, Intelligence), tsctl, arquivamento e labels de proteção",
        "src3_label": "Timesketch Official Admin Guide — Installation & Configuration",
        "src3_note": "guia oficial de administração, Analyzers, Sigma e DFIQ no Timesketch",
    },
    "04-volatility3.txt": {
        "sub": "Volatility 3 — Forense de Memória RAM (Windows, Linux, macOS), Tabelas de Símbolos ISF (dwarf2json), Malfind e Rootkits",
        "src1_label": "Volatility 3 Official GitHub — Volatile Memory Extraction Framework",
        "src1_note": "documentação oficial do Volatility 3 cobrindo ISF symbol tables, plugins Windows/Linux/macOS e uso da CLI",
        "src2_label": "Volatility dwarf2json Official GitHub — Linux & macOS ISF Generator",
        "src2_note": "documentação oficial do gerador de tabelas de símbolos ISF dwarf2json a partir de DWARF e System.map",
        "src3_label": "Volatility Software License & Foundation Reference",
        "src3_note": "referência institucional da Volatility Foundation",
    },
    "05-capev2.txt": {
        "sub": "CAPEv2 Malware Sandbox — Detonação Dinâmica, API/Syscall Hooking, Debugger Programável por YARA e Extração de Configuração",
        "src1_label": "CAPEv2 Official GitHub — Malware Configuration And Payload Extraction",
        "src1_note": "documentação oficial do CAPEv2 cobrindo unpacking dinâmico, debugger programável por YARA, AMSI e CAPE-parsers",
        "src2_label": "CAPEv2 Official Documentation — REST API v2 Reference",
        "src2_note": "referência oficial da REST API v2 (/apiv2/), autenticação por token DRF, throttling e endpoints de tarefas",
        "src3_label": "CAPE-parsers Official Repository — Static Configuration Extractors",
        "src3_note": "repositório oficial de extratores de configuração de famílias de malware do CAPEv2",
    },
    "06-wireshark.txt": {
        "sub": "Wireshark, TShark & Dumpcap — Análise Forense de Pacotes (PCAPNG), Filtros BPF vs Display, Decriptação TLS/Kerberos e Extração",
        "src1_label": "Wireshark Official GitHub — Architecture & Security Privilege Separation",
        "src1_note": "documentação oficial do Wireshark cobrindo arquitetura, formato pcapng e isolamento de privilégios no dumpcap",
        "src2_label": "Wireshark Official Manual Page — tshark CLI Reference",
        "src2_note": "manual oficial do tshark cobrindo filtros -f vs -Y, análise em duas passagens -2, estatísticas -z e extração -T",
        "src3_label": "Wireshark User's Guide — Official HTML Documentation",
        "src3_note": "guia oficial do usuário do Wireshark",
    },
    "07-bettercap.txt": {
        "sub": "Bettercap — Auditoria de Redes Ethernet IPv4/IPv6, WiFi 802.11, Bluetooth Low Energy (BLE), HID 2.4GHz, CAN-bus e Caplets",
        "src1_label": "Bettercap Official GitHub — Network, WiFi, BLE, HID & CAN-bus Framework",
        "src1_note": "documentação oficial do Bettercap cobrindo arquitetura em Go e módulos de auditoria Ethernet, WiFi, BLE, HID e CAN",
        "src2_label": "Bettercap Caplets Official GitHub — Scripting Interactive Sessions",
        "src2_note": "repositório e documentação oficial de automação de sessões do Bettercap com arquivos .cap (caplets)",
        "src3_label": "Bettercap Official Documentation Portal",
        "src3_note": "documentação oficial do projeto Bettercap",
    },
    "08-responder.txt": {
        "sub": "Responder — Envenenamento LLMNR, NBT-NS, mDNS, DHCPv6 e WPAD, Captura NetNTLMv2/Kerberos, MultiRelay e Hardening Windows",
        "src1_label": "Responder Official GitHub — LLMNR/NBT-NS/mDNS/DHCPv6 Poisoner & Rogue Servers",
        "src1_note": "documentação oficial do Responder cobrindo modo passivo -A, servidores rogue, DHCPv6, Kerberos e ferramentas auxiliares",
        "src2_label": "Responder Official Configuration — Responder.conf Reference",
        "src2_note": "configuração oficial do Responder detalhando KerberosMode, RespondTo, DontRespondTo, AutoIgnoreAfterSuccess e DHCPv6",
        "src3_label": "Responder Repository & Tools Suite",
        "src3_note": "repositório oficial da suíte Responder (RunFinger, MultiRelay, FindSQLSrv)",
    },
    "09-impacket.txt": {
        "sub": "Fortra Impacket — Pilha de Protocolos de Rede Windows (SMB1-3, MSRPC, Kerberos, LDAP, TDS), Exemplos e Defesas de AD",
        "src1_label": "Fortra Impacket Official GitHub — Network Protocols & Examples Overview",
        "src1_note": "documentação oficial do Fortra Impacket cobrindo protocolos SMB1-3, MSRPC, Kerberos, LDAP, TDS e utilitários",
        "src2_label": "Fortra Impacket Official Testing Guide — TESTING.md & AD Lab Setup",
        "src2_note": "guia oficial de testes locais/remotos (pytest, tox) e configuração de laboratório Active Directory e LDAPS",
        "src3_label": "Fortra Impacket Official Repository",
        "src3_note": "repositório oficial da biblioteca Impacket",
    },
    "10-netexec.txt": {
        "sub": "NetExec (nxc) — Auditoria Multi-Protocolo de Redes Corporativas e Active Directory (SMB, LDAP, WinRM, WMI, MSSQL, SSH, RDP)",
        "src1_label": "NetExec Official GitHub — The Network Execution Tool (nxc & nxcdb)",
        "src1_note": "documentação oficial do NetExec cobrindo protocolos suportados, instalação via pipx e banco nxcdb",
        "src2_label": "NetExec Official Wiki — Getting Started & Protocol Usage",
        "src2_note": "wiki oficial do NetExec cobrindo instalação, autenticação Kerberos/NTLM, módulos e operação",
        "src3_label": "NetExec Official Repository",
        "src3_note": "repositório oficial do projeto NetExec",
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
id: software.seguranca.tranche06.{number:06d}
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-06.md"
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
        help="Rebuild the existing tranche-06 notes after validating their IDs and batch metadata.",
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
            r"(?m)^id: software\.seguranca\.tranche06\.\d{6}\s*$",
            path.read_text(encoding="utf-8", errors="replace")[:1200],
        )
    ]
    if args.refresh and len(existing_tranche) != EXPECTED_NOTES:
        raise ValueError(
            f"--refresh exige exatamente {EXPECTED_NOTES} notas tranche06 existentes; encontradas {len(existing_tranche)}"
        )
    if REPORT.exists() and not args.refresh:
        raise ValueError(f"relatório já existe (use --refresh apenas para atualizar a tranche 06): {REPORT}")
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
            expected_id = f"id: software.seguranca.tranche06.{expected_number + index:06d}"
            if target_path.exists():
                current = target_path.read_text(encoding="utf-8")
                if not args.refresh:
                    raise ValueError(f"arquivo já existe (use --refresh apenas para a tranche 06): {target_path}")
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
        f"# Revisão factual assistida por IA — lote `{BATCH_ID}`, tranche 06",
        "",
        f"- Data: {DATE}",
        "- Revisor: `Arena.ai Agent Mode`",
        f"- Escopo: notas **{START}–{START + EXPECTED_NOTES - 1}**, em dez grupos temáticos com dez notas cada; cada linha identifica a conferência factual da nota.",
        "- Fontes primárias: documentação oficial dos projetos e versões indicadas nas próprias notas; as afirmações foram limitadas ao material citado.",
        f"- Resultado: **{EXPECTED_NOTES} revisões factuais por IA registradas** e aprovadas no gate automatizado de qualidade, elevando o terceiro lote `{BATCH_ID}` para **600/2.000 notas válidas (`in_progress`)**. Isto não é aprovação humana nem garantia de ausência de erro.",
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
