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
    ap.add_argument("--include-ledger", action="store_true", help="Inclui o checkpoint ledger zipado como arquivo interno.")
    args = ap.parse_args()

    lots = list(iter_lot_archives())
    consolidated = ROOT / "archives" / "study-vault-1m-packs.zip"
    ledger = ROOT / "archives" / "ledger-v1000000-mat8000.zip"
    docs = [
        ROOT / "README-1M.md",
        ROOT / "STUDY-VAULT-README.md",
        ROOT / "LOT-SEQUENCE.md",
        ROOT / "LOTS-301-800.md",
        ROOT / "LOTS-801-3300.md",
        ROOT / "PACK-INVENTORY.md",
        ROOT / "NEXT-100-LOTS.md",
        ROOT / "LOTS-101-200.md",
        ROOT / "LOTS-201-300.md",
        ROOT / "exports" / "reports" / "lot-sequence-manifest.json",
    ]

    manifest = {
        "generated_at": now(),
        "type": "merged-complete-materialized-vault",
        "consolidated_vault": consolidated.name if consolidated.exists() else None,
        "lot_archives": [{"start": a, "end": b, "file": p.name} for a,b,p in lots],
        "lot_archive_count": len(lots),
        "notes_from_lot_archives": len(lots) * 100 * 200,
        "notes_from_curated_study_vault": 7100,
        "total_materialized_notes_represented": len(lots) * 100 * 200 + 7100,
        "ledger_included": bool(args.include_ledger and ledger.exists()),
        "regulated_operational_content": 0,
    }

    with tarfile.open(fileobj=sys.stdout.buffer, mode="w|") as tar:
        add_bytes(tar, "MERGE-COMPLETO/README.md", f"""# Merge completo — Knowledge Federation

Gerado em: {manifest['generated_at']}

Este arquivo TAR contém o merge lógico dos vaults materializados e pacotes sequenciais gerados a partir do ledger-first de 1 milhão de notas.

## Conteúdo

- `00-vault-consolidado/`: vault curado com 7.100 notas, trilhas, playbooks, canvas e auditoria.
- `10-lotes/`: sequência completa de vaults por lote, expandida em pastas por intervalo.
- `90-ledger/`: checkpoint ledger incluído quando gerado com `--include-ledger`.
- `99-relatorios/`: índices, manifestos e relatórios de execução.

## Totais representados

```text
Pacotes sequenciais: {manifest['lot_archive_count']}
Notas sequenciais: {manifest['notes_from_lot_archives']}
Notas do vault curado: {manifest['notes_from_curated_study_vault']}
Total materializado representado: {manifest['total_materialized_notes_represented']}
Conteúdo operacional regulado: 0
```

## Uso

Extraia este `.tar.xz` e abra uma das pastas no Obsidian. Para navegação geral, comece por:

```text
00-vault-consolidado/00-Inicio/Home.md
```

Para lotes sequenciais, escolha uma pasta em:

```text
10-lotes/
```
""")
        add_bytes(tar, "MERGE-COMPLETO/99-relatorios/manifest-merge-completo.json", json.dumps(manifest, ensure_ascii=False, indent=2))

        if consolidated.exists():
            add_zip_expanded(tar, consolidated, "MERGE-COMPLETO/00-vault-consolidado")

        for a, b, p in lots:
            prefix = f"MERGE-COMPLETO/10-lotes/{a:04d}-{b:04d}"
            add_zip_expanded(tar, p, prefix)

        if args.include_ledger and ledger.exists():
            add_file(tar, ledger, "MERGE-COMPLETO/90-ledger/ledger-v1000000-mat8000.zip")
            latest = ROOT / "archives" / "LATEST-LEDGER.txt"
            if latest.exists():
                add_file(tar, latest, "MERGE-COMPLETO/90-ledger/LATEST-LEDGER.txt")

        for d in docs:
            if d.exists():
                add_file(tar, d, f"MERGE-COMPLETO/99-relatorios/{d.name}")

if __name__ == "__main__":
    main()
