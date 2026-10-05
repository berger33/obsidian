---
id: software.criacao_ia.tranche05.000465
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
fontes: ["https://storybook.js.org/docs/writing-stories/loaders", "https://storybook.js.org/docs/writing-stories/args"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Storybook: usar loaders assíncronos como escape hatch para dados externos

## Em uma frase
Loaders são funções assíncronas executadas antes da renderização e seus resultados ficam disponíveis no contexto da story em `loaded`.

## Por que importa
Uma story que depende de dados externos pode precisar aguardar resposta antes de montar o componente, sem incorporar estado de rede à própria API de produção.

## Como funciona
Prefira args para dados estáticos de story. Quando há necessidade real de carga assíncrona, defina loaders no nível global, componente ou story e leia `loaded` no contexto de render ou decorator.

## Exemplo
Um loader de preview disponibiliza `currentUser` a todas as stories; um loader local busca um todo item e o render da story combina os dados carregados com args explícitos.

## Limites e trade-offs
A documentação classifica loaders como recurso avançado e recomenda args na maioria dos casos. Os loaders aplicáveis executam em paralelo e valores duplicados seguem precedência de global para componente e story.

## Como verificar
Teste ausência e sucesso de rede, confirme que o render aguarda conclusão, verifique chaves no contexto `loaded` e crie colisão controlada para validar precedência.

## Conexões
- [[storybook-globals-toolbar-decorator-theme]] — Storybook: usar globals e toolbar para variar contexto compartilhado como tema.
- [[storybook-play-interaction-canvas-userevent]] — Storybook: escrever testes de interação como play com canvas e userEvent awaited.

## Fontes
- [Storybook — Loaders](https://storybook.js.org/docs/writing-stories/loaders) — Define timing antes do render, contexto `loaded`, escopos, concorrência e precedência de loaders. Consulta: 2026-10-04.
- [Storybook — Args](https://storybook.js.org/docs/writing-stories/args) — Descreve args como forma recomendada de controlar dados de stories e renderização. Consulta: 2026-10-04.
