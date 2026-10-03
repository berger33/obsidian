---
id: software.testes.tranche20.001360
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
fontes: ["https://docs.gauge.org/writing-specifications", "https://github.com/getgauge/gauge"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Gauge: implementar passos no código

## Em uma frase
Cada passo da especificação corresponde a um método anotado no código do projeto, com parâmetros extraídos do texto do próprio passo.

## Por que importa
A separação entre texto e implementação permite revisar a intenção do teste sem ler código e reaproveitar passos entre especificações.

## Como funciona
Mantenha implementações curtas delegando a páginas e clientes, use trechos entre sinais para capturar valores e nomeie métodos pelo efeito no domínio.

## Exemplo
Um passo pode receber o nome do produto como parâmetro e delegar a busca ao objeto de página correspondente.

## Limites e trade-offs
Passos com lógica extensa viram software sem teste próprio, e frases ambíguas fazem duas implementações disputarem a mesma linha.

## Como verificar
Execute a especificação e confirme que a mensagem de passo ausente sugere exatamente a assinatura que falta implementar.

## Conexões
- [[gauge-specifications]] — Veja também: Gauge: escrever especificações em markdown.
- [[gauge-concepts]] — Veja também: Gauge: agrupar passos em conceitos.

## Fontes
- [Gauge — Escrever especificações](https://docs.gauge.org/writing-specifications) — sintaxe das especificações, tabelas de dados e conceitos; consultado em 2026-10-03.
- [Gauge — repositório oficial](https://github.com/getgauge/gauge) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
