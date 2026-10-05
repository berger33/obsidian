#!/usr/bin/env python3
"""Record the tranche-05 factual review and patch the 100 note frontmatters."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KF = ROOT / "knowledge-federation"
NOTES_DIR = KF / "domains" / "software-0010" / "software" / "criacao-ia"
DATA_DIR = Path(__file__).resolve().parent / "_criacao_ia_t05_data"
BATCH_ID = "software-criacao-ia-2000-0004"
DATE = "2026-10-04"
START = 401
COUNT = 100
REPORT_REL = f"knowledge-federation/exports/reports/ai-review-{BATCH_ID}-tranche-05.md"
REPORT_PATH = KF / "exports" / "reports" / f"ai-review-{BATCH_ID}-tranche-05.md"
GATE_PATH = KF / "exports" / "reports" / f"note-quality-{BATCH_ID}-tranche-05.md"


def load_groups() -> list[dict]:
    groups = []
    for path in sorted(DATA_DIR.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict) or not isinstance(data.get("notes"), list):
            raise ValueError(f"Formato inválido: {path.name}")
        groups.append(data)
    if len(groups) != 10 or any(len(group["notes"]) != 10 for group in groups):
        raise ValueError("A revisão exige dez grupos de dez notas cada")
    return groups


def load_rows() -> tuple[list[dict], list[dict]]:
    groups = load_groups()
    rows = [row for group in groups for row in group["notes"]]
    if len(rows) != COUNT:
        raise ValueError(f"Esperadas {COUNT} notas, encontradas {len(rows)}")
    for row in rows:
        if len(row.get("sources", [])) != 2:
            raise ValueError(f"{row.get('slug', '?')}: esperadas duas fontes específicas")
        if not row.get("review", "").strip():
            raise ValueError(f"{row.get('slug', '?')}: decisão factual vazia")
        for source in row["sources"]:
            if not source.get("url", "").startswith("https://"):
                raise ValueError(f"{row['slug']}: fonte não HTTPS")
    return rows, groups


def validate_initial_gate() -> None:
    if not GATE_PATH.is_file():
        raise FileNotFoundError(
            f"Execute primeiro o gate da tranche 5 e gere {GATE_PATH.relative_to(ROOT)}"
        )
    report = GATE_PATH.read_text(encoding="utf-8")
    expected_lines = (
        "- Arquivos avaliados: **100**",
        "- Candidatas aprovadas no gate e prontas para revisão factual: **100**",
    )
    missing = [line for line in expected_lines if line not in report]
    if missing:
        raise ValueError(f"Gate não confirma 100 notas prontas: {missing}")


def build_report(rows: list[dict], groups: list[dict]) -> str:
    lines = [
        "---",
        "tipo: revisao-factual-ia",
        f"lote: {BATCH_ID}",
        "tranche: 05",
        f"data: {DATE}",
        "resultado: aprovada",
        "---",
        "",
        f"# Revisão factual por IA — lote `{BATCH_ID}`, tranche 5 (IDs {START:06d}–{START + COUNT - 1:06d})",
        "",
        f"- Data: {DATE}",
        "- Revisor: `Arena.ai Agent Mode`",
        "- Escopo: **100 notas**, IDs 401–500, em dez grupos de dez; cada registro abaixo confere a alegação central, o procedimento, os limites e os exemplos contra duas fontes HTTPS específicas da própria nota.",
        "- Método: revisão das fontes primárias oficiais indicadas em cada registro, com atenção a nomes de eventos/endpoints, defaults, versões, ciclos de vida, condições de erro e distinção entre comportamento documentado e recomendações de implementação. Afirmações que não encontrei nas fontes foram removidas ou limitadas; exemplos de produto foram mantidos como cenários, não como garantias da ferramenta.",
        "- Fontes e escopo de versão: Ollama API; ComfyUI Server e Comfy API v2; Godot 4.7 stable API; Unity Sentis 2.5 e Addressables 2.7.6; OpenAI Realtime API GA; Vercel AI SDK 5; Storybook 10.6; Docusaurus 3.10.2; repositório/runtime oficial Ink; documentação oficial atual do Storybook e Docusaurus. A cobertura é deliberadamente específica às versões e páginas citadas em cada nota.",
        "- Retificações aplicadas durante a conferência: ComfyUI `executed` foi separado do fim (`executing` com `node: null`) e do sucesso explícito (`execution_success`); `/upload/mask` foi identificado como fluxo especializado que usa `original_ref`; Comfy API v2 foi diferenciada das rotas diretas do servidor e da Cloud API v1 depreciada. No Storybook, loaders assíncronos substituíram a candidata redundante de mocks MSW por story. Em OpenAI Realtime, o fluxo push-to-talk foi qualificado por transporte.",
        "- Ressalvas de fonte: a página tutorial de Godot `Import plugins` sinaliza conteúdo ainda em atualização para 4.7; os contratos de método usados nas notas foram conferidos na referência de classe `EditorImportPlugin` da documentação stable 4.7. Páginas genéricas WebRTC/WebSocket que apresentavam GPT-Live não foram usadas para claims da Realtime API; as notas usam guias `realtime-*` e referências Realtime específicas.",
        "- Resultado: **100/100 revisões factuais por IA registradas**. Isso não certifica exatidão futura nem substitui revisão humana; a contagem de aprovações humanas permanece inalterada.",
        "- Revisão humana: **0/100**; nenhuma aprovação humana foi solicitada, registrada ou inferida. As 49 aprovações humanas históricas permanecem separadas e inalteradas.",
        "",
        "## Trilhas verificadas",
        "",
    ]
    for group in groups:
        lines.append(f"- {group['group']} — 10 notas.")
    lines.extend(
        [
            "",
            "## Registro por nota",
            "",
            "| ID | Nota | Fontes primárias consultadas | Verificação factual / decisão |",
            "|---:|---|---|---|",
        ]
    )
    for offset, row in enumerate(rows):
        number = START + offset
        sources = " · ".join(
            f"[{source['label']}]({source['url']})" for source in row["sources"]
        )
        review = row["review"].strip().replace("|", "\\|")
        if not review.endswith((".", "!", "?")):
            review += "."
        title = row["title"].replace("|", "\\|")
        lines.append(
            f"| {number} | [[{row['slug']}]] — {title} | {sources} | {review} Decisão: aprovada por IA. |"
        )
    lines.extend(
        [
            "",
            "## Separação de status",
            "",
            "A revisão acima altera somente `revisao_ia`, `revisor_ia`, `data_revisao_ia` e `relatorio_revisao_ia` nas notas 401–500. Não altera `revisao_humana`, `revisor`, aprovações históricas, nem o conteúdo de tranches anteriores.",
            "",
        ]
    )
    return "\n".join(lines)


def patch_frontmatters(rows: list[dict]) -> list[tuple[Path, str]]:
    updates: list[tuple[Path, str]] = []
    expected_pending = {
        "revisao_ia": "pendente",
        "revisor_ia": '""',
        "data_revisao_ia": '""',
        "relatorio_revisao_ia": '""',
    }
    for row in rows:
        path = NOTES_DIR / f"{row['slug']}.md"
        text = path.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---\n", text, flags=re.S)
        if not match:
            raise ValueError(f"Frontmatter ausente em {path.name}")
        fm = match.group(1)
        for key, value in expected_pending.items():
            occurrences = re.findall(rf"(?m)^{re.escape(key)}: (.*?)$", fm)
            if occurrences != [value]:
                raise ValueError(f"{path.name}: estado inicial inesperado para {key}: {occurrences}")

        if re.findall(r"(?m)^revisao_humana: (.*?)$", fm) != ["nao_solicitada"]:
            raise ValueError(f"{path.name}: estado de revisão humana mudou")
        if re.findall(r"(?m)^revisor: (.*?)$", fm) != ['""']:
            raise ValueError(f"{path.name}: campo de revisor humano mudou")
        if re.findall(r"(?m)^status: (.*?)$", fm) != ["candidata"]:
            raise ValueError(f"{path.name}: status inesperado antes da revisão")

        replacements = {
            "revisao_ia": "aprovada",
            "revisor_ia": '"Arena.ai Agent Mode"',
            "data_revisao_ia": DATE,
            "relatorio_revisao_ia": f'"{REPORT_REL}"',
        }
        updated_fm = fm
        for key, value in replacements.items():
            updated_fm, count = re.subn(
                rf"(?m)^{re.escape(key)}: .*?$",
                f"{key}: {value}",
                updated_fm,
            )
            if count != 1:
                raise ValueError(f"{path.name}: esperado um campo {key}, encontrados {count}")
        updated_text = text[: match.start(1)] + updated_fm + text[match.end(1) :]
        updates.append((path, updated_text))
    if len(updates) != COUNT:
        raise ValueError(f"Frontmatters planejados: {len(updates)}/{COUNT}")
    return updates


def main() -> int:
    rows, groups = load_rows()
    validate_initial_gate()
    if REPORT_PATH.exists():
        raise FileExistsError(f"Relatório já existe; não será sobrescrito: {REPORT_PATH}")
    if len({row["slug"] for row in rows}) != COUNT:
        raise ValueError("Slugs não são únicos no conjunto da tranche")

    updates = patch_frontmatters(rows)
    report = build_report(rows, groups)
    for path, text in updates:
        path.write_text(text, encoding="utf-8")
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(report, encoding="utf-8")
    print(f"Revisão factual gravada: {REPORT_REL} ({len(rows)} registros).")
    print(f"Frontmatter atualizado: {len(updates)}/{COUNT}; revisão humana continua não solicitada.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
