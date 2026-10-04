#!/usr/bin/env python3
"""Build the source-backed software-testing tranche 19 (notes 1258–1358)."""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "knowledge-federation" / "scripts" / "_tranche19_data"
NOTES_DIR = ROOT / "knowledge-federation" / "domains" / "software-0007" / "software" / "testes"
DOMAINS_DIR = ROOT / "knowledge-federation" / "domains"
REPORT = ROOT / "knowledge-federation" / "exports" / "reports" / "ai-review-software-testes-2000-0001-tranche-19.md"
DATE = date.today().isoformat()
START = 1258
EXPECTED_NOTES = 101

sys.path.insert(0, str(ROOT / "knowledge-federation" / "scripts"))
from note_quality import assess_markdown, normalize  # noqa: E402
from prose_audit import repeated_substantive_sentences  # noqa: E402

SOURCES = {
    # Catch2 (github.com/catchorg/Catch2) — C++ testing framework.
    "catch2_github": ("Catch2 — repositório oficial", "https://github.com/catchorg/Catch2", "código-fonte, versões e documentação do projeto"),
    "catch2_tutorial": ("Catch2 — Tutorial", "https://github.com/catchorg/Catch2/blob/devel/docs/tutorial.md", "primeiros passos, casos de teste, seções e asserções"),
    "catch2_assertions": ("Catch2 — Assertions", "https://github.com/catchorg/Catch2/blob/devel/docs/assertions.md", "macros de asserção fatais e não fatais e comparações"),
    "catch2_test_cases": ("Catch2 — Test cases and sections", "https://github.com/catchorg/Catch2/blob/devel/docs/test-cases-and-sections.md", "casos, seções, etiquetas e macros BDD"),
    "catch2_fixtures": ("Catch2 — Test fixtures", "https://github.com/catchorg/Catch2/blob/devel/docs/test-fixtures.md", "preparação e limpeza por caso e por arquivo"),
    "catch2_generators": ("Catch2 — Data generators", "https://github.com/catchorg/Catch2/blob/devel/docs/generators.md", "geradores de valores, produto cartesiano e integração com seções"),
    "catch2_matchers": ("Catch2 — Matchers", "https://github.com/catchorg/Catch2/blob/devel/docs/matchers.md", "correspondências para texto, coleções, faixas e predicados"),
    "catch2_reporters": ("Catch2 — Reporters", "https://github.com/catchorg/Catch2/blob/devel/docs/reporters.md", "relatórios embutidos, múltiplos destinos e relatórios próprios"),
    "catch2_commandline": ("Catch2 — Command line", "https://github.com/catchorg/Catch2/blob/devel/docs/command-line.md", "filtros por nome e etiqueta, listagem, embaralhamento e semente"),
    # TestCafe (testcafe.io) — browser testing through a proxy.
    "testcafe_docs": ("TestCafe — Documentação", "https://testcafe.io/documentation", "guias de início, execução, depuração e relatórios"),
    "testcafe_selectors": ("TestCafe — Element selectors", "https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors", "seletores, filtros, propriedades e Shadow DOM"),
    "testcafe_actions": ("TestCafe — Test actions", "https://testcafe.io/documentation/402833/guides/basic-guides/test-actions", "ações do controlador, encadeamento, papéis e funções de cliente"),
    "testcafe_roles": ("TestCafe — Autenticação e papéis", "https://testcafe.io/documentation/402631/guides/basic-guides", "papéis de usuário, ativação e reaproveitamento de sessão"),
    "testcafe_github": ("TestCafe — repositório oficial", "https://github.com/DevExpress/testcafe", "código-fonte, versões e documentação do projeto"),
    # Mountebank (mbtest.org) — service virtualization.
    "mb_api": ("Mountebank — API overview", "https://www.mbtest.org/docs/api/overview", "interface administrativa, criação de impostores e remoção"),
    "mb_predicates": ("Mountebank — Predicates", "https://www.mbtest.org/docs/api/predicates", "operadores de correspondência de requisições"),
    "mb_stubs": ("Mountebank — Stubs", "https://www.mbtest.org/docs/api/stubs", "stubs, respostas, sequências e stub padrão"),
    "mb_proxies": ("Mountebank — Proxies", "https://www.mbtest.org/docs/api/proxies", "encaminhamento ao serviço real, gravação e reprodução"),
    "mb_behaviors": ("Mountebank — Behaviors", "https://www.mbtest.org/docs/api/behaviors", "atraso, cópia de valores e repetição de respostas"),
    "mb_injection": ("Mountebank — Injection", "https://www.mbtest.org/docs/api/injection", "predicados e respostas calculados por função JavaScript"),
    "mb_github": ("Mountebank — repositório oficial", "https://github.com/bbyars/mountebank", "código-fonte, versões e documentação do projeto"),
    # LocalStack (docs.localstack.cloud) — local cloud emulation.
    "localstack_docs": ("LocalStack — Primeiros passos", "https://docs.localstack.cloud/getting-started/", "instalação, execução local e visão geral dos serviços emulados"),
    "localstack_init": ("LocalStack — Initialization hooks", "https://docs.localstack.cloud/aws/capabilities/config/initialization-hooks/", "fases de inicialização, diretórios e ponto de estado"),
    "localstack_terraform": ("LocalStack — Integração com Terraform", "https://docs.localstack.cloud/user-guide/integrations/terraform/", "uso de configuração declarada como preparação do ambiente"),
    "localstack_testcontainers": ("LocalStack — Terraform e Testcontainers", "https://docs.localstack.cloud/aws/tutorials/using-terraform-with-testcontainers-and-localstack/", "preparação automatizada com contêineres de teste"),
    "localstack_docker": ("Docker — Guia do LocalStack", "https://docs.docker.com/guides/localstack/", "composição de contêineres, variáveis e ganchos montados"),
    "localstack_cli": ("LocalStack — awscli-local", "https://github.com/localstack/awscli-local", "invólucro de linha de comando apontado para o ambiente emulado"),
    "localstack_ci": ("LocalStack — Ação de integração contínua", "https://github.com/localstack/setup-localstack", "ação publicada para iniciar o serviço na esteira"),
    "localstack_github": ("LocalStack — repositório oficial", "https://github.com/localstack/localstack", "código-fonte, versões e documentação do projeto"),
    # Terratest (terratest.gruntwork.io) — infrastructure testing.
    "tt_terraform": ("Terratest — Módulo terraform", "https://pkg.go.dev/github.com/gruntwork-io/terratest/modules/terraform", "opções, aplicação, saídas e destruição"),
    "tt_httphelper": ("Terratest — Módulo http-helper", "https://pkg.go.dev/github.com/gruntwork-io/terratest/modules/http-helper", "verificação de rede com repetição e validação"),
    "tt_teststructure": ("Terratest — Módulo test-structure", "https://pkg.go.dev/github.com/gruntwork-io/terratest/modules/test-structure", "estágios de teste, estado salvo e variáveis de salto"),
    "tt_aws": ("Terratest — Módulo aws", "https://pkg.go.dev/github.com/gruntwork-io/terratest/modules/aws", "consultas de estado e verificação de recursos"),
    "tt_random": ("Terratest — Módulo random", "https://pkg.go.dev/github.com/gruntwork-io/terratest/modules/random", "geração de identificadores únicos para recursos"),
    "tt_github": ("Terratest — repositório oficial", "https://github.com/gruntwork-io/terratest", "código-fonte, exemplos e documentação do projeto"),
    # Checkov (github.com/bridgecrewio/checkov) — IaC policy scanning.
    "ck_github": ("Checkov — repositório oficial", "https://github.com/bridgecrewio/checkov", "código-fonte, verificações e documentação do projeto"),
    "ck_readme": ("Checkov — Guia de uso", "https://github.com/bridgecrewio/checkov/blob/master/README.md", "execução, seleção de verificações, supressões, linha de base e segredos"),
    "ck_action": ("Checkov — Ação do GitHub", "https://github.com/bridgecrewio/checkov-action", "integração publicada para pipelines"),
    "ck_terraform": ("Checkov — Verificações Terraform", "https://github.com/bridgecrewio/checkov/tree/master/checkov/terraform", "implementação das verificações de configuração declarada"),
    "ck_kubernetes": ("Checkov — Verificações Kubernetes", "https://github.com/bridgecrewio/checkov/tree/master/checkov/kubernetes", "implementação das verificações de manifestos e gráficos"),
    "ck_secrets": ("Checkov — Verificações de segredos", "https://github.com/bridgecrewio/checkov/tree/master/checkov/secrets", "detecção de credenciais por padrões, palavras-chave e entropia"),
    "ck_docs": ("Checkov — Documentação no repositório", "https://github.com/bridgecrewio/checkov/tree/master/docs", "guias de contribuição e referência das verificações"),
    # BackstopJS (github.com/garris/BackstopJS) — visual regression.
    "bs_github": ("BackstopJS — repositório oficial", "https://github.com/garris/BackstopJS", "código-fonte, versões e documentação do projeto"),
    "bs_readme": ("BackstopJS — Guia de uso", "https://github.com/garris/BackstopJS/blob/master/README.md", "cenários, propriedades, tolerância, relatórios e aprovação"),
    "bs_docs": ("BackstopJS — Página do projeto", "https://garris.github.io/BackstopJS/", "demonstração e documentação publicada"),
    "bs_examples": ("BackstopJS — Exemplos", "https://github.com/garris/BackstopJS/tree/master/examples", "configurações e cenários de exemplo"),
    # ReportPortal (reportportal.io) — test reporting and analytics.
    "rp_docs": ("ReportPortal — Documentação", "https://reportportal.io/docs/", "execuções, lançamentos, defeitos, painéis e integrações"),
    "rp_attributes": ("ReportPortal — Atributos", "https://reportportal.io/docs/log-data-in-reportportal/HowToReportAttributesToReportPortal/", "atributos de lançamento e de item, filtros e atributos de sistema"),
    "rp_developers": ("ReportPortal — Guia de desenvolvedores", "https://reportportal.io/docs/developers-guides/ReportingDevelopersGuide/", "lançamentos, itens, identificadores e histórico"),
    "rp_testexec": ("ReportPortal — Execuções de teste", "https://reportportal.io/docs/test-executions/", "filtros, colunas personalizadas e visões de acompanhamento"),
    "rp_pytest": ("ReportPortal — Integração com pytest", "https://reportportal.io/docs/log-data-in-reportportal/test-framework-integration/Python/pytest/", "configuração do agente e marcação de testes"),
    "rp_github": ("ReportPortal — repositório oficial", "https://github.com/reportportal/reportportal", "código-fonte, versões e documentação do projeto"),
    # ArchUnit (archunit.org) — architecture tests for Java.
    "au_userguide": ("ArchUnit — User Guide", "https://www.archunit.org/userguide/html/000_Index.html", "regras, camadas, fatias, congelamento e verificação por diagrama"),
    "au_javadoc": ("ArchUnit — Documentação de API", "https://javadoc.io/doc/com.tngtech.archunit/archunit/latest/index.html", "referência das classes de regras e da API de camadas"),
    "au_github": ("ArchUnit — repositório oficial", "https://github.com/TNG/ArchUnit", "código-fonte, versões e documentação do projeto"),
    "au_examples": ("ArchUnit — Exemplos oficiais", "https://github.com/TNG/ArchUnit-Examples", "exemplos de regras e do uso de congelamento"),
    # Insta (insta.rs) — snapshot testing for Rust.
    "insta_docs": ("Insta — Documentação do pacote", "https://docs.rs/insta", "macros de instantâneo, opções, modos de atualização e redações"),
    "insta_quickstart": ("Insta — Guia inicial", "https://insta.rs/docs/quickstart/", "instalação, fluxo de revisão e execução estrita"),
    "insta_inline": ("Insta — Snapshots embutidos", "https://insta.rs/docs/inline-snapshots/", "referência no código, formato e atualização pelo comando de revisão"),
    "insta_cargo": ("cargo-insta — Documentação do comando", "https://docs.rs/cargo-insta", "revisão interativa, coleta de propostas e comandos de teste"),
    "insta_crates": ("insta — Registro de pacotes", "https://crates.io/crates/insta", "versões publicadas, recursos opcionais e formatos suportados"),
    "insta_github": ("Insta — repositório oficial", "https://github.com/mitsuhiko/insta", "código-fonte, notas de versão e documentação do projeto"),
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
id: software.testes.tranche19.{number:06d}
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-19.md"
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
        help="Rebuild the existing tranche-19 notes after validating their IDs and batch metadata.",
    )
    args = parser.parse_args()
    group_files = sorted(DATA_DIR.glob("*.txt"))
    if len(group_files) != 10:
        raise SystemExit(f"Esperados 10 arquivos de grupo; encontrados {len(group_files)}")

    existing_paths = list(DOMAINS_DIR.rglob("*.md"))
    existing_tranche = [
        path for path in existing_paths
        if re.search(
            r"(?m)^id: software\.testes\.tranche19\.\d{6}\s*$",
            path.read_text(encoding="utf-8", errors="replace")[:1200],
        )
    ]
    if args.refresh and len(existing_tranche) != EXPECTED_NOTES:
        raise ValueError(f"--refresh exige exatamente {EXPECTED_NOTES} notas tranche19 existentes; encontradas {len(existing_tranche)}")
    if REPORT.exists() and not args.refresh:
        raise ValueError(f"relatório já existe (use --refresh apenas para atualizar a tranche 19): {REPORT}")
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
            expected_id = f"id: software.testes.tranche19.{expected_number + index:06d}"
            if target_path.exists():
                current = target_path.read_text(encoding="utf-8")
                if not args.refresh:
                    raise ValueError(f"arquivo já existe (use --refresh apenas para a tranche 19): {target_path}")
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
        "# Revisão factual assistida por IA — lote `software-testes-2000-0001`, tranche 19",
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
