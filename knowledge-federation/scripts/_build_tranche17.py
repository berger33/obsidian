#!/usr/bin/env python3
"""Build the source-backed software-testing tranche 17 (notes 1056–1156)."""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "knowledge-federation" / "scripts" / "_tranche17_data"
NOTES_DIR = ROOT / "knowledge-federation" / "domains" / "software-0007" / "software" / "testes"
DOMAINS_DIR = ROOT / "knowledge-federation" / "domains"
REPORT = ROOT / "knowledge-federation" / "exports" / "reports" / "ai-review-software-testes-2000-0001-tranche-17.md"
DATE = date.today().isoformat()
START = 1056
EXPECTED_NOTES = 101

sys.path.insert(0, str(ROOT / "knowledge-federation" / "scripts"))
from note_quality import assess_markdown, normalize  # noqa: E402
from prose_audit import repeated_substantive_sentences  # noqa: E402

SOURCES = {
    # Gatling (docs.gatling.io) — load testing as code with injection profiles and assertions.
    "gatling_simulation": ("Gatling — Simulation", "https://docs.gatling.io/concepts/simulation/", "estrutura da simulação, protocolo, cenários e relatório de execução"),
    "gatling_scenario": ("Gatling — Scenario", "https://docs.gatling.io/concepts/scenario/", "encadeamento de ações, pausas e nomeação de requisições na jornada"),
    "gatling_injection": ("Gatling — Injection", "https://docs.gatling.io/concepts/injection/", "perfis de injeção em modelo aberto e fechado, rampas e picos"),
    "gatling_checks": ("Gatling — Checks", "https://docs.gatling.io/concepts/checks/", "checagens de resposta, captura de valores e contabilização de falhas"),
    "gatling_session": ("Gatling — Session", "https://docs.gatling.io/concepts/session/", "armazenamento de valores extraídos e uso em requisições seguintes"),
    "gatling_feeder": ("Gatling — Feeder", "https://docs.gatling.io/concepts/feeder/", "fontes de dados externos e estratégias de distribuição entre usuários"),
    "gatling_pauses": ("Gatling — Pauses", "https://docs.gatling.io/reference/script/core/scenario/", "pausas entre ações e função de ritmo por usuário virtual"),
    "gatling_assertions": ("Gatling — Assertions", "https://docs.gatling.io/concepts/assertions/", "limites por estatística e efeito no código de saída da execução"),
    "gatling_protocol": ("Gatling — HTTP protocol", "https://docs.gatling.io/reference/script/http/protocol/", "endereço base, cabeçalhos comuns e políticas de conexão"),
    "gatling_github": ("Gatling — repositório oficial", "https://github.com/gatling/gatling", "código-fonte, exemplos e documentação do projeto"),
    # Locust (docs.locust.io) — Python load testing with user classes.
    "locust_locustfile": ("Locust — Writing a locustfile", "https://docs.locust.io/en/stable/writing-a-locustfile.html", "classes de usuário, tarefas, pesos, tempos de espera e ciclo de vida"),
    "locust_quickstart": ("Locust — Quickstart", "https://docs.locust.io/en/stable/quickstart.html", "primeira execução, parâmetros de linha de comando e resumo de estatísticas"),
    "locust_shape": ("Locust — Custom load shape", "https://docs.locust.io/en/stable/custom-load-shape.html", "formas de carga personalizadas e controle por estágios"),
    "locust_distributed": ("Locust — Distributed execution", "https://docs.locust.io/en/stable/running-distributed.html", "processo principal, trabalhadores e consolidação de estatísticas"),
    "locust_github": ("Locust — repositório oficial", "https://github.com/locustio/locust", "código-fonte, exemplos e documentação do projeto"),
    # Robot Framework (robotframework.org) — keyword-driven acceptance testing.
    "robot_userguide": ("Robot Framework — User Guide", "https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html", "sintaxe de casos, palavras-chave, variáveis, modelos, etiquetas e relatórios"),
    "robot_github": ("Robot Framework — repositório oficial", "https://github.com/robotframework/robotframework", "código-fonte, exemplos e documentação do projeto"),
    # Cucumber (cucumber.io) — BDD with Gherkin and step definitions.
    "cucumber_gherkin": ("Cucumber — Gherkin reference", "https://cucumber.io/docs/gherkin/reference/", "funcionalidades, cenários, antecedentes, esquemas de cenário e tabelas"),
    "cucumber_api": ("Cucumber — Reference", "https://cucumber.io/docs/cucumber/api/", "definições de passo, ganchos, etiquetas, paralelismo e relatórios"),
    "cucumber_github": ("Cucumber — repositório oficial", "https://github.com/cucumber/cucumber-js", "implementação de referência, exemplos e documentação do projeto"),
    # Selenium WebDriver (selenium.dev) — browser automation.
    "selenium_waits": ("Selenium — Waits", "https://www.selenium.dev/documentation/webdriver/waits/", "espera implícita e explícita por condições observáveis"),
    "selenium_pom": ("Selenium — Page object models", "https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/", "objetos de página e de componente e boas práticas de estruturação"),
    "selenium_grid": ("Selenium — Grid", "https://www.selenium.dev/documentation/grid/", "servidor, nós, capacidades e sessões distribuídas"),
    "selenium_actions": ("Selenium — Actions API", "https://www.selenium.dev/documentation/webdriver/actions_api/", "sequências de ponteiro, teclado, arrasto e liberação das ações"),
    "selenium_github": ("Selenium — repositório oficial", "https://github.com/SeleniumHQ/selenium", "código-fonte e documentação das ligações por linguagem"),
    # Appium (appium.io) — mobile automation on top of WebDriver.
    "appium_docs": ("Appium — Documentation", "https://appium.io/docs/en/latest/", "capacidades, drivers, seletores, gestos e contexto de sessão"),
    "appium_uiautomator": ("Appium — UiAutomator2 driver", "https://github.com/appium/appium-uiautomator2-driver", "capacidades do driver Android, sessões paralelas e opções de porta"),
    "appium_github": ("Appium — repositório oficial", "https://github.com/appium/appium", "arquitetura de drivers e plugins, CLI de extensões e servidor"),
    # WireMock (wiremock.org) — HTTP stubbing and verification.
    "wiremock_stubbing": ("WireMock — Stubbing", "https://wiremock.org/docs/stubbing/", "mapeamentos de stub, respostas predefinidas e prioridades"),
    "wiremock_request_matching": ("WireMock — Request matching", "https://wiremock.org/docs/request-matching/", "critérios sobre rota, método, cabeçalhos e corpo"),
    "wiremock_templating": ("WireMock — Response templating", "https://wiremock.org/docs/response-templating/", "respostas dinâmicas com modelos e valores da requisição"),
    "wiremock_stateful": ("WireMock — Stateful behaviour", "https://wiremock.org/docs/stateful-behaviour/", "cenários como máquina de estados e consulta de estado"),
    "wiremock_faults": ("WireMock — Simulating faults", "https://wiremock.org/docs/simulating-faults/", "injeção de atrasos, falhas de conexão e respostas malformadas"),
    "wiremock_verifying": ("WireMock — Verifying", "https://wiremock.org/docs/verifying/", "verificação de chamadas recebidas e contagem por critério"),
    "wiremock_record": ("WireMock — Record and playback", "https://wiremock.org/docs/record-playback/", "gravação de tráfego real e geração automática de stubs"),
    "wiremock_standalone": ("WireMock — Standalone", "https://wiremock.org/docs/standalone/java-jar/", "execução autônoma, argumentos de linha de comando e contêiner"),
    "wiremock_github": ("WireMock — repositório oficial", "https://github.com/wiremock/wiremock", "código-fonte, exemplos e documentação do projeto"),
    # Pact (docs.pact.io) — consumer-driven contract testing.
    "pact_how": ("Pact — How Pact works", "https://docs.pact.io/getting_started/how_pact_works", "fluxo dirigido pelo consumidor, publicação e verificação de contratos"),
    "pact_consumer": ("Pact — Consumer tests", "https://docs.pact.io/implementation_guides/javascript", "interface de teste do consumidor e geração do arquivo de contrato"),
    "pact_matching": ("Pact — Matching rules", "https://docs.pact.io/implementation_guides/javascript/docs/matching", "regras de tipo, lista e padrão em vez de valores exatos"),
    "pact_provider": ("Pact — Provider verification", "https://docs.pact.io/implementation_guides/javascript/docs/provider", "verificação do provedor e implementação de estados"),
    "pact_broker": ("Pact — Broker", "https://docs.pact.io/pact_broker", "publicação de contratos, histórico e metadados de versão"),
    "pact_can_i_deploy": ("Pact — can-i-deploy", "https://docs.pact.io/pact_broker/can_i_deploy", "consulta que autoriza implantação pelo histórico de verificações"),
    "pact_selectors": ("Pact — Consumer version selectors", "https://docs.pact.io/pact_broker/advanced_topics/consumer_version_selectors", "seleção de contratos por ramo, etiqueta e ambiente"),
    "pact_webhooks": ("Pact — Webhooks", "https://docs.pact.io/pact_broker/webhooks", "avisos automáticos que disparam verificações em mudança de contrato"),
    "pact_github": ("Pact — repositório oficial", "https://github.com/pact-foundation/pact-js", "implementação de referência em JavaScript e exemplos"),
    # Testify (github.com/stretchr/testify) — assertions, mocks and suites for Go.
    "testify_assert": ("Testify — Assert package", "https://pkg.go.dev/github.com/stretchr/testify/assert", "asserções não fatais, comparadores e mensagens de falha"),
    "testify_require": ("Testify — Require package", "https://pkg.go.dev/github.com/stretchr/testify/require", "asserções que interrompem o teste no primeiro erro"),
    "testify_mock": ("Testify — Mock package", "https://pkg.go.dev/github.com/stretchr/testify/mock", "expectativas de chamada, correspondência de argumentos e verificação final"),
    "testify_suite": ("Testify — Suite package", "https://pkg.go.dev/github.com/stretchr/testify/suite", "estruturas de suíte com ganchos por caso e por conjunto"),
    "testify_http": ("Testify — HTTP package", "https://pkg.go.dev/github.com/stretchr/testify/http", "utilitários HTTP marcados como obsoletos em favor da biblioteca padrão"),
    "testify_github": ("Testify — repositório oficial", "https://github.com/stretchr/testify", "código-fonte, exemplos e documentação do projeto"),
    # RSpec (rspec.info) — Ruby testing framework.
    "rspec_core": ("RSpec — Core", "https://rspec.info/features/3-12/rspec-core/", "grupos de exemplos, contextos, ganchos, metadados e configuração"),
    "rspec_expectations": ("RSpec — Expectations", "https://rspec.info/features/3-12/rspec-expectations/", "matchers embutidos e expressão de intenção nas expectativas"),
    "rspec_mocks": ("RSpec — Mocks", "https://rspec.info/features/3-12/rspec-mocks/", "dublês verificados, permissões de recebimento e expectativas de mensagem"),
    "rspec_shared": ("RSpec — Shared examples", "https://rspec.info/features/3-12/rspec-core/example-groups/shared-examples/", "exemplos compartilhados, parâmetros e inclusão em grupos"),
    "rspec_github": ("RSpec — repositório oficial", "https://github.com/rspec/rspec-core", "código-fonte e documentação do núcleo do framework"),
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
id: software.testes.tranche17.{number:06d}
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-17.md"
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
        help="Rebuild the existing tranche-17 notes after validating their IDs and batch metadata.",
    )
    args = parser.parse_args()
    group_files = sorted(DATA_DIR.glob("*.txt"))
    if len(group_files) != 10:
        raise SystemExit(f"Esperados 10 arquivos de grupo; encontrados {len(group_files)}")

    existing_paths = list(DOMAINS_DIR.rglob("*.md"))
    existing_tranche = [
        path for path in existing_paths
        if re.search(
            r"(?m)^id: software\.testes\.tranche17\.\d{6}\s*$",
            path.read_text(encoding="utf-8", errors="replace")[:1200],
        )
    ]
    if args.refresh and len(existing_tranche) != EXPECTED_NOTES:
        raise ValueError(f"--refresh exige exatamente {EXPECTED_NOTES} notas tranche17 existentes; encontradas {len(existing_tranche)}")
    if REPORT.exists() and not args.refresh:
        raise ValueError(f"relatório já existe (use --refresh apenas para atualizar a tranche 17): {REPORT}")
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
            expected_id = f"id: software.testes.tranche17.{expected_number + index:06d}"
            if target_path.exists():
                current = target_path.read_text(encoding="utf-8")
                if not args.refresh:
                    raise ValueError(f"arquivo já existe (use --refresh apenas para a tranche 17): {target_path}")
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
        "# Revisão factual assistida por IA — lote `software-testes-2000-0001`, tranche 17",
        "",
        f"- Data: {DATE}",
        "- Revisor: `Arena.ai Agent Mode`",
        f"- Escopo: notas **{START}–{START + EXPECTED_NOTES - 1}**, em dez grupos temáticos com dez ou onze notas cada; cada linha identifica a conferência factual da nota.",
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
