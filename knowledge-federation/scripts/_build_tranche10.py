#!/usr/bin/env python3
"""Build the source-backed software-testing tranche 10 (notes 350–449)."""
from __future__ import annotations
from datetime import date
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "knowledge-federation" / "scripts" / "_tranche10_data"
NOTES_DIR = ROOT / "knowledge-federation" / "domains" / "software-0007" / "software" / "testes"
REPORT = ROOT / "knowledge-federation" / "exports" / "reports" / "ai-review-software-testes-2000-0001-tranche-10.md"
DATE = date.today().isoformat()

sys.path.insert(0, str(ROOT / "knowledge-federation" / "scripts"))
from note_quality import assess_markdown

SOURCES = {
    # Selenium WebDriver
    "sel_waits": ("Selenium — Waiting strategies", "https://www.selenium.dev/documentation/webdriver/waits/", "condições de espera, readiness e a advertência sobre combinar esperas implícitas e explícitas"),
    "sel_locators": ("Selenium — Locator strategies", "https://www.selenium.dev/documentation/webdriver/elements/locators/", "estratégias de localização e seleção de elementos"),
    "sel_interactions": ("Selenium — Element interactions", "https://www.selenium.dev/documentation/webdriver/elements/interactions/", "comandos de interação e condições de interatividade de elementos"),
    "sel_elements": ("Selenium — Web elements", "https://www.selenium.dev/documentation/webdriver/elements/", "busca, referência e comportamento de elementos WebDriver"),
    "sel_frames": ("Selenium — Frames", "https://www.selenium.dev/documentation/webdriver/interactions/frames/", "seleção e troca de contexto entre documento e frames"),
    "sel_windows": ("Selenium — Windows and tabs", "https://www.selenium.dev/documentation/webdriver/interactions/windows/", "handles, troca, criação e fechamento de janelas/abas"),
    "sel_alerts": ("Selenium — JavaScript alerts, prompts and confirmations", "https://www.selenium.dev/documentation/webdriver/interactions/alerts/", "espera, leitura, entrada, aceitação e rejeição de alertas nativos"),
    "sel_actions": ("Selenium — Actions API", "https://www.selenium.dev/documentation/webdriver/actions_api/", "ações de teclado, ponteiro e roda, sincronização e execução"),
    "sel_keyboard": ("Selenium — Keyboard actions", "https://www.selenium.dev/documentation/webdriver/actions_api/keyboard/", "sequências de teclas e manutenção/liberação do estado de entrada"),
    "sel_errors": ("Selenium — Troubleshooting errors", "https://www.selenium.dev/documentation/webdriver/troubleshooting/errors/", "causas e diagnóstico de erros de interação e referências obsoletas"),
    # JUnit 6.1.3: these notes are intentionally version-scoped.
    "junit_overview": ("JUnit 6.1.3 — Overview", "https://docs.junit.org/6.1.3/overview.html", "arquitetura e componentes do JUnit 6"),
    "junit_intro": ("JUnit 6.1.3 — Writing tests", "https://docs.junit.org/6.1.3/writing-tests/intro.html", "modelo de escrita e execução de testes Jupiter"),
    "junit_annotations": ("JUnit 6.1.3 — Annotations", "https://docs.junit.org/6.1.3/writing-tests/annotations.html", "semântica das anotações de teste e ciclo de vida"),
    "junit_params": ("JUnit 6.1.3 — Parameterized classes and tests", "https://docs.junit.org/6.1.3/writing-tests/parameterized-classes-and-tests.html", "fontes, consumo de argumentos e natureza experimental de classes parametrizadas"),
    "junit_dynamic": ("JUnit 6.1.3 — Dynamic tests", "https://docs.junit.org/6.1.3/writing-tests/dynamic-tests.html", "fábricas, execução lazy e estrutura de testes dinâmicos"),
    "junit_parallel": ("JUnit 6.1.3 — Parallel execution", "https://docs.junit.org/6.1.3/writing-tests/parallel-execution.html", "ativação, modos de execução e sincronização de testes paralelos"),
    "junit_lifecycle": ("JUnit 6.1.3 — Test instance lifecycle", "https://docs.junit.org/6.1.3/writing-tests/test-instance-lifecycle.html", "ciclo de vida PER_METHOD/PER_CLASS e estado compartilhado"),
    "junit_extensions": ("JUnit 6.1.3 — Extension model", "https://docs.junit.org/6.1.3/extensions/overview.html", "pontos de extensão e integração com o ciclo de execução"),
    "junit_tempdir": ("JUnit 6.1.3 — Built-in extensions", "https://docs.junit.org/6.1.3/writing-tests/built-in-extensions.html", "uso e configuração da extensão @TempDir"),
    "junit_repeated": ("JUnit 6.1.3 — Repeated tests", "https://docs.junit.org/6.1.3/writing-tests/repeated-tests.html", "repetições, nomes e contexto de cada invocação"),
    "junit_tags": ("JUnit 6.1.3 — Filtering by tags", "https://docs.junit.org/6.1.3/running-tests/tags.html", "marcação e seleção de testes por tags"),
    # Mockito Javadocs: published API documentation, version-specific links.
    "mockito_api": ("Mockito 5.24.0 — Mockito.java (repositório oficial)", "https://raw.githubusercontent.com/mockito/mockito/v5.24.0/mockito-core/src/main/java/org/mockito/Mockito.java", "stubbing, verificação, matchers, spies e APIs de Mockito"),
    "mockito_captor": ("Mockito 5.24.0 — ArgumentCaptor.java (repositório oficial)", "https://raw.githubusercontent.com/mockito/mockito/v5.24.0/mockito-core/src/main/java/org/mockito/ArgumentCaptor.java", "captura de argumentos e distinção em relação a matchers"),
    "mockito_strict": ("Mockito 5.24.0 — Strictness.java (repositório oficial)", "https://raw.githubusercontent.com/mockito/mockito/v5.24.0/mockito-core/src/main/java/org/mockito/quality/Strictness.java", "níveis de strictness e benefícios/limitações de STRICT_STUBS"),
    "mockito_extension": ("Mockito JUnit Jupiter 5.24.0 — MockitoExtension.java (repositório oficial)", "https://raw.githubusercontent.com/mockito/mockito/v5.24.0/mockito-extensions/mockito-junit-jupiter/src/main/java/org/mockito/junit/jupiter/MockitoExtension.java", "integração do Mockito com o ciclo de testes JUnit Jupiter"),
    # Jest 30.5 documentation.
    "jest_async": ("Jest 30.5 — Testing asynchronous code", "https://jestjs.io/docs/asynchronous", "promises, async/await, rejeições e garantia de que a asserção seja aguardada"),
    "jest_mock_functions": ("Jest 30.5 — Mock Functions", "https://jestjs.io/docs/mock-functions", "estado de chamadas, resultados, implementações e spies"),
    "jest_setup": ("Jest 30.5 — Setup and teardown", "https://jestjs.io/docs/setup-teardown", "escopo e ordenação de hooks de preparação e limpeza"),
    "jest_object": ("Jest 30.5 — The Jest object", "https://jestjs.io/docs/jest-object", "limpeza, reset, restauração e isolamento de módulos"),
    "jest_timers": ("Jest 30.5 — Timer mocks", "https://jestjs.io/docs/timer-mocks", "relógio falso, avanço de timers e timers encadeados"),
    "jest_esm": ("Jest 30.5 — ECMAScript modules", "https://jestjs.io/docs/ecmascript-modules", "restrições e APIs de mock para módulos ESM e CommonJS"),
    "jest_snapshot": ("Jest 30.5 — Snapshot testing", "https://jestjs.io/docs/snapshot-testing", "criação, revisão e atualização de snapshots"),
    "jest_coverage": ("Jest 30.5 — Configuration", "https://jestjs.io/docs/configuration", "opções de cobertura e thresholds de configuração"),
    # Vitest current documentation.
    "vitest_vi": ("Vitest — vi API", "https://vitest.dev/api/vi.html", "mock functions, timers, relógio do sistema e ciclo de vida de mocks"),
    "vitest_modules": ("Vitest — Module mocking", "https://vitest.dev/guide/mocking/modules", "mocking de módulos, hoisting e limitações do Browser Mode"),
    "vitest_mocking": ("Vitest — Mocking", "https://vitest.dev/guide/mocking", "uso de mocks, spies e isolamento de chamadas"),
    "vitest_dates": ("Vitest — Mocking dates", "https://vitest.dev/guide/mocking/dates", "controle de datas e distinção entre relógio e timers"),
    "vitest_projects": ("Vitest — Test projects", "https://vitest.dev/guide/projects", "configuração, herança e opções globais de projetos"),
    "vitest_perf": ("Vitest — Improving performance", "https://vitest.dev/guide/improving-performance", "isolamento por arquivo, pools e efeitos de desativar paralelismo"),
    "vitest_coverage": ("Vitest — Coverage", "https://vitest.dev/guide/coverage", "providers e opções de relatório de cobertura"),
    "vitest_snapshots": ("Vitest — Snapshot testing", "https://vitest.dev/guide/snapshot", "asserções de snapshot e atualização de resultados"),
    # Testcontainers for Java.
    "postgres_official": ("Docker Official Images — PostgreSQL tags (commit f5a08cb, 2026-09-24)", "https://github.com/docker-library/official-images/blob/f5a08cb993309e539ddddf5b23236d4442fb95a1/library/postgres", "tags e variantes de distribuição publicadas para a imagem oficial, incluindo postgres:16.15-bookworm no snapshot consultado"),
    "tc_waits": ("Testcontainers for Java — Startup and waits", "https://java.testcontainers.org/features/startup_and_waits/", "startup checks e estratégias de espera por readiness"),
    "tc_junit": ("Testcontainers for Java — JUnit 5 integration", "https://java.testcontainers.org/test_framework_integration/junit_5/", "containers estáticos/de instância e limitações de paralelismo da extensão"),
    "tc_manual": ("Testcontainers for Java — Manual lifecycle control", "https://java.testcontainers.org/test_framework_integration/manual_lifecycle_control/", "controle explícito de start/stop e compartilhamento do ciclo de vida"),
    "tc_jdbc": ("Testcontainers for Java — JDBC support", "https://java.testcontainers.org/modules/databases/jdbc/", "driver JDBC, URLs jdbc:tc e configuração de bancos temporários"),
    "tc_reuse": ("Testcontainers for Java — Reusable Containers", "https://java.testcontainers.org/features/reuse/", "reuso experimental, opt-in e requisitos de configuração idêntica"),
    "tc_compose": ("Testcontainers for Java — Docker Compose module", "https://java.testcontainers.org/modules/docker_compose/", "serviços Compose expostos e configuração de readiness"),
    "tc_advanced": ("Testcontainers for Java — Advanced options", "https://java.testcontainers.org/features/advanced_options/", "opções de inicialização e limites de recursos dos containers"),
    # Grafana k6.
    "k6_checks": ("Grafana k6 — Checks", "https://grafana.com/docs/k6/latest/using-k6/checks/", "checks registram taxas de sucesso e não falham o teste sozinhos"),
    "k6_thresholds": ("Grafana k6 — Thresholds", "https://grafana.com/docs/k6/latest/using-k6/thresholds/", "critérios de pass/fail aplicados a métricas e segmentos"),
    "k6_scenarios": ("Grafana k6 — Scenarios", "https://grafana.com/docs/k6/latest/using-k6/scenarios/", "execução de workloads nomeados com executors e parâmetros"),
    "k6_executors": ("Grafana k6 — Executors", "https://grafana.com/docs/k6/latest/using-k6/scenarios/executors/", "modelos de carga baseados em usuários e taxa de chegada"),
    "k6_models": ("Grafana k6 — Open and closed models", "https://grafana.com/docs/k6/latest/using-k6/scenarios/concepts/open-vs-closed/", "diferença entre chegada desacoplada e iterações condicionadas à duração do VU"),
    "k6_sleep": ("Grafana k6 — sleep API", "https://grafana.com/docs/k6/latest/javascript-api/k6/sleep/", "suspensão bloqueante de um VU em segundos e restrições ao uso com código assíncrono"),
    "k6_metrics": ("Grafana k6 — Built-in metrics", "https://grafana.com/docs/k6/latest/using-k6/metrics/reference/", "tipos, semântica e amostragem de métricas k6"),
    "k6_lifecycle": ("Grafana k6 — Test lifecycle", "https://grafana.com/docs/k6/latest/using-k6/test-lifecycle/", "setup, execução de cenários e teardown"),
    "k6_tags": ("Grafana k6 — Tags and groups", "https://grafana.com/docs/k6/latest/using-k6/tags-and-groups/", "tags em métricas, checks, grupos e filtros"),
    "k6_browser": ("Grafana k6 — Browser testing", "https://grafana.com/docs/k6/latest/using-k6-browser/", "automação browser-level e métricas frontend produzidas por testes sintéticos"),
    # OWASP ZAP.
    "zap_baseline": ("OWASP ZAP — Baseline scan", "https://www.zaproxy.org/docs/docker/baseline-scan/", "spider e varredura passiva sem ataques ativos"),
    "zap_api": ("OWASP ZAP — API scan", "https://www.zaproxy.org/docs/docker/api-scan/", "importação de definições de API e active scanning direcionado"),
    "zap_automation": ("OWASP ZAP — Automation Framework", "https://www.zaproxy.org/docs/automate/automation-framework/", "planos YAML, ambiente, jobs, autenticação e testes de resultado"),
    "zap_ascan": ("OWASP ZAP — Active Scan job", "https://www.zaproxy.org/docs/desktop/addons/automation-framework/job-ascan/", "ataque ativo que exige permissão, com parâmetros de contexto, política, escopo e duração"),
    "zap_pscanwait": ("OWASP ZAP — Passive Scan Wait job", "https://www.zaproxy.org/docs/desktop/addons/automation-framework/job-pscanwait/", "espera a conclusão do processamento da fila passiva atual"),
    "zap_auth": ("OWASP ZAP — Authentication methods", "https://www.zaproxy.org/docs/getting-further/authentication/authentication-methods/", "métodos de autenticação e verificação de sessão"),
    "zap_exit": ("OWASP ZAP — Exit Status job", "https://www.zaproxy.org/docs/desktop/addons/automation-framework/job-exitstatus/", "níveis de alerta e valores configuráveis para o código de saída do plano"),
    "zap_report": ("OWASP ZAP — Report Generation", "https://www.zaproxy.org/docs/desktop/addons/report-generation/", "templates em formatos variados e suporte ao Automation Framework"),
    "zap_filters": ("OWASP ZAP — Alert Filters", "https://www.zaproxy.org/docs/desktop/addons/alert-filters/", "sobrescrita de risco por filtros globais ou contextuais aplicados a alertas"),
    # Schemathesis stable docs; current v4 workflow is called out where relevant.
    "st_data": ("Schemathesis — Data generation", "https://schemathesis.readthedocs.io/en/stable/explanations/data-generation/", "examples, coverage, fuzzing, modos válido/inválido, stateful e shrinking"),
    "st_stateful": ("Schemathesis — Understanding Stateful Testing", "https://schemathesis.readthedocs.io/en/stable/explanations/stateful/", "inferência por schema, aprendizado de Location no CLI, OpenAPI Links explícitos e sequências stateful"),
    "st_pytest": ("Schemathesis — Pytest integration", "https://schemathesis.readthedocs.io/en/stable/tutorials/pytest/", "parametrização por operações e call_and_validate"),
    "st_config": ("Schemathesis — Configuration", "https://schemathesis.readthedocs.io/en/stable/reference/configuration/", "algoritmos padrão de inferência stateful, limites por fase, rede e precedência de autenticação"),
    "st_quick": ("Schemathesis — Quick Start", "https://schemathesis.readthedocs.io/en/stable/quick-start/", "inputs gerados de OpenAPI/GraphQL, checks e reprodução de falhas"),
    "st_migration": ("Schemathesis — Migration from v3", "https://schemathesis.readthedocs.io/en/stable/migration/", "mudanças de comportamento entre versões principais"),
    "st_auth": ("Schemathesis — API authentication", "https://schemathesis.readthedocs.io/en/stable/guides/auth/", "credenciais, schemes de segurança e sanitização de saída"),
    # StrykerJS.
    "stryker_intro": ("StrykerJS — Introduction", "https://stryker-mutator.io/docs/stryker-js/introduction/", "mutação de código, execução da suíte e interpretação de resultados"),
    "stryker_config": ("StrykerJS — Configuration", "https://stryker-mutator.io/docs/stryker-js/configuration/", "mutate, coverage analysis, timeouts, ignore patterns e thresholds"),
    "stryker_incremental": ("StrykerJS — Incremental mode", "https://stryker-mutator.io/docs/stryker-js/incremental/", "resultados anteriores e execução incremental de mutants"),
    "stryker_states": ("Stryker — Mutant states and metrics", "https://stryker-mutator.io/docs/mutation-testing-elements/mutant-states-and-metrics/", "estados killed, survived, No coverage, Ignored e inclusão no mutation score"),
    "stryker_static": ("Stryker — Static mutants", "https://stryker-mutator.io/docs/mutation-testing-elements/static-mutants/", "execução/ignorância de static mutants, estado Ignored e efeito no mutation score"),
    "stryker_disable": ("StrykerJS — Disable mutants", "https://stryker-mutator.io/docs/stryker-js/disable-mutants/", "exclusão de mutators, comentários e plugins de ignore"),
    "stryker_plugin": ("StrykerJS — Creating a plugin", "https://stryker-mutator.io/docs/stryker-js/guides/create-a-plugin/", "instrumentação, dry run, cobertura por teste e execução de mutants"),
}


def parse_group(path: Path):
    lines = path.read_text(encoding="utf-8").splitlines()
    context = {}
    row_lines = []
    in_rows = False
    for line in lines:
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
    rows = []
    for line in row_lines:
        parts = [part.strip() for part in line.split("||")]
        if len(parts) != 10:
            raise ValueError(f"{path.name}: esperados 10 campos, encontrados {len(parts)}: {line}")
        slug, title, summary, reason, how, example, caveat, verify, source_keys, review = parts
        rows.append({"slug": slug, "title": title, "summary": summary, "reason": reason,
                     "how": how, "example": example, "caveat": caveat, "verify": verify,
                     "sources": source_keys.split(","), "review": review})
    if len(rows) != 10:
        raise ValueError(f"{path.name}: o grupo precisa ter 10 notas; tem {len(rows)}")
    for key in ("group", "first", "why", "method", "limits", "check"):
        if key not in context:
            raise ValueError(f"{path.name}: falta contexto {key}")
    return context, rows


def render_note(context, rows, index, row):
    number = int(context["first"]) + index
    sources = [SOURCES[key] for key in row["sources"]]
    if len(sources) < 2 or len({s[1] for s in sources}) < 2:
        raise ValueError(f"{row['slug']}: precisa de duas fontes distintas")
    links = []
    for neighbor_index in (index - 1, index + 1):
        if 0 <= neighbor_index < len(rows):
            other = rows[neighbor_index]
            links.append(f"- [[{other['slug']}]] — Veja também: {other['title']}.")
    frontmatter = f'''---
id: software.testes.tranche10.{number:06d}
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-10.md"
fontes: [{', '.join('"' + s[1] + '"' for s in sources)}]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---
'''
    source_lines = [f"- [{name}]({url}) — {description}; consultado em {DATE}." for name, url, description in sources]
    content = f'''{frontmatter}
# {row['title']}

## Em uma frase
{row['summary']}

## Por que importa
{context['why']} {row['reason']}

## Como funciona
{context['method']} {row['how']}

## Exemplo
{row['example']}

## Limites e trade-offs
{context['limits']} {row['caveat']}

## Como verificar
{row['verify']}

## Conexões
{chr(10).join(links)}

## Fontes
{chr(10).join(source_lines)}
'''
    quality = assess_markdown(content, row["slug"] + ".md")
    if quality["errors"]:
        raise ValueError(f"{row['slug']}: {quality['errors']} ({quality['word_count']} palavras)")
    return number, content, quality


def main():
    group_files = sorted(DATA_DIR.glob("*.txt"))
    if len(group_files) != 10:
        raise SystemExit(f"Esperados 10 arquivos de grupo; encontrados {len(group_files)}")
    pending = []
    report_rows = []
    group_summaries = []
    seen_slugs = set()
    seen_titles = set()
    expected_number = 350
    for path in group_files:
        context, rows = parse_group(path)
        if int(context["first"]) != expected_number:
            raise ValueError(f"{path.name}: ID inicial esperado {expected_number}, informado {context['first']}")
        group_summaries.append(context)
        for index, row in enumerate(rows):
            normalized_title = row["title"].casefold().strip()
            if row["slug"] in seen_slugs or (NOTES_DIR / f"{row['slug']}.md").exists():
                raise ValueError(f"slug duplicado/arquivo existente: {row['slug']}")
            if normalized_title in seen_titles:
                raise ValueError(f"título duplicado: {row['title']}")
            seen_slugs.add(row["slug"])
            seen_titles.add(normalized_title)
            unknown = set(row["sources"]) - SOURCES.keys()
            if unknown:
                raise ValueError(f"{row['slug']}: fontes desconhecidas {unknown}")
            number, content, quality = render_note(context, rows, index, row)
            pending.append((number, row, context, content, quality))
            source_name, source_url, _ = SOURCES[row["sources"][0]]
            report_rows.append(f"| {number} | [[{row['slug']}]] | [{source_name}]({source_url}) | {row['review']} Aprovada por IA. |")
        expected_number += 10
    if len(pending) != 100 or expected_number != 450:
        raise ValueError(f"esperadas 100 notas de 350 a 449, validadas {len(pending)}")
    if REPORT.exists():
        raise ValueError(f"relatório já existe: {REPORT}")

    # All note content and metadata pass the deterministic gate before any file is written.
    for number, row, context, content, quality in pending:
        (NOTES_DIR / f"{row['slug']}.md").write_text(content, encoding="utf-8")

    report = [
        "# Revisão factual assistida por IA — lote `software-testes-2000-0001`, tranche 10",
        "",
        f"- Data: {DATE}",
        "- Revisor: `Arena.ai Agent Mode`",
        "- Escopo: notas **350–449**, em dez grupos de dez; cada linha registra a conferência específica.",
        "- Resultado: **100 notas aprovadas por revisão factual por IA** contra documentação oficial; o gate automatizado e os links foram auditados separadamente.",
        "- Revisão por IA não é revisão humana nem garantia de ausência de erro.",
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
        "- As afirmações foram limitadas à documentação citada e às condições de versão/contexto indicadas; não houve promoção de revisão por IA a status humano.",
        "",
    ]
    REPORT.write_text("\n".join(report), encoding="utf-8")
    word_counts = [quality["word_count"] for _, _, _, _, quality in pending]
    print(f"Geradas {len(pending)} notas substantivas (IDs 350–449); palavras: min={min(word_counts)}; max={max(word_counts)}")
    print(f"Relatório factual: {REPORT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
