#!/usr/bin/env python3
"""Build the source-backed software-testing tranche 23 (notes 1660–1759)."""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "knowledge-federation" / "scripts" / "_tranche23_data"
NOTES_DIR = ROOT / "knowledge-federation" / "domains" / "software-0007" / "software" / "testes"
DOMAINS_DIR = ROOT / "knowledge-federation" / "domains"
REPORT = ROOT / "knowledge-federation" / "exports" / "reports" / "ai-review-software-testes-2000-0001-tranche-23.md"
DATE = date.today().isoformat()
START = 1660
EXPECTED_NOTES = 100

sys.path.insert(0, str(ROOT / "knowledge-federation" / "scripts"))
from note_quality import assess_markdown, normalize  # noqa: E402
from prose_audit import repeated_substantive_sentences  # noqa: E402

SOURCES = {
    # Karma (karma-runner.github.io + GitHub) — test runner for JavaScript in real browsers.
    "kr_readme": ("Karma — README oficial", "https://github.com/karma-runner/karma/blob/master/README.md", "proposta, descontinuação, adaptadores e quando usar"),
    "kr_index": ("Karma — página inicial da documentação", "https://karma-runner.github.io/latest/index.html", "destaques: real devices, remote control, frameworks, CI"),
    "kr_init": ("Karma — Configuration (intro)", "https://github.com/karma-runner/karma/blob/master/docs/intro/02-configuration.md", "assistente karma init, start e overrides de CLI"),
    "kr_config": ("Karma — Configuration file reference", "https://github.com/karma-runner/karma/blob/master/docs/config/01-configuration-file.md", "descoberta do arquivo, File Patterns e opções do objeto de configuração"),
    # JUnit 4 (junit.org + wiki junit-team) — xUnit clássico em modo manutenção.
    "j4_home": ("JUnit 4 — página oficial About", "https://junit.org/junit4/", "modo manutenção, exemplo @Test com Hamcrest e índice de referências"),
    "j4_getting": ("JUnit 4 — Getting started (wiki)", "https://github.com/junit-team/junit4/wiki/Getting-started", "jars, javac/java, JUnitCore e formatos de saída"),
    "j4_fixtures": ("JUnit 4 — Test fixtures (wiki)", "https://github.com/junit-team/junit4/wiki/Test-fixtures", "BeforeClass/AfterClass e Before/After com ordem de exemplo"),
    "j4_assertthat": ("JUnit 4 — Matchers and assertThat (wiki)", "https://github.com/junit-team/junit4/wiki/Matchers-and-assertthat", "origem JMock, importações estáticas de Hamcrest e mensagens de falha"),
    "j4_exception": ("JUnit 4 — Exception testing (wiki)", "https://github.com/junit-team/junit4/wiki/Exception-testing", "assertThrows no 4.13, perigos do expected e ExpectedException deprecada"),
    "j4_timeout": ("JUnit 4 — Timeout for tests (wiki)", "https://github.com/junit-team/junit4/wiki/Timeout-for-tests", "parâmetro timeout, regra Timeout e semântica de interrupt"),
    "j4_rules": ("JUnit 4 — Rules (wiki)", "https://github.com/junit-team/junit4/wiki/Rules", "TemporaryFolder, ExternalResource, ErrorCollector, Verifier e TestWatcher"),
    "j4_param": ("JUnit 4 — Parameterized tests (wiki)", "https://github.com/junit-team/junit4/wiki/Parameterized-tests", "cross-product, @Parameter, nome de casos e parâmetro único"),
    "j4_repo": ("JUnit 4 — repositório GitHub", "https://github.com/junit-team/junit4", "espelho do README/About que declara a descontinuidade do projeto"),
    "j4_assume": ("JUnit 4 — Assumptions with assume (wiki)", "https://github.com/junit-team/junit4/wiki/Assumptions-with-assume", "assumeThat/assumeTrue e efeito em Before"),
    # ApprovalTests.Java (approvals org) — verificação por aprovação.
    "at_readme": ("ApprovalTests.Java — README oficial", "https://github.com/approvals/ApprovalTests.Java/blob/master/README.md", "proposta, compatibilidades, exemplo verifyAll, artefatos aprovados e licença"),
    "at_getting": ("ApprovalTests — tutorial Getting Started", "https://github.com/approvals/ApprovalTests.Java/blob/master/approvaltests/docs/tutorials/GettingStarted.md", "verify, verifyAll, JSON, AWT, combinações, aprovação e reporters"),
    "at_site": ("ApprovalTests — site oficial", "https://approvaltests.com/", "porta de entrada referenciada pelo README"),
    # Go native fuzzing (go.dev) — testing.F na toolchain.
    "gfl_doc": ("Go — Go Fuzzing (documentação oficial)", "https://go.dev/doc/security/fuzz/", "requisitos, modos, saída, falhas, minimização, formato do corpus e glossário"),
    "gfl_issue": ("Go — proposal de fuzzing nativo (issue 44551)", "https://go.dev/issue/44551", "proposal referenciada pela doc oficial"),
    "gfl_cmdgo": ("Go — docs de cmd/go", "https://pkg.go.dev/cmd/go", "flags de fuzzing documentadas no pacote do comando"),
    "gfl_ossfuzz": ("OSS-Fuzz — guia para Go (native fuzzing)", "https://google.github.io/oss-fuzz/getting-started/new-project-guide/go-lang/", "suporte a fuzz tests nativos citado pela doc do Go"),
    # cargo-fuzz (rust-fuzz) — libFuzzer via subcomando cargo.
    "cf_readme": ("cargo-fuzz — README oficial", "https://github.com/rust-fuzz/cargo-fuzz/blob/main/README.md", "instalação, plataformas, subcomandos, workspace e licenças"),
    "cf_book": ("Rust Fuzz Book — tutorial do cargo-fuzz", "https://rust-fuzz.github.io/book/cargo-fuzz/tutorial.html", "init, alvo fuzz_target, saída, crash em artifacts e cargo fuzz list"),
    "cf_trophy": ("Rust Fuzz — trophy case", "https://github.com/rust-fuzz/trophy-case", "lista compartilhada de bugs encontrados, referenciada pelo README"),
    # AFL++ (AFLplusplus) — fuzzing dirigido por cobertura em C/C++.
    "afl_readme": ("AFL++ — README oficial (stable)", "https://github.com/AFLplusplus/AFLplusplus/blob/stable/README.md", "versão 5.03c, licenças, quick start, Docker e branches"),
    "afl_docs": ("AFL++ — índice da documentação", "https://github.com/AFLplusplus/AFLplusplus/blob/stable/docs/README.md", "mapa dos guias: in-depth, binary-only, GUI, value profiling"),
    "afl_depth": ("AFL++ — Fuzzing in depth (guia oficial)", "https://github.com/AFLplusplus/AFLplusplus/blob/stable/docs/fuzzing_in_depth.md", "riscos, compiladores, sanitizers, corpus, execução, dicionários e paralelismo"),
    # boofuzz (jtpereyda) — fuzzing de protocolo de rede.
    "bf_readme": ("boofuzz — README.rst oficial", "https://github.com/jtpereyda/boofuzz/blob/master/README.rst", "sucessão ao Sulley, features, instalação e comunidade"),
    "bf_github": ("boofuzz — repositório oficial", "https://github.com/jtpereyda/boofuzz", "árvore do repositório com monitores, examples e request_definitions"),
    "bf_docs": ("boofuzz — Quickstart (Read the Docs)", "https://boofuzz.readthedocs.io/en/stable/user/quickstart.html", "Session, Target, conexões, Requests, grafo, resultados e exemplos"),
    # Hyperfoil (hyperfoil.io) — benchmark distribuído.
    "hf_home": ("Hyperfoil — página inicial oficial", "https://hyperfoil.io/", "definição e destaques distributed, accurate, versatile, low-allocation"),
    "hf_overview": ("Hyperfoil — Overview", "https://hyperfoil.io/docs/overview/", "licença, distribuição, acurácia e versatilidade do DSL"),
    "hf_concepts": ("Hyperfoil — Concepts", "https://hyperfoil.io/docs/overview/concepts/", "controller e agents, fases, sessões e cenário/sequências/steps"),
    "hf_quickstart1": ("Hyperfoil — Quickstart 1: First benchmark", "https://hyperfoil.io/docs/getting-started/quickstart1/", "download, start-local, upload, run e stats"),
    "hf_docs": ("Hyperfoil — índice da documentação", "https://hyperfoil.io/docs/", "nove seções: overview, quickstarts, user guide, API REST, extensions"),
    # Infection (infection.github.io) — mutation testing para PHP.
    "if_intro": ("Infection — Introduction do guia oficial", "https://infection.github.io/guide/", "mutation testing, os cinco passos, métricas MSI/MCC e playground"),
    "if_install": ("Infection — Installation", "https://infection.github.io/guide/installation.html", "phar assinado, phive, composer, brew e tabela de compatibilidade"),
    "if_cli": ("Infection — Command line options", "https://infection.github.io/guide/command-line-options.html", "threads, test-framework, coverage, git-diff e loggers"),
    "if_mutators": ("Infection — Mutators", "https://infection.github.io/guide/mutators.html", "famílias de mutadores AST e o comando describe"),
    # Atheris (google) — fuzzing nativo de Python.
    "ath_readme": ("Atheris — README oficial", "https://github.com/google/atheris/blob/master/README.md", "definição, instalação, instrumentação, API e mutators custom"),
    "ath_native": ("Atheris — Native Extension Fuzzing", "https://github.com/google/atheris/blob/master/native_extension_fuzzing.md", "documento dedicado à instrumentação de extensões nativas"),
    "ath_libfuzzer": ("LLVM — LibFuzzer documentation", "https://llvm.org/docs/LibFuzzer.html#options", "lista de flags consumidas pelo Setup, referenciada pelo README"),
    "ath_fuzzingdocs": ("google/fuzzing — Structure-aware fuzzing", "https://github.com/google/fuzzing/blob/master/docs/structure-aware-fuzzing.md", "doc de custom mutators usada como referência pelo README"),
    "ath_ossfuzz": ("OSS-Fuzz — guia para Python", "https://google.github.io/oss-fuzz/getting-started/new-project-guide/python-lang", "integração declarada pela seção de OSS-Fuzz do README"),
    "kr_angular": ("Angular Blog — Moving Angular CLI to Jest and Web Test Runner", "https://blog.angular.io/moving-angular-cli-to-jest-and-web-test-runner-ef85ef69ceca", "anúncio de migração linkado pelo README do Karma"),
    "kr_travis": ("Travis CI — GUI and headless browsers", "https://docs.travis-ci.com/user/gui-and-headless-browsers/#karma-and-firefox-inactivity-timeouts", "página citada pela referência do browserNoActivityTimeout"),
    "gfl_tut": ("Go — Tutorial: Fuzzing with Go", "https://go.dev/doc/tutorial/fuzz", "tutorial profundo indicado na seção Resources da doc oficial"),
    "afl_dockerhub": ("AFL++ — imagem no Docker Hub", "https://hub.docker.com/r/aflplusplus/aflplusplus", "registry da imagem que o README oficial manda puxar"),
    "lf_docs": ("LLVM — libFuzzer documentation", "https://llvm.org/docs/LibFuzzer.html", "motor base de cargo-fuzz e Atheris: corpus, -merge=1, requisitos do fuzz target"),
    "ath_pypi": ("Atheris — página no PyPI", "https://pypi.org/project/atheris/", "distribuição pip citada pela política de versões do README"),
    "ath_covpy": ("coverage.py — documentação oficial", "https://coverage.readthedocs.io/", "ferramenta de visualização referenciada pelo README do Atheris"),
    "ath_pyimport": ("Python — The import system (docs oficiais)", "https://docs.python.org/3/reference/import.html#the-module-cache", "seção 5.3.1: sys.modules é o cache de módulos já importados"),
    "ath_pyargv": ("Python — sys.argv (docs oficiais)", "https://docs.python.org/3/library/sys.html#sys.argv", "lista de argumentos de processo que o Setup do Atheris consome"),
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
id: software.testes.tranche23.{number:06d}
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-23.md"
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
        help="Rebuild the existing tranche-23 notes after validating their IDs and batch metadata.",
    )
    args = parser.parse_args()
    group_files = sorted(DATA_DIR.glob("*.txt"))
    if len(group_files) != 10:
        raise SystemExit(f"Esperados 10 arquivos de grupo; encontrados {len(group_files)}")

    existing_paths = list(DOMAINS_DIR.rglob("*.md"))
    existing_tranche = [
        path for path in existing_paths
        if re.search(
            r"(?m)^id: software\.testes\.tranche23\.\d{6}\s*$",
            path.read_text(encoding="utf-8", errors="replace")[:1200],
        )
    ]
    if args.refresh and len(existing_tranche) != EXPECTED_NOTES:
        raise ValueError(f"--refresh exige exatamente {EXPECTED_NOTES} notas tranche23 existentes; encontradas {len(existing_tranche)}")
    if REPORT.exists() and not args.refresh:
        raise ValueError(f"relatório já existe (use --refresh apenas para atualizar a tranche 23): {REPORT}")
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
            expected_id = f"id: software.testes.tranche23.{expected_number + index:06d}"
            if target_path.exists():
                current = target_path.read_text(encoding="utf-8")
                if not args.refresh:
                    raise ValueError(f"arquivo já existe (use --refresh apenas para a tranche 23): {target_path}")
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
        "# Revisão factual assistida por IA — lote `software-testes-2000-0001`, tranche 23",
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
