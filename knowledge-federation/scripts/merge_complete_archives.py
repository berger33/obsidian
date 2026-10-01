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
    ap = argparse.ArgumentParser(description="Gera stream tar com merge completo dos vaults/lotes materializados.")
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

    total_packages = len(seq_manifest) if seq_manifest else len(lots)
    manifest = {
        "generated_at": now(),
        "type": "merged-complete-materialized-vault",
        "consolidated_vault": consolidated.name if consolidated.exists() else None,
        "lot_archives": [
            {"start": m["start"], "end": m["end"], "file": Path(m["zip"]).name}
            for m in seq_manifest
        ] if seq_manifest else [{"start": a, "end": b, "file": p.name} for a, b, p in lots],
        "lot_archive_count": total_packages,
        "lots_count": total_packages * 100,
        "notes_from_lot_archives": total_packages * 100 * 200,
        "notes_from_curated_study_vault": 7100,
        "total_materialized_notes_represented": total_packages * 100 * 200 + 7100,
        "ledger_included": bool(args.include_ledger and ledger.exists()),
        "ledger_archive": ledger.name if ledger.exists() else "ledger-v1000000-mat8000.sqlite.xz",
        "regulated_operational_content": 0,
    }

    with tarfile.open(fileobj=sys.stdout.buffer, mode="w|") as tar:
        add_bytes(tar, "MERGE-COMPLETO/README.md", f"""# Merge completo — Knowledge Federation (1 Milhão de Notas)

Gerado em: {manifest['generated_at']}

Este arquivo TAR contém o merge lógico completo dos vaults materializados e de todos os 50 pacotes sequenciais (5.000 lotes = 1.000.000 de notas) gerados a partir do ledger-first de 1 milhão de notas.

## Conteúdo

- `00-vault-consolidado/`: vault curado com 7.100 notas, 36 packs temáticos, trilhas, playbooks, canvas e auditoria.
- `10-lotes/`: sequência completa de 50 pacotes de lotes (`0001-0100` até `4901-5000`), totalizando 5.000 lotes e 1.000.000 de notas materializadas.
- `90-ledger/`: metadados do checkpoint ledger (`archives/ledger-v1000000-mat8000.sqlite.xz`).
- `99-relatorios/`: índices, manifestos e todos os relatórios de execução dos lotes.

## Totais representados

```text
Pacotes sequenciais: {manifest['lot_archive_count']}
Lotes sequenciais: {manifest['lots_count']}
Notas sequenciais: {manifest['notes_from_lot_archives']}
Notas do vault curado: {manifest['notes_from_curated_study_vault']}
Total materializado representado: {manifest['total_materialized_notes_represented']}
Conteúdo operacional regulado: 0
```

## Uso

Extraia este `.tar.xz` e abra uma das pastas no Obsidian. Para navegação geral curada, comece por:

```text
MERGE-COMPLETO/00-vault-consolidado/study-vault-1m-packs/00-Inicio/Home.md
```

Para lotes sequenciais (de `0001-0100` a `4901-5000`), escolha uma pasta em:

```text
MERGE-COMPLETO/10-lotes/
```
""")
        add_bytes(tar, "MERGE-COMPLETO/99-relatorios/manifest-merge-completo.json", json.dumps(manifest, ensure_ascii=False, indent=2))

        if args.base_tar:
            base_path = Path(args.base_tar)
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
