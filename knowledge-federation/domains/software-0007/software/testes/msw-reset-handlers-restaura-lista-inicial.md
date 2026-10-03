---
id: software.testes.tranche15.000923
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
fontes: ["https://mswjs.io/api/setup-server/reset-handlers", "https://mswjs.io/api/setup-server/use"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MSW: distinguir resetHandlers sem argumentos de substituição da lista

## Em uma frase
Sem argumentos, `resetHandlers()` remove handlers adicionados em runtime e restaura a lista inicial passada a `setupServer`; quando recebe novos handlers, estes substituem a lista inicial.

## Por que importa
A diferença importa para fixtures globais: uma chamada que parece limpar o estado pode na verdade redefinir qual conjunto passa a ser baseline para o restante da execução.

## Como funciona
O nome do método não implica sempre o mesmo conjunto restaurado.

## Exemplo
Use `afterEach(() => server.resetHandlers())` para remover overrides de cada teste, ou passe handlers explícitos apenas quando quiser estabelecer um novo baseline conhecido.

## Limites e trade-offs
Chamar reset com argumento errado pode descartar handlers de setup essenciais e produzir requests não tratados que só aparecem em uma ordem específica de casos.

## Como verificar
Monte um handler inicial, acrescente um override e teste as duas formas de reset, verificando a lista efetiva com requests que distinguem cada resposta.

## Conexões
- [[msw-use-como-override-de-comportamento]] — Veja também: MSW: usar server.use para acrescentar overrides locais a um cenário.
- [[msw-restore-handlers-nao-e-reset-handlers]] — Veja também: MSW: usar restoreHandlers para rearmar handlers de uso único.

## Fontes
- [MSW — resetHandlers()](https://mswjs.io/api/setup-server/reset-handlers) — reset de overrides e substituição da lista inicial; consultado em 2026-10-02.
- [MSW — use()](https://mswjs.io/api/setup-server/use) — adição e precedência de runtime handlers; consultado em 2026-10-02.
