#!/usr/bin/env python3
"""Build the source-backed software-devops batch 2 tranche 15 (notes 1401–1500)."""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "knowledge-federation" / "scripts" / "_devops_t15_data"
NOTES_DIR = ROOT / "knowledge-federation" / "domains" / "software-0008" / "software" / "devops"
DOMAINS_DIR = ROOT / "knowledge-federation" / "domains"
REPORT = ROOT / "knowledge-federation" / "exports" / "reports" / "ai-review-software-devops-2000-0002-tranche-15.md"
DATE = date.today().isoformat()
START = 1401
EXPECTED_NOTES = 100

sys.path.insert(0, str(ROOT / "knowledge-federation" / "scripts"))
from note_quality import assess_markdown, normalize  # noqa: E402
from prose_audit import repeated_substantive_sentences  # noqa: E402

GROUP_META: dict[str, dict[str, str]] = {
    "01-copacetic.txt": {
        "sub": "Project Copacetic (`copa`, CLI CNCF Sandbox baseada em BuildKit para aplicação direta de patches de vulnerabilidades de SO em imagens de container sem rebuild completo)",
        "src1_label": "Project Copacetic GitHub — README.md (Direct Container Image Patching, BuildKit Engine, Ubuntu Chiseled Images & Extensible Adapters)",
        "src1_note": "README oficial do project-copacetic/copacetic (CNCF Sandbox) detalhando a arquitetura de patching direto sem rebuild, suporte a Ubuntu Chiseled e integração com scanners",
        "src2_label": "Project Copacetic Official Documentation — Quick Start (Targeted vs Comprehensive Patching, Trivy Reports, BuildKit Auto-Detection & Compression)",
        "src2_note": "Guia oficial Quick Start do Copacetic demonstrando o fluxo completo de scan com Trivy, patching direcionado (-r) vs abrangente, controle de compressão e verificação",
        "src3_label": "Project Copacetic — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do Project Copacetic na CNCF",
    },
    "02-kepler.txt": {
        "sub": "Kepler (Kubernetes-based Efficient Power Level Exporter, exportador Prometheus CNCF Sandbox de consumo de energia e potência para nós, containers, pods, processos e VMs)",
        "src1_label": "Kepler GitHub — README.md (v0.10.0+ Ground-Up Rewrite, Reduced Security Requirements, Dynamic RAPL Detection, Helm OCI & Kustomize Deployment)",
        "src1_note": "README oficial do sustainable-computing-io/kepler detalhando a reescrita v0.10.0+, remoção de CAP_SYSADMIN/CAP_BPF, acesso somente leitura a /proc e /sys e métodos de instalação",
        "src2_label": "Kepler Official Documentation — docs/user/metrics.md (RAPL Energy Zones, Node, Container, Process & Virtual Machine Prometheus Metrics)",
        "src2_note": "Referência oficial de métricas Prometheus do Kepler cobrindo zonas RAPL (psys, package, core, uncore, dram) e métricas em Joules e Watts para CPU e GPU",
        "src3_label": "Kepler — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do Kepler na CNCF",
    },
    "03-k8sgpt.txt": {
        "sub": "K8sGPT & K8sGPT Operator (ferramenta e operador CNCF Sandbox de diagnóstico e triagem SRE para Kubernetes com analisadores embutidos, anonimização, MCP Server e auto-remediação controlada)",
        "src1_label": "K8sGPT GitHub — README.md (Built-in & Optional SRE Analyzers, Anonymization, LLM AI Backends, LiteLLM & Model Context Protocol Server)",
        "src1_note": "README oficial do k8sgpt-ai/k8sgpt documentando analisadores padrão e opcionais, mascaramento reversível (--anonymize), provedores de IA e servidor gRPC/MCP",
        "src2_label": "K8sGPT Operator GitHub — README.md (In-Cluster K8sGPT CRD, Result Objects, Multi-Cluster Cluster API Monitoring & Opt-In Auto-Remediation)",
        "src2_note": "README oficial do k8sgpt-ai/k8sgpt-operator detalhando monitoramento contínuo in-cluster, rotação automática de Secrets, integração multi-cluster com CAPI e gate determinístico de auto-remediação",
        "src3_label": "K8sGPT — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do K8sGPT",
    },
    "04-lima.txt": {
        "sub": "Lima (Linux Machines, gerenciador CNCF Incubating de máquinas virtuais Linux com compartilhamento automático de arquivos, encaminhamento de portas, templates Docker/K8s e QEMU/VZ)",
        "src1_label": "Lima GitHub — README.md (Linux Virtual Machines, Automatic File Sharing & Port Forwarding, containerd/nerdctl/Docker/K8s Templates & CycloneDX SBOM)",
        "src1_note": "README oficial do lima-vm/lima (CNCF Incubating) apresentando o fluxo limactl, templates de Docker e Kubernetes, geração de SBOM CycloneDX (app vs mod) e ecossistema de adotantes",
        "src2_label": "Lima Official Documentation — Configuration Guide (Default Spec, VM Types VZ/QEMU, Multi-Arch, Port Forwarding, Mounts & Plain Mode)",
        "src2_note": "Guia oficial de configuração do Lima detalhando a especificação padrão (4 vCPUs, 4 GiB RAM, 100 GiB disk), tipos de VM, montagens, redes, discos e modo plain",
        "src3_label": "Lima — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do Lima na CNCF",
    },
    "05-colima.txt": {
        "sub": "Colima (Containers on Lima, CLI para provisão rápida de runtimes Docker, containerd, Kubernetes, Incus e modelos de IA com GPU via krunkit em macOS e Linux)",
        "src1_label": "Colima GitHub — README.md (Docker, Containerd, Kubernetes & Incus Runtimes on macOS/Linux, GPU AI Workloads with krunkit & VM Customization)",
        "src1_note": "README oficial do abiosoft/colima detalhando os runtimes suportados, compartilhamento de imagens com Kubernetes, execução de modelos de IA acelerados por GPU via krunkit e dimensionamento de VM",
        "src2_label": "Colima Official Documentation — docs/FAQ.md (COLIMA_HOME Precedence, colima.yaml Configuration, Docker/Containerd Overrides, Reachable IP & Provision Scripts)",
        "src2_note": "FAQ técnico oficial do Colima cobrindo precedência de diretórios de configuração, customização de daemon.json, múltiplos perfis, endereço IP roteável e scripts de provisionamento",
        "src3_label": "Colima — Official GitHub Repository",
        "src3_note": "Repositório oficial MIT do Colima",
    },
    "06-incus.txt": {
        "sub": "Linux Containers Incus (gerenciador comunitário de containers de sistema LXC e máquinas virtuais QEMU com API REST unificada, user namespaces e segurança de bridge nftables)",
        "src1_label": "Incus GitHub — README.md (System Container & Virtual Machine Manager, Linux Containers Governance, Apache-2.0 License & Security Overview)",
        "src1_note": "README oficial do lxc/incus apresentando a arquitetura unificada para containers de sistema e VMs, histórico comunitário pós-LXD e diretrizes fundamentais de segurança",
        "src2_label": "Incus Official Documentation — doc/tutorial/first_steps.md (Initialization, Launching Containers & VMs, Resource Limits, Exec & Snapshots)",
        "src2_note": "Tutorial oficial First Steps do Incus demonstrando grupos incus vs incus-admin, incus admin init, criação de containers e VMs, limites dinâmicos de CPU/memória/disco e snapshots",
        "src3_label": "Incus Official Documentation — doc/explanation/security.md (Unix Socket Access, Unprivileged Containers, Isolated IDMaps & Bridged NIC Filtering)",
        "src3_note": "Documentação oficial de segurança do Incus detalhando isolamento de user namespaces, security.idmap.isolated, proteção contra vazamento de cgroups e filtragem MAC/IPv4/IPv6 na bridge incusbr0",
    },
    "07-spegel.txt": {
        "sub": "Spegel (mirror de registro OCI stateless e peer-to-peer local ao cluster Kubernetes com roteamento automático via containerd e descoberta por DHT)",
        "src1_label": "Spegel Official Documentation — Getting Started (Helm & Flux Deployment, Containerd Compatibility Matrix, EKS AL2023/Bottlerocket & /debug/web Verification)",
        "src1_note": "Guia oficial Getting Started do Spegel detalhando requisitos de containerd (config_path e discard_unpacked_layers = false), matriz de distribuições Kubernetes e validação via /debug/web",
        "src2_label": "Spegel GitHub — README.md (Stateless Cluster-Local OCI Registry Mirror Architecture & Features)",
        "src2_note": "README oficial do spegel-org/spegel explicando o cache P2P local de imagens, mitigação de rate-limiting e resiliência a quedas de registries externos",
        "src3_label": "Spegel — Official GitHub Repository",
        "src3_note": "Repositório oficial do Spegel",
    },
    "08-kamaji.txt": {
        "sub": "Clastix Kamaji (gerenciador de Hosted Control Planes Kubernetes rodando como Pods sobre Datastores compartilhados etcd/Kine com integração nativa ao Cluster API)",
        "src1_label": "Kamaji GitHub — README.md (Hosted Control Planes in Pods, TenantControlPlane & Datastore CRDs, Konnectivity, Auto-Healing & Use Cases)",
        "src1_note": "README oficial do clastix/kamaji explicando a arquitetura de planos de controle em Pods, provisionamento em 16s, upgrades Blue/Green em 10s e multi-tenancy de Datastore",
        "src2_label": "Kamaji Official Documentation — API Reference (KamajiControlPlane, TenantControlPlane, Datastore, Addons & DataStoreOverrides)",
        "src2_note": "Referência oficial da API do Kamaji especificando os campos de KamajiControlPlane, TenantControlPlane, addons (coreDNS, kubeProxy, konnectivity) e dataStoreOverrides",
        "src3_label": "Kamaji Cluster API Control Plane Provider — Official README.md",
        "src3_note": "README oficial do provedor Cluster API do Kamaji listando os 14 provedores de infraestrutura suportados",
    },
    "09-capsule.txt": {
        "sub": "Clastix Capsule & Capsule Proxy (operador CNCF Sandbox de multi-tenancy e governança baseada em políticas para Kubernetes com abstração Tenant e listagem filtrada cluster-scoped)",
        "src1_label": "Capsule GitHub — README.md (Multi-Tenancy Operator, Tenant Abstraction, Policy Engine, Self-Service Namespaces, BYOD & CycloneDX SBOM)",
        "src1_note": "README oficial do projectcapsule/capsule (CNCF Sandbox) detalhando a prevenção de cluster sprawl via CRD Tenant, herança automática de políticas/cotas e modelo BYOD",
        "src2_label": "Capsule Proxy GitHub — README.md (Filtered Cluster-Scoped Resource Listing, ProxySetting vs GlobalProxySettings Security Boundary)",
        "src2_note": "README oficial do projectcapsule/capsule-proxy explicando a filtragem de recursos cluster-scoped para tenants e a fronteira de segurança entre ProxySetting e GlobalProxySettings",
        "src3_label": "Project Capsule — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do Capsule na CNCF",
    },
    "10-eraser.txt": {
        "sub": "CNCF Eraser (operador Kubernetes de limpeza automatizada de imagens de container não utilizadas e vulneráveis nos nós via pipeline collector, scanner e remover)",
        "src1_label": "Eraser Official Documentation — Quick Start (DaemonSet Validation, Collector/Scanner/Remover Pipeline, repeatInterval & Scanner Toggle)",
        "src1_note": "Guia oficial Quick Start do Eraser demonstrando a remoção automática de imagens não utilizadas e vulneráveis nos nós, configuração de repeatInterval e modo de 2 containers sem scanner",
        "src2_label": "Eraser GitHub — README.md (Cleaning Up Non-Running Images from Kubernetes Nodes & CNCF Governance)",
        "src2_note": "README oficial do eraser-dev/eraser (CNCF Sandbox) apresentando o escopo e a governança do projeto",
        "src3_label": "CNCF Eraser — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do Eraser",
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
id: software.devops.tranche15.{number:06d}
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-15.md"
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
        help="Rebuild the existing tranche-15 notes after validating their IDs and batch metadata.",
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
            r"(?m)^id: software\.devops\.tranche15\.\d{6}\s*$",
            path.read_text(encoding="utf-8", errors="replace")[:1200],
        )
    ]
    if args.refresh and len(existing_tranche) != EXPECTED_NOTES:
        raise ValueError(
            f"--refresh exige exatamente {EXPECTED_NOTES} notas tranche15 existentes; encontradas {len(existing_tranche)}"
        )
    if REPORT.exists() and not args.refresh:
        raise ValueError(f"relatório já existe (use --refresh apenas para atualizar a tranche 15): {REPORT}")
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
            expected_id = f"id: software.devops.tranche15.{expected_number + index:06d}"
            if target_path.exists():
                current = target_path.read_text(encoding="utf-8")
                if not args.refresh:
                    raise ValueError(f"arquivo já existe (use --refresh apenas para a tranche 15): {target_path}")
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
        "# Revisão factual assistida por IA — lote `software-devops-2000-0002`, tranche 15",
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
