---
id: software.testes.tranche17.001117
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
fontes: ["https://wiremock.org/docs/stubbing/", "https://wiremock.org/docs/request-matching/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# WireMock: corresponder por rota, método e corpo

## Em uma frase
Os critérios podem exigir caminho exato ou por padrão, método, cabeçalhos e condições sobre o corpo em formatos estruturados.

## Por que importa
Uma correspondência precisa garante que o teste falhe quando o cliente envia a requisição errada, em vez de aceitar qualquer chamada.

## Como funciona
Combine critérios suficientes para distinguir os casos, use padrões quando houver identificador na rota e evite condições sobre campos voláteis.

## Exemplo
A rota de detalhe pode corresponder a um padrão numérico no caminho e ao método de leitura, diferenciando-a da rota de coleção.

## Limites e trade-offs
Correspondências amplas capturam chamadas de outros testes, e condições rígidas demais quebram com campos gerados pelo cliente.

## Como verificar
Envie uma requisição com método diferente do declarado e confirme que o stub não corresponde e a chamada é registrada como não atendida.

## Conexões
- [[wiremock-stub-mapping]] — Veja também: WireMock: definir um stub de resposta.
- [[wiremock-response-templating]] — Veja também: WireMock: variar respostas com modelos.

## Fontes
- [WireMock — Stubbing](https://wiremock.org/docs/stubbing/) — mapeamentos de stub, respostas predefinidas e prioridades; consultado em 2026-10-03.
- [WireMock — Request matching](https://wiremock.org/docs/request-matching/) — critérios sobre rota, método, cabeçalhos e corpo; consultado em 2026-10-03.
