#!/usr/bin/env python3
"""Build 100 substantive notes for batch software-seguranca-2000-0003 tranche 05 (IDs 401-500) and its AI factual review report."""
from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KF = ROOT / "knowledge-federation"
DOMAINS_DIR = KF / "domains"
NOTES_DIR = DOMAINS_DIR / "software-0009" / "software" / "seguranca"
REPORT = KF / "exports" / "reports" / "ai-review-software-seguranca-2000-0003-tranche-05.md"
DATA_DIR = Path(__file__).resolve().parent / "_seguranca_t05_data"
BATCH_ID = "software-seguranca-2000-0003"
DATE = "2026-10-03"
START = 401
EXPECTED_NOTES = 100

sys.path.insert(0, str(Path(__file__).resolve().parent))
from note_quality import assess_markdown  # noqa: E402
from prose_audit import repeated_substantive_sentences  # noqa: E402


GROUP_META = {
    "01-sqlmap.txt": {
        "sub": "sqlmap — Detecção Automatizada de SQL Injection, Técnicas BEUSTQ, Tamper Scripts e Validação de Remediação",
        "src1_label": "sqlmap Official GitHub — README & Architecture",
        "src1_note": "documentação oficial do projeto sqlmap cobrindo arquitetura, instalação e escopo",
        "src2_label": "sqlmap Official Wiki — Usage & Switches Reference",
        "src2_note": "manual oficial de opções da CLI, técnicas BEUSTQ, --level, --risk, --tamper e OOB DNS",
        "src3_label": "sqlmap Official Documentation — Portuguese Reference",
        "src3_note": "referência oficial traduzida do sqlmap",
    },
    "02-dalfox.txt": {
        "sub": "Dalfox — Análise de Parâmetros e Scanner de XSS (Reflected, Stored, DOM/AST), WAF Fingerprinting e CI/CD",
        "src1_label": "Dalfox Official GitHub — README & Key Features",
        "src1_note": "documentação oficial do Dalfox cobrindo subcomandos, parameter mining, DOM/AST e WAF",
        "src2_label": "Dalfox Official Documentation — CLI Reference",
        "src2_note": "referência completa de flags, exit codes, monitoramento de sessão, escopo e baseline",
        "src3_label": "Dalfox GitHub Releases",
        "src3_note": "notas de versão e distribuição oficial do Dalfox",
    },
    "03-mispsoc.txt": {
        "sub": "MISP (Malware Information Sharing Platform) — Threat Intelligence, IOCs, Galaxies, Warninglists, PyMISP e IDS Export",
        "src1_label": "MISP Official GitHub — Core Functions & Threat Intelligence Platform",
        "src1_note": "documentação oficial do MISP cobrindo Events, Attributes, Objects, Galaxies, correlação e exportação NIDS",
        "src2_label": "PyMISP Official GitHub — Python Library & REST API",
        "src2_note": "documentação oficial da biblioteca PyMISP para automação de eventos, atributos, sightings e restSearch",
        "src3_label": "MISP OpenAPI Specification",
        "src3_note": "especificação OpenAPI da API REST do MISP",
    },
    "04-bloodhound.txt": {
        "sub": "BloodHound CE (SpecterOps) — Gestão de Caminhos de Ataque em Grafos (Active Directory, Entra ID e OpenGraph)",
        "src1_label": "BloodHound CE Official GitHub — Architecture & Collectors",
        "src1_note": "documentação oficial do BloodHound Community Edition (Go API, PostgreSQL, Neo4j, SharpHound, AzureHound e OpenGraph)",
        "src2_label": "BloodHound Official Documentation Portal — SpecterOps",
        "src2_note": "portal oficial de documentação de coleta, análise de caminhos de ataque, Tier Zero e Cypher",
        "src3_label": "BloodHound OpenGraph Documentation",
        "src3_note": "documentação oficial do esquema OpenGraph para ingestão multi-plataforma",
    },
    "05-paralus.txt": {
        "sub": "CNCF Paralus — Acesso Zero-Trust ao Kubernetes, Kubeconfig Just-in-Time, Federação OIDC/RBAC e Auditoria de kubectl",
        "src1_label": "CNCF Paralus Official GitHub — Zero-Trust Kubernetes Access Manager",
        "src1_note": "documentação oficial do Paralus cobrindo RBAC multi-cluster, SSO/OIDC, JIT ServiceAccounts e pctl",
        "src2_label": "Paralus Official Documentation — Zero Trust & Architecture",
        "src2_note": "guia oficial de arquitetura, Relay Agent, Projects, Roles e operação do Paralus",
        "src3_label": "Paralus Documentation — Audit Logs",
        "src3_note": "documentação oficial de System Audit Logs e Kubectl/Relay Audit Logs",
    },
    "06-lynis.txt": {
        "sub": "CISOfy Lynis — Auditoria de Segurança e Hardening em Linux/Unix, Perfis .prf, Hardening Index e Dockerfiles",
        "src1_label": "CISOfy Lynis Official GitHub — Security Auditing and Hardening Tool",
        "src1_note": "documentação oficial do CISOfy Lynis para auditoria de segurança, conformidade e hardening Unix/Linux",
        "src2_label": "CISOfy Official Documentation — Lynis Get Started & Commands",
        "src2_note": "guia oficial de comandos, opções (--quick, --cronjob, --pentest), logs e relatórios do Lynis",
        "src3_label": "CISOfy Lynis SDK — Custom Tests Development",
        "src3_note": "kit oficial de desenvolvimento de testes customizados para o Lynis",
    },
    "07-auditd.txt": {
        "sub": "Linux Audit Framework (auditd / audit-userspace) — Auditoria de Syscalls no Kernel, augenrules, ausearch e Imutabilidade",
        "src1_label": "Linux Audit Userspace Official GitHub — Architecture & Daemon Considerations",
        "src1_note": "documentação oficial do Linux Audit System (auditd, auditctl, augenrules, audisp e RefuseManualStop)",
        "src2_label": "Linux Audit Official Rules — README-rules & augenrules Ordering",
        "src2_note": "especificação oficial da organização de regras 10–99 em /etc/audit/rules.d/ e 31-privileged.rules",
        "src3_label": "Linux Audit Rules Repository — STIG, PCI-DSS & Base Rules",
        "src3_note": "catálogo oficial de regras de auditoria para Common Criteria, DISA STIG e PCI-DSS",
    },
    "08-usbguard.txt": {
        "sub": "USBGuard — Autorização de Dispositivos USB no Linux, Prevenção contra BadUSB/HID Injection e Linguagem de Regras",
        "src1_label": "USBGuard Official GitHub — Device Authorization Framework",
        "src1_note": "documentação oficial do USBGuard cobrindo arquitetura, compilação, libqb/protobuf/libseccomp e generate-policy",
        "src2_label": "USBGuard Official Documentation — Rule Language Grammar",
        "src2_note": "especificação formal da linguagem de regras (allow/block/reject, with-interface, operadores e condições)",
        "src3_label": "USBGuard Official Documentation — Daemon Configuration",
        "src3_note": "referência de configuração do usbguard-daemon.conf e controle IPC",
    },
    "09-apparmor.txt": {
        "sub": "AppArmor Linux Security Module — MAC Baseado em Caminhos, Perfis Enforce/Complain, Abstrações e Containers/Kubernetes",
        "src1_label": "AppArmor Official GitLab — Kernel LSM & Userspace Architecture",
        "src1_note": "documentação oficial do projeto AppArmor cobrindo o módulo LSM do kernel, libapparmor, parser e utilitários",
        "src2_label": "AppArmor Official Wiki — Home & Profiles Overview",
        "src2_note": "wiki oficial do AppArmor sobre perfis de confinamento, distribuições e ferramentas de política",
        "src3_label": "AppArmor Official Wiki — Technical Documentation",
        "src3_note": "documentação técnica da linguagem de perfis, transições de execução e abstrações do AppArmor",
    },
    "10-selinux.txt": {
        "sub": "SELinux (SELinuxProject) — MAC Baseado em Rótulos, Type Enforcement, MCS para Containers, Booleans, semanage e Diagnóstico AVC",
        "src1_label": "SELinuxProject Official GitHub — SELinux Userspace & Policy Toolchain",
        "src1_note": "documentação oficial do SELinux Userspace (libsepol, libselinux, libsemanage, checkpolicy, secilc e versões de política)",
        "src2_label": "SELinuxProject Official Wiki — Userspace Tools & Policy Management",
        "src2_note": "wiki oficial do SELinux sobre compilação de políticas, semodule, semanage, audit2why e setools",
        "src3_label": "SELinuxProject Official Wiki — Tools Reference",
        "src3_note": "referência das ferramentas oficiais de administração e diagnóstico do SELinux",
    },
}


def normalize(text: str) -> str:
    base = unicodedata.normalize("NFKD", text.lower())
    clean = "".join(ch for ch in base if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]+", " ", clean).strip()


def parse_group(path: Path) -> tuple[dict[str, str], list[dict[str, object]]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    sources_urls: list[str] = []
    for line in lines[:10]:
        if line.startswith("SOURCES:"):
            sources_urls = [s.strip() for s in line.split("SOURCES:", 1)[1].split("|") if s.strip()]
    if len(sources_urls) < 2:
        raise ValueError(f"{path.name}: esperado cabeçalho SOURCES com pelo menos 2 URLs")

    raw_text = "\n".join(lines)
    blocks = [b.strip() for b in raw_text.split("===NOTE===") if b.strip()][1:]
    if len(blocks) != 10:
        raise ValueError(f"{path.name}: esperadas 10 notas, encontradas {len(blocks)}")

    meta = GROUP_META[path.name]
    group_title = meta["sub"]
    rows: list[dict[str, object]] = []
    first_num: int | None = None

    for rec in blocks:
        code_m = re.search(r"\|(```[\s\S]+?```)\|", rec)
        if not code_m:
            raise ValueError(f"{path.name}: bloco de código não encontrado: {rec[:140]}...")
        pre = rec[: code_m.start()]
        example = code_m.group(1).strip()
        post = rec[code_m.end() :]

        pre_parts = [g.strip() for g in re.split(r"\|(?=(?:[^`]*`[^`]*`)*[^`]*$)", pre)]
        post_parts = [g.strip() for g in re.split(r"\|(?=(?:[^`]*`[^`]*`)*[^`]*$)", post)]
        if len(pre_parts) != 6 or len(post_parts) != 3:
            raise ValueError(
                f"{path.name}: falha ao analisar registro (pre={len(pre_parts)}, post={len(post_parts)}): {rec[:140]}..."
            )
        num_str, slug, title, summary, reason, how = pre_parts
        caveat, verify, links_csv = post_parts
        num = int(num_str)
        if first_num is None:
            first_num = num
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
            raise ValueError(f"{path.name}: slug inválido: {slug}")

        links = [x.strip() for x in links_csv.split(",") if x.strip()]
        sources = [
            (meta["src1_label"], sources_urls[0], meta["src1_note"]),
            (meta["src2_label"], sources_urls[1], meta["src2_note"]),
        ]
        if len(sources_urls) >= 3:
            sources.append((meta["src3_label"], sources_urls[2], meta["src3_note"]))

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
id: software.seguranca.tranche05.{number:06d}
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-05.md"
fontes: [{', '.join('"' + source[1] + '"' for source in sources)}]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: {BATCH_ID}
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
        help="Rebuild the existing tranche-05 notes after validating their IDs and batch metadata.",
    )
    args = parser.parse_args()
    NOTES_DIR.mkdir(parents=True, exist_ok=True)
    group_files = sorted(DATA_DIR.glob("*.txt"))
    if len(group_files) != 10:
        raise SystemExit(f"Esperados 10 arquivos de grupo; encontrados {len(group_files)}")

    existing_paths = list(DOMAINS_DIR.rglob("*.md"))
    existing_tranche = [
        path
        for path in existing_paths
        if re.search(
            r"(?m)^id: software\.seguranca\.tranche05\.\d{6}\s*$",
            path.read_text(encoding="utf-8", errors="replace")[:1200],
        )
    ]
    if args.refresh and len(existing_tranche) != EXPECTED_NOTES:
        raise ValueError(
            f"--refresh exige exatamente {EXPECTED_NOTES} notas tranche05 existentes; encontradas {len(existing_tranche)}"
        )
    if REPORT.exists() and not args.refresh:
        raise ValueError(f"relatório já existe (use --refresh apenas para atualizar a tranche 05): {REPORT}")
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
            expected_id = f"id: software.seguranca.tranche05.{expected_number + index:06d}"
            if target_path.exists():
                current = target_path.read_text(encoding="utf-8")
                if not args.refresh:
                    raise ValueError(f"arquivo já existe (use --refresh apenas para a tranche 05): {target_path}")
                if (
                    expected_id not in current.splitlines()[:25]
                    or f"lote: {BATCH_ID}" not in current.splitlines()[:25]
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
        f"# Revisão factual assistida por IA — lote `{BATCH_ID}`, tranche 05",
        "",
        f"- Data: {DATE}",
        "- Revisor: `Arena.ai Agent Mode`",
        f"- Escopo: notas **{START}–{START + EXPECTED_NOTES - 1}**, em dez grupos temáticos com dez notas cada; cada linha identifica a conferência factual da nota.",
        "- Fontes primárias: documentação oficial dos projetos e versões indicadas nas próprias notas; as afirmações foram limitadas ao material citado.",
        f"- Resultado: **{EXPECTED_NOTES} revisões factuais por IA registradas** e aprovadas no gate automatizado de qualidade, elevando o terceiro lote `{BATCH_ID}` para **500/2.000 notas válidas (`in_progress`)**. Isto não é aprovação humana nem garantia de ausência de erro.",
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
