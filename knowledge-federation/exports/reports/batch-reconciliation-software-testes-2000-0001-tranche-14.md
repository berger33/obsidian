# Reconciliação — `software-testes-2000-0001`, tranche 14

Data: 2026-10-02

Resultado: **100 notas contabilizadas após gate e revisão factual por IA**. Esta reconciliação não representa aprovação humana.

## Escopo da tranche

- IDs: **750–849**, 100 arquivos em dez grupos de dez; conteúdo substantivo de **175–237 palavras por nota**, conforme o construtor.
- Fontes e dados reproduzíveis: [`_build_tranche14.py`](../../scripts/_build_tranche14.py) e [`_tranche14_data/`](../../scripts/_tranche14_data/).
- Relatório de revisão: [`ai-review-software-testes-2000-0001-tranche-14.md`](ai-review-software-testes-2000-0001-tranche-14.md). Registra 100 decisões factuais por IA, sem alterar as 49 aprovações humanas históricas.

## Auditorias e resultados

| Verificação | Resultado |
|---|---|
| Gate do lote de testes de software | **849/849 aprovadas**; 0 pendências. A auditoria específica incluiu as 749 notas anteriores e as 100 novas. |
| Gate das notas novas | **100/100 aprovadas**; mínimo de 175 palavras e duas fontes HTTPS específicas por nota. |
| Revisão factual do lote | **9 humanas históricas + 840 por IA**; separação preservada. As novas 100 foram revisadas por IA. |
| Testes automatizados do repositório | **12 aprovados** (`python -m unittest discover -s knowledge-federation/tests -v`). |
| Auditoria global por arquivos e ledger | **989 Markdown ativos**, 889 válidos (49 humanas + 840 IA) e 100 legados com pendências, excluídos da contagem. O ledger mantém 1.000.000 registros-template e não contribui para notas válidas. |
| IDs, títulos, slugs e conteúdo duplicado | 100 IDs únicos no intervalo; sem colisão de slug/título com o inventário ativo; nenhum corpo idêntico e nenhum par com similaridade Jaccard de shingles de cinco palavras ≥ 0,45 envolvendo a tranche. |
| Frases substantivas repetidas | Nenhuma repetição entre as notas 750–849, nem entre uma delas e as notas anteriores comparadas. |
| Links locais | Os 100 wikilinks das notas e as novas referências do manifesto, fila e MOC foram resolvidos; manifesto e fila mantêm a sequência completa atualizada. |

Relatórios reproduzíveis: [qualidade do lote](note-quality-software-testes-2000-0001.md), [qualidade global](note-quality-audit.md) e [auditoria rápida do inventário](global-audit-fast.md). A auditoria rápida mostra zeros do SQLite local vazio; isso **não** substitui a contagem editorial por arquivos acima.

## Conferência de fontes e escopo factual

As afirmações foram comparadas às páginas oficiais atuais indicadas nas próprias notas: Bazel, Maven Surefire/Failsafe, Gradle JVM testing, Django 6.1, Android Espresso, Rails 8.1 e APIs 8.1.4, tox 4, Nox, Laravel 13 e Python 3.14. A verificação pontual confirmou, entre outros itens, `-Dit.test` na documentação de Failsafe, helpers ActiveJob/ActionMailer nas APIs Rails, fakes de eventos/filas/mail no Laravel e o contrato de descoberta/mocks do `unittest`. Cada nota mantém ressalvas e pelo menos duas URLs oficiais específicas; revisão factual por IA não é garantia de ausência de erro.

## Contagens reconciliadas

- Lote `software-testes-2000-0001`: **849/2.000 (42,45%)**; 9 aprovações humanas + 840 revisões factuais por IA; **1.151 notas materiais restantes**; estado permanece `in_progress`.
- Total global: **889/1.000.000 (0,0889%)**; 49 aprovações humanas + 840 revisões factuais por IA. Os 100 arquivos legados com pendências continuam excluídos.
- O MOC, o manifesto, a fila, os relatórios de qualidade e os resumos ativos foram sincronizados. A meta global continua **1.000.000**, sem reativar a meta anterior de 2.000.000.
- Nenhuma tranche posterior foi iniciada; salvar este estado no GitHub antes de avançar.
