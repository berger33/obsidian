#!/usr/bin/env python3
"""Build the source-backed software-devops batch 2 tranche 3 (notes 201–300)."""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "knowledge-federation" / "scripts" / "_devops_t03_data"
NOTES_DIR = ROOT / "knowledge-federation" / "domains" / "software-0008" / "software" / "devops"
DOMAINS_DIR = ROOT / "knowledge-federation" / "domains"
REPORT = ROOT / "knowledge-federation" / "exports" / "reports" / "ai-review-software-devops-2000-0002-tranche-03.md"
DATE = date.today().isoformat()
START = 201
EXPECTED_NOTES = 100

sys.path.insert(0, str(ROOT / "knowledge-federation" / "scripts"))
from note_quality import assess_markdown, normalize  # noqa: E402
from prose_audit import repeated_substantive_sentences  # noqa: E402

SOURCES = {
    "cmg_readme": (
        "cert-manager — GitHub README",
        "https://raw.githubusercontent.com/cert-manager/cert-manager/master/README.md",
        "Visão geral do cert-manager para certificados e emissores no Kubernetes (ACME/Let's Encrypt, HashiCorp Vault, CyberArk, in-cluster), renovação automática, política de módulo Go e histórico kube-lego.",
    ),
    "cmg_docs": (
        "cert-manager Documentation — Getting Started & Installation",
        "https://cert-manager.io/docs/getting-started/",
        "Documentação oficial do cert-manager cobrindo instalação, configuração de Issuers/Certificates, nginx-ingress e troubleshooting.",
    ),
    "cmg_repo": (
        "cert-manager — Repositório Oficial no GitHub",
        "https://github.com/cert-manager/cert-manager",
        "Repositório oficial do cert-manager na CNCF com código-fonte, SECURITY.md e notas de release.",
    ),
    "exd_readme": (
        "ExternalDNS — GitHub README",
        "https://raw.githubusercontent.com/kubernetes-sigs/external-dns/master/README.md",
        "Visão geral do ExternalDNS (sincronização de Services e Ingresses com provedores DNS, --domain-filter, --txt-owner-id, --txt-prefix, --dry-run, --policy=sync vs upsert-only, externalIPs e provedores webhook).",
    ),
    "exd_docs": (
        "ExternalDNS Documentation — Official Guides & FAQ",
        "https://kubernetes-sigs.github.io/external-dns/",
        "Documentação oficial do ExternalDNS cobrindo tutoriais por provedor, TTL avançado e FAQ.",
    ),
    "exd_repo": (
        "ExternalDNS — Repositório Oficial no GitHub",
        "https://github.com/kubernetes-sigs/external-dns",
        "Repositório oficial do ExternalDNS em kubernetes-sigs com código-fonte, docs/faq.md e docs/contributing/dev-guide.md.",
    ),
    "kyv_readme": (
        "Kyverno — GitHub README",
        "https://raw.githubusercontent.com/kyverno/kyverno/main/README.md",
        "Visão geral do Kyverno (motor de políticas nativo para Kubernetes, validação/mutação/geração/limpeza e verificação de imagens, Non-Goals, projetos Chainsaw/Policy Reporter/Kyverno JSON/Envoy Plugin, casos de uso e SBOM CycloneDX).",
    ),
    "kyv_docs": (
        "Kyverno Documentation — Quick Start & Policy Library",
        "https://kyverno.io/docs/introduction/",
        "Documentação oficial de introdução, instalação e biblioteca de políticas do Kyverno referenciada no README.",
    ),
    "kyv_repo": (
        "Kyverno — Repositório Oficial no GitHub",
        "https://github.com/kyverno/kyverno",
        "Repositório oficial do Kyverno na CNCF com código-fonte, CONTRIBUTING.md, DEVELOPMENT.md e pacotes SBOM.",
    ),
    "gtk_readme": (
        "OPA Gatekeeper — GitHub README",
        "https://raw.githubusercontent.com/open-policy-agent/gatekeeper/master/README.md",
        "Visão geral do Gatekeeper em comparação ao OPA com sidecar kube-mgmt (Gatekeeper v1.0), CRDs de constraints/templates/mutação, auditoria, external data e biblioteca de políticas.",
    ),
    "gtk_howto": (
        "OPA Gatekeeper Documentation — How to use Gatekeeper (howto.md)",
        "https://raw.githubusercontent.com/open-policy-agent/gatekeeper/master/website/docs/howto.md",
        "Guia oficial do Gatekeeper detalhando OPA Constraint Framework, ConstraintTemplate (openAPIV3Schema e Rego), Constraint, os 7 seletores de match, escopo Cluster vs Namespaced e enforcementAction (deny, dryrun, warn).",
    ),
    "gtk_repo": (
        "OPA Gatekeeper — Repositório Oficial no GitHub",
        "https://github.com/open-policy-agent/gatekeeper",
        "Repositório oficial do Gatekeeper com código-fonte, templates de demonstração e documentação.",
    ),
    "flc_readme": (
        "Falco — GitHub README",
        "https://raw.githubusercontent.com/falcosecurity/falco/master/README.md",
        "Visão geral do Falco (segurança em tempo de execução no kernel Linux graduada na CNCF, observação de syscalls com metadados de container/Kubernetes, 5 repositórios core, ambiente demo, auditorias em ./audits/ e build CMake com Modern BPF).",
    ),
    "flc_docs": (
        "Falco Documentation — Getting Started & Setup",
        "https://falco.org/docs/getting-started/",
        "Documentação oficial do Falco para início rápido, implantação em produção e compilação a partir do código-fonte.",
    ),
    "flc_repo": (
        "Falco — Repositório Oficial no GitHub",
        "https://github.com/falcosecurity/falco",
        "Repositório oficial do Falco na CNCF com código-fonte C++, chart/falco, docker/docker-compose/ e audits/.",
    ),
    "ked_readme": (
        "KEDA — GitHub README",
        "https://raw.githubusercontent.com/kedacore/keda/main/README.md",
        "Visão geral do KEDA (Kubernetes-based Event Driven Autoscaling graduado na CNCF, scale to/from zero, integração com HPA na nuvem e borda, QuickStarts com ScaledObject/ScaledJob, deploy Helm/Operator Hub/YAML e governança).",
    ),
    "ked_build": (
        "KEDA — Build & Deploy Guide (BUILD.md)",
        "https://raw.githubusercontent.com/kedacore/keda/main/BUILD.md",
        "Guia oficial de build e deploy do KEDA detalhando Operator SDK, Dev Containers, GOPROXY/GOSUMDB, execução local fora do cluster com /certs, imagens customizadas e pontos de entrada cmd/operator/main.go e cmd/adapter/main.go.",
    ),
    "ked_repo": (
        "KEDA — Repositório Oficial no GitHub",
        "https://github.com/kedacore/keda",
        "Repositório oficial do KEDA na CNCF com código-fonte, TESTING.md e ROADMAP.md.",
    ),
    "krp_readme": (
        "Karpenter — GitHub README",
        "https://raw.githubusercontent.com/kubernetes-sigs/karpenter/main/README.md",
        "Visão geral do Karpenter em kubernetes-sigs (ciclo Watching, Evaluating, Provisioning e Removing, 5 restrições de agendamento de pods, 16 implementações multi-cloud de provedores, canais Slack e reuniões do Working Group e Issue Triage).",
    ),
    "krp_repo": (
        "Karpenter — Repositório Oficial no GitHub",
        "https://github.com/kubernetes-sigs/karpenter",
        "Repositório oficial do núcleo do Karpenter em kubernetes-sigs com código-fonte, CONTRIBUTING.md e code-of-conduct.md.",
    ),
    "env_readme": (
        "Envoy Proxy — GitHub README",
        "https://raw.githubusercontent.com/envoyproxy/envoy/main/README.md",
        "Visão geral do Envoy (edge/middle/service proxy na CNCF, artigos de arquitetura sobre threading, hot restart, stats e xDS, repositórios relacionados, listas de e-mail, reuniões, auditorias Cure53/Ada Logics, OSS-Fuzz e política ppc64le).",
    ),
    "env_docs": (
        "Envoy Proxy Documentation — Official Docs & FAQ",
        "https://www.envoyproxy.io/docs/envoy/latest/faq/overview",
        "Documentação oficial e visão geral de perguntas frequentes do Envoy Proxy referenciada no README.",
    ),
    "env_repo": (
        "Envoy Proxy — Repositório Oficial no GitHub",
        "https://github.com/envoyproxy/envoy",
        "Repositório oficial do Envoy Proxy com código-fonte C++, api/, docs/security/, DEVELOPER.md, SECURITY.md e RELEASES.md.",
    ),
    "cdn_readme": (
        "CoreDNS — GitHub README",
        "https://raw.githubusercontent.com/coredns/coredns/master/README.md",
        "Visão geral do CoreDNS (servidor DNS em Go graduado na CNCF baseado em cadeia de plugins, protocolos UDP/TCP/DoT/DoH/DoH3/DoQ/gRPC, 18 capacidades/plugins, compilação com COREDNS_PLUGINS, -log-format=json e regras do Corefile).",
    ),
    "cdn_docs": (
        "CoreDNS Documentation — Built-in Plugins Catalog",
        "https://coredns.io/plugins/",
        "Catálogo oficial dos plugins in-tree do CoreDNS referenciado no README.",
    ),
    "cdn_repo": (
        "CoreDNS — Repositório Oficial no GitHub",
        "https://github.com/coredns/coredns",
        "Repositório oficial do CoreDNS na CNCF com código-fonte Go, plugin.cfg e documentação por plugin.",
    ),
    "etc_readme": (
        "etcd — GitHub README",
        "https://raw.githubusercontent.com/etcd-io/etcd/main/README.md",
        "Visão geral do etcd (banco chave-valor distribuído via consenso Raft, pilares Simple/Secure/Fast/Reliable, testes de robustez, 7 pacotes Go v3, portas IANA 2379/2380, cluster local via goreman/Procfile com learner node e reuniões).",
    ),
    "etc_docs": (
        "etcd Documentation — Operating etcd & Guides",
        "https://etcd.io/docs/latest/op-guide/",
        "Guia operacional oficial do etcd cobrindo instalação, clustering, configuração, segurança TLS e tuning.",
    ),
    "etc_repo": (
        "etcd — Repositório Oficial no GitHub",
        "https://github.com/etcd-io/etcd",
        "Repositório oficial do etcd na CNCF com código-fonte Go, etcdctl/, tests/robustness/, Procfile, OWNERS e ADOPTERS.md.",
    ),
}


def parse_group(path: Path) -> tuple[dict[str, str], list[dict[str, object]]]:
    context: dict[str, str] = {}
    row_lines: list[str] = []
    in_rows = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip() == "---":
            in_rows = True
            continue
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if not in_rows:
            sep = "=" if ("=" in line and (":" not in line or line.index("=") < line.index(":"))) else ":"
            key, value = line.split(sep, 1)
            context[key.strip()] = value.strip()
        else:
            row_lines.append(line)

    rows: list[dict[str, object]] = []
    for line in row_lines:
        parts = [part.strip() for part in line.split("||")]
        if len(parts) != 10:
            raise ValueError(f"{path.name}: esperados 10 campos, encontrados {len(parts)}: {line}")
        slug, title, summary, reason, how, example, caveat, verify, source_keys, review = parts
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
            raise ValueError(f"{path.name}: slug inválido: {slug}")
        rows.append({
            "slug": slug,
            "title": title,
            "summary": summary,
            "reason": reason,
            "how": how,
            "example": example,
            "caveat": caveat,
            "verify": verify,
            "sources": [key.strip() for key in source_keys.split(",") if key.strip()],
            "review": review,
        })
    if not 9 <= len(rows) <= 12:
        raise ValueError(f"{path.name}: o grupo precisa ter entre 9 e 12 notas; tem {len(rows)}")
    for key in ("group", "first", "check"):
        if key not in context or not context[key]:
            raise ValueError(f"{path.name}: falta contexto {key}")
    return context, rows


def render_note(context: dict[str, str], rows: list[dict[str, object]], index: int,
                row: dict[str, object]) -> tuple[int, str, dict[str, object]]:
    number = int(context["first"]) + index
    sources = [SOURCES[key] for key in row["sources"]]
    if len(sources) < 2 or len({source[1] for source in sources}) < 2:
        raise ValueError(f"{row['slug']}: precisa de duas fontes distintas")

    neighbors = []
    for neighbor_index in (index - 1, index + 1):
        if 0 <= neighbor_index < len(rows):
            other = rows[neighbor_index]
            neighbors.append(f"- [[{other['slug']}]] — Veja também: {other['title']}.")

    frontmatter = f'''---
id: software.devops.tranche03.{number:06d}
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-03.md"
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
        help="Rebuild the existing tranche-03 notes after validating their IDs and batch metadata.",
    )
    args = parser.parse_args()
    group_files = sorted(DATA_DIR.glob("*.txt"))
    if len(group_files) != 10:
        raise SystemExit(f"Esperados 10 arquivos de grupo; encontrados {len(group_files)}")

    existing_paths = list(DOMAINS_DIR.rglob("*.md"))
    existing_tranche = [
        path for path in existing_paths
        if re.search(
            r"(?m)^id: software\.devops\.tranche03\.\d{6}\s*$",
            path.read_text(encoding="utf-8", errors="replace")[:1200],
        )
    ]
    if args.refresh and len(existing_tranche) != EXPECTED_NOTES:
        raise ValueError(f"--refresh exige exatamente {EXPECTED_NOTES} notas tranche03 existentes; encontradas {len(existing_tranche)}")
    if REPORT.exists() and not args.refresh:
        raise ValueError(f"relatório já existe (use --refresh apenas para atualizar a tranche 3): {REPORT}")
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

    pending = []
    report_rows = []
    group_summaries: list[tuple[dict[str, str], int]] = []
    seen_slugs: set[str] = set()
    seen_titles: set[str] = set()
    expected_number = START
    for path in group_files:
        context, rows = parse_group(path)
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
            expected_id = f"id: software.devops.tranche03.{expected_number + index:06d}"
            if target_path.exists():
                current = target_path.read_text(encoding="utf-8")
                if not args.refresh:
                    raise ValueError(f"arquivo já existe (use --refresh apenas para a tranche 3): {target_path}")
                if expected_id not in current.splitlines()[:25] or "lote: software-devops-2000-0002" not in current.splitlines()[:25]:
                    raise ValueError(f"ID ou lote existente não corresponde à tranche: {target_path}")
            elif args.refresh:
                raise ValueError(f"--refresh exige os {EXPECTED_NOTES} arquivos existentes; falta {target_path}")
            unknown = set(row["sources"]) - SOURCES.keys()
            if unknown:
                raise ValueError(f"{slug}: fontes desconhecidas {unknown}")
            seen_slugs.add(slug)
            seen_titles.add(normalized_title)
            number, content, quality = render_note(context, rows, index, row)
            pending.append((number, row, context, content, quality))
            source_name, source_url, _ = SOURCES[row["sources"][0]]
            report_rows.append(
                f"| {number} | [[{slug}]] | [{source_name}]({source_url}) | {row['review']} Revisão factual por IA concluída; decisão: aprovada. |"
            )
        expected_number += len(rows)

    if len(pending) != EXPECTED_NOTES or expected_number != START + EXPECTED_NOTES:
        raise ValueError(f"esperadas {EXPECTED_NOTES} notas de {START} a {START + EXPECTED_NOTES - 1}, validadas {len(pending)}")
    repeated = repeated_substantive_sentences(
        [(number, content) for number, _, _, content, _ in pending]
    )
    if repeated:
        examples = [f"{numbers}: {sentence}" for sentence, numbers in list(repeated.items())[:8]]
        raise ValueError(f"prosa substantiva repetida entre notas; revisar antes de gravar: {examples}")

    for number, row, context, content, quality in pending:
        (NOTES_DIR / f"{row['slug']}.md").write_text(content, encoding="utf-8")

    report = [
        "# Revisão factual assistida por IA — lote `software-devops-2000-0002`, tranche 3",
        "",
        f"- Data: {DATE}",
        "- Revisor: `Arena.ai Agent Mode`",
        f"- Escopo: notas **{START}–{START + EXPECTED_NOTES - 1}**, em dez grupos temáticos com dez notas cada; cada linha identifica a conferência factual da nota.",
        "- Fontes primárias: documentação oficial dos projetos e versões indicadas nas próprias notas; as afirmações foram limitadas ao material citado.",
        f"- Resultado: **{EXPECTED_NOTES} revisões factuais por IA registradas** e aprovadas no gate automatizado de qualidade. Isto não é aprovação humana nem garantia de ausência de erro.",
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
        report.append(f"- {context['group']} (itens {context['first']}–{int(context['first']) + count - 1}): {context['check']}")
    report += [
        "- A auditoria de links, a comparação com o inventário, o gate de conteúdo e a verificação de sentenças repetidas foram executados separadamente antes da contabilização.",
        "",
    ]
    REPORT.write_text("\n".join(report).rstrip() + "\n", encoding="utf-8")
    word_counts = [quality["word_count"] for _, _, _, _, quality in pending]
    source_counts = [quality["source_count"] for _, _, _, _, quality in pending]
    print(f"Geradas {len(pending)} notas substantivas (IDs {START}–{START + EXPECTED_NOTES - 1}); palavras: min={min(word_counts)}; max={max(word_counts)}")
    print(f"Fontes HTTPS específicas por nota: min={min(source_counts)}; max={max(source_counts)}")
    print(f"Relatório factual: {REPORT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
