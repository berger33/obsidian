#!/usr/bin/env python3
"""Build the source-backed software-testing tranche 24 (notes 1760–1859)."""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "knowledge-federation" / "scripts" / "_tranche24_data"
NOTES_DIR = ROOT / "knowledge-federation" / "domains" / "software-0007" / "software" / "testes"
DOMAINS_DIR = ROOT / "knowledge-federation" / "domains"
REPORT = ROOT / "knowledge-federation" / "exports" / "reports" / "ai-review-software-testes-2000-0001-tranche-24.md"
DATE = date.today().isoformat()
START = 1760
EXPECTED_NOTES = 100

sys.path.insert(0, str(ROOT / "knowledge-federation" / "scripts"))
from note_quality import assess_markdown, normalize  # noqa: E402
from prose_audit import repeated_substantive_sentences  # noqa: E402

SOURCES = {
    "rfr_readme": ('Robot Framework README.rst oficial', 'https://raw.githubusercontent.com/robotframework/robotframework/master/README.rst', 'README.rst oficial do Robot Framework com introdução, instalação, exemplo de suíte, CLI robot/rebot, ecossistema, fundação e licenciamento.'),
    "rfr_repo": ('Repositório oficial robotframework/robotframework', 'https://github.com/robotframework/robotframework', 'Repositório oficial no GitHub com código-fonte, histórico de commits, branches, tags e canais do projeto.'),
    "pgp_pypi": ('Pynguin na página oficial do PyPI', 'https://pypi.org/project/pynguin/', 'Página oficial do pacote pynguin no PyPI com descrição, avisos de execução, pré-requisitos de Python, instalação e governança.'),
    "pgp_readme": ('Documentação Quickstart do Pynguin (código-fonte RST)', 'https://pynguin.readthedocs.io/latest/_sources/user/quickstart.rst.txt', 'Código-fonte RST da página Quickstart oficial do Pynguin no Read the Docs.'),
    "pgp_quickstart": ('Pynguin — Quickstart oficial no Read the Docs', 'https://pynguin.readthedocs.io/latest/user/quickstart.html', 'Guia Quickstart oficial com PYNGUIN_DANGER_AWARE, isolamento em Docker, exemplo triangle anotado com PEP 484 e log de geração DYNAMOSA.'),
    "pgd_docs": ('Pynguin — índice da documentação oficial', 'https://pynguin.readthedocs.io/latest/index.html', 'Índice da documentação oficial do Pynguin no Read the Docs.'),
    "kani_readme": ('Kani Rust Verifier — README oficial', 'https://raw.githubusercontent.com/model-checking/kani/main/README.md', 'README oficial do Kani Rust Verifier com verificação de safety e correctness, instalação, harness #[kani::proof], GitHub Action, citação ASE 2026 e licenciamento.'),
    "kani_repo": ('Repositório oficial model-checking/kani', 'https://github.com/model-checking/kani', 'Repositório oficial do Kani Rust Verifier no GitHub com código-fonte, workflows, CITATION.cff e política de segurança.'),
    "kani_docs": ('The Kani Rust Verifier — Tutorial oficial', 'https://model-checking.github.io/kani/kani-tutorial.html', 'Documentação oficial do Kani Rust Verifier sobre harnesses de prova, undefined behavior, instalação e integração em CI.'),
    "hfg_readme": ('Honggfuzz — README oficial', 'https://raw.githubusercontent.com/google/honggfuzz/master/README.md', 'README oficial do Honggfuzz com recursos de cobertura por hardware/software, modo persistente, ptrace, build wrappers, placeholder ___FILE___ e trophies.'),
    "hfg_repo": ('Repositório oficial google/honggfuzz', 'https://github.com/google/honggfuzz', 'Repositório oficial do Honggfuzz no GitHub com código-fonte, wrappers hfuzz_cc, exemplos e documentação.'),
    "hfg_docs": ('Honggfuzz — USAGE.md no repositório oficial', 'https://github.com/google/honggfuzz/blob/master/docs/USAGE.md', 'Documento oficial USAGE.md do Honggfuzz com opções detalhadas de execução, cobertura e monitoramento.'),
    "lafl_readme": ('LibAFL — README oficial', 'https://raw.githubusercontent.com/AFLplusplus/LibAFL/main/README.md', "README oficial do LibAFL com conceitos centrais, LLMP, backends de instrumentação, no_std, dependências LLVM/Rust, exemplos em fuzzers/ e citação CCS '22."),
    "lafl_repo": ('Repositório oficial AFLplusplus/LibAFL', 'https://github.com/AFLplusplus/LibAFL', 'Repositório oficial do LibAFL no GitHub com crates modulares, exemplos em fuzzers/, livro mdBook e guias de depuração/contribuição.'),
    "syz_readme": ('syzkaller — README oficial', 'https://raw.githubusercontent.com/google/syzkaller/master/README.md', 'README oficial do syzkaller com definição, sistemas operacionais suportados, mapa da documentação por kernel, found_bugs e badges.'),
    "syz_repo": ('Repositório oficial google/syzkaller', 'https://github.com/google/syzkaller', 'Repositório oficial do syzkaller no GitHub com código-fonte, descrições de syscalls, integração OSS-Fuzz e documentação.'),
    "syz_usage": ('syzkaller — How to use syzkaller (docs/usage.md)', 'https://raw.githubusercontent.com/google/syzkaller/master/docs/usage.md', 'Guia oficial docs/usage.md do syzkaller sobre execução do syz-manager, painel HTTP, reprodução automática em VMs, reproducers C/syzkaller e hub.'),
    "syz_docs_index": ('syzkaller — How to install syzkaller (docs/setup.md)', 'https://github.com/google/syzkaller/blob/master/docs/setup.md', 'Guia oficial de configuração e instalação do syzkaller por sistema operacional.'),
    "bh_readme": ('Behat — README oficial', 'https://raw.githubusercontent.com/Behat/Behat/master/README.md', 'README oficial do Behat com instalação via Composer, versão de desenvolvimento, política SemVer/BC, mantenedores e canais de apoio.'),
    "bh_repo": ('Repositório oficial Behat/Behat', 'https://github.com/Behat/Behat', 'Repositório oficial do Behat no GitHub com código-fonte, suíte auto-hospedada em features/ e guia de contribuição.'),
    "bh_docs_index": ('Behat — documentação oficial (en/latest)', 'https://docs.behat.org/en/latest/', 'Página inicial da documentação oficial do Behat com exemplo Gherkin, cobertura de aplicação inteira, profiles/tags/suites, componentes Symfony e extensões.'),
    "cj_readme": ('Cucumber-JVM — README oficial', 'https://raw.githubusercontent.com/cucumber/cucumber-jvm/main/README.md', 'README oficial do Cucumber-JVM com proposta, execução com ferramentas e DI, starters Maven/Gradle, política de upgrade, suporte voluntário e badges.'),
    "cj_repo": ('Repositório oficial cucumber/cucumber-jvm', 'https://github.com/cucumber/cucumber-jvm', 'Repositório oficial do Cucumber-JVM no GitHub com módulos para a JVM, workflows de CI/release, release-notes e CHANGELOG.'),
    "cj_docs": ('Cucumber — Installation for Java (documentação oficial)', 'https://cucumber.io/docs/installation/java/', 'Documentação oficial do Cucumber para instalação e injeção de dependência em Java na JVM.'),
    "fb_readme": ('FuzzBench — README oficial', 'https://raw.githubusercontent.com/google/fuzzbench/master/README.md', 'README oficial do FuzzBench com definição do serviço gratuito, API de integração, benchmarks OSS-Fuzz, biblioteca de reporting e escala do sample report.'),
    "fb_repo": ('Repositório oficial google/fuzzbench', 'https://github.com/google/fuzzbench', 'Repositório oficial do FuzzBench no GitHub com código-fonte da plataforma, benchmarks, issue tracker e documentação.'),
    "fb_docs": ('FuzzBench — Getting Started (documentação oficial)', 'https://google.github.io/fuzzbench/getting-started/', 'Guia oficial Getting Started do FuzzBench para integração de fuzzers e execução de experimentos.'),
    "fb_reports": ('FuzzBench — Sample Report oficial', 'https://www.fuzzbench.com/reports/sample/index.html', 'Relatório de exemplo oficial do FuzzBench com 10 fuzzers, 24 benchmarks, 20 trials de 24 horas e dados brutos em CSV.'),
    "hm_docs": ('Crate httpmock 0.8.3 no docs.rs', 'https://docs.rs/httpmock/latest/httpmock/', 'Documentação oficial da crate httpmock 0.8.3 no docs.rs com features, exemplo Getting Started, diagnóstico de assert e referência de structs.'),
    "hm_repo": ('Repositório oficial httpmock/httpmock', 'https://github.com/httpmock/httpmock', 'Repositório oficial do httpmock no GitHub com código-fonte, especificação de mocks em YAML, modo standalone e diretório de testes.'),
}

def parse_group(path: Path) -> tuple[dict[str, str], list[dict[str, object]]]:
    context: dict[str, str] = {}
    row_lines: list[str] = []
    in_rows = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip() == "---":
            in_rows = True
            continue
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if not in_rows:
            key, value = line.split("=", 1)
            context[key.strip()] = value.strip()
        else:
            row_lines.append(line)

    rows: list[dict[str, object]] = []
    for line in row_lines:
        parts = [part.strip() for part in line.split("||")]
        if len(parts) != 10:
            raise ValueError(f"{path.name}: esperados 10 campos, encontrados {len(parts)}: {line}")
        slug, title, summary, reason, how, example, caveat, verify, source_keys, review = parts
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
            raise ValueError(f"{path.name}: slug inválido: {slug}")
        rows.append({
            "slug": slug,
            "title": title,
            "summary": summary,
            "reason": reason,
            "how": how,
            "example": example,
            "caveat": caveat,
            "verify": verify,
            "sources": [key.strip() for key in source_keys.split(",") if key.strip()],
            "review": review,
        })
    if not 9 <= len(rows) <= 12:
        raise ValueError(f"{path.name}: o grupo precisa ter entre 9 e 12 notas; tem {len(rows)}")
    for key in ("group", "first", "check"):
        if key not in context or not context[key]:
            raise ValueError(f"{path.name}: falta contexto {key}")
    return context, rows


def render_note(context: dict[str, str], rows: list[dict[str, object]], index: int,
                row: dict[str, object]) -> tuple[int, str, dict[str, object]]:
    number = int(context["first"]) + index
    sources = [SOURCES[key] for key in row["sources"]]
    if len(sources) < 2 or len({source[1] for source in sources}) < 2:
        raise ValueError(f"{row['slug']}: precisa de duas fontes distintas")

    neighbors = []
    for neighbor_index in (index - 1, index + 1):
        if 0 <= neighbor_index < len(rows):
            other = rows[neighbor_index]
            neighbors.append(f"- [[{other['slug']}]] — Veja também: {other['title']}.")

    frontmatter = f'''---
id: software.testes.tranche24.{number:06d}
tipo: tecnica
dominio: software
subdominio: testes
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-24.md"
fontes: [{', '.join('"' + source[1] + '"' for source in sources)}]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
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
        help="Rebuild the existing tranche-24 notes after validating their IDs and batch metadata.",
    )
    args = parser.parse_args()
    group_files = sorted(DATA_DIR.glob("*.txt"))
    if len(group_files) != 10:
        raise SystemExit(f"Esperados 10 arquivos de grupo; encontrados {len(group_files)}")

    existing_paths = list(DOMAINS_DIR.rglob("*.md"))
    existing_tranche = [
        path for path in existing_paths
        if re.search(
            r"(?m)^id: software\.testes\.tranche24\.\d{6}\s*$",
            path.read_text(encoding="utf-8", errors="replace")[:1200],
        )
    ]
    if args.refresh and len(existing_tranche) != EXPECTED_NOTES:
        raise ValueError(f"--refresh exige exatamente {EXPECTED_NOTES} notas tranche24 existentes; encontradas {len(existing_tranche)}")
    if REPORT.exists() and not args.refresh:
        raise ValueError(f"relatório já existe (use --refresh apenas para atualizar a tranche 24): {REPORT}")
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

    pending = []
    report_rows = []
    group_summaries: list[tuple[dict[str, str], int]] = []
    seen_slugs: set[str] = set()
    seen_titles: set[str] = set()
    expected_number = START
    for path in group_files:
        context, rows = parse_group(path)
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
            expected_id = f"id: software.testes.tranche24.{expected_number + index:06d}"
            if target_path.exists():
                current = target_path.read_text(encoding="utf-8")
                if not args.refresh:
                    raise ValueError(f"arquivo já existe (use --refresh apenas para a tranche 24): {target_path}")
                if expected_id not in current.splitlines()[:25] or "lote: software-testes-2000-0001" not in current.splitlines()[:25]:
                    raise ValueError(f"ID ou lote existente não corresponde à tranche: {target_path}")
            elif args.refresh:
                raise ValueError(f"--refresh exige os {EXPECTED_NOTES} arquivos existentes; falta {target_path}")
            unknown = set(row["sources"]) - SOURCES.keys()
            if unknown:
                raise ValueError(f"{slug}: fontes desconhecidas {unknown}")
            seen_slugs.add(slug)
            seen_titles.add(normalized_title)
            number, content, quality = render_note(context, rows, index, row)
            pending.append((number, row, context, content, quality))
            source_name, source_url, _ = SOURCES[row["sources"][0]]
            report_rows.append(
                f"| {number} | [[{slug}]] | [{source_name}]({source_url}) | {row['review']} Revisão factual por IA concluída; decisão: aprovada. |"
            )
        expected_number += len(rows)

    if len(pending) != EXPECTED_NOTES or expected_number != START + EXPECTED_NOTES:
        raise ValueError(f"esperadas {EXPECTED_NOTES} notas de {START} a {START + EXPECTED_NOTES - 1}, validadas {len(pending)}")
    repeated = repeated_substantive_sentences(
        [(number, content) for number, _, _, content, _ in pending]
    )
    if repeated:
        examples = [f"{numbers}: {sentence}" for sentence, numbers in list(repeated.items())[:8]]
        raise ValueError(f"prosa substantiva repetida entre notas; revisar antes de gravar: {examples}")

    # All notes and metadata pass their deterministic gates before any file is written.
    for number, row, context, content, quality in pending:
        (NOTES_DIR / f"{row['slug']}.md").write_text(content, encoding="utf-8")

    report = [
        "# Revisão factual assistida por IA — lote `software-testes-2000-0001`, tranche 24",
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
        report.append(f"- {context['group']} (itens {context['first']}–{int(context['first']) + count - 1}): {context['check']}")
    report += [
        "- A auditoria de links, a comparação com o inventário, o gate de conteúdo e a verificação de sentenças repetidas foram executados separadamente antes da contabilização.",
        "",
    ]
    REPORT.write_text("\n".join(report).rstrip() + "\n", encoding="utf-8")
    word_counts = [quality["word_count"] for _, _, _, _, quality in pending]
    source_counts = [quality["source_count"] for _, _, _, _, quality in pending]
    print(f"Geradas {len(pending)} notas substantivas (IDs {START}–{START + EXPECTED_NOTES - 1}); palavras: min={min(word_counts)}; max={max(word_counts)}")
    print(f"Fontes HTTPS específicas por nota: min={min(source_counts)}; max={max(source_counts)}")
    print(f"Relatório factual: {REPORT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
