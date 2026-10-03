# Reconciliação — `software-testes-2000-0001`, tranche 19

Data: 2026-10-03

Resultado: **101 notas contabilizadas após gate e revisão factual por IA**. Esta reconciliação não representa aprovação humana.

## Escopo da tranche

- IDs: **1258–1358**, 101 arquivos em dez grupos temáticos (dez ou onze notas cada); conteúdo substantivo de **169–209 palavras por nota**, conforme o construtor.
- Fontes e dados reproduzíveis: [`_build_tranche19.py`](../../scripts/_build_tranche19.py) e [`_tranche19_data/`](../../scripts/_tranche19_data/).
- Relatório de revisão: [`ai-review-software-testes-2000-0001-tranche-19.md`](ai-review-software-testes-2000-0001-tranche-19.md). Registra 101 decisões factuais por IA, sem alterar as 49 aprovações humanas históricas.
- Grupos: Catch2, TestCafe, Mountebank, LocalStack, Terratest, Checkov, BackstopJS, ReportPortal, ArchUnit e Insta.

## Auditorias e resultados

| Verificação | Resultado |
|---|---|
| Gate do lote de testes de software | **1358/1358 aprovadas**; 0 pendências. A auditoria específica incluiu as 1257 notas anteriores e as 101 novas. |
| Gate das notas novas | **101/101 aprovadas**; mínimo de 169 palavras, seções obrigatórias e duas fontes HTTPS específicas por nota. |
| Revisão factual do lote | **9 humanas históricas + 1349 por IA**; separação preservada. As novas 101 foram revisadas por IA. |
| Testes automatizados do repositório | **12 aprovados** (`python -m unittest discover -s knowledge-federation/tests -v`). |
| Auditoria global por arquivos e ledger | **1498 Markdown ativos**, 1398 válidos (49 humanas + 1349 IA) e 100 legados com pendências, excluídos da contagem. O ledger mantém 1.000.000 registros-template e não contribui para notas válidas. |
| IDs, títulos, slugs e conteúdo duplicado | 101 IDs únicos no intervalo; sem colisão de slug/título com o inventário ativo; nenhum corpo idêntico; similaridade Jaccard máxima de shingles de cinco palavras de **0,1129** contra notas anteriores e **0,0242** dentro da tranche. |
| Frases substantivas repetidas | Nenhuma repetição entre as notas 1258–1358, nem entre uma delas e as notas anteriores comparadas. |
| Links locais | Os wikilinks das novas notas foram resolvidos pelo gate; **3201 links relativos** de todos os documentos foram verificados na varredura final, sem alvo ausente após esta reconciliação. |

Relatórios reproduzíveis: [qualidade do lote](note-quality-software-testes-2000-0001.md), [qualidade global](note-quality-audit.md) e [auditoria rápida do inventário](global-audit-fast.md). A auditoria rápida mostra zeros do SQLite local vazio; isso **não** substitui a contagem editorial por arquivos acima.

## Conferência de fontes e escopo factual

As afirmações foram comparadas às páginas oficiais atuais indicadas nas próprias notas:

- **Catch2 — casos, seções, asserções, geradores e relatórios** (itens 1258–1267): Conferi o guia inicial, a referência de asserções, as seções, os geradores, a linha de comando e o sistema de relatórios do Catch2 antes de redigir as dez notas.
- **TestCafe — fixtures, seletores, ações, asserções e papéis** (itens 1268–1277): Conferi a documentação de seletores, as ações de teste, os papéis de autenticação, o repositório oficial e os exemplos do TestCafe antes de redigir as dez notas.
- **Mountebank — impostores, stubs, predicados, proxies e comportamento** (itens 1278–1287): Conferi a visão geral da API, os predicados, os stubs, os proxies, os comportamentos e o repositório oficial do Mountebank antes de redigir as dez notas.
- **LocalStack — emulação de nuvem, ganchos de inicialização e testes** (itens 1288–1297): Conferi a documentação de ganchos de inicialização, o guia com Docker, o tutorial com Terraform e Testcontainers e o repositório oficial do LocalStack antes de redigir as dez notas.
- **Terratest — testes de infraestrutura, destruição, repetição e estágios** (itens 1298–1307): Conferi a documentação do módulo de infraestrutura, os módulos auxiliares publicados e o repositório oficial do Terratest antes de redigir as dez notas.
- **Checkov — políticas como código, supressões, linha de base e esteira** (itens 1308–1317): Conferi o repositório oficial, o guia de uso, a ação publicada e as árvores de verificações de infraestrutura, Kubernetes e segredos do Checkov antes de redigir as dez notas.
- **BackstopJS — regressão visual, cenários, seletores e aprovação** (itens 1318–1327): Conferi o guia do projeto, as propriedades de cenário, os exemplos oficiais e a página de demonstração do BackstopJS antes de redigir as dez notas.
- **ReportPortal — lançamentos, itens, atributos, histórico e análise** (itens 1328–1337): Conferi a documentação de execuções, o guia de atributos, o guia de integração de framework, o guia de desenvolvedores e o repositório oficial do ReportPortal antes de redigir as dez notas.
- **ArchUnit — regras de arquitetura, camadas, ciclos e congelamento** (itens 1338–1347): Conferi o guia do usuário, a documentação de API publicada, os exemplos oficiais e o repositório do ArchUnit antes de redigir as dez notas.
- **Insta — snapshots, revisão, snapshots embutidos e redação** (itens 1348–1358): Conferi a documentação do pacote, o guia inicial, a página de snapshots embutidos, o registro de pacotes e o repositório oficial do insta antes de redigir as onze notas.

Cada nota mantém ressalvas e pelo menos duas URLs oficiais específicas; revisão factual por IA não é garantia de ausência de erro.

## Contagens reconciliadas

- Lote `software-testes-2000-0001`: **1358/2.000 (67,90%)**; 9 aprovações humanas + 1349 revisões factuais por IA; **642 notas materiais restantes**; estado permanece `in_progress`.
- Total global: **1398/1.000.000 (0,1398%)**; 49 aprovações humanas + 1349 revisões factuais por IA. Os 100 arquivos legados com pendências continuam excluídos.
- O MOC, o manifesto, a fila, os relatórios de qualidade e os resumos ativos foram sincronizados. A meta global continua **1.000.000**, sem reativar a meta anterior de 2.000.000.
- Nenhuma tranche posterior foi iniciada; salvar este estado no GitHub antes de avançar.
