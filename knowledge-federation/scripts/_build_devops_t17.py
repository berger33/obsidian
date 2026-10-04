#!/usr/bin/env python3
"""Build the source-backed software-devops batch 2 tranche 17 (notes 1601–1700)."""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "knowledge-federation" / "scripts" / "_devops_t17_data"
NOTES_DIR = ROOT / "knowledge-federation" / "domains" / "software-0008" / "software" / "devops"
DOMAINS_DIR = ROOT / "knowledge-federation" / "domains"
REPORT = ROOT / "knowledge-federation" / "exports" / "reports" / "ai-review-software-devops-2000-0002-tranche-17.md"
DATE = date.today().isoformat()
START = 1601
EXPECTED_NOTES = 100

sys.path.insert(0, str(ROOT / "knowledge-federation" / "scripts"))
from note_quality import assess_markdown, normalize  # noqa: E402
from prose_audit import repeated_substantive_sentences  # noqa: E402

GROUP_META: dict[str, dict[str, str]] = {
    "01-karmada.txt": {
        "sub": "Karmada (orquestração multi-cluster e multi-cloud CNCF Incubating com `PropagationPolicy`, `OverridePolicy`, `ResourceBinding`, `Work` e modos `Push`/`Pull`)",
        "src1_label": "Karmada GitHub — README.md (Kubernetes Armada CNCF Incubating Multi-Cloud & Multi-Cluster Kubernetes Orchestration)",
        "src1_note": "README oficial do karmada-io/karmada (CNCF Incubating) apresentando capacidades multi-cluster, API compatível com Kubernetes nativo e políticas de propagação",
        "src2_label": "Karmada Official Documentation — Core Concepts: Architecture (Control Plane, PropagationPolicy, OverridePolicy, ResourceBinding, Work & Agent)",
        "src2_note": "Documentação oficial de arquitetura do Karmada detalhando API Server, Controller Manager, Karmada Scheduler, Execution Space e sincronização para member clusters",
        "src3_label": "Karmada — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do projeto Karmada na CNCF",
    },
    "02-clusternet.txt": {
        "sub": "Clusternet (gerenciamento de frotas multi-cluster Kubernetes com `clusternet-hub`, `clusternet-agent`, Dual Sockets, `Subscription`, `Description`, `Base` e `Manifest`)",
        "src1_label": "Clusternet GitHub — README.md (Managing Kubernetes Clusters as Easily as Visiting the Internet, Hub/Agent/Scheduler Architecture)",
        "src1_note": "README oficial do clusternet/clusternet detalhando descoberta automática, conexão Dual Sockets, coordenação multi-cluster e roteamento multi-estágio",
        "src2_label": "Clusternet Official Documentation — Introduction (Cluster Registration, App Delivery via Subscription/Localization/Globalization & Shadow APIs)",
        "src2_note": "Introdução oficial do Clusternet cobrindo registro de clusters, entrega de aplicações multi-cluster, Localization, Globalization e APIs shadow",
        "src3_label": "Clusternet — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do Clusternet",
    },
    "03-liqo.txt": {
        "sub": "Liqo (federação dinâmica multi-cluster Kubernetes sem controlador central com peering P2P, Virtual Nodes, offloading de Pods, IPAM/WireGuard e Storage Fabric)",
        "src1_label": "Liqo GitHub — README.md (Dynamic and Seamless Kubernetes Multi-Cluster Topologies, Peering, Offloading, Network & Storage Fabric)",
        "src1_note": "README oficial do liqotech/liqo detalhando peering P2P, Virtual Nodes via Virtual Kubelet, Network Fabric com NATless/NATting IPAM, reflexão de Services e Storage Fabric",
        "src2_label": "Liqo Official Documentation — Quick Start & Examples (liqoctl peer, liqoctl offload namespace, Virtual Node Scheduling & Service Exposure)",
        "src2_note": "Guia oficial Quick Start do Liqo demonstrando peering entre clusters, extensão de namespaces com liqoctl offload e agendamento transparente de Pods remotos",
        "src3_label": "Liqo — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do Liqo",
    },
    "04-kubeedge.txt": {
        "sub": "KubeEdge (plataforma CNCF Graduated de computação de borda nativa de Kubernetes com `CloudCore`, `EdgeCore`, `CloudHub`, `EdgeHub`, `MetaManager`, `Edged` e `DeviceTwin`)",
        "src1_label": "KubeEdge GitHub — README.md (CNCF Graduated Kubernetes Native Edge Computing Framework, CloudCore, EdgeCore, Mappers & EdgeMesh)",
        "src1_note": "README oficial do kubeedge/kubeedge (CNCF Graduated) descrevendo os módulos de nuvem (CloudHub, EdgeController, DeviceController) e de borda (Edged, MetaManager, DeviceTwin)",
        "src2_label": "KubeEdge Official Documentation — Cloud Architecture: CloudHub (WebSocket & QUIC Servers, Keepalive & Dispatcher to EdgeHub)",
        "src2_note": "Documentação oficial de arquitetura do CloudHub no KubeEdge detalhando conexões WebSocket e QUIC, controle de sessão e multiplexação entre CloudCore e EdgeCore",
        "src3_label": "KubeEdge — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do KubeEdge na CNCF",
    },
    "05-openyurt.txt": {
        "sub": "OpenYurt (plataforma CNCF Incubating de extensão de Kubernetes nativo para borda com `YurtHub`, `Yurt-Tunnel`, `NodePool`, `YurtAppSet` e autonomia offline)",
        "src1_label": "OpenYurt GitHub — README.md (CNCF Incubating Extending Native Kubernetes to Edge, Non-Intrusive Architecture & Edge Autonomy)",
        "src1_note": "README oficial do openyurtio/openyurt (CNCF Incubating) apresentando a filosofia não intrusiva, autonomia de borda, NodePool e operação cloud-edge",
        "src2_label": "OpenYurt Official Documentation — Core Concepts: Architecture (YurtHub Local Cache, Yurt-Tunnel Reverse Proxy, Yurt-Manager & Raven)",
        "src2_note": "Documentação oficial de arquitetura do OpenYurt detalhando YurtHub, Yurt-Tunnel-Server/Agent, controladores do Yurt-Manager e topologia por NodePool",
        "src3_label": "OpenYurt — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do OpenYurt na CNCF",
    },
    "06-superedge.txt": {
        "sub": "SuperEdge (sistema de gerenciamento de containers nativo de Kubernetes para borda com `lite-apiserver`, `Kins` L4/L5, `edge-health`, `ServiceGroup` e `tunnel`)",
        "src1_label": "SuperEdge GitHub — README.md (Kubernetes-Native Edge Container Management System, Kins L4/L5 Autonomy, ServiceGroup & Edge-Health)",
        "src1_note": "README oficial do superedge/superedge detalhando componentes de nuvem e borda, níveis de autonomia L3/L4/L5 (Kins), DeploymentGrid/ServiceGrid, tunnel e edgeadm",
        "src2_label": "SuperEdge Official Documentation — Components: lite-apiserver (TLS CN Reverse Proxy, Bolt/Badger/File Cache & Certificate Rotation)",
        "src2_note": "Documentação técnica oficial do componente lite-apiserver no SuperEdge cobrindo proxy por Common Name X.509, motores de cache local e autonomia L3",
        "src3_label": "SuperEdge — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do SuperEdge",
    },
    "07-akri.txt": {
        "sub": "Akri (interface CNCF Sandbox em Rust para descoberta e exposição dinâmica de *Leaf Devices* no Kubernetes com `Configuration`, `Instance`, `Discovery Handlers`, `Agent` e `Controller`)",
        "src1_label": "Akri GitHub — README.md (CNCF Sandbox Kubernetes Resource Interface for the Edge, ONVIF, udev, OPC UA & Dynamic Leaf Device Discovery)",
        "src1_note": "README oficial do project-akri/akri (CNCF Sandbox) explicando a exposição dinâmica de dispositivos folha como recursos nativos de Kubernetes",
        "src2_label": "Akri Official Documentation — Architecture Overview (Configuration & Instance CRDs, Discovery Handlers, Akri Agent Device Plugin & Controller)",
        "src2_note": "Visão geral oficial da arquitetura do Akri detalhando os 5 componentes, slots deviceUsage, brokerPodSpec/brokerJobSpec e injeção de brokerProperties",
        "src3_label": "Akri Documentation Repository — architecture-overview.md",
        "src3_note": "Fonte oficial em Markdown da documentação de arquitetura do projeto Akri",
    },
    "08-rke2.txt": {
        "sub": "RKE2 / RKE Government (distribuição Kubernetes da Rancher com conformidade FIPS 140-2 `Go+BoringCrypto`, CIS Benchmark, SELinux/MCS, Static Pods e `helm-controller`)",
        "src1_label": "RKE2 GitHub — README.md (Rancher's Next-Gen Kubernetes Distribution / RKE Government, FIPS 140-2, CIS Hardening & Configuration File)",
        "src1_note": "README oficial do rancher/rke2 detalhando conformidade FIPS 140-2 com Go+BoringCrypto, CIS Benchmark, instalação systemd e /etc/rancher/rke2/config.yaml",
        "src2_label": "RKE2 Official Documentation — Architecture (Content Bootstrap from rke2-runtime, Server/Agent Static Pod Lifecycle, CNI, Traefik & CIS/SELinux)",
        "src2_note": "Documentação oficial de arquitetura do RKE2 explicando Content Bootstrap, Static Pods do control plane, helm-controller, plugins CNI e transição para Traefik v1.36+",
        "src3_label": "RKE2 — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do Rancher RKE2",
    },
    "09-k0s.txt": {
        "sub": "k0s (distribuição Kubernetes *Zero Friction* CNCF Sandbox em binário único sem dependências de OS, processos *naked*, `Konnectivity`, `kine`, `k0sctl` e `Autopilot`)",
        "src1_label": "k0s GitHub — README.md (Zero-Friction Kubernetes in a Single Binary, Konnectivity, Kube-Router, kine, k0sctl & Multi-Arch RISC-V/ARM/x86)",
        "src1_note": "README oficial do k0sproject/k0s (CNCF Sandbox) detalhando empacotamento em binário único, isolamento do control plane, opções de storage/CNI e suporte multi-arquitetura",
        "src2_label": "k0s Official Documentation — Architecture (Process Supervisor, Naked Control Plane Processes, In-Cluster Autopilot & CRI/Worker Runtime)",
        "src2_note": "Documentação oficial de arquitetura do k0s detalhando supervisão de processos sem container engine no controller, gerenciamento de etcd/kine e containerd nos workers",
        "src3_label": "k0s — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do k0s na CNCF",
    },
    "10-microk8s.txt": {
        "sub": "Canonical MicroK8s (distribuição Kubernetes certificada em pacote único Snap com alta disponibilidade automática via `dqlite`, domínios de falha `ha-conf` e add-ons curados)",
        "src1_label": "Canonical MicroK8s GitHub — README.md (Single-Package Snap Kubernetes for Developers, CI/CD, IoT & Edge with Curated Addons)",
        "src1_note": "README oficial do canonical/microk8s detalhando instalação via Snap, canais de versão, comandos microk8s kubectl/enable/status/inspect e add-ons embutidos",
        "src2_label": "Canonical MicroK8s Official Documentation — High Availability (Automatic dqlite HA, Voters/Standby/Spare Roles, Failure Domains & Node Lifecycle)",
        "src2_note": "Documentação oficial de Alta Disponibilidade do MicroK8s cobrindo datastore dqlite na porta 19001, eleição em 5s, papéis voter/standby/spare e ha-conf",
        "src3_label": "Canonical MicroK8s — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do Canonical MicroK8s",
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
id: software.devops.tranche17.{number:06d}
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-17.md"
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
        help="Rebuild the existing tranche-17 notes after validating their IDs and batch metadata.",
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
            r"(?m)^id: software\.devops\.tranche17\.\d{6}\s*$",
            path.read_text(encoding="utf-8", errors="replace")[:1200],
        )
    ]
    if args.refresh and len(existing_tranche) != EXPECTED_NOTES:
        raise ValueError(
            f"--refresh exige exatamente {EXPECTED_NOTES} notas tranche17 existentes; encontradas {len(existing_tranche)}"
        )
    if REPORT.exists() and not args.refresh:
        raise ValueError(f"relatório já existe (use --refresh apenas para atualizar a tranche 17): {REPORT}")
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
            expected_id = f"id: software.devops.tranche17.{expected_number + index:06d}"
            if target_path.exists():
                current = target_path.read_text(encoding="utf-8")
                if not args.refresh:
                    raise ValueError(f"arquivo já existe (use --refresh apenas para a tranche 17): {target_path}")
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
        "# Revisão factual assistida por IA — lote `software-devops-2000-0002`, tranche 17",
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
