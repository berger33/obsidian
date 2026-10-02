---
id: software.testes.tranche11.000463
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-11.md"
fontes: ["https://wiremock.org/docs/stubbing/", "https://wiremock.org/docs/request-matching/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# WireMock: definir prioridade quando mappings se sobrepõem

## Em uma frase
Se múltiplos stubs combinam com uma request, a prioridade controla qual resposta é selecionada; números menores indicam prioridade maior.

## Por que importa
Um catch-all pode interceptar rota específica e transformar o erro de roteamento em resposta aparentemente válida.

## Como funciona
Atribua prioridade alta ao caso específico e baixa ao fallback, ou torne os matchers mutuamente exclusivos.

## Exemplo
Um stub para /api/orders/42 vence o fallback de /api/orders/* mesmo quando ambos são elegíveis.

## Limites e trade-offs
A ordem em que mappings são registrados também influencia a seleção quando não se define prioridade; não dependa acidentalmente dela.

## Como verificar
Ative ambos mappings e teste a rota específica, outra rota válida e uma rota inexistente, conferindo status e id do stub.

## Conexões
- [[wiremock-json-body-matcher-estrutura]] — Veja também: WireMock: comparar estrutura JSON sem fixar formatação textual.
- [[wiremock-scenario-maquina-de-estados]] — Veja também: WireMock: modelar fluxo stateful com cenário explícito.

## Fontes
- [WireMock — Stubbing](https://wiremock.org/docs/stubbing/) — mapeamentos de request/response, prioridade, defaults, reset e persistência de stubs; consultado em 2026-10-02.
- [WireMock — Request Matching](https://wiremock.org/docs/request-matching/) — matching de URL, método, query, headers, cookies, body, JSON e formulários; consultado em 2026-10-02.
