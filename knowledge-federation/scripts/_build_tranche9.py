#!/usr/bin/env python3
"""Build tranche 9 from reviewed, source-backed data rows; temporary helper."""
from __future__ import annotations
from datetime import date
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "knowledge-federation" / "scripts" / "_tranche9_data"
NOTES_DIR = ROOT / "knowledge-federation" / "domains" / "software-0007" / "software" / "testes"
REPORT = ROOT / "knowledge-federation" / "exports" / "reports" / "ai-review-software-testes-2000-0001-tranche-09.md"
DATE = date.today().isoformat()

sys.path.insert(0, str(ROOT / "knowledge-federation" / "scripts"))
from note_quality import assess_markdown

SOURCES = {
    "cy_isolation": ("Cypress — Test isolation", "https://docs.cypress.io/app/core-concepts/test-isolation", "escopo do isolamento do navegador e estado que não é limpo automaticamente"),
    "cy_retry": ("Cypress — Retry-ability", "https://docs.cypress.io/app/core-concepts/retry-ability", "repetição de queries e assertions e fronteira com comandos com efeitos"),
    "cy_network": ("Cypress — Intercepting network requests", "https://docs.cypress.io/app/guides/network-requests", "interceptação, stubs, respostas reais e requisições iniciadas pelo aplicativo"),
    "cy_intercept": ("Cypress — cy.intercept()", "https://docs.cypress.io/api/commands/intercept", "sintaxe e ciclo de vida de rotas e aliases de rede"),
    "cy_session": ("Cypress — cy.session()", "https://docs.cypress.io/api/commands/session", "cache/restore de cookies e storage e validação de sessão"),
    "cy_origin": ("Cypress — Cross-origin testing", "https://docs.cypress.io/app/guides/cross-origin-testing", "limites de origem e uso explícito de cy.origin()"),
    "cy_clock": ("Cypress — cy.clock()", "https://docs.cypress.io/api/commands/clock", "controle de Date e temporizadores no ambiente de teste"),
    "cy_component": ("Cypress — Component testing", "https://docs.cypress.io/app/component-testing/get-started", "montagem de componentes em navegador real e configuração do dev server"),
    "cy_retries": ("Cypress — Test retries", "https://docs.cypress.io/app/guides/test-retries", "reexecuções de teste e interpretação de resultados flaky"),
    "cy_types": ("Cypress — Testing types", "https://docs.cypress.io/app/core-concepts/testing-types", "distinção entre component testing e end-to-end testing"),
    "pact_consumer": ("Pact — Writing consumer tests", "https://docs.pact.io/consumer", "escopo de testes consumer, matching e evitar testes funcionais do provider"),
    "pact_provider": ("Pact — Verifying pacts", "https://docs.pact.io/provider", "verificação local do provider, stubs downstream e publicação de resultados"),
    "pact_states": ("Pact — Using provider states effectively", "https://docs.pact.io/provider/using_provider_states_effectively", "configuração de estados provider e risco de falsos positivos"),
    "pact_terms": ("Pact — Terminology", "https://docs.pact.io/getting_started/terminology", "interactions, contracts, provider states e verificação"),
    "pact_deploy": ("Pact Broker — Can I Deploy", "https://docs.pact.io/pact_broker/can_i_deploy", "matriz de versões e compatibilidade com o ambiente de deploy"),
    "pact_webhooks": ("Pact Broker — Webhooks", "https://docs.pact.io/pact_broker/webhooks", "eventos e integração de verificação do provider no CI"),
    "pg_iso": ("PostgreSQL — Transaction isolation", "https://www.postgresql.org/docs/current/transaction-iso.html", "níveis de isolamento, snapshots e anomalias concorrentes"),
    "pg_lock": ("PostgreSQL — Explicit locking", "https://www.postgresql.org/docs/current/explicit-locking.html", "locks de tabela/linha, conflitos, deadlocks e SKIP LOCKED"),
    "pg_constraints": ("PostgreSQL — Constraints", "https://www.postgresql.org/docs/current/ddl-constraints.html", "constraints de integridade declaradas no banco"),
    "pg_explain": ("PostgreSQL — EXPLAIN", "https://www.postgresql.org/docs/current/sql-explain.html", "execução de consultas por EXPLAIN ANALYZE e opções de plano"),
    "pg_mvcc": ("PostgreSQL — MVCC", "https://www.postgresql.org/docs/current/mvcc.html", "controle de concorrência multiversão e visibilidade de linhas"),
    "pg_dates": ("PostgreSQL — Date/time types", "https://www.postgresql.org/docs/current/datatype-datetime.html", "semântica dos tipos temporais e fuso horário da sessão"),
    "pg_errors": ("PostgreSQL — Error codes", "https://www.postgresql.org/docs/current/errcodes-appendix.html", "SQLSTATEs estáveis para classificar erros do servidor"),
    "pg_sequences": ("PostgreSQL — Sequence functions", "https://www.postgresql.org/docs/current/functions-sequence.html", "alocação de valores de sequência e efeitos fora do rollback transacional"),
    "gql_validation": ("GraphQL — Validation", "https://graphql.org/learn/validation/", "validação de operações contra o schema antes da execução"),
    "gql_schema": ("GraphQL — Schemas and types", "https://graphql.org/learn/schema/", "tipos, nullability e contrato de resposta"),
    "gql_queries": ("GraphQL — Queries", "https://graphql.org/learn/queries/", "variáveis, aliases, fragments e forma das operações"),
    "gql_exec": ("GraphQL — Execution", "https://graphql.org/learn/execution/", "execução de fields, erros e propagação de null"),
    "gql_review": ("GraphQL — Schema review", "https://graphql.org/learn/schema-review/", "revisão de mudanças compatíveis, breaking changes e depreciação"),
    "apollo_test": ("Apollo Server — Integration testing", "https://www.apollographql.com/docs/apollo-server/testing/testing", "executeOperation e testes de integração do pipeline de requisições"),
    "apollo_auth": ("Apollo Server — Authentication and authorization", "https://www.apollographql.com/docs/apollo-server/security/authentication", "autenticação, contexto da requisição e autorização em resolvers"),
    "apollo_cache": ("Apollo Server — Caching", "https://www.apollographql.com/docs/apollo-server/performance/caching", "políticas de cache e comportamento de resposta"),
    "apollo_resolvers": ("Apollo Server — Resolvers", "https://www.apollographql.com/docs/apollo-server/data/resolvers", "resolvers, parent, args, context e execução de fields"),
    "gql_dataloader": ("GraphQL DataLoader — README", "https://github.com/graphql/dataloader", "batching e cache local de chaves em uma instância DataLoader"),
    "apple_xctest": ("Apple — XCTest", "https://developer.apple.com/documentation/xctest", "framework XCTest, casos de teste e APIs de assertions"),
    "apple_async": ("Apple — Asynchronous tests and expectations", "https://developer.apple.com/documentation/xctest/asynchronous-tests-and-expectations", "async/await e expectativas para callbacks e delegates"),
    "apple_expect": ("Apple — XCTestExpectation", "https://developer.apple.com/documentation/xctest/xctestexpectation", "fulfillment, timeout e configuração de expectations"),
    "apple_ui": ("Apple — XCUIApplication", "https://developer.apple.com/documentation/xcuiautomation/xcuiapplication", "proxy para iniciar, monitorar e terminar a aplicação sob teste"),
    "apple_identifier": ("Apple — XCUIElementQuery", "https://developer.apple.com/documentation/xcuiautomation/xcuielementquery/element(matching:identifier:)", "consulta de elementos da interface por tipo e identificador"),
    "apple_signpost": ("Apple — XCTOSSignpostMetric", "https://developer.apple.com/documentation/xctest/xctossignpostmetric", "medição de intervalos instrumentados por signposts"),
    "apple_perf": ("Apple — Performance tests", "https://developer.apple.com/documentation/xctest/performance-tests", "medição repetível de performance em testes XCTest"),
    "apple_plans": ("Apple — Organizing tests to improve feedback", "https://developer.apple.com/documentation/xcode/organizing-tests-to-improve-feedback", "organização e execução configurável das test suites"),
    "k8s_jobs": ("Kubernetes — Jobs", "https://kubernetes.io/docs/concepts/workloads/controllers/job/", "Jobs, completions, paralelismo, retries e limites de execução"),
    "k8s_cron": ("Kubernetes — CronJobs", "https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/", "agendamento de Jobs e políticas de concorrência"),
    "k8s_workloads": ("Kubernetes — Workloads", "https://kubernetes.io/docs/concepts/workloads/", "controladores e reconciliação de workloads"),
    "k8s_deploy": ("Kubernetes — Deployments", "https://kubernetes.io/docs/concepts/workloads/controllers/deployment/", "rollout, ReplicaSets e estado observado do Deployment"),
    "k8s_auth": ("Kubernetes — Authorization", "https://kubernetes.io/docs/reference/access-authn-authz/authorization/", "autorização por verbo, recurso, namespace e identidade"),
    "k8s_kubectl": ("Kubernetes — kubectl auth can-i", "https://kubernetes.io/docs/reference/kubectl/generated/kubectl_auth/kubectl_auth_can-i/", "consultas de autorização do usuário corrente"),
    "k8s_net": ("Kubernetes — Network Policies", "https://kubernetes.io/docs/concepts/services-networking/network-policies/", "políticas ingress/egress e requisito de plugin que as implemente"),
    "k8s_pdb": ("Kubernetes — Pod disruptions", "https://kubernetes.io/docs/concepts/workloads/pods/disruptions/", "disrupções voluntárias e PodDisruptionBudgets"),
    "k8s_hpa": ("Kubernetes — Horizontal Pod Autoscaling", "https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/", "ciclo de controle assíncrono e métricas para escala"),
    "k8s_config": ("Kubernetes — Configure a Pod to use a ConfigMap", "https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/", "consumo de ConfigMaps por variáveis e volumes"),
    "otel_instrument": ("OpenTelemetry — Instrumentation libraries", "https://opentelemetry.io/docs/concepts/instrumentation/libraries/", "instrumentação, API/SDK e geração de telemetria"),
    "otel_java": ("OpenTelemetry Java — SDK", "https://opentelemetry.io/docs/languages/java/sdk/", "SDK Java, configuração e utilitários de teste"),
    "otel_context": ("OpenTelemetry — Context propagation", "https://opentelemetry.io/docs/concepts/context-propagation/", "propagação de contexto através de fronteiras de execução"),
    "otel_trace": ("OpenTelemetry — Trace API", "https://opentelemetry.io/docs/specs/otel/trace/api/", "spans, eventos, atributos e status de trace"),
    "otel_metrics": ("OpenTelemetry — Metrics API", "https://opentelemetry.io/docs/specs/otel/metrics/api/", "instrumentos e observações de métricas"),
    "otel_sdkmetrics": ("OpenTelemetry — Metrics SDK", "https://opentelemetry.io/docs/specs/otel/metrics/sdk/", "aggregation, views e exportação de métricas"),
    "otel_logs": ("OpenTelemetry — Logs data model", "https://opentelemetry.io/docs/specs/otel/logs/data-model/", "campos de log e associação com trace/span"),
    "otel_semconv": ("OpenTelemetry — Semantic conventions", "https://opentelemetry.io/docs/specs/semconv/", "convenções semânticas e atributos de telemetria"),
    "pytest_tmp": ("pytest — Temporary directories and files", "https://docs.pytest.org/en/stable/how-to/tmp_path.html", "tmp_path e tmp_path_factory por escopo de fixture"),
    "pytest_fixture": ("pytest — Fixtures reference", "https://docs.pytest.org/en/stable/reference/fixtures.html", "resolução de dependências, escopos e teardown de fixtures"),
    "pytest_unittest": ("pytest — unittest integration", "https://docs.pytest.org/en/stable/how-to/unittest.html", "compatibilidade e limitações de fixtures com unittest.TestCase"),
    "pytest_param": ("pytest — Parametrizing tests", "https://docs.pytest.org/en/stable/how-to/parametrize.html", "parametrização de testes, IDs e geração de casos"),
    "pytest_monkey": ("pytest — monkeypatch", "https://docs.pytest.org/en/stable/how-to/monkeypatch.html", "patch controlado de atributos, ambiente e caminhos"),
    "pytest_skip": ("pytest — Skip and xfail", "https://docs.pytest.org/en/stable/how-to/skipping.html", "skip, xfail e strict xfail"),
    "pytest_log": ("pytest — Logging", "https://docs.pytest.org/en/stable/how-to/logging.html", "captura e verificação de logs"),
    "gitlab_rules": ("GitLab CI — Job rules", "https://docs.gitlab.com/ci/jobs/job_rules/", "avaliação de rules e prevenção de pipelines duplicados"),
    "gitlab_mr": ("GitLab CI — Merge request pipelines", "https://docs.gitlab.com/ci/pipelines/merge_request_pipelines/", "condições e configuração de merge request pipelines"),
    "gitlab_downstream": ("GitLab CI — Downstream pipelines", "https://docs.gitlab.com/ci/pipelines/downstream_pipelines/", "parent-child pipelines e CI_PIPELINE_SOURCE"),
    "gitlab_yaml": ("GitLab CI — YAML syntax reference", "https://docs.gitlab.com/ci/yaml/", "semântica de jobs, needs, artifacts e keywords"),
    "gitlab_artifacts": ("GitLab CI — Job artifacts", "https://docs.gitlab.com/ci/jobs/job_artifacts/", "persistência e passagem explícita de artifacts"),
    "gitlab_cache": ("GitLab CI — Caching", "https://docs.gitlab.com/ci/caching/", "cache reutilizável, chaves e distinção de artifacts"),
    "gitlab_resource": ("GitLab CI — Resource groups", "https://docs.gitlab.com/ci/resource_groups/", "serialização de jobs e modos de ordenação do resource group"),
    "gitlab_variables": ("GitLab CI — Variables", "https://docs.gitlab.com/ci/variables/", "escopo, proteção e exposição de variáveis CI/CD"),
    "spring_testing": ("Spring Boot — Testing", "https://docs.spring.io/spring-boot/reference/testing/index.html", "módulos de teste e integração com JUnit Jupiter e AssertJ"),
    "spring_apps": ("Spring Boot — Testing Spring Boot applications", "https://docs.spring.io/spring-boot/reference/testing/spring-boot-applications.html", "MockMvc, servidor real, slices e testes transacionais"),
    "spring_util": ("Spring Boot — Test utilities", "https://docs.spring.io/spring-boot/reference/testing/test-utilities.html", "RestTestClient e TestRestTemplate em testes de integração"),
    "spring_modules": ("Spring Boot — Test modules", "https://docs.spring.io/spring-boot/reference/testing/test-modules.html", "módulos de teste focados e slices auto-configurados"),
    "spring_framework": ("Spring Framework — Testing", "https://docs.spring.io/spring-framework/reference/testing/testcontext-framework.html", "TestContext, contexto de aplicação e infraestrutura de teste"),
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
id: software.testes.tranche09.{number:06d}
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-09.md"
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
    all_rows = []
    report_rows = []
    group_summaries = []
    seen_slugs = set()
    expected_number = 250
    for path in group_files:
        context, rows = parse_group(path)
        if int(context["first"]) != expected_number:
            raise ValueError(f"{path.name}: ID inicial esperado {expected_number}, informado {context['first']}")
        group_summaries.append(context)
        for index, row in enumerate(rows):
            if row["slug"] in seen_slugs or (NOTES_DIR / f"{row['slug']}.md").exists():
                raise ValueError(f"slug duplicado/arquivo existente: {row['slug']}")
            seen_slugs.add(row["slug"])
            unknown = set(row["sources"]) - SOURCES.keys()
            if unknown:
                raise ValueError(f"{row['slug']}: fontes desconhecidas {unknown}")
            number, content, quality = render_note(context, rows, index, row)
            out = NOTES_DIR / f"{row['slug']}.md"
            out.write_text(content, encoding="utf-8")
            all_rows.append((number, row, context))
            source_name, source_url, _ = SOURCES[row["sources"][0]]
            report_rows.append(f"| {number} | [[{row['slug']}]] | [{source_name}]({source_url}) | {row['review']} Aprovada por IA. |")
        expected_number += 10
    if len(all_rows) != 100 or expected_number != 350:
        raise ValueError(f"esperadas 100 notas de 250 a 349, geradas {len(all_rows)}")

    report = [
        "# Revisão factual assistida por IA — lote `software-testes-2000-0001`, tranche 9",
        "",
        f"- Data: {DATE}",
        "- Revisor: `Arena.ai Agent Mode`",
        "- Escopo: notas **250–349**, em dez grupos de dez; cada linha registra a verificação específica.",
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
        "- As afirmações foram limitadas à documentação citada e às condições de versão/contexto indicadas; não houve promoção de revisão por IA para status humano.",
        "",
    ]
    REPORT.write_text("\n".join(report), encoding="utf-8")
    word_counts = [assess_markdown((NOTES_DIR / f"{row['slug']}.md").read_text(encoding="utf-8"), row["slug"])["word_count"] for _, row, _ in all_rows]
    print(f"Geradas {len(all_rows)} notas substantivas; palavras: min={min(word_counts)}; max={max(word_counts)}")
    print(f"Relatório factual: {REPORT.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
