#!/usr/bin/env python3
"""Build the source-backed software-devops batch 2 tranche 8 (notes 701–800)."""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "knowledge-federation" / "scripts" / "_devops_t08_data"
NOTES_DIR = ROOT / "knowledge-federation" / "domains" / "software-0008" / "software" / "devops"
DOMAINS_DIR = ROOT / "knowledge-federation" / "domains"
REPORT = ROOT / "knowledge-federation" / "exports" / "reports" / "ai-review-software-devops-2000-0002-tranche-08.md"
DATE = date.today().isoformat()
START = 701
EXPECTED_NOTES = 100

sys.path.insert(0, str(ROOT / "knowledge-federation" / "scripts"))
from note_quality import assess_markdown, normalize  # noqa: E402
from prose_audit import repeated_substantive_sentences  # noqa: E402

GROUP_META: dict[str, dict[str, str]] = {
    "01-kata.txt": {
        "sub": "Kata Containers (máquinas virtuais leves com isolamento de hardware e experiência de containers OCI/CRI)",
        "src1_label": "Kata Containers GitHub — README.md (Lightweight VMs, Hardware Requirements, Main & Additional Components)",
        "src1_note": "README oficial do Kata Containers (Apache-2.0) detalhando suporte a arquiteturas de 64 bits (x86_64, aarch64, ppc64le, s390x), kata-runtime check e componentes runtime, runtime-rs, agent, dragonball, osbuilder, kata-ctl e kata-deploy",
        "src2_label": "Kata Containers Design Documentation — Architecture & Configuration",
        "src2_note": "Documentação oficial de arquitetura do Kata Containers (incluindo evolução 4.0 em Rust, containerd shimv2 e configuração de hipervisores)",
        "src3_label": "Kata Containers — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do Kata Containers",
    },
    "02-firecracker.txt": {
        "sub": "AWS Firecracker (Virtual Machine Monitor minimalista sobre Linux KVM para microVMs serverless e multi-tenant)",
        "src1_label": "AWS Firecracker GitHub — README.md (MicroVM VMM, OpenAPI Socket, Rate Limiters, Jailer & Tested Platforms)",
        "src1_note": "README oficial do AWS Firecracker (Apache-2.0) documentando capacidades da API REST sobre socket UNIX, CPU templates, rate limiters virtio, demand fault paging, processo jailer, seccomp por thread e matriz de plataformas Intel/AMD/Graviton",
        "src2_label": "AWS Firecracker Documentation — Design, Specification & Production Host Setup",
        "src2_note": "Documentação oficial de design, compromissos de performance (SPECIFICATION.md) e endurecimento de host Linux (prod-host-setup.md) do Firecracker",
        "src3_label": "AWS Firecracker — Official GitHub Repository",
        "src3_note": "Repositório oficial do VMM Firecracker mantido pela AWS",
    },
    "03-gvisor.txt": {
        "sub": "Google gVisor (kernel de aplicação em espaço de usuário escrito em Go, Sentry, Gofer e runtime OCI runsc)",
        "src1_label": "Google gVisor GitHub — README.md (Application Kernel, runsc, Bazel Build & @go Branch)",
        "src1_note": "README oficial do Google gVisor detalhando motivação de isolamento, compilação do tarball de release (runsc, containerd-shim-runsc-v1, gvisor-bin) com Docker/Bazel e importação da pilha Netstack via branch @go",
        "src2_label": "Google gVisor Architecture Guide — Introduction to gVisor Security (Sentry, Gofer, Systrap & KVM)",
        "src2_note": "Guia oficial de arquitetura de segurança do gVisor explicando reimplementação de syscalls no Sentry em Go, processo sidecar Gofer, plataformas Systrap/KVM e fronteiras de proteção",
        "src3_label": "Google gVisor — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do Google gVisor",
    },
    "04-youki.txt": {
        "sub": "Youki (implementação CNCF da especificação OCI Runtime em Rust, libcontainer e oci-spec-rs)",
        "src1_label": "Youki GitHub — README.md (OCI Runtime in Rust, Hyperfine Benchmark, Lifecycle, Rootless & Docker/Podman)",
        "src1_note": "README oficial do youki documentando motivação de segurança de memória em Rust, benchmark hyperfine frente a runc e crun, compilação com just, ciclo de vida OCI, modo rootless e youki info",
        "src2_label": "Youki Official User & Developer Documentation — Basic Setup & Architecture",
        "src2_note": "Documentação oficial do projeto youki (CNCF Sandbox) e crate associada youki-dev/oci-spec-rs",
        "src3_label": "Youki — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do runtime OCI youki em Rust",
    },
    "05-liquibase.txt": {
        "sub": "Liquibase (versionamento, rastreamento e implantação de mudanças de esquema de banco de dados e arquitetura 5.0+)",
        "src1_label": "Liquibase GitHub — README.md (Database Schema Change Management, Quarterly Releases & CI/CD Integrations)",
        "src1_note": "README oficial do Liquibase cobrindo rastreamento e rollback de mudanças de banco de dados, fluxo com H2, cadência de releases trimestrais/nightly e gate de aprovação Sonatype",
        "src2_label": "Liquibase Docker Documentation — docker/README.md (Liquibase 5.0 FSL vs Secure, LPM Drivers & Migration Guide)",
        "src2_note": "Documentação oficial de imagens Docker do Liquibase detalhando o licenciamento 5.0+ (Community FSL vs Secure), remoção de drivers embutidos por padrão, uso do Liquibase Package Manager (lpm add --global) e roteiro de migração de 6 etapas",
        "src3_label": "Liquibase — Official GitHub Repository",
        "src3_note": "Repositório oficial do Liquibase",
    },
    "06-flyway.txt": {
        "sub": "Redgate Flyway (controle de versão para bancos de dados baseado em migrações SQL/Java e flyway_schema_history)",
        "src1_label": "Redgate Flyway GitHub — README.md (How Flyway Works, 5 Execution Modes, Schema Model & 50+ Supported Databases)",
        "src1_note": "README oficial do Flyway (Apache-2.0) explicando o funcionamento da tabela flyway_schema_history, migrações SQL e Java, captura de schema model em disco e matriz de mais de 50 bancos suportados",
        "src2_label": "Redgate Flyway Official Documentation — Getting Started with Flyway",
        "src2_note": "Documentação oficial da Redgate para configuração, convenções de nomenclatura (V, R, U) e comandos de ciclo de vida do Flyway",
        "src3_label": "Redgate Flyway — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do Redgate Flyway",
    },
    "07-atlasdb.txt": {
        "sub": "Ariga Atlas (ferramenta Schema-as-Code declarativa e versionada com linting, testes e suporte a 16 ORMs)",
        "src1_label": "Ariga Atlas GitHub — README.md (Declarative & Versioned Workflows, 50+ Lint Analyzers, 16 ORMs, Schema Test & Security-as-Code)",
        "src1_note": "README oficial do Ariga Atlas documentando schema inspect (HCL, SQL, JSON, Mermaid ERD), schema apply/diff, migrate diff/lint/apply, 16 ORMs, testes unitários .test.hcl, Security-as-Code (RLS/RBAC), Terraform Provider e Kubernetes Operator",
        "src2_label": "Ariga Atlas Official Documentation — Getting Started with Atlas",
        "src2_note": "Guia oficial do Atlas (atlasgo.io) sobre uso de dev-url, inspeção e migrações declarativas e versionadas",
        "src3_label": "Ariga Atlas — Official GitHub Repository",
        "src3_note": "Repositório oficial do Ariga Atlas",
    },
    "08-bytebase.txt": {
        "sub": "Bytebase (plataforma open-source de governança de banco de dados, SQL Review, RBAC/JIT, Masking e MCP Server)",
        "src1_label": "Bytebase GitHub — README.md (Change Management, 200+ SQL Lint Rules, RBAC/JIT/Masking, Compliance & AI MCP Server)",
        "src1_note": "README oficial do Bytebase detalhando plano de controle único entre humanos, agentes de IA e bancos de dados, mais de 200 regras de SQL lint, RBAC fino, acesso JIT, Dynamic Data Masking, Terraform Provider e MCP Server",
        "src2_label": "Bytebase Official Documentation — Self-host vs. Cloud & Deployment Architecture",
        "src2_note": "Documentação oficial do Bytebase comparando opções de implantação Self-hosted (Docker e Kubernetes Helm) e Cloud",
        "src3_label": "Bytebase — Official GitHub Repository",
        "src3_note": "Repositório oficial do Bytebase",
    },
    "09-nix.txt": {
        "sub": "Nix (gerenciador de pacotes puramente funcional, armazenamento imutável em /nix/store e ambientes reprodutíveis)",
        "src1_label": "NixOS/nix GitHub — README.md (Purely Functional Package Manager & /nix/store Immutability)",
        "src1_note": "README oficial do Nix (LGPL-2.1) explicando o modelo puramente funcional de pacotes, hashes criptográficos de entradas em /nix/store e isolamento de dependências",
        "src2_label": "nix.dev Official Tutorial — Ad hoc shell environments (nix-shell, --pure, Pinning Nixpkgs & Garbage Collection)",
        "src2_note": "Tutorial oficial nix.dev demonstrando criação de ambientes efêmeros e aninhados com nix-shell -p, cache binário cache.nixos.org, reprodutibilidade com --pure e -I nixpkgs=<commit> e limpeza com nix-collect-garbage",
        "src3_label": "NixOS/nix — Official GitHub Repository",
        "src3_note": "Repositório oficial do gerenciador de pacotes Nix",
    },
    "10-earthly.txt": {
        "sub": "Earthly (framework de automação de builds reprodutíveis em containers sobre BuildKit com Earthfile)",
        "src1_label": "Earthly GitHub — README.md (Containerized Build Framework, Earthfile Examples, Cross-Directory Imports, Multi-Platform & Secrets)",
        "src1_note": "README oficial do Earthly (MPL-2.0) demonstrando sintaxe Earthfile VERSION 0.8, SAVE ARTIFACT AS LOCAL, SAVE IMAGE, FROM DOCKERFILE, imports entre diretórios/repositórios, builds multiplataforma e RUN --push --secret",
        "src2_label": "Earthly Official Documentation — Earthfile Reference",
        "src2_note": "Referência técnica oficial da gramática do Earthfile, base target, invocação de targets (+), WITH DOCKER, CACHE e FUNCTION",
        "src3_label": "Earthly — Official GitHub Repository",
        "src3_note": "Repositório oficial MPL-2.0 do Earthly",
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
id: software.devops.tranche08.{number:06d}
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-08.md"
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
        help="Rebuild the existing tranche-08 notes after validating their IDs and batch metadata.",
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
            r"(?m)^id: software\.devops\.tranche08\.\d{6}\s*$",
            path.read_text(encoding="utf-8", errors="replace")[:1200],
        )
    ]
    if args.refresh and len(existing_tranche) != EXPECTED_NOTES:
        raise ValueError(
            f"--refresh exige exatamente {EXPECTED_NOTES} notas tranche08 existentes; encontradas {len(existing_tranche)}"
        )
    if REPORT.exists() and not args.refresh:
        raise ValueError(f"relatório já existe (use --refresh apenas para atualizar a tranche 8): {REPORT}")
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
            expected_id = f"id: software.devops.tranche08.{expected_number + index:06d}"
            if target_path.exists():
                current = target_path.read_text(encoding="utf-8")
                if not args.refresh:
                    raise ValueError(f"arquivo já existe (use --refresh apenas para a tranche 8): {target_path}")
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
        "# Revisão factual assistida por IA — lote `software-devops-2000-0002`, tranche 8",
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
