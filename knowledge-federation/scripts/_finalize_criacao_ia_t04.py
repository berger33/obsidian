#!/usr/bin/env python3
"""Generate the tranche-04 AI factual review report and record per-note review metadata."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KF = ROOT / "knowledge-federation"
NOTES_DIR = KF / "domains" / "software-0010" / "software" / "criacao-ia"
DATA_DIR = Path(__file__).resolve().parent / "_criacao_ia_t04_data"
BATCH_ID = "software-criacao-ia-2000-0004"
DATE = "2026-10-04"
START = 301
REPORT_REL = f"knowledge-federation/exports/reports/ai-review-{BATCH_ID}-tranche-04.md"
REPORT_PATH = KF / "exports" / "reports" / f"ai-review-{BATCH_ID}-tranche-04.md"


def load_rows() -> list[dict]:
    rows = []
    for path in sorted(DATA_DIR.glob("*.json")):
        group = json.loads(path.read_text(encoding="utf-8"))
        rows.extend(group["notes"])
    if len(rows) != 100:
        raise ValueError(f"Esperadas 100 notas, encontradas {len(rows)}")
    return rows


def build_report(rows: list[dict]) -> str:
    lines = [
        "---",
        "tipo: revisao-factual-ia",
        f"lote: {BATCH_ID}",
        "tranche: 04",
        f"data: {DATE}",
        "resultado: aprovada",
        "---",
        "",
        f"# Revisão factual por IA — lote `{BATCH_ID}`, tranche 4 (IDs {START:06d}–{START + 99:06d})",
        "",
        f"- Data: {DATE}",
        "- Revisor: `Arena.ai Agent Mode`",
        "- Escopo: notas **301–400**, em dez grupos temáticos de dez notas cada; cada registro resume a alegação central conferida e a decisão individual.",
        "- Método: conferi as afirmações, defaults, limites e exemplos contra as fontes primárias específicas registradas em cada nota (textos oficiais na íntegra quando o formato o permitiu); onde a documentação é versionada, mantive o escopo dessa versão — os READMEs do llama.cpp leem-se contra o master da data. As notas continuam sujeitas a novas versões das ferramentas.",
        "- Resultado: **100 revisões factuais por IA registradas**; todas as 100 passaram no gate estrutural e editorial da tranche. A revisão por IA não é aprovação humana nem garantia de ausência de erro.",
        "- Revisão humana: **0/100**; nenhuma aprovação humana foi solicitada, registrada ou inferida. As 49 aprovações humanas históricas permanecem inalteradas.",
        "- Eixos selecionados: WebGPU (adapter/limites/buffers/bindings/queries); WGSL (classes de armazenamento, layout, atômicos, uniformidade); Bevy ECS (schedules, paralelismo por acesso, queries, Commands, resources, plugins, App/Schedule/World); Unity Entities@1.4 (mudanças estruturais, ECB, IJobEntity, safety system, chunks, blob assets, aspects, baking); Godot 4.7 (shaders canvas-item/spatial/linguagem; GDExtension e o arquivo .gdextension); Blender 5.2 LTS (view transforms, Non-Color, VSE proxy/cache, painel System); Web Audio (contexto/autoplay, fontes one-shot, automação, decode, AudioWorklet, Panner/Convolver/Analyser); llama.cpp server (contexto/batch, KV, slots, caches, endpoints, exposição de rede, GBNF/JSON Schema, ordem de samplers); Transformers v5 (GenerationConfig, estratégias, filtros de amostragem, anti-repetição, cache_implementation, decodificação assistida, retornos e custom_generate).",
        "- Retificações da fonte: nenhuma nota afirma o comportamento de `detach` do buffer em `decodeAudioData` nem regra de descarte parcial para consultas de oclusão — ausentes das páginas conferidas e, portanto, omitidas; em Bevy, states/assets/eventos ficaram de fora por ausência de fonte lida. Em Blender, o painel System do manual 5.2 LTS substituiu caminhos antigos do VSE (proxy/cache migraram para editors/video_sequencer).",
        "",
        "## Registro por nota",
        "",
        "| # | Nota | Fontes primárias consultadas | Verificação factual / decisão |",
        "|---:|---|---|---|",
    ]
    for offset, row in enumerate(rows):
        number = START + offset
        srcs = " · ".join(f"[{s['label']}]({s['url']})" for s in row["sources"])
        review = row["review"].strip()
        if not review.endswith("."):
            review += "."
        lines.append(
            f"| {number} | [[{row['slug']}]] — {row['title']} | {srcs} | {review} Decisão: aprovada. |"
        )
    lines.append("")
    return "\n".join(lines)


def patch_frontmatter(rows: list[dict]) -> int:
    patched = 0
    for row in rows:
        path = NOTES_DIR / f"{row['slug']}.md"
        text = path.read_text(encoding="utf-8")
        m = re.match(r"^(---\n)(.*?\n)(---\n)", text, flags=re.S)
        if not m:
            raise ValueError(f"Frontmatter ausente em {path.name}")
        fm = m.group(2)
        fm = fm.replace("revisao_ia: pendente", "revisao_ia: aprovada")
        fm = fm.replace('revisor_ia: ""', 'revisor_ia: "Arena.ai Agent Mode"')
        fm = fm.replace('data_revisao_ia: ""', f"data_revisao_ia: {DATE}")
        fm = fm.replace('relatorio_revisao_ia: ""', f'relatorio_revisao_ia: "{REPORT_REL}"')
        for key in ("revisao_ia", "revisor_ia", "data_revisao_ia", "relatorio_revisao_ia"):
            if not re.search(rf"(?m)^{key}: (?!\"\"$|pendente$)", fm):
                raise ValueError(f"{path.name}: campo {key} não atualizado")
        path.write_text(m.group(1) + fm + m.group(3) + text[m.end():], encoding="utf-8")
        patched += 1
    return patched


def main() -> int:
    rows = load_rows()
    REPORT_PATH.write_text(build_report(rows), encoding="utf-8")
    print(f"Relatório de revisão IA gravado: {REPORT_REL} ({len(rows)} linhas).")
    patched = patch_frontmatter(rows)
    print(f"Frontmatter de revisão atualizado em {patched}/100 notas (revisao_ia: aprovada).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
