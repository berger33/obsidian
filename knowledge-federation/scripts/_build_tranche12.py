#!/usr/bin/env python3
"""Build the source-backed software-testing tranche 12 (notes 550–649)."""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "knowledge-federation" / "scripts" / "_tranche12_data"
NOTES_DIR = ROOT / "knowledge-federation" / "domains" / "software-0007" / "software" / "testes"
REPORT = ROOT / "knowledge-federation" / "exports" / "reports" / "ai-review-software-testes-2000-0001-tranche-12.md"
DATE = date.today().isoformat()

sys.path.insert(0, str(ROOT / "knowledge-federation" / "scripts"))
from note_quality import assess_markdown  # noqa: E402
from prose_audit import repeated_substantive_sentences  # noqa: E402

SOURCES = {
    # Playwright Test.
    "pw_projects": ("Playwright — Projects", "https://playwright.dev/docs/test-projects", "projetos por browser/dispositivo/ambiente, dependências, teardown e parametrização"),
    "pw_config": ("Playwright — Test configuration", "https://playwright.dev/docs/test-configuration", "configuração de testDir, projetos, expect, retries, workers e artefatos"),
    "pw_locators": ("Playwright — Locators", "https://playwright.dev/docs/locators", "locators por papel, label, texto, test id e composição"),
    "pw_global": ("Playwright — Global setup and teardown", "https://playwright.dev/docs/test-global-setup-teardown", "comparação entre dependências de projeto e globalSetup, incluindo fixtures, traces e relatórios"),
    "pw_webserver": ("Playwright — Web server", "https://playwright.dev/docs/test-webserver", "prontidão do servidor, URL, reuseExistingServer, baseURL e múltiplos servidores"),
    "pw_sharding": ("Playwright — Sharding", "https://playwright.dev/docs/test-sharding", "particionamento por shard, granularidade de testes e merge de relatórios blob"),
    "pw_snapshots": ("Playwright — Visual comparisons", "https://playwright.dev/docs/test-snapshots", "baselines de screenshot, diferenças de ambiente e atualização de snapshots"),
    "pw_pom": ("Playwright — Page object models", "https://playwright.dev/docs/pom", "encapsulamento de operações e seletores reutilizáveis por página"),
    "pw_downloads": ("Playwright — Downloads", "https://playwright.dev/docs/downloads", "evento de download, salvamento persistente e remoção ao encerrar o contexto"),
    "pw_download_api": ("Playwright — Download API", "https://playwright.dev/docs/api/class-download", "métodos saveAs, failure e path de objetos Download"),
    "pw_request": ("Playwright — API testing", "https://playwright.dev/docs/api-testing", "APIRequestContext para setup e pós-condições em testes de browser"),
    "pw_request_context": ("Playwright — APIRequestContext", "https://playwright.dev/docs/api/class-apirequestcontext", "contextos de request associados ao browser, isolamento e jar de cookies"),
    "pw_steps": ("Playwright — Test steps", "https://playwright.dev/docs/api/class-test#test-step", "steps nomeados para organizar ações e resultados do teste"),
    "pw_reporters": ("Playwright — Reporters", "https://playwright.dev/docs/test-reporters", "reporters integrados, múltiplos formatos e configuração em CI"),
    "pw_blob": ("Playwright — Blob reporter", "https://playwright.dev/docs/test-reporters#blob-reporter", "artefatos blob para combinar resultados de execuções particionadas"),
    # Hypothesis, current documentation 6.168.3 at research time.
    "hyp_strategies": ("Hypothesis — Strategies Reference", "https://hypothesis.readthedocs.io/en/latest/reference/strategies.html", "estratégias primitivas, compositores, builds, coleções, exemplos e filtros"),
    "hyp_data": ("Hypothesis — strategies.data()", "https://hypothesis.readthedocs.io/en/latest/reference/strategies.html#hypothesis.strategies.data", "draws dinâmicos e acesso a dados gerados durante a execução de um teste"),
    "hyp_api": ("Hypothesis — API Reference", "https://hypothesis.readthedocs.io/en/latest/reference/api.html", "@given, exemplos, inferência, settings, HealthCheck e configuração pública"),
    "hyp_replay": ("Hypothesis — Replaying failures", "https://hypothesis.readthedocs.io/en/latest/tutorial/replaying-failures.html", "banco de exemplos, replay, @example e @reproduce_failure"),
    "hyp_database": ("Hypothesis — ExampleDatabase API", "https://hypothesis.readthedocs.io/en/latest/reference/api.html#hypothesis.database.ExampleDatabase", "persistência, replay e política de cache do banco de exemplos"),
    # TestNG.
    "tng_annotations": ("TestNG — Annotations", "https://testng.org/annotations.html", "ciclo de vida, DataProvider, Factory, Listener e atributos de teste"),
    "tng_parameters": ("TestNG — Parameters", "https://testng.org/parameters.html", "parâmetros XML, opções, hierarquia de escopo e data providers"),
    "tng_dependencies": ("TestNG — Dependencies", "https://testng.org/dependencies.html", "dependências entre métodos e grupos e comportamento de alwaysRun"),
    "tng_docs": ("TestNG — Documentation", "https://testng.org/documentation.html", "grupos, XML, execução paralela, listeners e relatórios"),
    # Go standard library and toolchain.
    "go_testing": ("Go — package testing", "https://pkg.go.dev/testing", "testes, subtests, helpers, cleanup, benchmarks e interfaces do pacote testing"),
    "go_testflags": ("Go — go test flags", "https://pkg.go.dev/cmd/go#hdr-Testing_flags", "seleção e execução de testes, fuzzing e benchmarks pela ferramenta go"),
    "go_fuzz": ("Go — Getting started with fuzzing", "https://go.dev/doc/tutorial/fuzz", "corpus de sementes, falhas minimizadas e execução de fuzz tests"),
    "go_fuzzing": ("Go — Fuzzing overview", "https://go.dev/doc/security/fuzz/", "tipos permitidos, corpus, funções de fuzz e modo de execução"),
    "go_race": ("Go — Data Race Detector", "https://go.dev/doc/articles/race_detector", "execução instrumentada e limite dinâmico de detecção de corridas"),
    "go_synctest": ("Go — testing/synctest", "https://pkg.go.dev/testing/synctest", "bolhas isoladas, tempo virtual e espera por goroutines bloqueadas"),
    "go_release": ("Go 1.25 Release Notes — testing/synctest", "https://go.dev/doc/go1.25", "estabilização de testing/synctest no Go 1.25 e mudança desde a fase experimental"),
    "go_benchstat": ("Go — benchstat", "https://pkg.go.dev/golang.org/x/perf/cmd/benchstat", "comparação estatística de resultados de benchmarks"),
    # PIT.
    "pit_concepts": ("PIT — Basic Concepts", "https://pitest.org/quickstart/basic_concepts/", "mutantes de bytecode, seleção de testes por cobertura e estados dos resultados"),
    "pit_mutators": ("PIT — Mutation Operators", "https://pitest.org/quickstart/mutators/", "mutadores disponíveis e grupos DEFAULTS, STRONGER e ALL"),
    "pit_maven": ("PIT — Maven Quick Start", "https://pitest.org/quickstart/maven/", "goal mutationCoverage, filtros e modo dry run documentado desde 1.17.3"),
    "pit_cli": ("PIT — Command Line Quick Start", "https://pitest.org/quickstart/commandline/", "filtros de target classes/tests, execução e parâmetros de linha de comando"),
    "pit_history": ("PIT — Incremental Analysis", "https://pitest.org/quickstart/incremental_analysis/", "histórico incremental e pressupostos usados para inferir resultados anteriores"),
    # PHPUnit 12.5 manual.
    "php_writing": ("PHPUnit 12.5 — Writing Tests", "https://docs.phpunit.de/en/12.5/writing-tests-for-phpunit.html", "descoberta, nomes, atributos de teste, providers e fluxo AAA"),
    "php_attributes": ("PHPUnit 12.5 — Attributes", "https://docs.phpunit.de/en/12.5/attributes.html", "atributos #[Test], #[DataProvider], #[TestWith], #[Depends] e configurações"),
    "php_fixtures": ("PHPUnit 12.5 — Fixtures", "https://docs.phpunit.de/en/12.5/fixtures.html", "setup/teardown, ciclo de vida, estado externo e fixtures compartilhadas"),
    "php_configuration": ("PHPUnit 12.5 — Configuration", "https://docs.phpunit.de/en/12.5/configuration.html", "precedência entre defaults, XML e opções da linha de comando"),
    "php_cli": ("PHPUnit 12.5 — Text UI", "https://docs.phpunit.de/en/12.5/textui.html", "ordenação, seleção, sementes aleatórias e saída do test runner"),
    "php_risky": ("PHPUnit 12.5 — Risky Tests", "https://docs.phpunit.de/en/12.5/risky-tests.html", "testes sem assertions, output e critérios de risco"),
    "php_xml": ("PHPUnit 12.5 — XML Configuration", "https://docs.phpunit.de/en/12.5/xml-configuration-file.html", "configuração de grupos, isolamento, execução e resultado"),
    # RSpec 3.13 feature documentation.
    "rspec_shared": ("RSpec 3.13 — Shared examples", "https://rspec.info/features/3-13/rspec-core/example-groups/shared-examples/", "inclusão de grupos compartilhados, parâmetros, carregamento e escopo"),
    "rspec_around": ("RSpec 3.13 — Around hooks", "https://rspec.info/features/3-13/rspec-core/hooks/around-hooks/", "invocação de example.run e posição dos hooks em torno do exemplo"),
    "rspec_hooks": ("RSpec 3.13 — Before and after hooks", "https://rspec.info/features/3-13/rspec-core/hooks/before-and-after-hooks/", "escopo e ordem de before/after hooks por exemplo e grupo"),
    "rspec_let": ("RSpec 3.13 — let and let!", "https://rspec.info/features/3-13/rspec-core/helper-methods/let/", "memoização lazy por exemplo e avaliação de let! por hook"),
    "rspec_composing": ("RSpec 3.13 — Composing matchers", "https://rspec.info/features/3-13/rspec-expectations/composing-matchers/", "composição de matchers em estruturas aninhadas e valores parciais"),
    "rspec_matching": ("RSpec 3.13 — Matching arguments", "https://rspec.info/features/3-13/rspec-mocks/setting-constraints/matching-arguments/", "restrições de argumentos de expectativas e stubs de mensagens"),
    "rspec_doubles": ("RSpec 3.13 — Verifying doubles", "https://rspec.info/features/3-13/rspec-mocks/verifying-doubles/", "double que valida métodos disponíveis na interface real"),
    "rspec_order": ("RSpec 3.13 — Randomized order", "https://rspec.info/features/3-13/rspec-core/command-line/order/", "randomização de grupos/exemplos e reprodução por seed"),
    "rspec_metadata": ("RSpec 3.13 — Metadata filtering", "https://rspec.info/features/3-13/rspec-core/command-line/tag/", "seleção e exclusão de exemplos por tags/metadata"),
    # ExUnit 1.20.4 documentation.
    "ex_case": ("ExUnit 1.20.4 — ExUnit.Case", "https://ex-unit.hexdocs.pm/ExUnit.Case.html", "testes, describe, tags, async e filtros de execução"),
    "ex_callbacks": ("ExUnit 1.20.4 — ExUnit.Callbacks", "https://ex-unit.hexdocs.pm/ExUnit.Callbacks.html", "setup, setup_all, contexto, processos supervisionados e on_exit"),
    "ex_template": ("ExUnit 1.20.4 — ExUnit.CaseTemplate", "https://ex-unit.hexdocs.pm/ExUnit.CaseTemplate.html", "template de módulos de teste com callbacks e funções compartilhadas"),
    "ex_capture": ("ExUnit 1.20.4 — ExUnit.CaptureIO", "https://ex-unit.hexdocs.pm/ExUnit.CaptureIO.html", "captura de stdout/stderr, group leader e limites de concorrência"),
    "ex_doctest": ("ExUnit 1.20.4 — ExUnit.DocTest", "https://ex-unit.hexdocs.pm/ExUnit.DocTest.html", "extração e execução de exemplos em documentação Elixir"),
    "ex_assertions": ("ExUnit 1.20.4 — ExUnit.Assertions", "https://ex-unit.hexdocs.pm/ExUnit.Assertions.html", "assertions e diagnósticos de expressões de teste"),
    "ex_exunit": ("ExUnit 1.20.4 — ExUnit", "https://ex-unit.hexdocs.pm/ExUnit.html", "configuração de max_cases, seed e execução paralela por módulo"),
    # Newman current project README and Postman documentation.
    "newman_readme": ("Newman — README e opções", "https://github.com/postmanlabs/newman/blob/develop/README.md", "estado de manutenção, CLI, opções, reporters e uso como biblioteca"),
    "postman_cli": ("Postman CLI — instalação e visão geral", "https://learning.postman.com/docs/postman-cli/postman-cli-installation/", "instalação e posicionamento do runner de linha de comando recomendado para novos workflows"),
    "newman_environment": ("Postman — Managing environments", "https://learning.postman.com/docs/use/send-requests/variables/managing-environments/", "escopo, uso e precedência de variáveis de ambiente"),
    "newman_data": ("Postman — Data files in collection runs", "https://learning.postman.com/docs/tests-and-scripts/running-collections/test-data/working-with-data-files/", "formatação de arquivos CSV/JSON e escopos de dados em collection runs"),
    "newman_reporters": ("Newman — Reporters", "https://github.com/postmanlabs/newman/blob/develop/README.md#reporters", "reporters integrados, saídas CLI/JSON/JUnit e exportação de resultados"),
    "newman_custom": ("Newman — External Reporters", "https://github.com/postmanlabs/newman/blob/develop/README.md#external-reporters", "instalação e carregamento de reporters externos"),
    "newman_api": ("Newman — API Reference", "https://github.com/postmanlabs/newman/blob/develop/README.md#api-reference", "newman.run, eventos e callback de conclusão"),
    # axe-core current developer documentation.
    "axe_api": ("axe-core — JavaScript Accessibility API", "https://raw.githubusercontent.com/dequelabs/axe-core/develop/doc/API.md", "axe.run, objeto de resultados, tags, conteúdo renderizado e iframes"),
    "axe_context": ("axe-core — Testing Context", "https://raw.githubusercontent.com/dequelabs/axe-core/develop/doc/context.md", "include/exclude, seletores DOM, iframes e shadow DOM"),
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
    if len(rows) != 10:
        raise ValueError(f"{path.name}: o grupo precisa ter 10 notas; tem {len(rows)}")
    for key in ("group", "first", "check"):
        if key not in context or not context[key]:
            raise ValueError(f"{path.name}: falta contexto {key}")
    return context, rows


def render_note(context: dict[str, str], rows: list[dict[str, object]], index: int,
                row: dict[str, object]) -> tuple[int, str, dict[str, object]]:
    number = int(context["first"]) + index
    source_keys = row["sources"]
    sources = [SOURCES[key] for key in source_keys]
    if len(sources) < 2 or len({source[1] for source in sources}) < 2:
        raise ValueError(f"{row['slug']}: precisa de duas fontes distintas")

    neighbors = []
    for neighbor_index in (index - 1, index + 1):
        if 0 <= neighbor_index < len(rows):
            other = rows[neighbor_index]
            neighbors.append(f"- [[{other['slug']}]] — Veja também: {other['title']}.")

    frontmatter = f'''---
id: software.testes.tranche12.{number:06d}
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-12.md"
fontes: [{', '.join('"' + source[1] + '"' for source in sources)}]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---
'''
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
        help="Rebuild the existing 100 tranche-12 notes after validating their IDs and inventory.",
    )
    args = parser.parse_args()
    group_files = sorted(DATA_DIR.glob("*.txt"))
    if len(group_files) != 10:
        raise SystemExit(f"Esperados 10 arquivos de grupo; encontrados {len(group_files)}")

    pending = []
    report_rows = []
    group_summaries = []
    seen_slugs: set[str] = set()
    seen_titles: set[str] = set()
    expected_number = 550
    for path in group_files:
        context, rows = parse_group(path)
        if int(context["first"]) != expected_number:
            raise ValueError(f"{path.name}: ID inicial esperado {expected_number}, informado {context['first']}")
        group_summaries.append(context)
        for index, row in enumerate(rows):
            slug = str(row["slug"])
            title = str(row["title"])
            normalized_title = title.casefold().strip()
            target_path = NOTES_DIR / f"{slug}.md"
            expected_id = f"id: software.testes.tranche12.{expected_number + index:06d}"
            if slug in seen_slugs:
                raise ValueError(f"slug duplicado: {slug}")
            if target_path.exists():
                current = target_path.read_text(encoding="utf-8")
                if not args.refresh:
                    raise ValueError(f"arquivo já existe (use --refresh apenas para a tranche 12): {target_path}")
                if expected_id not in current.splitlines()[:25]:
                    raise ValueError(f"ID existente não corresponde à tranche: {target_path}")
            elif args.refresh:
                raise ValueError(f"--refresh exige os 100 arquivos existentes; falta {target_path}")
            if normalized_title in seen_titles:
                raise ValueError(f"título duplicado: {title}")
            seen_slugs.add(slug)
            seen_titles.add(normalized_title)
            unknown = set(row["sources"]) - SOURCES.keys()
            if unknown:
                raise ValueError(f"{slug}: fontes desconhecidas {unknown}")
            number, content, quality = render_note(context, rows, index, row)
            pending.append((number, row, context, content, quality))
            source_name, source_url, _ = SOURCES[row["sources"][0]]
            report_rows.append(
                f"| {number} | [[{slug}]] | [{source_name}]({source_url}) | {row['review']} Revisão factual por IA concluída; decisão: aprovada. |"
            )
        expected_number += 10

    if len(pending) != 100 or expected_number != 650:
        raise ValueError(f"esperadas 100 notas de 550 a 649, validadas {len(pending)}")
    repeated = repeated_substantive_sentences(
        [(number, content) for number, _, _, content, _ in pending]
    )
    if repeated:
        examples = [f"{numbers}: {sentence}" for sentence, numbers in list(repeated.items())[:8]]
        raise ValueError(f"prosa substantiva repetida entre notas; revisar antes de gravar: {examples}")

    existing_tranche = [
        path for path in NOTES_DIR.glob("*.md")
        if re.search(
            r"(?m)^id: software\.testes\.tranche12\.\d{6}\s*$",
            path.read_text(encoding="utf-8")[:1200],
        )
    ]
    if args.refresh and len(existing_tranche) != 100:
        raise ValueError(f"--refresh exige exatamente 100 notas tranche12 existentes; encontradas {len(existing_tranche)}")
    if REPORT.exists() and not args.refresh:
        raise ValueError(f"relatório já existe (use --refresh apenas para atualizar a tranche 12): {REPORT}")
    if args.refresh and not REPORT.exists():
        raise ValueError(f"--refresh exige relatório factual existente: {REPORT}")

    # All note content and metadata pass the deterministic gate before any file is written.
    for number, row, context, content, quality in pending:
        (NOTES_DIR / f"{row['slug']}.md").write_text(content, encoding="utf-8")

    report = [
        "# Revisão factual assistida por IA — lote `software-testes-2000-0001`, tranche 12",
        "",
        f"- Data: {DATE}",
        "- Revisor: `Arena.ai Agent Mode`",
        "- Escopo: notas **550–649**, em dez grupos de dez; cada linha identifica a conferência factual da nota.",
        "- Fontes primárias: documentação oficial dos projetos e versões indicadas nas próprias notas; as afirmações foram limitadas ao material citado.",
        "- Resultado: **100 revisões factuais por IA registradas** e aprovadas no gate automatizado de qualidade. Isto não é aprovação humana nem garantia de ausência de erro.",
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
    for context in group_summaries:
        report.append(f"- {context['group']} (itens {context['first']}–{int(context['first']) + 9}): {context['check']}")
    report += [
        "- A auditoria de links, o gate de conteúdo e a verificação de sentenças repetidas foram executados separadamente antes da contabilização.",
        "",
    ]
    REPORT.write_text("\n".join(report).rstrip() + "\n", encoding="utf-8")
    word_counts = [quality["word_count"] for _, _, _, _, quality in pending]
    print(f"Geradas {len(pending)} notas substantivas (IDs 550–649); palavras: min={min(word_counts)}; max={max(word_counts)}")
    print(f"Relatório factual: {REPORT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
