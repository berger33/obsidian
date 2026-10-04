---
id: software.testes.tranche13.000665
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-13.md"
fontes: ["https://jasmine.github.io/api/7.0/Spy", "https://jasmine.github.io/api/7.0/matchers"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Jasmine: inspecionar histórico de chamadas de spy

## Em uma frase
O objeto Spy expõe histórico de chamadas para examinar quantidade, argumentos e ordem observada.

## Por que importa
Histórico detalhado ajuda a validar a colaboração relevante sem substituir uma asserção sobre o resultado visível ao usuário.

## Como funciona
Use os métodos do rastreador de chamadas para consultar chamadas específicas, limpe ou crie novo spy conforme o escopo e evite exigir chamadas internas sem valor contratual.

## Exemplo
Um teste pode verificar que um cliente enviou o identificador do pedido uma vez, além de conferir que a tela recebeu o estado final esperado.

## Limites e trade-offs
A assertion de chamadas não prova que o serviço remoto processou a solicitação; spies registram interação local no processo de teste.

## Como verificar
Introduza uma chamada extra e uma ordem alterada para confirmar que o spec detecta apenas a diferença prevista no contrato escolhido.

## Conexões
- [[jasmine-spy-through-vs-stub]] — Veja também: Jasmine: distinguir spy que observa de spy com resposta.
- [[jasmine-beforeall-state-boundary]] — Veja também: Jasmine: limitar estado compartilhado em beforeAll.

## Fontes
- [Jasmine 7 — Spy](https://jasmine.github.io/api/7.0/Spy) — spy calls and call-tracking API; consultado em 2026-10-02.
- [Jasmine 7 — Matchers](https://jasmine.github.io/api/7.0/matchers) — matcher methods and matcher behavior; consultado em 2026-10-02.
