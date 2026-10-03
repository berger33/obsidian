---
id: software.testes.tranche15.000933
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
data_revisao_ia: "2026-10-02"
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://nodejs.org/api/test.html", "https://nodejs.org/api/test.html#class-testcontext"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# node:test: registrar teardown no contexto do caso

## Em uma frase
O callback de um teste recebe `TestContext`, que pode fornecer helpers e registro de limpeza; usar esse escopo reduz risco de deixar recursos abertos depois de uma assertion falhar.

## Por que importa
O lifecycle do caso é o lugar natural para fechar server, remover temporários ou restaurar mocks criados naquela execução.

## Como funciona
Recursos globais exigem hook de suite e coordenação distinta, especialmente quando arquivos rodam em processos separados.

## Exemplo
Crie um arquivo temporário no teste e registre a remoção com o mecanismo de teardown do `TestContext`; valide que o callback de limpeza roda após sucesso e após falha.

## Limites e trade-offs
Limpeza registrada depois de criar vários recursos precisa observar dependências de encerramento e não deve depender da ordem incidental de subtestes concorrentes.

## Como verificar
Faça um teste falhar depois de abrir o recurso e confirme no processo que o teardown foi executado e que uma execução repetida não herda arquivo ou porta.

## Conexões
- [[node-test-name-pattern-e-filtros-de-casos]] — Veja também: node:test: usar filtro de nome sem confundir seleção com descoberta.
- [[node-test-mocks-com-restauracao-do-contexto]] — Veja também: node:test: preferir mocks vinculados ao contexto para restauração automática.

## Fontes
- [Node.js v26.10 — Test runner](https://nodejs.org/api/test.html) — TestContext, isolamento, hooks, mocks, concorrência e reporters; consultado em 2026-10-02.
- [Node.js v26.10 — Test runner: TestContext](https://nodejs.org/api/test.html#class-testcontext) — hooks de cleanup por caso e ciclo de vida de subtestes; consultado em 2026-10-02.
