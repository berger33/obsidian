#!/usr/bin/env python3
"""Build the 100 substantive candidate notes for batch 4, tranche 03."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KF = ROOT / "knowledge-federation"
NOTES_DIR = KF / "domains" / "software-0010" / "software" / "criacao-ia"
DATA_DIR = Path(__file__).resolve().parent / "_criacao_ia_t03_data"
BATCH_ID = "software-criacao-ia-2000-0004"
TRANCHE = "tranche03"
DATE = "2026-10-04"
START = 201
EXPECTED_NOTES = 100
AI_REVIEW_REPORT = "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-03.md"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from note_quality import assess_markdown, normalize  # noqa: E402
from prose_audit import repeated_substantive_sentences  # noqa: E402

REQUIRED_KEYS = {
    "slug", "title", "one", "why", "how", "example", "limits", "verify", "sources", "review"
}


def load_groups() -> list[dict]:
    groups = []
    for path in sorted(DATA_DIR.glob("*.json")):
        group = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(group, dict) or not isinstance(group.get("notes"), list):
            raise ValueError(f"Formato inválido: {path.name}")
        group["_path"] = path
        groups.append(group)
    if len(groups) != 10:
        raise ValueError(f"Esperados 10 grupos, encontrados {len(groups)}")
    if any(len(group["notes"]) != 10 for group in groups):
        raise ValueError("Cada grupo deve conter exatamente 10 notas")
    return groups


def render_note(group: dict, index: int, row: dict, number: int, all_rows: list[dict]) -> str:
    missing = REQUIRED_KEYS - row.keys()
    if missing:
        raise ValueError(f"{row.get('slug', '?')}: campos ausentes {sorted(missing)}")
    slug = row["slug"]
    sources = row["sources"]
    if not isinstance(sources, list) or len(sources) != 2:
        raise ValueError(f"{slug}: devem existir exatamente duas fontes")
    for src in sources:
        if not all(k in src for k in ("label", "url", "why")):
            raise ValueError(f"{slug}: fonte incompleta")
        if not src["url"].startswith("https://"):
            raise ValueError(f"{slug}: fonte sem HTTPS: {src['url']}")

    links = []
    for other_index in (index - 1, index + 1):
        if 0 <= other_index < len(all_rows):
            other = all_rows[other_index]
            links.append(f"- [[{other['slug']}]] — {other['title']}.")

    source_urls = ", ".join(f'"{src["url"]}"' for src in sources)
    frontmatter = f'''---
id: software.criacao_ia.{TRANCHE}.{number:06d}
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: avancado
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
fontes: [{source_urls}]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: {BATCH_ID}
---'''

    source_lines = [
        f"- [{src['label']}]({src['url']}) — {src['why']} Consulta: {DATE}."
        for src in sources
    ]
    body = f'''# {row['title']}

## Em uma frase
{row['one']}

## Por que importa
{row['why']}

## Como funciona
{row['how']}

## Exemplo
{row['example']}

## Limites e trade-offs
{row['limits']}

## Como verificar
{row['verify']}

## Conexões
{chr(10).join(links)}

## Fontes
{chr(10).join(source_lines)}
'''
    return f"{frontmatter}\n\n{body}"


def main() -> int:
    groups = load_groups()
    rows = [row for group in groups for row in group["notes"]]
    if len(rows) != EXPECTED_NOTES:
        raise ValueError(f"Esperadas {EXPECTED_NOTES} notas, encontradas {len(rows)}")

    existing_files = {p.stem.casefold(): p for p in NOTES_DIR.glob("*.md")}
    existing_titles = set()
    for path in NOTES_DIR.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        match = re.search(r"(?m)^#\s+(.+?)\s*$", text)
        if match:
            existing_titles.add(normalize(match.group(1).strip()))

    pending = []
    seen_slugs: set[str] = set()
    seen_titles: set[str] = set()
    for index, (group, row) in enumerate((g, r) for g in groups for r in g["notes"]):
        number = START + index
        slug = row["slug"]
        title = row["title"]
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
            raise ValueError(f"Slug não canônico: {slug}")
        if slug.casefold() in existing_files:
            raise ValueError(f"Slug já existe: {slug} -> {existing_files[slug.casefold()]}")
        normalized_title = normalize(title)
        if normalized_title in existing_titles or normalized_title in seen_titles:
            raise ValueError(f"Título duplicado ou sobreposto: {title}")
        seen_slugs.add(slug)
        seen_titles.add(normalized_title)
        content = render_note(group, index % 10, row, number, group["notes"])
        quality = assess_markdown(content, f"{slug}.md")
        if not quality["ready_for_review"]:
            raise ValueError(f"Falha estrutural antes da gravação em {slug}: {quality['errors']}")
        pending.append((number, row, group, content, quality))

    repeated = repeated_substantive_sentences(
        [(number, content) for number, _row, _group, content, _quality in pending]
    )
    if repeated:
        examples = [f"{numbers}: {sentence}" for sentence, numbers in list(repeated.items())[:8]]
        raise ValueError(f"Prosa substantiva repetida entre notas: {examples}")

    NOTES_DIR.mkdir(parents=True, exist_ok=True)
    for _number, row, _group, content, _quality in pending:
        target = NOTES_DIR / f"{row['slug']}.md"
        if target.exists():
            raise FileExistsError(target)
        target.write_text(content, encoding="utf-8")

    word_counts = [quality["word_count"] for *_rest, quality in pending]
    source_counts = [quality["source_count"] for *_rest, quality in pending]
    print(f"Geradas {len(pending)} notas candidatas (IDs {START}–{START + EXPECTED_NOTES - 1}).")
    print(f"Gate preliminar (prontas para revisão factual): {sum(q['ready_for_review'] for *_rest, q in pending)}/{len(pending)}")
    print(f"Palavras por nota: min={min(word_counts)}, max={max(word_counts)}; fontes HTTPS: min={min(source_counts)}, max={max(source_counts)}")
    print("Metadados de revisão IA permanecem pendentes até o relatório factual separado.")
    print(f"Relatório de revisão previsto: {AI_REVIEW_REPORT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
