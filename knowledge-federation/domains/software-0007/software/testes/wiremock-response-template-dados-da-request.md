---
id: software.testes.tranche11.000469
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
fontes: ["https://wiremock.org/docs/response-templating/", "https://wiremock.org/docs/stubbing/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# WireMock: tornar resposta dinâmica com response templating configurado

## Em uma frase
Response templating pode preencher partes da resposta com valores do contexto da request em vez de manter uma fixture fixa.

## Por que importa
WireMock devolve respostas configuradas para requests correspondentes e mantém evidência de tráfego recebido, permitindo isolar dependências sem substituir assertions do sistema testado. Resposta com id constante pode limitar um fluxo de teste que precisa verificar propagação de dado entre chamada e retorno.

## Como funciona
Configure mappings próximos do caso, use matchers que expressem o contrato observado e isole servidor, request journal e cenários entre testes; verifique requests e respostas em vez de testar somente o stub. Habilite explicitamente a extensão de templating e use apenas variáveis de request necessárias na resposta.

## Exemplo
O stub devolve um echo do request id em JSON e o client comprova que preservou o identificador.

## Limites e trade-offs
Um mock não prova a compatibilidade com serviço real. Journal e cenários possuem estado, matchers genéricos podem aceitar requests incorretos e extensões como templating exigem configuração explícita. Template não substitui validação de saída e pode introduzir risco se refletir conteúdo não confiável sem escape adequado.

## Como verificar
Envie valores simples, caracteres especiais e campos ausentes; confirme encoding, status e que nenhuma variável secreta foi refletida.

## Conexões
- [[wiremock-junit-extension-reset-por-teste]] — Veja também: WireMock: confirmar lifecycle e reset da extensão JUnit.

## Fontes
- [WireMock — Response Templating](https://wiremock.org/docs/response-templating/) — templates de resposta baseados em dados da request; consultado em 2026-10-02.
- [WireMock — Stubbing](https://wiremock.org/docs/stubbing/) — mapeamentos de request/response, prioridade, defaults, reset e persistência de stubs; consultado em 2026-10-02.
