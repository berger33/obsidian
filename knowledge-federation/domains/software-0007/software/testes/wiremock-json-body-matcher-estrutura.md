---
id: software.testes.tranche11.000462
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
fontes: ["https://wiremock.org/docs/request-matching/", "https://wiremock.org/docs/verifying/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# WireMock: comparar estrutura JSON sem fixar formatação textual

## Em uma frase
WireMock fornece matchers de corpo JSON que comparam conteúdo estruturado, além de comparação literal ou JSONPath.

## Por que importa
WireMock devolve respostas configuradas para requests correspondentes e mantém evidência de tráfego recebido, permitindo isolar dependências sem substituir assertions do sistema testado. Espaços, ordem de propriedades ou diferenças irrelevantes de formatação não deveriam quebrar um mock quando o contrato exige mesmos valores.

## Como funciona
Configure mappings próximos do caso, use matchers que expressem o contrato observado e isole servidor, request journal e cenários entre testes; verifique requests e respostas em vez de testar somente o stub. Escolha equalToJson ou matcher de JSONPath para os campos pertinentes e configure tolerância a propriedades extras somente quando fizer sentido.

## Exemplo
Um POST com propriedades JSON reordenadas ainda corresponde ao stub, mas um amount diferente não corresponde.

## Limites e trade-offs
Um mock não prova a compatibilidade com serviço real. Journal e cenários possuem estado, matchers genéricos podem aceitar requests incorretos e extensões como templating exigem configuração explícita. Permitir propriedades extras pode esconder campos não esperados; a escolha de strictness deve refletir o objetivo do teste.

## Como verificar
Envie payloads com formatação equivalente e com uma diferença de valor e confirme respostas distintas do mapping.

## Conexões
- [[wiremock-urlpath-query-param-matching]] — Veja também: WireMock: separar path matching da comparação de query.
- [[wiremock-priority-sobreposicao-stubs]] — Veja também: WireMock: definir prioridade quando mappings se sobrepõem.

## Fontes
- [WireMock — Request Matching](https://wiremock.org/docs/request-matching/) — matching de URL, método, query, headers, cookies, body, JSON e formulários; consultado em 2026-10-02.
- [WireMock — Verifying](https://wiremock.org/docs/verifying/) — request journal, verificações, requests não correspondidos e near misses; consultado em 2026-10-02.
