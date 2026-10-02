---
id: software.testes.tranche12.000642
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

# axe-core: planejar frames e shadow DOM no contexto

## Em uma frase
axe-core tem opções de contexto para limitar seleção dentro de frames e de regiões de shadow DOM.

## Por que importa
Conteúdo hospedado em árvore aninhada pode exigir seletores específicos; uma análise do documento principal não basta para presumir que todos os elementos foram avaliados.

## Como funciona
Use a seleção `fromFrames` documentada para indicar níveis de iframe e forneça axe-core nos documentos que participam da verificação; teste a estratégia de shadow DOM suportada pela aplicação.

## Exemplo
Um formulário de pagamento embutido em iframe pode ser selecionado por cadeia de frame e seletor do formulário interno.

## Limites e trade-offs
Origem cruzada, frame ainda carregando ou modo de shadow DOM não suportado podem impedir que o conteúdo apareça na análise.

## Como verificar
Inspecione os nós retornados por cada frame e rode casos com frame vazio e preenchido para descobrir se o runner inclui o conteúdo esperado.

## Conexões
- [[axe-context-include-exclude]] — Veja também: axe-core: restringir contexto sem abandonar cobertura.
- [[axe-runonly-tags-rules]] — Veja também: axe-core: selecionar regras com `runOnly`.

## Fontes
- [axe-core — Testing Context](https://raw.githubusercontent.com/dequelabs/axe-core/develop/doc/context.md) — include/exclude, seletores DOM, iframes e shadow DOM; consultado em 2026-10-02.
- [axe-core — JavaScript Accessibility API](https://raw.githubusercontent.com/dequelabs/axe-core/develop/doc/API.md) — axe.run, objeto de resultados, tags, conteúdo renderizado e iframes; consultado em 2026-10-02.
