#!/usr/bin/env python3
"""Reconcile tranche 23 across manifest, MOC, review registry and status docs.

Every replacement is asserted: a missing pattern aborts the script instead of
silently leaving a stale count in the editorial documents. The script is
idempotent: re-running it skips blocks and pairs already applied.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KF = ROOT / "knowledge-federation"
SCRIPTS = KF / "scripts"
BATCH_ID = "software-testes-2000-0001"
REPORT_NAME = "ai-review-software-testes-2000-0001-tranche-23.md"
RECON_NAME = "batch-reconciliation-software-testes-2000-0001-tranche-23.md"
DATE = "2026-10-03"


def load_builder():
    spec = importlib.util.spec_from_file_location("b23", SCRIPTS / "_build_tranche23.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_groups(b23):
    groups = []
    for path in sorted(b23.DATA_DIR.glob("*.txt")):
        context, rows = b23.parse_group(path)
        groups.append((context, rows))
    return groups


def manifest_section(groups) -> str:
    lines = ["## Tranche 23 — runners de navegador para JavaScript, JUnit 4, approval tests, fuzzing em Go/Rust/C/Python, boofuzz, Hyperfoil e Infection (100 notas; revisão factual por IA registrada)", ""]
    for context, rows in groups:
        lines.append(f"### {context['group']}")
        lines.append("")
        for index, row in enumerate(rows):
            number = int(context["first"]) + index
            lines.append(
                f"{number}. [{row['title']}](../../domains/software-0007/software/testes/{row['slug']}.md)"
            )
        lines.append("")
    return "\n".join(lines) + "\n"


def moc_section(groups) -> str:
    lines = ["## Tranche 23 — runners de navegador para JavaScript, JUnit 4, approval tests, fuzzing em Go/Rust/C/Python, boofuzz, Hyperfoil e Infection", ""]
    for context, rows in groups:
        lines.append(f"### {context['group']}")
        lines.append("")
        for index, row in enumerate(rows):
            number = int(context["first"]) + index
            lines.append(f"{number}. [[{row['slug']}]] — {row['summary']}")
        lines.append("")
    return "\n".join(lines) + "\n"


def review_rows(groups) -> str:
    lines = []
    for context, rows in groups:
        for index, row in enumerate(rows):
            number = int(context["first"]) + index
            position = 1700 + (number - 1660)
            lines.append(
                f"| {position} | `{BATCH_ID}` | [{row['title']}](../../domains/software-0007/software/testes/{row['slug']}.md) "
                f"| APROVADA POR IA | IA: Arena.ai Agent Mode | Revisão factual por IA registrada em {DATE} no relatório "
                f"`{REPORT_NAME}` (nota {number}); não é aprovação humana. |"
            )
    return "\n".join(lines) + "\n"


def apply(path: Path, pairs: list[tuple[str, str]]) -> None:
    text = path.read_text(encoding="utf-8")
    original = text
    for old, new in pairs:
        if new in text:
            # Already applied (covers pairs whose old text is a prefix of the new text).
            continue
        count = text.count(old)
        if count == 0:
            raise SystemExit(f"{path.relative_to(ROOT)}: padrão não encontrado: {old[:140]}")
        if count != 1:
            raise SystemExit(f"{path.relative_to(ROOT)}: padrão encontrado {count} vezes: {old[:140]}")
        text = text.replace(old, new)
    if text == original:
        print(f"já reconciliado {path.relative_to(ROOT)}")
        return
    path.write_text(text, encoding="utf-8")
    print(f"ok {path.relative_to(ROOT)}")


def insert_before(path: Path, anchor: str, block: str, marker: str | None = None) -> None:
    text = path.read_text(encoding="utf-8")
    marker = marker if marker is not None else block.splitlines()[0]
    if marker in text:
        print(f"já presente {path.relative_to(ROOT)}")
        return
    if text.count(anchor) != 1:
        raise SystemExit(f"{path.relative_to(ROOT)}: âncora encontrada {text.count(anchor)} vezes: {anchor}")
    text = text.replace(anchor, block + anchor, 1)
    path.write_text(text, encoding="utf-8")
    print(f"ok inserção {path.relative_to(ROOT)}")


def main() -> None:
    b23 = load_builder()
    groups = load_groups(b23)
    total = sum(len(rows) for _, rows in groups)
    if total != 100 or int(groups[0][0]["first"]) != 1660 or int(groups[-1][0]["first"]) != 1750:
        raise SystemExit(f"dados inesperados: {total} notas, primeiro grupo em {groups[0][0]['first']}")

    manifest = KF / "exports" / "batches" / f"{BATCH_ID}.md"
    moc = KF / "00-home-vault" / "MOCs" / "MOC-Testes-Software-0007.md"
    queue = KF / "exports" / "reports" / "human-review-queue.md"

    insert_before(manifest, "## Critérios e próximo passo", manifest_section(groups))
    insert_before(moc, "## Estado editorial", moc_section(groups))
    queue_block = review_rows(groups)
    insert_before(queue, "## Regra de contagem", queue_block)

    apply(manifest, [
        ('- Notas efetivamente redigidas até agora: **1659 / 2.000 (82,95%)**',
         '- Notas efetivamente redigidas até agora: **1759 / 2.000 (87,95%)**'),
        ('- Gate automatizado: **1659/1659 aprovadas**',
         '- Gate automatizado: **1759/1759 aprovadas**'),
        ('reexecutado após a tranche 22)',
         'reexecutado após a tranche 23)'),
        ('- Revisão factual humana: **9/1659**',
         '- Revisão factual humana: **9/1759**'),
        ('- Revisão factual por IA: **1650/1659**',
         '- Revisão factual por IA: **1750/1759**'),
        ('Contabilizadas como válidas: **1659/1659**',
         'Contabilizadas como válidas: **1759/1759**'),
        ('- Revisor das 1650 notas aprovadas por IA',
         '- Revisor das 1750 notas aprovadas por IA'),
        ('tranches 2–22 (1650 notas, IDs 10–1659) foram conferidas factualmente por IA',
         'tranches 2–23 (1750 notas, IDs 10–1759) foram conferidas factualmente por IA'),
        ('[`tranche 21`](../reports/ai-review-software-testes-2000-0001-tranche-21.md), [`tranche 21`](../reports/ai-review-software-testes-2000-0001-tranche-21.md), [`tranche 22`](../reports/ai-review-software-testes-2000-0001-tranche-22.md)',
         '[`tranche 21`](../reports/ai-review-software-testes-2000-0001-tranche-21.md), [`tranche 21`](../reports/ai-review-software-testes-2000-0001-tranche-21.md), [`tranche 22`](../reports/ai-review-software-testes-2000-0001-tranche-22.md)'),
        ('[`batch-reconciliation-software-testes-2000-0001-tranche-22.md`](../reports/batch-reconciliation-software-testes-2000-0001-tranche-22.md)',
         '[`batch-reconciliation-software-testes-2000-0001-tranche-22.md`](../reports/batch-reconciliation-software-testes-2000-0001-tranche-22.md)'),
        ('Existem 1659 notas materiais listadas abaixo; não há IDs reservados, placeholders ou registros virtuais para as 341 restantes.',
         'Existem 1759 notas materiais listadas abaixo; não há IDs reservados, placeholders ou registros virtuais para as 241 restantes.'),
        ('as 1650 notas 10–1659 das tranches 2–22 têm revisão factual por IA registrada nos relatórios vinculados',
         'as 1750 notas 10–1759 das tranches 2–23 têm revisão factual por IA registrada nos relatórios vinculados'),
        ('são 1659/2.000 notas válidas, restando 341 notas materiais',
         'são 1759/2.000 notas válidas, restando 241 notas materiais'),
    ])

    apply(moc, [
        ('Índice das 1659 notas substantivas redigidas até agora no lote `software-testes-2000-0001`, cuja meta é 2.000. As 1659 passaram pelo gate automatizado e têm revisão factual registrada: nove aprovadas pelo usuário e 1650 aprovadas por IA',
         'Índice das 1759 notas substantivas redigidas até agora no lote `software-testes-2000-0001`, cuja meta é 2.000. As 1759 passaram pelo gate automatizado e têm revisão factual registrada: nove aprovadas pelo usuário e 1750 aprovadas por IA'),
        ('O gate automatizado foi aprovado por 1659/1659 notas e as 1659 contam como válidas pelo protocolo atualizado: nove têm aprovação humana histórica e 1650 têm revisão factual por IA registrada separadamente. O lote de 2.000 continua `in_progress` (1659 notas substantivas; 341 ainda não produzidas).',
         'O gate automatizado foi aprovado por 1759/1759 notas e as 1759 contam como válidas pelo protocolo atualizado: nove têm aprovação humana histórica e 1750 têm revisão factual por IA registrada separadamente. O lote de 2.000 continua `in_progress` (1759 notas substantivas; 241 ainda não produzidas).'),
        ('[reconciliação mais recente do manifesto/fila](../../exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-22.md)',
         '[reconciliação mais recente do manifesto/fila](../../exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-23.md))'),
        (', [19](../../exports/reports/ai-review-software-testes-2000-0001-tranche-19.md), [20](../../exports/reports/ai-review-software-testes-2000-0001-tranche-20.md), [21](../../exports/reports/ai-review-software-testes-2000-0001-tranche-21.md) e [22](../../exports/reports/ai-review-software-testes-2000-0001-tranche-22.md).',
         ', [19](../../exports/reports/ai-review-software-testes-2000-0001-tranche-19.md), [20](../../exports/reports/ai-review-software-testes-2000-0001-tranche-20.md), [21](../../exports/reports/ai-review-software-testes-2000-0001-tranche-21.md), [22](../../exports/reports/ai-review-software-testes-2000-0001-tranche-22.md) e [23](../../exports/reports/ai-review-software-testes-2000-0001-tranche-23.md).'),
    ])

    apply(queue, [
        ('distingue 1650 revisões factuais realizadas por IA no lote `software-testes-2000-0001`',
         'distingue 1750 revisões factuais realizadas por IA no lote `software-testes-2000-0001`'),
        ('- Aprovações por IA registradas separadamente: **1650**.',
         '- Aprovações por IA registradas separadamente: **1750**.'),
        ('- Notas válidas contabilizadas (gate + revisão humana ou IA): **1699**.',
         '- Notas válidas contabilizadas (gate + revisão humana ou IA): **1799**.'),
        ('As 1650 linhas `APROVADA POR IA` (nº 50–1699) correspondem às notas 10–1659 e às revisões documentadas nos relatórios das tranches 2–22',
         'As 1750 linhas `APROVADA POR IA` (nº 50–1799) correspondem às notas 10–1759 e às revisões documentadas nos relatórios das tranches 2–23'),
    ])

    apply(ROOT / 'README.md', [
        ('| Notas válidas contabilizadas | 1699 / 1.000.000 (0,1699%) | 49 com aprovação humana histórica + 1650 com revisão factual por IA |',
         '| Notas válidas contabilizadas | 1799 / 1.000.000 (0,1799%) | 49 com aprovação humana histórica + 1750 com revisão factual por IA |'),
        ('| Notas com revisão factual por IA registrada | 1650 |',
         '| Notas com revisão factual por IA registrada | 1750 |'),
        ('| Primeiro lote `software-testes-2000-0001` | 1659 / 2.000 (82,95%) | 9 aprovadas por humano + 1650 por IA; faltam 341 notas substantivas |',
         '| Primeiro lote `software-testes-2000-0001` | 1759 / 2.000 (87,95%) | 9 aprovadas por humano + 1750 por IA; faltam 241 notas substantivas |'),
        ('| Arquivos Markdown ativos em `knowledge-federation/domains/` | 1799 | 100 notas legadas com pendências + 1699 notas autorais substantivas |',
         '| Arquivos Markdown ativos em `knowledge-federation/domains/` | 1899 | 100 notas legadas com pendências + 1799 notas autorais substantivas |'),
        ('é `software-testes-2000-0001`: 1659 notas materiais já passaram pelo gate e revisão factual (9 humanas + 1650 IA)',
         'é `software-testes-2000-0001`: 1759 notas materiais já passaram pelo gate e revisão factual (9 humanas + 1750 IA)'),
        (', [19](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-19.md), [20](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-20.md), [21](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-21.md) e [22](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-22.md))',
         ', [19](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-19.md), [20](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-20.md), [21](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-21.md), [22](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-22.md) e [23](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-23.md))'),
        ('além da [reconciliação da tranche 22](knowledge-federation/exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-22.md)',
         'além da [reconciliação da tranche 23](knowledge-federation/exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-23.md))'),
    ])

    apply(KF / 'README.md', [
        ('- Arquivos Markdown ativos: **1799** (100 notas legadas com pendências + 1699 notas autorais substantivas).',
         '- Arquivos Markdown ativos: **1899** (100 notas legadas com pendências + 1799 notas autorais substantivas).'),
        ('- Notas válidas pelo protocolo atual: **1699** (49 aprovações humanas históricas + 1650 revisões factuais por IA).',
         '- Notas válidas pelo protocolo atual: **1799** (49 aprovações humanas históricas + 1750 revisões factuais por IA).'),
        ('- Progresso: **1699 / 1.000.000 (0,1699%)**; faltam 998.301 notas válidas.',
         '- Progresso: **1799 / 1.000.000 (0,1799%)**; faltam 998.201 notas válidas.'),
        ('- Lote em andamento `software-testes-2000-0001`: **1659 / 2.000** notas válidas (82,95%); 9 humanas e 1650 por IA; faltam 341 notas materiais.',
         '- Lote em andamento `software-testes-2000-0001`: **1759 / 2.000** notas válidas (87,95%); 9 humanas e 1750 por IA; faltam 241 notas materiais.'),
        (', [19](exports/reports/ai-review-software-testes-2000-0001-tranche-19.md), [20](exports/reports/ai-review-software-testes-2000-0001-tranche-20.md), [21](exports/reports/ai-review-software-testes-2000-0001-tranche-21.md) e [22](exports/reports/ai-review-software-testes-2000-0001-tranche-22.md); veja também a [reconciliação da tranche 22](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-22.md).',
         ', [19](exports/reports/ai-review-software-testes-2000-0001-tranche-19.md), [20](exports/reports/ai-review-software-testes-2000-0001-tranche-20.md), [21](exports/reports/ai-review-software-testes-2000-0001-tranche-21.md), [22](exports/reports/ai-review-software-testes-2000-0001-tranche-22.md) e [23](exports/reports/ai-review-software-testes-2000-0001-tranche-23.md); veja também a [reconciliação da tranche 23](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-23.md)).'),
    ])

    apply(KF / 'README-1M.md', [
        ('tem 1699 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 1650 revisões factuais por IA registradas separadamente). O diretório ativo tem 1799 arquivos Markdown, incluindo 100 notas legadas com pendências, ainda excluídas da contagem. O lote `software-testes-2000-0001` tem 1659/2.000 notas válidas e segue em andamento; as notas 1560–1659 estão no [relatório factual por IA da tranche 22](exports/reports/ai-review-software-testes-2000-0001-tranche-22.md) e na [reconciliação da tranche 22](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-22.md); as notas 1460–1559 ficam no [relatório da tranche 21](exports/reports/ai-review-software-testes-2000-0001-tranche-21.md);',
         'tem 1799 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 1750 revisões factuais por IA registradas separadamente). O diretório ativo tem 1899 arquivos Markdown, incluindo 100 notas legadas com pendências, ainda excluídas da contagem. O lote `software-testes-2000-0001` tem 1759/2.000 notas válidas e segue em andamento; as notas 1660–1759 estão no [relatório factual por IA da tranche 23](exports/reports/ai-review-software-testes-2000-0001-tranche-23.md) e na [reconciliação da tranche 23](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-23.md); as notas 1560–1659 ficam no [relatório da tranche 22](exports/reports/ai-review-software-testes-2000-0001-tranche-22.md);'),
    ])

    apply(KF / 'STATUS-CONSOLIDACAO-1M.md', [
        ('A auditoria encontrou 1799 arquivos Markdown ativos: 1699 notas substantivas passaram pelo gate e receberam revisão factual registrada (49 humanas históricas + 1650 por IA)',
         'A auditoria encontrou 1899 arquivos Markdown ativos: 1799 notas substantivas passaram pelo gate e receberam revisão factual registrada (49 humanas históricas + 1750 por IA)'),
        ('| Progresso válido global | 1699 / 1.000.000 (0,1699%) | 49 revisões humanas históricas + 1650 revisões por IA registradas separadamente |',
         '| Progresso válido global | 1799 / 1.000.000 (0,1799%) | 49 revisões humanas históricas + 1750 revisões por IA registradas separadamente |'),
        ('| Revisões factuais por IA registradas | 1650 | Relatórios das tranches 2–22',
         '| Revisões factuais por IA registradas | 1750 | Relatórios das tranches 2–23'),
        ('| Primeiro lote | 1659 / 2.000 (82,95%) | 9 humanas + 1650 IA; faltam 341 notas substantivas |',
         '| Primeiro lote | 1759 / 2.000 (87,95%) | 9 humanas + 1750 IA; faltam 241 notas substantivas |'),
        ('| Candidatas que passaram pelo gate automatizado | 1699 |',
         '| Candidatas que passaram pelo gate automatizado | 1799 |'),
        ('Revisadas factualmente por IA as notas 10–1659 do lote (1650 no total)',
         'Revisadas factualmente por IA as notas 10–1759 do lote (1750 no total)'),
        (', [19](exports/reports/ai-review-software-testes-2000-0001-tranche-19.md), [20](exports/reports/ai-review-software-testes-2000-0001-tranche-20.md), [21](exports/reports/ai-review-software-testes-2000-0001-tranche-21.md) e [22](exports/reports/ai-review-software-testes-2000-0001-tranche-22.md).',
         ', [19](exports/reports/ai-review-software-testes-2000-0001-tranche-19.md), [20](exports/reports/ai-review-software-testes-2000-0001-tranche-20.md), [21](exports/reports/ai-review-software-testes-2000-0001-tranche-21.md), [22](exports/reports/ai-review-software-testes-2000-0001-tranche-22.md) e [23](exports/reports/ai-review-software-testes-2000-0001-tranche-23.md).'),
        ('4. Resultado parcial do primeiro lote: 1659/1659 aprovadas pelo gate; nove revisões humanas e 1650 revisões por IA no total após a tranche 22, incluindo as 100 novas revisões das notas 1560–1659.',
         '4. Resultado parcial do primeiro lote: 1759/1759 aprovadas pelo gate; nove revisões humanas e 1750 revisões por IA no total após a tranche 23, incluindo as 100 novas revisões das notas 1660–1659.'),
        ('Relatórios atualizados: [reconciliação da tranche 22](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-22.md)',
         'Relatórios atualizados: [reconciliação da tranche 23](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-23.md))'),
        ('faltam 341 notas para o tamanho configurado de 2.000',
         'faltam 241 notas para o tamanho configurado de 2.000'),
    ])

    apply(KF / 'PLANO-CONTINUO-1M.md', [
        ('- Notas válidas globais: **1699** (49 aprovações humanas históricas + 1650 revisões factuais por IA).',
         '- Notas válidas globais: **1799** (49 aprovações humanas históricas + 1750 revisões factuais por IA).'),
        ('- Progresso: **1699 / 1.000.000 (0,1699%)**; faltam **998.301** notas válidas.',
         '- Progresso: **1799 / 1.000.000 (0,1799%)**; faltam **998.201** notas válidas.'),
        ('- Lote atual `software-testes-2000-0001`: **1659 / 2.000 (82,95%)** notas válidas (9 humanas + 1650 IA); faltam **341** notas substantivas.',
         '- Lote atual `software-testes-2000-0001`: **1759 / 2.000 (87,95%)** notas válidas (9 humanas + 1750 IA); faltam **241** notas substantivas.'),
        ('- Arquivos Markdown ativos: **1799**; 100 com pendências de qualidade, excluídos da contagem.',
         '- Arquivos Markdown ativos: **1899**; 100 com pendências de qualidade, excluídos da contagem.'),
        ('| 4 | Conferir factual e registrar notas 10–1659 do primeiro lote | **Concluído até a tranche 22** | 1650 revisões por IA em relatórios das tranches 2–22, além das 9 aprovações humanas. |',
         '| 4 | Conferir factual e registrar notas 10–1759 do primeiro lote | **Concluído até a tranche 22** | 1750 revisões por IA em relatórios das tranches 2–23, além das 9 aprovações humanas. |'),
        ('| 5 | Rodar gate, testes, auditorias e diff | **Concluído para o estado atual** | Lote: 1659/1659 no gate, 9 humanas, 1650 IA. Global: 1799 arquivos, 1699 válidas, 100 com pendências legadas; veja a [reconciliação da tranche 22](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-22.md). |',
         '| 5 | Rodar gate, testes, auditorias e diff | **Concluído para o estado atual** | Lote: 1759/1759 no gate, 9 humanas, 1750 IA. Global: 1899 arquivos, 1799 válidas, 100 com pendências legadas; veja a [reconciliação da tranche 23](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-23.md)). |'),
        ('| 7 | Completar o lote `software-testes-2000-0001` até 2.000 notas | **Em andamento** | 1659/2.000; faltam 341 notas;',
         '| 7 | Completar o lote `software-testes-2000-0001` até 2.000 notas | **Em andamento** | 1759/2.000; faltam 241 notas;'),
        ('Progresso atual: 1699 notas válidas, 0/500 lotes completos.',
         'Progresso atual: 1799 notas válidas, 0/500 lotes completos.'),
    ])

    apply(KF / 'RECOVERY-AND-SCALE-NOTE.md', [
        ('há 1799 arquivos: 100 legados com pendências e 1699 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 1650 revisões por IA). O lote `software-testes-2000-0001` tem 1659/2.000 notas válidas (9 humanas + 1650 IA), com status `in_progress` e 341 notas qualificadas restantes. As notas 1560–1659 passaram pelo gate e têm revisão factual por IA registrada na [tranche 22](exports/reports/ai-review-software-testes-2000-0001-tranche-22.md), com [reconciliação](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-22.md);',
         'há 1899 arquivos: 100 legados com pendências e 1799 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 1750 revisões por IA). O lote `software-testes-2000-0001` tem 1759/2.000 notas válidas (9 humanas + 1750 IA), com status `in_progress` e 241 notas qualificadas restantes. As notas 1660–1759 passaram pelo gate e têm revisão factual por IA registrada na [tranche 23](exports/reports/ai-review-software-testes-2000-0001-tranche-23.md), com [reconciliação](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-23.md));'),
        ('1. Continuar o lote atual em tranches de conteúdo real; faltam 341 notas qualificadas para completar as 2.000 configuradas.',
         '1. Continuar o lote atual em tranches de conteúdo real; faltam 241 notas qualificadas para completar as 2.000 configuradas.'),
    ])

    apply(KF / '00-home-vault' / 'Home.md', [
        ('[[MOC-Testes-Software-0007]] — 1659 notas do lote de escala (meta: 2.000); nove têm aprovação humana histórica e 1650 revisões factuais por IA.',
         '[[MOC-Testes-Software-0007]] — 1759 notas do lote de escala (meta: 2.000); nove têm aprovação humana histórica e 1750 revisões factuais por IA.'),
        ('[[human-review-queue|Registro de revisões factuais]] — 49 aprovações humanas e 1650 aprovações por IA, identificadas separadamente.',
         '[[human-review-queue|Registro de revisões factuais]] — 49 aprovações humanas e 1750 aprovações por IA, identificadas separadamente.'),
        ('[[note-quality-audit|Auditoria de qualidade]] — 1699 notas válidas pelo protocolo atual (49 humanas + 1650 IA) e 100 notas legadas com falhas.',
         '[[note-quality-audit|Auditoria de qualidade]] — 1799 notas válidas pelo protocolo atual (49 humanas + 1750 IA) e 100 notas legadas com falhas.'),
    ])

    apply(KF / '00-home-vault' / 'Indice-Global.md', [
        ('- Arquivos Markdown em `domains/`: **1799** (100 sementes legadas + 1699 notas autorais substantivas).',
         '- Arquivos Markdown em `domains/`: **1899** (100 sementes legadas + 1799 notas autorais substantivas).'),
        ('- Candidatas aprovadas no gate automatizado: **1699**; revisões humanas registradas: **49**; revisões factuais por IA: **1650**; 100 sementes legadas mantêm pendências.',
         '- Candidatas aprovadas no gate automatizado: **1799**; revisões humanas registradas: **49**; revisões factuais por IA: **1750**; 100 sementes legadas mantêm pendências.'),
        ('- Os lotes atuais totalizam 1699 notas válidas pelo protocolo; o lote `software-testes-2000-0001` tem 1659/2.000, incluindo as notas 1560–1659 revisadas por IA na [tranche 22](../exports/reports/ai-review-software-testes-2000-0001-tranche-22.md) e na [reconciliação da tranche 22](../exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-22.md), as notas 1460–1559 na [tranche 21](../exports/reports/ai-review-software-testes-2000-0001-tranche-21.md),',
         '- Os lotes atuais totalizam 1799 notas válidas pelo protocolo; o lote `software-testes-2000-0001` tem 1759/2.000, incluindo as notas 1660–1759 revisadas por IA na [tranche 23](../exports/reports/ai-review-software-testes-2000-0001-tranche-23.md) e na [reconciliação da tranche 23](../exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-23.md), as notas 1560–1659 na [tranche 22](../exports/reports/ai-review-software-testes-2000-0001-tranche-22.md),'),
    ])
    print("reconciliação concluída")


if __name__ == "__main__":
    main()
