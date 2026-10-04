---
id: software.testes.tranche17.001118
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-17.md"
fontes: ["https://wiremock.org/docs/response-templating/", "https://wiremock.org/docs/stubbing/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# WireMock: variar respostas com modelos

## Em uma frase
A resposta pode usar modelos que leem valores da requisição, geram identificadores e formatam datas no momento da chamada.

## Por que importa
Valores fixos em todos os testes escondem defeitos que aparecem apenas com dados variados, e o modelo produz variação controlada.

## Como funciona
Ative a transformação no stub, referencie campos da requisição com a sintaxe de modelo e gere valores com formato coerente com o contrato.

## Exemplo
Um stub de criação pode devolver identificador gerado e data atual, permitindo que o teste verifique o encadeamento sem conhecer valores de antemão.

## Limites e trade-offs
Modelos mal escritos falham em tempo de execução da resposta e nem sempre produzem erro claro, exigindo teste do próprio stub.

## Como verificar
Requisite a mesma rota duas vezes e verifique que o identificador gerado muda enquanto os campos fixos permanecem iguais.

## Conexões
- [[wiremock-request-matching]] — Veja também: WireMock: corresponder por rota, método e corpo.
- [[wiremock-stateful-scenarios]] — Veja também: WireMock: simular fluxos com estado.

## Fontes
- [WireMock — Response templating](https://wiremock.org/docs/response-templating/) — respostas dinâmicas com modelos e valores da requisição; consultado em 2026-10-03.
- [WireMock — Stubbing](https://wiremock.org/docs/stubbing/) — mapeamentos de stub, respostas predefinidas e prioridades; consultado em 2026-10-03.
