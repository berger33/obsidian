---
id: software.testes.tranche16.000966
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-16.md"
fontes: ["https://www.artillery.io/docs/reference/engines/playwright", "https://www.artillery.io/docs/get-started/first-test"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Artillery: medir navegador com mecanismo de browser

## Em uma frase
Além de requisições HTTP, a ferramenta aceita mecanismo que controla navegador real, permitindo medir carregamento completo de páginas sob carga.

## Por que importa
Métricas de navegador incluem renderização, scripts e recursos de terceiros, que uma chamada HTTP isolada não captura.

## Como funciona
Selecione o mecanismo, declare os passos em linguagem de navegador e mantenha o número de usuários compatível com a capacidade do executor.

## Exemplo
Um cenário pode abrir a página inicial, aguardar um elemento visível e registrar o tempo até a interação ficar disponível.

## Limites e trade-offs
Testes de navegador consomem muito mais recursos que requisições HTTP, e o executor usado para gerar carga precisa ser dimensionado para não virar o gargalo da medição.

## Como verificar
Compare o tempo de carregamento com e sem recursos de terceiros bloqueados para confirmar onde está o custo dominante.

## Conexões
- [[artillery-metrics-interpretation]] — Veja também: Artillery: interpretar o resumo de métricas.
- [[artillery-expect-plugin]] — Veja também: Artillery: verificar respostas com asserções.

## Fontes
- [Artillery — Playwright engine](https://www.artillery.io/docs/reference/engines/playwright) — controle de navegador real e coleta de métricas de página sob carga; consultado em 2026-10-03.
- [Artillery — First test](https://www.artillery.io/docs/get-started/first-test) — config, fases, cenários, capturas, métricas e execução de carga; consultado em 2026-10-03.
