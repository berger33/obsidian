---
id: software.testes.tranche12.000646
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

# axe-core: usar impact para priorizar sem certificar conformidade

## Em uma frase
O campo `impact` ajuda a ordenar a severidade estimada de uma violação retornada, mas não é certificado de conformidade ou medida completa de impacto ao usuário.

## Por que importa
Prioridade acelera triagem quando há muitos achados, enquanto uma fila baseada só em rótulos pode ignorar barreiras importantes para uma pessoa específica.

## Como funciona
Leia `impact` junto de regra, nó, contexto e objetivo de remediação; mantenha decisão de prioridade e estado de conformidade em campos separados.

## Exemplo
Uma violação classificada como moderada pode bloquear uma tarefa central para determinado usuário e merecer correção antes de outra marcada como alta.

## Limites e trade-offs
Impacto pode estar ausente em resultados inconclusivos e não captura todo contexto assistivo ou fluxo alternativo.

## Como verificar
Revise exemplos de níveis com equipe de acessibilidade e confirme que o ranking não substitui análise do critério e da jornada.

## Conexões
- [[axe-incomplete-manual-review]] — Veja também: axe-core: revisar resultados marcados como incomplete.
- [[axe-tags-nao-cobertura-total-wcag]] — Veja também: axe-core: interpretar tags como escopo de regras.

## Fontes
- [axe-core — JavaScript Accessibility API](https://raw.githubusercontent.com/dequelabs/axe-core/develop/doc/API.md) — axe.run, objeto de resultados, tags, conteúdo renderizado e iframes; consultado em 2026-10-02.
- [axe-core — Testing Context](https://raw.githubusercontent.com/dequelabs/axe-core/develop/doc/context.md) — include/exclude, seletores DOM, iframes e shadow DOM; consultado em 2026-10-02.
