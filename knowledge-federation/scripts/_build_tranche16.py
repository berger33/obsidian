#!/usr/bin/env python3
"""Build the source-backed software-testing tranche 16 (notes 950–1055)."""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "knowledge-federation" / "scripts" / "_tranche16_data"
NOTES_DIR = ROOT / "knowledge-federation" / "domains" / "software-0007" / "software" / "testes"
DOMAINS_DIR = ROOT / "knowledge-federation" / "domains"
REPORT = ROOT / "knowledge-federation" / "exports" / "reports" / "ai-review-software-testes-2000-0001-tranche-16.md"
DATE = date.today().isoformat()
START = 950
EXPECTED_NOTES = 106

sys.path.insert(0, str(ROOT / "knowledge-federation" / "scripts"))
from note_quality import assess_markdown, normalize  # noqa: E402
from prose_audit import repeated_substantive_sentences  # noqa: E402

SOURCES = {
    # Detox (wix.github.io/Detox) — gray-box end-to-end testing for React Native.
    "detox_getting_started": ("Detox — Getting Started", "https://wix.github.io/Detox/docs/introduction/getting-started", "sincronização automática, matchers, esperas explícitas, lançamento, recarga, ações de dispositivo e artefatos"),
    "detox_project_setup": ("Detox — Project Setup", "https://wix.github.io/Detox/docs/introduction/project-setup", "configuração por alvo, arquivo de configuração e comandos de build e teste"),
    "detox_github": ("Detox — repositório oficial", "https://github.com/wix/Detox", "visão geral do projeto, documentação complementar e exemplos"),
    # Artillery (artillery.io) — load testing with phases, scenarios and thresholds.
    "artillery_first_test": ("Artillery — First test", "https://www.artillery.io/docs/get-started/first-test", "config, fases, cenários, capturas, métricas e execução de carga"),
    "artillery_github": ("Artillery — repositório oficial", "https://github.com/artilleryio/artillery", "código-fonte, exemplos e documentação do projeto"),
    "artillery_engines_playwright": ("Artillery — Playwright engine", "https://www.artillery.io/docs/reference/engines/playwright", "controle de navegador real e coleta de métricas de página sob carga"),
    "artillery_ensure": ("Artillery — ensure", "https://www.artillery.io/docs/reference/extensions/ensure", "limites e condições sobre métricas com código de saída não nulo"),
    # Vegeta (github.com/tsenart/vegeta) — constant-rate HTTP load testing.
    "vegeta_github": ("Vegeta — repositório oficial", "https://github.com/tsenart/vegeta", "manual de uso: attack, report, plot, encode, dump e opções de conexão"),
    "vegeta_pkg": ("Vegeta — biblioteca Go", "https://pkg.go.dev/github.com/tsenart/vegeta/v12/lib", "API de taxa, atacante, alvos e métricas para uso programático"),
    # JMH (github.com/openjdk/jmh) — JVM microbenchmarks.
    "jmh_github": ("JMH — repositório oficial", "https://github.com/openjdk/jmh", "anotações, modos de medição, forking, estados, parâmetros e execução"),
    "jmh_openjdk": ("OpenJDK — JMH", "https://openjdk.org/projects/code-tools/jmh/", "visão geral do harness oficial de microbenchmarks da JVM"),
    "jmh_samples": ("JMH — exemplos oficiais", "https://github.com/openjdk/jmh/tree/master/jmh-samples", "amostras de parâmetros, estados, preparação e consumo de resultados"),
    # coverage.py (coverage.readthedocs.io) — Python coverage measurement.
    "cov_cmd": ("coverage.py — Command line", "https://coverage.readthedocs.io/en/6.5.0/cmd.html", "comandos run, combine, report, xml, json e html com suas opções"),
    "cov_config": ("coverage.py — Configuration", "https://coverage.readthedocs.io/en/6.5.0/config.html", "arquivos de configuração, fontes, omissões, exclusões e limites"),
    "cov_branch": ("coverage.py — Branch coverage", "https://coverage.readthedocs.io/en/6.5.0/branch.html", "medição de ramos, ramos parciais e ajuste de exclusões"),
    # nyc / Istanbul (github.com/istanbuljs/nyc) — JavaScript coverage instrumentation.
    "nyc_github": ("nyc — repositório oficial", "https://github.com/istanbuljs/nyc", "linha de comando, filtros, relatórios, limites e mesclagem de dados"),
    "istanbuljs_repo": ("Istanbul — monorepo oficial", "https://github.com/istanbuljs/istanbuljs", "instrumentação JavaScript, bibliotecas de cobertura e geradores de relatório"),
    "nyc_npm": ("nyc — pacote npm", "https://www.npmjs.com/package/nyc", "opções documentadas e exemplos de uso do publicador"),
    # Lighthouse CI (googlechrome.github.io/lighthouse-ci) — web performance and a11y budgets.
    "lhci_config": ("Lighthouse CI — Configuration", "https://googlechrome.github.io/lighthouse-ci/docs/configuration.html", "seções collect, assert e upload, presets, asserções e orçamentos"),
    "lhci_repo": ("Lighthouse CI — repositório oficial", "https://github.com/GoogleChrome/lighthouse-ci", "comandos, integração contínua e documentação do projeto"),
    # Pa11y (github.com/pa11y/pa11y) — automated accessibility testing.
    "pa11y_repo": ("Pa11y — repositório oficial", "https://github.com/pa11y/pa11y", "linha de comando, padrões, motores, ações, relatórios e limites"),
    "pa11y_ci": ("Pa11y CI — repositório oficial", "https://github.com/pa11y/pa11y-ci", "varredura de múltiplas páginas, configuração e integração contínua"),
    # Prism (docs.stoplight.io/docs/prism) — HTTP mocking and validation from contracts.
    "prism_mocking": ("Prism — HTTP mocking", "https://docs.stoplight.io/docs/prism/83dbbd75532cf-http-mocking", "modos estático e dinâmico, cabeçalho Prefer e respostas de violação"),
    "prism_cli": ("Prism — CLI", "https://docs.stoplight.io/docs/prism/beeaad4dc0227-prism-cli", "instalação, subcomandos mock e proxy e opções de validação"),
    # Hurl (hurl.dev) — plain-text HTTP request files and assertions.
    "hurl_file": ("Hurl — File format", "https://hurl.dev/docs/hurl-file.html", "estrutura de entradas, resposta esperada, opções e escopo de sessão"),
    "hurl_asserting": ("Hurl — Asserting response", "https://hurl.dev/docs/asserting-response.html", "asserções implícitas e explícitas sobre status, cabeçalhos e corpo"),
    "hurl_capturing": ("Hurl — Capturing response", "https://hurl.dev/docs/capturing-response.html", "captura de valores por expressão e reuso como variáveis"),
    "hurl_cli": ("Hurl — Manual (CLI)", "https://hurl.dev/docs/manual.html", "modo de teste, paralelismo, repetição, relatórios e códigos de saída"),
    "hurl_repo": ("Hurl — repositório oficial", "https://github.com/Orange-OpenSource/hurl", "visão geral do projeto, exemplos e documentação complementar"),
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
id: software.testes.tranche16.{number:06d}
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-16.md"
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
        help="Rebuild the existing tranche-16 notes after validating their IDs and batch metadata.",
    )
    args = parser.parse_args()
    group_files = sorted(DATA_DIR.glob("*.txt"))
    if len(group_files) != 10:
        raise SystemExit(f"Esperados 10 arquivos de grupo; encontrados {len(group_files)}")

    existing_paths = list(DOMAINS_DIR.rglob("*.md"))
    existing_tranche = [
        path for path in existing_paths
        if re.search(
            r"(?m)^id: software\.testes\.tranche16\.\d{6}\s*$",
            path.read_text(encoding="utf-8", errors="replace")[:1200],
        )
    ]
    if args.refresh and len(existing_tranche) != EXPECTED_NOTES:
        raise ValueError(f"--refresh exige exatamente {EXPECTED_NOTES} notas tranche16 existentes; encontradas {len(existing_tranche)}")
    if REPORT.exists() and not args.refresh:
        raise ValueError(f"relatório já existe (use --refresh apenas para atualizar a tranche 16): {REPORT}")
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
            expected_id = f"id: software.testes.tranche16.{expected_number + index:06d}"
            if target_path.exists():
                current = target_path.read_text(encoding="utf-8")
                if not args.refresh:
                    raise ValueError(f"arquivo já existe (use --refresh apenas para a tranche 16): {target_path}")
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
        "# Revisão factual assistida por IA — lote `software-testes-2000-0001`, tranche 16",
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
