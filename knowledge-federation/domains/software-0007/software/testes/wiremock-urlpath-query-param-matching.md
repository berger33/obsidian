---
id: software.testes.tranche11.000461
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
fontes: ["https://wiremock.org/docs/request-matching/", "https://wiremock.org/docs/stubbing/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# WireMock: separar path matching da comparação de query

## Em uma frase
WireMock permite comparar URL completa ou só o path e declarar query parameters separadamente.

## Por que importa
Comparar URL inteira pode tornar o teste sensível à ordem de parâmetros, apesar de ela não representar a distinção do contrato que se quer verificar.

## Como funciona
Use urlPathEqualTo para a rota e withQueryParam para cada parâmetro cuja presença ou valor seja relevante.

## Exemplo
O stub /search aceita query term=wiremock independentemente da ordem com page=2, e rejeita termo diferente.

## Limites e trade-offs
Regex amplo de URL pode aceitar caminhos não pretendidos; delimite segmentos e valores que importam ao caso.

## Como verificar
Envie as mesmas query parameters em ordens diferentes e confirme igualdade; depois varie um valor contratualmente significativo.

## Conexões
- [[wiremock-mapping-request-response-contrato]] — Veja também: WireMock: parear matcher de request com resposta explícita.
- [[wiremock-json-body-matcher-estrutura]] — Veja também: WireMock: comparar estrutura JSON sem fixar formatação textual.

## Fontes
- [WireMock — Request Matching](https://wiremock.org/docs/request-matching/) — matching de URL, método, query, headers, cookies, body, JSON e formulários; consultado em 2026-10-02.
- [WireMock — Stubbing](https://wiremock.org/docs/stubbing/) — mapeamentos de request/response, prioridade, defaults, reset e persistência de stubs; consultado em 2026-10-02.
