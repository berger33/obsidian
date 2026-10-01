#!/usr/bin/env python3
import json, re, shutil, sqlite3, tempfile, zipfile
from pathlib import Path
from checkpoint_common import cached_sqlite_from_archive
from kf_common import ROOT, TODAY, slugify, now
from materialize_from_checkpoint import render as render_pack_note
from enhance_study_vault import TRILHAS, PLAYBOOKS

# Mapeamento completo dos 78 subdomínios da taxonomia para os 78 study packs
ALL_78_PACKS = [
    # Software (16)
    ("software-fundamentos", "software", "fundamentos", "Software — Fundamentos", "3", "study-pack-software-fundamentos.zip"),
    ("software-arquitetura", "software", "arquitetura", "Software — Arquitetura", "3", "study-pack-software-arquitetura.zip"),
    ("software-frontend", "software", "frontend", "Software — Frontend", "3", "study-pack-software-frontend.zip"),
    ("software-backend", "software", "backend", "Software — Backend", "3", "study-pack-software-backend.zip"),
    ("software-mobile", "software", "mobile", "Software — Mobile", "3", "study-pack-software-mobile.zip"),
    ("software-desktop", "software", "desktop", "Software — Desktop", "3", "study-pack-software-desktop.zip"),
    ("software-dados", "software", "dados", "Software — Dados", "3", "study-pack-software-dados.zip"),
    ("software-devops", "software", "devops", "Software — DevOps", "3", "study-pack-software-devops.zip"),
    ("software-seguranca", "software", "seguranca", "Software — Segurança", "3", "study-pack-software-seguranca.zip"),
    ("software-testes", "software", "testes", "Software — Testes", "3", "study-pack-software-testes.zip"),
    ("software-produto", "software", "produto", "Software — Produto", "3", "study-pack-software-produto.zip"),
    ("software-jogos", "software", "jogos", "Software — Jogos (Engenharia)", "3", "study-pack-software-jogos.zip"),
    ("software-sistemas-empresariais", "software", "sistemas-empresariais", "Software — Sistemas Empresariais", "3", "study-pack-software-sistemas-empresariais.zip"),
    ("software-low-code", "software", "low-code", "Software — Low-Code", "3", "study-pack-software-low-code.zip"),
    ("software-automacao", "software", "automacao", "Software — Automação", "3", "study-pack-software-automacao.zip"),
    ("software-apis", "software", "apis", "Software — APIs", "3", "study-pack-software-apis.zip"),
    # IA (12)
    ("ia-fundamentos", "ia", "fundamentos", "IA — Fundamentos", "2", "study-pack-ia-fundamentos.zip"),
    ("ia-llms", "ia", "llms", "IA — LLMs", "2", "study-pack-ia-llms.zip"),
    ("ia-agentes", "ia", "agentes", "IA — Agentes", "2", "study-pack-ia-agentes-from-1m.zip"),
    ("ia-rag", "ia", "rag", "IA — RAG", "2", "study-pack-ia-rag.zip"),
    ("ia-fine-tuning", "ia", "fine-tuning", "IA — Fine-Tuning", "2", "study-pack-ia-fine-tuning.zip"),
    ("ia-modelos-locais", "ia", "modelos-locais", "IA — Modelos Locais", "2", "study-pack-ia-modelos-locais.zip"),
    ("ia-avaliacao", "ia", "avaliacao", "IA — Avaliação", "2", "study-pack-ia-avaliacao.zip"),
    ("ia-seguranca", "ia", "seguranca", "IA — Segurança", "2", "study-pack-ia-seguranca.zip"),
    ("ia-custos", "ia", "custos", "IA — Custos", "2", "study-pack-ia-custos.zip"),
    ("ia-ferramentas", "ia", "ferramentas", "IA — Ferramentas", "2", "study-pack-ia-ferramentas.zip"),
    ("ia-multimodal", "ia", "multimodal", "IA — Multimodal", "2", "study-pack-ia-multimodal.zip"),
    ("ia-mlops", "ia", "mlops", "IA — MLOps", "2", "study-pack-ia-mlops.zip"),
    # Vibe Coding (10)
    ("vibe-coding-conceitos", "vibe-coding", "conceitos", "Vibe Coding — Conceitos", "4", "study-pack-vibe-coding-conceitos.zip"),
    ("vibe-coding-ferramentas", "vibe-coding", "ferramentas", "Vibe Coding — Ferramentas", "4", "study-pack-vibe-coding-ferramentas.zip"),
    ("vibe-coding-workflows", "vibe-coding", "workflows", "Vibe Coding — Workflows", "4", "study-pack-vibe-coding-workflows.zip"),
    ("vibe-coding-prompts", "vibe-coding", "prompts", "Vibe Coding — Prompts", "4", "study-pack-vibe-coding-prompts.zip"),
    ("vibe-coding-context-engineering", "vibe-coding", "context-engineering", "Vibe Coding — Context Engineering", "4", "study-pack-vibe-coding-context-engineering.zip"),
    ("vibe-coding-spec-driven-dev", "vibe-coding", "spec-driven-dev", "Vibe Coding — Spec-Driven Dev", "4", "study-pack-vibe-coding-spec-driven-dev.zip"),
    ("vibe-coding-qualidade", "vibe-coding", "qualidade", "Vibe Coding — Qualidade", "4", "study-pack-vibe-coding-qualidade.zip"),
    ("vibe-coding-riscos", "vibe-coding", "riscos", "Vibe Coding — Riscos", "4", "study-pack-vibe-coding-riscos.zip"),
    ("vibe-coding-estudos", "vibe-coding", "estudos", "Vibe Coding — Estudos", "4", "study-pack-vibe-coding-estudos.zip"),
    ("vibe-coding-orquestracao", "vibe-coding", "orquestracao", "Vibe Coding — Orquestração", "4", "study-pack-vibe-coding-orquestracao.zip"),
    # Jogos (12)
    ("jogos-2d", "jogos", "2d", "Jogos — 2D", "5", "study-pack-jogos-2d.zip"),
    ("jogos-3d", "jogos", "3d", "Jogos — 3D", "5", "study-pack-jogos-3d.zip"),
    ("jogos-engines", "jogos", "engines", "Jogos — Engines", "5", "study-pack-jogos-engines.zip"),
    ("jogos-netcode", "jogos", "netcode", "Jogos — Netcode", "5", "study-pack-jogos-netcode.zip"),
    ("jogos-mmo", "jogos", "mmo", "Jogos — MMO", "5", "study-pack-jogos-mmo.zip"),
    ("jogos-game-design", "jogos", "game-design", "Jogos — Game Design", "5", "study-pack-jogos-game-design.zip"),
    ("jogos-level-design", "jogos", "level-design", "Jogos — Level Design", "5", "study-pack-jogos-level-design.zip"),
    ("jogos-arte", "jogos", "arte", "Jogos — Arte", "5", "study-pack-jogos-arte.zip"),
    ("jogos-audio", "jogos", "audio", "Jogos — Áudio", "5", "study-pack-jogos-audio.zip"),
    ("jogos-ui-ux", "jogos", "ui-ux", "Jogos — UI/UX", "5", "study-pack-jogos-ui-ux.zip"),
    ("jogos-publicacao", "jogos", "publicacao", "Jogos — Publicação", "5", "study-pack-jogos-publicacao.zip"),
    ("jogos-live-ops", "jogos", "live-ops", "Jogos — Live Ops", "5", "study-pack-jogos-live-ops.zip"),
    # Cannabis Medicinal (11)
    ("cannabis-legal-regulatorio", "cannabis-medicinal", "legal-regulatorio", "Cannabis Medicinal — Legal e Regulatório", "6", "study-pack-cannabis-legal-regulatorio.zip"),
    ("cannabis-documentacao-paciente", "cannabis-medicinal", "paciente-documentacao", "Cannabis Medicinal — Documentação do Paciente", "6", "study-pack-cannabis-documentacao-paciente.zip"),
    ("cannabis-botanica-geral", "cannabis-medicinal", "botanica-geral", "Cannabis Medicinal — Botânica Geral", "6", "study-pack-cannabis-botanica-geral.zip"),
    ("cannabis-farmacologia", "cannabis-medicinal", "farmacologia", "Cannabis Medicinal — Farmacologia", "6", "study-pack-cannabis-farmacologia.zip"),
    ("cannabis-canabinoides", "cannabis-medicinal", "canabinoides", "Cannabis Medicinal — Canabinoides", "6", "study-pack-cannabis-canabinoides.zip"),
    ("cannabis-terpenos", "cannabis-medicinal", "terpenos", "Cannabis Medicinal — Terpenos", "6", "study-pack-cannabis-terpenos.zip"),
    ("cannabis-formas-de-uso-legais", "cannabis-medicinal", "formas-de-uso-legais", "Cannabis Medicinal — Formas de Uso Legais", "6", "study-pack-cannabis-formas-de-uso-legais.zip"),
    ("cannabis-riscos-interacoes", "cannabis-medicinal", "riscos-e-interacoes", "Cannabis Medicinal — Riscos e Interações", "6", "study-pack-cannabis-riscos-interacoes.zip"),
    ("cannabis-estudos-clinicos", "cannabis-medicinal", "estudos-clinicos", "Cannabis Medicinal — Estudos Clínicos", "6", "study-pack-cannabis-estudos-clinicos.zip"),
    ("cannabis-qualidade-rastreabilidade", "cannabis-medicinal", "qualidade-e-rastreabilidade", "Cannabis Medicinal — Qualidade e Rastreabilidade", "6", "study-pack-cannabis-qualidade-rastreabilidade.zip"),
    ("cannabis-glossario", "cannabis-medicinal", "glossario", "Cannabis Medicinal — Glossário", "6", "study-pack-cannabis-glossario.zip"),
    # Micologia (9)
    ("micologia-fundamentos", "micologia", "fundamentos", "Micologia — Fundamentos", "1", "study-pack-micologia-fundamentos.zip"),
    ("micologia-taxonomia", "micologia", "taxonomia", "Micologia — Taxonomia", "1", "study-pack-micologia-taxonomia.zip"),
    ("micologia-ecologia", "micologia", "ecologia", "Micologia — Ecologia", "1", "study-pack-micologia-ecologia.zip"),
    ("micologia-cogumelos-comestiveis-legais", "micologia", "cogumelos-comestiveis-legais", "Micologia — Cogumelos Comestíveis Legais", "1", "study-pack-micologia-cogumelos-comestiveis-legais.zip"),
    ("micologia-cogumelos-medicinais-legais", "micologia", "cogumelos-medicinais-legais", "Micologia — Cogumelos Medicinais Legais", "1", "study-pack-micologia-cogumelos-medicinais-legais.zip"),
    ("micologia-psilocybe-historia-taxonomia-legislacao", "micologia", "psilocybe-historia-taxonomia-legislacao", "Micologia — Psilocybe: História, Taxonomia e Legislação", "1", "study-pack-micologia-psilocybe-historia-taxonomia-legislacao.zip"),
    ("micologia-psilocibina-pesquisa-clinica", "micologia", "psilocibina-pesquisa-clinica", "Micologia — Psilocibina: Pesquisa Clínica", "1", "study-pack-micologia-psilocibina-pesquisa-clinica.zip"),
    ("micologia-riscos-reducao-danos", "micologia", "riscos-e-reducao-de-danos", "Micologia — Riscos e Redução de Danos", "1", "study-pack-micologia-riscos-reducao-danos.zip"),
    ("micologia-glossario", "micologia", "glossario", "Micologia — Glossário", "1", "study-pack-micologia-glossario.zip"),
    # Negócio, Carreira e Produto (8)
    ("negocio-mvp", "negocio-carreira-produto", "mvp", "Negócio — MVP", "3", "study-pack-negocio-mvp.zip"),
    ("negocio-validacao", "negocio-carreira-produto", "validacao", "Negócio — Validação", "3", "study-pack-negocio-validacao.zip"),
    ("negocio-monetizacao", "negocio-carreira-produto", "monetizacao", "Negócio — Monetização", "3", "study-pack-negocio-monetizacao.zip"),
    ("negocio-portfolio", "negocio-carreira-produto", "portfolio", "Negócio — Portfólio", "3", "study-pack-negocio-portfolio.zip"),
    ("negocio-carreira", "negocio-carreira-produto", "carreira", "Negócio — Carreira", "3", "study-pack-negocio-carreira.zip"),
    ("negocio-mercado", "negocio-carreira-produto", "mercado", "Negócio — Mercado", "3", "study-pack-negocio-mercado.zip"),
    ("negocio-distribuicao", "negocio-carreira-produto", "distribuicao", "Negócio — Distribuição", "3", "study-pack-negocio-distribuicao.zip"),
    ("negocio-produto", "negocio-carreira-produto", "produto", "Negócio — Produto", "3", "study-pack-negocio-produto.zip"),
]

DOMAIN_TITLES = {
    "software": "Engenharia de Software",
    "ia": "Inteligência Artificial",
    "vibe-coding": "Vibe Coding e Orquestração Agêntica",
    "jogos": "Desenvolvimento de Jogos",
    "cannabis-medicinal": "Cannabis Medicinal (Educacional e Regulatório)",
    "micologia": "Micologia Segura e Científica",
    "negocio-carreira-produto": "Negócio, Carreira e Produto",
}

LINK_RE = re.compile(r"!??\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]")


def write_curated_note(vault_dir: Path, rel: str, title: str, body: str, tags: list[str]):
    p = vault_dir / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    fm = [
        "---",
        f"id: curado-{slugify(title)}",
        "tipo: guia-curado",
        f"ultima_verificacao: {TODAY}",
        "conteudo_operacional: false",
        f"tags: [{', '.join(tags)}]",
        f"aliases: [\"{title}\"]",
        "---",
        f"# {title}",
        body.strip(),
        "",
    ]
    p.write_text("\n".join(fm), encoding="utf-8")


def main():
    db = cached_sqlite_from_archive()
    con = sqlite3.connect(db)
    con.row_factory = sqlite3.Row

    work = Path(tempfile.gettempdir()) / "kf-build-78-packs"
    if work.exists():
        shutil.rmtree(work)
    vault_dir = work / "study-vault-1m-packs"
    (vault_dir / "00-Inicio").mkdir(parents=True, exist_ok=True)
    (vault_dir / "00-Mapas").mkdir(parents=True, exist_ok=True)
    (vault_dir / "_canvas").mkdir(parents=True, exist_ok=True)
    (vault_dir / ".obsidian").mkdir(parents=True, exist_ok=True)

    archives_dir = ROOT / "archives"
    archives_dir.mkdir(parents=True, exist_ok=True)

    by_domain = {d: [] for d in DOMAIN_TITLES}
    total_notes = 0

    for pack_slug, domain, subdomain, title, color, zip_name in ALL_78_PACKS:
        rows = list(con.execute(
            "SELECT * FROM virtual_notes WHERE domain=? AND subdomain=? ORDER BY domain, subdomain, title LIMIT 200",
            (domain, subdomain),
        ))
        if len(rows) != 200:
            raise SystemExit(f"Subdomínio com menos de 200 notas: {domain}/{subdomain} -> {len(rows)}")

        pack_dst = vault_dir / "10-Study-Packs" / pack_slug
        outdir = pack_dst / domain / subdomain
        outdir.mkdir(parents=True, exist_ok=True)

        note_stems = []
        for idx, row in enumerate(rows):
            related = rows[idx + 1 : idx + 6] + rows[:5]
            note_path = outdir / f"{row['slug']}.md"
            note_path.write_text(render_pack_note(row, related), encoding="utf-8")
            note_stems.append(row["slug"])

        readme = pack_dst / "README.md"
        readme.write_text(
            f"# Recorte materializado do checkpoint\n\nPacote: `{pack_slug}`\nNotas: {len(rows)}\nFiltro: domain={domain}, subdomain={subdomain}\n",
            encoding="utf-8",
        )

        # Só regrava o zip individual se ainda não existir ou se tinha menos de 200 notas (ex.: ia-agentes)
        zpath = archives_dir / zip_name
        need_zip = not zpath.exists() or pack_slug == "ia-agentes"
        if need_zip:
            with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
                for f in sorted(pack_dst.rglob("*")):
                    if f.is_file():
                        arc = Path("checkpoint-materialized") / pack_slug / f.relative_to(pack_dst)
                        zf.write(f, arc.as_posix())

        # Cria MOC do pack
        moc_name = f"MOC-{slugify(pack_slug)}"
        moc_lines = [
            "---",
            "tipo: moc",
            f"dominio: {domain}",
            f"subdominio: {subdomain}",
            "tags: [moc, study-pack, ledger-1m]",
            f"aliases: [\"{title}\"]",
            "---",
            f"# {title}",
            "",
            f"Pacote: `{pack_slug}`",
            f"Domínio: [[MOC-Dominio-{domain}|{DOMAIN_TITLES[domain]}]]",
            f"Subdomínio: `{subdomain}`",
            f"Notas: **{len(note_stems)}**",
            "",
            "## Notas",
            "",
        ]
        moc_lines += [f"- [[{stem}]]" for stem in sorted(note_stems)]
        moc_lines += [
            "",
            "## Como usar",
            "",
            "1. Leia as notas por blocos de 10 para construir visão panorâmica.",
            "2. Use backlinks e Graph View para explorar conexões locais.",
            "3. Verifique fontes primárias antes de tomar decisões críticas.",
        ]
        (vault_dir / "00-Mapas" / f"{moc_name}.md").write_text("\n".join(moc_lines) + "\n", encoding="utf-8")

        by_domain[domain].append((pack_slug, subdomain, title, color, moc_name, len(note_stems), zip_name))
        total_notes += len(note_stems)

    # Cria MOCs por Domínio + Canvases por Domínio
    for domain, packs in by_domain.items():
        dom_title = DOMAIN_TITLES[domain]
        dom_moc = f"MOC-Dominio-{domain}"
        dom_notes = sum(p[5] for p in packs)
        dlines = [
            "---",
            "tipo: moc-dominio",
            f"dominio: {domain}",
            "tags: [moc, moc-dominio, ledger-1m]",
            f"aliases: [\"{dom_title}\"]",
            "---",
            f"# {dom_title} — Mapa de Subdomínios",
            "",
            f"Domínio: `{domain}`",
            f"Subdomínios / Study Packs: **{len(packs)}**",
            f"Notas curadas neste domínio: **{dom_notes}**",
            "",
            "## Study Packs do Domínio",
            "",
        ]
        cnodes = [{"id": "dom", "type": "file", "file": f"00-Mapas/{dom_moc}.md", "x": 0, "y": 0, "width": 420, "height": 150, "color": packs[0][3]}]
        cedges = []
        for idx, (pack_slug, subdomain, title, color, moc_name, n_count, zip_name) in enumerate(packs):
            dlines.append(f"- [[{moc_name}]] — {title} ({n_count} notas) — `{zip_name}`")
            nid = f"sub-{idx}"
            cnodes.append({
                "id": nid,
                "type": "file",
                "file": f"00-Mapas/{moc_name}.md",
                "x": ((idx % 4) - 1.5) * 480,
                "y": 260 + (idx // 4) * 220,
                "width": 420,
                "height": 130,
                "color": color,
            })
            cedges.append({"id": f"e-{idx}", "fromNode": "dom", "toNode": nid})
        dlines += [
            "",
            "## Navegação",
            "",
            "- Voltar para [[Home]]",
            f"- Abrir Canvas do domínio: `_canvas/Mapa-{domain}.canvas`",
        ]
        (vault_dir / "00-Mapas" / f"{dom_moc}.md").write_text("\n".join(dlines) + "\n", encoding="utf-8")
        (vault_dir / "_canvas" / f"Mapa-{domain}.canvas").write_text(
            json.dumps({"nodes": cnodes, "edges": cedges}, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    # Adiciona Trilhas e Playbooks curados
    for rel, (title, body, tags) in {**TRILHAS, **PLAYBOOKS}.items():
        write_curated_note(vault_dir, rel, title, body, tags)

    # Home.md completo
    home_lines = [
        "---",
        "tipo: moc",
        "dominio: home",
        "tags: [home, study-pack, ledger-1m]",
        "aliases: [Home, Study Vault 1M]",
        "---",
        "# Home — Study Vault Completo (78 Subdomínios / 15.600 Notas)",
        "",
        "Este vault contém os **78 study packs temáticos** (100% dos subdomínios da taxonomia, com **200 notas por subdomínio = 15.600 notas curadas**), derivados do ledger de **1.000.000 de notas lógicas**.",
        "",
        f"Gerado em: {now()}",
        "",
        "## Mapas por Domínio (7 Domínios / 78 Subdomínios)",
        "",
    ]
    for domain, packs in by_domain.items():
        home_lines.append(f"- [[MOC-Dominio-{domain}|{DOMAIN_TITLES[domain]}]] — {len(packs)} packs ({sum(p[5] for p in packs)} notas)")

    home_lines += [
        "",
        "## Trilhas guiadas",
        "",
        "- [[Trilha-Orquestrador-de-IA]]",
        "- [[Trilha-Fullstack-com-IA]]",
        "- [[Trilha-Jogos-2D-Online-MMO]]",
        "- [[Trilha-Produto-Carreira-MVP]]",
        "- [[Trilha-Ciencias-Reguladas-Seguras]]",
        "",
        "## Playbooks e matrizes de decisão",
        "",
        "- [[Como-Estudar-Um-Pack|Playbook — Como estudar um pack]]",
        "- [[Como-Materializar-Novos-Recortes|Playbook — Como materializar novos recortes]]",
        "- [[Checklist-Fontes-e-Volatilidade|Checklist — Fontes e Volatilidade]]",
        "- [[Matriz-Ferramentas-IA-Dev|Matriz — Ferramentas de IA para Desenvolvimento]]",
        "- [[Matriz-Engine-Jogos|Matriz — Engine para Jogos]]",
        "- [[Perguntas-Para-Profissionais-Regulados|Perguntas para profissionais em domínios regulados]]",
        "",
        "## Todos os 78 Study Packs por Subdomínio",
        "",
    ]
    for pack_slug, domain, subdomain, title, color, zip_name in ALL_78_PACKS:
        moc_name = f"MOC-{slugify(pack_slug)}"
        home_lines.append(f"- [[{moc_name}]] — {title} (200 notas)")

    home_lines += [
        "",
        f"Total materializado neste vault: **{total_notes} notas** em **{len(ALL_78_PACKS)} study packs**.",
        "",
        "## Mapas visuais (Obsidian Canvas)",
        "",
        "- `_canvas/Mapa-Geral.canvas` (visão geral dos 7 domínios e 78 packs)",
        "- `_canvas/Trilhas-e-Playbooks.canvas` (trilhas guiadas e matrizes de decisão)",
        "- `_canvas/Mapa-software.canvas`",
        "- `_canvas/Mapa-ia.canvas`",
        "- `_canvas/Mapa-vibe-coding.canvas`",
        "- `_canvas/Mapa-jogos.canvas`",
        "- `_canvas/Mapa-cannabis-medicinal.canvas`",
        "- `_canvas/Mapa-micologia.canvas`",
        "- `_canvas/Mapa-negocio-carreira-produto.canvas`",
    ]
    (vault_dir / "00-Inicio" / "Home.md").write_text("\n".join(home_lines) + "\n", encoding="utf-8")

    (vault_dir / "README.md").write_text("\n".join([
        "# Study Vault — Ledger 1M (78 Study Packs Completos)",
        "",
        "Abra esta pasta no Obsidian. Comece por `00-Inicio/Home.md`.",
        "",
        f"Notas materializadas em packs: {total_notes}",
        f"Study packs (100% dos subdomínios): {len(ALL_78_PACKS)}",
        "",
        "Este vault consolida todos os 78 subdomínios da federação de 1 milhão de notas.",
    ]) + "\n", encoding="utf-8")

    # Canvas Geral e Canvas de Trilhas
    gnodes = [{"id": "home", "type": "file", "file": "00-Inicio/Home.md", "x": 0, "y": 0, "width": 420, "height": 150, "color": "1"}]
    gedges = []
    for d_idx, (domain, packs) in enumerate(by_domain.items()):
        did = f"dom-{d_idx}"
        dx = ((d_idx % 4) - 1.5) * 600
        dy = 280 + (d_idx // 4) * 260
        gnodes.append({
            "id": did,
            "type": "file",
            "file": f"00-Mapas/MOC-Dominio-{domain}.md",
            "x": dx,
            "y": dy,
            "width": 460,
            "height": 140,
            "color": packs[0][3],
        })
        gedges.append({"id": f"ed-{d_idx}", "fromNode": "home", "toNode": did})
    (vault_dir / "_canvas" / "Mapa-Geral.canvas").write_text(
        json.dumps({"nodes": gnodes, "edges": gedges}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    tnodes = [{"id": "home", "type": "file", "file": "00-Inicio/Home.md", "x": 0, "y": 0, "width": 360, "height": 140, "color": "1"}]
    tedges = []
    tfiles = list(TRILHAS.keys()) + list(PLAYBOOKS.keys())
    for i, rel in enumerate(tfiles):
        nid = f"n{i}"
        tnodes.append({
            "id": nid,
            "type": "file",
            "file": rel,
            "x": ((i % 3) - 1) * 560,
            "y": 260 + (i // 3) * 240,
            "width": 460,
            "height": 130,
            "color": str((i % 6) + 1),
        })
        tedges.append({"id": f"e{i}", "fromNode": "home", "toNode": nid})
    (vault_dir / "_canvas" / "Trilhas-e-Playbooks.canvas").write_text(
        json.dumps({"nodes": tnodes, "edges": tedges}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # Config Obsidian Graph
    colors = [
        ("tag:#dominio/software", 3447003),
        ("tag:#dominio/ia", 10181046),
        ("tag:#dominio/vibe-coding", 16755200),
        ("tag:#dominio/jogos", 3066993),
        ("tag:#dominio/cannabis-medicinal", 15105570),
        ("tag:#dominio/micologia", 10038562),
        ("tag:#dominio/negocio-carreira-produto", 5763719),
        ("tag:#moc", 16737792),
    ]
    graph = {
        "showTags": True,
        "showAttachments": False,
        "hideUnresolved": False,
        "showOrphans": True,
        "colorGroups": [{"query": q, "color": {"a": 1, "rgb": c}} for q, c in colors],
        "nodeSizeMultiplier": 1.15,
        "lineSizeMultiplier": 1.0,
        "linkDistance": 220,
    }
    (vault_dir / ".obsidian" / "graph.json").write_text(json.dumps(graph, ensure_ascii=False, indent=2), encoding="utf-8")
    (vault_dir / ".obsidian" / "app.json").write_text(json.dumps({"readableLineLength": True}, indent=2), encoding="utf-8")

    # Auditoria completa de links do vault
    md_files = sorted(vault_dir.rglob("*.md"))
    stems = {p.stem for p in md_files}
    paths = {p.relative_to(vault_dir).as_posix() for p in md_files}
    broken = []
    total_links = 0
    for p in md_files:
        txt = p.read_text(encoding="utf-8", errors="ignore")
        for m in LINK_RE.finditer(txt):
            target = m.group(1).strip()
            total_links += 1
            if target.endswith(".md"):
                ok = target in paths or target.replace(" ", "%20") in paths
            else:
                ok = target in stems
            if not ok:
                broken.append((p.relative_to(vault_dir).as_posix(), target))

    canvas_files = sorted(vault_dir.rglob("*.canvas"))
    audit_lines = [
        "# Auditoria — Study Vault 1M Packs (78 Subdomínios Completos)",
        "",
        f"Gerado em: {now()}",
        "",
        f"Study packs (subdomínios): {len(ALL_78_PACKS)}",
        f"Notas de estudo nos packs: {total_notes}",
        f"Arquivos Markdown totais no vault: {len(md_files)}",
        f"MOCs (78 subdomínios + 7 domínios + Home): 86",
        f"Trilhas e Playbooks: {len(TRILHAS) + len(PLAYBOOKS)}",
        f"Arquivos Canvas: {len(canvas_files)}",
        f"Links wiki analisados: {total_links}",
        f"Links quebrados: {len(broken)}",
        "",
        "Nenhum link quebrado encontrado pela auditoria de wiki links." if not broken else f"Links quebrados encontrados: {len(broken)}",
    ]
    if broken:
        raise SystemExit(f"Links quebrados detectados: {broken[:10]}")

    audit_path = vault_dir / "_meta" / "auditoria-study-vault.md"
    audit_path.parent.mkdir(parents=True, exist_ok=True)
    audit_path.write_text("\n".join(audit_lines) + "\n", encoding="utf-8")
    (ROOT / "exports" / "reports" / "auditoria-study-vault.md").write_text("\n".join(audit_lines) + "\n", encoding="utf-8")

    # Compacta study-vault-1m-packs.zip
    out_zip = archives_dir / "study-vault-1m-packs.zip"
    if out_zip.exists():
        out_zip.unlink()
    with zipfile.ZipFile(out_zip, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for f in sorted(vault_dir.rglob("*")):
            if f.is_file():
                arc = Path("study-vault-1m-packs") / f.relative_to(vault_dir)
                zf.write(f, arc.as_posix())

    shutil.rmtree(work, ignore_errors=True)
    print(f"78 packs built! total_notes={total_notes} md={len(md_files)} canvas={len(canvas_files)} links={total_links} broken={len(broken)} zip_size={out_zip.stat().st_size}")


if __name__ == "__main__":
    main()
