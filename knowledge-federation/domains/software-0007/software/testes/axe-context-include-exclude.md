---
id: software.testes.tranche12.000641
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
fontes: ["https://raw.githubusercontent.com/dequelabs/axe-core/develop/doc/context.md", "https://raw.githubusercontent.com/dequelabs/axe-core/develop/doc/API.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# axe-core: restringir contexto sem abandonar cobertura

## Em uma frase
O argumento `context` aceita seletores ou nós DOM para incluir regiões e uma configuração de exclusão para omitir áreas escolhidas.

## Por que importa
Escopo focado acelera feedback de componente e facilita associar achados a uma mudança, mas excluir uma região reduz o que a execução efetivamente cobriu.

## Como funciona
Inclua o container da feature sob teste, use `exclude` apenas para uma fronteira intencional e registre por que a parte excluída não pode ser avaliada naquele cenário.

## Exemplo
Uma verificação de componente pode incluir `main` e excluir um banner de terceiro enquanto uma varredura de página inteira roda em outro teste.

## Limites e trade-offs
Resultados de um container pequeno não representam automaticamente cabeçalho, navegação ou rodapé que ficaram fora do seletor.

## Como verificar
Compare a árvore selecionada com a página completa e mantenha uma execução ampla que detecte quando o componente sai do contexto planejado.

## Conexões
- [[axe-rendered-dom-state]] — Veja também: axe-core: executar análise depois de renderizar o estado.
- [[axe-frames-shadow-dom-context]] — Veja também: axe-core: planejar frames e shadow DOM no contexto.

## Fontes
- [axe-core — Testing Context](https://raw.githubusercontent.com/dequelabs/axe-core/develop/doc/context.md) — include/exclude, seletores DOM, iframes e shadow DOM; consultado em 2026-10-02.
- [axe-core — JavaScript Accessibility API](https://raw.githubusercontent.com/dequelabs/axe-core/develop/doc/API.md) — axe.run, objeto de resultados, tags, conteúdo renderizado e iframes; consultado em 2026-10-02.
