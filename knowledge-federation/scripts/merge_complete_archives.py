#!/usr/bin/env python3
import argparse, io, json, re, sys, tarfile, zipfile
from pathlib import Path
from kf_common import ROOT, now

RANGE_RE = re.compile(r"study-vault-lotes-(\d+)-(\d+)\.zip$")


def add_bytes(tar, arcname, data, mtime=0):
    if isinstance(data, str):
        data = data.encode("utf-8")
    ti = tarfile.TarInfo(arcname)
    ti.size = len(data)
    ti.mtime = mtime
    ti.mode = 0o644
    tar.addfile(ti, io.BytesIO(data))


def add_file(tar, path, arcname):
    path = Path(path)
    ti = tar.gettarinfo(str(path), arcname=arcname)
    ti.mtime = 0
    with path.open("rb") as f:
        tar.addfile(ti, f)


def markdown_entry_count(zip_path):
    if not zip_path.exists():
        return None
    with zipfile.ZipFile(zip_path) as archive:
        return sum(
            1 for item in archive.infolist()
            if not item.is_dir() and item.filename.lower().endswith(".md")
        )


def iter_lot_archives():
    first = ROOT / "archives" / "study-vault-next-100-lotes.zip"
    if first.exists():
        yield (1, 100, first)
    found = []
    for p in (ROOT / "archives").glob("study-vault-lotes-*.zip"):
        m = RANGE_RE.match(p.name)
        if m:
            found.append((int(m.group(1)), int(m.group(2)), p))
    yield from sorted(found)


def add_zip_expanded(tar, zip_path, prefix):
    count = 0
    with zipfile.ZipFile(zip_path) as z:
        for info in z.infolist():
            if info.is_dir():
                continue
            data = z.read(info.filename)
            arcname = f"{prefix}/{info.filename}"
            ti = tarfile.TarInfo(arcname)
            ti.size = len(data)
            ti.mtime = 0
            ti.mode = 0o644
            tar.addfile(ti, io.BytesIO(data))
            count += 1
    return count


def main():
    ap = argparse.ArgumentParser(description="Agrupa arquivos históricos de catálogo; contagens de arquivos não são contagens de notas válidas.")
    ap.add_argument("--base-tar", default=None, help="Tar.xz anterior para preservar lotes já podados (0001-3300).")
    ap.add_argument("--include-ledger", action="store_true", help="Inclui o checkpoint ledger compactado como arquivo interno.")
    args = ap.parse_args()

    lots = list(iter_lot_archives())
    new_lot_prefixes = {f"MERGE-COMPLETO/10-lotes/{a:04d}-{b:04d}/" for a, b, _ in lots}
    consolidated = ROOT / "archives" / "study-vault-1m-packs.zip"
    ledger_xz = ROOT / "archives" / "ledger-v1000000-mat8000.sqlite.xz"
    ledger_zip = ROOT / "archives" / "ledger-v1000000-mat8000.zip"
    ledger = ledger_xz if ledger_xz.exists() else ledger_zip

    seq_manifest_path = ROOT / "exports" / "reports" / "lot-sequence-manifest.json"
    seq_manifest = json.loads(seq_manifest_path.read_text(encoding="utf-8")) if seq_manifest_path.exists() else []

    docs = [
        ROOT / "README-1M.md",
        ROOT / "STUDY-VAULT-README.md",
        ROOT / "STATUS-CONSOLIDACAO-1M.md",
        ROOT / "LOT-SEQUENCE.md",
        ROOT / "LOTS-301-800.md",
        ROOT / "LOTS-801-3300.md",
        ROOT / "LOTS-3301-5000.md",
        ROOT / "PACK-INVENTORY.md",
        ROOT / "NEXT-100-LOTS.md",
        ROOT / "LOTS-101-200.md",
        ROOT / "LOTS-201-300.md",
        seq_manifest_path,
    ]

    base_path = Path(args.base_tar).expanduser() if args.base_tar else None
    if base_path is not None and not base_path.is_file():
        ap.error(f"--base-tar não existe ou não é arquivo: {base_path}")
    if seq_manifest and not lots and base_path is None:
        ap.error("os zips dos lotes foram podados; use --base-tar para preservar a sequência já arquivada")

    if seq_manifest:
        lot_count = sum(
            int(item.get("lots", int(item["end"]) - int(item["start"]) + 1))
            for item in seq_manifest
        )
        catalog_files_from_lots = sum(
            int(item.get("notes", int(item.get("lots", 0)) * 200))
            for item in seq_manifest
        )
        lot_archive_metadata = [
            {"start": item["start"], "end": item["end"], "file": Path(item["zip"]).name}
            for item in seq_manifest
        ]
    else:
        lot_count = sum(end - start + 1 for start, end, _ in lots)
        catalog_files_from_lots = lot_count * 200
        lot_archive_metadata = [
            {"start": start, "end": end, "file": path.name}
            for start, end, path in lots
        ]

    manifest = {
        "generated_at": now(),
        "type": "historical-catalog-placeholder-archive",
        "consolidated_vault": consolidated.name if consolidated.exists() else None,
        "consolidated_vault_markdown_files": markdown_entry_count(consolidated),
        "lot_archives": lot_archive_metadata,
        "lot_archive_count": len(lot_archive_metadata),
        "lots_count": lot_count,
        "expected_catalog_placeholder_files_from_lots": catalog_files_from_lots,
        "notes_validated_by_this_aggregator": 0,
        "quality_validation": "not_performed_by_archive_aggregator",
        "ledger_included": bool(args.include_ledger and ledger.exists()),
        "ledger_archive": ledger.name if ledger.exists() else "ledger-v1000000-mat8000.sqlite.xz",
    }

    with tarfile.open(fileobj=sys.stdout.buffer, mode="w|") as tar:
        add_bytes(tar, "MERGE-COMPLETO/README.md", f"""# Arquivo consolidado histórico — Knowledge Federation

Gerado em: {manifest['generated_at']}

> Este TAR agrega arquivos de catálogo e materializações históricas. Os números representam registros, lotes e arquivos, não notas válidas. A agregação não executa avaliação editorial nem revisão humana.

## Conteúdo

- `00-vault-consolidado/`: Study Vault com packs estruturais, MOCs, trilhas, playbooks, canvas e auditoria de navegação. Seus arquivos derivados do ledger não são conteúdo validado.
- `10-lotes/`: lotes de arquivos-placeholder gerados a partir do catálogo.
- `90-ledger/`: metadados do checkpoint (`archives/ledger-v1000000-mat8000.sqlite.xz`).
- `99-relatorios/`: índices, manifestos e relatórios históricos.

## Inventário (não é contagem editorial)

```text
Pacotes de lotes: {manifest['lot_archive_count']}
Lotes sequenciais: {manifest['lots_count']}
Arquivos-placeholder esperados nos lotes: {manifest['expected_catalog_placeholder_files_from_lots']}
Arquivos Markdown no Study Vault: {manifest['consolidated_vault_markdown_files']}
Notas aprovadas por este agregador: {manifest['notes_validated_by_this_aggregator']}
Validação de qualidade: {manifest['quality_validation']}
```

## Uso

Extraia este `.tar.xz` para inspecionar os artefatos históricos. Para retomar a redação, utilize notas candidatas auditadas e aguarde aprovação humana; não trate os lotes ou MOCs como prova de qualidade.
""")
        add_bytes(tar, "MERGE-COMPLETO/99-relatorios/manifest-merge-completo.json", json.dumps(manifest, ensure_ascii=False, indent=2))

        if base_path is not None:
            with tarfile.open(base_path, mode="r|*") as base:
                for member in base:
                    if not member.isfile():
                        continue
                    name = member.name
                    if name == "MERGE-COMPLETO/README.md":
                        continue
                    if name.startswith("MERGE-COMPLETO/90-ledger/") or name.startswith("MERGE-COMPLETO/99-relatorios/"):
                        continue
                    if any(name.startswith(pref) for pref in new_lot_prefixes):
                        continue
                    fobj = base.extractfile(member)
                    if fobj is not None:
                        ti = tarfile.TarInfo(name)
                        ti.size = member.size
                        ti.mtime = 0
                        ti.mode = 0o644
                        tar.addfile(ti, fobj)
        else:
            if consolidated.exists():
                add_zip_expanded(tar, consolidated, "MERGE-COMPLETO/00-vault-consolidado")

        for a, b, p in lots:
            prefix = f"MERGE-COMPLETO/10-lotes/{a:04d}-{b:04d}"
            add_zip_expanded(tar, p, prefix)

        latest = ROOT / "archives" / "LATEST-LEDGER.txt"
        if latest.exists():
            add_file(tar, latest, "MERGE-COMPLETO/90-ledger/LATEST-LEDGER.txt")
        if args.include_ledger and ledger.exists():
            add_file(tar, ledger, f"MERGE-COMPLETO/90-ledger/{ledger.name}")

        for d in docs:
            if d.exists():
                add_file(tar, d, f"MERGE-COMPLETO/99-relatorios/{d.name}")

        for rep in sorted((ROOT / "exports" / "reports").glob("*report.md")):
            add_file(tar, rep, f"MERGE-COMPLETO/99-relatorios/reports/{rep.name}")


if __name__ == "__main__":
    main()
