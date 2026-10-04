---
id: software.testes.tranche18.001220
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
fontes: ["https://github.com/dequelabs/axe-core/blob/develop/doc/API.md", "https://github.com/dequelabs/axe-core/blob/develop/doc/rule-descriptions.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# axe-core: configurar regras e excluir trechos

## Em uma frase
As opções permitem habilitar ou desabilitar regras específicas e limitar a análise a regiões da página.

## Por que importa
Exceções estreitas e justificadas evitam bloquear a verificação por componentes fora do controle do time.

## Como funciona
Desabilite regras pontuais com comentário, limite o contexto a elementos sob responsabilidade do time e documente cada exceção.

## Exemplo
Um componente de terceiro embutido pode ser excluído enquanto o restante da página permanece analisado.

## Limites e trade-offs
Desabilitar por classe inteira de regras esvazia a verificação, e exclusões esquecidas continuam ocultando problemas reais.

## Como verificar
Reative temporariamente uma regra desabilitada e confirme quantas violações ela estava suprimindo.

## Conexões
- [[axe-impact-levels]] — Veja também: axe-core: priorizar por impacto.
- [[axe-experimental-rules]] — Veja também: axe-core: tratar regras experimentais.

## Fontes
- [axe-core — JavaScript API](https://github.com/dequelabs/axe-core/blob/develop/doc/API.md) — chamada de análise, opções, etiquetas, impacto e formato do resultado; consultado em 2026-10-03.
- [axe-core — Rule descriptions](https://github.com/dequelabs/axe-core/blob/develop/doc/rule-descriptions.md) — catálogo de regras, etiquetas de norma e classificação por boas práticas; consultado em 2026-10-03.
