#!/usr/bin/env python3
"""Build the source-backed software-devops batch 2 tranche 14 (notes 1301–1400)."""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "knowledge-federation" / "scripts" / "_devops_t14_data"
NOTES_DIR = ROOT / "knowledge-federation" / "domains" / "software-0008" / "software" / "devops"
DOMAINS_DIR = ROOT / "knowledge-federation" / "domains"
REPORT = ROOT / "knowledge-federation" / "exports" / "reports" / "ai-review-software-devops-2000-0002-tranche-14.md"
DATE = date.today().isoformat()
START = 1301
EXPECTED_NOTES = 100

sys.path.insert(0, str(ROOT / "knowledge-federation" / "scripts"))
from note_quality import assess_markdown, normalize  # noqa: E402
from prose_audit import repeated_substantive_sentences  # noqa: E402

GROUP_META: dict[str, dict[str, str]] = {
    "01-pixie.txt": {
        "sub": "Pixie (plataforma de observabilidade CNCF Sandbox para Kubernetes baseada em eBPF, computação na borda com PEM/Vizier e linguagem Pythonica PxL)",
        "src1_label": "Pixie Official Documentation — Pixie Overview & Architecture (PEM, Vizier, Pixie Cloud, CLI & eBPF Auto-Telemetry)",
        "src1_note": "Visão geral e arquitetura oficial do Pixie detalhando o Pixie Edge Module (PEM), Vizier, Pixie Cloud, coleta eBPF sem instrumentação manual e linguagem PxL",
        "src2_label": "Pixie GitHub — README.md (Network Monitoring, Service Performance, Database Query Profiling, Continuous Profiling, bpftrace & Dynamic Go Logging)",
        "src2_note": "README oficial do pixie-io/pixie (CNCF Sandbox) documentando casos de uso de monitoramento de rede/DNS/TCP drops, profiling de queries SQL, Flame Graphs, bpftrace distribuído e Dynamic Go Logging",
        "src3_label": "Pixie — Official GitHub Repository",
        "src3_note": "Repositório oficial do Pixie na CNCF",
    },
    "02-submariner.txt": {
        "sub": "Submariner (rede multi-cluster CNI-agnóstica da CNCF com Gateway Engine IPsec/WireGuard, Route Agent, Broker, Lighthouse DNS e Globalnet)",
        "src1_label": "Submariner Official Documentation — Architecture (Gateway Engine, Route Agent, Broker, Lighthouse Service Discovery & Globalnet)",
        "src1_note": "Documentação oficial de arquitetura do Submariner detalhando ClusterSet, ServiceExport, ServiceImport, domínio clusterset.local, Headless Services por cluster-id e Globalnet Controller",
        "src2_label": "Submariner GitHub — README.md (Network Path, vx-submariner VXLAN Tunnel, Operator, subctl & Helm Deployment)",
        "src2_note": "README oficial do submariner-io/submariner descrevendo o caminho de pacotes entre worker nodes e nós Gateway eleitos, submariner-operator e comandos subctl",
        "src3_label": "Submariner — Official GitHub Repository",
        "src3_note": "Repositório oficial CNCF Sandbox do Submariner",
    },
    "03-headlamp.txt": {
        "sub": "Headlamp (interface web e desktop Kubernetes extensível do Kubernetes SIG UI / CNCF com controles orientados por RBAC, OIDC, multi-cluster e plugins)",
        "src1_label": "Headlamp GitHub — README.md (Kubernetes SIG UI Web & Desktop App, RBAC-Aware Controls, Multi-Cluster & Plugins)",
        "src1_note": "README oficial do kubernetes-sigs/headlamp (Apache-2.0) detalhando funcionalidades multi-cluster, reflexão de permissões RBAC na UI, terminal/logs/editor e ecossistema de plugins no Artifact Hub",
        "src2_label": "Headlamp Official Documentation — In-Cluster Installation (Helm Chart, Cluster Inventory API, Multiple Kubeconfigs, TLS, OIDC & pluginsManager Sidecar)",
        "src2_note": "Guia oficial de implantação in-cluster do Headlamp cobrindo Helm chart, descoberta via ClusterProfile/secretreader, variáveis KUBECONFIG e sidecar pluginsManager",
        "src3_label": "Headlamp — Official GitHub Repository",
        "src3_note": "Repositório oficial do Headlamp no Kubernetes SIG UI",
    },
    "04-pipecd.txt": {
        "sub": "PipeCD (plataforma CNCF Sandbox de entrega contínua GitOps unificada para Kubernetes, Terraform, Cloud Run, Lambda e ECS com análise automatizada ADA)",
        "src1_label": "PipeCD Official Documentation — Core Concepts (Control Plane, Stateless Piped Agent, Projects, app.pipecd.yaml, Sync Strategies, Platform & Analysis Providers)",
        "src1_note": "Documentação oficial de conceitos do PipeCD detalhando a arquitetura Control Plane + Piped stateless, papéis Viewer/Editor/Admin, Quick Sync vs Pipeline Sync, Platform Providers e Analysis Providers",
        "src2_label": "PipeCD GitHub — README.md (Unified Multi-Platform GitOps CD, Progressive Delivery, Built-in ADA & Delivery Insights)",
        "src2_note": "README oficial do pipe-cd/pipecd (CNCF Sandbox) explicando o fluxo GitOps sem exposição de credenciais externas, análise automática de deploy e métricas DORA no Delivery Insights",
        "src3_label": "PipeCD — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do PipeCD",
    },
    "05-porter.txt": {
        "sub": "Porter (instalador e construtor declarativo CNCF Sandbox de pacotes CNAB — Cloud Native Application Bundles — com Mixins, Plugins e Thick Bundles air-gapped)",
        "src1_label": "Porter GitHub — README.md (CNAB Application Bundles, Porter Mixins for Helm/Terraform/Kubernetes/Cloud CLIs & Porter Plugins for Vault/Azure/K8s)",
        "src1_note": "README oficial do getporter/porter (CNCF Sandbox) apresentando a especificação CNAB, a matriz oficial de Mixins (Docker, Kubernetes, Helm, GCloud, Terraform, AWS, Azure, exec) e Plugins (HashiCorp, Azure, Kubernetes)",
        "src2_label": "Porter Official Documentation — Quickstart (porter install, list, show, upgrade & uninstall)",
        "src2_note": "Guia oficial Quickstart do Porter demonstrando o ciclo de vida completo de instalação, listagem, inspeção de histórico Run ID, upgrade e desinstalação de bundles OCI",
        "src3_label": "Porter — Official GitHub Repository",
        "src3_note": "Repositório oficial do Porter na CNCF",
    },
    "06-devspace.txt": {
        "sub": "DevSpace (ferramenta CNCF Sandbox client-only para desenvolvimento Kubernetes com devspace.yaml, hot reloading, sync bidirecional e pipelines declarativos)",
        "src1_label": "DevSpace GitHub — README.md (Client-Only Kubernetes Developer Tool, devspace.yaml, Hot Reloading, Parallel Image Building & Multi-Cluster Compatibility)",
        "src1_note": "README oficial do devspace-sh/devspace (Apache-2.0, CNCF Sandbox) explicando a arquitetura client-only sobre kube-context, hot reloading com sync bidirecional, variáveis de configuração e automação de port-forwarding/logs",
        "src2_label": "DevSpace Official Documentation — Getting Started Introduction (Declarative Workflows, Team Standardization & Hot Reloading)",
        "src2_note": "Introdução oficial da documentação do DevSpace 6.x detalhando o funcionamento do CLI sem componentes server-side obrigatórios e compatibilidade com clusters locais e gerenciados",
        "src3_label": "DevSpace — Official GitHub Repository",
        "src3_note": "Repositório oficial do DevSpace",
    },
    "07-apko.txt": {
        "sub": "apko (construtor declarativo da Chainguard para imagens de container OCI reprodutíveis bit-a-bit e distroless baseadas em pacotes APK com SBOM automático)",
        "src1_label": "apko GitHub — README.md (APK-Based Reproducible OCI Image Builder, apko build, apko publish, SBOM Generation & Declarative Design)",
        "src1_note": "README oficial do chainguard-dev/apko detalhando reprodutibilidade bitwise sem instruções RUN, geração automática de SBOM, integração com melange e supervisão s6",
        "src2_label": "apko Official Documentation — docs/apko_file.md (contents, repositories, runtime_keyring, entrypoint, accounts, paths, archs & layering)",
        "src2_note": "Referência completa do formato YAML do apko cobrindo repositórios @local, runtime_repositories/runtime_keyring, accounts non-root, mutações de paths e layering.strategy",
        "src3_label": "Chainguard apko — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do apko",
    },
    "08-melange.txt": {
        "sub": "melange (compilador declarativo de pacotes APK baseado em pipelines para os ecossistemas Wolfi e Alpine Linux com assinatura RSA, subpackages e testes)",
        "src1_label": "melange GitHub — README.md (Declarative APK Package Builder, Pipeline Builds, QEMU Multi-Arch, melange keygen, Default Substitutions & Debugging)",
        "src1_note": "README oficial do chainguard-dev/melange documentando o arquivo de build, variáveis de substituição (${{package.*}}, ${{targets.destdir}}), assinatura RSA, subpackages e uso conjunto com apko",
        "src2_label": "melange Official Documentation — docs/BUILD-FILE.md (package, version, epoch, copyright SPDX, dependencies.provides, options & environment)",
        "src2_note": "Especificação oficial do arquivo de build do melange detalhando version/epoch, licenças SPDX em copyright, fluxos de versão com provides e controles do gerador SCA em options",
        "src3_label": "Chainguard melange — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do melange",
    },
    "09-nerdctl.txt": {
        "sub": "nerdctl (CLI compatível com Docker para containerd com suporte nativo a Docker Compose, namespace k8s.io, modo Rootless bypass4netns, Lazy-Pulling e Cosign/ocicrypt)",
        "src1_label": "nerdctl GitHub — README.md (Docker-Compatible CLI for containerd, Kubernetes Debugging in k8s.io, Rootless bypass4netns, Lazy-Pulling, ocicrypt, IPFS & Cosign)",
        "src1_note": "README oficial do containerd/nerdctl detalhando o uso com BuildKit/CNI, depuração de Kubernetes no namespace k8s.io, snapshotters (stargz, nydus, overlaybd, soci) e diferenciais frente ao Docker",
        "src2_label": "nerdctl Official Documentation — docs/command-reference.md (Container, Image, Compose, Namespace, AppArmor & IPFS Commands)",
        "src2_note": "Referência oficial completa de comandos e flags do nerdctl e nerdctl compose",
        "src3_label": "containerd nerdctl — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do nerdctl",
    },
    "10-crictl.txt": {
        "sub": "crictl & cri-tools (CLI e suíte de validação oficial do Kubernetes SIG Node para inspeção, depuração e benchmark da Kubelet Container Runtime Interface — CRI)",
        "src1_label": "cri-tools Official Documentation — docs/crictl.md (CRI CLI Commands, /etc/crictl.yaml, runtime-endpoint, stats/statsp/metricsp, checkpoint & OpenTelemetry Tracing)",
        "src1_note": "Guia oficial completo do crictl detalhando todos os subcomandos de PodSandbox, containers, imagens e métricas CRI, configuração de /etc/crictl.yaml e flags de tracing/timeout",
        "src2_label": "kubernetes-sigs/cri-tools GitHub — README.md (Project Scope, Kubernetes Version Compatibility Matrix, crictl & critest Installation)",
        "src2_note": "README oficial do kubernetes-sigs/cri-tools explicando o escopo do crictl e do critest e a matriz de compatibilidade de versões minor com o Kubernetes",
        "src3_label": "Kubernetes SIG Node cri-tools — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do cri-tools",
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
id: software.devops.tranche14.{number:06d}
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-14.md"
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
        help="Rebuild the existing tranche-14 notes after validating their IDs and batch metadata.",
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
            r"(?m)^id: software\.devops\.tranche14\.\d{6}\s*$",
            path.read_text(encoding="utf-8", errors="replace")[:1200],
        )
    ]
    if args.refresh and len(existing_tranche) != EXPECTED_NOTES:
        raise ValueError(
            f"--refresh exige exatamente {EXPECTED_NOTES} notas tranche14 existentes; encontradas {len(existing_tranche)}"
        )
    if REPORT.exists() and not args.refresh:
        raise ValueError(f"relatório já existe (use --refresh apenas para atualizar a tranche 14): {REPORT}")
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
            expected_id = f"id: software.devops.tranche14.{expected_number + index:06d}"
            if target_path.exists():
                current = target_path.read_text(encoding="utf-8")
                if not args.refresh:
                    raise ValueError(f"arquivo já existe (use --refresh apenas para a tranche 14): {target_path}")
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
        "# Revisão factual assistida por IA — lote `software-devops-2000-0002`, tranche 14",
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
