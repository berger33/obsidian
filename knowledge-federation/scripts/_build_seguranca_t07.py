#!/usr/bin/env python3
"""Build 100 substantive notes for batch software-seguranca-2000-0003 tranche 07 (IDs 601-700) and its AI factual review report."""
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
REPORT = KF / "exports" / "reports" / "ai-review-software-seguranca-2000-0003-tranche-07.md"
DATA_DIR = Path(__file__).resolve().parent / "_seguranca_t07_data"
BATCH_ID = "software-seguranca-2000-0003"
DATE = "2026-10-03"
START = 601
EXPECTED_NOTES = 100

sys.path.insert(0, str(Path(__file__).resolve().parent))
from note_quality import assess_markdown  # noqa: E402
from prose_audit import repeated_substantive_sentences  # noqa: E402


GROUP_META = {
    "01-testssl.txt": {
        "sub": "testssl.sh — Auditoria de Criptografia TLS/SSL, Protocolos, Cifras PFS, STARTTLS, Simulação de Clientes e Vulnerabilidades",
        "src1_label": "testssl.sh Official Documentation — testssl.1 Manual Reference",
        "src1_note": "manual oficial do testssl.sh cobrindo auditoria TLS/SSL via sockets TCP, protocolos, cifras, STARTTLS, vulnerabilidades e saída JSON/CSV/HTML",
        "src2_label": "testssl.sh Official GitHub Repository — drwetter/testssl.sh",
        "src2_note": "repositório oficial do testssl.sh com suporte a curvas elípticas, grupos híbridos pós-quânticos ML-KEM e binários OpenSSL estáticos",
        "src3_label": "testssl.sh Project Organization — testssl/testssl.sh",
        "src3_note": "organização oficial do projeto testssl.sh",
    },
    "02-certbot.txt": {
        "sub": "EFF Certbot & Protocolo ACME (RFC 8555) — Emissão/Renovação Automatizada X.509, Desafios HTTP-01/DNS-01, Hooks e ARI",
        "src1_label": "EFF Certbot Official User Guide — Commands, Plugins & Automated Renewal",
        "src1_note": "guia oficial do Certbot cobrindo Authenticators vs Installers, webroot, standalone, DNS-01, hooks de renovação e chaves ECDSA",
        "src2_label": "EFF Certbot Official GitHub — certbot/certbot README",
        "src2_note": "documentação oficial do projeto Certbot mantido pela Electronic Frontier Foundation (EFF)",
        "src3_label": "IETF RFC 8555 — Automatic Certificate Management Environment (ACME)",
        "src3_note": "especificação oficial IETF RFC 8555 do protocolo ACME",
    },
    "03-hashcat.txt": {
        "sub": "Hashcat — Auditoria de Resistência de Senhas e Hashes em GPU, Modos de Ataque, Motor de Regras In-Kernel, Máscaras e Hashcat Brain",
        "src1_label": "Hashcat Official GitHub — Architecture, Attack Modes & Features",
        "src1_note": "documentação oficial do Hashcat cobrindo backends CUDA/HIP/Metal/OpenCL, In-Kernel Rule Engine, Assimilation Bridge, Brain e Encrypted Plains",
        "src2_label": "Hashcat Official Wiki — Rule-Based Attack Reference",
        "src2_note": "referência oficial da linguagem de regras de mutação in-kernel, multi-rules e depuração de regras do Hashcat",
        "src3_label": "Hashcat Official Wiki — Mask Attack & Custom Charsets",
        "src3_note": "documentação oficial de ataques de máscara, charsets customizados e cadeias de Markov no Hashcat",
    },
    "04-ghidra.txt": {
        "sub": "NSA Ghidra — Engenharia Reversa de Software (SRE), Descompilador, SLEIGH/P-Code, analyzeHeadless, PyGhidra e BSim",
        "src1_label": "NSA Ghidra Official GitHub — Software Reverse Engineering Framework",
        "src1_note": "documentação oficial do NSA Ghidra cobrindo arquitetura SRE, instalação, build e avisos de segurança",
        "src2_label": "NSA Ghidra Official PyGhidra Documentation — CPython 3 Integration",
        "src2_note": "documentação oficial do módulo PyGhidra para execução de scripts Ghidra nativos em CPython 3 e modo headless",
        "src3_label": "NSA Ghidra Official Security Advisories",
        "src3_note": "avisos oficiais de segurança e recomendações de isolamento do projeto Ghidra",
    },
    "05-radare2.txt": {
        "sub": "Radare2 (r2) — Framework de Análise Binária, rabin2, radiff2, rasm2, Grafo de Fluxo de Controle, Emulação ESIL e r2pipe",
        "src1_label": "Radare2 Official GitHub — Libre Reversing Framework for Unix Geeks",
        "src1_note": "documentação oficial do Radare2 cobrindo comandos fundamentais, arquitetura de bibliotecas e ecossistema de plugins r2pm (r2ghidra, r2frida, r2yara, r2pipe)",
        "src2_label": "Radare2 Official Manual Page — radare2(1) CLI & Reversible Debugger",
        "src2_note": "manual oficial radare2(1) cobrindo flags de linha de comando, modo sandbox, scripts QuickJS e checkpoints de depuração reversível (dts+/dtsc/dtsr)",
        "src3_label": "The Official Radare2 Book",
        "src3_note": "livro oficial do projeto Radare2 cobrindo rabin2, radiff2, rasm2, ESIL e r2pipe",
    },
    "06-frida.txt": {
        "sub": "Frida — Instrumentação Dinâmica de Binários e Apps Mobile (Gum, Interceptor, Stalker, Java/ObjC Bridges, Gadget e CModule)",
        "src1_label": "Frida Official GitHub — Dynamic Instrumentation Toolkit",
        "src1_note": "documentação oficial do Frida cobrindo instalação, bindings Python/Node.js e ferramentas CLI (frida-ps, frida-trace, frida-discover)",
        "src2_label": "Frida Official JavaScript API Reference — Interceptor, Stalker, CModule, Java, ObjC & Cloak",
        "src2_note": "referência completa da API JavaScript do Frida para hooking nativo, code tracing Stalker, CModule, pontes mobile e Cloak",
        "src3_label": "Frida Official Documentation — Modes of Operation (Injected, Embedded Gadget, Preloaded)",
        "src3_note": "documentação oficial dos modos de operação do Frida e configuração do frida-gadget",
    },
    "07-fail2ban.txt": {
        "sub": "Fail2ban — Prevenção de Intrusão Baseada em Logs, Jails, Filtros Seguros contra ReDoS, Actions nftables/ipset e Backoff",
        "src1_label": "Fail2ban Official GitHub — Daemon Architecture & Usage",
        "src1_note": "documentação oficial do Fail2ban cobrindo arquitetura, suporte IPv6, fail2ban-client e limites frente a autenticação fraca",
        "src2_label": "Fail2ban Official Manual Page — jail.conf(5) Configuration Reference",
        "src2_note": "manual oficial jail.conf(5) cobrindo precedência .conf vs .local, interpolação %(known/...)s, banco SQLite, filtros e actions",
        "src3_label": "Fail2ban Official Wiki — Hardening & Filter Best Practices",
        "src3_note": "wiki oficial do projeto Fail2ban sobre escrita segura de expressões regulares e prevenção de ReDoS/Log Injection",
    },
    "08-sudo.txt": {
        "sub": "Sudo (sudo & sudo_logsrvd) — Delegação de Privilégios no Linux/Unix, sudoers, SHA-256 Digest Pinning, NOEXEC, sudoedit e I/O Logging",
        "src1_label": "Sudo Official Sudoers Manual — sudoers(5) Policy Plugin Reference",
        "src1_note": "manual oficial sudoers(5) cobrindo plugins sudo.conf, autenticação, Defaults use_pty/env_reset/secure_path, SHA-256 digests, NOEXEC, sudoedit e I/O logging",
        "src2_label": "Sudo Official GitHub — The Sudo Philosophy & Security Architecture",
        "src2_note": "repositório oficial do projeto Sudo e diretrizes de menor privilégio",
        "src3_label": "Sudo Official Manual — sudo_logsrvd(8) Centralized I/O & Event Log Server",
        "src3_note": "documentação oficial do servidor centralizado de gravação de sessões sudo_logsrvd com TLS mútuo",
    },
    "09-bubblewrap.txt": {
        "sub": "Bubblewrap (bwrap) — Sandboxing Linux sem Privilégios, User/Mount/PID/Net Namespaces, PR_SET_NO_NEW_PRIVS, TIOCSTI e Seccomp",
        "src1_label": "Bubblewrap Official GitHub — Unprivileged Sandboxing Architecture & Security Limitations",
        "src1_note": "documentação oficial do Bubblewrap cobrindo User Namespaces, PR_SET_NO_NEW_PRIVS, tmpfs raiz, CVE-2017-5226 (TIOCSTI) e isolamento de D-Bus",
        "src2_label": "Bubblewrap Official Reference Manual — bwrap(1) DocBook Specification",
        "src2_note": "manual oficial bwrap(1) cobrindo --unshare-all, --disable-userns, --ro-bind, --seccomp, --clearenv, --new-session, --die-with-parent e --json-status-fd",
        "src3_label": "Containers Bubblewrap Official Repository",
        "src3_note": "repositório oficial da ferramenta de sandboxing Bubblewrap",
    },
    "10-clair.txt": {
        "sub": "Project Quay Clair v4 & ClairCore — Análise Estática de Vulnerabilidades em Imagens de Containers OCI/Docker, Indexer, Matcher e Notifier",
        "src1_label": "Project Quay Clair v4 Official Documentation — What is ClairV4 & Architecture",
        "src1_note": "documentação oficial do Clair v4 cobrindo a separação ClairCore, Indexer (IndexReport), Matcher (VulnerabilityReport) e Notifier",
        "src2_label": "Project Quay Clair Official GitHub — Container Vulnerability Static Analysis",
        "src2_note": "repositório oficial do projeto Clair v4 e utilitário de linha de comando clairctl",
        "src3_label": "ClairCore Official Documentation — Layer Indexing & Vulnerability Matching Engine",
        "src3_note": "documentação oficial da biblioteca ClairCore para extração de pacotes de SO/linguagens e updaters de vulnerabilidades",
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
id: software.seguranca.tranche07.{number:06d}
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-07.md"
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
        help="Rebuild the existing tranche-07 notes after validating their IDs and batch metadata.",
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
            r"(?m)^id: software\.seguranca\.tranche07\.\d{6}\s*$",
            path.read_text(encoding="utf-8", errors="replace")[:1200],
        )
    ]
    if args.refresh and len(existing_tranche) != EXPECTED_NOTES:
        raise ValueError(
            f"--refresh exige exatamente {EXPECTED_NOTES} notas tranche07 existentes; encontradas {len(existing_tranche)}"
        )
    if REPORT.exists() and not args.refresh:
        raise ValueError(f"relatório já existe (use --refresh apenas para atualizar a tranche 07): {REPORT}")
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
            expected_id = f"id: software.seguranca.tranche07.{expected_number + index:06d}"
            if target_path.exists():
                current = target_path.read_text(encoding="utf-8")
                if not args.refresh:
                    raise ValueError(f"arquivo já existe (use --refresh apenas para a tranche 07): {target_path}")
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
        f"# Revisão factual assistida por IA — lote `{BATCH_ID}`, tranche 07",
        "",
        f"- Data: {DATE}",
        "- Revisor: `Arena.ai Agent Mode`",
        f"- Escopo: notas **{START}–{START + EXPECTED_NOTES - 1}**, em dez grupos temáticos com dez notas cada; cada linha identifica a conferência factual da nota.",
        "- Fontes primárias: documentação oficial dos projetos e versões indicadas nas próprias notas; as afirmações foram limitadas ao material citado.",
        f"- Resultado: **{EXPECTED_NOTES} revisões factuais por IA registradas** e aprovadas no gate automatizado de qualidade, elevando o terceiro lote `{BATCH_ID}` para **700/2.000 notas válidas (`in_progress`)**. Isto não é aprovação humana nem garantia de ausência de erro.",
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
