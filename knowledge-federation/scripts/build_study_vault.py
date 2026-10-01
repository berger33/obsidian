#!/usr/bin/env python3
from pathlib import Path
import shutil, zipfile, json, re
from kf_common import ROOT, slugify, now

PACKS = {
    "ia-agentes": {"title": "IA — Agentes", "domain": "ia", "color": "2"},
    "ia-rag": {"title": "IA — RAG", "domain": "ia", "color": "2"},
    "ia-seguranca": {"title": "IA — Segurança", "domain": "ia", "color": "2"},
    "ia-modelos-locais": {"title": "IA — Modelos Locais", "domain": "ia", "color": "2"},
    "ia-avaliacao": {"title": "IA — Avaliação", "domain": "ia", "color": "2"},
    "software-backend": {"title": "Software — Backend", "domain": "software", "color": "3"},
    "software-arquitetura": {"title": "Software — Arquitetura", "domain": "software", "color": "3"},
    "software-devops": {"title": "Software — DevOps", "domain": "software", "color": "3"},
    "software-testes": {"title": "Software — Testes", "domain": "software", "color": "3"},
    "software-frontend": {"title": "Software — Frontend", "domain": "software", "color": "3"},
    "vibe-coding-orquestracao": {"title": "Vibe Coding — Orquestração", "domain": "vibe-coding", "color": "4"},
    "vibe-coding-context-engineering": {"title": "Vibe Coding — Context Engineering", "domain": "vibe-coding", "color": "4"},
    "vibe-coding-qualidade": {"title": "Vibe Coding — Qualidade", "domain": "vibe-coding", "color": "4"},
    "jogos-mmo": {"title": "Jogos — MMO", "domain": "jogos", "color": "5"},
    "jogos-2d": {"title": "Jogos — 2D", "domain": "jogos", "color": "5"},
    "jogos-netcode": {"title": "Jogos — Netcode", "domain": "jogos", "color": "5"},
    "jogos-game-design": {"title": "Jogos — Game Design", "domain": "jogos", "color": "5"},
    "cannabis-documentacao-paciente": {"title": "Cannabis Medicinal — Documentação do Paciente", "domain": "cannabis-medicinal", "color": "6"},
    "cannabis-estudos-clinicos": {"title": "Cannabis Medicinal — Estudos Clínicos", "domain": "cannabis-medicinal", "color": "6"},
    "cannabis-qualidade-rastreabilidade": {"title": "Cannabis Medicinal — Qualidade e Rastreabilidade", "domain": "cannabis-medicinal", "color": "6"},
    "cannabis-riscos-interacoes": {"title": "Cannabis Medicinal — Riscos e Interações", "domain": "cannabis-medicinal", "color": "6"},
    "micologia-riscos-reducao-danos": {"title": "Micologia — Riscos e Redução de Danos", "domain": "micologia", "color": "1"},
    "micologia-cogumelos-medicinais-legais": {"title": "Micologia — Cogumelos Medicinais Legais", "domain": "micologia", "color": "1"},
    "micologia-taxonomia": {"title": "Micologia — Taxonomia", "domain": "micologia", "color": "1"},
    "negocio-mvp": {"title": "Negócio — MVP", "domain": "negocio-carreira-produto", "color": "3"},
    "negocio-carreira": {"title": "Negócio — Carreira", "domain": "negocio-carreira-produto", "color": "3"},
}
VAULT = ROOT / "study-vault-1m-packs"
SRC = ROOT / "checkpoint-materialized"
ZIP = ROOT / "archives" / "study-vault-1m-packs.zip"

FM_RE = re.compile(r"^---\n(.*?)\n---\n#\s*(.*)$", re.S)

def all_md(folder):
    return sorted([p for p in folder.rglob("*.md") if p.name != "README.md"])

def count_pack(folder):
    return len(all_md(folder))

def rel_from_vault(p):
    return p.relative_to(VAULT).as_posix()

def main():
    if VAULT.exists():
        shutil.rmtree(VAULT)
    (VAULT / "00-Inicio").mkdir(parents=True, exist_ok=True)
    (VAULT / "00-Mapas").mkdir(parents=True, exist_ok=True)
    (VAULT / "_canvas").mkdir(parents=True, exist_ok=True)
    (VAULT / ".obsidian").mkdir(parents=True, exist_ok=True)

    copied = []
    for pack, meta in PACKS.items():
        src = SRC / pack
        if not src.exists():
            continue
        dst = VAULT / "10-Study-Packs" / pack
        shutil.copytree(src, dst)
        copied.append((pack, meta, dst))

    # MOCs
    home_lines = [
        "---",
        "tipo: moc",
        "dominio: home",
        "tags: [home, study-pack, ledger-1m]",
        "aliases: [Home, Study Vault 1M]",
        "---",
        "# Home — Study Vault do Ledger de 1M",
        "",
        "Este vault é um recorte materializado do ledger de **1.000.000 notas lógicas**. Ele não contém o ledger inteiro: contém study packs pequenos para estudar no Obsidian.",
        "",
        f"Gerado em: {now()}",
        "",
        "## Study packs",
        "",
    ]
    total = 0
    for pack, meta, dst in copied:
        n = count_pack(dst); total += n
        moc_name = f"MOC-{slugify(pack)}"
        home_lines.append(f"- [[{moc_name}]] — {meta['title']} ({n} notas)")
        notes = all_md(dst)
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
            f"Notas: **{n}**",
            "",
            "## Notas",
            "",
        ]
        for note in notes:
            lines.append(f"- [[{note.stem}]]")
        lines += [
            "",
            "## Como usar",
            "",
            "1. Leia as notas em sequência quando quiser panorama.",
            "2. Use backlinks e Graph View para navegar por relações locais.",
            "3. Quando encontrar uma nota útil, expanda com fontes primárias e contexto do seu projeto.",
        ]
        (VAULT / "00-Mapas" / f"{moc_name}.md").write_text("\n".join(lines)+"\n", encoding="utf-8")

    home_lines += [
        "",
        f"Total materializado neste vault: **{total} notas**.",
        "",
        "## Mapas visuais",
        "",
        "- Abra `_canvas/Mapa-Geral.canvas` no Obsidian Canvas.",
        "- Use o Graph View com cores por domínio já configuradas em `.obsidian/graph.json`.",
        "",
        "## Ledger completo",
        "",
        "O ledger completo está em `../archives/ledger-v1000000-mat8000.zip` no projeto original. Para consultar ou materializar novos recortes, use os scripts em `../scripts/`.",
    ]
    (VAULT / "00-Inicio" / "Home.md").write_text("\n".join(home_lines)+"\n", encoding="utf-8")

    # README
    (VAULT / "README.md").write_text("\n".join([
        "# Study Vault — Ledger 1M",
        "",
        "Abra esta pasta no Obsidian. Comece por `00-Inicio/Home.md`.",
        "",
        f"Notas materializadas: {total}",
        "",
        "Este vault é um recorte; o ledger completo permanece compactado no projeto `knowledge-federation`.",
    ])+"\n", encoding="utf-8")

    # Canvas
    nodes=[]; edges=[]
    nodes.append({"id":"home","type":"file","file":"00-Inicio/Home.md","x":0,"y":0,"width":360,"height":140,"color":"1"})
    for i,(pack,meta,dst) in enumerate(copied):
        x = ((i % 3)-1)*520
        y = (i//3 + 1)*280
        nid=f"pack-{i}"
        nodes.append({"id":nid,"type":"file","file":f"00-Mapas/MOC-{slugify(pack)}.md","x":x,"y":y,"width":420,"height":130,"color":meta['color']})
        edges.append({"id":f"e-{i}","fromNode":"home","toNode":nid})
    (VAULT / "_canvas" / "Mapa-Geral.canvas").write_text(json.dumps({"nodes":nodes,"edges":edges}, ensure_ascii=False, indent=2), encoding="utf-8")

    # Obsidian graph config
    colors = [
        ("tag:#dominio/software", 3447003),
        ("tag:#dominio/ia", 10181046),
        ("tag:#dominio/vibe-coding", 16755200),
        ("tag:#dominio/jogos", 3066993),
        ("tag:#dominio/cannabis-medicinal", 15105570),
        ("tag:#dominio/micologia", 10038562),
        ("tag:#moc", 16737792),
    ]
    graph = {"showTags": True, "showAttachments": False, "hideUnresolved": False, "showOrphans": True, "colorGroups":[{"query":q,"color":{"a":1,"rgb":c}} for q,c in colors], "nodeSizeMultiplier": 1.15, "lineSizeMultiplier": 1.0, "linkDistance": 220}
    (VAULT / ".obsidian" / "graph.json").write_text(json.dumps(graph, ensure_ascii=False, indent=2), encoding="utf-8")
    (VAULT / ".obsidian" / "app.json").write_text(json.dumps({"readableLineLength": True}, indent=2), encoding="utf-8")

    # Zip
    if ZIP.exists(): ZIP.unlink()
    ZIP.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for f in VAULT.rglob("*"):
            if f.is_file():
                z.write(f, f.relative_to(ROOT))
    print(f"Vault: {VAULT}")
    print(f"Zip: {ZIP}")
    print(f"Notas: {total}")

if __name__ == "__main__":
    main()
