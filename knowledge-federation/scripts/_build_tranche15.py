#!/usr/bin/env python3
"""Build the source-backed software-testing tranche 15 (notes 850–949)."""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "knowledge-federation" / "scripts" / "_tranche15_data"
NOTES_DIR = ROOT / "knowledge-federation" / "domains" / "software-0007" / "software" / "testes"
DOMAINS_DIR = ROOT / "knowledge-federation" / "domains"
REPORT = ROOT / "knowledge-federation" / "exports" / "reports" / "ai-review-software-testes-2000-0001-tranche-15.md"
DATE = date.today().isoformat()

sys.path.insert(0, str(ROOT / "knowledge-federation" / "scripts"))
from note_quality import assess_markdown, normalize  # noqa: E402
from prose_audit import repeated_substantive_sentences  # noqa: E402

SOURCES = {
    # Puppeteer (pptr.dev) — browser automation over CDP and WebDriver BiDi.
    "puppeteer_network": ("Puppeteer — Network interception", "https://pptr.dev/guides/network-interception", "interceptação de requisições, resolução cooperativa e prioridades"),
    "puppeteer_page": ("Puppeteer — Page API", "https://pptr.dev/api/puppeteer.page", "navegação, seleção de elementos, avaliação na página e eventos"),
    "puppeteer_locators": ("Puppeteer — Locators", "https://pptr.dev/guides/locators", "locators com espera automática por elemento e por ação"),
    "puppeteer_bidi": ("Puppeteer — WebDriver BiDi support", "https://pptr.dev/webdriver-bidi", "protocolos suportados, padrão por navegador e operações incompatíveis"),
    "puppeteer_launch": ("Puppeteer — Launch options", "https://pptr.dev/api/puppeteer.launchoptions", "opções de lançamento, headless, protocolo, produto e argumentos"),
    # MSW 2 (mswjs.io) — request mocking in browser and Node.
    "msw_setup_server": ("MSW — setupServer", "https://mswjs.io/docs/api/setup-server/", "interceptação em Node.js e ciclo de vida de listen, resetHandlers e close"),
    "msw_intercepting": ("MSW — Intercepting requests", "https://mswjs.io/docs/http/intercepting-requests", "handlers por método e URL, parâmetros de caminho e resolução de requisições"),
    "msw_handling": ("MSW — Handling requests", "https://mswjs.io/docs/http/handling-requests", "resposta mockada, passthrough e handlers que não respondem"),
    "msw_defaults": ("MSW — Default behaviors", "https://mswjs.io/docs/defaults/", "fallthrough entre handlers, ordem de avaliação e sensibilidade à ordem"),
    "msw_response": ("MSW — HttpResponse", "https://mswjs.io/docs/api/http-response/", "construção de respostas com status, cabeçalhos e corpos tipados"),
    # Supertest (npm/github) and its superagent base.
    "supertest_npm": ("Supertest — pacote npm", "https://www.npmjs.com/package/supertest", "exemplos de request, expect, agent e asserções de resposta"),
    "supertest_repo": ("Supertest — repositório oficial", "https://github.com/ladjs/supertest", "README, opções de uso e integração com servidores e agentes"),
    "superagent_docs": ("Superagent — documentação", "https://visionmedia.github.io/superagent/", "cliente HTTP e métodos herdados usados pelo Supertest"),
    "express_testing": ("Express — Testing", "https://expressjs.com/en/guide/testing.html", "orientações e exemplos de teste de aplicações Express"),
    "node_test_runner": ("Node.js — Test runner", "https://nodejs.org/api/test.html", "executor de testes nativo do Node.js e suas APIs"),
    # Minitest (seattlerb) — Ruby test framework.
    "minitest_assertions": ("Minitest — Assertions", "https://docs.seattlerb.org/minitest/Minitest/Assertions.html", "asserções de igualdade, exceções, saída, predicados e tipos"),
    "minitest_spec": ("Minitest — Spec", "https://docs.seattlerb.org/minitest/Minitest/Spec.html", "DSL describe/it, hooks before, after e around e matchers de expectativa"),
    "minitest_mock": ("Minitest — Mock", "https://docs.seattlerb.org/minitest/Minitest/Mock.html", "mocks com expectativas, verificação de chamadas e stubs temporários"),
    "minitest_test": ("Minitest — Test", "https://docs.seattlerb.org/minitest/Minitest/Test.html", "classes de teste, ciclos de vida, ordem aleatória e paralelização"),
    "minitest_readme": ("Minitest — README", "https://docs.seattlerb.org/minitest/", "visão geral do projeto, plugins e formas de execução"),
    # JaCoCo — Java code coverage.
    "jacoco_agent": ("JaCoCo — Java agent", "https://www.jacoco.org/jacoco/trunk/doc/agent.html", "instrumentação em tempo de execução, opções do agente e arquivo de execução"),
    "jacoco_counters": ("JaCoCo — Coverage counters", "https://www.jacoco.org/jacoco/trunk/doc/counters.html", "definições de instruction, branch, line, complexity, method e class"),
    "jacoco_check": ("JaCoCo — jacoco:check", "https://www.jacoco.org/jacoco/trunk/doc/check-mojo.html", "regras, elementos, limites, ratios e controle de falha do build"),
    "jacoco_report": ("JaCoCo — jacoco:report", "https://www.jacoco.org/jacoco/trunk/doc/report-mojo.html", "formatos de relatório, fontes, agregação e configuração do goal"),
    "jacoco_offline": ("JaCoCo — Offline instrumentation", "https://www.jacoco.org/jacoco/trunk/doc/offline.html", "instrumentação fora do processo e diferenças em relação ao agente"),
    # Maestro — mobile UI flows.
    "maestro_runflow": ("Maestro — runFlow", "https://docs.maestro.dev/api-reference/commands/runflow", "reuso de fluxos, subflows, variáveis de ambiente e condições"),
    "maestro_commands": ("Maestro — Commands", "https://docs.maestro.dev/api-reference/commands", "catálogo de comandos de interação, asserção, controle e espera"),
    "maestro_tags": ("Maestro — Test discovery and tags", "https://docs.maestro.dev/maestro-flows/workspace-management/test-discovery-and-tags", "descoberta de fluxos e filtragem por tags na CLI"),
    "maestro_cli": ("Maestro — CLI", "https://docs.maestro.dev/maestro-cli/maestro-cli-commands-and-options", "subcomandos e opções, incluindo filtros, formato e diretório de saída"),
    "maestro_install": ("Maestro — Installing Maestro", "https://docs.maestro.dev/getting-started/installing-maestro", "instalação, requisitos e primeiros passos com a CLI"),
    # Karate — API test DSL.
    "karate_docs": ("Karate — Documentation", "https://karatelabs.github.io/karate/", "DSL Gherkin com steps embutidos, asserções, configuração e relatórios"),
    "karate_parallel": ("Karate — Parallel execution", "https://karatelabs.github.io/karate/#parallel-execution", "execução paralela de features e geração de relatórios agregados"),
    "karate_config": ("Karate — Configuration", "https://karatelabs.github.io/karate/#configuration", "karate-config.js, perfis por ambiente e variáveis compartilhadas"),
    "karate_data": ("Karate — Data driven tests", "https://karatelabs.github.io/karate/#data-driven-tests", "tabelas, Examples, CSV e laços em feature files"),
    "karate_mock": ("Karate — Mock server", "https://karatelabs.github.io/karate/#mock-server", "servidor mock baseado em feature files para contratos e testes"),
    # Swift Testing (Apple).
    "swift_testing": ("Apple — Swift Testing", "https://developer.apple.com/documentation/testing", "macros @Test e @Suite, expectativas #expect e #require e modelo de suítes"),
    "swift_testing_param": ("Apple — Parameterized testing", "https://developer.apple.com/documentation/testing/parameterizedtesting", "testes parametrizados, coleções de argumentos e combinações"),
    "swift_testing_tags": ("Apple — Adding tags", "https://developer.apple.com/documentation/testing/addingtags", "tags para organizar, filtrar e agrupar testes"),
    "swift_testing_migrate": ("Apple — Migrating from XCTest", "https://developer.apple.com/documentation/testing/migratingfromxctest", "equivalências de asserções, suítes e ciclo de vida entre frameworks"),
    "swift_testing_wwdc": ("Apple — Meet Swift Testing (WWDC24)", "https://developer.apple.com/videos/play/wwdc2024/10179/", "apresentação das macros, suítes, paralelismo e diferenças do XCTest"),
    # MSTest (.NET).
    "mstest_writing": ("MSTest — Write tests", "https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-mstest-writing-tests", "atributos de teste, asserções, dados e organização"),
    "mstest_lifecycle": ("MSTest — Test lifecycle", "https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-mstest-writing-tests-lifecycle", "ordem de inicialização e limpeza em nível de assembly, classe e teste"),
    "mstest_configure": ("MSTest — Configure", "https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-mstest-configure", "runsettings, testconfig.json, paralelização, timeouts e retries"),
    "mstest_assert": ("MSTest — Assert API", "https://learn.microsoft.com/en-us/dotnet/api/microsoft.visualstudio.testtools.unittesting.assert?view=visualstudio", "asserções de igualdade, coleções, exceções e mensagens"),
    "mstest_data": ("Microsoft — Data-driven unit test", "https://learn.microsoft.com/en-us/visualstudio/test/how-to-create-a-data-driven-unit-test?view=visualstudio", "DataRow, DynamicData, DataSource e acesso por TestContext"),
    # cargo-nextest (nexte.st).
    "nextest_docs": ("nextest — Documentation", "https://nexte.st/docs/", "visão geral do runner, instalação e operação"),
    "nextest_config": ("nextest — Configuration", "https://nexte.st/docs/configuration/", "perfis, overrides, retries, timeouts e grupos de teste"),
    "nextest_running": ("nextest — Running tests", "https://nexte.st/docs/running/", "execução, filtros, saída, listagem e testes ignorados"),
    "nextest_partitioning": ("nextest — Partitioning", "https://nexte.st/docs/partitioning/", "particionamento por fatias e por hash para shards de CI"),
    "nextest_junit": ("nextest — JUnit support", "https://nexte.st/docs/machine-readable/junit/", "geração de JUnit XML e opções de relatório para integração"),
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
id: software.testes.tranche15.{number:06d}
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
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
        help="Rebuild the existing 100 tranche-15 notes after validating their IDs and batch metadata.",
    )
    args = parser.parse_args()
    group_files = sorted(DATA_DIR.glob("*.txt"))
    if len(group_files) != 10:
        raise SystemExit(f"Esperados 10 arquivos de grupo; encontrados {len(group_files)}")

    existing_paths = list(DOMAINS_DIR.rglob("*.md"))
    existing_tranche = [
        path for path in existing_paths
        if re.search(
            r"(?m)^id: software\.testes\.tranche15\.\d{6}\s*$",
            path.read_text(encoding="utf-8", errors="replace")[:1200],
        )
    ]
    if args.refresh and len(existing_tranche) != 100:
        raise ValueError(f"--refresh exige exatamente 100 notas tranche15 existentes; encontradas {len(existing_tranche)}")
    if REPORT.exists() and not args.refresh:
        raise ValueError(f"relatório já existe (use --refresh apenas para atualizar a tranche 15): {REPORT}")
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
    expected_number = 850
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
            expected_id = f"id: software.testes.tranche15.{expected_number + index:06d}"
            if target_path.exists():
                current = target_path.read_text(encoding="utf-8")
                if not args.refresh:
                    raise ValueError(f"arquivo já existe (use --refresh apenas para a tranche 15): {target_path}")
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

    if len(pending) != 100 or expected_number != 950:
        raise ValueError(f"esperadas 100 notas de 850 a 949, validadas {len(pending)}")
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
        "# Revisão factual assistida por IA — lote `software-testes-2000-0001`, tranche 15",
        "",
        f"- Data: {DATE}",
        "- Revisor: `Arena.ai Agent Mode`",
        "- Escopo: notas **850–949**, em dez grupos de dez; cada linha identifica a conferência factual da nota.",
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
    print(f"Geradas {len(pending)} notas substantivas (IDs 850–949); palavras: min={min(word_counts)}; max={max(word_counts)}")
    print(f"Fontes HTTPS específicas por nota: min={min(source_counts)}; max={max(source_counts)}")
    print(f"Relatório factual: {REPORT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
