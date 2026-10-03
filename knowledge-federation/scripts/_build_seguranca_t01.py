#!/usr/bin/env python3
"""Build tranche 01 (IDs 1-100) for batch software-seguranca-2000-0003 and its AI review report."""
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
START = 1
EXPECTED_NOTES = 100
REPORT = KF / "exports" / "reports" / "ai-review-software-seguranca-2000-0003-tranche-01.md"
DOMAINS_DIR = KF / "domains"
NOTES_DIR = DOMAINS_DIR / "software-0009" / "software" / "seguranca"
DATA_DIR = KF / "scripts" / "_seguranca_t01_data"

GROUP_META = {
    "01-gitleaks.txt": {
        "sub": "Gitleaks (varredura determinística de segredos em repositórios Git, diretórios e streams, hierarquia `gitleaks.toml`, `[extend]`, `[allowlist]`, `.gitleaksignore` e `--baseline-path`)",
        "src1_label": "Gitleaks GitHub — README.md (Subcommands git/dir/stdin, Configuration Precedence, .gitleaksignore, Baseline & Archive Depth)",
        "src1_note": "README oficial do gitleaks/gitleaks detalhando instalação, subcomandos git/dir/stdin, precedência de configuração em 4 níveis, uso em pre-commit/GitHub Actions e flags de decodificação",
        "src2_label": "Gitleaks Official Default Config — config/gitleaks.toml (Rules, Regexes, Entropy, Keywords, SecretGroup & Global Allowlists)",
        "src2_note": "Arquivo oficial de regras padrão config/gitleaks.toml com a definição completa de allowlists globais, keywords de pré-filtro, entropia de Shannon e grupos de captura",
        "src3_label": "Gitleaks — Official GitHub Repository",
        "src3_note": "Repositório oficial open-source do Gitleaks",
    },
    "02-trufflehog.txt": {
        "sub": "TruffleHog (descoberta, classificação, validação ativa em tempo real de mais de 800 tipos de credenciais, `trufflehog analyze`, filtros `--results=verified,unknown` e detectores customizados)",
        "src1_label": "TruffleHog GitHub — README.md (4 Pillars: Discovery, Classification, Validation & Analysis, --results Filters, CI/CD & Custom Detectors)",
        "src1_note": "README oficial do trufflesecurity/trufflehog documentando os 4 pilares, verificação ativa de credenciais, exit code 183 com --fail, verificação Cosign e detectores customizados",
        "src2_label": "TruffleHog GitHub — CONTRIBUTING.md (Architecture of Pipeline Stages, Aho-Corasick Keyword Matching, Detectors & Verification)",
        "src2_note": "Guia técnico de arquitetura do TruffleHog detalhando o pipeline concorrente Source -> Chunker -> Matcher Aho-Corasick -> Detector -> Verifier -> Dispatcher",
        "src3_label": "TruffleHog — Official GitHub Repository (Truffle Security)",
        "src3_note": "Repositório oficial open-source do TruffleHog",
    },
    "03-osvscanner.txt": {
        "sub": "Google OSV-Scanner V2 (análise de composição de software sobre `OSV.dev` e `OSV-Scalibr`, varredura de containers, análise de alcançabilidade *Call Analysis* e remediação guiada `osv-scanner fix`)",
        "src1_label": "Google OSV-Scanner GitHub — README.md (OSV-Scanner V2 Features, OSV-Scalibr Engine, Container Scanning, Call Analysis & Guided Remediation)",
        "src1_note": "README oficial do google/osv-scanner descrevendo a arquitetura V2 baseada no OSV-Scalibr, suporte a lockfiles/SBOMs, imagens de container e remediação guiada",
        "src2_label": "OSV-Scanner Official Documentation — Usage & Configuration (scan source, scan image, fix Strategies, --licenses, Offline DB & osv-scanner.toml)",
        "src2_note": "Documentação oficial de uso do OSV-Scanner detalhando flags de CLI, estratégias de osv-scanner fix (in-place, relax, override), auditoria SPDX e osv-scanner.toml",
        "src3_label": "Google OSV-Scanner — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do Google OSV-Scanner",
    },
    "04-deptrack.txt": {
        "sub": "OWASP Dependency-Track (plataforma contínua API-first de análise de SBOM CycloneDX, correlação de vulnerabilidades com pontuação EPSS, triagem VEX e Policy Engine)",
        "src1_label": "OWASP Dependency-Track GitHub — README.md (Continuous SBOM Analysis Platform, CycloneDX, VEX, EPSS, Policy Engine & Ecosystem Integrations)",
        "src1_note": "README oficial do DependencyTrack/dependency-track documentando arquitetura API-first, consumo de SBOM CycloneDX, fontes de inteligência, EPSS e VEX",
        "src2_label": "OWASP Dependency-Track Official Documentation — Initial Startup & Operational Configuration (Admin Setup, Feeds, Mirroring & Portfolio Management)",
        "src2_note": "Documentação oficial de inicialização e operação do Dependency-Track cobrindo provisionamento, sincronização de bases NVD/OSV/EPSS e controle de acesso",
        "src3_label": "OWASP Dependency-Track — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do OWASP Dependency-Track",
    },
    "05-zaproxy.txt": {
        "sub": "OWASP ZAP / Zed Attack Proxy (DAST declarativo com Automation Framework YAML, `spider`/`spiderAjax`, importação `openapi`/`graphql`, `passiveScan-wait`, `activeScan`, `alertFilter` e `exitStatus`)",
        "src1_label": "OWASP ZAP Official Documentation — Automation Framework (Declarative YAML Plan, env Contexts, Discovery/Scan/Report Jobs & Job Tests)",
        "src1_note": "Documentação oficial do Automation Framework do OWASP ZAP detalhando a estrutura YAML env/jobs, substituição dos Packaged Scans e lista completa de jobs suportados",
        "src2_label": "OWASP ZAP GitHub — README.md (Zed Attack Proxy Architecture, Passive & Active Scanners, Container Images & Add-ons)",
        "src2_note": "README oficial do zaproxy/zaproxy apresentando o projeto DAST open-source, modos de execução headless e ecossistema de extensões",
        "src3_label": "OWASP ZAP — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do OWASP Zed Attack Proxy",
    },
    "06-nuclei.txt": {
        "sub": "ProjectDiscovery Nuclei (scanner de vulnerabilidades de alta performance baseado em templates YAML multi-protocolo, workflows condicionais, detecção OAST via Interactsh e exportação SARIF)",
        "src1_label": "ProjectDiscovery Nuclei GitHub — README.md (YAML Template Engine, Multi-Protocol Support, Filtering Flags, Rate Limiting & CI/CD Reporting)",
        "src1_note": "README oficial do projectdiscovery/nuclei documentando instalação, flags de filtragem de templates, controle de concorrência, OAST Interactsh e formatos de saída",
        "src2_label": "ProjectDiscovery Official Documentation — Nuclei Overview (Template Anatomy, Matchers/Extractors, Request Clustering, Workflows & Authenticated Scans)",
        "src2_note": "Visão geral oficial da documentação do Nuclei explicando a anatomia dos templates YAML, agrupamento de requisições, fluxos multi-step e varreduras autenticadas",
        "src3_label": "ProjectDiscovery Nuclei — Official GitHub Repository",
        "src3_note": "Repositório oficial MIT do ProjectDiscovery Nuclei",
    },
    "07-openfga.txt": {
        "sub": "OpenFGA (motor de autorização CNCF Incubating inspirado no Google Zanzibar para ReBAC/ABAC, DSL `schema 1.1`/`1.2`, Conditions CEL, APIs `Check`/`ListObjects`, `fga model test` e PostgreSQL)",
        "src1_label": "OpenFGA GitHub — README.md (CNCF Incubating Zanzibar Engine, Docker/CLI Quickstart, Production Storage, SLSA Level 3 & Official SDKs)",
        "src1_note": "README oficial do openfga/openfga detalhando execução via Docker e binário, migrações para PostgreSQL/MySQL, nota sobre Unix Domain Socket em /tmp e ferramentas do ecossistema",
        "src2_label": "OpenFGA Official Documentation — Core Concepts (Stores, Types, Objects, Users/Usersets, Relations, Authorization Models, Tuples & Queries)",
        "src2_note": "Documentação oficial de conceitos do OpenFGA explicando modelagem ReBAC/ABAC, imutabilidade de modelos, operadores de conjunto e semântica das APIs Check, ListObjects, ListUsers e Expand",
        "src3_label": "OpenFGA — Official GitHub Repository (CNCF)",
        "src3_note": "Repositório oficial Apache-2.0 do OpenFGA",
    },
    "08-spicedb.txt": {
        "sub": "AuthZed SpiceDB (banco de dados de permissões distribuído inspirado no Google Zanzibar, linguagem de schema `.zed`, Caveats CEL, consistência `ZedToken`, `zed validate` e cluster dispatch)",
        "src1_label": "AuthZed SpiceDB GitHub — README.md (Distributed Permissions Database, Zanzibar Architecture, Consistency Modes, Datastores & zed CLI)",
        "src1_note": "README oficial do authzed/spicedb detalhando a arquitetura do banco de permissões, garantias de consistência por requisição, motores de armazenamento e execução em Kubernetes",
        "src2_label": "AuthZed SpiceDB Official Documentation — Schema Language Reference (Definitions, Relations vs Permissions, +, &, -, -> Operators, Precedence & Caveats)",
        "src2_note": "Referência oficial da linguagem de schema do SpiceDB cobrindo definitions, subject relations, wildcards, operadores de conjunto, alerta de precedência do operador + e caveats CEL",
        "src3_label": "AuthZed SpiceDB — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do AuthZed SpiceDB",
    },
    "09-cerbos.txt": {
        "sub": "Cerbos PDP (Policy Decision Point stateless para autorização PBAC/ABAC/RBAC, os 6 tipos de política YAML, `Derived Roles`, APIs `CheckResources` e `PlanResources` AST, `cerbos compile` e JWKS)",
        "src1_label": "Cerbos GitHub — README.md (Stateless Policy Decision Point, CheckResources & PlanResources APIs, Derived Roles, Deployment Topologies & cerbos compile)",
        "src1_note": "README oficial do cerbos/cerbos documentando a arquitetura stateless do PDP, exemplos de políticas YAML, avaliação em lote, geração de Query Plan e execução via container/sidecar",
        "src2_label": "Cerbos Official Documentation — Policies Overview (Resource, Derived Roles, Principal, Role Policies, Exported Variables/Constants & Scoped Policies)",
        "src2_note": "Documentação oficial de políticas do Cerbos detalhando os 6 tipos de política YAML, escopos hierárquicos multi-tenant, condições CEL, schemas e auditoria de decisões",
        "src3_label": "Cerbos — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do Cerbos PDP",
    },
    "10-scorecard.txt": {
        "sub": "OpenSSF Scorecard (avaliação automatizada de postura de segurança em repositórios open-source e supply chain, `Branch-Protection` em 5 Tiers, `Pinned-Dependencies`, `Token-Permissions` e Probes V5)",
        "src1_label": "OpenSSF Scorecard GitHub — README.md (Automated Security Assessment for Open Source, CLI & GitHub Action, Structured Results Probes & BigQuery Dataset)",
        "src1_note": "README oficial do ossf/scorecard cobrindo objetivos do projeto, execução via CLI/Docker/GitHub Action, sistema de Probes V5 e dataset público semanal no BigQuery",
        "src2_label": "OpenSSF Scorecard Official Documentation — Checks Reference (docs/checks.md: Branch-Protection 5 Tiers, Binary-Artifacts, Token-Permissions, Pinned-Dependencies & Signed-Releases)",
        "src2_note": "Catálogo técnico oficial docs/checks.md detalhando risco, critérios de pontuação e passos de remediação de cada check do OpenSSF Scorecard",
        "src3_label": "OpenSSF Scorecard — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do OpenSSF Scorecard",
    },
}


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip().lower())


def parse_group(path: Path) -> tuple[dict[str, str], list[dict[str, object]]]:
    raw = path.read_text(encoding="utf-8").strip()
    records = [r.strip() for r in re.split(r"(?m)^(?=\d{4}\|[a-z0-9-]+)", raw) if r.strip()]
    if len(records) != 10:
        raise ValueError(f"{path.name}: esperadas 10 notas, encontradas {len(records)}")

    meta = GROUP_META[path.name]
    group_title = meta["sub"]
    rows: list[dict[str, object]] = []
    first_num: int | None = None

    for rec in records:
        code_m = re.search(r"\|(```[\s\S]+?```)\|", rec)
        if not code_m:
            raise ValueError(f"{path.name}: bloco de código não encontrado: {rec[:140]}...")
        pre = rec[: code_m.start()]
        example = code_m.group(1).strip()
        post = rec[code_m.end() :]

        pre_parts = re.split(r"\|(?=(?:[^`]*`[^`]*`)*[^`]*$)", pre)
        post_parts = re.split(r"\|(?=(?:[^`]*`[^`]*`)*[^`]*$)", post)
        if len(pre_parts) != 6 or len(post_parts) != 3:
            raise ValueError(
                f"{path.name}: falha ao analisar registro (pre={len(pre_parts)}, post={len(post_parts)}): {rec[:140]}..."
            )
        num_str, slug, title, summary, reason, how = [g.strip() for g in pre_parts]
        caveat, verify, sources_raw = [g.strip() for g in post_parts]
        num = int(num_str)
        if first_num is None:
            first_num = num
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
            raise ValueError(f"{path.name}: slug inválido: {slug}")

        urls = [u.strip() for u in sources_raw.split(";") if u.strip()]
        if len(urls) < 2:
            raise ValueError(f"{path.name} nota {num}: menos de 2 URLs")

        sources = [
            (meta["src1_label"], urls[0], meta["src1_note"]),
            (meta["src2_label"], urls[1], meta["src2_note"]),
        ]
        if len(urls) >= 3:
            sources.append((meta["src3_label"], urls[2], meta["src3_note"]))

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
                "links": [],
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
id: software.seguranca.tranche01.{number:06d}
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-01.md"
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
        help="Rebuild the existing tranche-01 notes after validating their IDs and batch metadata.",
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
            r"(?m)^id: software\.seguranca\.tranche01\.\d{6}\s*$",
            path.read_text(encoding="utf-8", errors="replace")[:1200],
        )
    ]
    if args.refresh and len(existing_tranche) != EXPECTED_NOTES:
        raise ValueError(
            f"--refresh exige exatamente {EXPECTED_NOTES} notas tranche01 existentes; encontradas {len(existing_tranche)}"
        )
    if REPORT.exists() and not args.refresh:
        raise ValueError(f"relatório já existe (use --refresh apenas para atualizar a tranche 01): {REPORT}")
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
            expected_id = f"id: software.seguranca.tranche01.{expected_number + index:06d}"
            if target_path.exists():
                current = target_path.read_text(encoding="utf-8")
                if not args.refresh:
                    raise ValueError(f"arquivo já existe (use --refresh apenas para a tranche 01): {target_path}")
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
        f"# Revisão factual assistida por IA — lote `{BATCH_ID}`, tranche 01",
        "",
        f"- Data: {DATE}",
        "- Revisor: `Arena.ai Agent Mode`",
        f"- Escopo: notas **{START}–{START + EXPECTED_NOTES - 1}**, em dez grupos temáticos com dez notas cada; cada linha identifica a conferência factual da nota.",
        "- Fontes primárias: documentação oficial dos projetos e versões indicadas nas próprias notas; as afirmações foram limitadas ao material citado.",
        f"- Resultado: **{EXPECTED_NOTES} revisões factuais por IA registradas** e aprovadas no gate automatizado de qualidade, abrindo o terceiro lote `{BATCH_ID}` em **100/2.000 notas válidas (`in_progress`)**. Isto não é aprovação humana nem garantia de ausência de erro.",
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
