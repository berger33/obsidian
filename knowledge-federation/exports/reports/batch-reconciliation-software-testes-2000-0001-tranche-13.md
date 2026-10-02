# Reconciliação — `software-testes-2000-0001`, tranche 13

Data: 2026-10-02

Resultado: **100 notas contabilizadas após gate e revisão factual por IA**. Esta reconciliação não representa aprovação humana.

## Escopo da tranche

- IDs: **650–749**, 100 arquivos em dez grupos de dez; conteúdo substantivo de 173–229 palavras por nota, conforme o construtor.
- Fontes e dados reproduzíveis: [`_build_tranche13.py`](../../scripts/_build_tranche13.py) e [`_tranche13_data/`](../../scripts/_tranche13_data/).
- Relatório de revisão: [`ai-review-software-testes-2000-0001-tranche-13.md`](ai-review-software-testes-2000-0001-tranche-13.md). Registra 100 decisões factuais por IA, sem alterar as 49 aprovações humanas históricas.

## Auditorias e resultados

| Verificação | Resultado |
|---|---|
| Gate do lote de testes de software | **749/749 aprovadas**; 0 pendências. O relatório abrange as 649 notas anteriores e as 100 novas. |
| Revisão factual do lote | **9 humanas históricas + 740 por IA**; separação preservada. As novas 100 foram revisadas por IA. |
| Testes automatizados do repositório | **12 aprovados** (`python -m unittest discover -s knowledge-federation/tests -v`). |
| Auditoria global por arquivos | **889 Markdown ativos**, 789 válidos (49 humanas + 740 IA) e 100 legados com pendências, excluídos da contagem. O ledger contém 1.000.000 de registros-template e não contribui para notas válidas. |
| IDs, títulos, slugs e conteúdo duplicado | 100 IDs únicos no intervalo; nenhuma colisão de slug/título entre os arquivos da tranche e os domínios ativos; nenhum corpo idêntico e nenhum par com similaridade Jaccard de shingles de cinco palavras ≥ 0,45 envolvendo a tranche. |
| Frases substantivas repetidas | Nenhuma repetição entre as notas 650–749 nem entre uma delas e uma nota anterior. A varredura mais ampla encontrou padrões repetidos apenas em notas antigas até o ID 449; não foram alterados nesta tranche. |
| Referências locais atualizadas | Manifesto com IDs 1–749; fila com 49 decisões humanas e 740 por IA; MOC com os 100 novos links. Os links relativos adicionados no manifesto e na fila foram resolvidos. |

Relatórios reproduzíveis: [qualidade do lote](note-quality-software-testes-2000-0001.md), [qualidade global](note-quality-audit.md) e [auditoria rápida do inventário](global-audit-fast.md). A auditoria rápida mostra zeros do SQLite local vazio; isso **não** substitui a contagem editorial por arquivos acima.

## Conferência direcionada de fontes anteriormente sinalizadas

A checagem final foi direcionada às entradas que tinham alertas de URL/âncora:

- **Mocha retries:** a URL antiga de retries que retornava 404 não é usada pelo registro da nota. A nota `mocha-retry-diagnostic` aponta para a [CLI oficial](https://mochajs.org/running/cli/) e para o [modo paralelo](https://mochajs.org/features/parallel-mode/); a CLI atual inclui a opção `--retries`.
- **ScalaTest assíncrono:** substituída a referência Scaladoc de `AsyncFlatSpec` que não abria pela [seção oficial de testes assíncronos](https://www.scalatest.org/user_guide/async_testing), com a [página oficial de execução](https://www.scalatest.org/user_guide/running_your_tests) como fonte complementar. Ambas abriram e a seção assíncrona documenta estilos como `AsyncFlatSpec` e resultados `Future[Assertion]`.
- **Ginkgo/Gomega:** os destinos oficiais atuais foram conferidos: [paralelismo](https://onsi.github.io/ginkgo/#spec-parallelization), [labels](https://onsi.github.io/ginkgo/#spec-labels), [randomização](https://onsi.github.io/ginkgo/#spec-randomization), [tabelas](https://onsi.github.io/ginkgo/#table-specs), [decorators](https://onsi.github.io/ginkgo/MIGRATING_TO_V2#spec-decorators) e [asserções assíncronas do Gomega](https://onsi.github.io/gomega/#making-asynchronous-assertions). Os nomes de âncora atualizados correspondem às seções da documentação.

## Contagens reconciliadas

- Lote `software-testes-2000-0001`: **749/2.000 (37,45%)**; 9 aprovações humanas + 740 revisões factuais por IA; **1.251 notas materiais restantes**; estado permanece `in_progress`.
- Total global: **789/1.000.000 (0,0789%)**; 49 aprovações humanas + 740 revisões factuais por IA. Os 100 arquivos legados com pendências continuam excluídos.
- O MOC, o manifesto, a fila de revisão, os relatórios de qualidade e os resumos ativos foram sincronizados com essas contagens. A meta global continua **1.000.000**, sem reativar a meta anterior de 2.000.000.
- Nenhuma tranche posterior foi iniciada; avançar somente depois de salvar este estado no GitHub.
