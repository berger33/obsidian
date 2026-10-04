---
id: software.testes.tranche17.001116
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
fontes: ["https://wiremock.org/docs/stubbing/", "https://github.com/wiremock/wiremock"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# WireMock: definir um stub de resposta

## Em uma frase
Um stub associa critérios de correspondência da requisição a uma resposta predefinida, em arquivo, código ou documento estruturado.

## Por que importa
Serviços externos indisponíveis ou caros impedem testes determinísticos, e o stub fixa a resposta para que o comportamento verificado seja o do cliente.

## Como funciona
Declare a rota, o método e a resposta em arquivo versionado, mantendo um stub por comportamento relevante.

## Exemplo
Uma consulta de saldo pode responder com valor fixo para que o teste verifique a formatação e o fluxo de confirmação.

## Limites e trade-offs
Stubs que respondem qualquer coisa escondem divergências de contrato, e arquivos espalhados dificultam saber qual regra está ativa.

## Como verificar
Envie uma requisição para a rota declarada e confirme que a resposta corresponde exatamente ao documento do stub.

## Conexões
- [[wiremock-request-matching]] — Veja também: WireMock: corresponder por rota, método e corpo.

## Fontes
- [WireMock — Stubbing](https://wiremock.org/docs/stubbing/) — mapeamentos de stub, respostas predefinidas e prioridades; consultado em 2026-10-03.
- [WireMock — repositório oficial](https://github.com/wiremock/wiremock) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
