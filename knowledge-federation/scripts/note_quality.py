#!/usr/bin/env python3
"""Deterministic quality gates for Obsidian notes.

These checks detect incomplete, templated, or poorly sourced notes. A pass is
only a machine-screened candidate; factual correctness still needs a reviewer.
"""
from __future__ import annotations

from pathlib import Path
import re
import sqlite3
import unicodedata
from urllib.parse import urlparse

URL_RE = re.compile(r"https?://[^\s<>\]\[\"']+", re.IGNORECASE)
FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)(.*)\Z", re.DOTALL)
WORD_RE = re.compile(r"(?u)\b[\w]+(?:[-'][\w]+)*\b")

# Phrases emitted by the old scale pipeline. These are signals of a catalogue
# stub, not useful knowledge content. Keep this list conservative and test it.
PLACEHOLDER_PATTERNS = (
    r"nota semente sobre",
    r"nota virtual sobre",
    r"registro virtual ledger-first",
    r"criada para compor o mapa federado",
    r"em lotes futuros",
    r"fonte inicial a verificar",
    r"fontes a buscar",
    r"para estudo incremental",
    r"expanda a nota",
    r"ponto de partida para estudo",
    r"esta nota faz parte do ledger de conhecimento",
    r"vscale\s*#?\s*\d+",
    r"(?:conceito essencial|padrao pratico|erro comum|checklist de ia)\s*#?\s*\d+",
)

REQUIRED_FIELDS = (
    "id",
    "tipo",
    "dominio",
    "subdominio",
    "ultima_verificacao",
    "validade",
    "status",
    "fontes",
)
REQUIRED_HEADINGS = (
    "em uma frase",
    "por que importa",
    "como funciona",
    "exemplo",
    "como verificar",
    "fontes",
)


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).casefold()
    return "".join(ch for ch in text if not unicodedata.combining(ch))


def _parse_frontmatter(content: str) -> tuple[dict[str, str], str, bool]:
    match = FRONTMATTER_RE.match(content)
    if not match:
        return {}, content, False
    metadata: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line or line[0].isspace() or ":" not in line:
            continue
        key, value = line.split(":", 1)
        metadata[key.strip().casefold()] = value.strip().strip("\"'")
    return metadata, match.group(2), True


def _source_urls(body: str) -> list[str]:
    headings = list(re.finditer(r"(?m)^#{1,6}\s+(.+?)\s*#*\s*$", body))
    section = ""
    for index, heading in enumerate(headings):
        if normalize(heading.group(1).strip()) == "fontes":
            end = headings[index + 1].start() if index + 1 < len(headings) else len(body)
            section = body[heading.end():end]
            break
    urls: list[str] = []
    for raw_url in URL_RE.findall(section):
        url = raw_url.rstrip(".,;:!?)}")
        parsed = urlparse(url)
        if parsed.scheme == "https" and parsed.netloc and parsed.path.strip("/"):
            urls.append(url)
    return list(dict.fromkeys(urls))


def assess_markdown(content: str, path: str | Path = "", *, min_words: int = 100,
                    min_sources: int = 2) -> dict:
    """Return structural/content-quality findings for one Markdown note.

    A successful result means "ready for factual review", never "fact-checked".
    """
    metadata, body, has_frontmatter = _parse_frontmatter(content)
    errors: list[str] = []

    if not has_frontmatter:
        errors.append("missing_frontmatter")
    for field in REQUIRED_FIELDS:
        if not metadata.get(field):
            errors.append(f"missing_field:{field}")

    title_match = re.search(r"(?m)^#\s+(.+?)\s*$", body)
    title = title_match.group(1).strip() if title_match else ""
    if not title:
        errors.append("missing_title")
    elif re.search(r"(?i)\b(?:vscale\d*|batch-\d+|lote-\d+)\b|#\s*\d{3,}", title):
        errors.append("placeholder_title")

    headings = {
        normalize(match.group(1).strip()).rstrip("# ")
        for match in re.finditer(r"(?m)^#{1,6}\s+(.+?)\s*#*\s*$", body)
    }
    for required in REQUIRED_HEADINGS:
        if required not in headings:
            errors.append(f"missing_heading:{required}")
    if not any(heading.startswith("limites") or heading.startswith("quando nao usar") for heading in headings):
        errors.append("missing_heading:limites_ou_quando_nao_usar")

    prose = re.sub(r"```.*?```", " ", body, flags=re.DOTALL)
    prose = re.sub(r"`[^`]*`", " ", prose)
    word_count = len(WORD_RE.findall(prose))
    if word_count < min_words:
        errors.append(f"body_too_short:{word_count}/{min_words}")

    normalized_body = normalize(body)
    for pattern in PLACEHOLDER_PATTERNS:
        if re.search(pattern, normalized_body, re.IGNORECASE):
            errors.append(f"template_phrase:{pattern}")

    sources = _source_urls(body)
    if len(sources) < min_sources:
        errors.append(f"insufficient_specific_sources:{len(sources)}/{min_sources}")

    human_review = normalize(metadata.get("revisao_humana", ""))
    reviewer = metadata.get("revisor", "").strip()
    human_reviewed = human_review in {"aprovada", "aprovado", "validada", "validado", "reviewed"} and bool(reviewer)

    ai_review = normalize(metadata.get("revisao_ia", ""))
    ai_reviewer = metadata.get("revisor_ia", "").strip()
    ai_review_date = metadata.get("data_revisao_ia", "").strip()
    ai_review_report = metadata.get("relatorio_revisao_ia", "").strip()
    ai_reviewed = (
        ai_review in {"aprovada", "aprovado", "approved"}
        and bool(ai_reviewer)
        and bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}", ai_review_date))
        and bool(ai_review_report)
    )
    valid_reviewed = human_reviewed or ai_reviewed

    return {
        "path": str(path),
        "title": title,
        "word_count": word_count,
        "source_count": len(sources),
        "sources": sources,
        "errors": errors,
        "ready_for_review": not errors,
        "human_reviewed": human_reviewed,
        "ai_reviewed": ai_reviewed,
        "valid_reviewed": valid_reviewed,
    }


def inspect_ledger_database(database: str | Path) -> dict:
    """Count catalogue records and legacy virtual-note placeholders in SQLite."""
    con = sqlite3.connect(str(database))
    try:
        tables = {row[0] for row in con.execute("SELECT name FROM sqlite_master WHERE type='table'")}
        result = {
            "virtual_records": 0,
            "virtual_materialized": 0,
            "virtual_placeholder_records": 0,
            "physical_records": 0,
            "physical_deep_records": 0,
            "quality_candidate_records": 0,
            "needs_review_records": 0,
            "reviewed_records": 0,
        }
        if "virtual_notes" in tables:
            columns = {row[1] for row in con.execute("PRAGMA table_info(virtual_notes)")}
            result["virtual_records"] = con.execute("SELECT COUNT(*) FROM virtual_notes").fetchone()[0]
            if "materialized_path" in columns:
                result["virtual_materialized"] = con.execute(
                    "SELECT COUNT(*) FROM virtual_notes WHERE materialized_path IS NOT NULL"
                ).fetchone()[0]
            predicates = []
            if "summary" in columns:
                predicates.append("lower(coalesce(summary,'')) LIKE '%nota virtual sobre%'")
            if "body_seed" in columns:
                predicates.extend([
                    "lower(coalesce(body_seed,'')) LIKE '%registro virtual ledger-first%'",
                    "lower(coalesce(body_seed,'')) LIKE '%ao materializar, expanda%'",
                ])
            if "title" in columns:
                predicates.append("lower(coalesce(title,'')) LIKE '%vscale%'")
            if "quality_status" in columns:
                predicates.append("lower(coalesce(quality_status,'')) = 'catalog_only'")
            if predicates:
                result["virtual_placeholder_records"] = con.execute(
                    "SELECT COUNT(*) FROM virtual_notes WHERE " + " OR ".join(predicates)
                ).fetchone()[0]
            if "quality_status" in columns:
                result["reviewed_records"] += con.execute(
                    "SELECT COUNT(*) FROM virtual_notes WHERE lower(quality_status) IN ('reviewed','valid')"
                ).fetchone()[0]
                result["quality_candidate_records"] += con.execute(
                    "SELECT COUNT(*) FROM virtual_notes WHERE lower(quality_status) IN ('candidate','ready_for_review')"
                ).fetchone()[0]
                result["needs_review_records"] += con.execute(
                    "SELECT COUNT(*) FROM virtual_notes WHERE lower(quality_status) = 'needs_review'"
                ).fetchone()[0]
        if "notes" in tables:
            columns = {row[1] for row in con.execute("PRAGMA table_info(notes)")}
            result["physical_records"] = con.execute("SELECT COUNT(*) FROM notes").fetchone()[0]
            if "status" in columns:
                result["physical_deep_records"] = con.execute(
                    "SELECT COUNT(*) FROM notes WHERE lower(status) IN ('deep','reviewed','valid')"
                ).fetchone()[0]
            if "quality_status" in columns:
                result["reviewed_records"] += con.execute(
                    "SELECT COUNT(*) FROM notes WHERE lower(quality_status) IN ('reviewed','valid')"
                ).fetchone()[0]
                result["quality_candidate_records"] += con.execute(
                    "SELECT COUNT(*) FROM notes WHERE lower(quality_status) IN ('candidate','ready_for_review')"
                ).fetchone()[0]
                result["needs_review_records"] += con.execute(
                    "SELECT COUNT(*) FROM notes WHERE lower(quality_status) = 'needs_review'"
                ).fetchone()[0]
        return result
    finally:
        con.close()
