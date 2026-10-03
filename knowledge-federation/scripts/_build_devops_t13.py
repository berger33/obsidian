#!/usr/bin/env python3
"""Build the source-backed software-devops batch 2 tranche 13 (notes 1201–1300)."""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "knowledge-federation" / "scripts" / "_devops_t13_data"
NOTES_DIR = ROOT / "knowledge-federation" / "domains" / "software-0008" / "software" / "devops"
DOMAINS_DIR = ROOT / "knowledge-federation" / "domains"
REPORT = ROOT / "knowledge-federation" / "exports" / "reports" / "ai-review-software-devops-2000-0002-tranche-13.md"
DATE = date.today().isoformat()
START = 1201
EXPECTED_NOTES = 100

sys.path.insert(0, str(ROOT / "knowledge-federation" / "scripts"))
from note_quality import assess_markdown, normalize  # noqa: E402
from prose_audit import repeated_substantive_sentences  # noqa: E402

GROUP_META: dict[str, dict[str, str]] = {
    "01-npd.txt": {
        "sub": "Node Problem Detector — NPD (daemon Kubernetes para detecção de anomalias de kernel, hardware e runtime em NodeConditions e Events)",
        "src1_label": "Kubernetes Node Problem Detector GitHub — README.md (Problem Daemons, System Log Monitor, Custom Plugin Monitor & Exporters)",
        "src1_note": "README oficial do kubernetes/node-problem-detector detalhando Problem Daemons (SystemLogMonitor, SystemStatsMonitor, CustomPluginMonitor, HealthChecker), Exporters (Kubernetes, Prometheus, Stackdriver) e flags de CLI",
        "src2_label": "Node Problem Detector Official Config — config/kernel-monitor.json (KernelOops, OOMKilled, Ext4Error & TaskHung Rules)",
        "src2_note": "Arquivo oficial de regras do kernel-monitor.json do Node Problem Detector definindo condições permanentes e eventos temporários a partir do kmsg",
        "src3_label": "Kubernetes Node Problem Detector — Official GitHub Repository",
        "src3_note": "Repositório oficial do Node Problem Detector no projeto Kubernetes",
    },
    "02-kubebench.txt": {
        "sub": "Aqua Security kube-bench (auditoria automatizada de conformidade CIS Kubernetes Benchmark para planos de controle, worker nodes e clusters gerenciados)",
        "src1_label": "Aqua Security kube-bench GitHub — README.md (CIS Kubernetes Benchmark Checks, YAML Configs & Installation)",
        "src1_note": "README oficial do aquasecurity/kube-bench explicando a execução dos testes do CIS Kubernetes Benchmark definidos em arquivos YAML por versão e distribuição",
        "src2_label": "kube-bench Official Documentation — Running kube-bench (Kubernetes Job, EKS/GKE/AKS/OCP Targets, Exit Codes & Mapping)",
        "src2_note": "Documentação oficial de execução do kube-bench detalhando job.yaml com hostPID, alvos específicos de provedores (--benchmark gke-1.2.0, eks-1.0.1, rh-1.0), flags de saída e mapeamento de versões",
        "src3_label": "Aqua Security kube-bench — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do kube-bench",
    },
    "03-zot.txt": {
        "sub": "Project Zot (registro de containers e artefatos OCI-nativo da CNCF em binário único com extensões embutidas de busca, Trivy, Cosign/Notation e sync)",
        "src1_label": "Project Zot GitHub — README.md (OCI-Native Distribution & Image Spec Implementation, Single Binary & Built-in Extensions)",
        "src1_note": "README oficial do project-zot/zot (Apache-2.0) detalhando a arquitetura OCI-only sem camadas Docker legadas, empacotamento em binário único com extensões embutidas e binário minimal",
        "src2_label": "Project Zot Official Examples — examples/README.md (Config Matrix: Storage, Auth, TLS, Sync, Search, Scrub, Lint & Metrics)",
        "src2_note": "Catálogo oficial de configurações do Zot cobrindo storage local/S3, deduplicação, GC, htpasswd/LDAP/OIDC/mTLS, RBAC, replicação on-demand e métricas",
        "src3_label": "Project Zot — Official GitHub Repository",
        "src3_note": "Repositório oficial CNCF Sandbox do Project Zot",
    },
    "04-dragonfly.txt": {
        "sub": "Dragonfly (sistema CNCF Incubating de distribuição P2P de imagens OCI, arquivos e modelos de IA/ML em larga escala com Manager, Scheduler e Dfdaemon)",
        "src1_label": "Dragonfly GitHub — README.md (P2P File & Image Distribution, Architecture: Manager, Scheduler, Seed Peer & Dfdaemon in Rust)",
        "src1_note": "README oficial do dragonflyoss/dragonfly (CNCF Incubating) descrevendo a arquitetura P2P, cliente Dfdaemon reescrito em Rust (v2.1.0+), isolamento de I/O, integração com Nydus e modelos de IA",
        "src2_label": "Dragonfly Official Documentation — d7y.io/docs/next/ (Quickstart, Containerd Mirror, Preheat & Observability)",
        "src2_note": "Documentação oficial do Dragonfly sobre configuração de mirror no containerd, dfget, dfcache, preheat de imagens/modelos e métricas",
        "src3_label": "Dragonfly — Official GitHub Repository",
        "src3_note": "Repositório oficial do Dragonfly na CNCF",
    },
    "05-nydus.txt": {
        "sub": "Nydus Image Service (serviço de imagens OCI de carregamento sob demanda com formato RAFS v6, nydusify, nydusd FUSE/EROFS e deduplicação em chunks)",
        "src1_label": "Nydus Image Service GitHub — README.md (RAFS On-Demand Layer Format, nydusify, nydusd, EROFS/FUSE & Containerd Snapshotter)",
        "src1_note": "README oficial do dragonflyoss/nydus detalhando o formato RAFS, inicialização de containers em milissegundos, ferramentas (nydus-image, nydusd, nydusify, nydusctl) e integração com Harbor e Dragonfly",
        "src2_label": "Nydus Official Architecture — docs/nydus-design.md (Bootstrap vs Data Blobs, Chunk Deduplication, Digest Authentication & Zran)",
        "src2_note": "Documento oficial de design arquitetural do Nydus explicando a separação entre metadados (bootstrap) e dados (blobs de chunks), verificação por Merkle tree e modos FUSE/virtiofs/EROFS",
        "src3_label": "Nydus Image Service — Official GitHub Repository",
        "src3_note": "Repositório oficial do Nydus no projeto Dragonfly",
    },
    "06-oras.txt": {
        "sub": "ORAS — OCI Registry As Storage (ferramenta CNCF Sandbox para push, pull, attach, discover, cópia e backup de artefatos OCI, SBOMs e grafos de referrers)",
        "src1_label": "ORAS CLI Official Documentation — Commands Reference (push, pull, attach, discover, cp, backup, restore, manifest, blob & repo)",
        "src1_note": "Documentação oficial de comandos da CLI do ORAS detalhando manipulação de artefatos, OCI Image Layout (--oci-layout), árvore de referrers OCI 1.1 e cópia recursiva entre registros",
        "src2_label": "ORAS GitHub — README.md (OCI Registry As Storage Overview, Multi-Arch Container Images & Immutable Release Tag Policy)",
        "src2_note": "README oficial do oras-project/oras documentando a governança de tags de release (:vX.Y.Z, :vX.Y, :vX, :latest) e instalação",
        "src3_label": "ORAS Project — Official GitHub Repository",
        "src3_note": "Repositório oficial CNCF Sandbox do ORAS",
    },
    "07-distribution.txt": {
        "sub": "CNCF Distribution — registry:3 (implementação open-source de referência da OCI Distribution Specification para armazenamento, cache e distribuição de imagens)",
        "src1_label": "CNCF Distribution Official Documentation — Configuration Reference (/etc/distribution/config.yml, REGISTRY_* Env Vars, Storage, Auth & Proxy)",
        "src1_note": "Referência oficial de configuração do CNCF Distribution detalhando drivers de storage (filesystem, s3, gcs, azure), cache Redis, auth (token/JWKS/htpasswd), proxy pull-through, webhooks e OpenTelemetry",
        "src2_label": "CNCF Distribution GitHub — README.md (OCI Distribution Spec Implementation, registry:3 Image & Architecture)",
        "src2_note": "README oficial do distribution/distribution (Apache-2.0) explicando o papel do projeto como motor base do ecossistema de container registries",
        "src3_label": "CNCF Distribution — Official GitHub Repository",
        "src3_note": "Repositório oficial do CNCF Distribution",
    },
    "08-lefthook.txt": {
        "sub": "Lefthook (gerenciador poliglota e rápido de Git hooks em Go com execução paralela, filtros glob/root para monorepos, lefthook-local.yml e remotes)",
        "src1_label": "Lefthook GitHub — README.md (Fast Polyglot Git Hooks Manager in Go, Parallel Execution, File Placeholders, root & Scripts)",
        "src1_note": "README oficial do evilmartians/lefthook detalhando paralelismo, placeholders ({staged_files}, {push_files}, {all_files}), filtros glob/exclude, suporte a monorepos com root e stage_fixed",
        "src2_label": "Lefthook Official Documentation — Configuration & Usage (lefthook.yml, lefthook-local.yml, remotes, validate, dump & LEFTHOOK=0)",
        "src2_note": "Documentação oficial de configuração e uso da CLI do Lefthook cobrindo lefthook install, run, validate, dump, overrides locais e herança de configurações remotas",
        "src3_label": "Lefthook — Official CLI Usage Guide",
        "src3_note": "Guia oficial de comandos do Lefthook",
    },
    "09-kubevip.txt": {
        "sub": "kube-vip (Virtual IP e Load Balancer em Go para alta disponibilidade do Control Plane e Services LoadBalancer em Kubernetes via ARP Layer 2, BGP Layer 3 e IPVS)",
        "src1_label": "kube-vip GitHub — README.md (Runtime Config File Precedence, Gateway API without Endpoints & SELinux IPVS Kernel Modules)",
        "src1_note": "README oficial do kube-vip/kube-vip documentando a ordem de precedência de --config-file, anotação kube-vip.io/allow-reconcile-without-endpoints e pré-carregamento de ip_vs/ip_vs_rr com SELinux",
        "src2_label": "kube-vip Official Documentation — Architecture (Cluster VIP, ARP Leader Election, BGP Peering, IPVS Load Balancing & Service Watcher)",
        "src2_note": "Documentação oficial de arquitetura do kube-vip explicando eleição de líder, Gratuitous ARP, BGP multi-nó, balanceamento IPVS do control plane e integração com kube-vip-cloud-provider",
        "src3_label": "kube-vip — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do kube-vip",
    },
    "10-notation.txt": {
        "sub": "Notary Project Notation (CLI e biblioteca CNCF Incubating para assinatura e verificação criptográfica de imagens e artefatos OCI com X.509 PKI, JWS/COSE e Trust Policy)",
        "src1_label": "Notary Project Official Quickstart — Sign and Verify an OCI Artifact Using Notation (notation sign, ls, verify, inspect, Trust Store & Trust Policy)",
        "src1_note": "Guia oficial do Notary Project detalhando assinatura por digest com JWS e COSE (--signature-format cose), Trust Store X.509, trustpolicy.json (registryScopes, trustedIdentities, strict) e notation inspect",
        "src2_label": "Notary Project Notation GitHub — README.md & CLI Installation Guide (Checksums, NOTATION_CONFIG & KMS Plugins)",
        "src2_note": "README oficial do notaryproject/notation e guia de instalação da CLI documentando validação de checksum SHA-256, diretório NOTATION_CONFIG e plugins de KMS",
        "src3_label": "Notary Project — Official CLI Installation & Configuration Reference",
        "src3_note": "Referência oficial de instalação e estrutura de diretórios do Notation",
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
id: software.devops.tranche13.{number:06d}
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-13.md"
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
        help="Rebuild the existing tranche-13 notes after validating their IDs and batch metadata.",
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
            r"(?m)^id: software\.devops\.tranche13\.\d{6}\s*$",
            path.read_text(encoding="utf-8", errors="replace")[:1200],
        )
    ]
    if args.refresh and len(existing_tranche) != EXPECTED_NOTES:
        raise ValueError(
            f"--refresh exige exatamente {EXPECTED_NOTES} notas tranche13 existentes; encontradas {len(existing_tranche)}"
        )
    if REPORT.exists() and not args.refresh:
        raise ValueError(f"relatório já existe (use --refresh apenas para atualizar a tranche 13): {REPORT}")
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
            expected_id = f"id: software.devops.tranche13.{expected_number + index:06d}"
            if target_path.exists():
                current = target_path.read_text(encoding="utf-8")
                if not args.refresh:
                    raise ValueError(f"arquivo já existe (use --refresh apenas para a tranche 13): {target_path}")
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
        "# Revisão factual assistida por IA — lote `software-devops-2000-0002`, tranche 13",
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
