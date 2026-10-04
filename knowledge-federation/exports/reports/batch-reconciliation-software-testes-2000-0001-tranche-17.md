# Reconciliação — `software-testes-2000-0001`, tranche 17

Data: 2026-10-03

Resultado: **101 notas contabilizadas após gate e revisão factual por IA**. Esta reconciliação não representa aprovação humana.

## Escopo da tranche

- IDs: **1056–1156**, 101 arquivos em dez grupos temáticos (dez ou onze notas cada); conteúdo substantivo de **175–218 palavras por nota**, conforme o construtor.
- Fontes e dados reproduzíveis: [`_build_tranche17.py`](../../scripts/_build_tranche17.py) e [`_tranche17_data/`](../../scripts/_tranche17_data/).
- Relatório de revisão: [`ai-review-software-testes-2000-0001-tranche-17.md`](ai-review-software-testes-2000-0001-tranche-17.md). Registra 101 decisões factuais por IA, sem alterar as 49 aprovações humanas históricas.
- Grupos: Gatling, Locust, Robot Framework, Cucumber, Selenium WebDriver, Appium, WireMock, Pact, Testify e RSpec.

## Auditorias e resultados

| Verificação | Resultado |
|---|---|
| Gate do lote de testes de software | **1156/1156 aprovadas**; 0 pendências. A auditoria específica incluiu as 1055 notas anteriores e as 101 novas. |
| Gate das notas novas | **101/101 aprovadas**; mínimo de 175 palavras e duas fontes HTTPS específicas por nota. |
| Revisão factual do lote | **9 humanas históricas + 1147 por IA**; separação preservada. As novas 101 foram revisadas por IA. |
| Testes automatizados do repositório | **12 aprovados** (`python -m unittest discover -s knowledge-federation/tests -v`). |
| Auditoria global por arquivos e ledger | **1296 Markdown ativos**, 1196 válidos (49 humanas + 1147 IA) e 100 legados com pendências, excluídos da contagem. O ledger mantém 1.000.000 registros-template e não contribui para notas válidas. |
| IDs, títulos, slugs e conteúdo duplicado | 101 IDs únicos no intervalo; sem colisão de slug/título com o inventário ativo; nenhum corpo idêntico; similaridade Jaccard máxima de shingles de cinco palavras de **0,0543** contra notas anteriores e **0,0672** dentro da tranche. |
| Frases substantivas repetidas | Nenhuma repetição entre as notas 1056–1156, nem entre uma delas e as notas anteriores comparadas. |
| Links locais | Os wikilinks das novas notas foram resolvidos pelo gate; **2752 links relativos** dos documentos atualizados foram verificados, sem alvo ausente. |

Relatórios reproduzíveis: [qualidade do lote](note-quality-software-testes-2000-0001.md), [qualidade global](note-quality-audit.md) e [auditoria rápida do inventário](global-audit-fast.md). A auditoria rápida mostra zeros do SQLite local vazio; isso **não** substitui a contagem editorial por arquivos acima.

## Conferência de fontes e escopo factual

As afirmações foram comparadas às páginas oficiais atuais indicadas nas próprias notas:

- **Gatling — simulações, injeção de carga, checagens e asserções** (itens 1056–1065): Conferi os conceitos de simulação, cenário e injeção, a referência de protocolo HTTP, o repositório oficial e o tutorial de código como teste do Gatling antes de redigir as dez notas.
- **Locust — usuários, tarefas, tempos de espera e formas de carga** (itens 1066–1075): Conferi o guia de escrita do arquivo de teste, o início rápido, a página de formas de carga personalizadas e o repositório oficial do Locust antes de redigir as dez notas.
- **Robot Framework — palavras-chave, dados de teste, etiquetas e execução** (itens 1076–1085): Conferi o guia do usuário, a página oficial do projeto e o repositório do Robot Framework para sintaxe de testes, palavras-chave, modelos de dados, etiquetas e execução antes de redigir as dez notas.
- **Cucumber — Gherkin, definições de passo, ganchos e execução paralela** (itens 1086–1095): Conferi a referência de Gherkin, a referência de API do Cucumber e o repositório do Cucumber para cenários, definições de passo, ganchos, etiquetas e paralelismo antes de redigir as dez notas.
- **Selenium WebDriver — localizadores, esperas, objetos de página e grade** (itens 1096–1105): Conferi a documentação de esperas, o guia de objetos de página, a documentação da grade e o repositório oficial do Selenium para localizadores, ações e execução distribuída antes de redigir as dez notas.
- **Appium — capacidades, drivers, seletores e sessões móveis paralelas** (itens 1106–1115): Conferi a documentação geral do Appium, o repositório oficial e a documentação do driver de automação Android para capacidades, seletores, sessões paralelas e contexto antes de redigir as dez notas.
- **WireMock — stubs, correspondência de requisições, cenários e verificação** (itens 1116–1125): Conferi a documentação de stubs, a página de comportamento com estado, o guia de gravação e reprodução e o repositório oficial do WireMock para correspondência, respostas, cenários e verificação antes de redigir as dez notas.
- **Pact — contratos entre consumidor e provedor, correspondência e broker** (itens 1126–1135): Conferi a explicação de funcionamento, a documentação de verificação do provedor, a referência do broker com a consulta de autorização e o repositório do Pact para contratos, correspondência e fluxo de publicação antes de redigir as dez notas.
- **Testify — asserções, suítes, dublês e testes HTTP em Go** (itens 1136–1145): Conferi a documentação das bibliotecas de asserção, dublê, suíte, do repositório oficial e dos pacotes publicados do testify para asserções fatais, dublês, suítes e testes HTTP antes de redigir as dez notas.
- **RSpec — exemplos, expectativas, dublês, ganchos e exemplos compartilhados** (itens 1146–1156): Conferi a documentação de exemplos compartilhados, a referência de configuração do núcleo, a documentação de dublês e o repositório do RSpec para matchers, ganchos e organização antes de redigir as dez notas.

Cada nota mantém ressalvas e pelo menos duas URLs oficiais específicas; revisão factual por IA não é garantia de ausência de erro.

## Contagens reconciliadas

- Lote `software-testes-2000-0001`: **1156/2.000 (57,80%)**; 9 aprovações humanas + 1147 revisões factuais por IA; **844 notas materiais restantes**; estado permanece `in_progress`.
- Total global: **1196/1.000.000 (0,1196%)**; 49 aprovações humanas + 1147 revisões factuais por IA. Os 100 arquivos legados com pendências continuam excluídos.
- O MOC, o manifesto, a fila, os relatórios de qualidade e os resumos ativos foram sincronizados. A meta global continua **1.000.000**, sem reativar a meta anterior de 2.000.000.
- Nenhuma tranche posterior foi iniciada; salvar este estado no GitHub antes de avançar.
