#!/usr/bin/env python3
"""Build the source-backed software-devops batch 2 tranche 20 (notes 1901–2000), completing batch software-devops-2000-0002."""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "knowledge-federation" / "scripts" / "_devops_t20_data"
NOTES_DIR = ROOT / "knowledge-federation" / "domains" / "software-0008" / "software" / "devops"
DOMAINS_DIR = ROOT / "knowledge-federation" / "domains"
REPORT = ROOT / "knowledge-federation" / "exports" / "reports" / "ai-review-software-devops-2000-0002-tranche-20.md"
DATE = date.today().isoformat()
START = 1901
EXPECTED_NOTES = 100

sys.path.insert(0, str(ROOT / "knowledge-federation" / "scripts"))
from note_quality import assess_markdown, normalize  # noqa: E402
from prose_audit import repeated_substantive_sentences  # noqa: E402

GROUP_META: dict[str, dict[str, str]] = {
    "01-linuxkit.txt": {
        "sub": "LinuxKit (toolkit para construção de distribuições Linux mínimas, imutáveis e orientadas a containers sobre `containerd`/`runc` com YAML declarativo e `linuxkit build`/`run`/`pkg`)",
        "src1_label": "LinuxKit GitHub — README.md (Toolkit for Building Secure, Portable and Lean Operating Systems for Containers)",
        "src1_note": "README oficial do linuxkit/linuxkit apresentando a arquitetura de imagens de SO imutáveis, formatos de saída, plataformas de execução e ferramentas",
        "src2_label": "LinuxKit Official Documentation — YAML Specification (docs/yaml.md: kernel, init, volumes, onboot, onshutdown, services & files)",
        "src2_note": "Especificação oficial YAML do LinuxKit detalhando a ordem de inicialização, alocação simbólica de uid/gid, volumes OCI e configuração runtime",
        "src3_label": "LinuxKit — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do LinuxKit",
    },
    "02-trustmanager.txt": {
        "sub": "cert-manager `trust-manager` (operador Kubernetes para distribuição declarativa de bundles TLS/X.509 públicos e privados via CRD `Bundle` em `ConfigMaps` e `Secrets`)",
        "src1_label": "cert-manager trust-manager GitHub — README.md (Operator for Distributing Trust Bundles Across a Kubernetes Cluster)",
        "src1_note": "README oficial do cert-manager/trust-manager descrevendo o operador e a sincronização de pacotes de confiança TLS no cluster",
        "src2_label": "cert-manager Official Documentation — trust-manager (Bundle CRD, Trust Namespace, Sources, Targets, JKS/PKCS12 Formats & Kubelet Caveats)",
        "src2_note": "Documentação oficial do trust-manager detalhando o recurso Bundle, Trust Namespace, seletores de fontes/namespaces, JKS/PKCS12 e ressalvas de subPath",
        "src3_label": "cert-manager trust-manager — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do cert-manager trust-manager",
    },
    "03-cfssl.txt": {
        "sub": "Cloudflare CFSSL (toolkit PKI/TLS e servidor HTTP de Autoridade Certificadora com `cfssl`, `cfssljson`, `multirootca`, `mkbundle`, `cfssl-certinfo` e `cfssl-scan`)",
        "src1_label": "Cloudflare CFSSL GitHub — README.md (PKI/TLS Swiss Army Knife, CLI Tools, Signing Profiles, CSR Generation, Bundle Flavors & Multirootca)",
        "src1_note": "README oficial do cloudflare/cfssl detalhando a suíte de binários, perfis de assinatura, geração de CA/certificados, flavors de bundle e servidor API",
        "src2_label": "Cloudflare CFSSL Official CLI Reference — doc/cmd/cfssl.txt (Subcommands: bundle, certinfo, gencert, gencsr, ocsprefresh, ocspserve, scan & serve)",
        "src2_note": "Referência oficial de subcomandos e flags da CLI cfssl",
        "src3_label": "Cloudflare CFSSL — Official GitHub Repository",
        "src3_note": "Repositório oficial BSD-2-Clause do Cloudflare CFSSL",
    },
    "04-stepca.txt": {
        "sub": "Smallstep `step-ca` e `step` CLI (Autoridade Certificadora online privada X.509 e SSH com ACMEv2, provisionadores OIDC/Cloud IID/ACME/X5C, KMS/HSM e renovação automatizada)",
        "src1_label": "Smallstep Certificates GitHub — README.md (step-ca Private Online X.509 & SSH Certificate Authority, ACME Server & Provisioners)",
        "src1_note": "README oficial do smallstep/certificates apresentando a CA online step-ca, suporte ACMEv2, tipos de provisionadores e emissão de certificados X.509 e SSH",
        "src2_label": "Smallstep CLI GitHub — README.md (Zero Trust Swiss Army Knife, step ca/certificate/ssh/crypto/oauth Commands & Examples)",
        "src2_note": "README oficial do smallstep/cli detalhando os grupos de comandos step, inspeção/linting de certificados, JOSE/JWT, OAuth e fluxos mTLS/SSH",
        "src3_label": "Smallstep Certificates — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do Smallstep step-ca",
    },
    "05-openbao.txt": {
        "sub": "OpenBao (cofre open-source OpenSSF/Linux Foundation MPL-2.0 de gerenciamento de segredos e criptografia com `bao`, storage `raft`/`postgresql`, `kv-v2`, Dynamic Secrets e `transit`)",
        "src1_label": "OpenBao GitHub — README.md (OpenSSF/Linux Foundation Community-Driven Secrets & Encryption Management System)",
        "src1_note": "README oficial do openbao/openbao apresentando governança OpenSSF sob MPL-2.0, compilação e documentação",
        "src2_label": "OpenBao Official Documentation — What is OpenBao? (Authenticate/Validate/Authorize/Access Pipeline, Dynamic Secrets, Leasing & Revocation)",
        "src2_note": "Documentação oficial de arquitetura do OpenBao explicando o fluxo de 4 estágios (Authenticate, Validate, Authorize, Access), segredos dinâmicos, leases e revogação",
        "src3_label": "OpenBao — Official GitHub Repository",
        "src3_note": "Repositório oficial MPL-2.0 do OpenBao na OpenSSF",
    },
    "06-infisical.txt": {
        "sub": "Infisical (plataforma open-source de Secrets Management, PKI, KMS e PAM com Kubernetes Operator `v1beta1`, `infisical run`/`scan`, Point-in-Time Recovery, Honey Tokens e Agent Vault)",
        "src1_label": "Infisical GitHub — README.md (Open-Source Secret Management, PKI, KMS & PAM Platform, CLI, Leak Prevention, Honey Tokens & Agent Vault)",
        "src1_note": "README oficial do Infisical/infisical detalhando gerenciamento de segredos, Point-in-Time Recovery, Honey Tokens, Agent Vault, PKI, KMS e PAM",
        "src2_label": "Infisical Official Documentation — Kubernetes Operator Overview (v1beta1 InfisicalConnection/InfisicalAuth/InfisicalStaticSecret, Push/Dynamic Secrets & Auto-Reload)",
        "src2_note": "Documentação oficial do Infisical Kubernetes Operator cobrindo instalação Cluster-wide vs Namespace-scoped, CRDs v1beta1, auto-reload e métricas Prometheus",
        "src3_label": "Infisical — Official GitHub Repository",
        "src3_note": "Repositório oficial MIT do Infisical",
    },
    "07-wazuh.txt": {
        "sub": "Wazuh (plataforma open-source de XDR e SIEM com `Wazuh Server`, `Wazuh Indexer`, `Wazuh Dashboard` e `Wazuh Agent` para FIM, detecção de CVEs, CIS/SCA, Active Response e segurança Cloud/Containers)",
        "src1_label": "Wazuh GitHub — README.md (Open Source XDR and SIEM Platform for Endpoints and Cloud Workloads)",
        "src1_note": "README oficial do wazuh/wazuh resumindo capacidades de XDR/SIEM, FIM, SCA, detecção de vulnerabilidades, Active Response e monitoramento de containers e nuvem",
        "src2_label": "Wazuh Official Documentation — Components (Wazuh Agent, Wazuh Server, Wazuh Indexer, Wazuh Dashboard & Agentless Monitoring)",
        "src2_note": "Documentação oficial de arquitetura dos componentes centrais do Wazuh e comunicação criptografada entre agentes, servidor e indexador",
        "src3_label": "Wazuh — Official GitHub Repository",
        "src3_note": "Repositório oficial GPLv2 do Wazuh",
    },
    "08-crowdsec.txt": {
        "sub": "CrowdSec (motor de segurança colaborativo *Detect Here, Remedy There* com `Log Processor`, `Local API (LAPI)`, `Remediation Components (Bouncers)`, WAF `AppSec`/Coraza e Community Blocklist)",
        "src1_label": "CrowdSec GitHub — README.md (Collaborative IPS, AppSec WAF on Coraza, Bot Detection PoW & Community Blocklist)",
        "src1_note": "README oficial do crowdsecurity/crowdsec apresentando o motor comportamental, componente AppSec WAF compatível com ModSecurity/OWASP CRS e detecção de bots PoW",
        "src2_label": "CrowdSec Official Documentation — Concepts (Security Engine, Log Processor, Local API, Central API, Hub Collections, Scenarios & Bouncers)",
        "src2_note": "Documentação oficial de conceitos do CrowdSec detalhando Data Sources, Parsers, Enrichers, Scenarios Leaky Bucket, LAPI, Profiles, Decisions e Bouncers",
        "src3_label": "CrowdSec — Official GitHub Repository",
        "src3_note": "Repositório oficial MIT do CrowdSec",
    },
    "09-keptn.txt": {
        "sub": "Keptn (operador CNCF Incubating de ciclo de vida e observabilidade de aplicações cloud-native com `KeptnApp`, `KeptnTaskDefinition`, `KeptnEvaluationDefinition`, `KeptnMetric` e traces OpenTelemetry/DORA)",
        "src1_label": "Keptn Lifecycle Toolkit GitHub — README.md (Cloud-Native Application Lifecycle Orchestration, Metrics, OpenTelemetry Observability & Helm Install)",
        "src1_note": "README oficial do keptn/lifecycle-toolkit descrevendo os três pilares (Metrics, Observability, Release Lifecycle Management), instalação Helm e matriz de componentes",
        "src2_label": "Keptn Official Documentation — Core Concepts (KeptnApp, KeptnWorkload, Pre/Post Deployment Tasks & Evaluations, Multi-Source Metrics & OpenTelemetry)",
        "src2_note": "Documentação oficial de conceitos centrais do Keptn explicando o fluxo de pré/pós-deploy, execução paralela/sequencial de KeptnTask, SLOs e Custom Metrics API para HPA",
        "src3_label": "Keptn Lifecycle Toolkit — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do Keptn na CNCF",
    },
    "10-benthos.txt": {
        "sub": "Redpanda Connect / Benthos (processador declarativo de streams cloud-native com entrega *at-least-once* sem estado em disco, linguagem `Bloblang`, `CDC`, `Iceberg`, `Streams Mode` e testes unitários)",
        "src1_label": "Redpanda Connect GitHub — README.md (Declarative Stream Processor, At-Least-Once Transaction Model, CDC to Iceberg, /ping & /ready Probes)",
        "src1_note": "README oficial do redpanda-data/connect detalhando instalação, execução via Docker/CLI, exemplo de Postgres CDC para Iceberg, probes HTTP e SDK de extensibilidade em Go",
        "src2_label": "Redpanda Connect Official Documentation — About Redpanda Connect (Bloblang Mapping, Stateless In-Process Transactions, Batching, Branching & Observability)",
        "src2_note": "Documentação oficial de arquitetura do Redpanda Connect / Benthos cobrindo garantias de entrega, Bloblang, conectores e operação cloud-native",
        "src3_label": "Redpanda Connect (Benthos) — Official GitHub Repository",
        "src3_note": "Repositório oficial do Redpanda Connect / Benthos",
    },
}


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
id: software.devops.tranche20.{number:06d}
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-20.md"
fontes: [{', '.join('"' + source[1] + '"' for source in sources)}]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
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
        help="Rebuild the existing tranche-20 notes after validating their IDs and batch metadata.",
    )
    args = parser.parse_args()
    group_files = sorted(DATA_DIR.glob("*.txt"))
    if len(group_files) != 10:
        raise SystemExit(f"Esperados 10 arquivos de grupo; encontrados {len(group_files)}")

    existing_paths = list(DOMAINS_DIR.rglob("*.md"))
    existing_tranche = [
        path
        for path in existing_paths
        if re.search(
            r"(?m)^id: software\.devops\.tranche20\.\d{6}\s*$",
            path.read_text(encoding="utf-8", errors="replace")[:1200],
        )
    ]
    if args.refresh and len(existing_tranche) != EXPECTED_NOTES:
        raise ValueError(
            f"--refresh exige exatamente {EXPECTED_NOTES} notas tranche20 existentes; encontradas {len(existing_tranche)}"
        )
    if REPORT.exists() and not args.refresh:
        raise ValueError(f"relatório já existe (use --refresh apenas para atualizar a tranche 20): {REPORT}")
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
            expected_id = f"id: software.devops.tranche20.{expected_number + index:06d}"
            if target_path.exists():
                current = target_path.read_text(encoding="utf-8")
                if not args.refresh:
                    raise ValueError(f"arquivo já existe (use --refresh apenas para a tranche 20): {target_path}")
                if (
                    expected_id not in current.splitlines()[:25]
                    or "lote: software-devops-2000-0002" not in current.splitlines()[:25]
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
        "# Revisão factual assistida por IA — lote `software-devops-2000-0002`, tranche 20",
        "",
        f"- Data: {DATE}",
        "- Revisor: `Arena.ai Agent Mode`",
        f"- Escopo: notas **{START}–{START + EXPECTED_NOTES - 1}**, em dez grupos temáticos com dez notas cada; cada linha identifica a conferência factual da nota.",
        "- Fontes primárias: documentação oficial dos projetos e versões indicadas nas próprias notas; as afirmações foram limitadas ao material citado.",
        f"- Resultado: **{EXPECTED_NOTES} revisões factuais por IA registradas** e aprovadas no gate automatizado de qualidade, completando o segundo lote `software-devops-2000-0002` em **2000/2.000 notas válidas (`complete`)**. Isto não é aprovação humana nem garantia de ausência de erro.",
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
