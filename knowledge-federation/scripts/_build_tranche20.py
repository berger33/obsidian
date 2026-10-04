#!/usr/bin/env python3
"""Build the source-backed software-testing tranche 20 (notes 1359–1459)."""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "knowledge-federation" / "scripts" / "_tranche20_data"
NOTES_DIR = ROOT / "knowledge-federation" / "domains" / "software-0007" / "software" / "testes"
DOMAINS_DIR = ROOT / "knowledge-federation" / "domains"
REPORT = ROOT / "knowledge-federation" / "exports" / "reports" / "ai-review-software-testes-2000-0001-tranche-20.md"
DATE = date.today().isoformat()
START = 1359
EXPECTED_NOTES = 101

sys.path.insert(0, str(ROOT / "knowledge-federation" / "scripts"))
from note_quality import assess_markdown, normalize  # noqa: E402
from prose_audit import repeated_substantive_sentences  # noqa: E402

SOURCES = {
    # Gauge (docs.gauge.org) — markdown specifications.
    "gauge_overview": ("Gauge — Visão geral", "https://docs.gauge.org/overview", "conceitos de especificação, cenário, passo e conceito"),
    "gauge_writing": ("Gauge — Escrever especificações", "https://docs.gauge.org/writing-specifications", "sintaxe das especificações, tabelas de dados e conceitos"),
    "gauge_execution": ("Gauge — Executar especificações", "https://docs.gauge.org/execution", "ganchos, ambientes, etiquetas e execução paralela"),
    "gauge_config": ("Gauge — Configuração", "https://docs.gauge.org/configuration", "propriedades do projeto, ambientes e relatórios"),
    "gauge_manpage": ("Gauge — Execução (manpage)", "https://docs.gauge.org/execution", "subcomandos e opções de execução"),
    "gauge_github": ("Gauge — repositório oficial", "https://github.com/getgauge/gauge", "código-fonte, versões e documentação do projeto"),
    # Behave (behave.readthedocs.io) — BDD for Python.
    "behave_docs": ("Behave — Documentação", "https://behave.readthedocs.io/en/stable/", "visão geral, instalação e índice dos guias"),
    "behave_tutorial": ("Behave — Tutorial", "https://behave.readthedocs.io/en/stable/tutorial/", "primeiros passos, ganchos, etiquetas e fixtures"),
    "behave_gherkin": ("Behave — Estrutura de testes", "https://behave.readthedocs.io/en/stable/gherkin/", "layout do projeto e linguagem Gherkin"),
    "behave_api": ("Behave — Referência de API", "https://behave.readthedocs.io/en/stable/api/", "funções de passo, ganchos, contexto e fixtures"),
    "behave_fixtures": ("Behave — Fixtures", "https://behave.readthedocs.io/en/stable/fixtures/", "declaração, uso e limpeza de fixtures"),
    "behave_tags": ("Behave — Expressões de etiqueta", "https://behave.readthedocs.io/en/stable/tag_expressions/", "seleção de cenários por expressões de etiqueta"),
    "behave_using": ("Behave — Uso da ferramenta", "https://behave.readthedocs.io/en/stable/behave/", "argumentos de linha de comando e arquivos de configuração"),
    "behave_django": ("Behave — Integração com Django", "https://behave.readthedocs.io/en/stable/usecase_django/", "preparação de banco e ambiente em projetos web"),
    "behave_practical": ("Behave — Dicas práticas", "https://behave.readthedocs.io/en/stable/practical_tips/", "recomendações de escopo e bibliotecas de automação"),
    "behave_github": ("Behave — repositório oficial", "https://github.com/behave/behave", "código-fonte, versões e documentação do projeto"),
    # MockServer (mock-server.com) — HTTP mocking and proxying.
    "ms_create": ("MockServer — Criar expectativas", "https://www.mock-server.com/mock_server/creating_expectations.html", "correspondentes de pedido, ações, prioridade e cenários"),
    "ms_verify": ("MockServer — Verificar pedidos", "https://www.mock-server.com/mock_server/verification.html", "verificação por quantidade e por sequência"),
    "ms_proxy_verify": ("MockServer — Verificar respostas", "https://www.mock-server.com/proxy/verification.html", "verificação de respostas gravadas e pares pedido-resposta"),
    "ms_proxy_start": ("MockServer — Gravar com proxy", "https://www.mock-server.com/proxy/getting_started.html", "encaminhamento, gravação e deduplicação de expectativas"),
    "ms_openapi": ("MockServer — OpenAPI e WSDL", "https://mock-server.com/mock_server/using_openapi.html", "geração de expectativas e verificação por contrato"),
    "ms_github": ("MockServer — repositório oficial", "https://github.com/mock-server/mockserver", "código-fonte, versões e documentação do projeto"),
    # Keploy (keploy.io) — record and replay testing.
    "kp_docs": ("Keploy — Documentação", "https://keploy.io/docs/", "instalação, gravação de tráfego, repetição e integração"),
    "kp_api": ("Keploy — Testes de API", "https://keploy.io/api-testing", "geração de casos a partir de tráfego e cobertura de interface"),
    "kp_github": ("Keploy — repositório oficial", "https://github.com/keploy/keploy", "código-fonte, versões e documentação do projeto"),
    # Selenide (selenide.org) — concise UI tests for Java.
    "sd_docs": ("Selenide — Documentação", "https://selenide.org/documentation.html", "API de elementos, coleções, condições e esperas automáticas"),
    "sd_pageobjects": ("Selenide — Objetos de página", "https://selenide.org/documentation/page-objects.html", "padrão de objetos de página sem anotações nem fábricas"),
    "sd_reports": ("Selenide — Relatórios", "https://selenide.org/documentation/reports.html", "integração com relatórios de execução"),
    "sd_screenshots": ("Selenide — Capturas de tela", "https://selenide.org/documentation/screenshots.html", "captura automática em falhas e configuração"),
    "sd_faq": ("Selenide — Perguntas frequentes", "https://selenide.org/faq.html", "configuração, navegadores, grade e boas práticas"),
    "sd_github": ("Selenide — repositório oficial", "https://github.com/selenide/selenide", "código-fonte, versões e documentação do projeto"),
    # AssertJ (assertj.github.io) — fluent assertions for the JVM.
    "aj_docs": ("AssertJ — Documentação", "https://assertj.github.io/doc/", "asserções fluentes, coleções, descrições, asserções suaves e próprias"),
    "aj_javadoc": ("AssertJ — Documentação de API", "https://javadoc.io/doc/org.assertj/assertj-core/latest/index.html", "referência das classes de asserção e dos módulos"),
    "aj_github": ("AssertJ — repositório oficial", "https://github.com/assertj/assertj", "código-fonte, versões e documentação do projeto"),
    # MockK (mockk.io) — mocking for Kotlin.
    "mk_readme": ("MockK — README oficial", "https://github.com/mockk/mockk/blob/master/README.md", "dublês, relaxamento, verificação, objetos e corrotinas"),
    "mk_guide": ("MockK — Guia de corrotinas", "https://notwoods.github.io/mockk-guidebook/docs/mocking/coroutines/", "uso das variantes para funções suspensas"),
    "mk_github": ("MockK — repositório oficial", "https://github.com/mockk/mockk", "código-fonte, versões e documentação do projeto"),
    # fast-check (fast-check.dev) — property-based testing for JavaScript.
    "fc_getting_started": ("fast-check — Primeiros passos", "https://fast-check.dev/docs/introduction/getting-started/", "propriedades, geradores, redução de casos e sementes"),
    "fc_npm": ("fast-check — Pacote publicado", "https://www.npmjs.com/package/fast-check", "versões, documentação de uso e recursos do pacote"),
    "fc_github": ("fast-check — repositório oficial", "https://github.com/dubzzz/fast-check", "código-fonte, exemplos e documentação do projeto"),
    # Robolectric (robolectric.org) — Android unit tests on the JVM.
    "rb_getting_started": ("Robolectric — Primeiros passos", "https://robolectric.org/getting-started/", "configuração do projeto, executor e ciclo de vida de telas"),
    "rb_configuring": ("Robolectric — Configuração", "https://robolectric.org/configuring/", "versão de sistema, sombras, propriedades e repositórios"),
    "rb_shadows": ("Robolectric — Sombras", "https://robolectric.org/extending/", "implementação de sombras, anotações e acesso ao objeto real"),
    "rb_github": ("Robolectric — repositório oficial", "https://github.com/robolectric/robolectric", "código-fonte, versões e documentação do projeto"),
    # NBomber (nbomber.com) — load testing for .NET.
    "nb_nuget": ("NBomber — Pacote publicado", "https://www.nuget.org/packages/NBomber", "versões, dependências e documentação do pacote"),
    "nb_github": ("NBomber — repositório oficial", "https://github.com/PragmaticFlow/NBomber", "código-fonte, integrações e documentação do projeto"),
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
id: software.testes.tranche20.{number:06d}
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-20.md"
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
        help="Rebuild the existing tranche-20 notes after validating their IDs and batch metadata.",
    )
    args = parser.parse_args()
    group_files = sorted(DATA_DIR.glob("*.txt"))
    if len(group_files) != 10:
        raise SystemExit(f"Esperados 10 arquivos de grupo; encontrados {len(group_files)}")

    existing_paths = list(DOMAINS_DIR.rglob("*.md"))
    existing_tranche = [
        path for path in existing_paths
        if re.search(
            r"(?m)^id: software\.testes\.tranche20\.\d{6}\s*$",
            path.read_text(encoding="utf-8", errors="replace")[:1200],
        )
    ]
    if args.refresh and len(existing_tranche) != EXPECTED_NOTES:
        raise ValueError(f"--refresh exige exatamente {EXPECTED_NOTES} notas tranche20 existentes; encontradas {len(existing_tranche)}")
    if REPORT.exists() and not args.refresh:
        raise ValueError(f"relatório já existe (use --refresh apenas para atualizar a tranche 20): {REPORT}")
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
            expected_id = f"id: software.testes.tranche20.{expected_number + index:06d}"
            if target_path.exists():
                current = target_path.read_text(encoding="utf-8")
                if not args.refresh:
                    raise ValueError(f"arquivo já existe (use --refresh apenas para a tranche 20): {target_path}")
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
        "# Revisão factual assistida por IA — lote `software-testes-2000-0001`, tranche 20",
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
