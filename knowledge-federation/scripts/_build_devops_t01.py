#!/usr/bin/env python3
"""Build the source-backed software-devops batch 2 tranche 1 (notes 1–100)."""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "knowledge-federation" / "scripts" / "_devops_t01_data"
NOTES_DIR = ROOT / "knowledge-federation" / "domains" / "software-0008" / "software" / "devops"
DOMAINS_DIR = ROOT / "knowledge-federation" / "domains"
REPORT = ROOT / "knowledge-federation" / "exports" / "reports" / "ai-review-software-devops-2000-0002-tranche-01.md"
DATE = date.today().isoformat()
START = 1
EXPECTED_NOTES = 100

sys.path.insert(0, str(ROOT / "knowledge-federation" / "scripts"))
from note_quality import assess_markdown, normalize  # noqa: E402
from prose_audit import repeated_substantive_sentences  # noqa: E402

SOURCES = {
    "otc_readme": ('OpenTelemetry Collector — README oficial', 'https://raw.githubusercontent.com/open-telemetry/opentelemetry-collector/main/README.md', 'README oficial do OpenTelemetry Collector com proposta vendor-agnostic, cinco objetivos, versão OTLP v1.10.0, política de versões menores N e N-2 do Go, verificação cosign e governança do SIG.'),
    "otc_stability": ('OpenTelemetry Collector — Stability Levels and versioning', 'https://raw.githubusercontent.com/open-telemetry/opentelemetry-collector/main/docs/component-stability.md', 'Documento oficial docs/component-stability.md com os seis níveis de estabilidade por sinal, regras de depreciação em Beta/Stable (N+2 ou 6 meses) e requisitos de testes em Stable.'),
    "otc_repo": ('Repositório oficial open-telemetry/opentelemetry-collector', 'https://github.com/open-telemetry/opentelemetry-collector', 'Repositório oficial do OpenTelemetry Collector no GitHub com docs/vision.md, docs/security-best-practices.md, código-fonte e releases.'),
    "acd_readme": ('Argo CD — README oficial', 'https://raw.githubusercontent.com/argoproj/argo-cd/master/README.md', 'README oficial do Argo CD com definição GitOps para Kubernetes, os dois motivos centrais em Why Argo CD?, USERS.md, documentação, live demo, integrações do ecossistema e canais da comunidade.'),
    "acd_start": ('Argo CD — Getting Started (docs/getting_started.md)', 'https://raw.githubusercontent.com/argoproj/argo-cd/master/docs/getting_started.md', 'Guia oficial Getting Started do Argo CD: instalação com --server-side --force-conflicts (limite de 262 KB), modo core, segredo argocd-redis, LoadBalancer/Ingress/port-forward, argocd-initial-admin-secret e argocd cluster add.'),
    "acd_repo": ('Repositório oficial argoproj/argo-cd', 'https://github.com/argoproj/argo-cd', 'Repositório oficial do Argo CD no GitHub com manifests/, docs/, USERS.md e releases SLSA 3.'),
    "hlm_readme": ('Helm — README oficial', 'https://raw.githubusercontent.com/helm/helm/main/README.md', 'README oficial do Helm com definição de Charts, cinco casos de uso, Chart.yaml e templates/, suporte Helm v4 (main) vs Helm v3 (dev-v3 até jul/nov 2026), sete gerenciadores de pacotes, roadmap e canais da comunidade.'),
    "hlm_repo": ('Repositório oficial helm/helm', 'https://github.com/helm/helm', 'Repositório oficial do Helm no GitHub com código-fonte v4, milestones, CONTRIBUTING.md, code-of-conduct.md e releases.'),
    "hlm_quickstart": ('Helm — Quick Start Guide oficial', 'https://helm.sh/docs/intro/quickstart/', 'Guia oficial de início rápido do Helm sobre criação, instalação, upgrade e gerenciamento de Charts e releases.'),
    "otf_readme": ('OpenTofu — README oficial', 'https://raw.githubusercontent.com/opentofu/opentofu/main/README.md', 'README oficial do OpenTofu com definição OSS, quatro Key features (IaC, Execution Plans, Resource Graph e Change Automation), Nightly Builds (30 dias e latest.json), Security Policy, liaison@opentofu.org, Registry Policy, reuniões e licença MPL-2.0.'),
    "otf_repo": ('Repositório oficial opentofu/opentofu', 'https://github.com/opentofu/opentofu', 'Repositório oficial do OpenTofu no GitHub com código-fonte, RELEASE.md, CONTRIBUTING.md e LICENSE (MPL-2.0).'),
    "otf_install": ('OpenTofu — Installing OpenTofu (documentação oficial)', 'https://opentofu.org/docs/intro/install', 'Guia oficial de introdução e instalação do OpenTofu na documentação oficial opentofu.org.'),
    "ans_readme": ('Ansible — README oficial (branch devel)', 'https://raw.githubusercontent.com/ansible/ansible/devel/README.md', 'README oficial do Ansible com seis frentes de automação, nove princípios de design (agentless sobre SSH, zero bootstrap, non-root), instalação via pip/package manager, branches devel vs stable-2.X, Ansible Forum/Matrix/Bullhorn, context/, criador e licença GPL v3.0+.'),
    "ans_repo": ('Repositório oficial ansible/ansible', 'https://github.com/ansible/ansible', 'Repositório oficial do ansible-core no GitHub com diretório context/, COPYING (GPL v3.0+) e .github/CONTRIBUTING.md.'),
    "ans_install": ('Ansible — Installation Guide oficial', 'https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html', 'Guia oficial de instalação do Ansible em múltiplas plataformas via pip e gerenciadores de pacotes.'),
    "flx_readme": ('Flux v2 — README oficial', 'https://raw.githubusercontent.com/fluxcd/flux2/main/README.md', 'README oficial do Flux v2 com sincronização Git/OCI, integração Prometheus, multi-tenancy, GitOps Toolkit, as cinco famílias de controladores e todos os seus CRDs, quatro guias práticos e diretrizes de suporte.'),
    "flx_repo": ('Repositório oficial fluxcd/flux2', 'https://github.com/fluxcd/flux2', 'Repositório oficial do Flux v2 no GitHub com código-fonte, diagramas de arquitetura, CONTRIBUTING.md e releases SLSA 3.'),
    "flx_start": ('Flux — Get Started e documentação oficial', 'https://fluxcd.io/flux/get-started/', 'Guia oficial Get Started do Flux v2 para bootstrap em clusters Kubernetes e entrega contínua GitOps.'),
    "kst_readme": ('Kustomize — README oficial', 'https://raw.githubusercontent.com/kubernetes-sigs/kustomize/master/README.md', 'README oficial do Kustomize com customização YAML template-free (analogia make/sed), matriz de versões embutidas no kubectl, kustomization.yaml com labels/includeSelectors/configMapGenerator, kustomize build e overlays com patches.'),
    "kst_repo": ('Repositório oficial kubernetes-sigs/kustomize', 'https://github.com/kubernetes-sigs/kustomize', 'Repositório oficial do Kustomize no GitHub (sig-cli) com examples/, proposals/ e releases.'),
    "kst_docs": ('Kustomize — documentação oficial de referência', 'https://kubectl.docs.kubernetes.io/references/kustomize/', 'Documentação oficial de referência e glossário do Kustomize mantida pelo sig-cli do Kubernetes.'),
    "ctd_readme": ('containerd — README oficial', 'https://raw.githubusercontent.com/containerd/containerd/main/README.md', 'README oficial do containerd com arquitetura para Linux/Windows, guias ops/namespaces/client-opts, requisitos runc/hcsshim e kernel 4.x vs 3.18 btrfs, criu, OCI Distribution e hosts.md, autocompletar ctr, plugin CRI GA com critest/crictl e licenças.'),
    "ctd_repo": ('Repositório oficial containerd/containerd', 'https://github.com/containerd/containerd', 'Repositório oficial do containerd no GitHub com docs/, RELEASES.md, BUILDING.md e ADOPTERS.md.'),
    "ctd_pkgdoc": ('Pacote containerd v2 no pkg.go.dev', 'https://pkg.go.dev/github.com/containerd/containerd/v2', 'Referência oficial da biblioteca Go github.com/containerd/containerd/v2 no pkg.go.dev.'),
    "jgr_readme": ('Jaeger — README oficial', 'https://raw.githubusercontent.com/jaegertracing/jaeger/main/README.md', 'README oficial do Jaeger com Jaeger v2, Quick Start Docker all-in-one (portas 16686, 4317 e 4318), diagrama de arquitetura, garantia de depreciação (3 meses ou 2 versões menores), política Go (N) e matriz de suporte a Elasticsearch/OpenSearch/Cassandra/ClickHouse.'),
    "jgr_repo": ('Repositório oficial jaegertracing/jaeger', 'https://github.com/jaegertracing/jaeger', 'Repositório oficial do Jaeger no GitHub com código-fonte, GOVERNANCE.md, MAINTAINERS.md, CONTRIBUTING.md e ADOPTERS.md.'),
    "jgr_start": ('Jaeger — Getting Started Guide oficial', 'https://www.jaegertracing.io/docs/latest/getting-started/', 'Guia oficial Getting Started da documentação do Jaeger para implantação e uso da plataforma de tracing distribuído.'),
    "tkt_readme": ('Tekton Pipelines — README oficial', 'https://raw.githubusercontent.com/tektoncd/pipeline/main/README.md', 'README oficial do Tekton Pipelines com os três pilares (Cloud Native, Decoupled e Typed), tabela de versão mínima do Kubernetes (até v0.61.x -> K8s 1.28+), api_compatibility_policy.md, deprecations.md e guias de migração para v1.'),
    "tkt_docs": ('Tekton Pipelines — Tasks and Pipelines (docs/README.md)', 'https://raw.githubusercontent.com/tektoncd/pipeline/main/docs/README.md', 'Visão geral oficial em docs/README.md com a tabela das seis entidades (Task, TaskRun, Pipeline, PipelineRun, PipelineResource Deprecated e Run alpha), os 13 guias temáticos e licenças CC-BY-4.0 / Apache 2.0.'),
    "tkt_repo": ('Repositório oficial tektoncd/pipeline', 'https://github.com/tektoncd/pipeline', 'Repositório oficial do Tekton Pipelines no GitHub com docs/, examples/, DEVELOPMENT.md e releases.md.'),
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
            key, value = line.split("=", 1)
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
id: software.devops.tranche01.{number:06d}
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-25.md"
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
        help="Rebuild the existing tranche-25 notes after validating their IDs and batch metadata.",
    )
    args = parser.parse_args()
    group_files = sorted(DATA_DIR.glob("*.txt"))
    if len(group_files) != 10:
        raise SystemExit(f"Esperados 10 arquivos de grupo; encontrados {len(group_files)}")

    existing_paths = list(DOMAINS_DIR.rglob("*.md"))
    existing_tranche = [
        path for path in existing_paths
        if re.search(
            r"(?m)^id: software\.devops\.tranche01\.\d{6}\s*$",
            path.read_text(encoding="utf-8", errors="replace")[:1200],
        )
    ]
    if args.refresh and len(existing_tranche) != EXPECTED_NOTES:
        raise ValueError(f"--refresh exige exatamente {EXPECTED_NOTES} notas tranche01 existentes; encontradas {len(existing_tranche)}")
    if REPORT.exists() and not args.refresh:
        raise ValueError(f"relatório já existe (use --refresh apenas para atualizar a tranche 1): {REPORT}")
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
            expected_id = f"id: software.devops.tranche01.{expected_number + index:06d}"
            if target_path.exists():
                current = target_path.read_text(encoding="utf-8")
                if not args.refresh:
                    raise ValueError(f"arquivo já existe (use --refresh apenas para a tranche 1): {target_path}")
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

    # All notes and metadata pass their deterministic gates before any file is written.
    for number, row, context, content, quality in pending:
        (NOTES_DIR / f"{row['slug']}.md").write_text(content, encoding="utf-8")

    report = [
        "# Revisão factual assistida por IA — lote `software-devops-2000-0002`, tranche 1",
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
