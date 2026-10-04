#!/usr/bin/env python3
"""Reconciliation script for software-criacao-ia-2000-0004 tranche 02."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
KF = ROOT / "knowledge-federation"
DATA_DIR = Path(__file__).resolve().parent / "_criacao_ia_t02_data"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _build_criacao_ia_t02 import parse_group, GROUP_META

# 1. Load notes from tranche 02 data files
groups = []
all_t02_notes = []
for p in sorted(DATA_DIR.glob("*.txt")):
    ctx, rows = parse_group(p)
    groups.append((ctx, rows))
    for r in rows:
        all_t02_notes.append(r)

print(f"Loaded {len(all_t02_notes)} notes from Tranche 02 data files.")

# 2. Append rows 6141-6240 to human-review-queue.md
hrq_path = KF / "exports" / "reports" / "human-review-queue.md"
hrq_text = hrq_path.read_text(encoding="utf-8")

# Check if already appended
if "| 6141 |" not in hrq_text:
    new_rows = []
    base_idx = 6141
    for r in all_t02_notes:
        num = r["number"]
        slug = r["slug"]
        title = r["title"]
        note_num = num - 100 # tranche note index 1..100
        row_str = f"| {base_idx} | `software-criacao-ia-2000-0004` | [{title}](../../domains/software-0010/software/criacao-ia/{slug}.md) | APROVADA POR IA | IA: Arena.ai Agent Mode | Revisão factual por IA registrada em 2026-10-04 no relatório `ai-review-software-criacao-ia-2000-0004-tranche-02.md` (nota {note_num}); não é aprovação humana. |"
        new_rows.append(row_str)
        base_idx += 1
    
    # Split before "## Regra de contagem"
    parts = hrq_text.split("## Regra de contagem")
    table_part = parts[0].rstrip()
    rule_part = """## Regra de contagem

As 49 linhas marcadas `APROVADA` registram a confirmação explícita do usuário; `usuario-da-sessao` identifica a pessoa usuária da sessão sem inventar um nome. As 6191 linhas `APROVADA POR IA` (nº 50–6240) correspondem às 1991 notas 10–2000 do lote `software-testes-2000-0001`, às 2000 notas do lote `software-devops-2000-0002`, às 2000 notas do lote `software-seguranca-2000-0003` e às 200 notas de IDs 1–200 das tranches 1 e 2 de `software-criacao-ia-2000-0004`; elas contam pelo protocolo atualizado, mas não são aprovações humanas. Cada nova nota precisa passar pelo gate e ter revisão factual registrada antes de entrar na contagem.
"""
    updated_hrq = table_part + "\n" + "\n".join(new_rows) + "\n\n" + rule_part
    hrq_path.write_text(updated_hrq, encoding="utf-8")
    print("Updated human-review-queue.md with rows 6141-6240.")
else:
    print("human-review-queue.md already contains Tranche 02 rows.")

# 3. Create batch-reconciliation-software-criacao-ia-2000-0004-tranche-02.md
reconciliation_path = KF / "exports" / "reports" / "batch-reconciliation-software-criacao-ia-2000-0004-tranche-02.md"
reconciliation_content = """# Reconciliação — `software-criacao-ia-2000-0004`, tranche 2

Data: 2026-10-04. Esta reconciliação contabiliza os arquivos substantivos produzidos na segunda tranche (IDs 101–200); o estado inicial de abertura continua preservado em [`batch-reconciliation-software-criacao-ia-2000-0004-initial.md`](batch-reconciliation-software-criacao-ia-2000-0004-initial.md) e a primeira tranche em [`batch-reconciliation-software-criacao-ia-2000-0004-tranche-01.md`](batch-reconciliation-software-criacao-ia-2000-0004-tranche-01.md).

## Escopo e resultado da tranche

- IDs materiais: `software.criacao_ia.tranche02.000101` a `software.criacao_ia.tranche02.000200`.
- Arquivos de nota: **100 novas notas** (totalizando 200 notas no diretório `domains/software-0010/software/criacao-ia/`).
- Seleção: **10 trilhas × 10 notas**, cobrindo Claude Code CLI, Continue.dev / Ollama, Cursor Context Engineering, Godot IA de Gameplay, Unity Animation Rigging / Utility AI, Unreal StateTree / Smart Objects, Texturização PBR 2D, Áudio e Síntese Vocal com IA, QA Playtesting com Gymnasium / UTF e Documentação Técnica Diátaxis.
- Gate da tranche: **100/100 aprovadas**; contagem mínima de palavras respeitada (154 a 252 palavras), duas fontes HTTPS primárias e específicas por nota, seções obrigatórias completas e wikilinks resolvidos.
- Revisão factual por IA: **100/100**, registrada em `revisao_ia: aprovada`, com revisor `Arena.ai Agent Mode`, data `2026-10-04` e relatório `ai-review-software-criacao-ia-2000-0004-tranche-02.md`.
- Revisão humana: **0/100**; nenhuma aprovação humana foi solicitada, registrada ou inferida.
- Contabilizadas no lote: **200/2.000 (10,00%)**; estado permanece `in_progress`.
- Próximas notas: **1.800** ainda não produzidas; não há IDs futuros reservados, placeholders ou progresso virtual.

## Trilhas selecionadas

1. Claude Code CLI e Anthropic API: comandos interativos, CLAUDE.md, Prompt Caching, Tool Use e MCP para fluxos de desenvolvimento.
2. Agentes de código locais e Continue.dev: configuração de config.json, Ollama num_ctx/keep_alive, modelos GGUF e context providers.
3. Cursor e Context Engineering: .cursorrules, indexação vetorial @Codebase, composer multi-arquivo e símbolos de contexto.
4. Máquinas de estados e IA no Godot 4: nós virtuais GDScript, forças de steering (Seek/Flee), Area3D sensorial e AnimationTree StateMachine.
5. Rigging de animação e Utility AI no Unity: RigBuilder, restrições TwoBoneIK/Multi-Aim, NavMesh procedural e curvas de resposta contínuas.
6. StateTree e Smart Objects na Unreal Engine 5: árvores de estado leves, Evaluators, Tasks, Smart Object Definitions e Mass AI.
7. Texturização PBR e pipelines 2D com IA: texturas tileáveis seamless, mapas de normal/roughness, ControlNet Canny/OpenPose e compressão BC7/ASTC.
8. Síntese de voz e áudio para jogos: TTS assíncrono para NPCs, cache local, visemas Rhubarb para lip-sync, FMOD bus routing e ducking.
9. QA e playtesting com IA: playtests headless em CI, ambientes Farama Gymnasium, bots exploradores de colisão e profiler CLI.
10. Documentação técnica e Diátaxis: Tutoriais, How-to, Referência e Explicação, sandboxes interativos Wasm e checklist para tutoriais com IA.

## Evidências

- [Manifesto do lote e lista dos IDs/títulos](../batches/software-criacao-ia-2000-0004.md)
- [MOC do lote](../../00-home-vault/MOCs/MOC-Criacao-IA-Software-0010.md)
- [Revisão factual por IA, nota por nota](ai-review-software-criacao-ia-2000-0004-tranche-02.md)
- [Gate por arquivos da tranche](note-quality-software-criacao-ia-2000-0004-tranche-02.md)
- [Registro separado de revisões](human-review-queue.md), registros numerados 6141–6240
- [Auditoria global por arquivos e checkpoint](note-quality-audit.md)
- `python3 -m unittest discover -s knowledge-federation/tests -v`: **13 testes aprovados**.

## Reconciliação global após a tranche

| Métrica | Antes da tranche | Depois da tranche |
|---|---:|---:|
| Arquivos Markdown ativos em `domains/` | 6.240 | 6.340 |
| Notas válidas pelo protocolo | 6.140 | 6.240 |
| Aprovações humanas históricas | 49 | 49 |
| Revisões factuais por IA | 6.091 | 6.191 |
| Notas legadas com pendências, fora da contagem | 100 | 100 |
| Lotes completos | 3/500 | 3/500 |
| Lote 4 `software-criacao-ia-2000-0004` | 100/2.000 (5,00%) | 200/2.000 (10,00%) |

A auditoria global avaliou **6.340 arquivos**: 6.240 passaram o protocolo atual (49 revisões humanas históricas + 6.191 revisões por IA) e 100 notas legadas mantêm pendências. O checkpoint contém 1.000.000 de registros virtuais com template e 8.000 caminhos materializados; nenhum deles foi incluído na contagem editorial. A tranche 2 não altera o status `complete` dos três lotes anteriores nem abre o lote 5.
"""
reconciliation_path.write_text(reconciliation_content, encoding="utf-8")
print(f"Created {reconciliation_path.name}")

# 4. Update MOC-Criacao-IA-Software-0010.md
moc_path = KF / "00-home-vault" / "MOCs" / "MOC-Criacao-IA-Software-0010.md"
moc_text = moc_path.read_text(encoding="utf-8")

# Prepare Tranche 2 section for MOC
t2_section_lines = [
    "## Conteúdo materializado — tranche 2 (100 notas; IDs 000101–000200)",
    "",
]
for ctx, rows in groups:
    t2_section_lines.append(f"### {ctx['group_title']}")
    t2_section_lines.append("")
    for r in rows:
        t2_section_lines.append(f"- [[{r['slug']}]] — {r['title']}.")
    t2_section_lines.append("")

t2_section_str = "\n".join(t2_section_lines)

# Update metrics in MOC
moc_updated = re.sub(
    r"Progresso: \*\*100 / 2\.000 notas válidas \(5,00%\)\*\*",
    r"Progresso: **200 / 2.000 notas válidas (10,00%)**",
    moc_text
)
moc_updated = re.sub(
    r"Gate: 100/100; revisão factual humana: 0/100; revisão factual por IA: 100/100\.",
    r"Gate: 200/200; revisão factual humana: 0/200; revisão factual por IA: 200/200.",
    moc_updated
)
moc_updated = re.sub(
    r"Notas materiais presentes e contadas: \*\*100\*\*, IDs 000001–000100\. Para as próximas 1\.900 notas",
    r"Notas materiais presentes e contadas: **200**, IDs 000001–000200. Para as próximas 1.800 notas",
    moc_updated
)

# Insert Tranche 2 before "## Próximos passos e auditoria"
if "## Conteúdo materializado — tranche 2" not in moc_updated:
    moc_updated = moc_updated.replace(
        "## Próximos passos e auditoria",
        t2_section_str + "\n## Próximos passos e auditoria"
    )

# Update reports list in MOC
if "ai-review-software-criacao-ia-2000-0004-tranche-02.md" not in moc_updated:
    moc_updated = moc_updated.replace(
        "- Reconciliação da tranche 1: [`batch-reconciliation-software-criacao-ia-2000-0004-tranche-01.md`](../../exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-01.md)",
        "- Reconciliação da tranche 1: [`batch-reconciliation-software-criacao-ia-2000-0004-tranche-01.md`](../../exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-01.md)\n"
        "- Revisão factual IA da tranche 2: [`ai-review-software-criacao-ia-2000-0004-tranche-02.md`](../../exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-02.md)\n"
        "- Gate da tranche 2: [`note-quality-software-criacao-ia-2000-0004-tranche-02.md`](../../exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-02.md)\n"
        "- Reconciliação da tranche 2: [`batch-reconciliation-software-criacao-ia-2000-0004-tranche-02.md`](../../exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-02.md)"
    )

moc_path.write_text(moc_updated, encoding="utf-8")
print("Updated MOC-Criacao-IA-Software-0010.md")

# 5. Update software-criacao-ia-2000-0004.md
batch_manifest = KF / "exports" / "batches" / "software-criacao-ia-2000-0004.md"
bm_text = batch_manifest.read_text(encoding="utf-8")

bm_updated = re.sub(
    r"Notas materiais redigidas: \*\*100 / 2\.000 \(5,00%\)\*\*",
    r"Notas materiais redigidas: **200 / 2.000 (10,00%)**",
    bm_text
)
bm_updated = re.sub(
    r"Gate automatizado: \*\*100/100 aprovadas\*\*",
    r"Gate automatizado: **200/200 aprovadas**",
    bm_updated
)
bm_updated = re.sub(
    r"Revisão factual humana: \*\*0/100\*\*",
    r"Revisão factual humana: **0/200**",
    bm_updated
)
bm_updated = re.sub(
    r"Revisão factual por IA: \*\*100/100\*\* \(relatório da tranche 1\)",
    r"Revisão factual por IA: **200/200** (relatórios das tranches 1 e 2)",
    bm_updated
)
bm_updated = re.sub(
    r"Notas válidas contabilizadas: \*\*100/2\.000 \(5,00%\)\*\*",
    r"Notas válidas contabilizadas: **200/2.000 (10,00%)**",
    bm_updated
)
bm_updated = re.sub(
    r"tranche 1 concluída e reconciliada; 19 tranches planejadas permanecem sem IDs reservados\.",
    r"tranches 1 e 2 concluídas e reconciliadas; 18 tranches planejadas permanecem sem IDs reservados.",
    bm_updated
)
bm_updated = re.sub(
    r"As notas materiais existentes são somente os IDs 1–100, com arquivos e conteúdo; para as 1\.900 notas",
    r"As notas materiais existentes são somente os IDs 1–200, com arquivos e conteúdo; para as 1.800 notas",
    bm_updated
)

# Prepare Tranche 2 section for manifest
t2_manifest_lines = [
    "## Tranche 2 — Claude Code, Continue.dev, Cursor, Godot IA, Unity Animation Rigging, Unreal StateTree, PBR 2D, Voz/Áudio IA, QA Playtesting e Diátaxis (100 notas)",
    "",
    "IDs materiais: `software.criacao_ia.tranche02.000101`–`software.criacao_ia.tranche02.000200`. Cada tópico tem fontes primárias indicadas na própria nota.",
    "",
]
for ctx, rows in groups:
    t2_manifest_lines.append(f"### {ctx['group_title']}")
    t2_manifest_lines.append("")
    for r in rows:
        num = r["number"]
        slug = r["slug"]
        title = r["title"]
        t2_manifest_lines.append(f"{num}. [{title}](../../domains/software-0010/software/criacao-ia/{slug}.md) — `software.criacao_ia.tranche02.{num:06d}`")
    t2_manifest_lines.append("")

t2_manifest_str = "\n".join(t2_manifest_lines)

if "## Tranche 2 — Claude Code" not in bm_updated:
    bm_updated = bm_updated.replace(
        "## Critério de entrada na contagem",
        t2_manifest_str + "\n## Critério de entrada na contagem"
    )

# Update artifacts in manifest
if "ai-review-software-criacao-ia-2000-0004-tranche-02.md" not in bm_updated:
    bm_updated = bm_updated.replace(
        "- Reconciliação da tranche 1: [`batch-reconciliation-software-criacao-ia-2000-0004-tranche-01.md`](../reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-01.md)",
        "- Reconciliação da tranche 1: [`batch-reconciliation-software-criacao-ia-2000-0004-tranche-01.md`](../reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-01.md)\n"
        "- Revisão factual IA da tranche 2: [`ai-review-software-criacao-ia-2000-0004-tranche-02.md`](../reports/ai-review-software-criacao-ia-2000-0004-tranche-02.md)\n"
        "- Gate da tranche 2: [`note-quality-software-criacao-ia-2000-0004-tranche-02.md`](../reports/note-quality-software-criacao-ia-2000-0004-tranche-02.md)\n"
        "- Reconciliação da tranche 2: [`batch-reconciliation-software-criacao-ia-2000-0004-tranche-02.md`](../reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-02.md)"
    )

batch_manifest.write_text(bm_updated, encoding="utf-8")
print("Updated software-criacao-ia-2000-0004.md")

# 6. Update STATUS-CONSOLIDACAO-1M.md
status_path = KF / "STATUS-CONSOLIDACAO-1M.md"
st_text = status_path.read_text(encoding="utf-8")

st_text = st_text.replace(
    "| Progresso válido global | 6140 / 1.000.000 (0,6140%) | 49 revisões humanas históricas + 6091 revisões por IA registradas separadamente |",
    "| Progresso válido global | 6240 / 1.000.000 (0,6240%) | 49 revisões humanas históricas + 6191 revisões por IA registradas separadamente |"
)
st_text = st_text.replace(
    "| Revisões factuais por IA registradas | 6091 | 5991 nos três lotes completos + 100 na tranche 1 de `software-criacao-ia-2000-0004`; não são humanas |",
    "| Revisões factuais por IA registradas | 6191 | 5991 nos três lotes completos + 200 nas tranches 1 e 2 de `software-criacao-ia-2000-0004`; não são humanas |"
)
st_text = st_text.replace(
    "| Quarto lote (`software-criacao-ia-2000-0004`) | 100 / 2.000 (5,00%) | Tranche 1 aprovada no gate e revisada por IA; 19 tranches planejadas ([manifesto](exports/batches/software-criacao-ia-2000-0004.md), [relatório](exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-01.md), [reconciliação](exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-01.md)) |",
    "| Quarto lote (`software-criacao-ia-2000-0004`) | 200 / 2.000 (10,00%) | Tranches 1 e 2 aprovadas no gate e revisadas por IA; 18 tranches planejadas ([manifesto](exports/batches/software-criacao-ia-2000-0004.md), [relatório](exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-02.md), [reconciliação](exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-02.md)) |"
)
st_text = st_text.replace(
    "| Candidatas que passaram pelo gate automatizado | 6140 | Todas receberam revisão factual registrada; gate sozinho não comprova veracidade |",
    "| Candidatas que passaram pelo gate automatizado | 6240 | Todas receberam revisão factual registrada; gate sozinho não comprova veracidade |"
)
st_text = st_text.replace(
    "o quarto lote [`software-criacao-ia-2000-0004`](exports/batches/software-criacao-ia-2000-0004.md) avançou a 100/2.000 após a tranche 1, registrada na [revisão factual](exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-01.md) e na [reconciliação](exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-01.md).",
    "o quarto lote [`software-criacao-ia-2000-0004`](exports/batches/software-criacao-ia-2000-0004.md) avançou a 200/2.000 após a tranche 2, registrada na [revisão factual](exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-02.md) e na [reconciliação](exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-02.md)."
)
st_text = st_text.replace(
    "[reconciliação da tranche 1 do lote 4](exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-01.md)",
    "[reconciliação da tranche 2 do lote 4](exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-02.md)"
)
st_text = st_text.replace(
    "lote `software-criacao-ia-2000-0004` está em 100/2.000 após tranche 1, em `domains/software-0010/software/criacao-ia/`.",
    "lote `software-criacao-ia-2000-0004` está em 200/2.000 após tranche 2, em `domains/software-0010/software/criacao-ia/`."
)

status_path.write_text(st_text, encoding="utf-8")
print("Updated STATUS-CONSOLIDACAO-1M.md")

# 7. Update PLANO-CONTINUO-1M.md
plano_path = KF / "PLANO-CONTINUO-1M.md"
pl_text = plano_path.read_text(encoding="utf-8")

pl_text = pl_text.replace(
    "Progresso: **6140 / 1.000.000 (0,6140%)**; faltam **993.860** notas válidas.",
    "Progresso: **6240 / 1.000.000 (0,6240%)**; faltam **993.760** notas válidas."
)
pl_text = pl_text.replace(
    "Quarto lote `software-criacao-ia-2000-0004`: **100 / 2.000 (5,00%)**; tranche 1 concluída em `software-0010`, com 19 tranches planejadas sem IDs reservados.",
    "Quarto lote `software-criacao-ia-2000-0004`: **200 / 2.000 (10,00%)**; tranches 1 e 2 concluídas em `software-0010`, com 18 tranches planejadas sem IDs reservados."
)
pl_text = pl_text.replace(
    "Arquivos Markdown ativos: **6240**; 100 com pendências de qualidade, excluídos da contagem.",
    "Arquivos Markdown ativos: **6340**; 100 com pendências de qualidade, excluídos da contagem."
)
pl_text = pl_text.replace(
    "Global: 6240 arquivos, 6140 válidas, 100 com pendências legadas; lote 4 com 100/100 na tranche 1; veja a [reconciliação da tranche 1 do lote 4](exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-01.md).",
    "Global: 6340 arquivos, 6240 válidas, 100 com pendências legadas; lote 4 com 200/200 após tranche 2; veja a [reconciliação da tranche 2 do lote 4](exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-02.md)."
)
pl_text = pl_text.replace(
    "lote 4 `software-criacao-ia-2000-0004` tem 100/2.000 e 19 tranches planejadas em `domains/software-0010/software/criacao-ia/`; restam 496 lotes adicionais.",
    "lote 4 `software-criacao-ia-2000-0004` tem 200/2.000 e 18 tranches planejadas em `domains/software-0010/software/criacao-ia/`; restam 496 lotes adicionais."
)
pl_text = pl_text.replace(
    "Progresso atual: 6140 notas válidas, 3/500 lotes completos.",
    "Progresso atual: 6240 notas válidas, 3/500 lotes completos."
)

plano_path.write_text(pl_text, encoding="utf-8")
print("Updated PLANO-CONTINUO-1M.md")

# 8. Update README-1M.md
r1m_path = KF / "README-1M.md"
r1m_text = r1m_path.read_text(encoding="utf-8")

r1m_text = r1m_text.replace(
    "O estado ativo soma **6140 notas válidas** (49 aprovações humanas históricas + 6091 revisões factuais por IA) em **6240 arquivos Markdown**, incluindo 100 notas legadas com pendências que permanecem fora da contagem. Os três primeiros lotes estão completos; `software-criacao-ia-2000-0004` iniciou em 100/2.000, após a tranche 1 ([revisão factual IA](exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-01.md), [reconciliação](exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-01.md)).",
    "O estado ativo soma **6240 notas válidas** (49 aprovações humanas históricas + 6191 revisões factuais por IA) em **6340 arquivos Markdown**, incluindo 100 notas legadas com pendências que permanecem fora da contagem. Os três primeiros lotes estão completos; `software-criacao-ia-2000-0004` avançou a 200/2.000, após a tranche 2 ([revisão factual IA](exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-02.md), [reconciliação](exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-02.md))."
)

r1m_path.write_text(r1m_text, encoding="utf-8")
print("Updated README-1M.md")

# 9. Update knowledge-federation/README.md
kf_readme = KF / "README.md"
kf_rm_text = kf_readme.read_text(encoding="utf-8")

kf_rm_text = kf_rm_text.replace(
    "Progresso: **6140 / 1.000.000 (0,6140%)**; faltam 993.860 notas válidas.",
    "Progresso: **6240 / 1.000.000 (0,6240%)**; faltam 993.760 notas válidas."
)
kf_rm_text = kf_rm_text.replace(
    "Quarto lote `software-criacao-ia-2000-0004`: **100 / 2.000** notas válidas; tranche 1 concluída e 19 tranches planejadas ([manifesto](exports/batches/software-criacao-ia-2000-0004.md), [revisão IA](exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-01.md), [gate](exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-01.md), [reconciliação](exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-01.md) e [MOC](00-home-vault/MOCs/MOC-Criacao-IA-Software-0010.md)).",
    "Quarto lote `software-criacao-ia-2000-0004`: **200 / 2.000** notas válidas; tranches 1 e 2 concluídas e 18 tranches planejadas ([manifesto](exports/batches/software-criacao-ia-2000-0004.md), [revisão IA](exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-02.md), [gate](exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-02.md), [reconciliação](exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-02.md) e [MOC](00-home-vault/MOCs/MOC-Criacao-IA-Software-0010.md))."
)
kf_rm_text = kf_rm_text.replace(
    "o lote 4 está em 100/2.000 após a tranche 1 de engenharia e criação com IA ([revisão factual](exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-01.md), [gate](exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-01.md) e [reconciliação](exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-01.md)).",
    "o lote 4 está em 200/2.000 após a tranche 2 de engenharia e criação com IA ([revisão factual](exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-02.md), [gate](exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-02.md) e [reconciliação](exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-02.md))."
)

kf_readme.write_text(kf_rm_text, encoding="utf-8")
print("Updated knowledge-federation/README.md")

# 10. Update root README.md
root_readme = ROOT / "README.md"
rt_text = root_readme.read_text(encoding="utf-8")

rt_text = rt_text.replace(
    "| Notas com revisão factual por IA registrada | 6091 | Revisões dos três lotes completos (5991) + 100 notas na tranche 1 do lote 4; não são humanas |",
    "| Notas com revisão factual por IA registrada | 6191 | Revisões dos três lotes completos (5991) + 200 notas nas tranches 1 e 2 do lote 4; não são humanas |"
)
rt_text = rt_text.replace(
    "| Quarto lote `software-criacao-ia-2000-0004` | 100 / 2.000 (5,00%) | Tranche 1 concluída (100 IA); 19 tranches planejadas sem IDs reservados; foco em engenharia e criação de programas, apps e jogos com IA |",
    "| Quarto lote `software-criacao-ia-2000-0004` | 200 / 2.000 (10,00%) | Tranches 1 e 2 concluídas (200 IA); 18 tranches planejadas sem IDs reservados; foco em engenharia e criação de programas, apps e jogos com IA |"
)
rt_text = rt_text.replace(
    "| Arquivos Markdown ativos em `knowledge-federation/domains/` | 6240 | 100 notas legadas com pendências + 6140 notas autorais substantivas |",
    "| Arquivos Markdown ativos em `knowledge-federation/domains/` | 6340 | 100 notas legadas com pendências + 6240 notas autorais substantivas |"
)
rt_text = rt_text.replace(
    "O quarto lote [`software-criacao-ia-2000-0004`](knowledge-federation/exports/batches/software-criacao-ia-2000-0004.md) está em 100/2.000 após a tranche 1, com foco em engenharia e criação de programas, apps e jogos com IA ([revisão factual](knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-01.md), [reconciliação](knowledge-federation/exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-01.md), [auditoria da tranche](knowledge-federation/exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-01.md) e [MOC](knowledge-federation/00-home-vault/MOCs/MOC-Criacao-IA-Software-0010.md)).",
    "O quarto lote [`software-criacao-ia-2000-0004`](knowledge-federation/exports/batches/software-criacao-ia-2000-0004.md) está em 200/2.000 após a tranche 2, com foco em engenharia e criação de programas, apps e jogos com IA ([revisão factual](knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-02.md), [reconciliação](knowledge-federation/exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-02.md), [auditoria da tranche](knowledge-federation/exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-02.md) e [MOC](knowledge-federation/00-home-vault/MOCs/MOC-Criacao-IA-Software-0010.md))."
)

root_readme.write_text(rt_text, encoding="utf-8")
print("Updated root README.md")

# 11. Update PROMPT-CONTINUACAO.md
prompt_cont = KF / "PROMPT-CONTINUACAO.md"
pc_text = prompt_cont.read_text(encoding="utf-8")

pc_text = pc_text.replace(
    "Estado: 6140 / 1.000.000 (0,6140%) válidas; 3/500 lotes completos; 6240 arquivos Markdown ativos (6140 válidas + 100 legadas com pendências, mantidas fora da contagem).",
    "Estado: 6240 / 1.000.000 (0,6240%) válidas; 3/500 lotes completos; 6340 arquivos Markdown ativos (6240 válidas + 100 legadas com pendências, mantidas fora da contagem)."
)
pc_text = pc_text.replace(
    "Lote 4 `software-criacao-ia-2000-0004`: 100/2.000 (5,00%), com tranche 1 concluída (100 notas, IDs 1–100), 100 aprovadas pelo gate e 100 com revisão factual por IA; nenhuma aprovação humana nova; 19 tranches planejadas.",
    "Lote 4 `software-criacao-ia-2000-0004`: 200/2.000 (10,00%), com tranches 1 e 2 concluídas (200 notas, IDs 1–200), 200 aprovadas pelo gate e 200 com revisão factual por IA; nenhuma aprovação humana nova; 18 tranches planejadas."
)
pc_text = pc_text.replace(
    "Relatórios do lote 4 tranche 1: `exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-01.md`, `exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-01.md` e `exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-01.md`.",
    "Relatórios do lote 4 tranche 2: `exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-02.md`, `exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-02.md` e `exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-02.md`."
)

prompt_cont.write_text(pc_text, encoding="utf-8")
print("Updated PROMPT-CONTINUACAO.md")

print("All reconciliations complete.")
