#!/usr/bin/env python3
"""Reconciliation for software-criacao-ia-2000-0004 tranche 04 (IDs 301-400)."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KF = ROOT / "knowledge-federation"
DATA_DIR = Path(__file__).resolve().parent / "_criacao_ia_t04_data"
BATCH = "software-criacao-ia-2000-0004"
DATE = "2026-10-04"
START = 301
TR = "tranche-04"
NOTES_REL = "domains/software-0010/software/criacao-ia"


def load_rows() -> list[dict]:
    rows = []
    groups = []
    for path in sorted(DATA_DIR.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        groups.append((data["group"], data["notes"]))
        rows.extend(data["notes"])
    if len(rows) != 100:
        raise ValueError("esperadas 100 notas")
    return rows, groups


def sub_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise ValueError(f"{label}: ocorrência {count} (esperada 1) de: {old[:90]!r}")
    return text.replace(old, new)


rows, groups = load_rows()
log = []

# ---------------------------------------------------------------- fila humana
hrq = KF / "exports/reports/human-review-queue.md"
t = hrq.read_text(encoding="utf-8")
t = sub_once(
    t,
    "distingue 6091 revisões factuais realizadas por IA: `software-testes-2000-0001` (1991), `software-devops-2000-0002` (2000), `software-seguranca-2000-0003` (2000) e `software-criacao-ia-2000-0004` (100 na tranche 1).",
    "distingue 6391 revisões factuais realizadas por IA: `software-testes-2000-0001` (1991), `software-devops-2000-0002` (2000), `software-seguranca-2000-0003` (2000) e `software-criacao-ia-2000-0004` (400 nas tranches 1–4).",
    "fila: cabeçalho",
)
t = sub_once(t, "- Aprovações por IA registradas separadamente: **6091**.", "- Aprovações por IA registradas separadamente: **6391**.", "fila: bullets IA")
t = sub_once(t, "- Notas válidas contabilizadas (gate + revisão humana ou IA): **6140**.", "- Notas válidas contabilizadas (gate + revisão humana ou IA): **6440**.", "fila: bullets válidas")
if "| 6341 |" not in t:
    new_rows = []
    for i, row in enumerate(rows):
        num = 6341 + i
        new_rows.append(
            f"| {num} | `{BATCH}` | [{row['title']}](../../{NOTES_REL}/{row['slug']}.md) | APROVADA POR IA | IA: Arena.ai Agent Mode | "
            f"Revisão factual por IA registrada em {DATE} no relatório `ai-review-{BATCH}-tranche-04.md` (nota {i + 1}); não é aprovação humana. |"
        )
    parts = t.split("## Regra de contagem")
    t = parts[0].rstrip() + "\n" + "\n".join(new_rows) + "\n\n## Regra de contagem" + parts[1]
t = sub_once(
    t,
    "As 6291 linhas `APROVADA POR IA` (nº 50–6340) correspondem",
    "As 6391 linhas `APROVADA POR IA` (nº 50–6440) correspondem",
    "fila: regra nº",
)
t = sub_once(
    t,
    "às 300 notas de IDs 1–300 das tranches 1–3 de",
    "às 400 notas de IDs 1–400 das tranches 1–4 de",
    "fila: regra tranches",
)
hrq.write_text(t, encoding="utf-8")
log.append("fila humana: linhas 6341–6440 + cabeçalho e regra atualizados")

# ------------------------------------------------------------------------ MOC
moc = KF / "00-home-vault/MOCs/MOC-Criacao-IA-Software-0010.md"
m = moc.read_text(encoding="utf-8")
m = sub_once(m, "- Progresso: **300 / 2.000 notas válidas (15,00%)** (`status: in_progress`).", "- Progresso: **400 / 2.000 notas válidas (20,00%)** (`status: in_progress`).", "MOC: progresso")
m = sub_once(m, "- Gate: **300/300**; revisão factual humana: **0/300**; revisão factual por IA: **300/300**.", "- Gate: **400/400**; revisão factual humana: **0/400**; revisão factual por IA: **400/400**.", "MOC: gate")
m = sub_once(m, "- Notas materiais presentes e contadas: **300**, IDs 000001–000300. Para as próximas 1.700 notas", "- Notas materiais presentes e contadas: **400**, IDs 000001–000400. Para as próximas 1.600 notas", "MOC: materiais")
section = ["## Conteúdo materializado — tranche 4 (100 notas; IDs 000301–000400)", ""]
for title, notes in groups:
    section.append(f"### {title}")
    section.append("")
    for r in notes:
        section.append(f"- [[{r['slug']}]] — {r['title']}.")
    section.append("")
if "tranche 4 (100 notas; IDs 000301–000400)" not in m:
    m = sub_once(m, "## Mapa de escopo", "\n".join(section) + "## Mapa de escopo", "MOC: âncora seção")
m = sub_once(
    m,
    "Tranche 3: [revisão factual IA](../../exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-03.md), [gate](../../exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-03.md) e [reconciliação](../../exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-03.md). Lotes adicionais",
    "Tranche 3: [revisão factual IA](../../exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-03.md), [gate](../../exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-03.md) e [reconciliação](../../exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-03.md). Tranche 4: [revisão factual IA](../../exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-04.md), [gate](../../exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-04.md) e [reconciliação](../../exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-04.md). Lotes adicionais",
    "MOC: linha de tranches",
)
moc.write_text(m, encoding="utf-8")
log.append("MOC: métricas 400, seção tranche 4 e link do relatório adicionados")

# ------------------------------------------------------------------- manifesto
man = KF / f"exports/batches/{BATCH}.md"
b = man.read_text(encoding="utf-8")
b = sub_once(b, "- Notas materiais redigidas: **300 / 2.000 (15,00%)**", "- Notas materiais redigidas: **400 / 2.000 (20,00%)**", "manifesto: redigidas")
b = sub_once(b, "- Gate automatizado: **300/300 aprovadas**", "- Gate automatizado: **400/400 aprovadas**", "manifesto: gate")
b = sub_once(b, "- Revisão factual humana: **0/300**", "- Revisão factual humana: **0/400**", "manifesto: humana")
b = sub_once(b, "- Revisão factual por IA: **300/300** (relatórios das tranches 1, 2 e 3)", "- Revisão factual por IA: **400/400** (relatórios das tranches 1, 2, 3 e 4)", "manifesto: ia")
b = sub_once(b, "- Notas válidas contabilizadas: **300/2.000 (15,00%)**", "- Notas válidas contabilizadas: **400/2.000 (20,00%)**", "manifesto: válidas")
b = sub_once(b, "- Estado: `in_progress` — tranches 1, 2 e 3 concluídas e reconciliadas; 17 tranches planejadas permanecem sem IDs reservados.", "- Estado: `in_progress` — tranches 1, 2, 3 e 4 concluídas e reconciliadas; 16 tranches planejadas permanecem sem IDs reservados.", "manifesto: estado")
b = sub_once(b, "As notas materiais existentes são somente os IDs 1–300, com arquivos e conteúdo; para as 1.700 notas", "As notas materiais existentes são somente os IDs 1–400, com arquivos e conteúdo; para as 1.600 notas", "manifesto: cadência")
man_lines = [
    "## Tranche 4 — WebGPU, WGSL, Bevy ECS, Unity Entities, Godot shaders, GDExtension, Blender cor/VSE, Web Audio, llama.cpp server e geração no Transformers (100 notas)",
    "",
    f"IDs materiais: `software.criacao_ia.tranche04.000301`–`software.criacao_ia.tranche04.000400`. Cada tópico tem fontes primárias específicas na própria nota; eixos com cobertura anterior (Playwright, OpenTelemetry, OpenAPI genérico) não foram reescritos.",
    "",
]
num = START
for title, notes in groups:
    man_lines.append(f"### {title}")
    man_lines.append("")
    for r in notes:
        man_lines.append(f"{num}. [{r['title']}](../../{NOTES_REL}/{r['slug']}.md) — `software.criacao_ia.tranche04.{num:06d}`")
        num += 1
    man_lines.append("")
if "## Tranche 4 — WebGPU" not in b:
    b = sub_once(b, "## Critério de entrada na contagem", "\n".join(man_lines) + "## Critério de entrada na contagem", "manifesto: âncora seção")
b = sub_once(
    b,
    "- Reconciliação da tranche 3: [`batch-reconciliation-software-criacao-ia-2000-0004-tranche-03.md`](../reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-03.md)",
    "- Reconciliação da tranche 3: [`batch-reconciliation-software-criacao-ia-2000-0004-tranche-03.md`](../reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-03.md)\n"
    "- Revisão factual IA da tranche 4: [`ai-review-software-criacao-ia-2000-0004-tranche-04.md`](../reports/ai-review-software-criacao-ia-2000-0004-tranche-04.md)\n"
    "- Gate da tranche 4: [`note-quality-software-criacao-ia-2000-0004-tranche-04.md`](../reports/note-quality-software-criacao-ia-2000-0004-tranche-04.md)\n"
    "- Reconciliação da tranche 4: [`batch-reconciliation-software-criacao-ia-2000-0004-tranche-04.md`](../reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-04.md)",
    "manifesto: artefatos",
)
man.write_text(b, encoding="utf-8")
log.append("manifesto: métricas 400/2.000, seção tranche 4 e artefatos linkados")

# ------------------------------------------------------ relatório de reconciliação
eixos = "\n".join(f"{i + 1}. {title}" for i, (title, _n) in enumerate(groups))
rec = KF / f"exports/reports/batch-reconciliation-{BATCH}-tranche-04.md"
rec.write_text(
    f"""# Reconciliação — `{BATCH}`, tranche 4

Data: {DATE}. Esta reconciliação contabiliza os arquivos substantivos produzidos na quarta tranche (IDs 301–400); o estado inicial de abertura continua preservado em [`batch-reconciliation-{BATCH}-initial.md`](batch-reconciliation-{BATCH}-initial.md), e as tranches anteriores em [`batch-reconciliation-{BATCH}-tranche-01.md`](batch-reconciliation-{BATCH}-tranche-01.md), [`batch-reconciliation-{BATCH}-tranche-02.md`](batch-reconciliation-{BATCH}-tranche-02.md) e [`batch-reconciliation-{BATCH}-tranche-03.md`](batch-reconciliation-{BATCH}-tranche-03.md).

## Escopo e resultado da tranche

- IDs materiais: `software.criacao_ia.tranche04.000301` a `software.criacao_ia.tranche04.000400`.
- Arquivos de nota: **100 novas notas** (totalizando 400 notas no diretório `{NOTES_REL}/`).
- Seleção: **10 trilhas × 10 notas**, cobrindo os eixos abaixo; a seleção foi verificada contra o inventário existente para não regravar cobertura anterior (Playwright, OpenTelemetry e OpenAPI da tranche 3 ficaram de fora).
- Gate da tranche: **100/100 aprovadas** (340 a 531 palavras por nota, duas fontes HTTPS primárias e específicas, seções obrigatórias completas e wikilinks resolvidos) — relatório `note-quality-{BATCH}-tranche-04.md`.
- Revisão factual por IA: **100/100**, registrada em `revisao_ia: aprovada`, com revisor `Arena.ai Agent Mode`, data `{DATE}` e relatório `ai-review-{BATCH}-tranche-04.md`.
- Revisão humana: **0/100**; nenhuma aprovação humana foi solicitada, registrada ou inferida.
- Contabilizadas no lote: **400/2.000 (20,00%)**; estado permanece `in_progress`.
- Próximas notas: **1.600** ainda não produzidas; não há IDs futuros reservados, placeholders ou progresso virtual.

## Trilhas selecionadas

{eixos}

## Evidências

- [Manifesto do lote e lista dos IDs/títulos](../batches/{BATCH}.md)
- [MOC do lote](../../00-home-vault/MOCs/MOC-Criacao-IA-Software-0010.md)
- [Revisão factual por IA, nota por nota](ai-review-{BATCH}-tranche-04.md)
- [Gate por arquivos da tranche](note-quality-{BATCH}-tranche-04.md)
- [Registro separado de revisões](human-review-queue.md), registros numerados 6341–6440
- [Auditoria global por arquivos e checkpoint](note-quality-audit.md)
- `python3 -m unittest discover -s knowledge-federation/tests -v`: **13 testes aprovados**.

## Reconciliação global após a tranche

| Métrica | Antes da tranche | Depois da tranche |
|---|---:|---:|
| Arquivos Markdown ativos em `domains/` | 6.440 | 6.540 |
| Notas válidas pelo protocolo | 6.340 | 6.440 |
| Aprovações humanas históricas | 49 | 49 |
| Revisões factuais por IA | 6.291 | 6.391 |
| Notas legadas com pendências, fora da contagem | 100 | 100 |
| Lotes completos | 3/500 | 3/500 |
| Lote 4 `{BATCH}` | 300/2.000 (15,00%) | 400/2.000 (20,00%) |

A auditoria global avaliou **6.540 arquivos**: 6.440 passaram o protocolo atual (49 revisões humanas históricas + 6.391 revisões por IA) e 100 notas legadas mantêm pendências. O checkpoint contém 1.000.000 de registros virtuais com template e 8.000 caminhos materializados; nenhum deles foi incluído na contagem editorial. A tranche 4 não altera o status `complete` dos três lotes anteriores nem abre o lote 5.
""",
    encoding="utf-8",
)
log.append(f"relatório de reconciliação criado: {rec.name}")

# ---------------------------------------------------------------------- STATUS
st = KF / "STATUS-CONSOLIDACAO-1M.md"
s = st.read_text(encoding="utf-8")
s = sub_once(s, "| Progresso válido global | 6340 / 1.000.000 (0,6340%) | 49 revisões humanas históricas + 6291 revisões por IA registradas separadamente |", "| Progresso válido global | 6440 / 1.000.000 (0,6440%) | 49 revisões humanas históricas + 6391 revisões por IA registradas separadamente |", "STATUS: progresso")
s = sub_once(s, "| Revisões factuais por IA registradas | 6291 | 5991 nos três lotes completos + 300 nas tranches 1–3 de `software-criacao-ia-2000-0004`; não são humanas |", "| Revisões factuais por IA registradas | 6391 | 5991 nos três lotes completos + 400 nas tranches 1–4 de `software-criacao-ia-2000-0004`; não são humanas |", "STATUS: ia")
s = sub_once(s, "| Quarto lote (`software-criacao-ia-2000-0004`) | 300 / 2.000 (15,00%) | Tranches 1–3 aprovadas no gate e revisadas por IA; 17 tranches planejadas ([manifesto](exports/batches/software-criacao-ia-2000-0004.md), [relatório](exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-03.md), [reconciliação](exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-03.md)) |", "| Quarto lote (`software-criacao-ia-2000-0004`) | 400 / 2.000 (20,00%) | Tranches 1–4 aprovadas no gate e revisadas por IA; 16 tranches planejadas ([manifesto](exports/batches/software-criacao-ia-2000-0004.md), [relatório](exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-04.md), [reconciliação](exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-04.md)) |", "STATUS: lote4")
s = sub_once(s, "| Candidatas que passaram pelo gate automatizado | 6340 |", "| Candidatas que passaram pelo gate automatizado | 6440 |", "STATUS: gate")
s = sub_once(s, "avançou a 300/2.000 após a tranche 3, registrada na [revisão factual](exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-03.md) e na [reconciliação](exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-03.md).", "avançou a 400/2.000 após a tranche 4, registrada na [revisão factual](exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-04.md) e na [reconciliação](exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-04.md).", "STATUS: narrativa")
s = sub_once(s, "[reconciliação da tranche 3 do lote 4](exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-03.md), [auditoria global]", "[reconciliação da tranche 4 do lote 4](exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-04.md), [auditoria global]", "STATUS: relatórios")
s = sub_once(s, "está em 300/2.000 após tranche 3, em `domains/software-0010/software/criacao-ia/`", "está em 400/2.000 após tranche 4, em `domains/software-0010/software/criacao-ia/`", "STATUS: passo 3")
st.write_text(s, encoding="utf-8")
log.append("STATUS-CONSOLIDACAO-1M.md atualizado")

# ----------------------------------------------------------------------- PLANO
pl = KF / "PLANO-CONTINUO-1M.md"
p = pl.read_text(encoding="utf-8")
p = sub_once(p, "- Notas válidas globais: **6340** (49 aprovações humanas históricas + 6291 revisões factuais por IA).", "- Notas válidas globais: **6440** (49 aprovações humanas históricas + 6391 revisões factuais por IA).", "PLANO: válidas")
p = sub_once(p, "- Progresso: **6340 / 1.000.000 (0,6340%)**; faltam **993.660** notas válidas.", "- Progresso: **6440 / 1.000.000 (0,6440%)**; faltam **993.560** notas válidas.", "PLANO: progresso")
p = sub_once(p, "- Quarto lote `software-criacao-ia-2000-0004`: **300 / 2.000 (15,00%)**; tranches 1–3 concluídas em `software-0010`, com 17 tranches planejadas sem IDs reservados.", "- Quarto lote `software-criacao-ia-2000-0004`: **400 / 2.000 (20,00%)**; tranches 1–4 concluídas em `software-0010`, com 16 tranches planejadas sem IDs reservados.", "PLANO: lote4")
p = sub_once(p, "- Arquivos Markdown ativos: **6440**; 100 com pendências de qualidade, excluídos da contagem.", "- Arquivos Markdown ativos: **6540**; 100 com pendências de qualidade, excluídos da contagem.", "PLANO: arquivos")
p = sub_once(p, "Global: 6440 arquivos, 6340 válidas, 100 com pendências legadas; lote 4 com 300/300 após tranche 3; veja a [reconciliação da tranche 3 do lote 4](exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-03.md).", "Global: 6540 arquivos, 6440 válidas, 100 com pendências legadas; lote 4 com 400/400 após tranche 4; veja a [reconciliação da tranche 4 do lote 4](exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-04.md).", "PLANO: tabela passo 5")
p = sub_once(p, "tem 300/2.000 e 17 tranches planejadas em", "tem 400/2.000 e 16 tranches planejadas em", "PLANO: tabela passo 8")
p = sub_once(p, "Progresso atual: 6340 notas válidas, 3/500 lotes completos.", "Progresso atual: 6440 notas válidas, 3/500 lotes completos.", "PLANO: passo 10")
pl.write_text(p, encoding="utf-8")
log.append("PLANO-CONTINUO-1M.md atualizado")

# -------------------------------------------------------------------- READMEs
r1 = KF / "README-1M.md"
x = r1.read_text(encoding="utf-8")
x = sub_once(x, "O estado ativo soma **6340 notas válidas** (49 aprovações humanas históricas + 6291 revisões factuais por IA) em **6440 arquivos Markdown**", "O estado ativo soma **6440 notas válidas** (49 aprovações humanas históricas + 6391 revisões factuais por IA) em **6540 arquivos Markdown**", "README-1M: soma")
x = sub_once(x, "avançou a 300/2.000, após a tranche 3 ([revisão factual IA](exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-03.md), [reconciliação](exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-03.md)).", "avançou a 400/2.000, após a tranche 4 ([revisão factual IA](exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-04.md), [reconciliação](exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-04.md)).", "README-1M: lote4")
r1.write_text(x, encoding="utf-8")
log.append("README-1M.md atualizado")

r2 = KF / "README.md"
x = r2.read_text(encoding="utf-8")
x = sub_once(x, "- Arquivos Markdown ativos: **6440** (100 notas legadas com pendências + 6340 notas autorais substantivas).", "- Arquivos Markdown ativos: **6540** (100 notas legadas com pendências + 6440 notas autorais substantivas).", "KF-README: arquivos")
x = sub_once(x, "- Notas válidas pelo protocolo atual: **6340** (49 aprovações humanas históricas + 6291 revisões factuais por IA).", "- Notas válidas pelo protocolo atual: **6440** (49 aprovações humanas históricas + 6391 revisões factuais por IA).", "KF-README: válidas")
x = sub_once(x, "- Progresso: **6340 / 1.000.000 (0,6340%)**; faltam 993.660 notas válidas.", "- Progresso: **6440 / 1.000.000 (0,6440%)**; faltam 993.560 notas válidas.", "KF-README: progresso")
x = sub_once(x, "- Quarto lote `software-criacao-ia-2000-0004`: **300 / 2.000 (15,00%)** notas válidas; tranches 1–3 concluídas e 17 tranches planejadas ([manifesto](exports/batches/software-criacao-ia-2000-0004.md), [revisão IA](exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-03.md), [gate](exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-03.md), [reconciliação](exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-03.md) e [MOC](00-home-vault/MOCs/MOC-Criacao-IA-Software-0010.md)).", "- Quarto lote `software-criacao-ia-2000-0004`: **400 / 2.000 (20,00%)** notas válidas; tranches 1–4 concluídas e 16 tranches planejadas ([manifesto](exports/batches/software-criacao-ia-2000-0004.md), [revisão IA](exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-04.md), [gate](exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-04.md), [reconciliação](exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-04.md) e [MOC](00-home-vault/MOCs/MOC-Criacao-IA-Software-0010.md)).", "KF-README: lote4")
x = sub_once(x, "o lote 4 está em 300/2.000 após a tranche 3 de engenharia e criação com IA ([revisão factual](exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-03.md), [gate](exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-03.md) e [reconciliação](exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-03.md)).", "o lote 4 está em 400/2.000 após a tranche 4 de engenharia e criação com IA ([revisão factual](exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-04.md), [gate](exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-04.md) e [reconciliação](exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-04.md)).", "KF-README: parágrafo final")
r2.write_text(x, encoding="utf-8")
log.append("knowledge-federation/README.md atualizado")

r3 = ROOT / "README.md"
x = r3.read_text(encoding="utf-8")
x = sub_once(x, "| Notas válidas contabilizadas | 6340 / 1.000.000 (0,6340%) | 49 com aprovação humana histórica + 6291 com revisão factual por IA |", "| Notas válidas contabilizadas | 6440 / 1.000.000 (0,6440%) | 49 com aprovação humana histórica + 6391 com revisão factual por IA |", "raiz-README: válidas")
x = sub_once(x, "| Notas com revisão factual por IA registrada | 6291 | Revisões dos três lotes completos (5991) + 300 notas nas tranches 1–3 do lote 4; não são humanas |", "| Notas com revisão factual por IA registrada | 6391 | Revisões dos três lotes completos (5991) + 400 notas nas tranches 1–4 do lote 4; não são humanas |", "raiz-README: ia")
x = sub_once(x, "| Quarto lote `software-criacao-ia-2000-0004` | 300 / 2.000 (15,00%) | Tranches 1–3 concluídas (300 IA); 17 tranches planejadas", "| Quarto lote `software-criacao-ia-2000-0004` | 400 / 2.000 (20,00%) | Tranches 1–4 concluídas (400 IA); 16 tranches planejadas", "raiz-README: lote4")
x = sub_once(x, "| Arquivos Markdown ativos em `knowledge-federation/domains/` | 6440 | 100 notas legadas com pendências + 6340 notas autorais substantivas |", "| Arquivos Markdown ativos em `knowledge-federation/domains/` | 6540 | 100 notas legadas com pendências + 6440 notas autorais substantivas |", "raiz-README: arquivos")
x = sub_once(x, "está em 300/2.000 após a tranche 3, com foco em engenharia e criação de programas, apps e jogos com IA ([revisão factual](knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-03.md), [reconciliação](knowledge-federation/exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-03.md), [auditoria da tranche](knowledge-federation/exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-03.md) e [MOC]", "está em 400/2.000 após a tranche 4, com foco em engenharia e criação de programas, apps e jogos com IA ([revisão factual](knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-04.md), [reconciliação](knowledge-federation/exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-04.md), [auditoria da tranche](knowledge-federation/exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-04.md) e [MOC]", "raiz-README: parágrafo")
r3.write_text(x, encoding="utf-8")
log.append("README.md raiz atualizado")

# ------------------------------------------------------------- RECOVERY + Home + Índice + PROMPT
rv = KF / "RECOVERY-AND-SCALE-NOTE.md"
x = rv.read_text(encoding="utf-8")
x = sub_once(x, "No diretório ativo `knowledge-federation/domains/` há **6440 arquivos**: 100 legados com pendências e **6340 notas válidas** pelo protocolo (49 aprovações humanas históricas + 6291 revisões factuais por IA). Os lotes 1–3 estão completos; o quarto lote `software-criacao-ia-2000-0004` tem 300/2.000 notas válidas após a tranche 3, com relatório factual, gate e reconciliação próprios.", "No diretório ativo `knowledge-federation/domains/` há **6540 arquivos**: 100 legados com pendências e **6440 notas válidas** pelo protocolo (49 aprovações humanas históricas + 6391 revisões factuais por IA). Os lotes 1–3 estão completos; o quarto lote `software-criacao-ia-2000-0004` tem 400/2.000 notas válidas após a tranche 4, com relatório factual, gate e reconciliação próprios.", "RECOVERY: estado")
rv.write_text(x, encoding="utf-8")
log.append("RECOVERY-AND-SCALE-NOTE.md atualizado")

hm = KF / "00-home-vault/Home.md"
x = hm.read_text(encoding="utf-8")
x = sub_once(x, "lote 4 `software-criacao-ia-2000-0004` com 300/2.000 após a tranche 3; 17 tranches planejadas, sem IDs reservados.", "lote 4 `software-criacao-ia-2000-0004` com 400/2.000 após a tranche 4; 16 tranches planejadas, sem IDs reservados.", "Home: MOC")
x = sub_once(x, "49 aprovações humanas e 6291 revisões factuais por IA, identificadas separadamente.", "49 aprovações humanas e 6391 revisões factuais por IA, identificadas separadamente.", "Home: fila")
x = sub_once(x, "6340 notas válidas pelo protocolo atual (49 humanas + 6291 IA)", "6440 notas válidas pelo protocolo atual (49 humanas + 6391 IA)", "Home: auditoria")
hm.write_text(x, encoding="utf-8")
log.append("Home.md atualizado")

ix = KF / "00-home-vault/Indice-Global.md"
x = ix.read_text(encoding="utf-8")
x = sub_once(x, "- Arquivos Markdown em `domains/`: **6440** (100 sementes legadas + 6340 notas autorais substantivas).", "- Arquivos Markdown em `domains/`: **6540** (100 sementes legadas + 6440 notas autorais substantivas).", "Índice: arquivos")
x = sub_once(x, "- Candidatas aprovadas no gate automatizado: **6340**; revisões humanas registradas: **49**; revisões factuais por IA: **6291**; 100 sementes legadas mantêm pendências.", "- Candidatas aprovadas no gate automatizado: **6440**; revisões humanas registradas: **49**; revisões factuais por IA: **6391**; 100 sementes legadas mantêm pendências.", "Índice: gate")
x = sub_once(x, "Os lotes atuais totalizam 6340 notas válidas pelo protocolo; os três primeiros lotes estão completos e o quarto lote `software-criacao-ia-2000-0004` avançou para 300/2.000 após a tranche 3, com revisão factual, gate e reconciliação próprios.", "Os lotes atuais totalizam 6440 notas válidas pelo protocolo; os três primeiros lotes estão completos e o quarto lote `software-criacao-ia-2000-0004` avançou para 400/2.000 após a tranche 4, com revisão factual, gate e reconciliação próprios.", "Índice: totalizadores")
x = sub_once(x, "- Quarto lote em andamento: [`software-criacao-ia-2000-0004`](../exports/batches/software-criacao-ia-2000-0004.md), 300/2.000 após tranche 3; consulte a [revisão factual](../exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-03.md), o [gate](../exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-03.md), a [reconciliação](../exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-03.md) e [[MOC-Criacao-IA-Software-0010]].", "- Quarto lote em andamento: [`software-criacao-ia-2000-0004`](../exports/batches/software-criacao-ia-2000-0004.md), 400/2.000 após tranche 4; consulte a [revisão factual](../exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-04.md), o [gate](../exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-04.md), a [reconciliação](../exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-04.md) e [[MOC-Criacao-IA-Software-0010]].", "Índice: quarto lote")
ix.write_text(x, encoding="utf-8")
log.append("Indice-Global.md atualizado")

pr = KF / "PROMPT-CONTINUACAO.md"
x = pr.read_text(encoding="utf-8")
x = sub_once(x, "- Estado: 6340 / 1.000.000 (0,6340%) válidas; 3/500 lotes completos; 6440 arquivos Markdown ativos (6340 válidas + 100 legadas com pendências, mantidas fora da contagem).", "- Estado: 6440 / 1.000.000 (0,6440%) válidas; 3/500 lotes completos; 6540 arquivos Markdown ativos (6440 válidas + 100 legadas com pendências, mantidas fora da contagem).", "PROMPT: estado")
x = sub_once(x, "- Lote 4 `software-criacao-ia-2000-0004`: 300/2.000 (15,00%), com tranches 1–3 concluídas (300 notas, IDs 1–300), 300 aprovadas pelo gate e 300 com revisão factual por IA; nenhuma aprovação humana nova; 17 tranches planejadas.", "- Lote 4 `software-criacao-ia-2000-0004`: 400/2.000 (20,00%), com as tranches 1–4 concluídas (400 notas, IDs 1–400), 400 aprovadas pelo gate e 400 com revisão factual por IA; nenhuma aprovação humana nova; 16 tranches planejadas.", "PROMPT: lote4")
x = sub_once(x, "- Relatórios do lote 4 tranche 3: `exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-03.md`, `exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-03.md` e `exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-03.md`.", "- Relatórios do lote 4 tranche 4: `exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-04.md`, `exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-04.md` e `exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-04.md`.", "PROMPT: relatórios")
x = sub_once(x, "1. Se o usuário pedir para avançar novamente, produzir a próxima tranche de 100 notas do lote 4", "1. Se o usuário pedir para avançar novamente, produzir a tranche 5 (de 16 planejadas restantes) com 100 notas do lote 4", "PROMPT: tarefa")
pr.write_text(x, encoding="utf-8")
log.append("PROMPT-CONTINUACAO.md atualizado")

print("\n".join(f"- {line}" for line in log))
print("Reconciliação da tranche 4 concluída.")
