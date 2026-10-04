---
id: software.testes.tranche11.000464
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
fontes: ["https://wiremock.org/docs/stateful-behaviour/", "https://wiremock.org/docs/stubbing/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# WireMock: modelar fluxo stateful com cenário explícito

## Em uma frase
Um cenário WireMock representa uma máquina de estados simples; mappings podem exigir estado e mudar o estado após uma request.

## Por que importa
Mock sem estado devolve sempre a mesma resposta e não reproduz um fluxo em que uma ação altera o recurso simulado.

## Como funciona
Declare o estado inicial, configure transição em uma operação e responda de maneira diferente a uma leitura posterior.

## Exemplo
GET lista inicialmente sem item; POST adiciona item e muda estado; próximo GET devolve a lista atualizada.

## Limites e trade-offs
Cenários não modelam toda a regra de negócio e estado pode vazar quando o servidor é reutilizado sem reset.

## Como verificar
Execute sequência completa e depois resetScenario; repita o fluxo e confirme retorno ao estado inicial.

## Conexões
- [[wiremock-priority-sobreposicao-stubs]] — Veja também: WireMock: definir prioridade quando mappings se sobrepõem.
- [[wiremock-verificacao-de-request-journal]] — Veja também: WireMock: verificar request recebida sem confundir com resposta.

## Fontes
- [WireMock — Stateful Behaviour](https://wiremock.org/docs/stateful-behaviour/) — cenários como máquinas de estado, estados iniciais e reset; consultado em 2026-10-02.
- [WireMock — Stubbing](https://wiremock.org/docs/stubbing/) — mapeamentos de request/response, prioridade, defaults, reset e persistência de stubs; consultado em 2026-10-02.
