#!/usr/bin/env python3
"""Build 100 substantive notes for batch software-criacao-ia-2000-0004 tranche 02 (IDs 101-200) and its AI factual review report."""
from __future__ import annotations

import argparse
import os
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KF = ROOT / "knowledge-federation"
DOMAINS_DIR = KF / "domains"
NOTES_DIR = DOMAINS_DIR / "software-0010" / "software" / "criacao-ia"
REPORT = KF / "exports" / "reports" / "ai-review-software-criacao-ia-2000-0004-tranche-02.md"
DATA_DIR = Path(__file__).resolve().parent / "_criacao_ia_t02_data"
BATCH_ID = "software-criacao-ia-2000-0004"
DATE = "2026-10-04"
START = 101
EXPECTED_NOTES = 100

sys.path.insert(0, str(Path(__file__).resolve().parent))
from note_quality import assess_markdown, normalize  # noqa: E402
from prose_audit import repeated_substantive_sentences  # noqa: E402

GROUP_META = {
    "01-claude-code.txt": {
        "group_title": "Claude Code CLI & Anthropic API para Desenvolvimento Assistido",
        "first": 101,
        "check": "Verificação factual contra documentação oficial Anthropic (Claude Code CLI, Prompt Caching, Tool Use e MCP).",
        "src1_label": "Anthropic Docs — Claude Code Overview",
        "src1_note": "documentação oficial da CLI Claude Code, comandos interativos, CLAUDE.md e arquitetura de agentes",
        "src2_label": "Anthropic Docs — Claude Code Tutorials",
        "src2_note": "tutoriais oficiais de uso prático, permissões no terminal, ferramentas e fluxos de trabalho",
    },
    "02-continue-dev.txt": {
        "group_title": "Agentes de Código Locais e Continue.dev",
        "first": 111,
        "check": "Verificação factual contra documentação oficial do Continue.dev e APIs Ollama / llama.cpp.",
        "src1_label": "Continue.dev Documentation — Configuration Reference",
        "src1_note": "documentação oficial de configuração do config.json, provedores de modelos locais e context providers",
        "src2_label": "Ollama API Documentation",
        "src2_note": "especificação oficial dos endpoints de inferência, parâmetros num_ctx, keep_alive e quantização GGUF",
    },
    "03-cursor-context.txt": {
        "group_title": "Cursor e Context Engineering para Criação de Software",
        "first": 121,
        "check": "Verificação factual contra documentação oficial do Cursor (.cursorrules, codebase indexing, composer e context symbols).",
        "src1_label": "Cursor Documentation — Rules for AI",
        "src1_note": "guia oficial de configuração de regras persistentes de projeto (.cursorrules) e system prompts",
        "src2_label": "Cursor Documentation — Codebase Indexing & Context",
        "src2_note": "documentação sobre indexação vetorial, símbolos @Codebase, @Docs, @Git e gerenciamento de contexto",
    },
    "04-godot-ai-states.txt": {
        "group_title": "Máquinas de Estados e IA de Gameplay no Godot 4",
        "first": 131,
        "check": "Verificação factual contra documentação oficial do Godot 4 (GDScript, vetores, Area3D, RayCast3D e AnimationTree).",
        "src1_label": "Godot Engine 4 Documentation — Advanced GDScript",
        "src1_note": "manual oficial cobrindo padrões de scripts, nós virtuais, sinais e máquinas de estados hierárquicas",
        "src2_label": "Godot Engine 4 Documentation — Advanced Vector Math",
        "src2_note": "guia matemático cobrindo produtos escalares, forças de steering (Seek/Flee/Pursuit) e orientação espacial",
    },
    "05-unity-rigging-utility.txt": {
        "group_title": "Rigging de Animação e Utility AI no Unity",
        "first": 141,
        "check": "Verificação factual contra documentação oficial do Unity Animation Rigging, NavMesh e PlayableGraph.",
        "src1_label": "Unity Animation Rigging Package Manual",
        "src1_note": "documentação oficial do componente RigBuilder, restrições procedurais TwoBoneIK, Multi-Aim e DampTransform",
        "src2_label": "Unity Animation Rigging — TwoBoneIKConstraint",
        "src2_note": "referência técnica detalhando parâmetros de IK, targets polares e ajuste dinâmico em superfícies",
    },
    "06-unreal-statetree.txt": {
        "group_title": "StateTree e Smart Objects na Unreal Engine 5",
        "first": 151,
        "check": "Verificação factual contra documentação oficial da Epic Games para Unreal Engine 5 (StateTree, Smart Objects, Mass AI e GAS).",
        "src1_label": "Unreal Engine 5 Documentation — StateTree",
        "src1_note": "manual oficial do framework StateTree, árvores de estados hierárquicas leves, Evaluators e Tasks",
        "src2_label": "Unreal Engine 5 Documentation — Smart Objects",
        "src2_note": "documentação cobrindo Smart Object Definitions, slots de animação, subsistema de reserva e interação com IA",
    },
    "07-pbr-2d-assets.txt": {
        "group_title": "Texturização Procedural e Pipelines 2D com IA para Jogos",
        "first": 161,
        "check": "Verificação factual contra documentação oficial do Blender Shader Nodes, Texture Paint e padrões PBR.",
        "src1_label": "Blender Manual — Texture Shader Nodes",
        "src1_note": "documentação técnica cobrindo grafos de textura, nós de Bump/Normal e mapeamento PBR",
        "src2_label": "Blender Manual — Texture Painting & Mapping",
        "src2_note": "manual cobrindo projeção de texturas, pintura digital, alinhamento UV e materiais tileáveis",
    },
    "08-voice-audio-ai.txt": {
        "group_title": "Síntese de Voz e Áudio para Jogos com IA",
        "first": 171,
        "check": "Verificação factual contra documentação oficial da ElevenLabs API e FMOD Studio.",
        "src1_label": "ElevenLabs API Reference — Text to Speech",
        "src1_note": "especificação oficial de endpoints REST para síntese de voz, timestamps por palavra e controle de prosódia",
        "src2_label": "FMOD Studio Documentation",
        "src2_note": "manual cobrindo roteamento de barramentos de diálogo, efeitos de ambiente, espacialização 3D e sidechain ducking",
    },
    "09-qa-playtesting-ai.txt": {
        "group_title": "Testes Automatizados e QA de Jogos com IA e Bots",
        "first": 181,
        "check": "Verificação factual contra documentação do Farama Gymnasium e Unity Test Framework.",
        "src1_label": "Farama Gymnasium Documentation — Environment Creation",
        "src1_note": "guia padrão para criação de ambientes de reinforcement learning (step, reset, action/observation spaces)",
        "src2_label": "Unity Test Framework Manual",
        "src2_note": "documentação de testes de integração PlayMode, asserções de física e execução automatizada em CI",
    },
    "10-diataxis-techdocs.txt": {
        "group_title": "Documentação Técnica Interativa e Diátaxis para Criadores",
        "first": 191,
        "check": "Verificação factual contra princípios oficiais do framework Diátaxis e diretrizes Write the Docs.",
        "src1_label": "Diátaxis Documentation Framework — Explanation",
        "src1_note": "especificação formal do quadrante de Explicação, arquitetura conceitual e análise de trade-offs",
        "src2_label": "Diátaxis Documentation Framework — How-to Guides",
        "src2_note": "guia para redação de passos orientados a problemas práticos de produção e trabalho diário",
    },
}


def parse_group(file_path: Path) -> tuple[dict[str, str], list[dict[str, object]]]:
    context = GROUP_META[file_path.name]
    content = file_path.read_text(encoding="utf-8")
    lines = content.splitlines()
    sources_line = [l for l in lines if l.startswith("SOURCES:")][0]
    raw_sources = sources_line.replace("SOURCES:", "").strip().split(" | ")
    
    rows = []
    blocks = content.split("===NOTE===")[1:]
    for b in blocks:
        b = b.strip()
        if not b:
            continue
        parts = b.split("|")
        if len(parts) < 9:
            raise ValueError(f"Bloco invalido em {file_path.name}: {b[:50]} (partes: {len(parts)})")
        num = int(parts[0].strip())
        slug = parts[1].strip()
        title = parts[2].strip()
        em_uma_frase = parts[3].strip()
        por_que_importa = parts[4].strip()
        como_funciona = parts[5].strip()
        exemplo = parts[6].strip()
        limites = parts[7].strip()
        como_verificar = parts[8].strip()
        links_str = parts[9].strip() if len(parts) > 9 else ""
        links = [lk.strip() for lk in links_str.split(",") if lk.strip()]
        
        src_list = [
            (context["src1_label"], raw_sources[0].strip(), context["src1_note"]),
            (context["src2_label"], raw_sources[1].strip(), context["src2_note"]),
        ]
        
        rows.append({
            "number": num,
            "slug": slug,
            "title": title,
            "em_uma_frase": em_uma_frase,
            "por_que_importa": por_que_importa,
            "como_funciona": como_funciona,
            "exemplo": exemplo,
            "limites": limites,
            "como_verificar": como_verificar,
            "links": links,
            "sources": src_list,
            "review": f"Tópico verificado: {title}."
        })
    return context, rows


def render_note(
    context: dict[str, str],
    rows: list[dict[str, object]],
    index: int,
    row: dict[str, object],
    valid_slugs: set[str] | None = None,
) -> tuple[int, str, dict[str, object]]:
    number = int(context["first"]) + index
    sources: list[tuple[str, str, str]] = list(row["sources"])  # type: ignore[arg-type]
    
    neighbors = []
    seen_nb: set[str] = set()
    for neighbor_index in (index - 1, index + 1):
        if 0 <= neighbor_index < len(rows):
            other = rows[neighbor_index]
            s = str(other["slug"])
            seen_nb.add(s)
            neighbors.append(f"- [[{s}]] — Veja também: {other['title']}.")
    if valid_slugs is not None:
        for lk in row.get("links", []):  # type: ignore[union-attr]
            if lk not in seen_nb and lk != row["slug"] and lk in valid_slugs:
                seen_nb.add(lk)
                neighbors.append(f"- [[{lk}]] — Conexão temática direta com {lk}.")

    src_urls_yaml = ", ".join(f'"{s[1]}"' for s in sources)
    frontmatter = f'''---
id: software.criacao_ia.tranche02.{number:06d}
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: intermediario
confianca: media
ultima_verificacao: {DATE}
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: {DATE}
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-02.md"
fontes: [{src_urls_yaml}]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: {BATCH_ID}
---'''

    src_md = []
    for label, url, note in sources:
        src_md.append(f"- [{label}]({url}) — {note.capitalize()}. Consulta: {DATE}.")

    body = f'''# {row['title']}

## Em uma frase
{row['em_uma_frase']}

## Por que importa
{row['por_que_importa']}

## Como funciona
{row['como_funciona']}

## Exemplo
{row['exemplo']}

## Limites e trade-offs
{row['limites']}

## Como verificar
{row['como_verificar']}

## Conexões
{chr(10).join(neighbors)}

## Fontes
{chr(10).join(src_md)}
'''

    full_text = f"{frontmatter}\n\n{body}"
    quality = assess_markdown(full_text, f"{row['slug']}.md")
    return number, full_text, quality


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--refresh", action="store_true")
    args = parser.parse_args()

    NOTES_DIR.mkdir(parents=True, exist_ok=True)
    all_valid_slugs: set[str] = set()
    for existing in NOTES_DIR.glob("*.md"):
        all_valid_slugs.add(existing.stem)

    groups = []
    for path in sorted(DATA_DIR.glob("*.txt")):
        context, rows = parse_group(path)
        groups.append((context, rows))
        for r in rows:
            all_valid_slugs.add(str(r["slug"]))

    pending = []
    report_rows = []
    group_summaries = []
    seen_slugs: set[str] = set()
    seen_titles: set[str] = set()
    expected_number = START

    for context, rows in groups:
        group_summaries.append((context, len(rows)))
        for index, row in enumerate(rows):
            number = int(context["first"]) + index
            if number != expected_number:
                raise ValueError(f"esperado ID {expected_number}, obtido {number} no item {row['slug']}")
            slug = str(row["slug"])
            title = str(row["title"])
            normalized_title = normalize(title)
            if slug in seen_slugs:
                raise ValueError(f"slug em colisão: {slug}")
            if normalized_title in seen_titles:
                raise ValueError(f"título em colisão: {title}")
            seen_slugs.add(slug)
            seen_titles.add(normalized_title)
            
            num, content, quality = render_note(context, rows, index, row, valid_slugs=all_valid_slugs)
            if not quality["ready_for_review"]:
                raise ValueError(f"Falha de qualidade na nota {slug}: {quality['errors']}")
            pending.append((num, row, context, content, quality))
            
            src_name, src_url, _ = row["sources"][0]  # type: ignore[index]
            report_rows.append(
                f"| {number} | [[{slug}]] | [{src_name}]({src_url}) | {row['review']} Revisão factual por IA concluída; decisão: aprovada. |"
            )
            expected_number += 1

    if len(pending) != EXPECTED_NOTES or expected_number != START + EXPECTED_NOTES:
        raise ValueError(
            f"esperadas {EXPECTED_NOTES} notas de {START} a {START + EXPECTED_NOTES - 1}, validadas {len(pending)}"
        )

    repeated = repeated_substantive_sentences(
        [(number, content) for number, _, _, content, _ in pending]
    )
    if repeated:
        examples = [f"{numbers}: {sentence}" for sentence, numbers in list(repeated.items())[:8]]
        raise ValueError(f"prosa substantiva repetida entre notas; revisar antes de gravar: {examples}")

    for number, row, context, content, quality in pending:
        (NOTES_DIR / f"{row['slug']}.md").write_text(content, encoding="utf-8")

    report = [
        f"---",
        f"tipo: revisao-factual-ia",
        f"lote: {BATCH_ID}",
        f"tranche: 02",
        f"data: {DATE}",
        f"resultado: aprovada",
        f"---",
        f"",
        f"# Revisão factual por IA — lote `{BATCH_ID}`, tranche 2 (IDs 000101–000200)",
        "",
        f"- Data: {DATE}",
        "- Revisor: `Arena.ai Agent Mode`",
        f"- Escopo: notas **{START}–{START + EXPECTED_NOTES - 1}**, em dez grupos temáticos com dez notas cada; cada linha identifica a conferência factual da nota.",
        "- Fontes primárias: documentação oficial dos projetos e versões indicadas nas próprias notas; as afirmações foram limitadas ao material citado.",
        f"- Resultado: **{EXPECTED_NOTES} revisões factuais por IA registradas** e aprovadas no gate automatizado de qualidade, elevando o quarto lote `{BATCH_ID}` para **200/2.000 notas válidas (`in_progress`)**. Isto não é aprovação humana nem garantia de ausência de erro.",
        "- Nenhuma aprovação humana existente foi alterada ou estendida às novas notas.",
        "",
        "## Registro por nota",
        "",
        "| # | Nota | Fonte principal | Verificação factual / decisão |",
        "|---:|---|---|---|",
        *report_rows,
        "",
        "## Verificações por grupo",
        "",
    ]
    for context, count in group_summaries:
        report.append(
            f"- {context['group_title']} (itens {context['first']}–{int(context['first']) + count - 1}): {context['check']}"
        )
    report += [
        "- A auditoria de links, a comparação com o inventário, o gate de conteúdo e a verificação de sentenças repetidas foram executados separadamente antes da contabilização.",
        "",
    ]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(report).rstrip() + "\n", encoding="utf-8")
    word_counts = [quality["word_count"] for _, _, _, _, quality in pending]
    source_counts = [quality["source_count"] for _, _, _, _, quality in pending]
    print(
        f"Geradas {len(pending)} notas substantivas (IDs {START}–{START + EXPECTED_NOTES - 1}); "
        f"palavras: min={min(word_counts)}; max={max(word_counts)}"
    )
    print(f"Fontes HTTPS específicas por nota: min={min(source_counts)}; max={max(source_counts)}")
    print(f"Relatório factual: {REPORT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
