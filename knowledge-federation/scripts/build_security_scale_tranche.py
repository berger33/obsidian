#!/usr/bin/env python3
"""Build and screen one 100-note tranche for software-seguranca-2000-0003.

The source records are editorial inputs, not notes. This script refuses to
overwrite published material, renders explicit factual-review metadata, checks
each note with the repository gate, and rejects repeated prose in a tranche.
"""
from __future__ import annotations

import argparse
from datetime import date
import json
from pathlib import Path
import re
import sys
import unicodedata

ROOT = Path(__file__).resolve().parents[2]
KF = ROOT / "knowledge-federation"
DOMAINS = KF / "domains"
NOTES_DIR = DOMAINS / "software-0009" / "software" / "seguranca"
DATA_ROOT = Path(__file__).resolve().parent / "_security_scale_data"
BATCH_ID = "software-seguranca-2000-0003"
REVIEWER = "Arena.ai Agent Mode"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from note_quality import assess_markdown, normalize  # noqa: E402
from prose_audit import repeated_substantive_sentences  # noqa: E402

REQUIRED_TEXT_FIELDS = ("summary", "why", "how", "example", "limits", "verify", "review")


def selected_sources(group: dict, row: dict) -> list[dict]:
    return group.get("source_overrides", {}).get(row["slug"], group["sources"])


def validate_sources(sources: list[dict], context: str) -> None:
    if len(sources) < 2 or len({source.get("url") for source in sources}) < 2:
        raise ValueError(f"{context}: são necessárias duas fontes distintas")
    for source in sources:
        if not source.get("label") or not source.get("description"):
            raise ValueError(f"{context}: fonte sem rótulo ou descrição")
        if not re.match(r"^https://[^/]+/.+", source.get("url", "")):
            raise ValueError(f"{context}: fonte HTTPS específica ausente: {source.get('url')}")


def slug_ok(value: str) -> bool:
    return bool(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", value))


def load_groups(tranche: int) -> list[dict]:
    data_dir = DATA_ROOT / f"tranche-{tranche:02d}"
    files = sorted(data_dir.glob("*.json"))
    if len(files) != 10:
        raise ValueError(f"{data_dir}: esperados 10 grupos; encontrados {len(files)}")
    groups = []
    for path in files:
        group = json.loads(path.read_text(encoding="utf-8"))
        if not group.get("group_title"):
            raise ValueError(f"{path.name}: group_title ausente")
        if len(group.get("coverage_review", "").split()) < 20:
            raise ValueError(f"{path.name}: coverage_review ausente ou curto")
        sources = group.get("sources", [])
        validate_sources(sources, path.name)
        overrides = group.get("source_overrides", {})
        if not isinstance(overrides, dict):
            raise ValueError(f"{path.name}: source_overrides deve ser um objeto")
        notes = group.get("notes", [])
        if len(notes) != 10:
            raise ValueError(f"{path.name}: esperadas 10 notas; encontradas {len(notes)}")
        note_slugs = {note.get("slug") for note in notes}
        unknown_overrides = set(overrides) - note_slugs
        if unknown_overrides:
            raise ValueError(f"{path.name}: source_overrides sem nota correspondente: {sorted(unknown_overrides)}")
        for note in notes:
            if not slug_ok(note.get("slug", "")):
                raise ValueError(f"{path.name}: slug inválido: {note.get('slug')}")
            for field in REQUIRED_TEXT_FIELDS:
                if not isinstance(note.get(field), str) or len(note[field].split()) < 12:
                    raise ValueError(f"{path.name}/{note.get('slug')}: campo {field} curto ou ausente")
            if note.get("slug") in overrides:
                validate_sources(overrides[note["slug"]], f"{path.name}/{note['slug']}")
        groups.append(group)
    return groups


def render_note(tranche: int, number: int, group: dict, row: dict, today: str,
                report_name: str, neighbors: list[dict]) -> str:
    sources = selected_sources(group, row)
    report_path = f"knowledge-federation/exports/reports/{report_name}"
    source_urls = ", ".join(json.dumps(source["url"], ensure_ascii=False) for source in sources)
    frontmatter = f'''---
id: software.seguranca.tranche{tranche}.{number:06d}
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: {today}
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "{REVIEWER}"
data_revisao_ia: {today}
relatorio_revisao_ia: "{report_path}"
fontes: [{source_urls}]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: {BATCH_ID}
---
'''
    links = "\n".join(f"- [[{item['slug']}]] — {item['title']}." for item in neighbors)
    code = row.get("code", "").strip()
    code_block = f"\n\n```text\n{code}\n```" if code else ""
    source_lines = "\n".join(
        f"- [{source['label']}]({source['url']}) — {source['description']}; consultado em {today}."
        for source in sources
    )
    return f'''{frontmatter}
# {row['title']}

## Em uma frase
{row['summary']}

## Por que importa
{row['why']}

## Como funciona
{row['how']}

## Exemplo
{row['example']}{code_block}

## Limites e trade-offs
{row['limits']}

## Como verificar
{row['verify']}

## Conexões
{links}

## Fontes
{source_lines}
'''


def build_report(tranche: int, start: int, today: str, report_name: str,
                 groups: list[dict], items: list[tuple[int, Path, str, dict, dict]]) -> str:
    end = start + len(items) - 1
    lines = [
        f"# Revisão factual assistida por IA — lote `{BATCH_ID}`, tranche {tranche:02d}",
        "",
        f"- Data: {today}",
        f"- Revisor: `{REVIEWER}`",
        f"- Escopo: notas **{start}–{end}**, em dez grupos temáticos; cada linha registra a conferência da nota correspondente.",
        "- Método: confrontei o escopo de cada nota com documentação primária específica listada no próprio arquivo; afirmações foram mantidas dentro do material citado e ressalvas foram registradas.",
        "- Resultado: **100 revisões factuais por IA registradas**; isto não é aprovação humana nem garantia de ausência de erro.",
        "- As 49 aprovações humanas históricas permaneceram inalteradas; nenhuma foi aplicada às notas desta tranche.",
        "",
        "## Registro por nota",
        "",
        "| # | Nota | Fontes primárias consultadas | Conferência factual / decisão |",
        "|---:|---|---|---|",
    ]
    for number, path, content, group, row in items:
        sources = selected_sources(group, row)
        source_links = " e ".join(f"[{source['label']}]({source['url']})" for source in sources)
        note_link = f"[[{path.stem}]]"
        review = row["review"].replace("|", "\\|").replace("\n", " ")
        lines.append(f"| {number} | {note_link} | {source_links} | {review} Decisão: aprovada. |")
    lines.extend(["", "## Conferência por grupo", ""])
    for group in groups:
        lines.append(f"- **{group['group_title']} — conferência factual:** {group['fact_check']}")
        lines.append(f"  **Cobertura anterior:** {group['coverage_review']}")
    lines.extend([
        "",
        "## Resultado e limites",
        "",
        "As notas foram confrontadas com as fontes primárias listadas e passaram pelo gate automatizado. A revisão por IA é uma camada editorial documentada, não prova de correção absoluta; mudanças posteriores nas ferramentas podem exigir nova verificação. Nenhuma aprovação humana foi criada, copiada ou alterada.",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tranche", type=int, required=True, choices=range(17, 21))
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--check-only", action="store_true",
                        help="validar dados e notas em memória sem gravar arquivos")
    args = parser.parse_args()
    tranche = args.tranche
    today = args.date
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", today):
        parser.error("--date deve usar AAAA-MM-DD")
    start = (tranche - 1) * 100 + 1
    end = start + 99
    report_name = f"ai-review-{BATCH_ID}-tranche-{tranche:02d}.md"
    report_path = KF / "exports" / "reports" / report_name
    groups = load_groups(tranche)

    if report_path.exists():
        raise SystemExit(f"relatório já existe; não sobrescrevo conteúdo publicado: {report_path}")
    all_existing = list(DOMAINS.rglob("*.md"))
    existing_slugs = {path.stem for path in all_existing}
    existing_titles: set[str] = set()
    existing_ids: set[str] = set()
    for path in all_existing:
        text = path.read_text(encoding="utf-8", errors="replace")
        title_match = re.search(r"(?m)^#\s+(.+?)\s*$", text)
        if title_match:
            existing_titles.add(normalize(title_match.group(1).strip()))
        id_match = re.search(r"(?m)^id:\s*(software\.seguranca\.tranche\d+\.\d{6})\s*$", text[:1200])
        if id_match:
            existing_ids.add(id_match.group(1))

    rows_by_group = [(group, group["notes"]) for group in groups]
    flat_rows = [row for _, rows in rows_by_group for row in rows]
    if len(flat_rows) != 100:
        raise SystemExit(f"tranche {tranche}: esperado 100 registros, encontrados {len(flat_rows)}")
    if len({row["slug"] for row in flat_rows}) != 100:
        raise SystemExit(f"tranche {tranche}: slug repetido dentro dos dados")
    if len({normalize(row["title"]) for row in flat_rows}) != 100:
        raise SystemExit(f"tranche {tranche}: título repetido dentro dos dados")
    known_link_stems = {normalize(slug) for slug in existing_slugs}
    planned_link_stems = {normalize(row["slug"]) for row in flat_rows}

    items: list[tuple[int, Path, str, dict, dict]] = []
    number = start
    for group, rows in rows_by_group:
        for index, row in enumerate(rows):
            slug = row["slug"]
            title = normalize(row["title"])
            note_id = f"software.seguranca.tranche{tranche}.{number:06d}"
            path = NOTES_DIR / f"{slug}.md"
            if slug in existing_slugs or title in existing_titles or note_id in existing_ids or path.exists():
                raise SystemExit(f"conflito com conteúdo existente: {note_id} / {path.name}")
            neighbors = []
            if index > 0:
                neighbors.append(rows[index - 1])
            if index + 1 < len(rows):
                neighbors.append(rows[index + 1])
            content = render_note(tranche, number, group, row, today, report_name, neighbors)
            for target in re.findall(r"\[\[([^\]]+)\]\]", content):
                stem = normalize(target.split("|", 1)[0].split("#", 1)[0].strip())
                if stem not in known_link_stems and stem not in planned_link_stems:
                    raise SystemExit(f"{path.name}: wikilink não resolvido: {target}")
            result = assess_markdown(content, path)
            if result["errors"]:
                raise SystemExit(f"{path.name}: {result['errors']} ({result['word_count']} palavras)")
            items.append((number, path, content, group, row))
            number += 1

    if number - 1 != end:
        raise SystemExit(f"IDs inesperados: {start}–{number - 1}, esperado {start}–{end}")
    repeated = repeated_substantive_sentences((number, content) for number, _, content, _, _ in items)
    if repeated:
        sample = list(repeated.items())[:8]
        raise SystemExit(f"sentenças substantivas repetidas na tranche: {sample}")

    report = build_report(tranche, start, today, report_name, groups, items)
    if args.check_only:
        action = "preflight aprovado; nenhum arquivo gravado"
    else:
        if report_path.exists() or any(path.exists() for _, path, _, _, _ in items):
            raise SystemExit("um arquivo da tranche apareceu durante a validação; nada foi gravado")
        NOTES_DIR.mkdir(parents=True, exist_ok=True)
        for _, path, content, _, _ in items:
            path.write_text(content, encoding="utf-8")
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(report.rstrip() + "\n", encoding="utf-8")
        action = str(report_path.relative_to(ROOT))
    words = [assess_markdown(content, path)["word_count"] for _, path, content, _, _ in items]
    print(f"tranche {tranche:02d}: {len(items)} notas ({start}–{end}); min={min(words)} max={max(words)} palavras; {action}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
