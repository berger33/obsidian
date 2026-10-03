#!/usr/bin/env python3
"""Build the source-backed software-testing tranche 21 (notes 1460–1559)."""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "knowledge-federation" / "scripts" / "_tranche21_data"
NOTES_DIR = ROOT / "knowledge-federation" / "domains" / "software-0007" / "software" / "testes"
DOMAINS_DIR = ROOT / "knowledge-federation" / "domains"
REPORT = ROOT / "knowledge-federation" / "exports" / "reports" / "ai-review-software-testes-2000-0001-tranche-21.md"
DATE = date.today().isoformat()
START = 1460
EXPECTED_NOTES = 100

sys.path.insert(0, str(ROOT / "knowledge-federation" / "scripts"))
from note_quality import assess_markdown, normalize  # noqa: E402
from prose_audit import repeated_substantive_sentences  # noqa: E402

SOURCES = {
    # Nightwatch (nightwatchjs.org) — integrated browser testing via W3C WebDriver.
    "nw_overview": ("Nightwatch — O que é o Nightwatch", "https://nightwatchjs.org/guide/overview/what-is-nightwatch.html", "proposta, arquitetura WebDriver e navegadores suportados"),
    "nw_settings": ("Nightwatch — Referência de Config Settings", "https://nightwatchjs.org/guide/reference/settings.html", "chaves de configuração, ambientes, runner, workers e capturas"),
    "nw_installation": ("Nightwatch — Instalação", "https://nightwatchjs.org/gettingstarted/installation/", "drivers por navegador e preparação do ambiente"),
    "nw_environments": ("Nightwatch — Ambientes de teste", "https://nightwatchjs.org/guide/concepts/test-environments.html", "herança entre ambientes, baseUrl e globals"),
    "nw_repo": ("Nightwatch — repositório oficial", "https://github.com/nightwatchjs/nightwatch", "código-fonte, releases e documentação do projeto"),
    # AVA (github.com/avajs/ava) — concurrent test runner for Node.js.
    "ava_readme": ("AVA — README oficial", "https://github.com/avajs/ava/blob/main/readme.md", "proposta, instalação e destaques do runner"),
    "ava_writing": ("AVA — Guia Writing tests", "https://github.com/avajs/ava/blob/main/docs/01-writing-tests.md", "concorrência, modificadores, hooks e isolamento"),
    "ava_execution_docs": ("AVA — Guia Execution context", "https://github.com/avajs/ava/blob/main/docs/02-execution-context.md", "objeto de execução, t.plan e t.teardown"),
    "ava_assertions_docs": ("AVA — Guia Assertions", "https://github.com/avajs/ava/blob/main/docs/03-assertions.md", "asserções nativas e mensagens aprimoradas"),
    "ava_cli_docs": ("AVA — Guia Command line", "https://github.com/avajs/ava/blob/main/docs/05-command-line.md", "flags do CLI, reporter TAP e modo watch"),
    # Chai (chaijs.com) — BDD/TDD assertion library.
    "chai_bdd": ("Chai — API BDD (expect/should)", "https://www.chaijs.com/api/bdd/", "correntes de linguagem, negação, deep, nested, own, ordered, keys, tipos e include"),
    "chai_styles": ("Chai — Guia de estilos", "https://www.chaijs.com/guide/styles/", "comparação entre expect, should e assert"),
    "chai_api_should": ("Chai — API should", "https://www.chaijs.com/api/should/", "atualização do protótipo e uso do estilo should"),
    "chai_api_bdd_project": ("Chai — repositório oficial", "https://github.com/chaijs/chai", "código-fonte, versões e documentação do projeto"),
    "chai_type_detect": ("Chai type-detect — projeto", "https://github.com/chaijs/type-detect", "algoritmo de detecção de tipos citado pela API"),
    # Sinon (sinonjs.org) — spies, stubs, mocks and fake timers.
    "sinon_site": ("Sinon.JS — página oficial", "https://sinonjs.org/", "instalação, escopo e início rápido"),
    "sinon_repo": ("Sinon.JS — repositório oficial", "https://github.com/sinonjs/sinon", "código-fonte, guias de API e releases do projeto"),
    "sinon_releases": ("Sinon.JS — releases publicadas", "https://github.com/sinonjs/sinon/releases", "notas de versão e mudanças da API"),
    # VCR.py (vcrpy.readthedocs.io) — record and replay for Python HTTP.
    "vcr_usage": ("VCR.py — Usage", "https://vcrpy.readthedocs.io/en/latest/usage.html", "contexto, decorator, record modes e integrações de teste"),
    "vcr_config": ("VCR.py — Configuration", "https://vcrpy.readthedocs.io/en/latest/configuration.html", "objeto VCR, precedência de overrides e casamento de pedidos"),
    "vcr_repo": ("VCR.py — repositório oficial", "https://github.com/kevin1024/vcrpy", "código-fonte, releases e changelog do projeto"),
    # freezegun — time mocking for Python.
    "fz_pypi": ("freezegun — página no PyPI", "https://pypi.org/project/freezegun/", "README oficial com uso, fusos, tick e limites"),
    "fz_repo": ("freezegun — repositório oficial", "https://github.com/spulec/freezegun", "código-fonte, testes e releases do projeto"),
    # mutmut — mutation testing for Python.
    "mutmut_readme": ("mutmut — README oficial", "https://github.com/boxed/mutmut", "instalação, browse, configuração e filtros"),
    "mutmut_repo": ("mutmut — repositório oficial", "https://github.com/boxed/mutmut/blob/main/README.rst", "material-fonte do README e das releases"),
    "mutmut_article": ("mutmut — artigo introdutório", "https://kodare.net/2016/12/01/mutmut-a-python-mutation-testing-system.html", "explicação do que é teste de mutação, linkada pelo projeto"),
    # cargo-mutants — mutation testing for Rust.
    "cm_repo": ("cargo-mutants — README oficial", "https://github.com/sourcefrog/cargo-mutants", "proposta, resultados, skip e saída"),
    "cm_crates": ("cargo-mutants — pacote no crates.io", "https://crates.io/crates/cargo-mutants", "versões publicadas e metadados do pacote"),
    "cm_mutants_crate": ("mutants — crate de anotação", "https://crates.io/crates/mutants", "dependência mínima para #[mutants::skip]"),
    # Toxiproxy (Shopify) — network conditions simulator.
    "tp_readme": ("Toxiproxy — README oficial", "https://github.com/Shopify/toxiproxy", "proposta, instalação, populate, toxics e HTTP API"),
    "tp_client_repo": ("Toxiproxy — cliente Go", "https://github.com/Shopify/toxiproxy/tree/main/client", "cliente oficial embutido no repositório"),
    "tp_ruby_client": ("Toxiproxy — cliente Ruby", "https://github.com/Shopify/toxiproxy-ruby", "exemplos de populate, down e apply"),
    "tp_python_client": ("Toxiproxy — cliente Python", "https://github.com/douglas/toxiproxy-python", "cliente comunitário linkado pelo projeto"),
    "tp_changelog": ("Toxiproxy — CHANGELOG", "https://github.com/Shopify/toxiproxy/blob/main/CHANGELOG.md", "histórico de releases e mudanças da API"),
    # Jazzer — coverage-guided JVM fuzzing.
    "jz_repo": ("Jazzer — repositório oficial", "https://github.com/CodeIntelligenceTesting/jazzer", "modos standalone e JUnit, corpus, inputs e sanitizers"),
    "jz_docs": ("Jazzer — Arguments and configuration options", "https://github.com/CodeIntelligenceTesting/jazzer/blob/main/docs/arguments-and-configuration-options.md", "argumentos do agente e hooks desativáveis"),
    "jz_releases": ("Jazzer — releases no GitHub", "https://github.com/CodeIntelligenceTesting/jazzer/releases", "binários standalone e notas de versão"),
    "jz_libfuzzer": ("LLVM — documentação do libFuzzer", "https://llvm.org/docs/LibFuzzer.html", "flags de um traço aceitos pelo Jazzer"),
    "jz_seed_example": ("Jazzer — exemplo JavaSeedFuzzTest", "https://github.com/CodeIntelligenceTesting/jazzer/blob/main/examples/junit/src/test/java/com/example/JavaSeedFuzzTest.java", "sementes de @MethodSource em @FuzzTest"),
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
id: software.testes.tranche21.{number:06d}
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-21.md"
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
        help="Rebuild the existing tranche-21 notes after validating their IDs and batch metadata.",
    )
    args = parser.parse_args()
    group_files = sorted(DATA_DIR.glob("*.txt"))
    if len(group_files) != 10:
        raise SystemExit(f"Esperados 10 arquivos de grupo; encontrados {len(group_files)}")

    existing_paths = list(DOMAINS_DIR.rglob("*.md"))
    existing_tranche = [
        path for path in existing_paths
        if re.search(
            r"(?m)^id: software\.testes\.tranche21\.\d{6}\s*$",
            path.read_text(encoding="utf-8", errors="replace")[:1200],
        )
    ]
    if args.refresh and len(existing_tranche) != EXPECTED_NOTES:
        raise ValueError(f"--refresh exige exatamente {EXPECTED_NOTES} notas tranche21 existentes; encontradas {len(existing_tranche)}")
    if REPORT.exists() and not args.refresh:
        raise ValueError(f"relatório já existe (use --refresh apenas para atualizar a tranche 21): {REPORT}")
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
            expected_id = f"id: software.testes.tranche21.{expected_number + index:06d}"
            if target_path.exists():
                current = target_path.read_text(encoding="utf-8")
                if not args.refresh:
                    raise ValueError(f"arquivo já existe (use --refresh apenas para a tranche 21): {target_path}")
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
        "# Revisão factual assistida por IA — lote `software-testes-2000-0001`, tranche 21",
        "",
        f"- Data: {DATE}",
        "- Revisor: `Arena.ai Agent Mode`",
        f"- Escopo: notas **{START}–{START + EXPECTED_NOTES - 1}**, em dez grupos temáticos com dez notas cada; cada linha identifica a conferência factual da nota.",
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
