---
id: software.criacao_ia.tranche05.000467
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
fontes: ["https://storybook.js.org/docs/writing-tests/integrations/vitest-addon", "https://storybook.js.org/docs/writing-tests/interaction-testing"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Storybook: executar stories como component tests com addon Vitest

## Em uma frase
O addon Vitest transforma stories em testes de componente executados em browser e pode combiná-los com cobertura e outros addons de teste.

## Por que importa
Os mesmos estados que documentam o componente também podem ser exercitados em terminal ou CI, reduzindo divergência entre showcase e suíte de teste.

## Como funciona
Instale e configure `@storybook/addon-vitest`, verifique suporte do framework Vite e da versão Vitest exigida e habilite browser mode conforme setup oficial.

## Exemplo
Um projeto React Vite executa stories com Playwright Chromium em modo headless, usando seu `play` e verificações no pipeline de integração contínua.

## Limites e trade-offs
A documentação exige framework Storybook baseado em Vite e Vitest compatível; setup para Next.js requer o framework `@storybook/nextjs-vite` nas condições indicadas.

## Como verificar
Rode addon no terminal, confirme que cada story esperada aparece como teste, execute uma falha intencional e valide saída no CI.

## Conexões
- [[storybook-play-interaction-canvas-userevent]] — Storybook: escrever testes de interação como play com canvas e userEvent awaited.
- [[storybook-visual-tests-baselines-chromatic]] — Storybook: detectar regressões de pixels com visual tests e baselines revisados.

## Fontes
- [Storybook — Vitest addon](https://storybook.js.org/docs/writing-tests/integrations/vitest-addon) — Descreve stories como component tests, browser mode e pré-requisitos do addon. Consulta: 2026-10-04.
- [Storybook — Interaction tests](https://storybook.js.org/docs/writing-tests/interaction-testing) — Explica as funções play que o Vitest addon pode executar como parte do teste. Consulta: 2026-10-04.
