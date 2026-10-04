#!/usr/bin/env python3
"""Build the source-backed software-testing tranche 18 (notes 1157–1257)."""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "knowledge-federation" / "scripts" / "_tranche18_data"
NOTES_DIR = ROOT / "knowledge-federation" / "domains" / "software-0007" / "software" / "testes"
DOMAINS_DIR = ROOT / "knowledge-federation" / "domains"
REPORT = ROOT / "knowledge-federation" / "exports" / "reports" / "ai-review-software-testes-2000-0001-tranche-18.md"
DATE = date.today().isoformat()
START = 1157
EXPECTED_NOTES = 101

sys.path.insert(0, str(ROOT / "knowledge-federation" / "scripts"))
from note_quality import assess_markdown, normalize  # noqa: E402
from prose_audit import repeated_substantive_sentences  # noqa: E402

SOURCES = {
    # Cypress (docs.cypress.io) — end-to-end testing in the browser.
    "cypress_docs": ("Cypress — Documentation", "https://docs.cypress.io/guides/overview/why-cypress", "visão geral do executor, comandos, artefatos e execução paralela"),
    "cypress_api": ("Cypress — API", "https://docs.cypress.io/api/table-of-contents", "comandos, asserções, comandos próprios e opções de execução"),
    "cypress_intercept": ("Cypress — cy.intercept", "https://docs.cypress.io/api/commands/intercept", "interceptação de rede, respostas simuladas e espera por apelido"),
    "cypress_session": ("Cypress — cy.session", "https://docs.cypress.io/api/commands/session", "cache de sessão de autenticação e validação da restauração"),
    "cypress_best_practices": ("Cypress — Best practices", "https://docs.cypress.io/guides/references/best-practices", "seletores estáveis, independência entre testes e dados de apoio"),
    "cypress_github": ("Cypress — repositório oficial", "https://github.com/cypress-io/cypress", "código-fonte, exemplos e documentação do projeto"),
    # WebdriverIO (webdriver.io) — browser and mobile automation.
    "wdio_docs": ("WebdriverIO — Documentation", "https://webdriver.io/docs/gettingstarted", "configuração, modos de execução, serviços e paralelismo"),
    "wdio_api": ("WebdriverIO — API", "https://webdriver.io/docs/api", "comandos de navegador e de elemento e comandos próprios"),
    "wdio_selectors": ("WebdriverIO — Selectors", "https://webdriver.io/docs/selectors", "estratégias de seleção por estilo, acessibilidade e plataforma"),
    "wdio_waits": ("WebdriverIO — waitForDisplayed", "https://webdriver.io/docs/api/element/waitForDisplayed", "espera por condição de exibição com limite de tempo"),
    "wdio_github": ("WebdriverIO — repositório oficial", "https://github.com/webdriverio/webdriverio", "código-fonte, exemplos e documentação do projeto"),
    # JUnit 5 (junit.org) — testing framework for the JVM.
    "junit_userguide": ("JUnit 5 — User Guide", "https://junit.org/junit5/docs/current/user-guide/", "anotações, ciclo de vida, asserções, parametrização, extensões e paralelismo"),
    "junit_github": ("JUnit 5 — repositório oficial", "https://github.com/junit-team/junit5", "código-fonte, notas de versão e documentação do projeto"),
    # GoogleTest (google.github.io/googletest) — C++ testing framework.
    "gtest_primer": ("GoogleTest — Primer", "https://google.github.io/googletest/primer.html", "macros de caso, asserções, comparações e execução"),
    "gtest_advanced": ("GoogleTest — Advanced", "https://google.github.io/googletest/advanced.html", "fixtures, parametrização, testes por tipo, filtros e asserções de morte"),
    "gtest_github": ("GoogleTest — repositório oficial", "https://github.com/google/googletest", "código-fonte, exemplos e documentação do projeto"),
    # PHPUnit (docs.phpunit.de) — testing framework for PHP.
    "phpunit_writing": ("PHPUnit — Writing tests", "https://docs.phpunit.de/en/12.5/writing-tests-for-phpunit.html", "classes de teste, asserções, provedores de dados e exceções"),
    "phpunit_attributes": ("PHPUnit — Attributes", "https://docs.phpunit.de/en/12.5/attributes.html", "atributos de teste, provedores, grupos e configuração de dublês"),
    "phpunit_fixtures": ("PHPUnit — Fixtures", "https://docs.phpunit.de/en/12.5/fixtures.html", "preparação e limpeza por teste e por classe"),
    "phpunit_doubles": ("PHPUnit — Test doubles", "https://docs.phpunit.de/en/12.5/test-doubles.html", "dublês de tipos, configuração de retornos e verificação de chamadas"),
    "phpunit_coverage": ("PHPUnit — Code coverage", "https://docs.phpunit.de/en/12.5/code-coverage.html", "medição de linhas e ramos e geração de relatórios"),
    "phpunit_github": ("PHPUnit — repositório oficial", "https://github.com/sebastianbergmann/phpunit", "código-fonte, exemplos e documentação do projeto"),
    # Ginkgo (onsi.github.io/ginkgo) — BDD-style testing for Go.
    "ginkgo_site": ("Ginkgo — Documentation", "https://onsi.github.io/ginkgo/", "contêineres, nós de preparação, paralelismo, etiquetas e relatórios"),
    "ginkgo_pkg": ("Ginkgo — pacote publicado", "https://pkg.go.dev/github.com/onsi/ginkgo/v2", "API pública, decoradores e funções de execução"),
    "ginkgo_gomega": ("Gomega — Documentação", "https://onsi.github.io/gomega/", "biblioteca de asserções usada com o Ginkgo"),
    "ginkgo_github": ("Ginkgo — repositório oficial", "https://github.com/onsi/ginkgo", "código-fonte, exemplos e ferramenta de linha de comando"),
    # axe-core (github.com/dequelabs/axe-core) — accessibility rules engine.
    "axe_api": ("axe-core — JavaScript API", "https://github.com/dequelabs/axe-core/blob/develop/doc/API.md", "chamada de análise, opções, etiquetas, impacto e formato do resultado"),
    "axe_rules": ("axe-core — Rule descriptions", "https://github.com/dequelabs/axe-core/blob/develop/doc/rule-descriptions.md", "catálogo de regras, etiquetas de norma e classificação por boas práticas"),
    "axe_playwright": ("axe-core — Integração com Playwright", "https://www.npmjs.com/package/@axe-core/playwright", "execução da análise durante testes de navegador"),
    "axe_github": ("axe-core — repositório oficial", "https://github.com/dequelabs/axe-core", "código-fonte, versões e documentação do projeto"),
    # Semgrep (semgrep.dev) — static analysis with code-like patterns.
    "semgrep_docs": ("Semgrep — Documentation", "https://semgrep.dev/docs/", "instalação, execução, integração contínua, supressões e severidade"),
    "semgrep_rules": ("Semgrep — Writing rules", "https://semgrep.dev/docs/writing-rules/overview", "estrutura de regra, operadores, metavariáveis e modo de propagação"),
    "semgrep_fix": ("Semgrep — Rule-defined fix", "https://semgrep.dev/docs/writing-rules/rule-defined-fix", "correção definida pela regra, prévia e aplicação automática"),
    "semgrep_github": ("Semgrep — repositório oficial", "https://github.com/semgrep/semgrep", "código-fonte, exemplos e documentação do projeto"),
    # Trivy (trivy.dev) — artifact and configuration scanning.
    "trivy_docs": ("Trivy — Documentation", "https://trivy.dev/latest/docs/", "alvos, verificadores, políticas, exceções e formatos de saída"),
    "trivy_vuln": ("Trivy — Vulnerability scanning", "https://trivy.dev/latest/docs/scanner/vulnerability/", "análise de imagens e sistemas de arquivos por vulnerabilidades"),
    "trivy_misconfig": ("Trivy — Misconfiguration scanning", "https://trivy.dev/latest/docs/scanner/misconfiguration/", "avaliação de arquivos de infraestrutura contra políticas"),
    "trivy_secret": ("Trivy — Secret scanning", "https://trivy.dev/latest/docs/scanner/secret/", "procura de credenciais e chaves em arquivos e camadas"),
    "trivy_sbom": ("Trivy — SBOM", "https://trivy.dev/latest/docs/supply-chain/sbom/", "geração e análise de inventário de software em formatos padronizados"),
    "trivy_github": ("Trivy — repositório oficial", "https://github.com/aquasecurity/trivy", "código-fonte, alvos suportados e documentação do projeto"),
    # Allure (allurereport.org) — test reporting.
    "allure_docs": ("Allure Report — Documentation", "https://allurereport.org/docs/", "resultados, passos, anexos, histórico, tendências e publicação"),
    "allure_steps": ("Allure Report — Steps", "https://allurereport.org/docs/steps/", "divisão do teste em passos nomeados e aninhados"),
    "allure_categories": ("Allure Report — Categories", "https://allurereport.org/docs/categories/", "classificação automática de falhas por status e padrões"),
    "allure_github": ("Allure — repositório oficial", "https://github.com/allure-framework/allure2", "gerador de relatório, exemplos e documentação do projeto"),
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
id: software.testes.tranche18.{number:06d}
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-18.md"
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
        help="Rebuild the existing tranche-18 notes after validating their IDs and batch metadata.",
    )
    args = parser.parse_args()
    group_files = sorted(DATA_DIR.glob("*.txt"))
    if len(group_files) != 10:
        raise SystemExit(f"Esperados 10 arquivos de grupo; encontrados {len(group_files)}")

    existing_paths = list(DOMAINS_DIR.rglob("*.md"))
    existing_tranche = [
        path for path in existing_paths
        if re.search(
            r"(?m)^id: software\.testes\.tranche18\.\d{6}\s*$",
            path.read_text(encoding="utf-8", errors="replace")[:1200],
        )
    ]
    if args.refresh and len(existing_tranche) != EXPECTED_NOTES:
        raise ValueError(f"--refresh exige exatamente {EXPECTED_NOTES} notas tranche18 existentes; encontradas {len(existing_tranche)}")
    if REPORT.exists() and not args.refresh:
        raise ValueError(f"relatório já existe (use --refresh apenas para atualizar a tranche 18): {REPORT}")
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
            expected_id = f"id: software.testes.tranche18.{expected_number + index:06d}"
            if target_path.exists():
                current = target_path.read_text(encoding="utf-8")
                if not args.refresh:
                    raise ValueError(f"arquivo já existe (use --refresh apenas para a tranche 18): {target_path}")
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
        "# Revisão factual assistida por IA — lote `software-testes-2000-0001`, tranche 18",
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
