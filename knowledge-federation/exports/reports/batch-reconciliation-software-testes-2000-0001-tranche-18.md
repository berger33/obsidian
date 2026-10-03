# Reconciliação — `software-testes-2000-0001`, tranche 18

Data: 2026-10-03

Resultado: **101 notas contabilizadas após gate e revisão factual por IA**. Esta reconciliação não representa aprovação humana.

## Escopo da tranche

- IDs: **1157–1257**, 101 arquivos em dez grupos temáticos (dez ou onze notas cada); conteúdo substantivo de **166–215 palavras por nota**, conforme o construtor.
- Fontes e dados reproduzíveis: [`_build_tranche18.py`](../../scripts/_build_tranche18.py) e [`_tranche18_data/`](../../scripts/_tranche18_data/).
- Relatório de revisão: [`ai-review-software-testes-2000-0001-tranche-18.md`](ai-review-software-testes-2000-0001-tranche-18.md). Registra 101 decisões factuais por IA, sem alterar as 49 aprovações humanas históricas.
- Grupos: Cypress, WebdriverIO, JUnit 5, GoogleTest, PHPUnit, Ginkgo, axe-core, Semgrep, Trivy e Allure Report.

## Auditorias e resultados

| Verificação | Resultado |
|---|---|
| Gate do lote de testes de software | **1257/1257 aprovadas**; 0 pendências. A auditoria específica incluiu as 1156 notas anteriores e as 101 novas. |
| Gate das notas novas | **101/101 aprovadas**; mínimo de 166 palavras, seções obrigatórias e duas fontes HTTPS específicas por nota. |
| Revisão factual do lote | **9 humanas históricas + 1248 por IA**; separação preservada. As novas 101 foram revisadas por IA. |
| Testes automatizados do repositório | **12 aprovados** (`python -m unittest discover -s knowledge-federation/tests -v`). |
| Auditoria global por arquivos e ledger | **1397 Markdown ativos**, 1297 válidos (49 humanas + 1248 IA) e 100 legados com pendências, excluídos da contagem. O ledger mantém 1.000.000 registros-template e não contribui para notas válidas. |
| IDs, títulos, slugs e conteúdo duplicado | 101 IDs únicos no intervalo; sem colisão de slug/título com o inventário ativo; nenhum corpo idêntico; similaridade Jaccard máxima de shingles de cinco palavras de **0,1624** contra notas anteriores e **0,0814** dentro da tranche. |
| Frases substantivas repetidas | Nenhuma repetição entre as notas 1157–1257, nem entre uma delas e as notas anteriores comparadas. |
| Links locais | Os wikilinks das novas notas foram resolvidos pelo gate; **2988 links relativos** de todos os documentos foram verificados na varredura final, sem alvo ausente após esta reconciliação. |

Relatórios reproduzíveis: [qualidade do lote](note-quality-software-testes-2000-0001.md), [qualidade global](note-quality-audit.md) e [auditoria rápida do inventário](global-audit-fast.md). A auditoria rápida mostra zeros do SQLite local vazio; isso **não** substitui a contagem editorial por arquivos acima.

## Conferência de fontes e escopo factual

As afirmações foram comparadas às páginas oficiais atuais indicadas nas próprias notas:

- **Cypress — execução no navegador, retry-ability, interceptação e sessão** (itens 1157–1166): Conferi a visão geral, as práticas recomendadas, a referência de API, a interceptação de rede e o cache de sessão no material do Cypress antes de redigir as dez notas.
- **WebdriverIO — seletores, esperas, comandos, serviços e paralelismo** (itens 1167–1176): Conferi a documentação de seletores, a API de comandos de elemento, a espera por exibição e a configuração do WebdriverIO antes de redigir as dez notas.
- **JUnit 5 — anotações, ciclo de vida, parametrização, extensões e paralelismo** (itens 1177–1186): Conferi o guia do usuário do JUnit 5 para anotações, asserções, testes dinâmicos, injeção de dependência e execução paralela antes de redigir as dez notas.
- **GoogleTest — asserções, fixtures, parametrização e testes de morte** (itens 1187–1196): Conferi o guia básico e o guia avançado do GoogleTest para macros, comparações, filtros e asserções de morte antes de redigir as dez notas.
- **PHPUnit — atributos, fixtures, dublês e cobertura** (itens 1197–1206): Conferi as páginas de escrita de testes, atributos, fixtures, dublês e cobertura do PHPUnit antes de redigir as dez notas.
- **Ginkgo — contêineres BDD, preparação, paralelismo e etiquetas** (itens 1207–1216): Conferi o material do Ginkgo, o pacote publicado, a documentação do Gomega e o repositório oficial para nós, decoradores e relatórios antes de redigir as dez notas.
- **axe-core — regras, etiquetas, impacto e integração** (itens 1217–1227): Conferi a API JavaScript, a descrição das regras, a integração com navegador e o repositório do axe-core para opções, etiquetas e formatos de resultado antes de redigir as onze notas.
- **Semgrep — regras, operadores, propagação e correções** (itens 1228–1237): Conferi a documentação de escrita de regras, a correção definida pela regra, a integração contínua e o repositório do Semgrep antes de redigir as dez notas.
- **Trivy — imagens, configurações, segredos e inventário** (itens 1238–1247): Conferi a documentação de verificação de vulnerabilidades, configurações, segredos, inventário e formatos de saída do Trivy antes de redigir as dez notas.
- **Allure Report — resultados, passos, anexos, categorias e histórico** (itens 1248–1257): Conferi a documentação de resultados, passos, categorias e histórico do Allure antes de redigir as dez notas.

Cada nota mantém ressalvas e pelo menos duas URLs oficiais específicas; revisão factual por IA não é garantia de ausência de erro.

## Contagens reconciliadas

- Lote `software-testes-2000-0001`: **1257/2.000 (62,85%)**; 9 aprovações humanas + 1248 revisões factuais por IA; **743 notas materiais restantes**; estado permanece `in_progress`.
- Total global: **1297/1.000.000 (0,1297%)**; 49 aprovações humanas + 1248 revisões factuais por IA. Os 100 arquivos legados com pendências continuam excluídos.
- O MOC, o manifesto, a fila, os relatórios de qualidade e os resumos ativos foram sincronizados. A meta global continua **1.000.000**, sem reativar a meta anterior de 2.000.000.
- Nenhuma tranche posterior foi iniciada; salvar este estado no GitHub antes de avançar.
