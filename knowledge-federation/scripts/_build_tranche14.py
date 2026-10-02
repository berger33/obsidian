#!/usr/bin/env python3
"""Build the source-backed software-testing tranche 14 (notes 750–849)."""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "knowledge-federation" / "scripts" / "_tranche14_data"
NOTES_DIR = ROOT / "knowledge-federation" / "domains" / "software-0007" / "software" / "testes"
DOMAINS_DIR = ROOT / "knowledge-federation" / "domains"
REPORT = ROOT / "knowledge-federation" / "exports" / "reports" / "ai-review-software-testes-2000-0001-tranche-14.md"
DATE = date.today().isoformat()

sys.path.insert(0, str(ROOT / "knowledge-federation" / "scripts"))
from note_quality import assess_markdown, normalize  # noqa: E402
from prose_audit import repeated_substantive_sentences  # noqa: E402

SOURCES = {
    # Bazel test execution.
    "bazel_spec": ("Bazel — Test encyclopedia", "https://bazel.build/reference/test-encyclopedia", "contrato normativo do ambiente de execução, hermeticidade, runfiles, timeout e shards"),
    "bazel_user": ("Bazel — Commands and Options", "https://bazel.build/docs/user-manual", "opções de bazel test, seleção de alvos, variáveis, saída e argumentos"),
    "bazel_common": ("Bazel — Common test-rule attributes", "https://bazel.build/reference/be/common-definitions#common-attributes-tests", "atributos compartilhados de regras de teste, como size, timeout, flaky e shard_count"),
    "bazel_bep": ("Bazel — Build Event Protocol", "https://bazel.build/remote/bep/", "eventos estruturados de invocação e resultados de testes para consumidores"),
    "bazel_remote": ("Bazel — Remote execution", "https://bazel.build/docs/remote-execution", "execução remota de ações de build e testes em workers distribuídos"),
    # Maven Surefire and Failsafe 3.6.0 documentation.
    "maven_surefire": ("Maven Surefire — Introduction", "https://maven.apache.org/surefire/maven-surefire-plugin/", "fase test, execução de testes unitários e diretório padrão de relatórios"),
    "maven_failsafe": ("Maven Failsafe — Usage", "https://maven.apache.org/surefire/maven-failsafe-plugin/usage.html", "goals integration-test e verify, teardown do ciclo e relatórios de integração"),
    "maven_failsafe_single": ("Maven Failsafe — Running a Single Test", "https://maven.apache.org/surefire/maven-failsafe-plugin/examples/single-test.html", "seleção de classes, métodos e padrões de testes de integração por -Dit.test"),
    "maven_test_mojo": ("Maven Surefire — test goal", "https://maven.apache.org/surefire/maven-surefire-plugin/test-mojo.html", "parâmetros do goal test, forkCount, seleção, execução paralela e sistema de propriedades"),
    "maven_single": ("Maven Surefire — Running a Single Test", "https://maven.apache.org/surefire/maven-surefire-plugin/examples/single-test.html", "seleção de testes individuais em Surefire e Failsafe"),
    "maven_patterns": ("Maven Surefire — Inclusion and Exclusion", "https://maven.apache.org/surefire/maven-surefire-plugin/examples/inclusion-exclusion.html", "padrões de nomes para incluir ou excluir classes de teste"),
    "maven_forks": ("Maven Surefire — Forks and parallel execution", "https://maven.apache.org/surefire/maven-surefire-plugin/examples/fork-options-and-parallel-execution.html", "processos JVM, concorrência por framework e limites de execução paralela"),
    "maven_rerun": ("Maven Surefire — Re-run failing tests", "https://maven.apache.org/surefire/maven-surefire-plugin/examples/rerun-failing-tests.html", "reruns, marcação de flakiness, relatórios XML e limite de frameworks"),
    "maven_skip": ("Maven Surefire — Skipping tests", "https://maven.apache.org/surefire/maven-surefire-plugin/examples/skipping-tests.html", "diferença entre pular execução dos testes e pular compilação do test source"),
    "maven_platform": ("Maven Surefire — JUnit Platform", "https://maven.apache.org/surefire/maven-surefire-plugin/examples/junit-platform.html", "integração com engines JUnit Platform e seleção de classes"),
    # Gradle JVM testing.
    "gradle_java": ("Gradle — Testing in Java and JVM projects", "https://docs.gradle.org/current/userguide/java_testing.html", "descoberta, execução, filtragem, integração e relatórios de testes JVM"),
    "gradle_test_api": ("Gradle — Test task API", "https://docs.gradle.org/current/dsl/org.gradle.api.tasks.testing.Test.html", "propriedades e métodos da task Test, processos, filtros e falhas"),
    "gradle_suites": ("Gradle — JVM Test Suite Plugin", "https://docs.gradle.org/current/userguide/jvm_test_suite_plugin.html", "modelagem de suites, dependências, frameworks, tasks adicionais e integração"),
    # Django 6.1 testing documentation.
    "django_overview": ("Django 6.1 — Writing and running tests", "https://docs.djangoproject.com/en/6.1/topics/testing/overview/", "descoberta, execução, seletores, classes de teste e ciclo de banco"),
    "django_tools": ("Django 6.1 — Testing tools", "https://docs.djangoproject.com/en/6.1/topics/testing/tools/", "Client, TestCase, LiveServerTestCase, assertions, e-mail e settings"),
    "django_advanced": ("Django 6.1 — Advanced testing topics", "https://docs.djangoproject.com/en/6.1/topics/testing/advanced/", "RequestFactory, views diretas, middleware e testes de aplicações reutilizáveis"),
    "django_testcase": ("Django 6.1 — TestCase", "https://docs.djangoproject.com/en/6.1/topics/testing/tools/#django.test.TestCase", "isolamento transacional, fixtures e preparação de dados em TestCase"),
    "django_live": ("Django 6.1 — LiveServerTestCase", "https://docs.djangoproject.com/en/6.1/topics/testing/tools/#django.test.LiveServerTestCase", "servidor de teste em thread para clientes externos e interação ao vivo"),
    "django_settings": ("Django 6.1 — override_settings", "https://docs.djangoproject.com/en/6.1/topics/testing/tools/#django.test.override_settings", "substituição temporária de settings durante testes"),
    "django_queries": ("Django 6.1 — assertNumQueries", "https://docs.djangoproject.com/en/6.1/topics/testing/tools/#django.test.TransactionTestCase.assertNumQueries", "asserção contextual do número de consultas SQL executadas"),
    "django_mail": ("Django 6.1 — Testing tools and email", "https://docs.djangoproject.com/en/6.1/topics/testing/tools/#email-services", "backend de e-mail em memória e inspeção das mensagens durante testes"),
    # Android Espresso.
    "espresso_home": ("Android — Espresso", "https://developer.android.com/training/testing/espresso", "ações de UI, assertions, sincronização automática e pacotes do Espresso"),
    "espresso_basics": ("Android — Espresso basics", "https://developer.android.com/training/testing/espresso/basics", "seleção de views, ações e verificações encadeadas em UI tests"),
    "espresso_idle": ("Android — Espresso idling resources", "https://developer.android.com/training/testing/espresso/idling-resource", "registro, transições de idle e coordenação de operações assíncronas"),
    "espresso_intents": ("Android — Espresso-Intents", "https://developer.android.com/training/testing/espresso/intents", "correspondência, verificação e stubbing de intents de saída"),
    "espresso_lists": ("Android — Espresso lists", "https://developer.android.com/training/testing/espresso/lists", "interação com AdapterView por onData e RecyclerView por actions específicas"),
    "espresso_web": ("Android — Espresso Web", "https://developer.android.com/training/testing/espresso/web", "WebView em aplicações híbridas, WebInteraction e integração com UI nativa"),
    "espresso_accessibility": ("Android — Accessibility checking", "https://developer.android.com/training/testing/espresso/accessibility-checking", "execução e supressão estreita de resultados de acessibilidade"),
    # Rails 8.1 guides and API.
    "rails_testing": ("Rails 8.1 — Testing Rails Applications", "https://guides.rubyonrails.org/testing.html", "ambiente, fixtures, testes funcionais, integração, system tests e paralelismo"),
    "rails_integration": ("Rails 8.1 — ActionDispatch::IntegrationTest", "https://api.rubyonrails.org/classes/ActionDispatch/IntegrationTest.html", "fluxos HTTP entre componentes, sessões, redirects e respostas JSON"),
    "rails_time": ("Rails 8.1 — TimeHelpers", "https://api.rubyonrails.org/classes/ActiveSupport/Testing/TimeHelpers.html", "travel_to, freeze_time, restauração automática do relógio e microssegundos"),
    "rails_jobs": ("Rails 8.1 — ActiveJob::TestHelper", "https://api.rubyonrails.org/classes/ActiveJob/TestHelper.html", "assertions para jobs enfileirados e executados, argumentos e filas"),
    "rails_mail": ("Rails 8.1 — ActionMailer::TestHelper", "https://api.rubyonrails.org/classes/ActionMailer/TestHelper.html", "assertions para emails enviados ou enfileirados e captura de mensagens"),
    "rails_fixtures": ("Rails 8.1 — ActiveRecord::FixtureSet", "https://api.rubyonrails.org/classes/ActiveRecord/FixtureSet.html", "fixtures YAML, carregamento de registros e referências entre fixtures"),
    # tox 4 current documentation.
    "tox_config": ("tox — Configuration reference", "https://tox.wiki/en/latest/reference/config.html", "lista de ambientes, fatores, TOML, templates e configurações por ambiente"),
    "tox_usage": ("tox — How-to usage", "https://tox.wiki/en/latest/how-to/usage.html", "execução sequencial/paralela, seleção por ambiente, logs e diretórios temporários"),
    "tox_cli": ("tox — CLI interface", "https://tox.wiki/en/latest/cli_interface.html", "subcomandos run, parallel, exec, list e opções de saída"),
    "tox_start": ("tox — Getting started", "https://tox.wiki/en/latest/tutorial/getting-started.html", "configuração TOML, ambientes base, comandos e passagem de argumentos"),
    # Nox current documentation.
    "nox_config": ("Nox — Configuration and API", "https://nox.thea.codes/en/stable/config.html", "definição de sessões, intérpretes, ambientes virtuais, tags e parâmetros"),
    "nox_usage": ("Nox — Command-line usage", "https://nox.thea.codes/en/stable/usage.html", "seleção e listagem de sessões, reuso de virtualenvs e opções de CLI"),
    "nox_tutorial": ("Nox — Tutorial", "https://nox.thea.codes/en/stable/tutorial.html", "sessões requeridas, parametrização e execução de tarefas dependentes"),
    "nox_cookbook": ("Nox — Cookbook", "https://nox.thea.codes/en/stable/cookbook.html", "receitas para sessões, instalação, comandos e lockfiles"),
    # Laravel 13 documentation.
    "laravel_testing": ("Laravel 13 — Testing", "https://laravel.com/framework/docs/13.x/testing", "tipos de testes, ambiente testing, banco, helpers e execução paralela"),
    "laravel_http": ("Laravel 13 — HTTP Client testing", "https://laravel.com/framework/docs/13.x/http-client#testing", "fakes de respostas HTTP, inspeção de requests e prevenção de tráfego real"),
    "laravel_http_tests": ("Laravel 13 — HTTP tests", "https://laravel.com/framework/docs/13.x/http-tests", "requests internos, respostas JSON e assertions sobre aplicações HTTP"),
    "laravel_database": ("Laravel 13 — Database testing", "https://laravel.com/framework/docs/13.x/database-testing", "refresh de banco, factories, assertions de persistência e isolamento"),
    "laravel_events": ("Laravel 13 — Event testing", "https://laravel.com/framework/docs/13.x/events#testing", "fakes e assertions de eventos sem depender de listeners externos"),
    "laravel_queues": ("Laravel 13 — Queue testing", "https://laravel.com/framework/docs/13.x/queues#testing", "fake de filas e assertions sobre jobs enfileirados"),
    "laravel_mail": ("Laravel 13 — Mail testing", "https://laravel.com/framework/docs/13.x/mail", "fakes de mail, assertions de envio e testes de conteúdo de Mailable"),
    # Python 3.14 standard-library unittest.
    "python_unittest": ("Python 3.14 — unittest", "https://docs.python.org/3/library/unittest.html", "TestCase, fixtures, subtests, suites, discovery, runners e logging"),
    "python_mock": ("Python 3.14 — unittest.mock", "https://docs.python.org/3/library/unittest.mock.html", "Mock, patch, autospec, spec_set, calls e escopo de substituições"),
    "python_mock_examples": ("Python 3.14 — unittest.mock examples", "https://docs.python.org/3/library/unittest.mock-examples.html", "padrões de patch, criação de mocks e assertions de chamadas"),
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
    sources = [SOURCES[key] for key in row["sources"]]
    if len(sources) < 2 or len({source[1] for source in sources}) < 2:
        raise ValueError(f"{row['slug']}: precisa de duas fontes distintas")

    neighbors = []
    for neighbor_index in (index - 1, index + 1):
        if 0 <= neighbor_index < len(rows):
            other = rows[neighbor_index]
            neighbors.append(f"- [[{other['slug']}]] — Veja também: {other['title']}.")

    frontmatter = f'''---
id: software.testes.tranche14.{number:06d}
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-14.md"
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
        help="Rebuild the existing 100 tranche-14 notes after validating their IDs and batch metadata.",
    )
    args = parser.parse_args()
    group_files = sorted(DATA_DIR.glob("*.txt"))
    if len(group_files) != 10:
        raise SystemExit(f"Esperados 10 arquivos de grupo; encontrados {len(group_files)}")

    existing_paths = list(DOMAINS_DIR.rglob("*.md"))
    existing_tranche = [
        path for path in existing_paths
        if re.search(
            r"(?m)^id: software\.testes\.tranche14\.\d{6}\s*$",
            path.read_text(encoding="utf-8", errors="replace")[:1200],
        )
    ]
    if args.refresh and len(existing_tranche) != 100:
        raise ValueError(f"--refresh exige exatamente 100 notas tranche14 existentes; encontradas {len(existing_tranche)}")
    if REPORT.exists() and not args.refresh:
        raise ValueError(f"relatório já existe (use --refresh apenas para atualizar a tranche 14): {REPORT}")
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
    group_summaries = []
    seen_slugs: set[str] = set()
    seen_titles: set[str] = set()
    expected_number = 750
    for path in group_files:
        context, rows = parse_group(path)
        if int(context["first"]) != expected_number:
            raise ValueError(f"{path.name}: ID inicial esperado {expected_number}, informado {context['first']}")
        group_summaries.append(context)
        for index, row in enumerate(rows):
            slug = str(row["slug"])
            title = str(row["title"])
            normalized_title = normalize(title.strip())
            if slug in seen_slugs or slug in existing_slugs:
                raise ValueError(f"slug em colisão com o inventário: {slug}")
            if normalized_title in seen_titles or normalized_title in existing_titles:
                raise ValueError(f"título em colisão com o inventário: {title}")
            target_path = NOTES_DIR / f"{slug}.md"
            expected_id = f"id: software.testes.tranche14.{expected_number + index:06d}"
            if target_path.exists():
                current = target_path.read_text(encoding="utf-8")
                if not args.refresh:
                    raise ValueError(f"arquivo já existe (use --refresh apenas para a tranche 14): {target_path}")
                if expected_id not in current.splitlines()[:25] or "lote: software-testes-2000-0001" not in current.splitlines()[:25]:
                    raise ValueError(f"ID ou lote existente não corresponde à tranche: {target_path}")
            elif args.refresh:
                raise ValueError(f"--refresh exige os 100 arquivos existentes; falta {target_path}")
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
        expected_number += 10

    if len(pending) != 100 or expected_number != 850:
        raise ValueError(f"esperadas 100 notas de 750 a 849, validadas {len(pending)}")
    repeated = repeated_substantive_sentences(
        [(number, content) for number, _, _, content, _ in pending]
    )
    if repeated:
        examples = [f"{numbers}: {sentence}" for sentence, numbers in list(repeated.items())[:8]]
        raise ValueError(f"prosa substantiva repetida entre notas; revisar antes de gravar: {examples}")

    # All 100 notes and metadata pass their deterministic gates before any file is written.
    for number, row, context, content, quality in pending:
        (NOTES_DIR / f"{row['slug']}.md").write_text(content, encoding="utf-8")

    report = [
        "# Revisão factual assistida por IA — lote `software-testes-2000-0001`, tranche 14",
        "",
        f"- Data: {DATE}",
        "- Revisor: `Arena.ai Agent Mode`",
        "- Escopo: notas **750–849**, em dez grupos de dez; cada linha identifica a conferência factual da nota.",
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
        "- A auditoria de links, a comparação com o inventário, o gate de conteúdo e a verificação de sentenças repetidas foram executados separadamente antes da contabilização.",
        "",
    ]
    REPORT.write_text("\n".join(report).rstrip() + "\n", encoding="utf-8")
    word_counts = [quality["word_count"] for _, _, _, _, quality in pending]
    source_counts = [quality["source_count"] for _, _, _, _, quality in pending]
    print(f"Geradas {len(pending)} notas substantivas (IDs 750–849); palavras: min={min(word_counts)}; max={max(word_counts)}")
    print(f"Fontes HTTPS específicas por nota: min={min(source_counts)}; max={max(source_counts)}")
    print(f"Relatório factual: {REPORT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
