---
id: software.testes.tranche12.000643
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-12.md"
fontes: ["https://raw.githubusercontent.com/dequelabs/axe-core/develop/doc/API.md", "https://raw.githubusercontent.com/dequelabs/axe-core/develop/doc/context.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# axe-core: selecionar regras com `runOnly`

## Em uma frase
A opção `runOnly` restringe quais regras ou grupos identificados por tags participam de uma execução.

## Por que importa
Filtrar um subconjunto torna um teste mais focado, porém o relatório passa a responder apenas às regras selecionadas e não às que ficaram de fora.

## Como funciona
Use tags compatíveis com o alvo ou IDs de regras quando a intenção exigir precisão, mantenha a seleção versionada e publique seu escopo junto do resultado.

## Exemplo
Um job rápido pode checar as regras associadas a um conjunto de critérios WCAG escolhido, enquanto a verificação mais ampla usa outro escopo.

## Limites e trade-offs
Uma tag representa metadado de regra, não prova de que todos os critérios de uma norma foram cobertos.

## Como verificar
Inspecione as regras resolvidas pela configuração e compare a lista com a política de acessibilidade definida para o job.

## Conexões
- [[axe-frames-shadow-dom-context]] — Veja também: axe-core: planejar frames e shadow DOM no contexto.
- [[axe-result-categories]] — Veja também: axe-core: distinguir violations, passes, incomplete e inapplicable.

## Fontes
- [axe-core — JavaScript Accessibility API](https://raw.githubusercontent.com/dequelabs/axe-core/develop/doc/API.md) — axe.run, objeto de resultados, tags, conteúdo renderizado e iframes; consultado em 2026-10-02.
- [axe-core — Testing Context](https://raw.githubusercontent.com/dequelabs/axe-core/develop/doc/context.md) — include/exclude, seletores DOM, iframes e shadow DOM; consultado em 2026-10-02.
