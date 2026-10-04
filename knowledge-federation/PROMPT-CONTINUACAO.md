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

CONTEXTO JÁ VERIFICADO (na main, não recalcular do zero):
- Meta ativa: 500 lotes × 2.000 notas substantivas = 1.000.000 de notas válidas.
- Estado: 5.640 / 1.000.000 (0,5640%) válidas; 2/500 lotes completos; 5.740 arquivos Markdown ativos (5.640 válidas + 100 legadas com pendências, mantidas fora da contagem).
- Lote 1 `software-testes-2000-0001`: 2.000/2.000 (complete) — 9 humanas + 1.991 revisões por IA; em domains/software-0007/software/testes/.
- Lote 2 `software-devops-2000-0002`: 2.000/2.000 (complete) — 2.000 por IA; em domains/software-0008/software/devops/.
- Lote 3 `software-seguranca-2000-0003`: 1.600/2.000 (80,00%) — tranches 1–16, todas por IA; em domains/software-0009/software/seguranca/; faltam 400 notas (tranches 17–20, IDs 1601–2000).
- Protocolo de contagem: a nota só vale com frontmatter rastreável, ≥100 palavras, seções de explicação/exemplo/limites/como verificar, duas fontes HTTPS específicas, wikilinks resolvidos, sem marcadores de template, e revisão factual registrada — humana (`revisao_humana: aprovada` + `revisor`) ou por IA (`revisao_ia: aprovada` + `revisor_ia` + `data_revisao_ia` + `relatorio_revisao_ia`). Revisão por IA nunca preenche nem altera campos humanos.
- Artefatos por tranche: `exports/batches/<lote>.md` (manifesto), `exports/reports/ai-review-<lote>-tranche-NN.md`, `exports/reports/batch-reconciliation-<lote>-tranche-NN.md`, `exports/reports/note-quality-<lote>.md`, `exports/reports/human-review-queue.md`, `00-home-vault/MOCs/MOC-<Tema>-Software-00NN.md`, `STATUS-CONSOLIDACAO-1M.md`, `PLANO-CONTINUO-1M.md`, `README.md`, `00-home-vault/Home.md` e `00-home-vault/Indice-Global.md`.

TAREFA IMEDIATA:
1. Fechar o lote 3: produzir as tranches 17, 18, 19 e 20 (IDs 1601–2000), 100 notas substantivas por tranche em knowledge-federation/domains/software-0009/software/seguranca/, com uma tranche por commit e push no fim de cada uma.
2. Após cada tranche, rodar gate + auditorias, reconciliar manifesto/MOC/relatórios/índices e atualizar a contagem global (numerador e denominador).
3. Ao chegar a 2.000/2.000, marcar o lote 3 como `complete` e abrir o lote 4 `software-<tema>-2000-0004` em domains/software-0010/, com MOC, manifesto e relatórios próprios, mantendo a cadência de 20 tranches × 100 notas.
4. Nunca contar IDs reservados, placeholders, catálogo virtual do ledger, links ou arquivos vazios como progresso. Nunca alegar conclusão da meta de 1.000.000 antes do fim.

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
