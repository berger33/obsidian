from pathlib import Path
import zipfile, tempfile, shutil
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
    if not archive.exists():
        raise SystemExit(f"Archive não encontrado: {archive}")
    return archive


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
    with zipfile.ZipFile(archive) as z:
        if "knowledge.sqlite" not in z.namelist():
            raise SystemExit(f"knowledge.sqlite ausente em {archive}")
        z.extract("knowledge.sqlite", cache_root)
    marker.write_text(source_sig, encoding="utf-8")
    return db
