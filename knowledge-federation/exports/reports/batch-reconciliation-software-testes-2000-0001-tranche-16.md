# Reconciliação — `software-testes-2000-0001`, tranche 16

Data: 2026-10-03

Resultado: **106 notas contabilizadas após gate e revisão factual por IA**. Esta reconciliação não representa aprovação humana.

## Escopo da tranche

- IDs: **950–1055**, 106 arquivos em dez grupos temáticos (dez ou onze notas cada); conteúdo substantivo de **190–238 palavras por nota**, conforme o construtor.
- Fontes e dados reproduzíveis: [`_build_tranche16.py`](../../scripts/_build_tranche16.py) e [`_tranche16_data/`](../../scripts/_tranche16_data/).
- Relatório de revisão: [`ai-review-software-testes-2000-0001-tranche-16.md`](ai-review-software-testes-2000-0001-tranche-16.md). Registra 106 decisões factuais por IA, sem alterar as 49 aprovações humanas históricas.
- Grupos: Detox, Artillery, Vegeta, JMH, coverage.py, nyc/Istanbul, Lighthouse CI, Pa11y, Prism e Hurl.

## Auditorias e resultados

| Verificação | Resultado |
|---|---|
| Gate do lote de testes de software | **1055/1055 aprovadas**; 0 pendências. A auditoria específica incluiu as 949 notas anteriores e as 106 novas. |
| Gate das notas novas | **106/106 aprovadas**; mínimo de 190 palavras e duas fontes HTTPS específicas por nota. |
| Revisão factual do lote | **9 humanas históricas + 1046 por IA**; separação preservada. As novas 106 foram revisadas por IA. |
| Testes automatizados do repositório | **12 aprovados** (`python -m unittest discover -s knowledge-federation/tests -v`). |
| Auditoria global por arquivos e ledger | **1195 Markdown ativos**, 1095 válidos (49 humanas + 1046 IA) e 100 legados com pendências, excluídos da contagem. O ledger mantém 1.000.000 registros-template e não contribui para notas válidas. |
| IDs, títulos, slugs e conteúdo duplicado | 106 IDs únicos no intervalo; sem colisão de slug/título com o inventário ativo; nenhum corpo idêntico; similaridade Jaccard máxima de shingles de cinco palavras de **0,0147** contra notas anteriores e **0,0410** dentro da tranche. |
| Frases substantivas repetidas | Nenhuma repetição entre as notas 950–1055, nem entre uma delas e as notas anteriores comparadas. |
| Links locais | Os wikilinks das novas notas foram resolvidos pelo gate; **2540 links relativos** dos documentos atualizados foram verificados, sem alvo ausente. |

Relatórios reproduzíveis: [qualidade do lote](note-quality-software-testes-2000-0001.md), [qualidade global](note-quality-audit.md) e [auditoria rápida do inventário](global-audit-fast.md). A auditoria rápida mostra zeros do SQLite local vazio; isso **não** substitui a contagem editorial por arquivos acima.

## Conferência de fontes e escopo factual

As afirmações foram comparadas às páginas oficiais atuais indicadas nas próprias notas:

- **Detox — sincronização, seletores, lançamento, esperas, artefatos e configuração** (itens 950–960): Conferi o guia de primeiros passos, o guia de configuração de projeto e o repositório oficial do Detox para sincronização, seletores, lançamento, esperas e artefatos antes de redigir as onze notas.
- **Artillery — fases, cenários, capturas, limites e relatórios** (itens 961–971): Conferi o guia do primeiro teste, o repositório oficial, a referência de mecanismos e a extensão de verificação para fases, cenários, capturas, limites e relatórios antes de redigir as onze notas.
- **Vegeta — ataque de taxa constante, relatórios, gráficos e biblioteca** (itens 972–981): Conferi o manual de uso do repositório oficial e a referência da biblioteca para os subcomandos de ataque, relatório, gráfico, codificação e opções de conexão antes de redigir as dez notas.
- **JMH — anotações, modos, aquecimento, estado, parâmetros e perfiladores** (itens 982–991): Conferi o repositório oficial, a página do projeto no OpenJDK e os exemplos de amostra para anotações, modos, aquecimento, estado, parâmetros e consumo de resultados antes de redigir as dez notas.
- **coverage.py — execução, ramos, configuração, exclusões e relatórios** (itens 992–1001): Conferi a documentação oficial de linha de comando, configuração e cobertura de ramos para execução, exclusões, dados paralelos, limites e formatos de relatório antes de redigir as dez notas.
- **nyc e Istanbul — instrumentação, filtros, limites e consolidação** (itens 1002–1012): Conferi o repositório do nyc, o repositório do Istanbul e o pacote publicado para instrumentação, filtros, relatórios, limites e consolidação de dados antes de redigir as onze notas.
- **Lighthouse CI — coleta, asserções, orçamentos e publicação** (itens 1013–1022): Conferi a página de configuração do Lighthouse CI e o repositório oficial para coleta, número de execuções, asserções, orçamentos e publicação antes de redigir as dez notas.
- **Pa11y — padrões, motores, ações, limites e automação** (itens 1023–1033): Conferi o repositório do Pa11y e o do Pa11y CI, com os guias de uso em integração contínua, para padrões, motores, ações, limites e relatórios antes de redigir as onze notas.
- **Prism — simulação, negociação, validação e uso programático** (itens 1034–1044): Conferi a documentação oficial de simulação HTTP e de linha de comando, além do repositório do projeto, para modos de simulação, cabeçalhos de negociação, validação e uso programático antes de redigir as onze notas.
- **Hurl — arquivos, capturas, asserções e execução em lote** (itens 1045–1055): Conferi a documentação oficial do formato de arquivo, das asserções, das capturas e do manual de linha de comando, além do repositório do projeto, antes de redigir as onze notas.

Cada nota mantém ressalvas e pelo menos duas URLs oficiais específicas; revisão factual por IA não é garantia de ausência de erro.

## Contagens reconciliadas

- Lote `software-testes-2000-0001`: **1055/2.000 (52,75%)**; 9 aprovações humanas + 1046 revisões factuais por IA; **945 notas materiais restantes**; estado permanece `in_progress`.
- Total global: **1095/1.000.000 (0,1095%)**; 49 aprovações humanas + 1046 revisões factuais por IA. Os 100 arquivos legados com pendências continuam excluídos.
- O MOC, o manifesto, a fila, os relatórios de qualidade e os resumos ativos foram sincronizados. A meta global continua **1.000.000**, sem reativar a meta anterior de 2.000.000.
- Nenhuma tranche posterior foi iniciada; salvar este estado no GitHub antes de avançar.
