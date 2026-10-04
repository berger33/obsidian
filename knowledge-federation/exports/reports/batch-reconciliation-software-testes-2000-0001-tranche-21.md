# Reconciliação — `software-testes-2000-0001`, tranche 21

Data: 2026-10-03

Resultado: **100 notas contabilizadas após gate e revisão factual por IA**. Esta reconciliação não representa aprovação humana.

## Escopo da tranche

- IDs: **1460–1559**, 100 arquivos em dez grupos temáticos com dez notas cada; conteúdo substantivo de **185–242 palavras por nota**, conforme o construtor.
- Fontes e dados reproduzíveis: [`_build_tranche21.py`](../../scripts/_build_tranche21.py) e [`_tranche21_data/`](../../scripts/_tranche21_data/).
- Relatório de revisão: [`ai-review-software-testes-2000-0001-tranche-21.md`](ai-review-software-testes-2000-0001-tranche-21.md). Registra 100 decisões factuais por IA, sem alterar as 49 aprovações humanas históricas.
- Grupos: Nightwatch, AVA, Chai, Sinon.JS, VCR.py, freezegun, mutmut, cargo-mutants, Toxiproxy e Jazzer.
- Contexto de retomada: esta tranche continua a série a partir da tranche 20; a tranche 15 alternativa registrada no branch `arena/01a0f9df-obsidian` permanece substituída pela versão reconciliada no histórico do branch `arena/01a0ff06-obsidian`.

## Auditorias e resultados

| Verificação | Resultado |
|---|---|
| Gate do lote de testes de software | **1559/1559 aprovadas**; 0 pendências. A auditoria específica incluiu as 1459 notas anteriores e as 100 novas. |
| Gate das notas novas | **100/100 aprovadas**; mínimo de 100 palavras por nota, seções obrigatórias e duas fontes HTTPS específicas por nota. |
| Revisão factual do lote | **9 humanas históricas + 1550 por IA**; separação preservada. As novas 100 foram revisadas por IA. |
| Testes automatizados do repositório | **12 aprovados** (`python -m unittest discover -s knowledge-federation/tests`). |
| Auditoria global por arquivos | **1699 Markdown ativos**, 1599 válidos (49 humanas + 1550 IA) e 100 legados com pendências, excluídos da contagem. O ledger mantém 1.000.000 registros-template e não contribui para notas válidas. |
| IDs, títulos, slugs e conteúdo duplicado | 100 IDs únicos no intervalo; sem colisão de slug/título com o inventário ativo; nenhum corpo idêntico. Similaridade Jaccard máxima de shingles de cinco palavras no texto completo: **0,0386** contra notas anteriores e **0,1511** dentro da tranche — esta última atribuída às linhas Fontes/Conexões idênticas quando um grupo cita poucas páginas oficiais; no corpo substantivo (sem `## Fontes` nem `## Conexões`) as máximas caem para **0,0518** e **0,0128**. |
| Frases substantivas repetidas | Nenhuma repetição entre as notas 1460–1559 (gate de prosa do construtor). |
| Links relativos | Verificados após esta reconciliação em todos os documentos Markdown ativos, com alvos resolvidos, incluindo os 9 vínculos ao presente relatório criados pela reconciliação das documentações. |

Relatórios reproduzíveis: [qualidade do lote](note-quality-software-testes-2000-0001.md), [qualidade global](note-quality-audit.md) e [auditoria rápida do inventário](global-audit-fast.md). A auditoria rápida mostra zeros do SQLite local vazio; isso **não** substitui a contagem editorial por arquivos acima.

## Conferência de fontes e escopo factual

As afirmações foram comparadas às páginas oficiais atuais indicadas nas próprias notas:

- **Nightwatch — framework integrado de navegador e configuração** (itens 1460–1469): Conferi a página Visão geral, a referência de Config Settings, a instalação e o repositório oficial do Nightwatch antes de redigir as dez notas.
- **AVA — concorrência, modificadores e hooks por arquivo** (itens 1470–1479): Conferi o README oficial do AVA e o guia Writing tests do repositório, incluindo as páginas referenciadas sobre contexto de execução e configuração, antes de redigir as dez notas.
- **Chai — correntes de linguagem, negação e verificação por tipo** (itens 1480–1489): Conferi a referência de API BDD do Chai, o guia de estilos e as páginas de API should e assert citadas por ela antes de redigir as dez notas.
- **Sinon.JS — espiões, stubs, mocks, relógio e sandbox** (itens 1490–1499): Conferi a página inicial do Sinon com o exemplo de instalação e uso, além do material do repositório oficial antes de redigir as dez notas.
- **VCR.py — cassetes HTTP, modos de gravação e integração** (itens 1500–1509): Conferi as páginas Usage e Configuration da documentação do vcrpy (versão 8) e o repositório oficial antes de redigir as dez notas.
- **freezegun — congelar, deslocar e avançar o relógio do teste** (itens 1510–1519): Conferi o README publicado na página do PyPI do freezegun (uso, fuso, tick e limites) e o repositório oficial vinculado a ela antes de redigir as dez notas.
- **mutmut — mutantes incrementais, triagem interativa e filtros** (itens 1520–1529): Conferi o README oficial do mutmut no repositório boxed/mutmut (instalação, browse, configuração e filtros) e o artigo introdutório linkado por ele antes de redigir as dez notas.
- **cargo-mutants — mutação em crates, skip e saída auditable** (itens 1530–1539): Conferi o README oficial do cargo-mutants (resultados, skip, saída e dicas) e a página do pacote no crates.io antes de redigir as dez notas.
- **Toxiproxy — toxics de rede sobre proxy TCP controlado por HTTP** (itens 1540–1549): Conferi o README oficial do Toxiproxy (proposta, instalação, populate, toxics, campos da API HTTP e clientes) antes de redigir as dez notas.
- **Jazzer — fuzzing de JVM dirigido por cobertura com sanitizers** (itens 1550–1559): Conferi o README oficial do Jazzer no repositório CodeIntelligenceTesting (modo standalone, modo JUnit, diretórios de corpus e sanitizers) e o documento de argumentos linkado por ele antes de redigir as dez notas.

Cada nota mantém ressalvas e pelo menos duas URLs oficiais específicas; revisão factual por IA não é garantia de ausência de erro.

## Contagens reconciliadas

- Lote `software-testes-2000-0001`: **1559/2.000 (77,95%)**; 9 aprovações humanas + 1550 revisões factuais por IA; **441 notas materiais restantes**; estado permanece `in_progress`.
- Total global: **1599/1.000.000 (0,1599%)**; 49 aprovações humanas + 1550 revisões factuais por IA. Os 100 arquivos legados com pendências continuam excluídos.
- O MOC, o manifesto, a fila, os relatórios de qualidade e os resumos ativos foram sincronizados. A meta global continua **1.000.000**, sem reativar a meta anterior de 2.000.000.
- Nenhuma tranche posterior foi iniciada; salvar este estado no GitHub antes de avançar.
