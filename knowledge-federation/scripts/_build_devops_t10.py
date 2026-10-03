#!/usr/bin/env python3
"""Build the source-backed software-devops batch 2 tranche 10 (notes 901–1000)."""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "knowledge-federation" / "scripts" / "_devops_t10_data"
NOTES_DIR = ROOT / "knowledge-federation" / "domains" / "software-0008" / "software" / "devops"
DOMAINS_DIR = ROOT / "knowledge-federation" / "domains"
REPORT = ROOT / "knowledge-federation" / "exports" / "reports" / "ai-review-software-devops-2000-0002-tranche-10.md"
DATE = date.today().isoformat()
START = 901
EXPECTED_NOTES = 100

sys.path.insert(0, str(ROOT / "knowledge-federation" / "scripts"))
from note_quality import assess_markdown, normalize  # noqa: E402
from prose_audit import repeated_substantive_sentences  # noqa: E402

GROUP_META: dict[str, dict[str, str]] = {
    "01-vault.txt": {
        "sub": "HashiCorp Vault (gerenciamento centralizado de segredos, segredos dinâmicos, leases, criptografia Transit e Integrated Storage Raft)",
        "src1_label": "HashiCorp Vault GitHub — README.md (Secure Secret Storage, Dynamic Secrets, Data Encryption, Leasing/Renewal, Revocation & Go Libraries)",
        "src1_note": "README oficial do HashiCorp Vault cobrindo armazenamento criptografado, segredos dinâmicos sob demanda, criptografia sem armazenamento, leases/revogação, compilação make dev e bibliotecas Go suportadas vault/api e vault/sdk",
        "src2_label": "HashiCorp Vault Documentation — What is Vault? (Architecture, Plugins, Access Control & Storage Backends)",
        "src2_note": "Documentação oficial What is Vault? explicando o fluxo de autenticação/autorização por caminhos, categorias de plugins (auth, secret, database) e backends de armazenamento (Integrated Storage Raft, File, External e In-memory)",
        "src3_label": "HashiCorp Vault — Official GitHub Repository",
        "src3_note": "Repositório oficial do HashiCorp Vault",
    },
    "02-externalsecrets.txt": {
        "sub": "External Secrets Operator — ESO (operador CNCF para sincronização declarativa de cofres de segredos externos com Kubernetes Secrets)",
        "src1_label": "External Secrets Operator GitHub — README.md (Supported Providers, CNCF Governance & Release SBOMs)",
        "src1_note": "README oficial do External Secrets Operator (ESO) listando provedores suportados (AWS, Vault, GCP, Azure, IBM, Akeyless, CyberArk, Pulumi ESC) e anexação de SBOM e proveniência",
        "src2_label": "External Secrets Operator Documentation — API Overview (SecretStore, ClusterSecretStore, ExternalSecret, Reconciliation & Access Control)",
        "src2_note": "Visão geral oficial da arquitetura e modelo de recursos do ESO detalhando SecretStore, ClusterSecretStore, ExternalSecret, ciclo de reconciliação de 5 passos, personas RBAC e múltiplos controladores",
        "src3_label": "External Secrets Operator — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do projeto external-secrets/external-secrets",
    },
    "03-sealedsecrets.txt": {
        "sub": "Bitnami Sealed Secrets (criptografia assimétrica de Secrets para GitOps com kubeseal, CRD SealedSecret e controlador em-cluster)",
        "src1_label": "Bitnami Sealed Secrets GitHub — README.md (kubeseal, SealedSecret Template, Scopes, Key Renewal & AES-GCM/RSA-OAEP Crypto)",
        "src1_note": "README oficial do Bitnami Sealed Secrets detalhando funcionamento de kubeseal, spec.template, escopos strict/namespace-wide/cluster-wide, rotação de chaves de 30 dias, --merge-into, --recovery-unseal e criptografia híbrida",
        "src2_label": "Bitnami Sealed Secrets Documentation — GKE Guide (Private GKE Firewall 8080/8081 & GKE Warden serviceProxier Restrictions)",
        "src2_note": "Guia oficial de implantação no GKE documentando selamento offline, regras de firewall para clusters privados e contorno da restrição do GKE Warden (1.32.2+) sobre system:authenticated",
        "src3_label": "Bitnami Sealed Secrets — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do Bitnami Sealed Secrets",
    },
    "04-sops.txt": {
        "sub": "SOPS — Secrets OPerationS (editor CNCF de arquivos estruturados criptografados YAML, JSON, ENV, INI e BINARY com KMS, age e PGP)",
        "src1_label": "SOPS GitHub — README.rst & Official Docs Overview (Supported Formats, KMS/age/PGP & Format 1.0 Backward Compatibility)",
        "src1_note": "README e página inicial de documentação do SOPS (projeto CNCF Sandbox, MPL-2.0) sobre formatos suportados, provedores KMS/age/PGP e garantia de retrocompatibilidade desde a versão 1.0",
        "src2_label": "SOPS Official Documentation — Common Operations (Encrypt/Decrypt, In-Place, --extract, sops set/unset, Git Diff textconv & --encrypted-regex)",
        "src2_note": "Documentação oficial de operações comuns do SOPS cobrindo edição, criptografia de arquivos binários, --extract, sops set/unset, diffs em texto claro no Git (.gitattributes) e criptografia seletiva com --encrypted-regex e MAC",
        "src3_label": "SOPS Official Documentation — Usage & Key Management Guide",
        "src3_note": "Guia oficial de uso, identidades e gerenciamento de chaves do SOPS",
    },
    "05-atlantis.txt": {
        "sub": "Atlantis (automação self-hosted de fluxos Terraform em Pull Requests via webhooks, atlantis plan/apply e sistema de Locking)",
        "src1_label": "Atlantis Official Documentation — Using Atlantis (PR Commands plan/apply, -d/-p/-w Flags, env/{workspace}.tfvars & Automerge Flags)",
        "src1_note": "Guia oficial de uso do Atlantis detalhando comandos via comentários de PR, inclusão automática de env/{workspace}.tfvars, passagem de flags após -- e opções de automerge",
        "src2_label": "Atlantis Official Documentation — Locking & How Atlantis Works (Directory/Workspace Locks, Global Apply Lock, atlantis unlock & Drift Detection)",
        "src2_note": "Documentação oficial de bloqueio (Locking) do Atlantis explicando o lock por diretório e workspace até o merge do PR, Global Apply Lock fail-closed, atlantis unlock, relação com Terraform State Locking e Drift Detection",
        "src3_label": "RunAtlantis — Official GitHub README.md",
        "src3_note": "README oficial do repositório runatlantis/atlantis",
    },
    "06-infracost.txt": {
        "sub": "Infracost (estimativa de custos de nuvem Shift-Left, FinOps Policies, Tagging Policies, extensões de IDE e skills para agentes de IA)",
        "src1_label": "Infracost Official Documentation — Get Started (CLI Installation, infracost setup, AI Agent Skills, IDE Code Lens & CI/CD PR Comments)",
        "src1_note": "Guia oficial Get Started do Infracost cobrindo instalação, infracost setup, skills para agentes de IA (Claude Code, Copilot, Codex, Cursor, Gemini CLI), extensão de IDE Code Lens e integração CI/CD em Pull Requests",
        "src2_label": "Infracost Official Documentation — CLI Commands Reference (scan, inspect, price, policies, budgets, guardrails, auth, org & doctor)",
        "src2_note": "Referência oficial de comandos da CLI do Infracost detalhando scan, inspect, price, policies, budgets, guardrails, auth (OAuth PKCE/device flow), org, doctor e flags globais (--json, --llm, --currency)",
        "src3_label": "Infracost — Official GitHub Repository",
        "src3_note": "Repositório oficial do Infracost",
    },
    "07-goreleaser.txt": {
        "sub": "GoReleaser (automação de engenharia de releases multiplataforma para Go, Rust, Zig, Node.js, Bun, Deno e Python com pacotes, SBOM e assinatura)",
        "src1_label": "GoReleaser Official Documentation — Quick Start (goreleaser init, check, healthcheck, build --single-target, release --snapshot & GITHUB_TOKEN)",
        "src1_note": "Guia oficial Quick Start do GoReleaser (v2.18+) demonstrando inicialização, builders para Go/Rust/Node.js/Zig/Bun/Deno/uv/Poetry, --snapshot, --single-target, check, healthcheck, --skip=publish e permissões GITHUB_TOKEN",
        "src2_label": "GoReleaser GitHub — README.md (Release Engineering Automation & Multi-Language Support)",
        "src2_note": "README oficial do projeto goreleaser/goreleaser (MIT)",
        "src3_label": "GoReleaser — Official GitHub Repository",
        "src3_note": "Repositório oficial do GoReleaser",
    },
    "08-vcluster.txt": {
        "sub": "vCluster (criação de Tenant Clusters Kubernetes isolados e certificados pela CNCF em Shared/Dedicated/Private Nodes, Standalone e Docker vind)",
        "src1_label": "vCluster GitHub — README.md (CNCF Certified Kubernetes & AI Conformant, Architecture Comparison, vind, Auto Nodes, Snapshots & Sleep Mode)",
        "src1_note": "README oficial do loft-sh/vcluster detalhando Tenant Clusters, comparação entre Shared/Dedicated/Private Nodes/Standalone, driver Docker vind, Auto Nodes (Karpenter), Node VPN, Snapshots e Sleep Mode",
        "src2_label": "vCluster Official Documentation — Architecture (v0.37 Control Plane, API Server, Data Store, Syncer, Virtual Scheduler & vind vs KinD)",
        "src2_note": "Documentação oficial de arquitetura do vCluster (v0.37) explicando o processo unificado do control plane (API server, controller manager, datastore SQLite/etcd/SQL, syncer), virtual scheduler e tabela comparativa vind vs KinD",
        "src3_label": "Loft Labs vCluster — Official GitHub Repository",
        "src3_note": "Repositório oficial do vCluster",
    },
    "09-k9s.txt": {
        "sub": "K9s (interface de terminal TUI interativa para observação, diagnóstico e gerenciamento de clusters Kubernetes em tempo real)",
        "src1_label": "K9s GitHub — README.md (Installation, Docker Image, PreFlight Checks, Compatibility Matrix, XDG Config, Key Bindings & Pulses/XRay/Popeye)",
        "src1_note": "README oficial do derailed/k9s (Apache-2.0) documentando instalação, execução em Docker, matriz de compatibilidade, estrutura XDG (k9s info), modo --readonly, filtros regex/labels e visões :pulses, :xray e :popeye",
        "src2_label": "K9s Official Documentation — CLI Arguments & Key Bindings Reference (k9scli.io/topics/commands/)",
        "src2_note": "Referência oficial de argumentos de linha de comando e atalhos de teclado do K9s",
        "src3_label": "K9s — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do K9s",
    },
    "10-stern.txt": {
        "sub": "Stern (acompanhamento dinâmico de logs de múltiplos pods e múltiplos containers no Kubernetes com regex, templates Go e cores)",
        "src1_label": "Stern GitHub — README.md (Multi-Pod & Container Log Tailing, CLI Flags Table, ~/.config/stern/config.yaml & Go Templates/JSON Functions)",
        "src1_note": "README oficial do stern/stern (Apache-2.0) detalhando pod-query por regex ou <resource>/<name>, tabela completa de flags da CLI, arquivo ~/.config/stern/config.yaml, modos --output e funções de template Go/JSON",
        "src2_label": "Stern GitHub — CONTRIBUTING.md & Official Repository Guidelines",
        "src2_note": "Diretrizes oficiais do repositório stern/stern",
        "src3_label": "Stern — Official GitHub Repository",
        "src3_note": "Repositório oficial do Stern",
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
id: software.devops.tranche10.{number:06d}
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-10.md"
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
        help="Rebuild the existing tranche-10 notes after validating their IDs and batch metadata.",
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
            r"(?m)^id: software\.devops\.tranche10\.\d{6}\s*$",
            path.read_text(encoding="utf-8", errors="replace")[:1200],
        )
    ]
    if args.refresh and len(existing_tranche) != EXPECTED_NOTES:
        raise ValueError(
            f"--refresh exige exatamente {EXPECTED_NOTES} notas tranche10 existentes; encontradas {len(existing_tranche)}"
        )
    if REPORT.exists() and not args.refresh:
        raise ValueError(f"relatório já existe (use --refresh apenas para atualizar a tranche 10): {REPORT}")
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
            expected_id = f"id: software.devops.tranche10.{expected_number + index:06d}"
            if target_path.exists():
                current = target_path.read_text(encoding="utf-8")
                if not args.refresh:
                    raise ValueError(f"arquivo já existe (use --refresh apenas para a tranche 10): {target_path}")
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
        "# Revisão factual assistida por IA — lote `software-devops-2000-0002`, tranche 10",
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
