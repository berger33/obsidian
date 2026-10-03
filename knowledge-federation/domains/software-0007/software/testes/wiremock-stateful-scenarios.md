---
id: software.testes.tranche17.001119
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
fontes: ["https://wiremock.org/docs/stateful-behaviour/", "https://wiremock.org/docs/stubbing/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# WireMock: simular fluxos com estado

## Em uma frase
Um cenário é uma máquina de estados que começa em um estado inicial e muda conforme as chamadas, permitindo representar sequências.

## Por que importa
Operações que dependem de estado acumulado não podem ser representadas por respostas independentes, e o cenário reproduz a progressão.

## Como funciona
Nomeie o cenário, declare o estado exigido por cada stub e o próximo estado após a chamada que provoca a transição.

## Exemplo
Uma lista de tarefas pode responder vazia no início, aceitar um item e passar a devolvê-lo nas consultas seguintes.

## Limites e trade-offs
Cenários compartilhados entre testes mantêm estado residual, e reiniciar o servidor entre casos evita interferência.

## Como verificar
Consulte a rota de administração de cenários, execute as três chamadas em ordem e confirme as transições de estado registradas.

## Conexões
- [[wiremock-response-templating]] — Veja também: WireMock: variar respostas com modelos.
- [[wiremock-priorities]] — Veja também: WireMock: resolver sobreposição com prioridades.

## Fontes
- [WireMock — Stateful behaviour](https://wiremock.org/docs/stateful-behaviour/) — cenários como máquina de estados e consulta de estado; consultado em 2026-10-03.
- [WireMock — Stubbing](https://wiremock.org/docs/stubbing/) — mapeamentos de stub, respostas predefinidas e prioridades; consultado em 2026-10-03.
