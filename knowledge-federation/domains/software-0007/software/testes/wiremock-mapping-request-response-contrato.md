---
id: software.testes.tranche11.000460
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

# WireMock: parear matcher de request com resposta explícita

## Em uma frase
Um stub WireMock associa condições de request a uma response configurada por código ou arquivo JSON.

## Por que importa
WireMock devolve respostas configuradas para requests correspondentes e mantém evidência de tráfego recebido, permitindo isolar dependências sem substituir assertions do sistema testado. Se o matcher não inclui método ou caminho esperado, um teste pode receber resposta de sucesso para a chamada errada.

## Como funciona
Configure mappings próximos do caso, use matchers que expressem o contrato observado e isole servidor, request journal e cenários entre testes; verifique requests e respostas em vez de testar somente o stub. Defina método e URL, acrescente apenas atributos relevantes ao contrato e configure status, headers e body usados pelo consumidor.

## Exemplo
Um teste do client recebe JSON 200 somente para GET /inventory; POST ou caminho diferente não herda essa resposta.

## Limites e trade-offs
Um mock não prova a compatibilidade com serviço real. Journal e cenários possuem estado, matchers genéricos podem aceitar requests incorretos e extensões como templating exigem configuração explícita. Stub exercita o comportamento do consumidor diante da resposta simulada, não valida o serviço real que produziria o corpo.

## Como verificar
Envie uma request correta e duas variantes inválidas e confirme qual mapping respondeu a cada uma.

## Conexões
- [[wiremock-urlpath-query-param-matching]] — Veja também: WireMock: separar path matching da comparação de query.

## Fontes
- [WireMock — Stubbing](https://wiremock.org/docs/stubbing/) — mapeamentos de request/response, prioridade, defaults, reset e persistência de stubs; consultado em 2026-10-02.
- [WireMock — Request Matching](https://wiremock.org/docs/request-matching/) — matching de URL, método, query, headers, cookies, body, JSON e formulários; consultado em 2026-10-02.
