# Reconciliação — `software-testes-2000-0001`, tranche 22

Data: 2026-10-03

Resultado: **100 notas contabilizadas após gate e revisão factual por IA**. Esta reconciliação não representa aprovação humana.

## Escopo da tranche

- IDs: **1560–1659**, 100 arquivos em dez grupos temáticos com dez notas cada; conteúdo substantivo de **202–279 palavras por nota**, conforme o construtor.
- Fontes e dados reproduzíveis: [`_build_tranche22.py`](../../scripts/_build_tranche22.py) e [`_tranche22_data/`](../../scripts/_tranche22_data/).
- Relatório de revisão: [`ai-review-software-testes-2000-0001-tranche-22.md`](ai-review-software-testes-2000-0001-tranche-22.md). Registra 100 decisões factuais por IA, sem alterar as 49 aprovações humanas históricas.
- Grupos: Bats-core, Pester, Reqnroll, FluentAssertions, jqwik, Kotest property testing, Tavern, responses, Hoverfly e gcovr.
- Contexto de retomada: esta tranche continua a série a partir da tranche 21; a política de conteúdo permanece a mesma das tranches anteriores (gate automatizado + revisão factual registrada; revisão por IA nunca rotulada como humana).

## Auditorias e resultados

| Verificação | Resultado |
|---|---|
| Gate do lote de testes de software | **1659/1659 aprovadas**; 0 pendências. A auditoria específica incluiu as 1559 notas anteriores e as 100 novas. |
| Gate das notas novas | **100/100 aprovadas**; mínimo de 100 palavras por nota, seções obrigatórias e duas fontes HTTPS específicas por nota. |
| Revisão factual do lote | **9 humanas históricas + 1650 por IA**; separação preservada. As novas 100 foram revisadas por IA. |
| Testes automatizados do repositório | **12 aprovados** (`python -m unittest discover -s knowledge-federation/tests`). |
| Auditoria global por arquivos | **1799 Markdown ativos**, 1699 válidos (49 humanas + 1650 IA) e 100 legados com pendências, excluídos da contagem. O ledger mantém 1.000.000 registros-template e não contribui para notas válidas. |
| Fila de revisão | Posições **nº 50–1699** com exatamente uma linha `APROVADA POR IA` cada (1650 linhas); as 100 linhas novas (1600–1699) correspondem às notas 1560–1659. |
| IDs, títulos, slugs e conteúdo duplicado | 100 IDs únicos no intervalo; sem colisão de slug/título com o inventário ativo; nenhum corpo idêntico. Similaridade Jaccard de shingles de cinco palavras no texto completo: média **0,0911** contra notas de outros grupos e **0,1647** dentro da tranche — os valores são puxados pelas linhas `## Fontes`/`## Conexões`, que repetem títulos de páginas oficiais dentro de um mesmo grupo; no corpo substantivo (sem `## Fontes` nem `## Conexões`) as médias caem para **0,0002** e **0,0004**, com máximo **0,0198** (par interno que cita a mesma mensagem de exemplo da documentação). |
| Frases substantivas repetidas | Nenhuma repetição entre as notas 1560–1659 (gate de prosa do construtor). |
| Links relativos | **3516 vínculos relativos verificados** nos documentos reconciliados e nas notas, todos com alvos resolvidos — incluindo os 9 vínculos ao presente relatório criados pela própria reconciliação. Wikilinks do vault auditados pelo gate: 0 quebrados. |

Relatórios reproduzíveis: [qualidade do lote](note-quality-software-testes-2000-0001.md), [qualidade global](note-quality-audit.md) e [auditoria rápida do inventário](global-audit-fast.md). A auditoria rápida mostra zeros do SQLite local vazio; isso **não** substitui a contagem editorial por arquivos acima.

## Conferência de fontes e escopo factual

As afirmações foram comparadas ao conteúdo das fontes primárias capturadas para cada grupo:

- **Bats-core — suíte TAP em Bash puro** (itens 1560–1569): Conferi o README oficial no GitHub, a página inicial da documentação, e as páginas Writing tests e Usage (opções do CLI, formatters, paralelismo) antes de redigir as dez notas.
- **Pester — testes e mocking em PowerShell** (itens 1570–1579): Conferi o quick start, a página de mocking e a página de code coverage (v6) da documentação oficial em pester.dev antes de redigir as dez notas.
- **Reqnroll — BDD Gherkin em .NET** (itens 1580–1589): Conferi o README oficial no repositório e a guia "Migrating from SpecFlow" em docs.reqnroll.net na íntegra (renomeações, compat package, DataTable helpers, atenções de MsTest e LivingDoc) antes de redigir as dez notas.
- **FluentAssertions — asserções encadeadas** (itens 1590–1599): Conferi a página Introduction (chaining, detecção de frameworks, subject identification, AssertionScope) e a página Object graphs (BeEquivalentTo, recursão, tipagem, exclusões) antes de redigir as dez notas.
- **jqwik — property testing na plataforma JUnit 5** (itens 1600–1609): Conferi o User Guide 1.10.1 (definição de engine, configuração Gradle, relatório de falha, lifecycle, shrinking e módulos) e os repositórios Maven citados por ele antes de redigir as dez notas.
- **Kotest property testing — forAll e checkAll em Kotlin** (itens 1610–1619): Conferi as páginas Property Test Functions, Configuration e Seeds da documentação oficial (versão 6.2) antes de redigir as dez notas.
- **Tavern — testes de API em YAML sobre pytest** (itens 1620–1629): Conferi a página inicial oficial (proposta, quickstart, CLI tavern-ci, comparativos com Postman/Insomnia/pyresttest) e o manifesto do repositório antes de redigir as dez notas.
- **responses — mocking da biblioteca requests** (itens 1630–1639): Conferi o README oficial no master do repositório getsentry (activate, add, atalhos, contexto, parâmetros, matchers, passthru, calls, callback) e a tabela de deprecações antes de redigir as dez notas.
- **Hoverfly — simulação de APIs por proxy** (itens 1640–1649): Conferi o README oficial, a página inicial da documentação v1.12.15, o Getting Started e os tutoriais básicos de exportação e de captura com estado (capture, headers, `--url-pattern`, `--stateful`, requiresState/transitionsState) antes de redigir as dez notas.
- **gcovr — cobertura gcov em texto e XML** (itens 1650–1659): Conferi a página inicial da doc 8.6 (matriz de formatos de saída), o Getting Started (flags `--coverage -g -O0`, `-r`, html-details/html-nested) e as opções de filtro/exclusão da referência de linha de comando antes de redigir as dez notas.

Cada nota mantém ressalvas e pelo menos duas URLs oficiais específicas; revisão factual por IA não é garantia de ausência de erro. Links de páginas apenas referenciadas (por exemplo `DataTable Helpers` e `Cucumber Expressions` no Reqnroll, ou `New-PesterConfiguration` no Pester) foram usados como ponteiro de navegação, sem afirmações além do material efetivamente lido.

## Contagens reconciliadas

- Lote `software-testes-2000-0001`: **1659/2.000 (82,95%)**; 9 aprovações humanas + 1650 revisões factuais por IA; **341 notas materiais restantes**; estado permanece `in_progress`.
- Total global: **1699/1.000.000 (0,1699%)**; 49 aprovações humanas + 1650 revisões factuais por IA. Os 100 arquivos legados com pendências continuam excluídos. Faltam **998.301** notas válidas para a meta.
- O MOC, o manifesto, a fila, os relatórios de qualidade e os resumos ativos foram sincronizados, incluindo as cadeias de vínculo dos relatórios de IA (tranches 2–22) e da reconciliação mais recente (tranche 22). A meta global continua **1.000.000**, sem reativar a meta anterior de 2.000.000.
- Sugestão de tranche 23 (cobertura ainda não atingida no inventário): suítes e ferramentas como WebdriverIO, TestCafe, Karma, JUnit 4, ApprovalTests, go-fuzz, cargo-fuzz, AFL++, boofuzz, Hyperfoil e k6-advanced — a lista definitiva sai do grep de colisão de prefixos de slug na abertura da próxima tranche.
