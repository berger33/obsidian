# Reconciliação — `software-testes-2000-0001`, tranche 26 (conclusão do lote 2.000/2.000)

Data: 2026-10-03

Resultado: **41 notas finais contabilizadas após gate e revisão factual por IA**, concluindo o primeiro lote de escala `software-testes-2000-0001` com **2.000 / 2.000 notas válidas (100%)** (`complete`). Esta reconciliação não representa aprovação humana.

## Escopo da tranche

- IDs: **1960–2000**, 41 arquivos em quatro grupos temáticos (três grupos de dez notas e um grupo final de onze notas); conteúdo substantivo de **310–444 palavras por nota**, conforme o construtor.
- Fontes e dados reproduzíveis: [`_build_tranche26.py`](../../scripts/_build_tranche26.py) e [`_tranche26_data/`](../../scripts/_tranche26_data/).
- Relatório de revisão: [`ai-review-software-testes-2000-0001-tranche-26.md`](ai-review-software-testes-2000-0001-tranche-26.md). Registra 41 decisões factuais por IA, sem alterar as 49 aprovações humanas históricas.
- Grupos: ESBMC (10 notas, 1960–1969), SymbiYosys (10 notas, 1970–1979), gocheck (10 notas, 1980–1989) e Psalm (11 notas, 1990–2000).
- Contexto de retomada: esta tranche encerra a série iniciada após a tranche 25, completando as 2.000 notas substantivas do lote `software-testes-2000-0001` sob a mesma política editorial (gate automatizado + revisão factual registrada; revisão por IA nunca rotulada como humana).

## Auditorias e resultados

| Verificação | Resultado |
|---|---|
| Gate do lote de testes de software | **2000/2000 aprovadas (100%)**; 0 pendências. A auditoria específica incluiu as 1959 notas anteriores e as 41 novas. |
| Gate das notas novas | **41/41 aprovadas**; mínimo de 100 palavras por nota, seções obrigatórias e duas fontes HTTPS específicas (com caminho próprio) por nota. |
| Revisão factual do lote | **9 humanas históricas + 1991 por IA**; separação preservada. As novas 41 foram revisadas por IA. |
| Testes automatizados do repositório | **12 aprovados** (`python -m unittest discover -s knowledge-federation/tests`). |
| Auditoria global por arquivos | **2140 Markdown ativos**, 2040 válidos (49 humanas + 1991 IA) e 100 legados com pendências, excluídos da contagem. O ledger mantém 1.000.000 registros-template e não contribui para notas válidas. |
| Fila de revisão | Posições **nº 50–2040** com exatamente uma linha `APROVADA POR IA` cada (1991 linhas); as 41 linhas novas (2000–2040) correspondem às notas 1960–2000. |
| IDs, títulos, slugs e conteúdo duplicado | 41 IDs únicos no intervalo 1960–2000; sem colisão de slug/título com o inventário ativo; nenhum corpo idêntico. Similaridade Jaccard de shingles de cinco palavras no texto completo (frontmatter excluído): média **0,0011** contra amostra de 400 notas de outros lotes/grupos e **0,0332** dentro da tranche. No corpo substantivo (sem `## Fontes` nem `## Conexões`) as médias caem para **0,0001** e **0,0013**, com máximo **0,0184** (par interno `gocheck-assert-vs-check-methods` × `gocheck-commentinterface-and-commentf`, que menciona o contrato do último argumento `CommentInterface` em `Assert` e `Check`). |
| Frases substantivas repetidas | Nenhuma repetição entre as notas 1960–2000 (gate de prosa do construtor). |
| Links relativos | **7932 vínculos relativos verificados** nos documentos reconciliados e nas 2000 notas do lote (wikilinks resolvidos contra o vault inteiro), todos com alvos resolvidos — incluindo os vínculos ao presente relatório criados pela própria reconciliação; 0 quebrados. |

Relatórios reproduzíveis: [qualidade do lote](note-quality-software-testes-2000-0001.md), [qualidade global](note-quality-audit.md) e [auditoria rápida do inventário](global-audit-fast.md). A auditoria rápida mostra zeros do SQLite local vazio; isso **não** substitui a contagem editorial por arquivos acima.

## Conferência de fontes e escopo factual

As afirmações foram comparadas ao conteúdo das fontes primárias capturadas para cada grupo:

- **ESBMC — model checker limitado por contexto baseado em SMT para múltiplas linguagens** (itens 1960–1969): Conferi o README oficial no repositório `esbmc/esbmc` (definição, linguagens suportadas e os cinco frontends — Clang, Soot/Jimple, CPython 3.10, Solidity e ESBMC-PLC Ladder Diagram —, algoritmos incremental BMC e k-induction, lista de erros detectados em código sequencial e concorrente pthread, os sete solvers SMT mais SMTLIB pipe e os backends one-shot `--bitwuzllob` e `--neurosym`, instalação via PPA Ubuntu/Homebrew/releases, três integrações de editor/ferramenta e exemplo com `--incremental-bmc`) antes de redigir as dez notas.
- **SymbiYosys — verificação formal de hardware em Verilog e SystemVerilog sobre o Yosys** (itens 1970–1979): Conferi o README oficial no repositório `YosysHQ/sby` (definição como driver front-end para fluxos de verificação formal de hardware baseados no Yosys, licença ISC e licenças próprias dos solvers, distribuição no OSS CAD Suite e Tabby CAD Suite com suporte SVA/VHDL) e a página Getting started da documentação oficial em `yosyshq.readthedocs.io/projects/sby/en/latest/quickstart.html` (exemplo FIFO em `fifo.sv`, propriedades `assert` e `$past`, tarefas em `fifo.sby` com `:default`, execução `sby` e `sby -f`, artefatos `trace.vcd` / `trace_tb.v` / `trace.smtc` com `rc=2` e inspeção no GTKWave) antes de redigir as dez notas.
- **gocheck — extensão de suítes, checkers e fixtures para o pacote testing do Go** (itens 1980–1989): Conferi o README oficial no repositório `go-check/check` (branch `v1`, instalação com `go get gopkg.in/check.v1` e import com nome de pacote `check`) e a documentação oficial da API em `pkg.go.dev/gopkg.in/check.v1` (funções `Suite`, `TestingT`, `Run`, `RunAll`, `List` e `ListAll`, tipo `C` e seus métodos `Assert`, `Check`, `ExpectFailure`, `MkDir`, `Skip`, `Succeed`/`SucceedNow`, `GetTestLog` e métodos de benchmark, além de `Checker`, `Not`, `CheckerInfo`, `CommentInterface`/`Commentf` e `Result`/`RunConf`) antes de redigir as dez notas.
- **Psalm — análise estática de tipos, execução incremental e revisão interativa para PHP** (itens 1990–2000): Conferi o README oficial na branch `6.x` do repositório `vimeo/psalm` (proposta, canais, live demo em `psalm.dev`, documentação em `psalm.dev/docs`, suporte e mantenedores), o guia oficial `docs/running_psalm/installation.md` (requisito PHP >= 8.2 e Composer, `psalm --init`, `psalm --no-cache`, imagem Docker `ghcr.io/danog/psalm` +30%/+50% mais rápida, extensões e `phpstorm-stubs`, plugins com `psalm-plugin enable` e uso via Phar) e o guia oficial `docs/running_psalm/command_line_usage.md` (execução no projeto ou em arquivos específicos, códigos de saída `0`/`1`/`2`, integração `--shepherd`, aceleração com `--threads` e `--diff`/`--no-diff` e revisão interativa com `psalm-review`) antes de redigir as onze notas finais do lote.

Cada nota mantém ressalvas e pelo menos duas URLs oficiais específicas; revisão factual por IA não é garantia de ausência de erro. Links de páginas apenas referenciadas nos documentos primários (por exemplo `ARCHITECTURE.md` no ESBMC ou `dealing_with_code_issues.md` no Psalm) foram usados como ponteiro de navegação, sem afirmações além do material efetivamente lido.

## Contagens reconciliadas

- Lote `software-testes-2000-0001`: **2000/2.000 (100%)**; 9 aprovações humanas + 1991 revisões factuais por IA; **0 notas materiais restantes neste lote**; estado passa a `complete`.
- Lotes de escala completos: **1 / 500** (`software-testes-2000-0001`).
- Total global: **2040/1.000.000 (0,2040%)**; 49 aprovações humanas + 1991 revisões factuais por IA. Os 100 arquivos legados com pendências continuam excluídos. Faltam **997.960** notas válidas para a meta.
- O MOC, o manifesto, a fila, os relatórios de qualidade e os resumos ativos foram sincronizados, incluindo as cadeias de vínculo dos relatórios de IA (tranches 2–26) e da reconciliação mais recente (tranche 26). A meta global continua **1.000.000**, sem reativar a meta anterior de 2.000.000.
