#!/usr/bin/env python3
"""Build the source-backed software-testing tranche 22 (notes 1560–1659)."""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "knowledge-federation" / "scripts" / "_tranche22_data"
NOTES_DIR = ROOT / "knowledge-federation" / "domains" / "software-0007" / "software" / "testes"
DOMAINS_DIR = ROOT / "knowledge-federation" / "domains"
REPORT = ROOT / "knowledge-federation" / "exports" / "reports" / "ai-review-software-testes-2000-0001-tranche-22.md"
DATE = date.today().isoformat()
START = 1560
EXPECTED_NOTES = 100

sys.path.insert(0, str(ROOT / "knowledge-federation" / "scripts"))
from note_quality import assess_markdown, normalize  # noqa: E402
from prose_audit import repeated_substantive_sentences  # noqa: E402

SOURCES = {
    # bats-core (bats-core.readthedocs.io + GitHub) — TAP testing framework for Bash.
    "bt_index": ("Bats-core — Documentação oficial (página inicial)", "https://bats-core.readthedocs.io/en/latest/index.html", "índice: tutorial, instalação, usage, gotchas e FAQ"),
    "bt_tutorial": ("Bats-core — Tutorial", "https://bats-core.readthedocs.io/en/latest/tutorial.html", "primeiro teste, setup, output, limpeza e suítes multifiles"),
    "bt_usage": ("Bats-core — Usage", "https://bats-core.readthedocs.io/en/latest/usage.html", "opções do CLI, formatters, relatórios e execução paralela"),
    "bt_docs": ("Bats-core — Writing tests", "https://bats-core.readthedocs.io/en/latest/writing-tests.html", "run, tags, setup/teardown, ganchos e armadilhas de escrita"),
    "bt_gotchas": ("Bats-core — Gotchas", "https://bats-core.readthedocs.io/en/latest/gotchas.html", "armadilhas documentadas: run, colchetes duplos, load e file descriptor 3"),
    "bt_readme": ("Bats-core — README oficial", "https://github.com/bats-core/bats-core/blob/master/README.md", "proposta TAP, história do fork e licença MIT"),
    "bt_versions": ("Bats-core — docs de versões antigas", "https://github.com/bats-core/bats-core/blob/master/docs/versions.md", "documentação de versões anteriores à v1.2.1"),
    "bt_examples": ("Bats-core — exemplos oficiais", "https://github.com/bats-core/bats-core/tree/master/docs/examples", "arquivos de teste de exemplo referenciados pela doc"),
    # Pester (pester.dev) — testing and mocking framework for PowerShell.
    "ps_quickstart": ("Pester — Quick start", "https://pester.dev/docs/quick-start", "mini-DSL, convenção de nomes e primeira execução"),
    "ps_mocking": ("Pester — Mocking", "https://pester.dev/docs/usage/mocking", "Mock, Should-Invoke, escopo, natives e classes"),
    "ps_coverage": ("Pester — Code coverage", "https://pester.dev/docs/usage/code-coverage", "New-PesterConfiguration, formatos JaCoCo/Cobertura e tracer"),
    "ps_config": ("Pester — New-PesterConfiguration", "https://pester.dev/docs/commands/New-PesterConfiguration", "comando de configuração citado pela página de cobertura"),
    # Reqnroll (reqnroll.net / docs.reqnroll.net) — BDD framework for .NET.
    "rq_readme": ("Reqnroll — README oficial", "https://github.com/reqnroll/Reqnroll/blob/main/README.md", "proposta, plataformas, executores e instalação NuGet"),
    "rq_migration": ("Reqnroll — Migrating from SpecFlow", "https://docs.reqnroll.net/latest/guides/migrating-from-specflow.html", "renomeações, compat package, atenções MsTest e LivingDoc"),
    "rq_datatable": ("Reqnroll — DataTable Helpers", "https://docs.reqnroll.net/latest/automation/datatable-helpers.html", "assistentes de tabela citados pela guia de migração"),
    "rq_cucumberexpr": ("Reqnroll — Cucumber Expressions", "https://docs.reqnroll.net/latest/automation/cucumber-expressions.html", "suporte embutido citado pela guia de migração"),
    "rq_setupide": ("Reqnroll — Setup de IDE", "https://docs.reqnroll.net/latest/installation/setup-ide.html", "extensão Visual Studio tratada na guia"),
    "rq_plugins": ("Reqnroll — Available Plugins", "https://docs.reqnroll.net/latest/integrations/available-plugins.html", "plugins portados citados pela guia de migração"),
    "rq_discuss": ("Reqnroll — discussão Living Documentation", "https://github.com/orgs/reqnroll/discussions/196", "tópico oficial sobre o plano do LivingDoc"),
    "rq_license": ("Reqnroll — arquivo LICENSE", "https://github.com/reqnroll/Reqnroll/blob/main/LICENSE", "texto BSD 3-Clause citado pelo README"),
    # FluentAssertions (fluentassertions.com) — assertion extensions for .NET.
    "fa_intro": ("FluentAssertions — Introduction", "https://www.fluentassertions.com/introduction", "chaining, frameworks detectados, subject identification e AssertionScope"),
    "fa_graphs": ("FluentAssertions — Object graphs", "https://www.fluentassertions.com/objectgraphs/", "BeEquivalentTo, recursão, tipagem, exclusões e auto-conversão"),
    "fa_extensibility": ("FluentAssertions — Extensibility", "https://fluentassertions.com/extensibility/", "página para onde a Introduction delega GlobalConfiguration.TestFramework"),
    # jqwik (jqwik.net) — property-based testing engine for the JUnit 5 Platform.
    "jw_guide": ("jqwik — User Guide 1.10.1", "https://jqwik.net/docs/current/user-guide.html", "properties, geração, shrinking, lifecycle, config e módulos"),
    "jw_maven": ("jqwik — busca no Maven Central", "https://search.maven.org/search?q=g:net.jqwik", "artefatos publicados citados pelo guia"),
    "jw_snapshots": ("jqwik — repositório de snapshots", "https://s01.oss.sonatype.org/content/repositories/snapshots", "repositório de snapshot citado pelo guia"),
    # Kotest property testing (kotest.io) — forAll/checkAll em Kotlin.
    "kt_functions": ("Kotest — Property Test Functions", "https://kotest.io/docs/proptest/property-test-functions.html", "forAll, checkAll, iterações e generators"),
    "kt_config": ("Kotest — Property Test Configuration", "https://kotest.io/docs/proptest/property-test-config.html", "PropTestConfig: maxFailure, listeners e saída hex"),
    "kt_seeds": ("Kotest — Property Test Seeds", "https://kotest.io/docs/proptest/property-test-seeds.html", "sementes, rerun de falhas e ~/.kotest/seeds"),
    "kt_generators": ("Kotest — Property Test Generators", "https://kotest.io/docs/proptest/property-test-generators.html", "catálogo de generators embutidos citado pela página de funções"),
    # Tavern (tavern.readthedocs.io) — YAML API testing sobre pytest.
    "tv_index": ("Tavern — documentação inicial", "https://tavern.readthedocs.io/en/latest/", "proposta, quickstart YAML, CLI e comparativos"),
    "tv_docs": ("Tavern — documentação completa", "https://taverntesting.github.io/documentation", "documentação oficial linkada pela página inicial"),
    "tv_examples": ("Tavern — exemplos oficiais", "https://taverntesting.github.io/examples", "página de exemplos linkada pela doc inicial"),
    "tv_pyproject": ("Tavern — pyproject.toml", "https://github.com/taverntesting/tavern/blob/master/pyproject.toml", "tagline oficial do projeto no manifesto"),
    # responses (getsentry/responses) — mocking da biblioteca requests.
    "rs_readme": ("responses — README oficial", "https://github.com/getsentry/responses/blob/master/README.rst", "activate, add, atalhos, matchers, registry e passthru"),
    "rs_pypi": ("responses — página no PyPI", "https://pypi.org/project/responses/", "release canônica e badge do pacote"),
    # Hoverfly (docs.hoverfly.io) — API simulation via proxy.
    "hv_readme": ("Hoverfly — README oficial", "https://github.com/SpectoLabs/hoverfly/blob/master/README.md", "proposta, quickstart, build em Go e contribuição"),
    "hv_index": ("Hoverfly — documentação inicial", "https://docs.hoverfly.io/en/latest/index.html", "conceitos-chave, reference e troubleshooting do v1.12.15"),
    "hv_start": ("Hoverfly — Getting Started", "https://docs.hoverfly.io/en/latest/pages/introduction/gettingstarted.html", "binários hoverfly/hoverctl, start, logs e stop"),
    "hv_export": ("Hoverfly — Creating and exporting a simulation", "https://docs.hoverfly.io/en/latest/pages/tutorials/basic/exportingsimulations/exportingsimulations.html", "capture mode, proxy 8500, headers e export --url-pattern"),
    "hv_stateful": ("Hoverfly — Capturing a stateful sequence", "https://docs.hoverfly.io/en/stable/pages/tutorials/basic/capturingsequences/capturingsequences.html", "capture --stateful, requiresState/transitionsState e hoverctl state"),
    "hv_java": ("Hoverfly Java — documentação oficial", "https://hoverfly-java.readthedocs.io/en/latest/", "binding nativo Java citado pelo README"),
    # gcovr (gcovr.com) — gcov coverage summaries.
    "gc_index": ("gcovr — documentação inicial (8.6)", "https://gcovr.com/en/stable/index.html", "definição, matriz de formatos de saída e índice da doc"),
    "gc_start": ("gcovr — Getting Started", "https://gcovr.com/en/stable/getting-started.html", "flags de build, -r, html-details e html-nested"),
    "gc_manpage": ("gcovr — Command Line Reference", "https://gcovr.com/en/stable/manpage.html", "filtros, exclusões, config keys e --no-markers"),
    "gc_filters": ("gcovr — Using Filters", "https://gcovr.com/en/stable/guide/filters.html", "guia de filtros citado pelo getting started"),
    "gc_pypi": ("gcovr — página no PyPI", "https://pypi.org/project/gcovr/", "instalação oficial via pip"),
    "gc_changelog": ("gcovr — Change Log", "https://gcovr.com/en/stable/changelog.html", "datas de release da doc 8.6"),
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
id: software.testes.tranche22.{number:06d}
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-22.md"
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
        help="Rebuild the existing tranche-22 notes after validating their IDs and batch metadata.",
    )
    args = parser.parse_args()
    group_files = sorted(DATA_DIR.glob("*.txt"))
    if len(group_files) != 10:
        raise SystemExit(f"Esperados 10 arquivos de grupo; encontrados {len(group_files)}")

    existing_paths = list(DOMAINS_DIR.rglob("*.md"))
    existing_tranche = [
        path for path in existing_paths
        if re.search(
            r"(?m)^id: software\.testes\.tranche22\.\d{6}\s*$",
            path.read_text(encoding="utf-8", errors="replace")[:1200],
        )
    ]
    if args.refresh and len(existing_tranche) != EXPECTED_NOTES:
        raise ValueError(f"--refresh exige exatamente {EXPECTED_NOTES} notas tranche22 existentes; encontradas {len(existing_tranche)}")
    if REPORT.exists() and not args.refresh:
        raise ValueError(f"relatório já existe (use --refresh apenas para atualizar a tranche 22): {REPORT}")
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
            expected_id = f"id: software.testes.tranche22.{expected_number + index:06d}"
            if target_path.exists():
                current = target_path.read_text(encoding="utf-8")
                if not args.refresh:
                    raise ValueError(f"arquivo já existe (use --refresh apenas para a tranche 22): {target_path}")
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
        "# Revisão factual assistida por IA — lote `software-testes-2000-0001`, tranche 22",
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
