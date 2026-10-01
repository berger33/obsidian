from __future__ import annotations
from pathlib import Path
import json, sqlite3, hashlib, re, os, datetime

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config" / "taxonomy.json"
REGISTRY = ROOT / "registry"
DB = REGISTRY / "knowledge.sqlite"
TODAY = "2026-09-30"

TRANSLATE = str.maketrans("áàâãäéèêëíìîïóòôõöúùûüçñÁÀÂÃÄÉÈÊËÍÌÎÏÓÒÔÕÖÚÙÛÜÇÑ", "aaaaaeeeeiiiiooooouuuucnAAAAAEEEEIIIIOOOOOUUUUCN")

def now():
    return datetime.datetime.now().isoformat(timespec="seconds")

def load_config():
    return json.loads(CONFIG.read_text(encoding="utf-8"))

def slugify(text: str, max_len: int = 96) -> str:
    s = text.translate(TRANSLATE)
    s = re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-")
    return (s[:max_len].strip("-") or "nota").lower()

def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def connect():
    REGISTRY.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    init_db(con)
    return con

def init_db(con):
    con.executescript("""
    CREATE TABLE IF NOT EXISTS batches (
      batch_id TEXT PRIMARY KEY,
      domain TEXT NOT NULL,
      subdomain TEXT NOT NULL,
      vault TEXT NOT NULL,
      planned_count INTEGER NOT NULL,
      generated_count INTEGER DEFAULT 0,
      status TEXT NOT NULL,
      created_at TEXT NOT NULL,
      updated_at TEXT NOT NULL,
      manifest_path TEXT,
      audit_path TEXT,
      notes_zip TEXT
    );
    CREATE TABLE IF NOT EXISTS notes (
      id TEXT PRIMARY KEY,
      slug TEXT NOT NULL,
      title TEXT NOT NULL,
      domain TEXT NOT NULL,
      subdomain TEXT NOT NULL,
      type TEXT NOT NULL,
      level TEXT NOT NULL,
      status TEXT NOT NULL,
      batch_id TEXT NOT NULL,
      vault TEXT NOT NULL,
      path TEXT,
      content_hash TEXT,
      risk_legal TEXT DEFAULT 'baixo',
      risk_medical TEXT DEFAULT 'baixo',
      operational_content INTEGER DEFAULT 0,
      created_at TEXT NOT NULL,
      updated_at TEXT NOT NULL
    );
    CREATE INDEX IF NOT EXISTS idx_notes_domain ON notes(domain, subdomain);
    CREATE INDEX IF NOT EXISTS idx_notes_batch ON notes(batch_id);
    CREATE UNIQUE INDEX IF NOT EXISTS idx_notes_slug_vault ON notes(vault, slug);
    CREATE TABLE IF NOT EXISTS sources (
      id TEXT PRIMARY KEY,
      url TEXT NOT NULL,
      title TEXT,
      level TEXT,
      domain TEXT,
      accessed_at TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS links (
      from_id TEXT NOT NULL,
      to_id TEXT NOT NULL,
      batch_id TEXT NOT NULL,
      PRIMARY KEY(from_id, to_id)
    );
    """)
    con.commit()

def write_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def vault_for(domain: str, index: int = 1) -> str:
    return f"{slugify(domain)}-{index:04d}"

def batch_state_path(batch_id: str) -> Path:
    return ROOT / "registry" / f"{batch_id}.state.json"

def manifest_path(batch_id: str) -> Path:
    return ROOT / "registry" / f"{batch_id}.manifest.json"

def audit_path(batch_id: str) -> Path:
    return ROOT / "exports" / "reports" / f"{batch_id}.audit.md"

def note_dir(vault: str, domain: str, subdomain: str) -> Path:
    return ROOT / "domains" / vault / domain / subdomain

def ensure_home_vault():
    home = ROOT / "00-home-vault"
    home.mkdir(parents=True, exist_ok=True)
    (home / "Home.md").write_text("# Home — Knowledge Federation\n\nUse os índices gerados para navegar pelos sub-vaults.\n", encoding="utf-8")
