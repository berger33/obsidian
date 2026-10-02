#!/usr/bin/env python3
"""Build the source-backed software-testing tranche 11 (notes 450–549)."""
from __future__ import annotations
from datetime import date
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "knowledge-federation" / "scripts" / "_tranche11_data"
NOTES_DIR = ROOT / "knowledge-federation" / "domains" / "software-0007" / "software" / "testes"
REPORT = ROOT / "knowledge-federation" / "exports" / "reports" / "ai-review-software-testes-2000-0001-tranche-11.md"
DATE = date.today().isoformat()

sys.path.insert(0, str(ROOT / "knowledge-federation" / "scripts"))
from note_quality import assess_markdown

SOURCES = {
    # REST Assured: project-maintained wiki plus current API reference.
    "ra_usage": ("REST Assured — Usage (documentação do projeto)", "https://github.com/rest-assured/rest-assured/wiki/Usage", "DSL given/when/then, parâmetros HTTP, validação de resposta, autenticação, filtros e exemplos do projeto"),
    "ra_request": ("REST Assured — RequestSpecification API", "https://javadoc.io/doc/io.rest-assured/rest-assured/latest/io/restassured/specification/RequestSpecification.html", "configuração e composição de requests, parâmetros, corpos, headers, filtros e especificações reutilizáveis"),
    "ra_response": ("REST Assured — ValidatableResponse API", "https://javadoc.io/doc/io.rest-assured/rest-assured/latest/io/restassured/response/ValidatableResponse.html", "assertions encadeadas e validação de status, headers e corpo da resposta"),
    "ra_core": ("REST Assured — RestAssured API", "https://javadoc.io/doc/io.rest-assured/rest-assured/latest/io/restassured/RestAssured.html", "configuração de URI, especificações, parsers, filtros e valores estáticos padrão"),
    "ra_schema": ("REST Assured — JSON Schema Validation", "https://github.com/rest-assured/rest-assured/wiki/Usage#json-schema-validation", "matcher opcional para verificar resposta JSON contra schema"),
    "ra_filters": ("REST Assured — Filters", "https://github.com/rest-assured/rest-assured/wiki/Usage#filters", "interceptação e alteração de request/response, logging e composição de filtros"),
    "ra_auth": ("REST Assured — Authentication", "https://github.com/rest-assured/rest-assured/wiki/Usage#authentication", "esquemas de autenticação e configuração por requisição"),
    "ra_mapping": ("REST Assured — Object Mapping", "https://github.com/rest-assured/rest-assured/wiki/Usage#object-mapping", "serialização e desserialização com mapeadores disponíveis no classpath"),
    # WireMock.
    "wm_stubbing": ("WireMock — Stubbing", "https://wiremock.org/docs/stubbing/", "mapeamentos de request/response, prioridade, defaults, reset e persistência de stubs"),
    "wm_matching": ("WireMock — Request Matching", "https://wiremock.org/docs/request-matching/", "matching de URL, método, query, headers, cookies, body, JSON e formulários"),
    "wm_stateful": ("WireMock — Stateful Behaviour", "https://wiremock.org/docs/stateful-behaviour/", "cenários como máquinas de estado, estados iniciais e reset"),
    "wm_verify": ("WireMock — Verifying", "https://wiremock.org/docs/verifying/", "request journal, verificações, requests não correspondidos e near misses"),
    "wm_junit": ("WireMock — JUnit Jupiter", "https://wiremock.org/docs/junit-jupiter/", "ciclo de vida da extensão, portas dinâmicas e reset entre testes"),
    "wm_faults": ("WireMock — Simulating Faults", "https://wiremock.org/docs/simulating-faults/", "falhas de transporte e condições para testar resiliência"),
    "wm_templating": ("WireMock — Response Templating", "https://wiremock.org/docs/response-templating/", "templates de resposta baseados em dados da request"),
    "wm_proxy": ("WireMock — Proxying", "https://wiremock.org/docs/proxying/", "proxy incondicional/condicional e registro de requests"),
    # Robot Framework 7.5.
    "rf_guide": ("Robot Framework 7.5 — User Guide", "https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html", "formato de testes, setups, teardowns, tags, templates, variáveis, libraries e arquivos de saída"),
    "rf_builtin": ("Robot Framework 7.5 — BuiltIn library", "https://robotframework.org/robotframework/latest/libraries/BuiltIn.html", "keywords incorporadas de fluxo, logging, execução, variáveis e assertions"),
    "rf_collections": ("Robot Framework 7.5 — Collections library", "https://robotframework.org/robotframework/latest/libraries/Collections.html", "keywords para listas e dicionários e verificações de conteúdo"),
    "rf_tags": ("Robot Framework 7.5 — Tagging test cases", "https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#tagging-test-cases", "tags como metadados de casos e seleção por execução"),
    "rf_setup": ("Robot Framework 7.5 — Test setup and teardown", "https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#test-setup-and-teardown", "ordem e escopo do setup e teardown de testes"),
    "rf_templates": ("Robot Framework 7.5 — Test templates", "https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#test-templates", "execução orientada a dados por template e linhas de argumentos"),
    # Cucumber / Gherkin.
    "cu_gherkin": ("Cucumber — Gherkin Reference", "https://cucumber.io/docs/gherkin/reference/", "estrutura Feature, Rule, Scenario, Background, Outline, tags, steps e argumentos multilinha"),
    "cu_steps": ("Cucumber — Step Definitions", "https://cucumber.io/docs/cucumber/step-definitions/", "expressões, correspondência de steps e parâmetros tipados"),
    "cu_api": ("Cucumber — API Reference", "https://cucumber.io/docs/cucumber/api/", "hooks, tags, tabelas, resultados e regras de execução dos steps"),
    "cu_expr": ("Cucumber — Cucumber Expressions", "https://cucumber.io/docs/cucumber/cucumber-expressions/", "parâmetros nomeados, tipos integrados e expressões de step"),
    # NUnit current documentation.
    "nunit_test": ("NUnit — Test attribute", "https://docs.nunit.org/articles/nunit/writing-tests/attributes/test.html", "assinaturas de teste, métodos async e resultados esperados"),
    "nunit_case": ("NUnit — TestCase attribute", "https://docs.nunit.org/articles/nunit/writing-tests/attributes/testcase.html", "argumentos inline e criação de casos parametrizados"),
    "nunit_source": ("NUnit — TestCaseSource attribute", "https://docs.nunit.org/articles/nunit/writing-tests/attributes/testcasesource.html", "fontes estáticas de casos, sequências e versões com dados assíncronos"),
    "nunit_setup": ("NUnit — SetUp attribute", "https://docs.nunit.org/articles/nunit/writing-tests/attributes/setup.html", "preparação de fixture por caso de teste"),
    "nunit_teardown": ("NUnit — TearDown attribute", "https://docs.nunit.org/articles/nunit/writing-tests/attributes/teardown.html", "limpeza após o caso, inclusive tratamento após falha de setup/teste"),
    "nunit_once": ("NUnit — OneTimeSetUp attribute", "https://docs.nunit.org/articles/nunit/writing-tests/attributes/onetimesetup.html", "setup único da fixture, herança e escopo de SetUpFixture"),
    "nunit_fixture": ("NUnit — FixtureLifeCycle attribute", "https://docs.nunit.org/articles/nunit/writing-tests/attributes/fixturelifecycle.html", "instância compartilhada ou por test case e requisitos do lifecycle"),
    "nunit_parallel": ("NUnit — Parallelizable attribute", "https://docs.nunit.org/articles/nunit/writing-tests/attributes/parallelizable.html", "marcação de testes paralelizáveis e separação da configuração máxima de workers"),
    "nunit_order": ("NUnit — Order attribute", "https://docs.nunit.org/articles/nunit/writing-tests/attributes/order.html", "ordem local de início e ausência de garantia de conclusão sequencial"),
    "nunit_context": ("NUnit — TestContext", "https://docs.nunit.org/articles/nunit/writing-tests/TestContext.html", "contexto por caso ou fixture e informações/resultados de execução"),
    "nunit_assert": ("NUnit — Assertions", "https://docs.nunit.org/articles/nunit/writing-tests/assertions/assertions.html", "constraints, assertions agrupadas e comparação de resultados"),
    # xUnit.net v3.
    "xu_start": ("xUnit.net v3 — Getting Started", "https://xunit.net/docs/getting-started/v3/getting-started", "Fact, Theory, dados inline, descoberta e execução de casos"),
    "xu_shared": ("xUnit.net — Sharing Context between Tests", "https://xunit.net/docs/shared-context", "construtores, fixtures de classe/coleção, escopo e descarte"),
    "xu_parallel": ("xUnit.net — Running Tests in Parallel", "https://xunit.net/docs/running-tests-in-parallel", "coleções, modos de paralelismo, limites e escopo de runner"),
    "xu_output": ("xUnit.net — Capturing Output", "https://xunit.net/docs/capturing-output", "ITestOutputHelper, console e captura associada a testes"),
    "xu_assert": ("xUnit.net v3 — Assert API (v3.0.0)", "https://api.xunit.net/v3/3.0.0/Xunit.Assert.html", "referência da classe Assert, incluindo Throws, ThrowsAsync e outras assertions síncronas/assíncronas"),
    "xu_config": ("xUnit.net — Configuration Files", "https://xunit.net/docs/config-xunit-runner-json", "opções de runner, execução paralela e configuração por assembly"),
    "xu_lifetime": ("xUnit.net — Getting Started with xUnit.net v3", "https://xunit.net/docs/getting-started/v3/getting-started", "execução em v3 e configuração de métodos/casos assíncronos"),
    # Locust current stable documentation.
    "locust_file": ("Locust 2.46 — Writing a locustfile", "https://docs.locust.io/en/stable/writing-a-locustfile.html", "User/HttpUser, tarefas, pesos, wait_time, lifecycle, cliente e agrupamento de estatísticas"),
    "locust_api": ("Locust — API Reference", "https://docs.locust.io/en/stable/api.html", "classes User, HttpUser, TaskSet e helpers de pacing"),
    "locust_distributed": ("Locust — Distributed load generation", "https://docs.locust.io/en/stable/running-distributed.html", "processos master/worker, distribuição de carga, mensagens e limitações"),
    "locust_shape": ("Locust 2.46 — LoadTestShape API/source", "https://docs.locust.io/en/stable/_modules/locust/shape.html", "contrato de tick, contagem total de usuários, spawn rate e encerramento com None"),
    "locust_performance": ("Locust 2.46 — Increasing the request rate", "https://docs.locust.io/en/stable/increasing-request-rate.html", "diagnóstico de throughput, concorrência, saturação do gerador e uso de FastHttpUser para reduzir CPU"),
    "locust_tasks": ("Locust — TaskSet", "https://docs.locust.io/en/stable/tasksets.html", "tarefas aninhadas, pesos e sequências de comportamento"),
    "locust_events": ("Locust — Event hooks", "https://docs.locust.io/en/stable/extending-locust.html", "hooks de ciclo de vida e extensão de comportamento/estatísticas"),
    "locust_client": ("Locust — Using the HTTP client", "https://docs.locust.io/en/stable/writing-a-locustfile.html#http-client", "response context, validação manual e cliente HTTP sem browser"),
    # Apache JMeter User's Manual.
    "jm_plan": ("Apache JMeter — Elements of a Test Plan", "https://jmeter.apache.org/usermanual/test_plan.html", "Thread Groups, timers, assertions, execução e regras de escopo"),
    "jm_components": ("Apache JMeter — Component Reference", "https://jmeter.apache.org/usermanual/component_reference.html", "CSV Data Set, assertions, timers, extractors e controllers"),
    "jm_start": ("Apache JMeter — Getting Started", "https://jmeter.apache.org/usermanual/get-started.html", "modo CLI para load tests e opções de execução"),
    "jm_build": ("Apache JMeter — Building a Test Plan", "https://jmeter.apache.org/usermanual/build-test-plan.html", "edição/debug em GUI, execução em CLI e elementos do plano"),
    "jm_best": ("Apache JMeter — Best Practices", "https://jmeter.apache.org/usermanual/best-practices.html", "uso de CSV, redução de recursos e execução eficiente de carga"),
    "jm_hints": ("Apache JMeter — Hints and Tips", "https://jmeter.apache.org/usermanual/hints_and_tips.html", "escopo de variáveis por thread e uso de propriedades compartilhadas"),
    "jm_remote": ("Apache JMeter — Distributed Testing", "https://jmeter.apache.org/usermanual/jmeter_distributed_testing_step_by_step.html", "controller e engines remotos em execução distribuída"),
    # Gatling current documentation.
    "gat_scenario": ("Gatling — Scenario", "https://docs.gatling.io/concepts/scenario/", "sequência de ações, exec, controles de fluxo e pausas"),
    "gat_session": ("Gatling — Session API", "https://docs.gatling.io/concepts/session/api/", "estado de cada virtual user e propagação de atributos"),
    "gat_feeders": ("Gatling — Feeders", "https://docs.gatling.io/concepts/session/feeders/", "consumo de registros e injeção de dados na sessão do usuário"),
    "gat_checks": ("Gatling — Checks", "https://docs.gatling.io/concepts/checks/", "validação de resposta e extração saveAs condicionada ao sucesso"),
    "gat_assertions": ("Gatling — Assertions", "https://docs.gatling.io/concepts/assertions/", "critérios sobre estatísticas da simulação e escopos"),
    "gat_injection": ("Gatling — Injection", "https://docs.gatling.io/concepts/injection/", "modelos open/closed e perfis de usuários"),
    "gat_protocol": ("Gatling — HTTP Protocol", "https://docs.gatling.io/reference/script/http/protocol/", "configuração de protocolo reutilizável por cenário"),
    "gat_timing": ("Gatling — Timings", "https://docs.gatling.io/concepts/timings/", "pausas e temporização explícita dos fluxos simulados"),
    # Appium current documentation.
    "app_caps": ("Appium — Session Capabilities", "https://appium.io/docs/en/latest/guides/caps/", "parâmetros W3C de criação de sessão, prefixos Appium e capabilities imutáveis"),
    "app_context": ("Appium — Managing Contexts", "https://appium.io/docs/en/latest/guides/context/", "contextos native/web, enumeração e troca conforme suporte do driver"),
    "app_drivers": ("Appium — Drivers", "https://appium.io/docs/en/latest/ecosystem/drivers/", "drivers separados, plataformas e modos suportados"),
    "app_migration": ("Appium — Migrating to Appium 2", "https://appium.io/docs/en/latest/guides/migrating-1-to-2/", "arquitetura modular, instalação de drivers e vendor prefixes"),
    "app_migration3": ("Appium — Migrating to Appium 3", "https://appium.io/docs/en/latest/guides/migrating-2-to-3/", "mudanças de endpoint, comandos removidos e alternativas W3C/driver"),
    "app_test": ("Appium — Write a Test (JS)", "https://appium.io/docs/en/latest/quickstart/test-js/", "criação e término de sessão por cliente e capabilities de exemplo"),
    "app_grid": ("Appium — Appium and Selenium Grid", "https://appium.io/docs/en/latest/guides/grid/", "relay de sessões para nós com capabilities e devices"),
    "app_uia": ("Appium — UiAutomator2 Driver", "https://github.com/appium/appium-uiautomator2-driver", "opções e comportamento específico do driver Android UiAutomator2"),
    "app_xcui": ("Appium — XCUITest Driver", "https://github.com/appium/appium-xcuitest-driver", "opções e comportamento específico do driver Apple XCUITest"),
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
id: software.testes.tranche11.{number:06d}
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-11.md"
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
    expected_number = 450
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
    if len(pending) != 100 or expected_number != 550:
        raise ValueError(f"esperadas 100 notas de 450 a 549, validadas {len(pending)}")
    if REPORT.exists():
        raise ValueError(f"relatório já existe: {REPORT}")

    # All note content and metadata pass the deterministic gate before any file is written.
    for number, row, context, content, quality in pending:
        (NOTES_DIR / f"{row['slug']}.md").write_text(content, encoding="utf-8")

    report = [
        "# Revisão factual assistida por IA — lote `software-testes-2000-0001`, tranche 11",
        "",
        f"- Data: {DATE}",
        "- Revisor: `Arena.ai Agent Mode`",
        "- Escopo: notas **450–549**, em dez grupos de dez; cada linha registra a conferência específica.",
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
    REPORT.write_text("\n".join(report).rstrip() + "\n", encoding="utf-8")
    word_counts = [quality["word_count"] for _, _, _, _, quality in pending]
    print(f"Geradas {len(pending)} notas substantivas (IDs 450–549); palavras: min={min(word_counts)}; max={max(word_counts)}")
    print(f"Relatório factual: {REPORT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
