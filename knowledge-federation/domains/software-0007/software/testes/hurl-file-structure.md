---
id: software.testes.tranche16.001045
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
fontes: ["https://hurl.dev/docs/hurl-file.html", "https://github.com/Orange-OpenSource/hurl"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Hurl: descrever requisição e resposta esperada

## Em uma frase
O arquivo descreve uma entrada com a requisição e, opcionalmente, a resposta esperada logo abaixo, incluindo código de status e cabeçalhos.

## Por que importa
Escrever a expectativa junto do pedido torna o arquivo legível como contrato executável e mantém pedido e verificação no mesmo lugar.

## Como funciona
Declare método, endereço e cabeçalhos na requisição, e a linha de status esperada com os cabeçalhos e o corpo previstos na resposta.

## Exemplo
Uma entrada pode pedir a criação de um recurso e declarar que a resposta deve ter código de criação e tipo de conteúdo em formato específico.

## Limites e trade-offs
Código de status amplo aceita qualquer resposta e reduz o valor da verificação; a linha deve expressar o que se espera de fato.

## Como verificar
Compare o arquivo com a resposta obtida em execução contra o serviço para confirmar que cada linha declarada é verificável.

## Conexões
- [[hurl-implicit-assertions]] — Veja também: Hurl: aproveitar asserções implícitas.

## Fontes
- [Hurl — File format](https://hurl.dev/docs/hurl-file.html) — estrutura de entradas, resposta esperada, opções e escopo de sessão; consultado em 2026-10-03.
- [Hurl — repositório oficial](https://github.com/Orange-OpenSource/hurl) — visão geral do projeto, exemplos e documentação complementar; consultado em 2026-10-03.
