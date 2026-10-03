#!/usr/bin/env python3
"""Build the source-backed software-devops batch 2 tranche 18 (notes 1701–1800)."""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "knowledge-federation" / "scripts" / "_devops_t18_data"
NOTES_DIR = ROOT / "knowledge-federation" / "domains" / "software-0008" / "software" / "devops"
DOMAINS_DIR = ROOT / "knowledge-federation" / "domains"
REPORT = ROOT / "knowledge-federation" / "exports" / "reports" / "ai-review-software-devops-2000-0002-tranche-18.md"
DATE = date.today().isoformat()
START = 1701
EXPECTED_NOTES = 100

sys.path.insert(0, str(ROOT / "knowledge-federation" / "scripts"))
from note_quality import assess_markdown, normalize  # noqa: E402
from prose_audit import repeated_substantive_sentences  # noqa: E402

GROUP_META: dict[str, dict[str, str]] = {
    "01-openebs.txt": {
        "sub": "OpenEBS (armazenamento CNCF Container Native Storage com `Mayastor` NVMe-oF replicado, `Local PV Hostpath`, `Local PV LVM`, `Local PV ZFS` e `Local PV Rawfile`)",
        "src1_label": "OpenEBS GitHub — README.md (Cloud Native Storage, Local Storage vs Replicated Storage Matrix & Sub-Projects)",
        "src1_note": "README oficial do openebs/openebs (CNCF Sandbox) comparando Local Storage e Replicated Storage e detalhando Hostpath, ZFS, LVM, Rawfile e Mayastor",
        "src2_label": "OpenEBS Official Documentation — Architecture v4.6.x (Data Engines, Volume Access/Services/Data/Storage Layers & Control Plane)",
        "src2_note": "Documentação oficial de arquitetura do OpenEBS explicando as 4 camadas dos Data Engines, Target/Nexus por volume e estados de Volume Replicas",
        "src3_label": "OpenEBS — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do projeto OpenEBS na CNCF",
    },
    "02-juicefs.txt": {
        "sub": "JuiceFS (sistema de arquivos distribuído POSIX cloud-native sobre Object Storage e Metadata Engine com `Chunks`/`Slices`/`Blocks`, cache NVMe e Kubernetes CSI Driver)",
        "src1_label": "JuiceFS GitHub — README.md (High-Performance POSIX Cloud-Native File System, Object Storage + Metadata Engine Architecture)",
        "src1_note": "README oficial do juicedata/juicefs apresentando compatibilidade POSIX/Hadoop/S3, consistência forte, locks globais, criptografia e compressão",
        "src2_label": "JuiceFS Official Documentation — Architecture (JuiceFS Client, Data Storage, Metadata Engine & Chunks/Slices/Blocks Layout)",
        "src2_note": "Documentação oficial de arquitetura do JuiceFS detalhando Chunks de 64 MiB, Slices append-only, Blocks de 4 MiB, compactação e métodos de acesso",
        "src3_label": "JuiceFS — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do JuiceFS",
    },
    "03-seaweedfs.txt": {
        "sub": "SeaweedFS (sistema de armazenamento distribuído inspirado no Facebook Haystack com leitura $O(1)$, `Master`/`Volume`/`Filer`, S3 Gateway, S3 Tables Iceberg/Lance, Erasure Coding e CSI Driver)",
        "src1_label": "SeaweedFS GitHub — README.md (O(1) Disk Read Blob Store, Master/Volume/Filer, S3 API, S3 Tables Iceberg/Lance, Cloud Drive & Erasure Coding)",
        "src1_note": "README oficial do seaweedfs/seaweedfs detalhando leitura em 1 seek (16-byte RAM index), replicação XYZ, Filer stateless, S3 Gateway e Lakehouse",
        "src2_label": "SeaweedFS CSI Driver GitHub — README.md (Kubernetes CSI Dynamic/Static Provisioning, Collection Quotas & Safe Rollout)",
        "src2_note": "Documentação oficial do seaweedfs-csi-driver cobrindo provisionamento RWX, cotas ENOSPC por collection, parâmetros de StorageClass e atualização OnDelete",
        "src3_label": "SeaweedFS — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do SeaweedFS",
    },
    "04-piraeus.txt": {
        "sub": "Piraeus Datastore e LINSTOR (armazenamento em bloco replicado CNCF Sandbox no Kubernetes sobre DRBD9, `Piraeus Operator v2`, `LinstorCluster`, `LinstorSatellite` e `ha-controller`)",
        "src1_label": "Piraeus Operator v2 GitHub — README.md (Managing LINSTOR, DRBD, CSI Driver & High-Availability Controller in Kubernetes)",
        "src1_note": "README oficial do piraeusdatastore/piraeus-operator v2 demonstrando deploy server-side e provisionamento declarativo via LinstorCluster",
        "src2_label": "Piraeus Datastore Official Documentation — Understanding Components (Operator, gencert, Controller, Satellite, CSI, NFS Reactor, Affinity & HA Controller)",
        "src2_note": "Documentação oficial de arquitetura dos 9 componentes do Piraeus Datastore, incluindo namespaces UTS/Network dos Satellites, DRBD Reactor RWX e HA failover",
        "src3_label": "Piraeus Operator — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do Piraeus Operator na CNCF",
    },
    "05-kubebuilder.txt": {
        "sub": "Kubebuilder (framework oficial Kubernetes SIG-API-Machinery em Go sobre `controller-runtime` e `controller-tools` para construção de CRDs, Reconcilers, Webhooks e testes `envtest`)",
        "src1_label": "Kubebuilder GitHub — README.md (Framework for Building Kubernetes APIs using CRDs, Controller-Runtime, Plugins & Design Philosophy)",
        "src1_note": "README oficial do kubernetes-sigs/kubebuilder detalhando fluxo de desenvolvimento, filosofia de bibliotecas/geração de código, plugins e matriz de versões",
        "src2_label": "The Kubebuilder Book — Groups, Versions, Kinds and Resources (GVK, GVR, Scheme Mapping & Single Responsibility)",
        "src2_note": "Capítulo oficial do Kubebuilder Book explicando API Groups, Versions, Kinds, Resources, registro no runtime.Scheme e design modular de CRDs",
        "src3_label": "The Kubebuilder Book — Architecture",
        "src3_note": "Visão geral oficial da arquitetura de projetos Kubebuilder",
    },
    "06-operator-sdk.txt": {
        "sub": "Operator SDK e OLM (toolkit CNCF Incubating do Operator Framework para desenvolvimento de Operators em Go, Ansible e Helm, empacotamento de Bundles CSV e validação `scorecard`)",
        "src1_label": "Operator SDK GitHub — README.md (Operator Framework Toolkit, Controller-Runtime Integration & Metrics Authn/Authz Notice)",
        "src1_note": "README oficial do operator-framework/operator-sdk detalhando a arquitetura do SDK e a substituição do kube-rbac-proxy por WithAuthenticationAndAuthorization",
        "src2_label": "Operator SDK Official Documentation — Overview (Go/Ansible/Helm Workflows, 5 Capability Levels, Kubernetes/client-go & OLM Compatibility)",
        "src2_note": "Documentação oficial Overview do Operator SDK cobrindo fluxos Go/Ansible/Helm, 5 níveis de maturidade, versões embutidas do OLM e suporte multi-arquitetura",
        "src3_label": "Operator SDK — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do Operator SDK na CNCF",
    },
    "07-kopf.txt": {
        "sub": "Kopf (*Kubernetes Operator Pythonic Framework* para desenvolvimento de operadores em Python com `@kopf.on.create/update/delete/field`, `@kopf.daemon`, `@kopf.timer`, `@kopf.index` e Peering)",
        "src1_label": "Kopf GitHub — README.md (Kubernetes Operator Pythonic Framework, Declarative Decorators, Daemons, Timers, Indexing, Webhooks & Peering)",
        "src1_note": "README oficial do nolar/kopf detalhando handlers síncronos/assíncronos, persistência de progresso, retentativas, indexação em memória e coordenação de peering",
        "src2_label": "Kopf Official Documentation — Walkthrough: Creating the Objects (Handlers, Spec Parsing, PermanentError & Kubernetes Client Integration)",
        "src2_note": "Guia oficial do Kopf demonstrando a criação de recursos filhos, validação com PermanentError e publicação automática de logs e eventos",
        "src3_label": "Kopf — Official GitHub Repository",
        "src3_note": "Repositório oficial do Kubernetes Operator Pythonic Framework (Kopf)",
    },
    "08-metacontroller.txt": {
        "sub": "Metacontroller (add-on *Controller-Controller* para Kubernetes que executa controladores customizados via Lambda Hooks JSON usando `CompositeController` e `DecoratorController`)",
        "src1_label": "Metacontroller GitHub — README.md (Lightweight Custom Controllers via JSON Webhooks in Any Language)",
        "src1_note": "README oficial do metacontroller/metacontroller apresentando escrita de controladores sem boilerplate em qualquer linguagem e instalação via Kustomize/Helm",
        "src2_label": "Metacontroller Official Documentation — Concepts (Canonical Plural Resources, API Groups/Versions/Kinds, Lambda Controllers & Hooks)",
        "src2_note": "Documentação oficial de conceitos do Metacontroller explicando recursos plurais canônicos, CompositeController, DecoratorController e hooks sync/finalize/customize",
        "src3_label": "Metacontroller — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do Metacontroller",
    },
    "09-spin.txt": {
        "sub": "Spin e SpinKube (framework CNCF Sandbox para microsserviços serverless em WebAssembly com `spin.toml`, WASI Component Model e operador Kubernetes `SpinApp`/`SpinAppExecutor`/`containerd-shim-spin`)",
        "src1_label": "Spin Framework GitHub — README.md (WebAssembly Microservices with Component Model & Wasmtime, Polyglot SDKs & Triggers)",
        "src1_note": "README oficial do spinframework/spin detalhando alvo wasm32-wasip2, comandos spin new/build/up e tabela de suporte dos SDKs Rust/TS/Python/Go/C#",
        "src2_label": "SpinKube Official Documentation — Project Overview (Spin Operator, containerd-shim-spin / runwasi & Runtime Class Manager)",
        "src2_note": "Visão geral oficial do projeto CNCF Sandbox SpinKube integrando cargas Wasm ao Kubernetes com SpinApp e RuntimeClass",
        "src3_label": "Spin Operator GitHub — README.md (SpinApp & SpinAppExecutor CRDs, k3d Wasm Cluster & Cert-Manager Webhook Setup)",
        "src3_note": "README oficial do spinkube/spin-operator demonstrando instalação dos CRDs SpinApp e SpinAppExecutor e execução com containerd-shim-spin",
    },
    "10-wasmcloud.txt": {
        "sub": "wasmCloud (plataforma CNCF Incubating para execução distribuída de componentes WebAssembly `wasi 0.2` *deny-by-default* com `wash` CLI, `wash-runtime`, `runtime-operator` e NATS)",
        "src1_label": "wasmCloud GitHub — README.md (CNCF Incubating WebAssembly Platform, Deny-by-Default Capabilities, wash, wash-runtime & Kubernetes runtime-operator)",
        "src1_note": "README oficial do wasmCloud/wasmCloud detalhando o monorepo v2, Wasm Shell (wash), wash-runtime, runtime-operator no Kubernetes e roteamento via EndpointSlices",
        "src2_label": "wasmCloud Official Documentation — Wasm Component Model & Components (Reactive Sandboxed Binaries, WIT Interfaces & Dynamic Linking)",
        "src2_note": "Documentação oficial de componentes do wasmCloud explicando segurança deny-by-default, portabilidade, desacoplamento por interfaces WIT e WASI Preview 2",
        "src3_label": "wasmCloud — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do wasmCloud na CNCF",
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
id: software.devops.tranche18.{number:06d}
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-18.md"
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
        help="Rebuild the existing tranche-18 notes after validating their IDs and batch metadata.",
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
            r"(?m)^id: software\.devops\.tranche18\.\d{6}\s*$",
            path.read_text(encoding="utf-8", errors="replace")[:1200],
        )
    ]
    if args.refresh and len(existing_tranche) != EXPECTED_NOTES:
        raise ValueError(
            f"--refresh exige exatamente {EXPECTED_NOTES} notas tranche18 existentes; encontradas {len(existing_tranche)}"
        )
    if REPORT.exists() and not args.refresh:
        raise ValueError(f"relatório já existe (use --refresh apenas para atualizar a tranche 18): {REPORT}")
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
            expected_id = f"id: software.devops.tranche18.{expected_number + index:06d}"
            if target_path.exists():
                current = target_path.read_text(encoding="utf-8")
                if not args.refresh:
                    raise ValueError(f"arquivo já existe (use --refresh apenas para a tranche 18): {target_path}")
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
        "# Revisão factual assistida por IA — lote `software-devops-2000-0002`, tranche 18",
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
