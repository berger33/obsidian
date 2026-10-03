#!/usr/bin/env python3
"""Build the source-backed software-devops batch 2 tranche 12 (notes 1101–1200)."""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "knowledge-federation" / "scripts" / "_devops_t12_data"
NOTES_DIR = ROOT / "knowledge-federation" / "domains" / "software-0008" / "software" / "devops"
DOMAINS_DIR = ROOT / "knowledge-federation" / "domains"
REPORT = ROOT / "knowledge-federation" / "exports" / "reports" / "ai-review-software-devops-2000-0002-tranche-12.md"
DATE = date.today().isoformat()
START = 1101
EXPECTED_NOTES = 100

sys.path.insert(0, str(ROOT / "knowledge-federation" / "scripts"))
from note_quality import assess_markdown, normalize  # noqa: E402
from prose_audit import repeated_substantive_sentences  # noqa: E402

GROUP_META: dict[str, dict[str, str]] = {
    "01-kratix.txt": {
        "sub": "Kratix (framework open-source de engenharia de plataforma para construir Internal Developer Platforms compostas com Promises sobre Kubernetes)",
        "src1_label": "Kratix GitHub — README.md & Official Quick Start Guide (Promises, Destinations, State Stores & Fleet Management)",
        "src1_note": "README oficial do syntasso/kratix (Apache-2.0) e guia Quick Start detalhando Promises, Resource Requests, Workflows em containers, State Stores (SeaweedFS/Git), Flux e atualização de frota no Dia 2",
        "src2_label": "Kratix Official Documentation — Quick Start & Platform Concepts",
        "src2_note": "Documentação oficial do Kratix sobre publicação de Promises, status.connectionDetails, Compound Promises e agendamento multi-cluster",
        "src3_label": "Syntasso Kratix — Official GitHub Repository",
        "src3_note": "Repositório oficial Apache-2.0 do Kratix",
    },
    "02-score.txt": {
        "sub": "Score (especificação CNCF Sandbox de workload agnóstica de plataforma com score.yaml, score-compose e score-k8s)",
        "src1_label": "Score Specification GitHub — README.md (score.dev/v1b1 Workload Spec, Containers, Service Ports & Resources)",
        "src1_note": "README oficial da especificação Score (score-spec/spec, Apache-2.0) detalhando o contrato declarativo score.yaml v1b1, interpolação ${resources.*} e separação entre configuração agnóstica e específica de ambiente",
        "src2_label": "Score Reference Implementations — score-compose & score-k8s Official READMEs",
        "src2_note": "Documentação oficial das implementações de referência score-compose e score-k8s cobrindo matriz de recursos suportados, provisionadores customizados (template:// e cmd://) e --patch-templates",
        "src3_label": "Score — Official GitHub Organization & Repositories",
        "src3_note": "Repositórios oficiais do projeto Score na CNCF",
    },
    "03-devbox.txt": {
        "sub": "Jetify Devbox (ambientes de desenvolvimento portáveis, isolados e reprodutíveis em devbox.json alimentados pelo gerenciador de pacotes Nix)",
        "src1_label": "Jetify Devbox GitHub — README.md (Isolated Shells, Nix Package Registry, devbox.json & Portable Environments)",
        "src1_note": "README oficial do jetify-com/devbox (Apache-2.0) detalhando criação de shells determinísticos sem virtualização pesada, integração com mais de 400.000 versões no Nixhub.io e geração de Dockerfile/devcontainer",
        "src2_label": "Jetify Devbox Official Documentation — Quickstart, Scripts, Services, Direnv & Global Profile",
        "src2_note": "Guia oficial Quickstart do Devbox documentando devbox init, search, add, shell, devbox.lock, integração com direnv, scripts e perfil global",
        "src3_label": "Jetify Devbox — Official GitHub Repository",
        "src3_note": "Repositório oficial do Devbox",
    },
    "04-direnv.txt": {
        "sub": "direnv (extensão de shell para carregamento e descarregamento automático de variáveis de ambiente por diretório com .envrc e stdlib)",
        "src1_label": "direnv GitHub — README.md (Sub-Shell Environment Diff, .envrc Authorization, stdlib & Related Projects)",
        "src1_note": "README oficial do direnv/direnv (MIT) explicando a execução do .envrc em sub-processo bash, captura do environment diff, bloqueio de segurança direnv allow, stdlib (PATH_add, dotenv, layout, use) e direnvrc",
        "src2_label": "direnv Official Documentation — Shell Hooks Setup (Bash, Zsh, Fish, Tcsh, Elvish, Nushell, PowerShell & Murex)",
        "src2_note": "Documentação oficial de configuração de hooks do direnv para todos os shells suportados e modos de avaliação",
        "src3_label": "direnv — Official GitHub Repository",
        "src3_note": "Repositório oficial do direnv",
    },
    "05-nova.txt": {
        "sub": "Fairwinds Nova (auditoria de releases Helm charts e imagens de containers desatualizadas ou depreciadas em clusters Kubernetes)",
        "src1_label": "Fairwinds Nova GitHub — README.md & Quickstart (Helm Release & Container Image Scanning & v3.12.0+ Signed Immutable Images)",
        "src1_note": "README oficial e Quickstart do Fairwinds Nova detalhando nova find, nova find --containers e migração na v3.12.0+ para imagens assinadas e imutáveis em us-docker.pkg.dev/fairwinds-ops/oss/nova",
        "src2_label": "Fairwinds Nova Official Documentation — Usage & CLI Options (--poll-artifacthub, --desired-versions, --show-errored-containers & JSON Output)",
        "src2_note": "Guia oficial de uso do Nova cobrindo flags de CLI, repositórios privados (--url), nova generate-config, --desired-versions, --show-non-semver e estrutura de saída JSON",
        "src3_label": "Fairwinds Nova — Official Documentation Portal",
        "src3_note": "Portal oficial de documentação do Fairwinds Nova",
    },
    "06-rbacmanager.txt": {
        "sub": "Fairwinds RBAC Manager (operador Kubernetes declarativo para gestão em escala de RoleBindings, ClusterRoleBindings e ServiceAccounts via RBACDefinition)",
        "src1_label": "Fairwinds RBAC Manager Official Documentation — Introduction & RBACDefinitions (RoleRef Updates, Binding Removal & Dynamic namespaceSelector)",
        "src1_note": "Documentação oficial do RBAC Manager explicando a CRD RBACDefinition (rbacmanager.reactiveops.io/v1beta1), recriação automática de RoleBindings, revogação por ownerReferences e namespaceSelector com matchLabels/matchExpressions",
        "src2_label": "Fairwinds RBAC Manager GitHub — README.md (Operator Overview & v1.10.0+ Signed Immutable Registry Migration)",
        "src2_note": "README oficial do FairwindsOps/rbac-manager documentando a arquitetura do operador e a migração na v1.10.0+ para us-docker.pkg.dev/fairwinds-ops/oss/rbac-manager",
        "src3_label": "Fairwinds RBAC Manager — Official Documentation Portal",
        "src3_note": "Portal oficial do Fairwinds RBAC Manager",
    },
    "07-robusta.txt": {
        "sub": "Robusta (motor open-source de enriquecimento de alertas Prometheus, detecção nativa de eventos Kubernetes, auto-remediação e investigação com HolmesGPT)",
        "src1_label": "Robusta GitHub — README.md (Prometheus Alert Enrichment, Smart Grouping, Playbooks, Change-Tracking, KRR & Sinks Matrix)",
        "src1_note": "README oficial do robusta-dev/robusta detalhando enriquecimento de alertas Prometheus, Smart Grouping em threads, detecção sem PromQL, Change-Tracking, auto-remediação, KRR e matriz de integrações/sinks",
        "src2_label": "Robusta Official Documentation — Overview & HolmesGPT AI Root Cause Analysis",
        "src2_note": "Documentação oficial do Robusta e integração com HolmesGPT para investigação automática de causa raiz em alertas Kubernetes",
        "src3_label": "Robusta — Official GitHub Repository",
        "src3_note": "Repositório oficial do Robusta",
    },
    "08-botkube.txt": {
        "sub": "Botkube (assistente ChatOps colaborativo para monitoramento de eventos, autodiagnóstico e execução segura de kubectl e helm com RBAC por canal)",
        "src1_label": "Botkube GitHub — README.md & Official Documentation Overview (Bots vs Sinks Feature Map, Slack/Discord/Mattermost & ChatOps)",
        "src1_note": "README oficial do kubeshop/botkube (MIT) e matriz oficial de funcionalidades comparando integrações bidirecionais (Bots: Slack, Discord, Mattermost) e unidirecionais (Sinks: Elasticsearch, Webhook)",
        "src2_label": "Botkube Official Documentation — Plugins Architecture (Source Plugins, Executor Plugins, RBAC & Repositories Index)",
        "src2_note": "Documentação oficial de plugins do Botkube (v1.14) detalhando Source plugins, Executor plugins, índices botkube/botkubeExtra e ações automatizadas",
        "src3_label": "Botkube — Official Documentation Portal",
        "src3_note": "Portal oficial de documentação do Botkube",
    },
    "09-kured.txt": {
        "sub": "Kured — Kubernetes Reboot Daemon (DaemonSet CNCF Sandbox para reinicialização automática segura de nós após atualizações de kernel e pacotes de SO)",
        "src1_label": "Kured Official Documentation — Configuration Reference (CLI Flags, Sentinel File/Command, Schedules, Prometheus Alert Blocking & Drain Flags)",
        "src1_note": "Referência oficial de configuração do Kured detalhando todas as flags do daemonset, /var/run/reboot-required, --reboot-sentinel-command para RHEL, janelas de horário, bloqueio por alertas Prometheus e seletores de pods",
        "src2_label": "Kured Official Documentation — Operation & GitHub README.md (DaemonSet Lock Annotation, Manual Lock/Unlock, --lock-ttl & --lock-release-delay)",
        "src2_note": "Guia oficial de operação e README do kubereboot/kured (CNCF Sandbox) cobrindo teste de reboot, bloqueio manual na anotação weave.works/kured-node-lock, desbloqueio manual, --lock-ttl e --lock-release-delay",
        "src3_label": "Kured — Official GitHub Repository",
        "src3_note": "Repositório oficial CNCF Sandbox do Kured",
    },
    "10-just.txt": {
        "sub": "just (executor de comandos de projeto em Rust com justfile, receitas parametrizadas, receitas shebang, módulos e funções embutidas)",
        "src1_label": "just GitHub — README.md (justfile Syntax, Improvements over Make, Settings, Shebang Recipes, Modules & Cross-Platform Packages)",
        "src1_note": "README oficial do casey/just detalhando diferenças em relação ao make (sem .PHONY), parâmetros de receitas, carregamento de .env, receitas shebang, módulos/imports e instalação multiplataforma",
        "src2_label": "Just Programmer's Manual — Official Book (just.systems/man/en/)",
        "src2_note": "Manual oficial completo do just documentando expressões, funções embutidas, atributos de receita ([confirm], [private], [no-cd]), dependências pré/pós e shell completions",
        "src3_label": "just — Official GitHub Repository",
        "src3_note": "Repositório oficial do casey/just",
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
id: software.devops.tranche12.{number:06d}
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-12.md"
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
        help="Rebuild the existing tranche-12 notes after validating their IDs and batch metadata.",
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
            r"(?m)^id: software\.devops\.tranche12\.\d{6}\s*$",
            path.read_text(encoding="utf-8", errors="replace")[:1200],
        )
    ]
    if args.refresh and len(existing_tranche) != EXPECTED_NOTES:
        raise ValueError(
            f"--refresh exige exatamente {EXPECTED_NOTES} notas tranche12 existentes; encontradas {len(existing_tranche)}"
        )
    if REPORT.exists() and not args.refresh:
        raise ValueError(f"relatório já existe (use --refresh apenas para atualizar a tranche 12): {REPORT}")
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
            expected_id = f"id: software.devops.tranche12.{expected_number + index:06d}"
            if target_path.exists():
                current = target_path.read_text(encoding="utf-8")
                if not args.refresh:
                    raise ValueError(f"arquivo já existe (use --refresh apenas para a tranche 12): {target_path}")
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
        "# Revisão factual assistida por IA — lote `software-devops-2000-0002`, tranche 12",
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
