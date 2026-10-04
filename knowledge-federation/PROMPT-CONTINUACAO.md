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
- Estado: 6440 / 1.000.000 (0,6440%) válidas; 3/500 lotes completos; 6540 arquivos Markdown ativos (6440 válidas + 100 legadas com pendências, mantidas fora da contagem).
- Lotes 1–3: `software-testes-2000-0001`, `software-devops-2000-0002` e `software-seguranca-2000-0003`, todos 2.000/2.000 (`complete`).
- Lote 4 `software-criacao-ia-2000-0004`: 400/2.000 (20,00%), com as tranches 1–4 concluídas (400 notas, IDs 1–400), 400 aprovadas pelo gate e 400 com revisão factual por IA; nenhuma aprovação humana nova; 16 tranches planejadas.
- Escopo do lote 4: engenharia/criação de programas, aplicativos e jogos com IA; IA de gameplay, produção de vídeo/animação e documentação/tutorial. Não abrir lote 5 automaticamente.
- Contagem exige frontmatter rastreável, ≥100 palavras, seções de explicação/exemplo/limites/verificação, duas fontes HTTPS específicas, wikilinks resolvidos, sem marcadores de template, gate aprovado e revisão factual registrada. Revisão por IA nunca altera nem amplia as 49 aprovações humanas históricas.
- Relatórios do lote 4 tranche 4: `exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-04.md`, `exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-04.md` e `exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-04.md`.
- Artefatos por tranche: manifesto, relatório factual IA, auditoria/gate, reconciliação, fila de revisão, MOC e resumos globais.
- A tranche 4 foi integrada à `main` pelo PR #9; a tranche 5 recomeça do próximo ID livre (401), sem nenhuma reserva prévia.

HANDOFF OPERACIONAL DA TRANCHE 5 (padrão estabelecido nas tranches 2–4):
- Clone de `knowledge-federation/scripts/_build_criacao_ia_t04.py`, `_finalize_criacao_ia_t04.py` e `_reconcile_criacao_ia_t04.py`, mais a data dir `_criacao_ia_t04_data/` (10 JSONs; chaves `group`/`check`/`notes`; nota: `slug,title,one,why,how,example,limits,verify,sources×2{label,url,why},review`). No builder: TRANCHE=`tranche05`, START=401, DATA_DIR=`_criacao_ia_t05_data`, AI_REVIEW_REPORT=`ai-review-software-criacao-ia-2000-0004-tranche-05.md`. O builder exige exatamente 10 grupos × 10 notas, valida cada nota no gate antes de gravar e recusa frase de 8+ palavras repetida entre notas.
- Ordem dos grupos no data dir define os IDs (401–410 para o primeiro grupo, …, 491–500 para o décimo).
- Antes de qualquer contagem: gate por arquivo com os 100 `--path` (`note-quality-software-criacao-ia-2000-0004-tranche-05.md`), relatório de revisão IA com 100 linhas (401–500) e patch de frontmatter (`revisao_ia: aprovada`, `revisor_ia`, `data_revisao_ia`, `relatorio_revisao_ia`) via `_finalize_…t05.py`.
- Reconciliação na ordem do `_reconcile_…t04.py` (asserts de 1 ocorrência por substituição): fila (linhas 6441–6540; o cabeçalho da fila já está correto até 6391/6440), MOC (seção antes de `## Mapa de escopo`, links de relatório em `## Fontes, revisão e cadência`), manifesto (seção antes de `## Critério de entrada na contagem`, artefatos), `batch-reconciliation-…-tranche-05.md`, STATUS, PLANO, README-1M, README KF, README raiz, RECOVERY-AND-SCALE-NOTE, Home, Indice-Global, PROMPT-CONTINUACAO.
- Estado esperado após a tranche 5: 6.640 arquivos, 6.540 válidas (49 humanas + 6.491 IA), lote 4 em 500/2.000 (25,00%), 15 tranches planejadas, faltam 993.460 notas.
- Anti-duplicação: gere inventário de `git ls-files knowledge-federation/domains/software-0010/software/criacao-ia/` (slug|título) e busque no vault inteiro antes de fixar temas; fontes primárias específicas conferidas por leitura na data — claim não confirmado não entra (na tranche 4 foram omitidos, p. ex., Bevy states/assets/events e o compositor do Blender por falta de fonte lida).
- NÃO tocar: relatórios e reconciliações das tranches 1–4 (histórico), `LOTS-201-300.md`, `MOC-Seguranca-Software-0009.md`, `archives/LATEST-LEDGER.txt`, dump `.xz` do ledger. `LOT-SEQUENCE` e `_meta/plano-execucao` não mudam por tranche.
- Verificações: `python3 -m unittest discover -s knowledge-federation/tests -v` (13 testes) e a auditoria global com `--path knowledge-federation/domains --archive knowledge-federation/archives/ledger-v1000000-mat8000.sqlite.xz` (esperado 6640/6540 pós-tranche 5); commit+push só na branch da sessão e PR para `main`.

TAREFA IMEDIATA:
1. Se o usuário pedir para avançar novamente, produzir a tranche 5 (de 16 planejadas restantes) com 100 notas do lote 4 em `knowledge-federation/domains/software-0010/software/criacao-ia/`, depois de selecionar tópicos e fontes primárias específicas.
2. Antes de atualizar contagens, rodar gate, revisão factual, auditoria de links e reconciliação; só contar notas substantivas aprovadas.
3. Não atribuir IDs às notas futuras, não abrir lote 5 automaticamente e publicar a tranche concluída na branch da sessão.

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
