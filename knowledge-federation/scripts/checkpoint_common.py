from pathlib import Path
import zipfile, lzma, tempfile, shutil
from kf_common import ROOT


def latest_ledger_archive():
    latest = ROOT / "archives" / "LATEST-LEDGER.txt"
    if not latest.exists():
        raise SystemExit("archives/LATEST-LEDGER.txt não encontrado")
    data = {}
    for line in latest.read_text(encoding="utf-8").splitlines():
        if "=" in line:
            k, v = line.split("=", 1)
            data[k.strip()] = v.strip()
    name = data.get("archive")
    if not name:
        raise SystemExit("Campo archive ausente em LATEST-LEDGER.txt")
    archive = ROOT / "archives" / name
    if archive.exists():
        return archive
    # Fallback para formatos alternativos ou pasta reconstructed
    candidates = [
        ROOT / "archives" / "reconstructed" / name,
        ROOT / "archives" / "ledger-v1000000-mat8000.sqlite.xz",
        ROOT / "archives" / "ledger-v1000000-mat8000.zip",
        ROOT / "archives" / "reconstructed" / "ledger-v1000000-mat8000.sqlite.xz",
        ROOT / "archives" / "reconstructed" / "ledger-v1000000-mat8000.zip",
    ]
    for c in candidates:
        if c.exists():
            return c
    raise SystemExit(f"Archive não encontrado: {archive}")


def extract_sqlite_archive(archive: Path, dest_db: Path):
    dest_db.parent.mkdir(parents=True, exist_ok=True)
    if archive.name.endswith(".sqlite.xz") or archive.name.endswith(".xz"):
        with lzma.open(archive, "rb") as src, dest_db.open("wb") as dst:
            shutil.copyfileobj(src, dst, length=1024 * 1024)
    elif archive.name.endswith(".zip"):
        with zipfile.ZipFile(archive) as z:
            if "knowledge.sqlite" not in z.namelist():
                raise SystemExit(f"knowledge.sqlite ausente em {archive}")
            tmp_dir = dest_db.parent / "_tmp_extract"
            tmp_dir.mkdir(parents=True, exist_ok=True)
            z.extract("knowledge.sqlite", tmp_dir)
            shutil.move(str(tmp_dir / "knowledge.sqlite"), str(dest_db))
            shutil.rmtree(tmp_dir, ignore_errors=True)
    else:
        raise SystemExit(f"Formato de archive não suportado: {archive}")


def cached_sqlite_from_archive(archive=None, force=False):
    archive = Path(archive) if archive else latest_ledger_archive()
    if not archive.exists():
        raise SystemExit(f"Archive não encontrado: {archive}")
    cache_root = Path(tempfile.gettempdir()) / "knowledge-federation-ledger-cache" / archive.stem
    db = cache_root / "knowledge.sqlite"
    marker = cache_root / ".source"
    source_sig = f"{archive.resolve()}::{archive.stat().st_size}::{int(archive.stat().st_mtime)}"
    if force and cache_root.exists():
        shutil.rmtree(cache_root)
    if db.exists() and marker.exists() and marker.read_text(encoding="utf-8") == source_sig:
        return db
    cache_root.mkdir(parents=True, exist_ok=True)
    extract_sqlite_archive(archive, db)
    marker.write_text(source_sig, encoding="utf-8")
    return db
