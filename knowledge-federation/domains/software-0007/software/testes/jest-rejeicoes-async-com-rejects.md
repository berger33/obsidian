---
id: software.testes.tranche10.000381
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
fontes: ["https://jestjs.io/docs/asynchronous", "https://jestjs.io/docs/mock-functions"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Jest: testar rejeições com .rejects aguardado

## Em uma frase
Matchers .rejects permitem verificar o valor ou erro de uma Promise rejeitada e precisam ser retornados ou aguardados.

## Por que importa
Jest precisa aguardar corretamente operações assíncronas e isolar estado de mocks para que uma aprovação corresponda ao caminho realmente executado. Um teste que espera erro mas esquece await pode passar sem observar a rejeição esperada.

## Como funciona
Retorne ou aguarde Promises, configure hooks no escopo necessário e trate snapshots e thresholds como evidências revisáveis, não como objetivos isolados. Use await expect(promise).rejects e, em caminhos try/catch, registre assertions para garantir que a exceção ocorreu.

## Exemplo
O teste aguarda a rejeição de carregar usuário inexistente e compara o código de erro de domínio.

## Limites e trade-offs
Os exemplos seguem a documentação Jest 30.5; mocks, timers e suporte ESM variam conforme ambiente, transformação e versão do Node. Não capture qualquer exceção genérica se o contrato pede um erro específico, pois isso pode aceitar falha não relacionada.

## Como verificar
Faça a operação resolver indevidamente e confirme que a ausência de rejeição esperada reprova o teste.

## Conexões
- [[jest-retornar-promise-para-aguardar-assercoes]] — Veja também: Jest: retornar ou aguardar a Promise do teste.
- [[jest-hooks-escopo-e-ordem]] — Veja também: Jest: alinhar setup hooks ao escopo describe.

## Fontes
- [Jest 30.5 — Testing asynchronous code](https://jestjs.io/docs/asynchronous) — promises, async/await, rejeições e garantia de que a asserção seja aguardada; consultado em 2026-10-02.
- [Jest 30.5 — Mock Functions](https://jestjs.io/docs/mock-functions) — estado de chamadas, resultados, implementações e spies; consultado em 2026-10-02.
