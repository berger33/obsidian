#!/usr/bin/env python3
from pathlib import Path
import shutil, zipfile, json
from kf_common import ROOT, now

SRC = ROOT / "study-vault-1m-packs"
OUT = ROOT / "starter-vault-prioritario"
ZIP = ROOT / "archives" / "starter-vault-prioritario.zip"
PACKS = [
    ("ia-agentes", "IA — Agentes"),
    ("ia-rag", "IA — RAG"),
    ("software-backend", "Software — Backend"),
    ("vibe-coding-orquestracao", "Vibe Coding — Orquestração"),
    ("negocio-mvp", "Negócio — MVP"),
]


def copytree_if(src, dst):
    if src.exists():
        shutil.copytree(src, dst, dirs_exist_ok=True)


def all_notes(pack_dir):
    return sorted([p for p in pack_dir.rglob("*.md") if p.name != "README.md"])


def main():
    if not SRC.exists():
        raise SystemExit("study-vault-1m-packs não encontrado")
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "00-Inicio").mkdir(parents=True)
    (OUT / "00-Mapas").mkdir(parents=True)
    (OUT / "10-Study-Packs").mkdir(parents=True)
    (OUT / "20-Trilha-Inicial").mkdir(parents=True)
    (OUT / "_canvas").mkdir(parents=True)
    copytree_if(SRC / ".obsidian", OUT / ".obsidian")

    total = 0
    home = [
        "---",
        "tipo: home",
        "tags: [starter-vault, obsidian, ia, software]",
        "aliases: [Starter Vault Prioritário]",
        "---",
        "# Starter Vault Prioritário",
        "",
        f"Gerado em: {now()}",
        "",
        "Este é um pacote menor para começar rápido, sem extrair o merge completo.",
        "",
        "## Packs incluídos",
        "",
    ]
    nodes = [{"id":"home","type":"file","file":"00-Inicio/Home.md","x":0,"y":0,"width":420,"height":160,"color":"1"}]
    edges = []

    for i, (pack, title) in enumerate(PACKS):
        src_pack = SRC / "10-Study-Packs" / pack
        dst_pack = OUT / "10-Study-Packs" / pack
        if not src_pack.exists():
            continue
        shutil.copytree(src_pack, dst_pack)
        notes = all_notes(dst_pack)
        total += len(notes)
        moc_name = f"MOC-{pack}"
        home.append(f"- [[{moc_name}]] — {title} ({len(notes)} notas)")
        moc = [
            "---",
            "tipo: moc",
            "tags: [moc, starter-vault]",
            f"aliases: [\"{title}\"]",
            "---",
            f"# {title}",
            "",
            f"Pack: `{pack}`",
            f"Notas: **{len(notes)}**",
            "",
            "## Notas",
            "",
        ]
        moc += [f"- [[{n.stem}]]" for n in notes]
        (OUT / "00-Mapas" / f"{moc_name}.md").write_text("\n".join(moc) + "\n", encoding="utf-8")
        nid = f"pack-{i}"
        nodes.append({"id": nid, "type":"file", "file": f"00-Mapas/{moc_name}.md", "x": (i-2)*460, "y": 280, "width": 420, "height": 130, "color": str((i%6)+1)})
        edges.append({"id": f"e-{i}", "fromNode":"home", "toNode": nid})

    trilha = """---
tipo: trilha
tags: [trilha, starter-vault]
aliases: [Trilha Inicial]
---
# Trilha Inicial

## Ordem recomendada

1. [[MOC-ia-agentes]]
2. [[MOC-ia-rag]]
3. [[MOC-software-backend]]
4. [[MOC-vibe-coding-orquestracao]]
5. [[MOC-negocio-mvp]]

## Como estudar

- Leia 10 notas por dia.
- Para cada nota útil, escreva uma pergunta prática.
- Transforme a pergunta em tarefa, teste ou decisão.
- Verifique fontes primárias antes de decisões críticas.
"""
    (OUT / "20-Trilha-Inicial" / "Trilha-Inicial.md").write_text(trilha, encoding="utf-8")
    home += [
        "",
        f"Total de notas: **{total}**.",
        "",
        "## Comece aqui",
        "",
        "- [[Trilha-Inicial]]",
        "- Abra também `_canvas/Mapa-Starter.canvas`.",
        "",
    ]
    (OUT / "00-Inicio" / "Home.md").write_text("\n".join(home), encoding="utf-8")
    (OUT / "README.md").write_text(f"# Starter Vault Prioritário\n\nNotas: {total}\n\nAbra `00-Inicio/Home.md` no Obsidian.\n", encoding="utf-8")
    (OUT / "_canvas" / "Mapa-Starter.canvas").write_text(json.dumps({"nodes": nodes, "edges": edges}, ensure_ascii=False, indent=2), encoding="utf-8")

    if ZIP.exists():
        ZIP.unlink()
    with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for f in OUT.rglob("*"):
            if f.is_file():
                z.write(f, f.relative_to(ROOT))
    print(f"Starter vault: {OUT}")
    print(f"Zip: {ZIP}")
    print(f"Notas: {total}")

if __name__ == "__main__":
    main()
