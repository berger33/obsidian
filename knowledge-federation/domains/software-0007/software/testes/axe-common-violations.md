---
id: software.testes.tranche18.001226
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-18.md"
fontes: ["https://github.com/dequelabs/axe-core/blob/develop/doc/rule-descriptions.md", "https://github.com/dequelabs/axe-core"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# axe-core: corrigir violações frequentes

## Em uma frase
As regras mais acionadas costumam envolver texto alternativo, rótulos de formulário, contraste, estrutura de cabeçalhos e identificação de idioma.

## Por que importa
Corrigir primeiro as causas frequentes reduz o passivo rapidamente e melhora a experiência de quem usa recursos de assistência.

## Como funciona
Trate cada ocorrência com correção na origem, no componente compartilhado, em vez de ajustar caso a caso na página.

## Exemplo
Se um componente de campo sem rótulo é reutilizado, corrigir o componente remove a violação de todas as telas que o usam.

## Limites e trade-offs
Correções pontuais no teste escondem o problema sem melhorar a experiência, e a repetição do mesmo defeito indica falha de componente.

## Como verificar
Selecione uma regra recorrente e confirme que a correção no componente compartilhado elimina todas as ocorrências da lista.

## Conexões
- [[axe-baseline-and-history]] — Veja também: axe-core: acompanhar o passivo ao longo do tempo.
- [[axe-limits]] — Veja também: axe-core: reconhecer limites da ferramenta.

## Fontes
- [axe-core — Rule descriptions](https://github.com/dequelabs/axe-core/blob/develop/doc/rule-descriptions.md) — catálogo de regras, etiquetas de norma e classificação por boas práticas; consultado em 2026-10-03.
- [axe-core — repositório oficial](https://github.com/dequelabs/axe-core) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
