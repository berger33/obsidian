---
id: software.testes.tranche15.000862
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
fontes: ["https://mswjs.io/docs/api/setup-server/", "https://mswjs.io/docs/defaults/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MSW: tratar requisição sem handler como falha

## Em uma frase
Por padrão, uma requisição sem handler correspondente gera aviso; a opção `onUnhandledRequest` permite elevá-la a erro ou fornecer tratamento próprio.

## Por que importa
Um aviso perdido no log de integração contínua significa que o teste passou por acidente, usando rede real ou comportamento indefinido em vez do cenário planejado.

## Como funciona
Configure `onUnhandledRequest: 'error'` no ambiente de integração contínua e use uma função personalizada quando for necessário registrar a URL exata que escapou dos handlers.

## Exemplo
`server.listen({ onUnhandledRequest: 'error' })` faz o teste falhar imediatamente ao encontrar uma chamada sem resposta mockada definida.

## Limites e trade-offs
O erro de requisição não tratada não distingue tráfego intencional de serviços externos nem substitui uma política clara sobre o que pode sair para a rede; a opção precisa ser combinada com handlers completos.

## Como verificar
Remova deliberadamente um handler e confirme que a suíte falha com mensagem identificando método e URL, em vez de apenas emitir aviso.

## Conexões
- [[msw-lifecycle-listen-reset-close]] — Veja também: MSW: cumprir o ciclo listen, reset e close.
- [[msw-handler-order-and-overrides]] — Veja também: MSW: entender ordem e sobreposição de handlers.

## Fontes
- [MSW — setupServer](https://mswjs.io/docs/api/setup-server/) — interceptação em Node.js e ciclo de vida de listen, resetHandlers e close; consultado em 2026-10-02.
- [MSW — Default behaviors](https://mswjs.io/docs/defaults/) — fallthrough entre handlers, ordem de avaliação e sensibilidade à ordem; consultado em 2026-10-02.
