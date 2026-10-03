#!/usr/bin/env python3
"""Build the source-backed software-testing tranche 15 (notes 850–949)."""
from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
import re
import sys
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "knowledge-federation" / "scripts" / "_tranche15_data"
NOTES_DIR = ROOT / "knowledge-federation" / "domains" / "software-0007" / "software" / "testes"
DOMAINS_DIR = ROOT / "knowledge-federation" / "domains"
REPORT = ROOT / "knowledge-federation" / "exports" / "reports" / "ai-review-software-testes-2000-0001-tranche-15.md"
DATE = datetime.now(ZoneInfo("America/Sao_Paulo")).date().isoformat()

sys.path.insert(0, str(ROOT / "knowledge-federation" / "scripts"))
from note_quality import assess_markdown, normalize  # noqa: E402
from prose_audit import repeated_substantive_sentences  # noqa: E402

SOURCES = {
    # pytest-xdist.
    "xdist_dist": ("pytest-xdist — Distribution", "https://pytest-xdist.readthedocs.io/en/stable/distribution.html", "algoritmos load, loadscope, loadfile, loadgroup e worksteal, identidade de workers e afinidade"),
    "xdist_main": ("pytest-xdist — Documentation", "https://pytest-xdist.readthedocs.io/en/stable/", "visão geral, execução paralela, recursos suportados e limitações de captura"),
    "xdist_howto": ("pytest-xdist — How-tos", "https://pytest-xdist.readthedocs.io/en/stable/how-to.html", "fixtures worker_id/testrun_uid, variáveis de ambiente e coordenação de fixtures de sessão"),
    "xdist_works": ("pytest-xdist — How it works", "https://pytest-xdist.readthedocs.io/en/stable/how-it-works.html", "arquitetura de controlador/workers, coleta e protocolo de execução"),
    "xdist_crash": ("pytest-xdist — When tests crash", "https://pytest-xdist.readthedocs.io/en/stable/crash.html", "reinício de workers e limite de processos que podem ser reiniciados"),
    "xdist_remote": ("pytest-xdist — Sending tests to remote SSH accounts", "https://pytest-xdist.readthedocs.io/en/stable/remote.html", "workers remotos, gateways SSH e requisitos de execução distribuída"),
    # cargo-nextest.
    "nextest_partition": ("cargo-nextest — Partitioning test runs in CI", "https://nexte.st/docs/ci-features/partitioning/", "partições slice/hash/count, distribuição por shard e combinação de resultados"),
    "nextest_filtersets": ("cargo-nextest — Filterset DSL", "https://nexte.st/docs/filtersets/", "predicados, união e interseção de filtros de testes e pacotes"),
    "nextest_archiving": ("cargo-nextest — Archiving and reusing builds", "https://nexte.st/docs/ci-features/archiving/", "conteúdo e requisitos de archives para separar build de execução"),
    "nextest_retries": ("cargo-nextest — Retries and flaky tests", "https://nexte.st/docs/features/retries/", "tentativas, resultado flaky, backoff, overrides e integração JUnit"),
    "nextest_reporting": ("cargo-nextest — JUnit support", "https://nexte.st/docs/machine-readable/junit/", "formato XML, inclusão de stdout/stderr, skipped tests e estado flaky"),
    "nextest_groups": ("cargo-nextest — Test groups for mutual exclusion", "https://nexte.st/docs/configuration/test-groups/", "semaforização de subconjuntos e limites de concorrência por grupo"),
    "nextest_configuration": ("cargo-nextest — Repository configuration", "https://nexte.st/docs/configuration/", "perfis, herança e precedência de configurações do repositório"),
    "nextest_profiles": ("cargo-nextest — Configuration reference", "https://nexte.st/docs/configuration/reference/", "opções padrão de perfis, overrides e caminhos de relatórios"),
    # coverage.py 7.16.x.
    "coverage_contexts": ("Coverage.py 7.16.2 — Measurement contexts", "https://coverage.readthedocs.io/en/latest/contexts.html", "contextos estáticos e dinâmicos, função de teste e filtros por contexto"),
    "coverage_config": ("Coverage.py 7.16.2 — Configuration reference", "https://coverage.readthedocs.io/en/latest/config.html", "opções run/report, arquivos paralelos, paths, exclusões e limites"),
    "coverage_subprocess": ("Coverage.py 7.16.2 — Managing processes", "https://coverage.readthedocs.io/en/latest/subprocess.html", "instrumentação de subprocessos, multiprocessing, ambiente e combinação"),
    "coverage_combine": ("Coverage.py 7.16.2 — Combining data files", "https://coverage.readthedocs.io/en/latest/commands/cmd_combine.html", "arquivos paralelos, combinação, remoção de entradas antigas e remapeamento de caminhos"),
    "coverage_branch": ("Coverage.py 7.16.2 — Branch coverage measurement", "https://coverage.readthedocs.io/en/latest/branch.html", "destinos parciais, linhas ausentes e pragma no branch"),
    "coverage_excluding": ("Coverage.py 7.16.2 — Excluding code", "https://coverage.readthedocs.io/en/latest/excluding.html", "exclusões de linhas/blocos e efeito sobre branch coverage"),
    "coverage_main": ("Coverage.py 7.16.2 — Documentation", "https://coverage.readthedocs.io/en/latest/", "origem medida, capacidades e visão geral dos relatórios"),
    "coverage_commands": ("Coverage.py 7.16.2 — coverage report", "https://coverage.readthedocs.io/en/latest/commands/cmd_report.html", "resumo, contexts, fail-under, formatos e colunas de branch"),
    "coverage_reports": ("Coverage.py 7.16.2 — Reporting", "https://coverage.readthedocs.io/en/latest/commands/cmd_reporting.html", "formatos text, HTML, XML, JSON, LCOV e opções comuns de saída"),
    # Pest 5.
    "pest_datasets": ("Pest 5 — Datasets", "https://pestphp.com/docs/datasets", "datasets inline/compartilhados, chaves, parâmetros nomeados e bound datasets"),
    "pest_writing": ("Pest 5 — Writing tests", "https://pestphp.com/docs/writing-tests", "definição de testes, closures e integração com expectativas"),
    "pest_hooks": ("Pest 5 — Hooks", "https://pestphp.com/docs/hooks", "ciclo beforeEach/afterEach e hooks de arquivo"),
    "pest_cli": ("Pest 5 — CLI API Reference", "https://pestphp.com/docs/cli-api-reference", "opções de seleção, execução, paralelismo, shards e reporters"),
    "pest_ci": ("Pest 5 — Continuous Integration", "https://pestphp.com/docs/continuous-integration", "execução integral em CI, browser plugin, parallel e artifacts"),
    "pest_optimizing": ("Pest 5 — Optimizing Tests", "https://pestphp.com/docs/optimizing-tests", "parallel testing, profiling, sharding balanceado por tempo e saída"),
    "pest_tia": ("Pest 5 — Tia Engine", "https://pestphp.com/docs/tia", "baseline de impact analysis, driver de cobertura, testes afetados e replay"),
    "pest_browser": ("Pest 5 — Browser Testing", "https://pestphp.com/docs/browser-testing", "Playwright, navegação, seletores, browsers, timeout e diagnóstico"),
    "playwright_actionability": ("Playwright — Auto-waiting", "https://playwright.dev/docs/actionability", "verificações de actionability de locators e retry de assertions com timeout"),
    "pest_arch": ("Pest 5 — Architecture Testing", "https://pestphp.com/docs/arch-testing", "expectativas de namespace, uso, tipo de classe e presets arquiteturais"),
    # Deno runtime current docs.
    "deno_fundamentals": ("Deno Runtime — Testing", "https://docs.deno.com/runtime/test/", "steps, timeouts, affected tests, permissões, snapshots, sanitizers e reporters"),
    "deno_test_ref": ("Deno Runtime — deno test", "https://docs.deno.com/runtime/reference/cli/test/", "flags de filtro, shard, cobertura, snapshots e execução do runner"),
    "deno_snapshot": ("Deno Runtime — Snapshot testing", "https://docs.deno.com/runtime/test/snapshots/", "criação e atualização de snapshots com --update-snapshots e revisão do diff"),
    "deno_sanitizers": ("Deno Runtime — Test sanitizers", "https://docs.deno.com/runtime/test/sanitizers/", "sanitizers de ops, resources e exit com níveis de precedência"),
    "deno_coverage": ("Deno Runtime — Test coverage", "https://docs.deno.com/runtime/test/coverage/", "coleta, limpeza, métricas, thresholds e exportação de cobertura"),
    "deno_coverage_cli": ("Deno Runtime — deno coverage CLI", "https://docs.deno.com/runtime/reference/cli/coverage/", "threshold único para lines/branches/functions, precedência sobre thresholds no deno.json e formatos"),
    # Kotest 6.2.
    "kotest_isolation": ("Kotest 6.2 — Isolation Modes", "https://kotest.io/docs/framework/isolation-mode.html", "instâncias de Spec, SingleInstance, InstancePerRoot e modos depreciados"),
    "kotest_project_config": ("Kotest 6.2 — Project Level Config", "https://kotest.io/docs/framework/project-config.html", "configuração de engine no nível do projeto e precedência"),
    "kotest_concurrency": ("Kotest 6.2 — Concurrency", "https://kotest.io/docs/framework/concurrency6.html", "concorrência de specs/testes, dispatcher e escopo por plataforma"),
    "kotest_data": ("Kotest 6.2 — Data Driven Testing", "https://kotest.io/docs/framework/datatesting/data-driven-testing.html", "variantes withXXX, hierarquia, nomes e linhas de dados"),
    "kotest_names": ("Kotest 6.2 — Data Test Names", "https://kotest.io/docs/framework/datatesting/custom-test-names.html", "estabilidade de nomes, map, nameFn e WithDataTestName"),
    "kotest_config": ("Kotest 6.2 — Framework configuration properties", "https://kotest.io/docs/framework/framework-config-props.html", "filtros, tags, discovery, isolamento e parâmetros de execução"),
    "kotest_empty": ("Kotest 6.2 — Fail On Empty Test Suite", "https://kotest.io/docs/framework/fail-on-empty-test-suite.html", "failOnEmptyTestSuite e falha de módulo quando nenhum teste é executado após filtros"),
    "kotest_shared_config": ("Kotest 6.2 — Shared Test Config", "https://kotest.io/docs/framework/sharedtestconfig.html", "defaults de teste, timeout, retry e precedência local"),
    "kotest_test_config": ("Kotest 6.2 — Test Case Config", "https://kotest.io/docs/framework/testcaseconfig.html", "tags, retries, extensões e configuração de caso"),
    "kotest_extensions": ("Kotest 6.2 — Simple Extensions", "https://kotest.io/docs/framework/extensions/simple-extensions.html", "listeners de lifecycle por instância ou spec"),
    "kotest_setup": ("Kotest 6.2 — Setup", "https://kotest.io/docs/framework/project-setup.html", "diferenças de engine e targets multiplataforma"),
    # dbt v2.
    "dbt_data_tests": ("dbt v2 — Add data tests to your DAG", "https://docs.getdbt.com/docs/build/data-tests?version=2", "testes singulares/genéricos, registros violadores e argumentos"),
    "dbt_test_command": ("dbt v2 — About dbt test command", "https://docs.getdbt.com/reference/commands/test?version=2", "seleção de data/unit tests e pré-requisitos de materialização"),
    "dbt_test_config": ("dbt v2 — Data test configurations", "https://docs.getdbt.com/reference/data-test-configs?version=2", "severity, error_if, warn_if, store_failures, limit, where e fail_calc"),
    "dbt_severity": ("dbt — severity, error_if, and warn_if", "https://docs.getdbt.com/reference/resource-configs/severity.md", "ordem de avaliação das condições, diferença entre severity error/warn e promoção por --warn-error"),
    "dbt_limit": ("dbt — limit", "https://docs.getdbt.com/reference/resource-configs/limit.md", "limite de registros de falha retornados pela query e relação com armazenamento"),
    "dbt_fail_calc": ("dbt — fail_calc", "https://docs.getdbt.com/reference/resource-configs/fail_calc.md", "contagem padrão, expressão customizada e tratamento de resultado sem linhas"),
    "dbt_store_failures": ("dbt — store_failures", "https://docs.getdbt.com/reference/resource-configs/store_failures.md", "substituição dos resultados da execução anterior e interação com limit"),
    "dbt_properties": ("dbt v2 — Data test properties", "https://docs.getdbt.com/reference/resource-properties/data-tests?version=2", "sintaxe YAML e propriedades de testes genéricos"),
    "dbt_unit_tests": ("dbt v2 — Unit tests", "https://docs.getdbt.com/docs/build/unit-tests?version=2", "inputs e expected output de models antes da materialização"),
    # Mock Service Worker current API.
    "msw_node": ("MSW — Node.js integration", "https://mswjs.io/guides/integrations/node", "setupServer e ciclo listen/reset/close em testes"),
    "msw_listen": ("MSW — listen()", "https://mswjs.io/api/setup-server/listen", "início da interceptação e estratégias para frames sem handler"),
    "msw_use": ("MSW — use()", "https://mswjs.io/api/setup-server/use", "adição e precedência de runtime handlers"),
    "msw_reset": ("MSW — resetHandlers()", "https://mswjs.io/api/setup-server/reset-handlers", "reset de overrides e substituição da lista inicial"),
    "msw_restore": ("MSW — restoreHandlers()", "https://mswjs.io/api/setup-server/restore-handlers", "rearmar handlers de uso único"),
    "msw_close": ("MSW — close()", "https://mswjs.io/api/setup-server/close", "encerramento síncrono da interceptação Node"),
    "msw_boundary": ("MSW — boundary()", "https://mswjs.io/api/setup-server/boundary", "isolamento de comportamento de rede em escopos assíncronos concorrentes"),
    "msw_handlers": ("MSW — Structuring handlers", "https://mswjs.io/guides/best-practices/structuring-handlers", "handlers de sucesso, overrides e composição por domínio"),
    "msw_http": ("MSW — http", "https://mswjs.io/api/http", "handlers HTTP por método, resolver, parâmetros e opção once"),
    # Node.js v26.10.
    "node_test": ("Node.js v26.10 — Test runner", "https://nodejs.org/api/test.html", "TestContext, isolamento, hooks, mocks, concorrência e reporters"),
    "node_cli": ("Node.js v26.10 — Command-line API", "https://nodejs.org/api/cli.html", "flags de execução, seleção, reporters, cobertura e sharding"),
    "node_mock": ("Node.js v26.10 — Test runner: Mocking", "https://nodejs.org/api/test.html#mocking", "MockTracker e MockTimers ligados ao contexto de teste"),
    "node_hooks": ("Node.js v26.10 — Test runner: TestContext", "https://nodejs.org/api/test.html#class-testcontext", "hooks de cleanup por caso e ciclo de vida de subtestes"),
    # pgTAP.
    "pgtap_docs": ("pgTAP — Documentation", "https://pgtap.org/documentation.html", "assertions TAP, schema, comparações, diretivas e funções de teste"),
    "pgtap_results": ("pgTAP — Result set comparison assertions", "https://pgtap.org/documentation.html#results_eq", "comparadores de resultados ordenados e não ordenados, conjuntos e multiplicidade"),
    "pgtap_prove": ("pgTAP — pg_prove", "https://pgtap.org/pg_prove.html", "execução de scripts SQL e funções xUnit pelo TAP::Harness"),
    "pgtap_compare": ("PostgreSQL — Sorting Rows", "https://www.postgresql.org/docs/current/queries-order.html", "semântica de ORDER BY e ausência de garantia de ordenação sem cláusula explícita"),
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
        if len(parts) == 10:
            slug, title, summary, reason, how, example, caveat, verify, source_keys, review = parts
        elif len(parts) == 9:
            # Compact authoring form: the fourth field carries the rationale
            # and operating detail as two sentences (or clauses separated by a
            # semicolon). Split them into the required separate note sections.
            slug, title, summary, reason_how, example, caveat, verify, source_keys, review = parts
            split = re.split(r"(?<=[.!?])\s+", reason_how, maxsplit=1)
            if len(split) != 2:
                split = reason_how.split("; ", 1)
            if len(split) != 2 or not all(part.strip() for part in split):
                raise ValueError(f"{path.name}: falta separar justificativa e procedimento em: {line}")
            reason, how = split[0].strip(), split[1].strip()
        else:
            raise ValueError(f"{path.name}: esperados 9 ou 10 campos, encontrados {len(parts)}: {line}")
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
    unknown = set(row["sources"]) - SOURCES.keys()
    if unknown:
        raise ValueError(f"{row['slug']}: fontes desconhecidas {unknown}")
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
revisao_ia: pendente
revisor_ia: ""
data_revisao_ia: ""
relatorio_revisao_ia: ""
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
            seen_slugs.add(slug)
            seen_titles.add(normalized_title)
            number, content, quality = render_note(context, rows, index, row)
            pending.append((number, row, context, content, quality))
            source_name, source_url, _ = SOURCES[row["sources"][0]]
            report_rows.append(
                f"| {number} | [[{slug}]] | [{source_name}]({source_url}) | Revisão factual pendente: o gate automatizado não confirma esta afirmação. |"
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

    # All notes and metadata pass deterministic checks before any file is written.
    for number, row, context, content, quality in pending:
        (NOTES_DIR / f"{row['slug']}.md").write_text(content, encoding="utf-8")

    report = [
        "# Revisão factual assistida por IA — lote `software-testes-2000-0001`, tranche 15",
        "",
        f"- Data: {DATE}",
        "- Revisor: `Arena.ai Agent Mode`",
        "- Escopo: notas **850–949**, em dez grupos de dez; cada linha aponta a fonte principal e mantém explícito o estado factual pendente.",
        "- Fontes previstas: documentação oficial dos projetos e versões indicadas nas próprias notas; executar o gate automatizado não confirma as afirmações.",
        "- Resultado: **rascunho de revisão**. O construtor não registra revisão factual nem aprova notas; só a conferência posterior contra as fontes pode fazê-lo.",
        "- Nenhuma aprovação humana existente foi alterada ou estendida às novas notas.",
        "",
        "## Registro por nota",
        "",
        "Todas as 100 linhas começam pendentes. Não interprete aprovação no gate de qualidade como revisão factual.",
        "",
        "| # | Nota | Fonte principal | Estado da revisão factual |",
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
        "- A revisão factual foi assistida por IA e não representa aprovação humana.",
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
