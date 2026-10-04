# Reconciliação — `software-testes-2000-0001`, tranche 15

Data: 2026-10-02

Resultado: **100 notas contabilizadas após gate e revisão factual por IA**. Esta reconciliação não representa aprovação humana.

## Escopo da tranche

- IDs: **850–949**, 100 arquivos em dez grupos de dez; conteúdo substantivo de **184–237 palavras por nota**, conforme o construtor.
- Fontes e dados reproduzíveis: [`_build_tranche15.py`](../../scripts/_build_tranche15.py) e [`_tranche15_data/`](../../scripts/_tranche15_data/).
- Relatório de revisão: [`ai-review-software-testes-2000-0001-tranche-15.md`](ai-review-software-testes-2000-0001-tranche-15.md). Registra 100 decisões factuais por IA, sem alterar as 49 aprovações humanas históricas.
- Grupos: Puppeteer, Mock Service Worker, Supertest, Minitest, JaCoCo, Maestro, Karate, Swift Testing, MSTest e cargo-nextest.

## Auditorias e resultados

| Verificação | Resultado |
|---|---|
| Gate do lote de testes de software | **949/949 aprovadas**; 0 pendências. A auditoria específica incluiu as 849 notas anteriores e as 100 novas. |
| Gate das notas novas | **100/100 aprovadas**; mínimo de 184 palavras e duas fontes HTTPS específicas por nota. |
| Revisão factual do lote | **9 humanas históricas + 940 por IA**; separação preservada. As novas 100 foram revisadas por IA. |
| Testes automatizados do repositório | **12 aprovados** (`python -m unittest discover -s knowledge-federation/tests -v`). |
| Auditoria global por arquivos e ledger | **1089 Markdown ativos**, 989 válidos (49 humanas + 940 IA) e 100 legados com pendências, excluídos da contagem. O ledger mantém 1.000.000 registros-template e não contribui para notas válidas. |
| IDs, títulos, slugs e conteúdo duplicado | 100 IDs únicos no intervalo; sem colisão de slug/título com o inventário ativo; nenhum corpo idêntico; similaridade Jaccard máxima de shingles de cinco palavras de **0,0098** contra notas anteriores e **0,1461** dentro da tranche. |
| Frases substantivas repetidas | Nenhuma repetição entre as notas 850–949, nem entre uma delas e as notas anteriores comparadas. |
| Links locais | Os wikilinks das novas notas foram resolvidos pelo gate; **2058 links relativos** dos documentos atualizados foram verificados, sem alvo ausente. |

Relatórios reproduzíveis: [qualidade do lote](note-quality-software-testes-2000-0001.md), [qualidade global](note-quality-audit.md) e [auditoria rápida do inventário](global-audit-fast.md). A auditoria rápida mostra zeros do SQLite local vazio; isso **não** substitui a contagem editorial por arquivos acima.

## Conferência de fontes e escopo factual

As afirmações foram comparadas às páginas oficiais atuais indicadas nas próprias notas:

- **Puppeteer — locators, avaliação, rede, protocolos e evidências** (itens 850–859): Conferi a API de Page, o guia de locators com espera automática, o guia de interceptação de rede, a página de suporte a WebDriver BiDi e as opções de lançamento do Puppeteer antes de redigir as dez notas.
- **Mock Service Worker 2 — handlers, respostas, ciclo de vida e padrões de rede** (itens 860–869): Conferi a API de setupServer, o guia de interceptação, a página de tratamento de requisições, a documentação de comportamentos padrão e a API de HttpResponse do MSW 2 antes de redigir as dez notas.
- **Supertest — requisições HTTP, agentes, asserções e ciclo do servidor** (itens 870–879): Conferi o README e o pacote do Supertest, a documentação do Superagent, o guia de testes do Express e o executor de testes nativo do Node.js antes de redigir as dez notas.
- **Minitest — asserções, spec, mocks, ciclo de vida e paralelização** (itens 880–889): Conferi a documentação de Assertions, Spec, Mock e Test do Minitest 6, além do README do projeto, para asserções, DSL, dublês e execução paralela antes de redigir as dez notas.
- **JaCoCo — agente, contadores, relatórios, verificação e instrumentação offline** (itens 890–899): Conferi a documentação do agente Java, a definição dos contadores, o goal de verificação, o goal de relatório e a página de instrumentação offline do JaCoCo antes de redigir as dez notas.
- **Maestro — fluxos YAML, comandos, tags, reuso e evidências** (itens 900–909): Conferi a referência de comandos, o comando runFlow, a página de descoberta e tags, a referência da CLI e o guia de instalação do Maestro antes de redigir as dez notas.
- **Karate — feature files, asserções, configuração, paralelismo e mocks** (itens 910–919): Conferi a documentação principal do Karate e as seções de paralelismo, configuração, testes orientados a dados e servidor mock antes de redigir as dez notas.
- **Swift Testing — macros, suítes, traits, parametrização e migração** (itens 920–929): Conferi a documentação de Swift Testing da Apple, as páginas de testes parametrizados, tags e migração do XCTest, além da sessão introdutória da WWDC24 antes de redigir as dez notas.
- **MSTest — estrutura, dados, ciclo de vida, paralelização e configuração** (itens 930–939): Conferi a documentação de escrita de testes, o ciclo de vida, a configuração de paralelização e retries, a API de asserções e o guia de testes orientados a dados do MSTest antes de redigir as dez notas.
- **cargo-nextest — isolamento, perfis, retries, partições e relatórios** (itens 940–949): Conferi a documentação principal do nextest, as páginas de configuração, execução, particionamento e relatório JUnit para confirmar processos por teste, perfis, retries e limites antes de redigir as dez notas.

Cada nota mantém ressalvas e pelo menos duas URLs oficiais específicas; revisão factual por IA não é garantia de ausência de erro.

## Contagens reconciliadas

- Lote `software-testes-2000-0001`: **949/2.000 (47,45%)**; 9 aprovações humanas + 940 revisões factuais por IA; **1.051 notas materiais restantes**; estado permanece `in_progress`.
- Total global: **989/1.000.000 (0,0989%)**; 49 aprovações humanas + 940 revisões factuais por IA. Os 100 arquivos legados com pendências continuam excluídos.
- O MOC, o manifesto, a fila, os relatórios de qualidade e os resumos ativos foram sincronizados. A meta global continua **1.000.000**, sem reativar a meta anterior de 2.000.000.
- Nenhuma tranche posterior foi iniciada; salvar este estado no GitHub antes de avançar.
