---
id: software.criacao_ia.tranche05.000466
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-05.md"
fontes: ["https://storybook.js.org/docs/writing-tests/interaction-testing", "https://storybook.js.org/docs/writing-stories/play-function"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Storybook: escrever testes de interação como play com canvas e userEvent awaited

## Em uma frase
Uma função `play` executa depois da renderização e pode simular ações do usuário e verificar o estado resultante da story.

## Por que importa
Um estado estático comprova renderização, mas não garante que digitar, clicar, enviar formulário ou abrir diálogo funcione como esperado.

## Como funciona
Receba `canvas` e `userEvent` em `play`, consulte elementos com queries acessíveis e aguarde cada interação assíncrona. Use `screen` para elementos renderizados fora da raiz da story.

## Exemplo
A história preenche campos por label, clica em botão por role e verifica a confirmação visível sem depender da ordem de nós na árvore DOM.

## Limites e trade-offs
A execução automatizada não substitui a decisão sobre quais fluxos são importantes; `data-testid` deve ser último recurso depois de queries que representam a experiência real.

## Como verificar
Rode a story no painel Interactions e no ambiente de teste, confirme que cada `userEvent` foi awaited e que as asserções falham quando o resultado esperado é removido.

## Conexões
- [[storybook-loaders-before-render-loaded-context]] — Storybook: usar loaders assíncronos como escape hatch para dados externos.
- [[storybook-vitest-addon-stories-como-component-tests]] — Storybook: executar stories como component tests com addon Vitest.

## Fontes
- [Storybook — Interaction tests](https://storybook.js.org/docs/writing-tests/interaction-testing) — Documenta play, canvas, userEvent, asserções e preferência por queries acessíveis. Consulta: 2026-10-04.
- [Storybook — Play function](https://storybook.js.org/docs/writing-stories/play-function) — Explica execução pós-render, canvas e uso de `screen` para elementos externos. Consulta: 2026-10-04.
