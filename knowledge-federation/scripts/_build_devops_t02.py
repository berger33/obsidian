#!/usr/bin/env python3
"""Build the source-backed software-devops batch 2 tranche 2 (notes 101–200)."""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "knowledge-federation" / "scripts" / "_devops_t02_data"
NOTES_DIR = ROOT / "knowledge-federation" / "domains" / "software-0008" / "software" / "devops"
DOMAINS_DIR = ROOT / "knowledge-federation" / "domains"
REPORT = ROOT / "knowledge-federation" / "exports" / "reports" / "ai-review-software-devops-2000-0002-tranche-02.md"
DATE = date.today().isoformat()
START = 101
EXPECTED_NOTES = 100

sys.path.insert(0, str(ROOT / "knowledge-federation" / "scripts"))
from note_quality import assess_markdown, normalize  # noqa: E402
from prose_audit import repeated_substantive_sentences  # noqa: E402

SOURCES = {
    "xpl_readme": (
        "Crossplane — GitHub README",
        "https://raw.githubusercontent.com/crossplane/crossplane/main/README.md",
        "Visão geral do Crossplane como framework de control planes cloud-native na CNCF, tabela de releases e EOL (v1.20 e v2.2–v2.7), roadmap, reuniões e 14 SIGs.",
    ),
    "xpl_docs": (
        "Crossplane Documentation — Get Started with Composition",
        "https://docs.crossplane.io/latest/get-started/get-started-with-composition",
        "Documentação oficial de introdução ao Crossplane, instalação e quickstarts de recursos e composição referenciada no README.",
    ),
    "xpl_repo": (
        "Crossplane — Repositório Oficial no GitHub",
        "https://github.com/crossplane/crossplane",
        "Repositório oficial do Crossplane com código-fonte, ADOPTERS.md, contributing/README.md e notas de release.",
    ),
    "vel_readme": (
        "Velero — GitHub README",
        "https://raw.githubusercontent.com/vmware-tanzu/velero/main/README.md",
        "Visão geral do Velero para backup, restore e migração de recursos e volumes Kubernetes, matriz de compatibilidade (1.14–1.18), teste de upgrade N-2 e suporte IPv4/IPv6/dual-stack.",
    ),
    "vel_arch": (
        "Velero — Architecture Guide (ARCHITECTURE.md)",
        "https://raw.githubusercontent.com/vmware-tanzu/velero/main/ARCHITECTURE.md",
        "Guia oficial de arquitetura do Velero cobrindo servidor em réplica única, cliente CLI, file-system backup, data mover CSI, provider plugins e diretório design/.",
    ),
    "vel_repo": (
        "Velero — Repositório Oficial no GitHub",
        "https://github.com/vmware-tanzu/velero",
        "Repositório oficial do Velero com código-fonte, propostas de design implementadas e notas de versão.",
    ),
    "cil_readme": (
        "Cilium — GitHub README.rst",
        "https://raw.githubusercontent.com/cilium/cilium/main/README.rst",
        "Visão geral do Cilium (dataplane eBPF, CNI overlay/native/BGP, substituição do kube-proxy, Cluster Mesh, Network Policy L3-L7/DNS, Service Mesh, Hubble, releases estáveis, SBOM SPDX e licenças).",
    ),
    "cil_docs": (
        "Cilium Documentation — Architecture and Component Overview",
        "https://docs.cilium.io/en/stable/overview/component-overview/",
        "Documentação oficial de arquitetura, requisitos de sistema e operação do Cilium referenciada no README.",
    ),
    "cil_repo": (
        "Cilium — Repositório Oficial no GitHub",
        "https://github.com/cilium/cilium",
        "Repositório oficial do Cilium graduado na CNCF com código-fonte, templates BPF, USERS.md e MAINTAINERS.md.",
    ),
    "lkd_readme": (
        "Linkerd2 — GitHub README",
        "https://raw.githubusercontent.com/linkerd/linkerd2/main/README.md",
        "Visão geral do Linkerd como service mesh ultraleve e security-first na CNCF, layout dos 5 repositórios, auditorias de segurança em audits/, Steering Committee e licença Apache 2.0.",
    ),
    "lkd_build": (
        "Linkerd2 — Development and Architecture Guide (BUILD.md)",
        "https://raw.githubusercontent.com/linkerd/linkerd2/main/BUILD.md",
        "Guia oficial de arquitetura e build do Linkerd2 detalhando control plane em Go/React (destination, proxy-injector, identity), extensões viz e multicluster, data plane em Rust e flags de tracing.",
    ),
    "lkd_docs": (
        "Linkerd Documentation — Getting Started Guide",
        "https://linkerd.io/2/getting-started/",
        "Guia oficial de início rápido do Linkerd 2.x para Kubernetes referenciado no README e em BUILD.md.",
    ),
    "hbr_readme": (
        "Harbor — GitHub README",
        "https://raw.githubusercontent.com/goharbor/harbor/main/README.md",
        "Visão geral do Harbor como registro cloud-native na CNCF, features (RBAC, replicação, scan, LDAP/OIDC, GC, auditoria, API REST), instalação e verificação de assinatura com Cosign (v2.15.0+).",
    ),
    "hbr_docs": (
        "Harbor Documentation — Installation & Configuration Guide",
        "https://goharbor.io/docs/latest/install-config/",
        "Guia oficial de instalação, configuração e matriz de compatibilidade do Harbor referenciada no README.",
    ),
    "hbr_repo": (
        "Harbor — Repositório Oficial no GitHub",
        "https://github.com/goharbor/harbor",
        "Repositório oficial do Harbor com código-fonte, api/v2.0/swagger.yaml, docs/signature-verification.md e releases.",
    ),
    "thn_readme": (
        "Thanos — GitHub README",
        "https://raw.githubusercontent.com/thanos-io/thanos/main/README.md",
        "Visão geral do Thanos (CNCF Incubating), objetivos sobre o formato Prometheus 2.0, deduplicação HA, Store API gRPC, arquiteturas Sidecar vs Receive, filosofia UNIX/Go e releases a cada 6 semanas.",
    ),
    "thn_docs": (
        "Thanos Documentation — Getting Started & Design",
        "https://thanos.io/tip/thanos/getting-started.md/",
        "Documentação oficial de introdução e design arquitetural do Thanos referenciada no README.",
    ),
    "thn_repo": (
        "Thanos — Repositório Oficial no GitHub",
        "https://github.com/thanos-io/thanos",
        "Repositório oficial do Thanos com código-fonte em Go, docs/proposals-done, docs/integrations.md e website/data/adopters.yml.",
    ),
    "lok_readme": (
        "Grafana Loki — GitHub README",
        "https://raw.githubusercontent.com/grafana/loki/main/README.md",
        "Visão geral do Loki (agregação de logs indexada por labels no estilo Prometheus), pilha Alloy + Loki + Grafana, migração do Helm chart em março de 2026, LogCLI, Loki Canary e build a partir do fonte.",
    ),
    "lok_docs": (
        "Grafana Loki Documentation — Get Started & Operations",
        "https://grafana.com/docs/loki/latest/get-started/",
        "Documentação oficial do Grafana Loki cobrindo instalação, Grafana Alloy, labels, LogCLI e Loki Canary.",
    ),
    "lok_repo": (
        "Grafana Loki — Repositório Oficial no GitHub",
        "https://github.com/grafana/loki",
        "Repositório oficial do Grafana Loki com código-fonte em Go, cmd/loki/loki-local-config.yaml e Makefile.",
    ),
    "flb_readme": (
        "Fluent Bit — GitHub README",
        "https://raw.githubusercontent.com/fluent/fluent-bit/master/README.md",
        "Visão geral do Fluent Bit (agente graduado na CNCF para Logs, Metrics e Traces), suporte multi-plataforma, ciclo de 3–4 meses (v5.1), 70+ plugins, SQL Stream Processing, extensibilidade C/Lua/Go e build CMake.",
    ),
    "flb_docs": (
        "Fluent Bit Official Documentation — Pipeline Inputs, Filters & Outputs",
        "https://docs.fluentbit.io/manual/pipeline/inputs",
        "Documentação oficial dos plugins de Input, Filter e Output e guias de instalação do Fluent Bit.",
    ),
    "flb_repo": (
        "Fluent Bit — Repositório Oficial no GitHub",
        "https://github.com/fluent/fluent-bit",
        "Repositório oficial do Fluent Bit com código-fonte, MAINTENANCE.md, DEVELOPER_GUIDE.md e workflows de CI.",
    ),
    "vec_readme": (
        "Vector — GitHub README",
        "https://raw.githubusercontent.com/vectordotdev/vector/master/README.md",
        "Visão geral do Vector (pipeline de observabilidade em Rust para agent e aggregator), princípios, 5 casos de uso, escala na comunidade (500 TB/dia) e tabelas de performance e corretude.",
    ),
    "vec_docs": (
        "Vector Documentation — Quickstart & Components",
        "https://vector.dev/docs/setup/quickstart/",
        "Documentação oficial do Vector para configuração de sources, transforms e sinks referenciada no README.",
    ),
    "vec_repo": (
        "Vector — Repositório Oficial no GitHub",
        "https://github.com/vectordotdev/vector",
        "Repositório oficial do Vector em Rust com código-fonte, workflows de integração e links de políticas.",
    ),
    "skf_readme": (
        "Skaffold — GitHub README",
        "https://raw.githubusercontent.com/GoogleContainerTools/skaffold/main/README.md",
        "Visão geral do Skaffold (desenvolvimento contínuo para Kubernetes e blocos de CI/CD), features (source-to-deploy, skaffold render, skaffold init, client-side only), Cloud Code e Deprecation Policy.",
    ),
    "skf_docs": (
        "Skaffold Documentation — Install & Deprecation Policy",
        "https://skaffold.dev/docs/install/",
        "Documentação oficial de instalação, fases do pipeline e política de depreciação do Skaffold.",
    ),
    "skf_repo": (
        "Skaffold — Repositório Oficial no GitHub",
        "https://github.com/GoogleContainerTools/skaffold",
        "Repositório oficial do Skaffold com código-fonte, diretório examples/, SECURITY.md e security advisories.",
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

    if "check" not in context:
        context["check"] = (
            f"Conferi {context.get('source_scope', 'a documentação primária oficial')} "
            f"(cobrindo {context.get('area', context.get('group', ''))}) antes de redigir as dez notas."
        )

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
id: software.devops.tranche02.{number:06d}
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-02.md"
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
        help="Rebuild the existing tranche-02 notes after validating their IDs and batch metadata.",
    )
    args = parser.parse_args()
    group_files = sorted(DATA_DIR.glob("*.txt"))
    if len(group_files) != 10:
        raise SystemExit(f"Esperados 10 arquivos de grupo; encontrados {len(group_files)}")

    existing_paths = list(DOMAINS_DIR.rglob("*.md"))
    existing_tranche = [
        path for path in existing_paths
        if re.search(
            r"(?m)^id: software\.devops\.tranche02\.\d{6}\s*$",
            path.read_text(encoding="utf-8", errors="replace")[:1200],
        )
    ]
    if args.refresh and len(existing_tranche) != EXPECTED_NOTES:
        raise ValueError(f"--refresh exige exatamente {EXPECTED_NOTES} notas tranche02 existentes; encontradas {len(existing_tranche)}")
    if REPORT.exists() and not args.refresh:
        raise ValueError(f"relatório já existe (use --refresh apenas para atualizar a tranche 2): {REPORT}")
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
            expected_id = f"id: software.devops.tranche02.{expected_number + index:06d}"
            if target_path.exists():
                current = target_path.read_text(encoding="utf-8")
                if not args.refresh:
                    raise ValueError(f"arquivo já existe (use --refresh apenas para a tranche 2): {target_path}")
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
        "# Revisão factual assistida por IA — lote `software-devops-2000-0002`, tranche 2",
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
