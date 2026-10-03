---
id: software.testes.tranche15.000924
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
fontes: ["https://mswjs.io/api/setup-server/restore-handlers", "https://mswjs.io/api/setup-server/reset-handlers"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MSW: usar restoreHandlers para rearmar handlers de uso único

## Em uma frase
`restoreHandlers()` volta a marcar handlers configurados para uso único como não consumidos, permitindo que eles interceptem uma solicitação futura outra vez.

## Por que importa
Isso resolve um eixo diferente do `resetHandlers`: um handler `once` pode continuar cadastrado, mas estar marcado como usado.

## Como funciona
Restaurar o estado de consumo não reconstrói nem substitui a lista de handlers.

## Exemplo
Depois de fazer uma request atendida por handler `once`, chame `server.restoreHandlers()` no caso que precisa reproduzir a mesma resposta e envie nova solicitação.

## Limites e trade-offs
Repetir uma resposta de uso único sem reset pode esconder a intenção do teste, e a restauração global de handlers usados pode rearmar mais casos do que o necessário.

## Como verificar
Faça duas requests, confirme que a segunda passa ao comportamento normal, restaure handlers e confirme que a terceira volta à resposta mockada.

## Conexões
- [[msw-reset-handlers-restaura-lista-inicial]] — Veja também: MSW: distinguir resetHandlers sem argumentos de substituição da lista.
- [[msw-close-restaura-fronteira-de-processo]] — Veja também: MSW: fechar a interceptação depois da suite.

## Fontes
- [MSW — restoreHandlers()](https://mswjs.io/api/setup-server/restore-handlers) — rearmar handlers de uso único; consultado em 2026-10-02.
- [MSW — resetHandlers()](https://mswjs.io/api/setup-server/reset-handlers) — reset de overrides e substituição da lista inicial; consultado em 2026-10-02.
