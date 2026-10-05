#!/usr/bin/env python3
"""Reconciliation for software-criacao-ia-2000-0004 tranche 05 (IDs 401-500)."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KF = ROOT / "knowledge-federation"
DATA_DIR = Path(__file__).resolve().parent / "_criacao_ia_t05_data"
BATCH = "software-criacao-ia-2000-0004"
DATE = "2026-10-04"
START = 401
TR = "tranche-05"
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


def replace_between(text: str, start_marker: str, end_marker: str, replacement: str, label: str) -> str:
    if text.count(start_marker) != 1 or text.count(end_marker) != 1:
        raise ValueError(f"{label}: marcadores de seção não são únicos")
    start = text.index(start_marker)
    end = text.index(end_marker, start)
    if end <= start:
        raise ValueError(f"{label}: ordem dos marcadores inválida")
    return text[:start] + replacement + "\n\n" + text[end:]


rows, groups = load_rows()
log = []
pending_writes = []


def stage_write(path: Path, text: str) -> None:
    pending_writes.append((path, text))


link_audit = KF / "exports/reports/source-link-audit-software-criacao-ia-2000-0004-tranche-05.md"
if not link_audit.is_file():
    raise FileNotFoundError(f"auditoria de links ausente: {link_audit}")
link_audit_text = link_audit.read_text(encoding="utf-8")
for evidence in ("Referências examinadas: **200**", "IDs **401–500**", "wikilinks resolvidos: **100/100**"):
    if evidence not in link_audit_text:
        raise ValueError(f"auditoria de links sem evidência esperada: {evidence}")


# ---------------------------------------------------------------- fila humana
hrq = KF / "exports/reports/human-review-queue.md"
t = hrq.read_text(encoding="utf-8")
t = sub_once(
    t,
    'distingue 6391 revisões factuais realizadas por IA: `software-testes-2000-0001` (1991), `software-devops-2000-0002` (2000), `software-seguranca-2000-0003` (2000) e `software-criacao-ia-2000-0004` (400 nas tranches 1–4).',
    'distingue 6491 revisões factuais realizadas por IA: `software-testes-2000-0001` (1991), `software-devops-2000-0002` (2000), `software-seguranca-2000-0003` (2000) e `software-criacao-ia-2000-0004` (500 nas tranches 1–5).',
    "fila: cabeçalho",
)
t = sub_once(t, '- Aprovações por IA registradas separadamente: **6391**.', '- Aprovações por IA registradas separadamente: **6491**.', "fila: bullets IA")
t = sub_once(t, '- Notas válidas contabilizadas (gate + revisão humana ou IA): **6440**.', '- Notas válidas contabilizadas (gate + revisão humana ou IA): **6540**.', "fila: bullets válidas")
if "| 6441 |" not in t:
    new_rows = []
    for i, row in enumerate(rows):
        num = 6441 + i
        new_rows.append(
            f"| {num} | `{BATCH}` | [{row['title']}](../../{NOTES_REL}/{row['slug']}.md) | APROVADA POR IA | IA: Arena.ai Agent Mode | "
            f"Revisão factual por IA registrada em {DATE} no relatório `ai-review-{BATCH}-tranche-05.md` (nota {i + 1}); não é aprovação humana. |"
        )
    parts = t.split("## Regra de contagem")
    t = parts[0].rstrip() + "\n" + "\n".join(new_rows) + "\n\n## Regra de contagem" + parts[1]
t = sub_once(
    t,
    'As 6391 linhas `APROVADA POR IA` (nº 50–6440) correspondem',
    'As 6491 linhas `APROVADA POR IA` (nº 50–6540) correspondem',
    "fila: regra nº",
)
t = sub_once(
    t,
    'às 400 notas de IDs 1–400 das tranches 1–4 de',
    'às 500 notas de IDs 1–500 das tranches 1–5 de',
    "fila: regra tranches",
)
stage_write(hrq, t)
log.append("fila humana: linhas 6441–6540 + cabeçalho e regra atualizados")

# ------------------------------------------------------------------------ MOC
moc = KF / "00-home-vault/MOCs/MOC-Criacao-IA-Software-0010.md"
m = moc.read_text(encoding="utf-8")
m = sub_once(m, '- Progresso: **400 / 2.000 notas válidas (20,00%)** (`status: in_progress`).', '- Progresso: **500 / 2.000 notas válidas (25,00%)** (`status: in_progress`).', "MOC: progresso")
m = sub_once(m, '- Gate: **400/400**; revisão factual humana: **0/400**; revisão factual por IA: **400/400**.', '- Gate: **500/500**; revisão factual humana: **0/500**; revisão factual por IA: **500/500**.', "MOC: gate")
m = sub_once(m, '- Notas materiais presentes e contadas: **400**, IDs 000001–000400. Para as próximas 1.600 notas', '- Notas materiais presentes e contadas: **500**, IDs 000001–000500. Para as próximas 1.500 notas', "MOC: materiais")
m = sub_once(m, '- As tranches 1–4 foram selecionadas com documentação primária e concluídas em dez trilhas temáticas cada; as 16 tranches futuras e seus títulos ainda não estão decididos.', '- As tranches 1–5 foram selecionadas com documentação primária e concluídas em dez trilhas temáticas cada; as 15 tranches futuras e seus títulos ainda não estão decididos.', "MOC: cadência")
section = ["## Conteúdo materializado — tranche 5 (100 notas; IDs 000401–000500)", ""]
for title, notes in groups:
    section.append(f"### {title}")
    section.append("")
    for r in notes:
        section.append(f"- [[{r['slug']}]] — {r['title']}.")
    section.append("")
if "tranche 5 (100 notas; IDs 000401–000500)" not in m:
    m = sub_once(m, "## Mapa de escopo", "\n".join(section) + "## Mapa de escopo", "MOC: âncora seção")
m = sub_once(
    m,
    'Tranche 3: [revisão factual IA](../../exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-03.md), [gate](../../exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-03.md) e [reconciliação](../../exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-03.md). Tranche 4: [revisão factual IA](../../exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-04.md), [gate](../../exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-04.md) e [reconciliação](../../exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-04.md). Lotes adicionais',
    'Tranche 3: [revisão factual IA](../../exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-03.md), [gate](../../exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-03.md) e [reconciliação](../../exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-03.md). Tranche 4: [revisão factual IA](../../exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-04.md), [gate](../../exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-04.md) e [reconciliação](../../exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-04.md). Tranche 5: [revisão factual IA](../../exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-05.md), [gate](../../exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-05.md), [auditoria de links](../../exports/reports/source-link-audit-software-criacao-ia-2000-0004-tranche-05.md) e [reconciliação](../../exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-05.md). Lotes adicionais',
    "MOC: linha de tranches",
)
stage_write(moc, m)
log.append("MOC: métricas 500, seção tranche 5 e artefatos linkados")

# ------------------------------------------------------------------- manifesto
man = KF / f"exports/batches/{BATCH}.md"
b = man.read_text(encoding="utf-8")
b = sub_once(b, '- Notas materiais redigidas: **400 / 2.000 (20,00%)**', '- Notas materiais redigidas: **500 / 2.000 (25,00%)**', "manifesto: redigidas")
b = sub_once(b, '- Gate automatizado: **400/400 aprovadas**', '- Gate automatizado: **500/500 aprovadas**', "manifesto: gate")
b = sub_once(b, '- Revisão factual humana: **0/400**', '- Revisão factual humana: **0/500**', "manifesto: humana")
b = sub_once(b, '- Revisão factual por IA: **400/400** (relatórios das tranches 1, 2, 3 e 4)', '- Revisão factual por IA: **500/500** (relatórios das tranches 1, 2, 3, 4 e 5)', "manifesto: ia")
b = sub_once(b, '- Notas válidas contabilizadas: **400/2.000 (20,00%)**', '- Notas válidas contabilizadas: **500/2.000 (25,00%)**', "manifesto: válidas")
b = sub_once(b, '- Estado: `in_progress` — tranches 1, 2, 3 e 4 concluídas e reconciliadas; 16 tranches planejadas permanecem sem IDs reservados.', '- Estado: `in_progress` — tranches 1, 2, 3, 4 e 5 concluídas e reconciliadas; 15 tranches planejadas permanecem sem IDs reservados.', "manifesto: estado")
b = sub_once(b, 'As notas materiais existentes são somente os IDs 1–400, com arquivos e conteúdo; para as 1.600 notas', 'As notas materiais existentes são somente os IDs 1–500, com arquivos e conteúdo; para as 1.500 notas', "manifesto: cadência")
man_lines = [
    "## Tranche 5 — APIs e runtimes para criação assistida de software, jogos e documentação (100 notas)",
    "",
    f"IDs materiais: `software.criacao_ia.tranche05.000401`–`software.criacao_ia.tranche05.000500`. Os tópicos foram comparados ao inventário de 400 notas deste subdomínio e pesquisados no vault inteiro; cada nota cita duas fontes primárias específicas.",
    "",
]
num = START
for title, notes in groups:
    man_lines.append(f"### {title}")
    man_lines.append("")
    for r in notes:
        man_lines.append(f"{num}. [{r['title']}](../../{NOTES_REL}/{r['slug']}.md) — `software.criacao_ia.tranche05.{num:06d}`")
        num += 1
    man_lines.append("")
if "## Tranche 5 — APIs" not in b:
    b = sub_once(b, "## Critério de entrada na contagem", "\n".join(man_lines) + "## Critério de entrada na contagem", "manifesto: âncora seção")
b = sub_once(
    b,
    '- Reconciliação da tranche 3: [`batch-reconciliation-software-criacao-ia-2000-0004-tranche-03.md`](../reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-03.md)\n- Revisão factual IA da tranche 4: [`ai-review-software-criacao-ia-2000-0004-tranche-04.md`](../reports/ai-review-software-criacao-ia-2000-0004-tranche-04.md)\n- Gate da tranche 4: [`note-quality-software-criacao-ia-2000-0004-tranche-04.md`](../reports/note-quality-software-criacao-ia-2000-0004-tranche-04.md)\n- Reconciliação da tranche 4: [`batch-reconciliation-software-criacao-ia-2000-0004-tranche-04.md`](../reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-04.md)',
    '- Reconciliação da tranche 3: [`batch-reconciliation-software-criacao-ia-2000-0004-tranche-03.md`](../reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-03.md)\n- Revisão factual IA da tranche 4: [`ai-review-software-criacao-ia-2000-0004-tranche-04.md`](../reports/ai-review-software-criacao-ia-2000-0004-tranche-04.md)\n- Gate da tranche 4: [`note-quality-software-criacao-ia-2000-0004-tranche-04.md`](../reports/note-quality-software-criacao-ia-2000-0004-tranche-04.md)\n- Reconciliação da tranche 4: [`batch-reconciliation-software-criacao-ia-2000-0004-tranche-04.md`](../reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-04.md)\n- Revisão factual IA da tranche 5: [`ai-review-software-criacao-ia-2000-0004-tranche-05.md`](../reports/ai-review-software-criacao-ia-2000-0004-tranche-05.md)\n- Gate da tranche 5: [`note-quality-software-criacao-ia-2000-0004-tranche-05.md`](../reports/note-quality-software-criacao-ia-2000-0004-tranche-05.md)\n- Auditoria de links da tranche 5: [`source-link-audit-software-criacao-ia-2000-0004-tranche-05.md`](../reports/source-link-audit-software-criacao-ia-2000-0004-tranche-05.md)\n- Reconciliação da tranche 5: [`batch-reconciliation-software-criacao-ia-2000-0004-tranche-05.md`](../reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-05.md)\n',
    "manifesto: artefatos",
)
stage_write(man, b)
log.append("manifesto: métricas 500/2.000, seção tranche 5 e artefatos linkados")

# ------------------------------------------------------ relatório de reconciliação
eixos = "\n".join(f"{i + 1}. {title}" for i, (title, _n) in enumerate(groups))
rec = KF / f"exports/reports/batch-reconciliation-{BATCH}-tranche-05.md"
if rec.exists():
    raise FileExistsError(f"não sobrescrever reconciliação existente: {rec}")
if len(rows) != 100 or len(groups) != 10 or any(len(notes) != 10 for _title, notes in groups):
    raise ValueError("a reconciliação requer 100 notas em dez grupos de dez")
gate_path = KF / f"exports/reports/note-quality-{BATCH}-tranche-05.md"
review_path = KF / f"exports/reports/ai-review-{BATCH}-tranche-05.md"
if not gate_path.is_file() or not review_path.is_file():
    raise FileNotFoundError("gate final e relatório factual da tranche 5 são pré-requisitos")
gate_text = gate_path.read_text(encoding="utf-8")
for evidence in (
    "- Arquivos avaliados: **100**",
    "- Candidatas aprovadas no gate e prontas para revisão factual: **100**",
    "- Com revisão factual por IA aprovada e identificada: **100**",
    "- Notas válidas pelo protocolo atual (gate + aprovação humana ou IA): **100**",
):
    if evidence not in gate_text:
        raise ValueError(f"gate final não confirma tranche completa: {evidence}")
review_text = review_path.read_text(encoding="utf-8")
review_ids = [int(value) for value in re.findall(r"(?m)^\| (4[0-9]{2}|500) \|", review_text)]
if sorted(review_ids) != list(range(401, 501)):
    raise ValueError(f"relatório factual deve ter 100 registros (401–500), encontrados {len(review_ids)}")
for row in rows:
    note_path = KF / NOTES_REL / f"{row['slug']}.md"
    if not note_path.is_file():
        raise FileNotFoundError(note_path)
    text = note_path.read_text(encoding="utf-8")
    if f"id: software.criacao_ia.tranche05.{START + rows.index(row):06d}" not in text:
        raise ValueError(f"ID/frontmatter inesperado: {note_path}")
    for field_value in (
        "revisao_ia: aprovada",
        "revisor_ia: \"Arena.ai Agent Mode\"",
        "data_revisao_ia: 2026-10-04",
        f"relatorio_revisao_ia: \"knowledge-federation/exports/reports/ai-review-{BATCH}-tranche-05.md\"",
        "revisao_humana: nao_solicitada",
    ):
        if field_value not in text:
            raise ValueError(f"frontmatter sem {field_value}: {note_path.name}")

eixos = "\n".join(f"{i + 1}. {title}" for i, (title, _n) in enumerate(groups))
rec_text = f"""# Reconciliação — `{BATCH}`, tranche 5

Data: {DATE}. Esta reconciliação contabiliza somente as 100 notas materiais da tranche 5 (IDs 401–500). Preserva as reconciliações anteriores [`tranche 1`](batch-reconciliation-{BATCH}-tranche-01.md), [`tranche 2`](batch-reconciliation-{BATCH}-tranche-02.md), [`tranche 3`](batch-reconciliation-{BATCH}-tranche-03.md) e [`tranche 4`](batch-reconciliation-{BATCH}-tranche-04.md).

## Escopo, seleção e resultado

- IDs materiais: `software.criacao_ia.tranche05.000401` a `software.criacao_ia.tranche05.000500`.
- Arquivos novos: **100 notas**; o diretório `{NOTES_REL}/` passa de 400 para 500 notas deste lote.
- Seleção: **10 grupos × 10 notas**. Antes da geração, `git ls-files knowledge-federation/domains/software-0010/software/criacao-ia/` forneceu o inventário de 400 notas; títulos/slugs candidatos foram comparados com o inventário e pesquisados no vault inteiro. Resultado: **0 slugs ou títulos exatos duplicados**.
- Cobertura próxima foi mantida distinta: notas ComfyUI anteriores tratam workflows/produção; esta tranche trata a Server API. Ollama anterior cobre configuração local, `num_ctx`, `keep_alive` e embeddings no Continue.dev; esta tranche cobre contratos REST. Também foram encontrados temas adjacentes de Storybook/MSW/Backstage, importação genérica de assets Godot e Unity ECS, sem repetir esses focos.
- Gate final por arquivo: **100/100 aprovadas**, 209–301 palavras por nota, exatamente duas fontes HTTPS específicas e wikilinks resolvidos. O gate foi repetido depois do registro factual; evidência em [`note-quality-{BATCH}-tranche-05.md`](note-quality-{BATCH}-tranche-05.md).
- Revisão factual por IA: **100/100**, com registro por ID em [`ai-review-{BATCH}-tranche-05.md`](ai-review-{BATCH}-tranche-05.md). A revisão humana é **0/100**; as 49 aprovações humanas históricas permanecem inalteradas.
- Auditoria de links: **200 referências** em 100 notas, todas HTTPS; relatório [`source-link-audit-software-criacao-ia-2000-0004-tranche-05.md`](source-link-audit-software-criacao-ia-2000-0004-tranche-05.md). O relatório distingue a resolução interna do gate da checagem HTTP externa e documenta respostas TLS não conclusivas do sandbox.
- Contagem do lote 4: **500/2.000 (25,00%)**. Permanecem 1.500 notas não produzidas; nenhum ID futuro foi atribuído ou reservado e o lote 5 não foi aberto.

## Grupos selecionados

{eixos}

## Evidências e artefatos

- [Manifesto do lote, métricas e IDs/títulos](../batches/{BATCH}.md)
- [MOC do lote](../../00-home-vault/MOCs/MOC-Criacao-IA-Software-0010.md)
- [Auditoria de links externos e wiki](source-link-audit-software-criacao-ia-2000-0004-tranche-05.md)
- [Gate final da tranche](note-quality-{BATCH}-tranche-05.md)
- [Revisão factual por IA, registro por nota](ai-review-{BATCH}-tranche-05.md)
- [Fila separada de revisão humana](human-review-queue.md), linhas 6441–6540 (decisões IA não são aprovações humanas)
- [Auditoria global de qualidade e checkpoint](note-quality-audit.md), executada após esta reconciliação conforme o protocolo.

## Reconciliação global após a tranche

| Métrica | Antes | Depois |
|---|---:|---:|
| Arquivos Markdown ativos em `domains/` | 6.540 | 6.640 |
| Notas válidas pelo protocolo | 6.440 | 6.540 |
| Aprovações humanas históricas | 49 | 49 |
| Revisões factuais por IA | 6.391 | 6.491 |
| Notas legadas com pendências, fora da contagem | 100 | 100 |
| Lotes completos | 3/500 | 3/500 |
| Lote 4 `{BATCH}` | 400/2.000 (20,00%) | 500/2.000 (25,00%) |

Após a tranche, o total é **6.540 notas válidas** (49 humanas históricas + 6.491 revisões factuais por IA) em **6.640 arquivos Markdown ativos**, mantendo as 100 notas legadas fora da contagem. Restam **993.460** notas para a meta de 1.000.000. O checkpoint histórico de 1.000.000 registros virtuais e 8.000 caminhos materializados continua excluído da contagem; o estado `complete` dos três lotes anteriores não muda. As 15 tranches planejadas restantes são cadência, não reserva de IDs. Não abrir lote 5 nem atribuir IDs futuros automaticamente.

## Verificações globais obrigatórias antes de publicar

Executar, conforme `PROMPT-CONTINUACAO.md`, os testes unitários e a auditoria global sobre `knowledge-federation/domains` mais o arquivo de ledger. Os resultados desses comandos não são substituídos pelo gate da tranche.
"""
stage_write(rec, rec_text)
log.append(f"relatório de reconciliação preparado: {rec.name}")

# ---------------------------------------------------------------------- STATUS
st = KF / "STATUS-CONSOLIDACAO-1M.md"
s = st.read_text(encoding="utf-8")
s = sub_once(s, '| Progresso válido global | 6440 / 1.000.000 (0,6440%) | 49 revisões humanas históricas + 6391 revisões por IA registradas separadamente |', '| Progresso válido global | 6540 / 1.000.000 (0,6540%) | 49 revisões humanas históricas + 6491 revisões por IA registradas separadamente |', "STATUS: progresso")
s = sub_once(s, '| Revisões factuais por IA registradas | 6391 | 5991 nos três lotes completos + 400 nas tranches 1–4 de `software-criacao-ia-2000-0004`; não são humanas |', '| Revisões factuais por IA registradas | 6491 | 5991 nos três lotes completos + 500 nas tranches 1–5 de `software-criacao-ia-2000-0004`; não são humanas |', "STATUS: ia")
s = sub_once(s, '| Quarto lote (`software-criacao-ia-2000-0004`) | 400 / 2.000 (20,00%) | Tranches 1–4 aprovadas no gate e revisadas por IA; 16 tranches planejadas ([manifesto](exports/batches/software-criacao-ia-2000-0004.md), [relatório](exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-04.md), [reconciliação](exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-04.md)) |', '| Quarto lote (`software-criacao-ia-2000-0004`) | 500 / 2.000 (25,00%) | Tranches 1–5 aprovadas no gate e revisadas por IA; 15 tranches planejadas ([manifesto](exports/batches/software-criacao-ia-2000-0004.md), [relatório](exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-05.md), [reconciliação](exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-05.md)) |', "STATUS: lote4")
s = sub_once(s, '| Candidatas que passaram pelo gate automatizado | 6440 |', '| Candidatas que passaram pelo gate automatizado | 6540 |', "STATUS: gate")
s = sub_once(s, 'avançou a 400/2.000 após a tranche 4, registrada na [revisão factual](exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-04.md) e na [reconciliação](exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-04.md).', 'avançou a 500/2.000 após a tranche 5, registrada na [revisão factual](exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-05.md) e na [reconciliação](exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-05.md).', "STATUS: narrativa")
s = sub_once(s, '[reconciliação da tranche 4 do lote 4](exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-04.md), [auditoria global]', '[reconciliação da tranche 5 do lote 4](exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-05.md), [auditoria global]', "STATUS: relatórios")
s = sub_once(s, 'está em 400/2.000 após tranche 4, em `domains/software-0010/software/criacao-ia/`', 'está em 500/2.000 após tranche 5, em `domains/software-0010/software/criacao-ia/`', "STATUS: passo 3")
s = sub_once(
    s,
    "A auditoria encontrou 6.440 arquivos Markdown ativos: 6.340 notas substantivas passaram pelo gate e receberam revisão factual registrada (49 humanas históricas + 6.291 por IA); outras 100 mantêm pendências e continuam fora da contagem.",
    "A auditoria encontrou 6.640 arquivos Markdown ativos: 6.540 notas substantivas passaram pelo gate e receberam revisão factual registrada (49 humanas históricas + 6.491 por IA); outras 100 mantêm pendências e continuam fora da contagem.",
    "STATUS: resumo honesto",
)
stage_write(st, s)
log.append("STATUS-CONSOLIDACAO-1M.md atualizado")

# ----------------------------------------------------------------------- PLANO
pl = KF / "PLANO-CONTINUO-1M.md"
p = pl.read_text(encoding="utf-8")
p = sub_once(p, '- Notas válidas globais: **6440** (49 aprovações humanas históricas + 6391 revisões factuais por IA).', '- Notas válidas globais: **6540** (49 aprovações humanas históricas + 6491 revisões factuais por IA).', "PLANO: válidas")
p = sub_once(p, '- Progresso: **6440 / 1.000.000 (0,6440%)**; faltam **993.560** notas válidas.', '- Progresso: **6540 / 1.000.000 (0,6540%)**; faltam **993.460** notas válidas.', "PLANO: progresso")
p = sub_once(p, '- Quarto lote `software-criacao-ia-2000-0004`: **400 / 2.000 (20,00%)**; tranches 1–4 concluídas em `software-0010`, com 16 tranches planejadas sem IDs reservados.', '- Quarto lote `software-criacao-ia-2000-0004`: **500 / 2.000 (25,00%)**; tranches 1–5 concluídas em `software-0010`, com 15 tranches planejadas sem IDs reservados.', "PLANO: lote4")
p = sub_once(p, '- Arquivos Markdown ativos: **6540**; 100 com pendências de qualidade, excluídos da contagem.', '- Arquivos Markdown ativos: **6640**; 100 com pendências de qualidade, excluídos da contagem.', "PLANO: arquivos")
p = sub_once(p, 'Global: 6540 arquivos, 6440 válidas, 100 com pendências legadas; lote 4 com 400/400 após tranche 4; veja a [reconciliação da tranche 4 do lote 4](exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-04.md).', 'Global: 6640 arquivos, 6540 válidas, 100 com pendências legadas; lote 4 com 500/500 após tranche 5; veja a [reconciliação da tranche 5 do lote 4](exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-05.md).', "PLANO: tabela passo 5")
p = sub_once(p, 'tem 400/2.000 e 16 tranches planejadas em', 'tem 500/2.000 e 15 tranches planejadas em', "PLANO: tabela passo 8")
p = sub_once(p, 'Progresso atual: 6440 notas válidas, 3/500 lotes completos.', 'Progresso atual: 6540 notas válidas, 3/500 lotes completos.', "PLANO: passo 10")
stage_write(pl, p)
log.append("PLANO-CONTINUO-1M.md atualizado")

# -------------------------------------------------------------------- READMEs
r1 = KF / "README-1M.md"
x = r1.read_text(encoding="utf-8")
x = sub_once(x, 'O estado ativo soma **6440 notas válidas** (49 aprovações humanas históricas + 6391 revisões factuais por IA) em **6540 arquivos Markdown**', 'O estado ativo soma **6540 notas válidas** (49 aprovações humanas históricas + 6491 revisões factuais por IA) em **6640 arquivos Markdown**', "README-1M: soma")
x = sub_once(x, 'avançou a 400/2.000, após a tranche 4 ([revisão factual IA](exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-04.md), [reconciliação](exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-04.md)).', 'avançou a 500/2.000, após a tranche 5 ([revisão factual IA](exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-05.md), [reconciliação](exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-05.md)).', "README-1M: lote4")
stage_write(r1, x)
log.append("README-1M.md atualizado")

r2 = KF / "README.md"
x = r2.read_text(encoding="utf-8")
x = sub_once(x, '- Arquivos Markdown ativos: **6540** (100 notas legadas com pendências + 6440 notas autorais substantivas).', '- Arquivos Markdown ativos: **6640** (100 notas legadas com pendências + 6540 notas autorais substantivas).', "KF-README: arquivos")
x = sub_once(x, '- Notas válidas pelo protocolo atual: **6440** (49 aprovações humanas históricas + 6391 revisões factuais por IA).', '- Notas válidas pelo protocolo atual: **6540** (49 aprovações humanas históricas + 6491 revisões factuais por IA).', "KF-README: válidas")
x = sub_once(x, '- Progresso: **6440 / 1.000.000 (0,6440%)**; faltam 993.560 notas válidas.', '- Progresso: **6540 / 1.000.000 (0,6540%)**; faltam 993.460 notas válidas.', "KF-README: progresso")
x = sub_once(x, '- Quarto lote `software-criacao-ia-2000-0004`: **400 / 2.000 (20,00%)** notas válidas; tranches 1–4 concluídas e 16 tranches planejadas ([manifesto](exports/batches/software-criacao-ia-2000-0004.md), [revisão IA](exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-04.md), [gate](exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-04.md), [reconciliação](exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-04.md) e [MOC](00-home-vault/MOCs/MOC-Criacao-IA-Software-0010.md)).', '- Quarto lote `software-criacao-ia-2000-0004`: **500 / 2.000 (25,00%)** notas válidas; tranches 1–5 concluídas e 15 tranches planejadas ([manifesto](exports/batches/software-criacao-ia-2000-0004.md), [revisão IA](exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-05.md), [gate](exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-05.md), [reconciliação](exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-05.md) e [MOC](00-home-vault/MOCs/MOC-Criacao-IA-Software-0010.md)).', "KF-README: lote4")
x = sub_once(x, 'o lote 4 está em 400/2.000 após a tranche 4 de engenharia e criação com IA ([revisão factual](exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-04.md), [gate](exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-04.md) e [reconciliação](exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-04.md)).', 'o lote 4 está em 500/2.000 após a tranche 5 de engenharia e criação com IA ([revisão factual](exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-05.md), [gate](exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-05.md) e [reconciliação](exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-05.md)).', "KF-README: parágrafo final")
stage_write(r2, x)
log.append("knowledge-federation/README.md atualizado")

r3 = ROOT / "README.md"
x = r3.read_text(encoding="utf-8")
x = sub_once(x, '| Notas válidas contabilizadas | 6440 / 1.000.000 (0,6440%) | 49 com aprovação humana histórica + 6391 com revisão factual por IA |', '| Notas válidas contabilizadas | 6540 / 1.000.000 (0,6540%) | 49 com aprovação humana histórica + 6491 com revisão factual por IA |', "raiz-README: válidas")
x = sub_once(x, '| Notas com revisão factual por IA registrada | 6391 | Revisões dos três lotes completos (5991) + 400 notas nas tranches 1–4 do lote 4; não são humanas |', '| Notas com revisão factual por IA registrada | 6491 | Revisões dos três lotes completos (5991) + 500 notas nas tranches 1–5 do lote 4; não são humanas |', "raiz-README: ia")
x = sub_once(x, '| Quarto lote `software-criacao-ia-2000-0004` | 400 / 2.000 (20,00%) | Tranches 1–4 concluídas (400 IA); 16 tranches planejadas', '| Quarto lote `software-criacao-ia-2000-0004` | 500 / 2.000 (25,00%) | Tranches 1–5 concluídas (500 IA); 15 tranches planejadas', "raiz-README: lote4")
x = sub_once(x, '| Arquivos Markdown ativos em `knowledge-federation/domains/` | 6540 | 100 notas legadas com pendências + 6440 notas autorais substantivas |', '| Arquivos Markdown ativos em `knowledge-federation/domains/` | 6640 | 100 notas legadas com pendências + 6540 notas autorais substantivas |', "raiz-README: arquivos")
x = sub_once(x, 'está em 400/2.000 após a tranche 4, com foco em engenharia e criação de programas, apps e jogos com IA ([revisão factual](knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-04.md), [reconciliação](knowledge-federation/exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-04.md), [auditoria da tranche](knowledge-federation/exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-04.md) e [MOC]', 'está em 500/2.000 após a tranche 5, com foco em engenharia e criação de programas, apps e jogos com IA ([revisão factual](knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-05.md), [reconciliação](knowledge-federation/exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-05.md), [auditoria da tranche](knowledge-federation/exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-05.md) e [MOC]', "raiz-README: parágrafo")
stage_write(r3, x)
log.append("README.md raiz atualizado")

# ------------------------------------------------------------- RECOVERY + Home + Índice + PROMPT
rv = KF / "RECOVERY-AND-SCALE-NOTE.md"
x = rv.read_text(encoding="utf-8")
x = sub_once(x, 'No diretório ativo `knowledge-federation/domains/` há **6540 arquivos**: 100 legados com pendências e **6440 notas válidas** pelo protocolo (49 aprovações humanas históricas + 6391 revisões factuais por IA). Os lotes 1–3 estão completos; o quarto lote `software-criacao-ia-2000-0004` tem 400/2.000 notas válidas após a tranche 4, com relatório factual, gate e reconciliação próprios.', 'No diretório ativo `knowledge-federation/domains/` há **6640 arquivos**: 100 legados com pendências e **6540 notas válidas** pelo protocolo (49 aprovações humanas históricas + 6491 revisões factuais por IA). Os lotes 1–3 estão completos; o quarto lote `software-criacao-ia-2000-0004` tem 500/2.000 notas válidas após a tranche 5, com relatório factual, gate e reconciliação próprios.', "RECOVERY: estado")
stage_write(rv, x)
log.append("RECOVERY-AND-SCALE-NOTE.md atualizado")

hm = KF / "00-home-vault/Home.md"
x = hm.read_text(encoding="utf-8")
x = sub_once(x, 'lote 4 `software-criacao-ia-2000-0004` com 400/2.000 após a tranche 4; 16 tranches planejadas, sem IDs reservados.', 'lote 4 `software-criacao-ia-2000-0004` com 500/2.000 após a tranche 5; 15 tranches planejadas, sem IDs reservados.', "Home: MOC")
x = sub_once(x, '49 aprovações humanas e 6391 revisões factuais por IA, identificadas separadamente.', '49 aprovações humanas e 6491 revisões factuais por IA, identificadas separadamente.', "Home: fila")
x = sub_once(x, '6440 notas válidas pelo protocolo atual (49 humanas + 6391 IA)', '6540 notas válidas pelo protocolo atual (49 humanas + 6491 IA)', "Home: auditoria")
stage_write(hm, x)
log.append("Home.md atualizado")

ix = KF / "00-home-vault/Indice-Global.md"
x = ix.read_text(encoding="utf-8")
x = sub_once(x, '- Arquivos Markdown em `domains/`: **6540** (100 sementes legadas + 6440 notas autorais substantivas).', '- Arquivos Markdown em `domains/`: **6640** (100 sementes legadas + 6540 notas autorais substantivas).', "Índice: arquivos")
x = sub_once(x, '- Candidatas aprovadas no gate automatizado: **6440**; revisões humanas registradas: **49**; revisões factuais por IA: **6391**; 100 sementes legadas mantêm pendências.', '- Candidatas aprovadas no gate automatizado: **6540**; revisões humanas registradas: **49**; revisões factuais por IA: **6491**; 100 sementes legadas mantêm pendências.', "Índice: gate")
x = sub_once(x, 'Os lotes atuais totalizam 6440 notas válidas pelo protocolo; os três primeiros lotes estão completos e o quarto lote `software-criacao-ia-2000-0004` avançou para 400/2.000 após a tranche 4, com revisão factual, gate e reconciliação próprios.', 'Os lotes atuais totalizam 6540 notas válidas pelo protocolo; os três primeiros lotes estão completos e o quarto lote `software-criacao-ia-2000-0004` avançou para 500/2.000 após a tranche 5, com revisão factual, gate e reconciliação próprios.', "Índice: totalizadores")
x = sub_once(x, '- Quarto lote em andamento: [`software-criacao-ia-2000-0004`](../exports/batches/software-criacao-ia-2000-0004.md), 400/2.000 após tranche 4; consulte a [revisão factual](../exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-04.md), o [gate](../exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-04.md), a [reconciliação](../exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-04.md) e [[MOC-Criacao-IA-Software-0010]].', '- Quarto lote em andamento: [`software-criacao-ia-2000-0004`](../exports/batches/software-criacao-ia-2000-0004.md), 500/2.000 após tranche 5; consulte a [revisão factual](../exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-05.md), o [gate](../exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-05.md), a [reconciliação](../exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-05.md) e [[MOC-Criacao-IA-Software-0010]].', "Índice: quarto lote")
stage_write(ix, x)
log.append("Indice-Global.md atualizado")

pr = KF / "PROMPT-CONTINUACAO.md"
x = pr.read_text(encoding="utf-8")
x = sub_once(x, '- Estado: 6440 / 1.000.000 (0,6440%) válidas; 3/500 lotes completos; 6540 arquivos Markdown ativos (6440 válidas + 100 legadas com pendências, mantidas fora da contagem).', '- Estado: 6540 / 1.000.000 (0,6540%) válidas; 3/500 lotes completos; 6640 arquivos Markdown ativos (6540 válidas + 100 legadas com pendências, mantidas fora da contagem).', "PROMPT: estado")
x = sub_once(x, '- Lote 4 `software-criacao-ia-2000-0004`: 400/2.000 (20,00%), com as tranches 1–4 concluídas (400 notas, IDs 1–400), 400 aprovadas pelo gate e 400 com revisão factual por IA; nenhuma aprovação humana nova; 16 tranches planejadas.', '- Lote 4 `software-criacao-ia-2000-0004`: 500/2.000 (25,00%), com as tranches 1–5 concluídas (500 notas, IDs 1–500), 500 aprovadas pelo gate e 500 com revisão factual por IA; nenhuma aprovação humana nova; 15 tranches planejadas.', "PROMPT: lote4")
x = sub_once(x, '- Relatórios do lote 4 tranche 4: `exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-04.md`, `exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-04.md` e `exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-04.md`.', '- Relatórios do lote 4 tranche 5: `exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-05.md`, `exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-05.md` e `exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-05.md`.', "PROMPT: relatórios")
x = sub_once(
    x,
    "- A tranche 4 foi integrada à `main` pelo PR #9; a tranche 5 recomeça do próximo ID livre (401), sem nenhuma reserva prévia.",
    "- IDs 401–500 pertencem à tranche 5 concluída neste fluxo; nenhum ID posterior foi reservado e o lote 5 permanece fechado.",
    "PROMPT: registro da tranche",
)
x = replace_between(
    x,
    "HANDOFF OPERACIONAL DA TRANCHE 5 (padrão estabelecido nas tranches 2–4):",
    "VERIFICAÇÃO OBRIGATÓRIA ANTES DE CADA PUSH:",
    """RESULTADO DA TRANCHE 5 — NÃO AVANÇAR AUTOMATICAMENTE
- Tranche 5 materializada: 100 notas, IDs 401–500, em `domains/software-0010/software/criacao-ia/`; 100/100 passaram o gate e receberam revisão factual por IA. Revisão humana nova: 0; as 49 aprovações históricas não mudam.
- Artefatos: manifesto do lote, gate final, revisão factual, auditoria de links e reconciliação da tranche 5; fila humana numerada nas linhas 6441–6540.
- Estado esperado: 6.640 arquivos Markdown em `domains/`, 6.540 válidas (49 humanas + 6.491 IA), 100 legadas fora da contagem; lote 4 em 500/2.000 (25,00%), 15 tranches planejadas; faltam 993.460 notas.
- Não reservar IDs além de 500, não abrir o lote 5 nem produzir outra tranche sem solicitação explícita do usuário. Se solicitado, atualizar inventário e busca em todo o vault, selecionar temas não duplicados e conferir fontes primárias específicas antes de atribuir IDs apenas à tranche solicitada.
- Não tocar nos relatórios/reconciliações das tranches 1–4, `LOTS-201-300.md`, `MOC-Seguranca-Software-0009.md`, `archives/LATEST-LEDGER.txt` ou no dump `.xz`; `LOT-SEQUENCE` e `_meta/plano-execucao` não mudam por tranche.

TAREFA IMEDIATA:
1. A tranche 5 foi reconciliada; não iniciar tranche 6 nem lote 5 automaticamente.
2. Antes de qualquer push, executar os testes unitários e a auditoria global listados abaixo.
3. Publicar somente na branch da sessão e abrir PR para `main`, sem atribuir IDs futuros.""",
    "PROMPT: handoff concluído",
)
stage_write(pr, x)
log.append("PROMPT-CONTINUACAO.md atualizado")

for path, text in pending_writes:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
print("\n".join(f"- {line}" for line in log))
print("Reconciliação da tranche 5 concluída.")
