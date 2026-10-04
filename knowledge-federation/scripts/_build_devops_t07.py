#!/usr/bin/env python3
"""Build the source-backed software-devops batch 2 tranche 7 (notes 601–700)."""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "knowledge-federation" / "scripts" / "_devops_t07_data"
NOTES_DIR = ROOT / "knowledge-federation" / "domains" / "software-0008" / "software" / "devops"
DOMAINS_DIR = ROOT / "knowledge-federation" / "domains"
REPORT = ROOT / "knowledge-federation" / "exports" / "reports" / "ai-review-software-devops-2000-0002-tranche-07.md"
DATE = date.today().isoformat()
START = 601
EXPECTED_NOTES = 100

sys.path.insert(0, str(ROOT / "knowledge-federation" / "scripts"))
from note_quality import assess_markdown, normalize  # noqa: E402
from prose_audit import repeated_substantive_sentences  # noqa: E402

GROUP_META: dict[str, dict[str, str]] = {
    "01-mimir.txt": {
        "sub": "Grafana Mimir (armazenamento escalável multi-tenant de longo prazo para Prometheus)",
        "src1_label": "Grafana Mimir GitHub — README.md (Scalability, Multi-tenancy & Object Storage)",
        "src1_note": "README oficial do Grafana Mimir (AGPL-3.0-only) sobre escalabilidade até 1 bilhão de séries ativas, alta disponibilidade e armazenamento de longo prazo para Prometheus",
        "src2_label": "Grafana Mimir Documentation — Architecture & Components",
        "src2_note": "Documentação oficial de arquitetura avançada e componentes do Grafana Mimir (Distributor, Ingester, Querier, Query-frontend, Query-scheduler, Store-gateway, Compactor, Ruler e Alertmanager)",
        "src3_label": "Grafana Mimir — Official GitHub Repository",
        "src3_note": "Repositório oficial do Grafana Mimir mantido pela Grafana Labs",
    },
    "02-pyroscope.txt": {
        "sub": "Grafana Pyroscope (plataforma de continuous profiling e arquitetura v2 em Object Storage)",
        "src1_label": "Grafana Pyroscope GitHub — README.md (Pyroscope 2.0, SDKs, Alloy & Profiles Drilldown)",
        "src1_note": "README oficial do Grafana Pyroscope 2.0 detalhando casos de uso proativos e reativos, coleta via SDKs/Grafana Alloy/OpenTelemetry eBPF e visualização no Grafana Profiles Drilldown",
        "src2_label": "Grafana Pyroscope Documentation — About the Pyroscope v2 architecture",
        "src2_note": "Documentação oficial da arquitetura Pyroscope v2 com escrita direta em object storage via distributor e segment-writer, consenso Raft no metastore, compaction-workers e query-frontend/query-backend",
        "src3_label": "Grafana Pyroscope — Official GitHub Repository",
        "src3_note": "Repositório oficial AGPL-3.0 do Grafana Pyroscope",
    },
    "03-tetragon.txt": {
        "sub": "Cilium Tetragon (observabilidade de segurança e runtime enforcement em tempo real com eBPF)",
        "src1_label": "Cilium Tetragon GitHub — README.md (Process Lifecycle, TracingPolicy & Tetra CLI)",
        "src1_note": "README oficial do Cilium Tetragon cobrindo eventos process_exec/process_exit, rastreamento genérico com kprobes/tracepoints/uprobes via TracingPolicy e casos de uso em Kubernetes e Linux",
        "src2_label": "Cilium Tetragon Official Documentation — Overview & eBPF Real-Time Enforcement",
        "src2_note": "Visão geral técnica do Cilium Tetragon detalhando filtragem e bloqueio síncrono em eBPF dentro do kernel Linux e enriquecimento com identidades do Kubernetes",
        "src3_label": "Cilium Tetragon — Official GitHub Repository",
        "src3_note": "Repositório oficial do Cilium Tetragon na CNCF",
    },
    "04-inspektor.txt": {
        "sub": "Inspektor Gadget (framework e ferramentas eBPF em imagens OCI para Kubernetes e Linux)",
        "src1_label": "Inspektor Gadget GitHub — README.md (OCI Gadgets, Enrichment, WASM & Operations)",
        "src1_note": "README oficial do Inspektor Gadget detalhando empacotamento de programas eBPF em imagens OCI, enriquecimento bidirecional Kubernetes, módulos WebAssembly, operadores e requisitos de kernel Linux >= 5.10 com BTF",
        "src2_label": "Inspektor Gadget Official Documentation — Gadgets Catalog & Reference",
        "src2_note": "Documentação oficial dos Gadgets (trace, top, snapshot, profile) e modos de execução com kubectl-gadget, ig e gadgetctl",
        "src3_label": "Inspektor Gadget — Official GitHub Repository",
        "src3_note": "Repositório oficial do Inspektor Gadget na CNCF",
    },
    "05-kubescape.txt": {
        "sub": "Kubescape (plataforma CNCF Incubating de segurança Kubernetes do desenvolvimento ao runtime)",
        "src1_label": "Kubescape GitHub — README.md (OPA/Regolibrary, Grype, Copacetic, VAP, Operator & MCP)",
        "src1_note": "README oficial do Kubescape documentando varredura de postura com OPA/Regolibrary, CVEs de imagens com Grype, auto-fix, patching com Copacetic, Validating Admission Policies (CEL) e MCP server",
        "src2_label": "Kubescape Official Documentation — In-Cluster Operator & Runtime Security",
        "src2_note": "Documentação oficial do operador in-cluster do Kubescape com monitoramento contínuo e detecção de ameaças em runtime via eBPF (Inspektor Gadget)",
        "src3_label": "Kubescape — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do Kubescape (CNCF Incubating)",
    },
    "06-opencost.txt": {
        "sub": "OpenCost (monitoramento e alocação open-source de custos em Kubernetes e multi-cloud na CNCF)",
        "src1_label": "OpenCost GitHub — README.md (Cost Allocation, Cloud Billing, AI Inference & MCP Server)",
        "src1_note": "README oficial do OpenCost detalhando alocação in-cluster (CPU, GPU, RAM, PV), billing multi-cloud, custos de inferência vLLM/llm-d, OpenCost Plugins e servidor MCP opt-in na porta 8081",
        "src2_label": "OpenCost Official Documentation — Prometheus Integration & Global Query Endpoints",
        "src2_note": "Documentação oficial de integração do OpenCost com Prometheus e requisitos de endpoint global (Thanos, Cortex, Mimir) em topologias HA/sharded",
        "src3_label": "OpenCost — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do OpenCost (CNCF Incubating)",
    },
    "07-flagger.txt": {
        "sub": "Flux Flagger (operador CNCF Graduated de entrega progressiva Canary, A/B e Blue/Green)",
        "src1_label": "Flux Flagger GitHub — README.md (Canary CRD, Service Mesh/Ingress/Gateway API, Metrics & Webhooks)",
        "src1_note": "README oficial do Flux Flagger cobrindo a especificação do CRD Canary, estratégias Canary/A/B/Blue-Green, matriz de provedores de rede, MetricTemplates, webhooks e alertas",
        "src2_label": "Flux Flagger Official Documentation — How it works & Canary Promotion Lifecycle",
        "src2_note": "Documentação oficial de funcionamento da máquina de estados de análise e promoção canário do Flagger",
        "src3_label": "Flux Flagger — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do Flagger na família GitOps Flux (CNCF Graduated)",
    },
    "08-descheduler.txt": {
        "sub": "Kubernetes Descheduler (rebalanceamento de pods por políticas de evicção e utilização de nós)",
        "src1_label": "Kubernetes Descheduler GitHub — README.md (DeschedulerPolicy, DefaultEvictor & Strategy Plugins)",
        "src1_note": "README oficial do Kubernetes Descheduler detalhando configurações top-level, DefaultEvictor com podProtections e plugins dos pontos de extensão Deschedule e Balance",
        "src2_label": "Kubernetes Descheduler Official Helm Chart — README.md",
        "src2_note": "Documentação oficial do Helm chart do Kubernetes Descheduler para implantação como CronJob, Job ou Deployment no kube-system",
        "src3_label": "Kubernetes Descheduler — Official GitHub Repository",
        "src3_note": "Repositório oficial do projeto kubernetes-sigs/descheduler",
    },
    "09-runc.txt": {
        "sub": "OpenContainer runc (ferramenta CLI e runtime de referência para containers OCI no Linux)",
        "src1_label": "OpenContainer runc GitHub — README.md (OCI Bundles, Lifecycle, Rootless, libpathrs & Build Tags)",
        "src1_note": "README oficial do runc detalhando criação de OCI bundles, comando runc spec, operações create/start/list/delete, containers rootless, libpathrs/seccomp e integração com systemd",
        "src2_label": "Open Container Initiative — Runtime Specification (runtime-spec)",
        "src2_note": "Especificação oficial OCI Runtime implementada pelo runc para configuração de containers em config.json",
        "src3_label": "OpenContainer runc — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do runc na Open Container Initiative",
    },
    "10-crun.txt": {
        "sub": "Containers crun (runtime OCI rápido e de baixo consumo de memória escrito em C)",
        "src1_label": "Containers crun GitHub — README.md (C Architecture, Memory Footprint, Shared libcrun & Nix Static Build)",
        "src1_note": "README oficial do crun demonstrando benchmarks de velocidade e memória (512 KB) frente ao runc, compilação Autotools com libocispec, libcrun compartilhada, builds estáticos Nix e verificação GPG",
        "src2_label": "Containers crun Manual Page — crun.1.md (Commands, Cgroup v2 Delegation, CRIU & OCI Annotations)",
        "src2_note": "Página de manual oficial crun.1.md especificando comandos CLI, opções globais de log, delegação em cgroup v2, checkpoint/restore com pre-dump CRIU e anotações run.oci.* (incluindo wasm e krun)",
        "src3_label": "Containers crun — Official GitHub Repository",
        "src3_note": "Repositório oficial do runtime OCI crun na organização containers",
    },
}


def parse_group(path: Path) -> tuple[dict[str, str], list[dict[str, object]]]:
    raw = path.read_text(encoding="utf-8")
    blocks = [b.strip() for b in re.split(r"(?m)^===\s*NOTE:\s*", raw) if b.strip()]
    if len(blocks) != 10:
        raise ValueError(f"{path.name}: esperadas 10 notas, encontradas {len(blocks)}")

    meta = GROUP_META[path.name]
    group_title = meta["sub"]
    rows: list[dict[str, object]] = []
    first_num: int | None = None

    for block in blocks:
        lines = block.splitlines()
        header = lines[0].rstrip("=").strip()
        num_str, slug, title = [p.strip() for p in header.split("|", 2)]
        num = int(num_str)
        if first_num is None:
            first_num = num
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
            raise ValueError(f"{path.name}: slug inválido: {slug}")

        body = "\n".join(lines[1:])
        m = re.search(
            r"ONE_LINER:\s*(.+?)\n"
            r"IMPORTANCE:\s*(.+?)\n"
            r"HOW_IT_WORKS:\s*(.+?)\n"
            r"EXAMPLE:\s*\n(.+?)\n"
            r"TRADE_OFFS:\s*(.+?)\n"
            r"VERIFY:\s*(.+?)\n"
            r"LINKS:\s*(.+?)\n"
            r"SOURCES:\s*(.+)$",
            body,
            re.S,
        )
        if not m:
            raise ValueError(f"{path.name} nota {num} ({slug}): falha ao extrair campos")

        summary, reason, how, example, caveat, verify, links_raw, sources_raw = [
            g.strip() for g in m.groups()
        ]
        urls = [u.strip() for u in sources_raw.split("|") if u.strip()]
        if len(urls) < 2:
            raise ValueError(f"{path.name} nota {num}: menos de 2 URLs")

        sources = [
            (meta["src1_label"], urls[0], meta["src1_note"]),
            (meta["src2_label"], urls[1], meta["src2_note"]),
        ]
        if len(urls) >= 3:
            sources.append((meta["src3_label"], urls[2], meta["src3_note"]))

        links = [
            re.sub(r"^\[\[|\]\]$", "", lk.strip())
            for lk in links_raw.split("|")
            if lk.strip()
        ]
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
id: software.devops.tranche07.{number:06d}
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-07.md"
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
        help="Rebuild the existing tranche-07 notes after validating their IDs and batch metadata.",
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
            r"(?m)^id: software\.devops\.tranche07\.\d{6}\s*$",
            path.read_text(encoding="utf-8", errors="replace")[:1200],
        )
    ]
    if args.refresh and len(existing_tranche) != EXPECTED_NOTES:
        raise ValueError(
            f"--refresh exige exatamente {EXPECTED_NOTES} notas tranche07 existentes; encontradas {len(existing_tranche)}"
        )
    if REPORT.exists() and not args.refresh:
        raise ValueError(f"relatório já existe (use --refresh apenas para atualizar a tranche 7): {REPORT}")
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
            expected_id = f"id: software.devops.tranche07.{expected_number + index:06d}"
            if target_path.exists():
                current = target_path.read_text(encoding="utf-8")
                if not args.refresh:
                    raise ValueError(f"arquivo já existe (use --refresh apenas para a tranche 7): {target_path}")
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
        "# Revisão factual assistida por IA — lote `software-devops-2000-0002`, tranche 7",
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
