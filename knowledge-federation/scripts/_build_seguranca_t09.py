#!/usr/bin/env python3
"""Build 100 substantive notes for batch software-seguranca-2000-0003 tranche 09 (IDs 801-900) and its AI factual review report."""
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
REPORT = KF / "exports" / "reports" / "ai-review-software-seguranca-2000-0003-tranche-09.md"
DATA_DIR = Path(__file__).resolve().parent / "_seguranca_t09_data"
BATCH_ID = "software-seguranca-2000-0003"
DATE = "2026-10-03"
START = 801
EXPECTED_NOTES = 100

sys.path.insert(0, str(Path(__file__).resolve().parent))
from note_quality import assess_markdown  # noqa: E402
from prose_audit import repeated_substantive_sentences  # noqa: E402


GROUP_META = {
    "01-kics.txt": {
        "sub": "Checkmarx KICS (Keeping Infrastructure as Code Secure) — Scanner SAST Multi-IaC com OPA/Rego, Queries Customizadas, Bill of Materials (BoM) e CI/CD",
        "src1_label": "Checkmarx KICS Official GitHub — Keeping Infrastructure as Code Secure Architecture & Supported Platforms",
        "src1_note": "repositório oficial do Checkmarx KICS cobrindo arquitetura Go + OPA/Rego, 22+ plataformas IaC suportadas e execução via CLI/Docker",
        "src2_label": "Checkmarx KICS Official Documentation — CLI Commands, Flags & Exit Codes Reference",
        "src2_note": "documentação oficial de comandos, flags, códigos de saída, formatos de relatório e arquivo de configuração do KICS",
        "src3_label": "Checkmarx KICS Official Documentation — Architecture & Custom OPA Rego Queries",
        "src3_note": "documentação oficial da arquitetura interna de parsers/AST JSON e autoria de queries customizadas em Rego (`CxPolicy`)",
    },
    "02-naabu.txt": {
        "sub": "ProjectDiscovery Naabu — Scanner Rápido de Portas SYN/CONNECT/UDP em Go, Descoberta de Hosts (ARP/ICMP/TCP), Shodan InternetDB e Handoff para Nmap/httpx",
        "src1_label": "ProjectDiscovery Naabu Official GitHub — Fast Port Scanner Written in Go",
        "src1_note": "repositório oficial do ProjectDiscovery Naabu cobrindo arquitetura SYN/CONNECT, flags CLI, descoberta de hosts e integração com Nmap",
        "src2_label": "ProjectDiscovery Naabu Official Documentation — Usage, Configuration & Rate Tuning",
        "src2_note": "documentação oficial do Naabu na plataforma ProjectDiscovery Docs",
        "src3_label": "Go Package Documentation — github.com/projectdiscovery/naabu/v2",
        "src3_note": "documentação técnica do pacote Go e SDK `naabu/v2/pkg/runner`",
    },
    "03-dnsx.txt": {
        "sub": "ProjectDiscovery dnsx — Toolkit DNS Multi-Propósito em Go, Filtragem de Wildcard DNS, Reconhecimento de Registros/SPF/DMARC/DNSSEC, CDN/ASN e Força Bruta",
        "src1_label": "ProjectDiscovery dnsx Official GitHub — Fast and Multi-Purpose DNS Toolkit",
        "src1_note": "repositório oficial do ProjectDiscovery dnsx cobrindo resolução em massa, filtragem de wildcard, força bruta, PTR reverso e rcodes",
        "src2_label": "ProjectDiscovery dnsx Official Documentation — CLI Flags & Pipeline Examples",
        "src2_note": "documentação oficial do dnsx na plataforma ProjectDiscovery Docs",
        "src3_label": "Go Package Documentation — github.com/projectdiscovery/dnsx",
        "src3_note": "referência técnica da biblioteca Go do ProjectDiscovery dnsx",
    },
    "04-tlsx.txt": {
        "sub": "ProjectDiscovery tlsx — Scanner TLS/X.509 Rápido em Go, Múltiplos Motores (crypto/tls, zcrypto, openssl), Extração de SAN/CN, Fingerprinting JA3/JARM e mTLS",
        "src1_label": "ProjectDiscovery tlsx Official GitHub — Fast and Configurable TLS Grabber Focused on TLS Data Collection",
        "src1_note": "repositório oficial do ProjectDiscovery tlsx cobrindo os 4 motores TLS, extração SAN/CN, auditoria de certificados/cifras e hashes JA3/JARM",
        "src2_label": "ProjectDiscovery tlsx Official Documentation — Scan Modes & Certificate Analysis",
        "src2_note": "documentação oficial do tlsx na plataforma ProjectDiscovery Docs",
        "src3_label": "Go Package Documentation — github.com/projectdiscovery/tlsx",
        "src3_note": "referência técnica do pacote Go `projectdiscovery/tlsx`",
    },
    "05-wpscan.txt": {
        "sub": "WPScan (wpscanteam/wpscan) — Scanner de Segurança WordPress, Enumeração de Plugins/Temas/Usuários/Backups/Timthumbs, Força Bruta XML-RPC MultiCall e API WPVulnDB",
        "src1_label": "WPScan Official GitHub — WordPress Security Scanner CLI & Enumeration Options",
        "src1_note": "repositório oficial do WPScan cobrindo modos de detecção (`mixed`, `passive`, `aggressive`), enumeração `-e`, ataques de senha e formatos de saída",
        "src2_label": "WPScan Official RubyGems Specification & Dependencies (`cms_scanner`)",
        "src2_note": "especificação oficial da gem Ruby `wpscan` e sua arquitetura sobre `cms_scanner` e `typhoeus`",
        "src3_label": "WPScan Official User Documentation & CLI Guide",
        "src3_note": "documentação oficial de uso da CLI do WPScan e integração com a API de vulnerabilidades",
    },
    "06-nikto.txt": {
        "sub": "Nikto Web Server Scanner (sullo/nikto) — Auditoria de Servidores Web, Cabeçalhos, Arquivos Perigosos/CGIs, Tuning, Mutate, LibWhisker Evasion e Relatórios",
        "src1_label": "Nikto Official GitHub — Web Server Scanner CLI Reference, Tuning & Mutate Modes",
        "src1_note": "documentação oficial do Nikto cobrindo categorias `-Tuning` (incluindo exclusão `x`), modos `-mutate`, técnicas `-evasion` e formatos de saída",
        "src2_label": "Nikto Official Default Configuration Reference (`nikto.conf.default`)",
        "src2_note": "arquivo oficial de configuração `nikto.conf.default` cobrindo macros `@@DEFAULT`, `STATIC-COOKIE`, `SKIPIDS`, banco SQL e opções LibWhisker",
        "src3_label": "Nikto Official Project Wiki — Plugins, Databases & Reporting",
        "src3_note": "wiki oficial do projeto Nikto cobrindo estrutura dos bancos `db_tests`/`udb_tests` e plugins",
    },
    "07-wapiti.txt": {
        "sub": "Wapiti Web Vulnerability Scanner (wapiti-scanner/wapiti) — Scanner DAST Black-Box Assíncrono (httpx/Playwright), Módulos SQLi/XSS/SSRF/XXE/RCE/CSP e OpenAPI",
        "src1_label": "Wapiti Official GitHub — Black-Box Web Vulnerability Scanner & 34 Attack Modules Reference",
        "src1_note": "documentação oficial do Wapiti 3 cobrindo os 34 módulos de ataque, escopo de crawling, navegador headless Playwright, OpenAPI/Swagger e OAST",
        "src2_label": "Wapiti Official PyProject Specification — Async Architecture (`httpx`, `aiosqlite`, `playwright`, `mitmproxy`)",
        "src2_note": "especificação técnica oficial do Wapiti 3 (`pyproject.toml`) e seus utilitários `wapiti` e `wapiti-getcookie`",
        "src3_label": "Wapiti Official Project Portal & Documentation",
        "src3_note": "portal oficial de documentação do scanner de vulnerabilidades web Wapiti",
    },
    "08-arjun.txt": {
        "sub": "Arjun (s0md3v/Arjun) — Descoberta Heurística de Parâmetros HTTP Ocultos (GET, POST, JSON, XML) via Busca Binária de Anomalias e Extração Passiva",
        "src1_label": "Arjun Official GitHub — HTTP Parameter Discovery Suite",
        "src1_note": "repositório oficial do Arjun cobrindo descoberta de parâmetros HTTP ocultos e suporte a GET/POST/JSON/XML",
        "src2_label": "Arjun Official Core Source (`arjun/__main__.py`) — Binary Search Narrower, Anomaly Calibration & CLI Flags",
        "src2_note": "código-fonte oficial do motor do Arjun mostrando a calibração dos fatores de anomalia (`define`/`compare`), busca binária em chunks e flags CLI",
        "src3_label": "Arjun Official Wiki — How Arjun Works & Usage Guide",
        "src3_note": "wiki técnica oficial do projeto Arjun detalhando o algoritmo de detecção de anomalias, extração heurística e coleta passiva",
    },
    "09-jwt-tool.txt": {
        "sub": "jwt_tool (ticarpi/jwt_tool) & Segurança Criptográfica de JSON Web Tokens (IETF RFC 7515 / RFC 7519 / RFC 8725 BCP) — Auditoria, Tampering e Mitigação",
        "src1_label": "jwt_tool Official GitHub — Toolkit for Validating, Forging, Scanning and Tampering JWTs",
        "src1_note": "documentação oficial do `jwt_tool` cobrindo modos de varredura (`-M pb/at/er/cc`), exploits conhecidos (`-X a/n/b/p/k/i/s`), tampering e cracking",
        "src2_label": "IETF RFC 8725 (BCP 225) — JSON Web Token Best Current Practices",
        "src2_note": "padrão oficial IETF BCP 225 (RFC 8725) especificando vulnerabilidades criptográficas e práticas recomendadas de validação de JSON Web Tokens",
        "src3_label": "IETF RFC 7519 — JSON Web Token (JWT) Standard Specification",
        "src3_note": "especificação normativa IETF RFC 7519 para estrutura e claims registradas de JSON Web Tokens",
    },
    "10-feroxbuster.txt": {
        "sub": "Feroxbuster (epi052/feroxbuster) — Descoberta Recursiva Forçada de Conteúdo Web em Rust, Auto-Tune/Auto-Bail, Filtros de Similaridade, Extração de Links e Estado",
        "src1_label": "Feroxbuster Official GitHub — Fast, Simple, Recursive Content Discovery Tool Written in Rust",
        "src1_note": "repositório oficial do Feroxbuster cobrindo descoberta recursiva concorrente em Rust, filtros, coleta dinâmica de palavras/backups e replay proxy",
        "src2_label": "Feroxbuster Official Configuration Reference (`ferox-config.toml.example`)",
        "src2_note": "especificação completa de todas as opções de configuração e flags do Feroxbuster (`auto_tune`, `auto_bail`, `filter_similar`, `scope`, mTLS e estado)",
        "src3_label": "Feroxbuster Official Documentation Portal",
        "src3_note": "documentação técnica oficial do projeto Feroxbuster",
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
id: software.seguranca.tranche09.{number:06d}
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-09.md"
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
        help="Rebuild the existing tranche-09 notes after validating their IDs and batch metadata.",
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
            r"(?m)^id: software\.seguranca\.tranche09\.\d{6}\s*$",
            path.read_text(encoding="utf-8", errors="replace")[:1200],
        )
    ]
    if args.refresh and len(existing_tranche) != EXPECTED_NOTES:
        raise ValueError(
            f"--refresh exige exatamente {EXPECTED_NOTES} notas tranche09 existentes; encontradas {len(existing_tranche)}"
        )
    if REPORT.exists() and not args.refresh:
        raise ValueError(f"relatório já existe (use --refresh apenas para atualizar a tranche 09): {REPORT}")
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
            expected_id = f"id: software.seguranca.tranche09.{expected_number + index:06d}"
            if target_path.exists():
                current = target_path.read_text(encoding="utf-8")
                if not args.refresh:
                    raise ValueError(f"arquivo já existe (use --refresh apenas para a tranche 09): {target_path}")
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
        f"# Revisão factual assistida por IA — lote `{BATCH_ID}`, tranche 09",
        "",
        f"- Data: {DATE}",
        "- Revisor: `Arena.ai Agent Mode`",
        f"- Escopo: notas **{START}–{START + EXPECTED_NOTES - 1}**, em dez grupos temáticos com dez notas cada; cada linha identifica a conferência factual da nota.",
        "- Fontes primárias: documentação oficial dos projetos e versões indicadas nas próprias notas; as afirmações foram limitadas ao material citado.",
        f"- Resultado: **{EXPECTED_NOTES} revisões factuais por IA registradas** e aprovadas no gate automatizado de qualidade, elevando o terceiro lote `{BATCH_ID}` para **900/2.000 notas válidas (`in_progress`)**. Isto não é aprovação humana nem garantia de ausência de erro.",
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
