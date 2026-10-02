---
id: software.testes.tranche10.000380
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-10.md"
fontes: ["https://jestjs.io/docs/asynchronous", "https://jestjs.io/docs/setup-teardown"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Jest: retornar ou aguardar a Promise do teste

## Em uma frase
Jest considera uma função assíncrona concluída quando sua Promise retornada resolve ou rejeita.

## Por que importa
Jest precisa aguardar corretamente operações assíncronas e isolar estado de mocks para que uma aprovação corresponda ao caminho realmente executado. Sem return ou await, o teste pode terminar antes da resposta e deixar uma assertion tardia sem efeito no resultado.

## Como funciona
Retorne ou aguarde Promises, configure hooks no escopo necessário e trate snapshots e thresholds como evidências revisáveis, não como objetivos isolados. Retorne a cadeia de Promise ou declare a função async e aguarde cada operação cuja falha deve reprovar o caso.

## Exemplo
O teste retorna getUser(id).then(...) ou aguarda getUser(id) antes de validar o objeto renderizado.

## Limites e trade-offs
Os exemplos seguem a documentação Jest 30.5; mocks, timers e suporte ESM variam conforme ambiente, transformação e versão do Node. Criar uma Promise dentro do teste sem retorná-la nem aguardá-la não conecta sua falha ao lifecycle do runner.

## Como verificar
Force uma rejeição atrasada e confirme que Jest aguarda a Promise e marca a invocação como falha.

## Conexões
- [[jest-rejeicoes-async-com-rejects]] — Veja também: Jest: testar rejeições com .rejects aguardado.

## Fontes
- [Jest 30.5 — Testing asynchronous code](https://jestjs.io/docs/asynchronous) — promises, async/await, rejeições e garantia de que a asserção seja aguardada; consultado em 2026-10-02.
- [Jest 30.5 — Setup and teardown](https://jestjs.io/docs/setup-teardown) — escopo e ordenação de hooks de preparação e limpeza; consultado em 2026-10-02.
