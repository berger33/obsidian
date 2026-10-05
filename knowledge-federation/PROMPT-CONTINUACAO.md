# Consolidação de branches e prompt de continuação

Atualizado em 2026-10-04. Este arquivo registra a consolidação das branches paralelas na `main` e traz o **prompt pronto para colar** numa nova sessão de execução.

## 1. Registro da consolidação (2026-10-04)

Estado anterior: seis branches `arena/*` no `origin`, sendo três já integradas (`arena/01a0f4eb-obsidian`, `arena/01a0f8f9-obsidian`, `arena/01a0f960-obsidian` — todas com PRs #1, #2 e #3 já mesclados) e três com trabalho não integrado:

| Branch | Situação encontrada | Decisão |
|---|---|---|
| `arena/01a0ff06-obsidian` | 16 commits; ancestral direto de `arena/01a0ff9b-obsidian` | Integrada via `arena/01a0ff9b-obsidian`; branch removida |
| `arena/01a0ff9b-obsidian` | 58 commits à frente da `main`: fechamento do lote 1 (tranches 21–26), lote 2 completo (tranches 1–20) e lote 3 (tranches 1–16) | **Ramo canônico**, integrado à `main`; branch removida |
| `arena/01a0f9df-obsidian` | 1 commit exclusivo: Tranche 15 de testes com 100 notas (`cargo-nextest`/`coverage.py`/`dbt`) | Conteúdo **superado** pela Tranche 15 canônica (`jacoco`), que sustentou o lote 1 até 2.000/2.000. Descartado da contagem e preservado na tag `archive/tranche15-testes-alternativa` (commit `aecadd6e`) |

Verificações executadas antes e depois da integração:

- `python3 -m unittest discover -s knowledge-federation/tests -v` → **12/12 OK**.
- `python3 knowledge-federation/scripts/audit_note_quality.py --path knowledge-federation/domains --archive knowledge-federation/archives/ledger-v1000000-mat8000.sqlite.xz` → **5.740 arquivos, 5.640 válidas (49 humanas + 5.591 IA), 100 com pendências legadas**; ledger com 1.000.000 de registros virtuais fora da contagem.
- Nenhum arquivo existente na `main` foi removido pela integração (0 deleções; o resultado é superconjunto estrito da `main`).
- Os 8 arquivos de nota e os scripts de qualidade que divergiam são versões **estendidas** dos da `main` (suporte a `revisao_ia` em `note_quality.py`, `audit_batch.py` e testes), não regressões.
- As 49 aprovações humanas registradas em `exports/reports/human-review-queue.md` são datadas de 2026-10-02, posteriores à `STATUS-CONSOLIDACAO-1M.md` da `main` (2026-10-01, que registrava 0); são preservadas como histórico e não se estendem a notas novas.

## 2. Prompt para a próxima sessão

Copie o bloco abaixo e cole como primeira mensagem da nova sessão:

```text
Continue a execução do plano de 1.000.000 de notas válidas do repositório berger33/obsidian.

CONTEXTO JÁ VERIFICADO (estado editorial atual em 2026-10-04):
- Meta ativa: 500 lotes × 2.000 notas substantivas = 1.000.000 de notas válidas.
- Estado: 6540 / 1.000.000 (0,6540%) válidas; 3/500 lotes completos; 6640 arquivos Markdown ativos (6540 válidas + 100 legadas com pendências, mantidas fora da contagem).
- Lotes 1–3: `software-testes-2000-0001`, `software-devops-2000-0002` e `software-seguranca-2000-0003`, todos 2.000/2.000 (`complete`).
- Lote 4 `software-criacao-ia-2000-0004`: 500/2.000 (25,00%), com as tranches 1–5 concluídas (500 notas, IDs 1–500), 500 aprovadas pelo gate e 500 com revisão factual por IA; nenhuma aprovação humana nova; 15 tranches planejadas.
- Escopo do lote 4: engenharia/criação de programas, aplicativos e jogos com IA; IA de gameplay, produção de vídeo/animação e documentação/tutorial. Não abrir lote 5 automaticamente.
- Contagem exige frontmatter rastreável, ≥100 palavras, seções de explicação/exemplo/limites/verificação, duas fontes HTTPS específicas, wikilinks resolvidos, sem marcadores de template, gate aprovado e revisão factual registrada. Revisão por IA nunca altera nem amplia as 49 aprovações humanas históricas.
- Relatórios do lote 4 tranche 5: `exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-05.md`, `exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-05.md`, `exports/reports/source-link-audit-software-criacao-ia-2000-0004-tranche-05.md` e `exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-05.md`.
- Artefatos por tranche: manifesto, relatório factual IA, auditoria/gate, reconciliação, fila de revisão, MOC e resumos globais.
- IDs 401–500 pertencem à tranche 5 concluída neste fluxo; nenhum ID posterior foi reservado e o lote 5 permanece fechado.

RESULTADO DA TRANCHE 5 — NÃO AVANÇAR AUTOMATICAMENTE
- Tranche 5 materializada: 100 notas, IDs 401–500, em `domains/software-0010/software/criacao-ia/`; 100/100 passaram o gate e receberam revisão factual por IA. Revisão humana nova: 0; as 49 aprovações históricas não mudam.
- Artefatos: manifesto do lote, gate final, revisão factual, auditoria de links e reconciliação da tranche 5; fila humana numerada nas linhas 6441–6540.
- Estado esperado: 6.640 arquivos Markdown em `domains/`, 6.540 válidas (49 humanas + 6.491 IA), 100 legadas fora da contagem; lote 4 em 500/2.000 (25,00%), 15 tranches planejadas; faltam 993.460 notas.
- Não reservar IDs além de 500, não abrir o lote 5 nem produzir outra tranche sem solicitação explícita do usuário. Se solicitado, atualizar inventário e busca em todo o vault, selecionar temas não duplicados e conferir fontes primárias específicas antes de atribuir IDs apenas à tranche solicitada.
- Não tocar nos relatórios/reconciliações das tranches 1–4, `LOTS-201-300.md`, `MOC-Seguranca-Software-0009.md`, `archives/LATEST-LEDGER.txt` ou no dump `.xz`; `LOT-SEQUENCE` e `_meta/plano-execucao` não mudam por tranche.

TAREFA IMEDIATA:
1. A tranche 5 foi reconciliada; não iniciar tranche 6 nem lote 5 automaticamente.
2. Antes de qualquer push, executar os testes unitários e a auditoria global listados abaixo.
3. Publicar somente na branch da sessão e abrir PR para `main`, sem atribuir IDs futuros.

VERIFICAÇÃO OBRIGATÓRIA ANTES DE CADA PUSH:
python3 -m unittest discover -s knowledge-federation/tests -v
python3 knowledge-federation/scripts/audit_note_quality.py --path knowledge-federation/domains --archive knowledge-federation/archives/ledger-v1000000-mat8000.sqlite.xz

REGRAS DE HIGIENE (aprendidas na consolidação de 2026-10-04):
- Trabalhe apenas na branch da sessão. Não abra uma segunda branch para refazer uma tranche já publicada: foi exatamente isso que criou branches duplicadas para apagar.
- Não reescreva as 49 aprovações humanas históricas; elas valem só para as notas que o usuário aprovou.
- Conteúdo superado por uma reescrita não entra na contagem; se precisar preservar, use tag de arquivo em vez de branch paralela.
- Rode o gate no fim de toda tranche e reconcilie os artefatos antes de atualizar a contagem.
```

## 3. Como retomar o conteúdo superado (se necessário)

A Tranche 15 alternativa dos testes não está na contagem. Para inspecioná-la:

```bash
git fetch origin 'refs/tags/archive/*:refs/tags/archive/*'
git show --stat archive/tranche15-testes-alternativa
git ls-tree -r --name-only archive/tranche15-testes-alternativa -- knowledge-federation/domains/software-0007/software/testes/
```
