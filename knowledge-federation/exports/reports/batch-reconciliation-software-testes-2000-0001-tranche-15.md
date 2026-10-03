# Reconciliação — `software-testes-2000-0001`, tranche 15

Data: 2026-10-02 (America/Sao_Paulo)

Resultado: **100 notas contabilizadas após gate e revisão factual por IA**. Esta reconciliação não representa aprovação humana.

## Escopo da tranche

- IDs: **850–949**, 100 arquivos em dez grupos de dez: pytest-xdist, cargo-nextest, coverage.py, Pest 5, Deno.test, Kotest 6.2, dbt data tests, MSW, Node.js `node:test` e pgTAP.
- Conteúdo substantivo: **198–274 palavras por nota**; cada nota contém duas fontes HTTPS específicas.
- Fontes e gerador: [`_build_tranche15.py`](../../scripts/_build_tranche15.py) e [`_tranche15_data/`](../../scripts/_tranche15_data/).
- Relatório factual: [`ai-review-software-testes-2000-0001-tranche-15.md`](ai-review-software-testes-2000-0001-tranche-15.md), com decisão e fonte principal nota a nota. Os metadados das 100 notas apontam para esse relatório; nenhuma aprovação humana foi criada ou estendida.

## Auditorias e resultados

| Verificação | Resultado |
|---|---|
| Gate do lote de testes de software | **949/949 válidas**; zero pendências. A auditoria do diretório cobre 949 arquivos, com 9 revisões humanas históricas e 940 revisões por IA. |
| Gate das notas novas | **100/100 aprovadas**; mínimo de 198 palavras e duas fontes HTTPS específicas por nota. |
| Revisão factual do lote | **9 humanas históricas + 940 por IA**; separação preservada. As 100 novas foram conferidas contra documentação oficial e aprovadas por IA. |
| Testes automatizados do repositório | **13 aprovados** (`python -m unittest discover -s knowledge-federation/tests -v`), incluindo regressão para garantir que o construtor deixa a revisão factual pendente. |
| Auditoria global por arquivos e ledger | **1089 Markdown ativos**: 989 válidos (49 humanas + 940 IA) e 100 legados com pendências, excluídos da contagem. O ledger contém 1.000.000 de registros virtuais/template e não contribui para notas válidas. |
| IDs, slugs e títulos | 100 IDs novos únicos no intervalo; sem colisões de slug/título com o inventário ativo. Os 1089 IDs encontrados são únicos. |
| Duplicação e sobreposição | Nenhum corpo substantivo duplicado no inventário; **zero pares** tranche 15 × notas anteriores com Jaccard ≥ 0,45 em shingles de cinco palavras; o construtor também não encontrou frases substantivas repetidas entre as 100 notas novas. |
| Links locais | A auditoria específica do lote terminou sem pendências de gate ou wikilinks não resolvidos; manifesto, fila e MOC apontam para a tranche 15. |
| Auditoria do registro SQLite | `audit_batch.py` não encontrou o lote no `registry/knowledge.sqlite`, que está vazio nesta checkout. A contagem editorial e o gate foram verificados diretamente nos arquivos por `audit_note_quality.py`; `global-audit-fast.md` registra explicitamente esse limite do banco local. |

Relatórios reproduzíveis: [qualidade do lote](note-quality-software-testes-2000-0001.md), [qualidade global](note-quality-audit.md) e [auditoria rápida do inventário](global-audit-fast.md). O zero do SQLite local não altera a contagem editorial por arquivos.

## Conferência factual

As afirmações foram comparadas com documentação oficial específica de cada ferramenta, incluindo diferenças de versão, semântica de opções, garantias de concorrência, limites de cobertura, estados de falha e ressalvas operacionais. O relatório nota a nota registra as fontes principais e o escopo conferido. Entre as correções realizadas antes da aprovação estão sintaxe Kotest 6.2, permissões e limites de cobertura no Deno, falhas/limites de armazenamento no dbt, interceptação HTTP/WebSocket e isolamento contextual no MSW, randomização experimental no `node:test` e semânticas de comparação SQL no pgTAP. Revisão factual por IA não garante ausência de erro.

## Contagens reconciliadas

- Lote `software-testes-2000-0001`: **949/2.000 (47,45%)**; 9 aprovações humanas + 940 revisões factuais por IA; **1.051 notas materiais restantes**; estado permanece `in_progress`.
- Total global: **989/1.000.000 (0,0989%)**; 49 aprovações humanas + 940 revisões factuais por IA. Os 100 arquivos legados com pendências continuam excluídos.
- O MOC, o manifesto, a fila, os relatórios de qualidade e os resumos ativos foram sincronizados. A meta global continua **1.000.000**, sem reativar a meta anterior de 2.000.000.
- Nenhuma tranche posterior foi iniciada; salvar este estado no GitHub antes de avançar.
