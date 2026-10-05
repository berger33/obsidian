---
id: software.criacao_ia.tranche05.000470
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
fontes: ["https://storybook.js.org/docs/writing-tests/accessibility-testing", "https://github.com/dequelabs/axe-core"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Storybook a11y: combinar varredura axe com verificação manual de acessibilidade

## Em uma frase
O addon a11y verifica DOM com regras axe-core e identifica violações conhecidas, mas também lista situações que precisam de confirmação manual.

## Por que importa
Automação encontra problemas comuns de atributos e contraste, porém não demonstra por si só que teclado, leitor de tela e fluxo de uso funcionam para pessoas.

## Como funciona
Instale `@storybook/addon-a11y`, execute o painel por story e revise abas de violações, passes e incomplete; rode checks com Vitest addon se fizer sentido no CI.

## Exemplo
Uma story de menu passa axe, mas o time ainda percorre foco por teclado e confirma que leitor de tela anuncia abertura, seleção e retorno ao gatilho.

## Limites e trade-offs
A documentação descreve heurísticas e verificações automáticas, não certificação WCAG; achados incomplete e semântica contextual exigem avaliação humana.

## Como verificar
Use histórias com estados vazio, foco, erro e conteúdo dinâmico, examine incomplete e complete revisão manual de teclado, contraste e anúncio com tecnologia assistiva.

## Conexões
- [[storybook-autodocs-tags-living-documentation]] — Storybook: habilitar Autodocs por tag e estender a documentação com MDX.

## Fontes
- [Storybook — Accessibility tests](https://storybook.js.org/docs/writing-tests/accessibility-testing) — Descreve addon axe-core, violações, passes e itens incomplete para confirmar manualmente. Consulta: 2026-10-04.
- [Deque axe-core](https://github.com/dequelabs/axe-core) — Documenta a biblioteca de regras automatizadas usada pelo addon Storybook. Consulta: 2026-10-04.
