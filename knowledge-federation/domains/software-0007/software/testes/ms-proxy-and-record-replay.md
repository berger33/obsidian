---
id: software.testes.tranche20.001383
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
fontes: ["https://www.mock-server.com/proxy/getting_started.html", "https://github.com/mock-server/mockserver"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MockServer: gravar tráfego com proxy

## Em uma frase
No modo proxy, o pedido é encaminhado ao serviço real e o par pedido e resposta fica registrado, podendo ser recuperado como expectativa reutilizável.

## Por que importa
A gravação produz dados realistas sem depender do serviço externo em todas as execuções, reduzindo instabilidade e tempo.

## Como funciona
Aponte o proxy para o serviço real, deduplique e generalize valores variáveis ao recuperar as expectativas gravadas, e revise o resultado.

## Exemplo
Um fluxo de consulta a serviço de terceiro pode ser gravado uma vez e reutilizado como expectativa nas execuções seguintes.

## Limites e trade-offs
Valores gravados fixos deixam de corresponder a pedidos novos com identificadores diferentes, e gravações antigas deixam de refletir o serviço real.

## Como verificar
Recupere as expectativas gravadas, reenvie o pedido e confirme que a resposta vem do registro e não do serviço externo.

## Conexões
- [[ms-response-verification]] — Veja também: MockServer: verificar respostas registradas.
- [[ms-openapi-contract]] — Veja também: MockServer: usar especificação de contrato.

## Fontes
- [MockServer — Gravar com proxy](https://www.mock-server.com/proxy/getting_started.html) — encaminhamento, gravação e deduplicação de expectativas; consultado em 2026-10-03.
- [MockServer — repositório oficial](https://github.com/mock-server/mockserver) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
