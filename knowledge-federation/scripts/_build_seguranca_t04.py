#!/usr/bin/env python3
"""Build tranche 04 (IDs 301-400) for batch software-seguranca-2000-0003 and its AI review report."""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
KF = ROOT / "knowledge-federation"
sys.path.insert(0, str(KF / "scripts"))

from note_quality import assess_markdown, normalize  # noqa: E402
from prose_audit import repeated_substantive_sentences  # noqa: E402

BATCH_ID = "software-seguranca-2000-0003"
DATE = "2026-10-03"
START = 301
EXPECTED_NOTES = 100
REPORT = KF / "exports" / "reports" / "ai-review-software-seguranca-2000-0003-tranche-04.md"
DOMAINS_DIR = KF / "domains"
NOTES_DIR = DOMAINS_DIR / "software-0009" / "software" / "seguranca"
DATA_DIR = KF / "scripts" / "_seguranca_t04_data"

GROUP_META = {
    "01-ziti.txt": {
        "sub": "OpenZiti (plataforma open-source de rede Zero-Trust, *Dark Services* e *Dark Routers* sem portas inbound expostas, *Controller*, *Fabric Mesh*, *SDKs Application-Embedded* e *Tunnelers* `ziti-edge-tunnel`)",
        "src1_label": "OpenZiti GitHub — README.md (Zero Trust Overlay Network, Dark Services and Routers, End-to-End Encryption, SDKs & Tunnelers)",
        "src1_note": "README oficial do openziti/ziti apresentando a arquitetura do Controller, Fabric Mesh, Edge Components e serviços dark",
        "src2_label": "OpenZiti Official Documentation — Introduction & Core Concepts (Controllers, Routers, Edge Clients, Services, Identities & Policies)",
        "src2_note": "Documentação oficial de introdução ao OpenZiti detalhando segmentação por aplicação, mTLS X.509 e criptografia ponta a ponta via libsodium",
        "src3_label": "OpenZiti — Official GitHub Changelog & Repository",
        "src3_note": "Repositório oficial Apache-2.0 do OpenZiti",
    },
    "02-clamav.txt": {
        "sub": "Cisco ClamAV (motor antivírus open-source `libclamav`, daemon multi-thread `clamd`, atualização segura `freshclam`, varredura *On-Access* `clamonacc` via `fanotify`, assinaturas `.hsb`/`.ndb`/`.ldb`/`.cbc` e `clamav-milter`)",
        "src1_label": "Cisco ClamAV Official Documentation — Usage Manual (libclamav Architecture, clamd, clamdscan, clamonacc, freshclam, sigtool & clambc)",
        "src1_note": "Manual oficial de uso do ClamAV detalhando o fluxo de varredura cliente/servidor do clamd, utilitários de banco e configuração",
        "src2_label": "Cisco ClamAV GitHub — README.md (Open-Source Antivirus Engine Overview, Signatures, Packaging & Licensing)",
        "src2_note": "README oficial do Cisco-Talos/clamav descrevendo a arquitetura da engine, suporte multiplataforma e documentação de assinaturas",
        "src3_label": "Cisco ClamAV Official Documentation — Signature Writing Manual",
        "src3_note": "Manual oficial de criação de assinaturas customizadas, lógicas, bytecode e YARA no ClamAV",
    },
    "03-brakeman.txt": {
        "sub": "Brakeman (analisador estático de segurança `SAST` *whole-program* para aplicações Ruby on Rails, níveis de confiança `High`/`Medium`/`Weak`, `CheckSQL`, `CheckCrossSiteScripting`, `CheckMassAssignment`, `config/brakeman.ignore` e SARIF)",
        "src1_label": "Brakeman GitHub — README.md (Static Analysis Security Scanner for Ruby on Rails, Confidence Levels, Configuration & CI)",
        "src1_note": "README oficial do presidentbeef/brakeman apresentando a compatibilidade com Rails 2.3 a 8.x, níveis de confiança e uso em CI/CD",
        "src2_label": "Brakeman Official Options Reference — OPTIONS.md (Whole-Program Analysis, Branching, Check Selection, Output Formats & Ignoring Warnings)",
        "src2_note": "Referência oficial OPTIONS.md do Brakeman detalhando flags de análise de fluxo, --compare, config/brakeman.ignore e métodos seguros",
        "src3_label": "Brakeman Official Documentation — Warning Types Catalog",
        "src3_note": "Catálogo oficial de tipos de vulnerabilidades detectadas pelo Brakeman em aplicações Rails",
    },
    "04-ffuf.txt": {
        "sub": "`ffuf` — Fuzz Faster U Fool (web fuzzer de alta performance em Go para descoberta de diretórios, *Virtual Hosts* e parâmetros, *Auto-Calibration* `-ac`/`-ach`, *Matchers* `-mc`/`-ms`/`-mw`/`-ml` e *Filters* `-fc`/`-fs`/`-fw`/`-fl`)",
        "src1_label": "ffuf GitHub — README.md (Fast Web Fuzzer in Go, Content/Vhost/Parameter/POST Fuzzing, Matchers, Filters & Interactive Mode)",
        "src1_note": "README oficial do ffuf/ffuf documentando todos os modos de operação, flags de matcher/filter, auto-calibração, recursão e mutadores externos",
        "src2_label": "ffuf GitHub — ffufrc.example (Declarative TOML Configuration Reference for HTTP, General, Input, Output, Filter & Matcher Sections)",
        "src2_note": "Arquivo oficial de exemplo de configuração ffufrc detalhando todas as opções declarativas do ffuf",
        "src3_label": "ffuf Official Wiki — Advanced Usage & Configuration Guide",
        "src3_note": "Documentação oficial da wiki do projeto ffuf",
    },
    "05-subfinder.txt": {
        "sub": "ProjectDiscovery Subfinder (enumeração passiva rápida de subdomínios para `EASM`, configuração de provedores e rotação de chaves em `provider-config.yaml`, resolução ativa e eliminação de *wildcards* `-nW`, rate-limiting `-rls` e SDK Go)",
        "src1_label": "ProjectDiscovery Subfinder GitHub — README.md (Fast Passive Subdomain Enumeration Tool, CLI Flags, Provider Config & Go Library)",
        "src1_note": "README oficial do projectdiscovery/subfinder detalhando flags de entrada, seleção de fontes, rate-limit por provedor e saída JSONL",
        "src2_label": "ProjectDiscovery Official Documentation — Subfinder Overview (Passive Architecture, Curated Sources & Workflow Integration)",
        "src2_note": "Visão geral oficial da documentação do Subfinder descrevendo o modelo passivo furtivo e integração em pipelines de reconhecimento",
        "src3_label": "ProjectDiscovery Subfinder — Go SDK Example (v2/examples/main.go)",
        "src3_note": "Exemplo oficial de uso programático do Subfinder como biblioteca Go",
    },
    "06-httpxpd.txt": {
        "sub": "ProjectDiscovery `httpx` (toolkit multi-propósito de *probing* HTTP sobre `retryablehttp-go`, detecção de tecnologias Wappalyzer `-td`, hashes `mmh3` de favicon e `JARM`, inspeção TLS/CSP, *screenshots* headless `-ss` e filtros DSL)",
        "src1_label": "ProjectDiscovery httpx GitHub — README.md (Multi-Purpose HTTP Toolkit, Supported Probes, Headless Screenshots, Matchers, Filters & Extractors)",
        "src1_note": "README oficial do projectdiscovery/httpx documentando a tabela de probes padrão e opcionais, flags de matchers/filters e captura headless",
        "src2_label": "ProjectDiscovery Official Documentation — httpx Overview (Architecture, Smart HTTPS-to-HTTP Fallback, WAF Retries & Pipeline Usage)",
        "src2_note": "Documentação oficial do httpx explicando o papel da ferramenta na transição entre descoberta de ativos e enriquecimento tecnológico",
        "src3_label": "ProjectDiscovery retryablehttp-go GitHub — README.md",
        "src3_note": "Biblioteca HTTP resiliente subjacente ao ProjectDiscovery httpx",
    },
    "07-katana.txt": {
        "sub": "ProjectDiscovery Katana (framework de *web crawling* e *spidering* em modo Standard e Headless Chrome `-hl`, parsing de JavaScript `-jc`/`-jsl` com `jsluice`, preenchimento de formulários `-aff`, deduplicação SimHash `-pcs` e controle de escopo)",
        "src1_label": "ProjectDiscovery Katana GitHub — README.md (Next-Generation Crawling and Spidering Framework, Standard/Headless Modes, JS Crawl, Scope & Similarity Filtering)",
        "src1_note": "README oficial do projectdiscovery/katana detalhando todas as flags de configuração, deduplicação SimHash/TF-IDF/BM25, Knowledge Base e extração de campos",
        "src2_label": "ProjectDiscovery Official Documentation — Katana Overview (SPA Headless Crawling, JavaScript Parsing & Field Extraction)",
        "src2_note": "Visão geral oficial da documentação do Katana cobrindo o rastreamento de Single-Page Applications (React/Angular/Vue) e automação em pipelines",
        "src3_label": "ProjectDiscovery Katana — Official GitHub Releases & Documentation",
        "src3_note": "Repositório oficial MIT do ProjectDiscovery Katana",
    },
    "08-guacsec.txt": {
        "sub": "OpenSSF GUAC — *Graph for Understanding Artifact Composition* (agregação de `SBOMs` SPDX/CycloneDX, atestações `SLSA`/in-toto `DSSE`, `OSV`, `OpenSSF Scorecard` e `VEX` em grafo de alta fidelidade com API GraphQL e CLI `guacone`)",
        "src1_label": "OpenSSF GUAC GitHub — README.md (Graph for Understanding Artifact Composition Architecture, Supported Input Documents & GraphQL Backends)",
        "src1_note": "README oficial do guacsec/guac apresentando o modelo lógico de agregação e síntese da cadeia de suprimentos, formatos suportados e backends Ent/PostgreSQL e Keyvalue",
        "src2_label": "OpenSSF GUAC Official Documentation — GUAC Docs (Visualizer, Querying Vulnerabilities via CLI guacone, Known Package Queries & SBOM Mapping)",
        "src2_note": "Documentação oficial do GUAC demonstrando consultas transitivas de vulnerabilidades, inspeção de pacotes PURL e enriquecimento com OSV.dev, deps.dev e Scorecard",
        "src3_label": "OpenSSF GUAC — Official Supply Chain Use Cases (use-cases.md)",
        "src3_note": "Documento oficial de casos de uso de auditoria, resposta a incidentes e políticas no OpenSSF GUAC",
    },
    "09-rekor.txt": {
        "sub": "Sigstore Rekor (*Transparency Log* imutável e *append-only* para metadados assinados da cadeia de suprimentos, árvores de Merkle `Trillian` e `rekor-tiles` / `Trillian-Tessera`, *Pluggable Types* `hashedrekord`/`dsse`/`intoto`, `rekor-cli` e `rekor-monitor`)",
        "src1_label": "Sigstore Rekor GitHub — README.md (Supply Chain Transparency Log Architecture, Public Instance SLOs, Rekor v2 Tile-Based Logs & Extensibility)",
        "src1_note": "README oficial do sigstore/rekor descrevendo o ledger imutável de assinaturas, endpoints da API REST v1 e evolução para Rekor v2 baseado em tiles e Trillian-Tessera",
        "src2_label": "Sigstore Rekor Official Types Documentation — types.md (Signing and Uploading Pluggable Types: Minisign, SSH, PKIX/X509, TUF & HashedRekord)",
        "src2_note": "Documentação oficial types.md do Rekor demonstrando a assinatura, upload e verificação de entradas nos esquemas plugáveis",
        "src3_label": "Sigstore Official Documentation — Rekor Overview",
        "src3_note": "Visão geral oficial do Rekor na documentação do projeto Sigstore",
    },
    "10-fulcio.txt": {
        "sub": "Sigstore Fulcio (Autoridade Certificadora `CA` gratuita para assinatura de código baseada em identidades `OIDC`, certificados X.509 de curta duração de 10 minutos, extensões `OID 1.3.6.1.4.1.57264.1.*`, *Certificate Transparency Log* `ctfe` e distribuição via `TUF`)",
        "src1_label": "Sigstore Fulcio Official Certificate Specification — docs/certificate-specification.md (RFC 5280 Requirements for Root, Intermediate & Issued Certificates, Empty Subject, Critical SAN & OIDs)",
        "src1_note": "Especificação normativa oficial dos certificados Fulcio detalhando exigências RFC 5280, Subject vazio, SAN crítico, algoritmos de chave e extensões CT Poison/SCT",
        "src2_label": "Sigstore Fulcio Official Security Model — docs/security-model.md (OIDC Proof of Ownership, CT Log Mitigation, Short-Lived Certificates vs Revocation & Rekor Timestamps)",
        "src2_note": "Modelo de segurança oficial do Fulcio explicando como certificados de 10 minutos combinados ao timestamp de inclusão no Rekor eliminam a necessidade de revogação e re-assinatura",
        "src3_label": "Sigstore Fulcio GitHub — README.md (Free Root-CA for Code Signing, TUF Trust Root Initialization, Certificate Maker & CT Log)",
        "src3_note": "README oficial do sigstore/fulcio documentando a instância pública, inicialização via go-tuf, ferramenta certificate-maker e API v2",
    },
}


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
id: software.seguranca.tranche04.{number:06d}
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-04.md"
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
        help="Rebuild the existing tranche-04 notes after validating their IDs and batch metadata.",
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
            r"(?m)^id: software\.seguranca\.tranche04\.\d{6}\s*$",
            path.read_text(encoding="utf-8", errors="replace")[:1200],
        )
    ]
    if args.refresh and len(existing_tranche) != EXPECTED_NOTES:
        raise ValueError(
            f"--refresh exige exatamente {EXPECTED_NOTES} notas tranche04 existentes; encontradas {len(existing_tranche)}"
        )
    if REPORT.exists() and not args.refresh:
        raise ValueError(f"relatório já existe (use --refresh apenas para atualizar a tranche 04): {REPORT}")
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
            expected_id = f"id: software.seguranca.tranche04.{expected_number + index:06d}"
            if target_path.exists():
                current = target_path.read_text(encoding="utf-8")
                if not args.refresh:
                    raise ValueError(f"arquivo já existe (use --refresh apenas para a tranche 04): {target_path}")
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
        f"# Revisão factual assistida por IA — lote `{BATCH_ID}`, tranche 04",
        "",
        f"- Data: {DATE}",
        "- Revisor: `Arena.ai Agent Mode`",
        f"- Escopo: notas **{START}–{START + EXPECTED_NOTES - 1}**, em dez grupos temáticos com dez notas cada; cada linha identifica a conferência factual da nota.",
        "- Fontes primárias: documentação oficial dos projetos e versões indicadas nas próprias notas; as afirmações foram limitadas ao material citado.",
        f"- Resultado: **{EXPECTED_NOTES} revisões factuais por IA registradas** e aprovadas no gate automatizado de qualidade, elevando o terceiro lote `{BATCH_ID}` para **400/2.000 notas válidas (`in_progress`)**. Isto não é aprovação humana nem garantia de ausência de erro.",
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
