#!/usr/bin/env python3
"""Audit whether note files are substantive enough to enter human review."""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
import re
import sys

from note_quality import assess_markdown, inspect_ledger_database, normalize

SCRIPT_DIR = Path(__file__).resolve().parent
KF_ROOT = SCRIPT_DIR.parent
REPO_ROOT = KF_ROOT.parent


def markdown_files(paths: list[Path]) -> list[Path]:
    found: set[Path] = set()
    for path in paths:
        if path.is_file() and path.suffix.lower() == ".md":
            found.add(path.resolve())
        elif path.is_dir():
            found.update(p.resolve() for p in path.rglob("*.md") if p.is_file())
    return sorted(found)


WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
FRONTMATTER_RE = re.compile(r"\A---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|\Z)", re.DOTALL)


def _alias_values(value: str) -> list[str]:
    value = value.strip()
    if value.startswith("[") and value.endswith("]"):
        value = value[1:-1]
    aliases = []
    for quoted_double, quoted_single, bare in re.findall(r'"([^"]*)"|\'([^\']*)\'|([^,]+)', value):
        alias = (quoted_double or quoted_single or bare).strip().strip("\"'")
        if alias and alias.casefold() not in {"null", "none", "[]"}:
            aliases.append(alias)
    return aliases


def frontmatter_aliases(content: str) -> list[str]:
    match = FRONTMATTER_RE.match(content)
    if not match:
        return []
    aliases: list[str] = []
    in_alias_list = False
    for line in match.group(1).splitlines():
        if line.startswith("aliases:"):
            value = line.partition(":")[2].strip()
            if value:
                aliases.extend(_alias_values(value))
                in_alias_list = False
            else:
                in_alias_list = True
        elif in_alias_list and re.match(r"^\s+-\s*", line):
            aliases.extend(_alias_values(re.sub(r"^\s+-\s*", "", line)))
        elif line.strip() and not line[0].isspace():
            in_alias_list = False
    return aliases


def markdown_link_index(paths: list[Path]) -> tuple[set[str], set[str]]:
    stems: set[str] = set()
    relative_paths: set[str] = set()
    for path in markdown_files(paths):
        stems.add(normalize(path.stem))
        try:
            stems.update(normalize(alias) for alias in frontmatter_aliases(path.read_text(encoding="utf-8")))
        except (OSError, UnicodeError):
            pass
        for root in paths:
            if root.is_dir():
                try:
                    relative_paths.add(normalize(path.relative_to(root).with_suffix("").as_posix()))
                    break
                except ValueError:
                    continue
    return stems, relative_paths


def unresolved_wikilinks(content: str, known_stems: set[str], known_paths: set[str]) -> list[str]:
    missing = []
    for raw_target in WIKILINK_RE.findall(content):
        target = raw_target.split("|", 1)[0].split("#", 1)[0].strip().replace("\\", "/")
        if target.lower().endswith(".md"):
            target = target[:-3]
        target_path = normalize(target.strip("/"))
        target_stem = normalize(PurePosixPath(target_path).name)
        if target_stem not in known_stems and target_path not in known_paths:
            missing.append(raw_target)
    return list(dict.fromkeys(missing))


def render_report(results: list[dict], ledger: dict | None, roots: list[Path], link_roots: list[Path], min_words: int, min_sources: int) -> str:
    passed = [result for result in results if result["ready_for_review"]]
    failed = [result for result in results if not result["ready_for_review"]]
    reviewed = [result for result in passed if result["human_reviewed"]]
    issue_counts = Counter(
        error.split(":", 1)[0]
        for result in failed
        for error in result["errors"]
    )
    stamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    lines = [
        "# Auditoria de qualidade das notas",
        "",
        f"Executada em: `{stamp}`",
        "",
        "> Um resultado aprovado significa apenas que a nota passou por verificações automatizadas de estrutura, conteúdo mínimo, fontes específicas e ausência de marcadores de template. **Não comprova a veracidade das afirmações.** A validação factual e a aprovação humana permanecem separadas.",
        "",
        "## Arquivos Markdown ativos",
        "",
        f"- Escopo de notas: {', '.join(f'`{root.relative_to(REPO_ROOT)}`' if root.is_relative_to(REPO_ROOT) else f'`{root}`' for root in roots)}",
        f"- Escopo de resolução de links: {', '.join(f'`{root.relative_to(REPO_ROOT)}`' if root.is_relative_to(REPO_ROOT) else f'`{root}`' for root in link_roots)}",
        "- MOCs: fora do gate de qualidade; servem apenas como navegação.",
        f"- Arquivos avaliados: **{len(results):,}**",
        f"- Candidatas prontas para revisão humana: **{len(passed):,}**",
        f"- Com revisão humana aprovada e identificada no frontmatter: **{len(reviewed):,}**",
        f"- Notas válidas aprovadas (gate + revisão humana): **{len(reviewed):,}**",
        f"- Com pendências de qualidade: **{len(failed):,}**",
        f"- Critério aplicado: mínimo de {min_words} palavras, seções de conteúdo, {min_sources} fontes HTTPS específicas, links wiki resolvidos e sem frases de placeholder conhecidas.",
        "",
    ]

    if issue_counts:
        lines.extend(["### Pendências por tipo", ""])
        lines.extend(f"- `{kind}`: {count:,}" for kind, count in issue_counts.most_common())
        lines.append("")

    if passed:
        lines.extend(["### Candidatas prontas para revisão", ""])
        for result in passed:
            lines.append(
                f"- `{result['path']}` — {result['word_count']} palavras; {result['source_count']} fontes específicas; revisão humana: {'registrada' if result['human_reviewed'] else 'pendente'}."
            )
        lines.append("")

    if failed:
        lines.extend(["### Amostra de notas com pendências", ""])
        for result in failed[:40]:
            reasons = ", ".join(f"`{error}`" for error in result["errors"][:6])
            lines.append(f"- `{result['path']}` — {reasons}")
        if len(failed) > 40:
            lines.append(f"- … mais {len(failed) - 40:,} arquivos; consulte os critérios para reexecutar a auditoria por subdiretório.")
        lines.append("")

    if ledger is not None:
        virtual = ledger["virtual_records"]
        placeholders = ledger["virtual_placeholder_records"]
        lines.extend([
            "## Checkpoint SQLite legado",
            "",
            f"- Registros virtuais no ledger: **{virtual:,}** (inventário/IDs; não são automaticamente notas válidas).",
            f"- Registros com marcadores explícitos de conteúdo-template: **{placeholders:,}**.",
            f"- Registros virtuais restantes sem esses marcadores: **{max(0, virtual - placeholders):,}**; não são promovidos automaticamente a notas válidas.",
            f"- Registros virtuais com caminho materializado no checkpoint: **{ledger['virtual_materialized']:,}**; materialização de arquivo não equivale a validação editorial.",
            f"- Notas físicas registradas no checkpoint: **{ledger['physical_records']:,}**; status `deep/reviewed/valid` no schema antigo: **{ledger['physical_deep_records']:,}**.",
            f"- Registros no estado candidata/pronta para revisão no checkpoint: **{ledger['quality_candidate_records']:,}**.",
            f"- Registros com pendência de revisão no checkpoint: **{ledger['needs_review_records']:,}**.",
            f"- Registros com qualidade revisada explicitamente marcada no checkpoint: **{ledger['reviewed_records']:,}**.",
            "",
            "A auditoria do ledger usa os campos `summary`, `body_seed` e `title` para detectar o padrão legado. Mesmo um registro que não corresponda a esse padrão precisa ser materializado, avaliado e revisado antes de entrar na contagem válida.",
            "",
        ])

    lines.extend([
        "## Próximo passo",
        "",
        "Expandir as candidatas em lotes pequenos, revisar cada afirmação contra as fontes citadas e registrar `revisao_humana: aprovada` e o identificador do revisor somente após essa conferência. Não usar contagem de IDs, links ou arquivos como substituto da contagem de conteúdo validado.",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--path", action="append", dest="paths",
        help="Arquivo ou diretório Markdown a avaliar (repetível; padrão: knowledge-federation/domains).",
    )
    parser.add_argument(
        "--link-root", action="append", dest="link_roots",
        help="Raiz onde resolver wikilinks (repetível; padrão: knowledge-federation/ mais as pastas avaliadas).",
    )
    parser.add_argument("--min-words", type=int, default=100)
    parser.add_argument("--min-sources", type=int, default=2)
    parser.add_argument("--archive", help="Checkpoint .sqlite.xz/.zip a verificar além dos arquivos ativos.")
    parser.add_argument("--database", help="SQLite já extraído; alternativa a --archive.")
    parser.add_argument(
        "--out", default=str(KF_ROOT / "exports" / "reports" / "note-quality-audit.md"),
        help="Caminho do relatório Markdown.",
    )
    args = parser.parse_args()
    if args.min_words < 1 or args.min_sources < 1:
        parser.error("--min-words e --min-sources devem ser positivos")
    if args.archive and args.database:
        parser.error("use --archive ou --database, não ambos")

    roots = [Path(value).expanduser().resolve() for value in args.paths] if args.paths else [KF_ROOT / "domains"]
    link_roots = [Path(value).expanduser().resolve() for value in (args.link_roots or [])]
    if not args.link_roots:
        link_roots.append(KF_ROOT)
    link_roots.extend(roots)
    link_roots = list(dict.fromkeys(link_roots))
    known_stems, known_paths = markdown_link_index(link_roots)
    files = markdown_files(roots)
    results = []
    for path in files:
        try:
            content = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            results.append({
                "path": str(path.relative_to(REPO_ROOT)) if path.is_relative_to(REPO_ROOT) else str(path),
                "title": "", "word_count": 0, "source_count": 0, "sources": [],
                "errors": [f"unreadable:{type(exc).__name__}"],
                "ready_for_review": False, "human_reviewed": False,
            })
            continue
        display_path = str(path.relative_to(REPO_ROOT)) if path.is_relative_to(REPO_ROOT) else str(path)
        result = assess_markdown(content, display_path, min_words=args.min_words, min_sources=args.min_sources)
        unresolved = unresolved_wikilinks(content, known_stems, known_paths)
        result["unresolved_links"] = unresolved
        if unresolved:
            result["errors"].extend(f"broken_wikilink:{target}" for target in unresolved)
            result["ready_for_review"] = False
        results.append(result)

    ledger = None
    if args.database:
        ledger = inspect_ledger_database(Path(args.database).expanduser().resolve())
    elif args.archive:
        # Import lazily so simple directory audits do not need to inspect archives.
        from checkpoint_common import cached_sqlite_from_archive
        archive = Path(args.archive).expanduser()
        if not archive.is_absolute():
            archive = (Path.cwd() / archive).resolve()
        ledger = inspect_ledger_database(cached_sqlite_from_archive(str(archive)))

    report = render_report(results, ledger, roots, link_roots, args.min_words, args.min_sources)
    out = Path(args.out).expanduser()
    if not out.is_absolute():
        out = (Path.cwd() / out).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(report, encoding="utf-8")
    ready = sum(1 for result in results if result["ready_for_review"])
    valid = sum(1 for result in results if result["ready_for_review"] and result["human_reviewed"])
    print(f"Relatório: {out}")
    print(
        f"Arquivos: {len(results)} | candidatas para revisão: {ready} | "
        f"aprovadas por revisão humana: {valid} | com pendências: {len(results) - ready}"
    )
    if ledger is not None:
        print(
            "Ledger: "
            f"{ledger['virtual_records']} registros virtuais, "
            f"{ledger['virtual_placeholder_records']} com marcadores de template, "
            f"{ledger['virtual_materialized']} materializados"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
