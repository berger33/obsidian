#!/usr/bin/env python3
from pathlib import Path
import argparse, shutil, json, zipfile
from kf_common import ROOT, slugify, now

VAULT = ROOT / "study-vault-1m-packs"
SRC = ROOT / "checkpoint-materialized"
ZIP = ROOT / "archives" / "study-vault-1m-packs.zip"

PACKS = {
    "software-apis": {"title": "Software — APIs", "domain": "software", "color": "3"},
    "software-dados": {"title": "Software — Dados", "domain": "software", "color": "3"},
    "software-seguranca": {"title": "Software — Segurança", "domain": "software", "color": "3"},
    "ia-ferramentas": {"title": "IA — Ferramentas", "domain": "ia", "color": "2"},
    "ia-custos": {"title": "IA — Custos", "domain": "ia", "color": "2"},
    "vibe-coding-prompts": {"title": "Vibe Coding — Prompts", "domain": "vibe-coding", "color": "4"},
    "vibe-coding-workflows": {"title": "Vibe Coding — Workflows", "domain": "vibe-coding", "color": "4"},
    "jogos-engines": {"title": "Jogos — Engines", "domain": "jogos", "color": "5"},
    "negocio-portfolio": {"title": "Negócio — Portfólio", "domain": "negocio-carreira-produto", "color": "3"},
    "negocio-validacao": {"title": "Negócio — Validação", "domain": "negocio-carreira-produto", "color": "3"},
}


def all_md(folder):
    return sorted([p for p in folder.rglob("*.md") if p.name != "README.md"])


def zip_vault():
    if ZIP.exists():
        ZIP.unlink()
    with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for f in VAULT.rglob("*"):
            if f.is_file():
                z.write(f, f.relative_to(ROOT))


def main():
    ap = argparse.ArgumentParser(description="Acrescenta packs já materializados em checkpoint-materialized ao Study Vault.")
    ap.add_argument("packs", nargs="*", default=list(PACKS), help="IDs dos packs; default = próximos 10 lotes")
    ap.add_argument("--prune-source", action="store_true")
    args = ap.parse_args()
    if not VAULT.exists():
        raise SystemExit("Vault não existe; rode build_study_vault.py primeiro.")

    added = []
    for pack in args.packs:
        meta = PACKS.get(pack)
        if not meta:
            raise SystemExit(f"Pack desconhecido no manifest do script: {pack}")
        src = SRC / pack
        if not src.exists():
            raise SystemExit(f"Pasta materializada ausente: {src}")
        dst = VAULT / "10-Study-Packs" / pack
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        notes = all_md(dst)
        moc_name = f"MOC-{slugify(pack)}"
        lines = [
            "---",
            "tipo: moc",
            f"dominio: {meta['domain']}",
            "tags: [moc, study-pack, ledger-1m]",
            f"aliases: [\"{meta['title']}\"]",
            "---",
            f"# {meta['title']}",
            "",
            f"Pacote: `{pack}`",
            f"Notas: **{len(notes)}**",
            "",
            "## Notas",
            "",
        ]
        lines += [f"- [[{note.stem}]]" for note in notes]
        lines += ["", "## Como usar", "", "1. Leia por blocos de 10 notas.", "2. Converta notas úteis em perguntas, checklists e experimentos.", "3. Verifique fontes primárias antes de decisões críticas."]
        (VAULT / "00-Mapas" / f"{moc_name}.md").write_text("\n".join(lines)+"\n", encoding="utf-8")
        added.append((pack, meta, len(notes)))

    home = VAULT / "00-Inicio" / "Home.md"
    text = home.read_text(encoding="utf-8")
    for pack, meta, n in added:
        moc_name = f"MOC-{slugify(pack)}"
        line = f"- [[{moc_name}]] — {meta['title']} ({n} notas)"
        if line not in text:
            marker = "\nTotal materializado neste vault:"
            text = text.replace(marker, "\n" + line + "\n" + marker)
    total_notes = len([p for p in (VAULT / "10-Study-Packs").rglob("*.md") if p.name != "README.md"])
    import re
    text = re.sub(r"Total materializado neste vault: \*\*\d+ notas\*\*\.", f"Total materializado neste vault: **{total_notes} notas**.", text)
    home.write_text(text, encoding="utf-8")

    # Regenera canvas geral com todos os MOCs listados.
    mocs = sorted((VAULT / "00-Mapas").glob("MOC-*.md"))
    nodes = [{"id":"home","type":"file","file":"00-Inicio/Home.md","x":0,"y":0,"width":360,"height":140,"color":"1"}]
    edges = []
    for i,moc in enumerate(mocs):
        nid=f"pack-{i}"
        color=str((i % 6)+1)
        nodes.append({"id":nid,"type":"file","file":f"00-Mapas/{moc.name}","x":((i % 4)-1.5)*500,"y":280+(i//4)*240,"width":420,"height":130,"color":color})
        edges.append({"id":f"e-{i}","fromNode":"home","toNode":nid})
    (VAULT / "_canvas" / "Mapa-Geral.canvas").write_text(json.dumps({"nodes":nodes,"edges":edges}, ensure_ascii=False, indent=2), encoding="utf-8")

    readme = VAULT / "README.md"
    r = readme.read_text(encoding="utf-8") if readme.exists() else "# Study Vault — Ledger 1M\n"
    r = re.sub(r"Notas materializadas: \d+", f"Notas materializadas: {total_notes}", r)
    readme.write_text(r, encoding="utf-8")

    zip_vault()
    if args.prune_source:
        shutil.rmtree(SRC, ignore_errors=True)
    print(f"Packs adicionados: {len(added)}")
    print(f"Notas totais no vault: {total_notes}")
    print(f"Zip: {ZIP}")

if __name__ == "__main__":
    main()
