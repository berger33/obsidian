---
id: software.testes.tranche23.001738
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-23.md"
fontes: ["https://hyperfoil.io/docs/getting-started/quickstart1/", "https://hyperfoil.io/", "https://hyperfoil.io/docs/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# O stats por dentro: percentis, classes de status e os contadores de erro

## Em uma frase
O output do comando stats no Quickstart 1 oficial é uma tabela com cabeçalho denso: PHASE, METRIC, REQUESTS, MEAN, p50, p90, p99, p99.9, p99.99, colunas de contagem por classe de resposta (2xx, 3xx, 4xx, 5xx) e os quatro medidores de falha de infraestrutura do lado do driver: CACHE, TIMEOUTS, ERRORS e BLOCKED — com o rodapé Total stats from run agregando os agents.

## Por que importa
O detalhe que separa benchmark profissional de "curl em loop" é o último grupo: um teste de carga que engole timeouts e requisições bloqueadas no próprio driver distorce os percentis; aqui eles têm coluna própria e aparecem no run.

## Como funciona
A doc também orienta o próximo passo ergonômico depois do stats: a seção "editing with schema" dos how-tos como leitura para autores de benchmark, enquanto no início "any editor with YAML syntax highlighting will do the job".

## Exemplo
Rode um benchmark curto contra um endpoint lento o bastante para gerar BLOCKED ou TIMEOUTS e confira que as colunas saem de zero antes de qualquer 5xx — o stats do driver primeiro, o do servidor depois.

## Limites e trade-offs
O exemplo do quickstart é um único request, então a tabela é trivial — ler percentis de uma amostra de um não tem significado estatístico; a estrutura das colunas é o artefato didático ali, não o resultado.

## Como verificar
Abra o bloco de saída do passo 4 do Quickstart 1 e confirme o cabeçalho da tabela completo e a frase que chama as estatísticas do exemplo de moot.

## Conexões
- [[hyperfoil-first-run]] — Veja também: Do zero ao primeiro run: download, start-local, upload, run, stats.
- [[hyperfoil-extensions-api]] — Veja também: Fora do YAML: REST API OpenAPI, steps customizados em JVM e guia de migração.

## Fontes
- [Hyperfoil — Quickstart 1: First benchmark](https://hyperfoil.io/docs/getting-started/quickstart1/) — download, start-local, upload, run e stats; consultado em 2026-10-03.
- [Hyperfoil — página inicial oficial](https://hyperfoil.io/) — definição e destaques distributed, accurate, versatile, low-allocation; consultado em 2026-10-03.
- [Hyperfoil — índice da documentação](https://hyperfoil.io/docs/) — nove seções: overview, quickstarts, user guide, API REST, extensions; consultado em 2026-10-03.
