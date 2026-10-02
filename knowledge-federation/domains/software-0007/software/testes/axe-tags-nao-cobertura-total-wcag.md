---
id: software.testes.tranche12.000647
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

# axe-core: interpretar tags como escopo de regras

## Em uma frase
Tags de regras identificam relação com versões ou níveis de padrões e também podem marcar melhores práticas, entre outros metadados.

## Por que importa
Filtrar por tag facilita selecionar uma família de regras, mas uma execução automatizada cobre apenas as verificações implementadas e aplicáveis no DOM observado.

## Como funciona
Registre as tags selecionadas, a versão do axe-core e o contexto analisado, e complemente o processo com revisão de conteúdo, teclado e tecnologia assistiva.

## Exemplo
Um relatório pode enumerar as regras `wcag22aa` selecionadas sem afirmar que o site inteiro atende todos os critérios WCAG 2.2 AA.

## Limites e trade-offs
Sucesso em todas as regras executadas não detecta critérios que dependem de intenção, clareza, qualidade textual ou navegação não explorada.

## Como verificar
Compare a lista de regras com a estratégia de avaliação completa e documente quais critérios precisam de verificação manual ou outro método.

## Conexões
- [[axe-impact-priorizacao-nao-conformidade]] — Veja também: axe-core: usar impact para priorizar sem certificar conformidade.
- [[axe-dynamic-flows-multiple-scans]] — Veja também: axe-core: escanear separadamente estados de interação.

## Fontes
- [axe-core — JavaScript Accessibility API](https://raw.githubusercontent.com/dequelabs/axe-core/develop/doc/API.md) — axe.run, objeto de resultados, tags, conteúdo renderizado e iframes; consultado em 2026-10-02.
- [axe-core — Testing Context](https://raw.githubusercontent.com/dequelabs/axe-core/develop/doc/context.md) — include/exclude, seletores DOM, iframes e shadow DOM; consultado em 2026-10-02.
