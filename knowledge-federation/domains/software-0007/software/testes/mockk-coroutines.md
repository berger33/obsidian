---
id: software.testes.tranche20.001423
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
fontes: ["https://notwoods.github.io/mockk-guidebook/docs/mocking/coroutines/", "https://github.com/mockk/mockk/blob/master/README.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MockK: dublar funções suspensas

## Em uma frase
As funções de suspensão são configuradas e verificadas por variantes com prefixo próprio, que executam os blocos em contexto de corrotina.

## Por que importa
Código assíncrono exige os equivalentes de cada função, e usá-los corretamente mantém a verificação idêntica à de chamadas comuns.

## Como funciona
Use as variantes correspondentes para configurar e verificar, execute o caso em ambiente de teste de corrotinas e evite misturar as duas famílias.

## Exemplo
O repositório suspenso pode devolver o valor configurado, e a verificação confirma que a busca ocorreu uma única vez.

## Limites e trade-offs
Tentar configurar função suspensa com a função comum não compila, e o teste sem controle de tempo real fica lento e instável.

## Como verificar
Configure uma suspensão que nunca retorna e confirme que o teste falha por limite de tempo, como esperado.

## Conexões
- [[mockk-slots-and-capture]] — Veja também: MockK: capturar argumentos com slots.
- [[mockk-objects-and-statics]] — Veja também: MockK: dublar objetos e membros estáticos.

## Fontes
- [MockK — Guia de corrotinas](https://notwoods.github.io/mockk-guidebook/docs/mocking/coroutines/) — uso das variantes para funções suspensas; consultado em 2026-10-03.
- [MockK — README oficial](https://github.com/mockk/mockk/blob/master/README.md) — dublês, relaxamento, verificação, objetos e corrotinas; consultado em 2026-10-03.
