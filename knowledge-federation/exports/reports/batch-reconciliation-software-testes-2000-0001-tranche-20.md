# Reconciliação — `software-testes-2000-0001`, tranche 20

Data: 2026-10-03

Resultado: **101 notas contabilizadas após gate e revisão factual por IA**. Esta reconciliação não representa aprovação humana.

## Escopo da tranche

- IDs: **1359–1459**, 101 arquivos em dez grupos temáticos (dez ou onze notas cada); conteúdo substantivo de **171–212 palavras por nota**, conforme o construtor.
- Fontes e dados reproduzíveis: [`_build_tranche20.py`](../../scripts/_build_tranche20.py) e [`_tranche20_data/`](../../scripts/_tranche20_data/).
- Relatório de revisão: [`ai-review-software-testes-2000-0001-tranche-20.md`](ai-review-software-testes-2000-0001-tranche-20.md). Registra 101 decisões factuais por IA, sem alterar as 49 aprovações humanas históricas.
- Grupos: Gauge, Behave, MockServer, Keploy, Selenide, AssertJ, MockK, fast-check, Robolectric e NBomber.

## Auditorias e resultados

| Verificação | Resultado |
|---|---|
| Gate do lote de testes de software | **1459/1459 aprovadas**; 0 pendências. A auditoria específica incluiu as 1358 notas anteriores e as 101 novas. |
| Gate das notas novas | **101/101 aprovadas**; mínimo de 171 palavras, seções obrigatórias e duas fontes HTTPS específicas por nota. |
| Revisão factual do lote | **9 humanas históricas + 1450 por IA**; separação preservada. As novas 101 foram revisadas por IA. |
| Testes automatizados do repositório | **12 aprovados** (`python -m unittest discover -s knowledge-federation/tests -v`). |
| Auditoria global por arquivos e ledger | **1599 Markdown ativos**, 1499 válidos (49 humanas + 1450 IA) e 100 legados com pendências, excluídos da contagem. O ledger mantém 1.000.000 registros-template e não contribui para notas válidas. |
| IDs, títulos, slugs e conteúdo duplicado | 101 IDs únicos no intervalo; sem colisão de slug/título com o inventário ativo; nenhum corpo idêntico; similaridade Jaccard máxima de shingles de cinco palavras de **0,0661** contra notas anteriores e **0,0756** dentro da tranche. |
| Frases substantivas repetidas | Nenhuma repetição entre as notas 1359–1459, nem entre uma delas e as notas anteriores comparadas. |
| Links locais | Os wikilinks das novas notas foram resolvidos pelo gate; **3176 links relativos** de todos os documentos foram verificados após esta reconciliação, sem alvo ausente. |

Relatórios reproduzíveis: [qualidade do lote](note-quality-software-testes-2000-0001.md), [qualidade global](note-quality-audit.md) e [auditoria rápida do inventário](global-audit-fast.md). A auditoria rápida mostra zeros do SQLite local vazio; isso **não** substitui a contagem editorial por arquivos acima.

## Conferência de fontes e escopo factual

As afirmações foram comparadas às páginas oficiais atuais indicadas nas próprias notas:

- **Gauge — especificações em markdown, passos, conceitos e execução** (itens 1359–1368): Conferi a visão geral, a escrita de especificações, a execução, a configuração e a referência de linha de comando do Gauge antes de redigir as dez notas.
- **Behave — Gherkin, definições de passo, ganchos e fixtures** (itens 1369–1378): Conferi o guia de estrutura de testes, o tutorial, a referência de API, a página de fixtures e as expressões de etiqueta do Behave antes de redigir as dez notas.
- **MockServer — expectativas, verificação, proxy e contratos** (itens 1379–1388): Conferi a página de criação de expectativas, as páginas de verificação de pedidos e de respostas, o guia de proxy e o suporte a OpenAPI do MockServer antes de redigir as dez notas.
- **Keploy — gravação de tráfego, mocks e repetição na esteira** (itens 1389–1398): Conferi a documentação inicial, a página de testes de API e o repositório oficial do Keploy antes de redigir as dez notas.
- **Selenide — esperas automáticas, coleções e objetos de página** (itens 1399–1408): Conferi a documentação da API, a página de objetos de página, o FAQ e a documentação de relatórios do Selenide antes de redigir as dez notas.
- **AssertJ — asserções fluentes, coleções, descrições e suaves** (itens 1409–1418): Conferi a documentação principal, a referência de API publicada e o repositório oficial do AssertJ antes de redigir as dez notas.
- **MockK — dublês, relaxamento, verificação e corrotinas** (itens 1419–1428): Conferi o README oficial, o guia de corrotinas e o repositório do MockK antes de redigir as dez notas.
- **fast-check — propriedades, geradores, redução e modelos** (itens 1429–1438): Conferi o guia inicial, o pacote publicado e o repositório oficial do fast-check antes de redigir as dez notas.
- **Robolectric — testes na JVM, sombras e configuração** (itens 1439–1448): Conferi a página de primeiros passos, a página de configuração, a documentação de sombras e o repositório oficial do Robolectric antes de redigir as dez notas.
- **NBomber — cenários de carga, simulações, limites e relatórios** (itens 1449–1459): Conferi a página oficial, o pacote publicado e o repositório do NBomber antes de redigir as onze notas.

Cada nota mantém ressalvas e pelo menos duas URLs oficiais específicas; revisão factual por IA não é garantia de ausência de erro.

## Contagens reconciliadas

- Lote `software-testes-2000-0001`: **1459/2.000 (72,95%)**; 9 aprovações humanas + 1450 revisões factuais por IA; **541 notas materiais restantes**; estado permanece `in_progress`.
- Total global: **1499/1.000.000 (0,1499%)**; 49 aprovações humanas + 1450 revisões factuais por IA. Os 100 arquivos legados com pendências continuam excluídos.
- O MOC, o manifesto, a fila, os relatórios de qualidade e os resumos ativos foram sincronizados. A meta global continua **1.000.000**, sem reativar a meta anterior de 2.000.000.
- Nenhuma tranche posterior foi iniciada; salvar este estado no GitHub antes de avançar.
