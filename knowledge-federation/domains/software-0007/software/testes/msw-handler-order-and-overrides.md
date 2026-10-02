---
id: software.testes.tranche15.000863
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://mswjs.io/docs/defaults/", "https://mswjs.io/docs/http/intercepting-requests"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MSW: entender ordem e sobreposição de handlers

## Em uma frase
As requisições percorrem a lista de handlers em ordem até o primeiro que produzir uma instrução, e `server.use()` insere novos handlers no início da lista.

## Por que importa
Ignorar essa ordem faz um handler genérico colocado antes capturar requisições que deveriam ser atendidas por um caso mais específico definido depois.

## Como funciona
Organize handlers específicos antes dos genéricos, use `server.use()` para sobrescrever um cenário pontual e confie no reset do ciclo de vida para desfazer a inserção.

## Exemplo
Com um handler padrão de sucesso e outro de erro, registrar o de erro com `server.use()` no teste faz a próxima chamada receber a falha simulada.

## Limites e trade-offs
Apenas um handler é responsável por cada requisição, mas vários podem ser avaliados; a ordem só é visível quando dois padrões coincidem, e esse é justamente o caso que costuma enganar.

## Como verificar
Crie dois handlers sobrepostos, observe qual respondeu e confirme, após `resetHandlers()`, que o padrão inicial voltou a valer.

## Conexões
- [[msw-onunhandledrequest-fail]] — Veja também: MSW: tratar requisição sem handler como falha.
- [[msw-passthrough-real-response]] — Veja também: MSW: encaminhar requisições com passthrough.

## Fontes
- [MSW — Default behaviors](https://mswjs.io/docs/defaults/) — fallthrough entre handlers, ordem de avaliação e sensibilidade à ordem; consultado em 2026-10-02.
- [MSW — Intercepting requests](https://mswjs.io/docs/http/intercepting-requests) — handlers por método e URL, parâmetros de caminho e resolução de requisições; consultado em 2026-10-02.
