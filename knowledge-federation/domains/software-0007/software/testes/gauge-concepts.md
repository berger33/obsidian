---
id: software.testes.tranche20.001361
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-20.md"
fontes: ["https://docs.gauge.org/writing-specifications", "https://docs.gauge.org/overview"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Gauge: agrupar passos em conceitos

## Em uma frase
Conceitos combinam uma sequência de passos em uma unidade nomeada, declarada em arquivo próprio e usada como qualquer outro passo.

## Por que importa
O agrupamento expressa uma intenção de negócio de alto nível e reduz a repetição da mesma sequência em várias especificações.

## Como funciona
Extraia conceito quando a mesma sequência aparecer em três cenários, nomeie-o pela intenção e mantenha o arquivo junto das especificações.

## Exemplo
O conceito de autenticação pode reunir navegação, preenchimento e envio, sendo chamado em qualquer cenário que exija sessão iniciada.

## Limites e trade-offs
Conceitos que escondem verificações importantes dificultam a leitura do que é testado, e aninhamento profundo torna a falha difícil de localizar.

## Como verificar
Expanda o conceito durante uma execução e confirme que os passos internos aparecem no relatório na ordem declarada.

## Conexões
- [[gauge-steps-implementation]] — Veja também: Gauge: implementar passos no código.
- [[gauge-tags-and-filtering]] — Veja também: Gauge: selecionar execuções por etiquetas.

## Fontes
- [Gauge — Escrever especificações](https://docs.gauge.org/writing-specifications) — sintaxe das especificações, tabelas de dados e conceitos; consultado em 2026-10-03.
- [Gauge — Visão geral](https://docs.gauge.org/overview) — conceitos de especificação, cenário, passo e conceito; consultado em 2026-10-03.
