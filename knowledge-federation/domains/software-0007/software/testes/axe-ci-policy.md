---
id: software.testes.tranche18.001223
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
fontes: ["https://github.com/dequelabs/axe-core", "https://github.com/dequelabs/axe-core/blob/develop/doc/API.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# axe-core: definir política de bloqueio no pipeline

## Em uma frase
A execução pode falhar conforme a política escolhida, seja por qualquer violação, por níveis de impacto ou por lista de regras.

## Por que importa
A política transforma a análise em critério objetivo e evita que a verificação vire relatório ignorado.

## Como funciona
Escolha o critério a partir do passivo atual, bloqueie falhas novas e acompanhe a redução das antigas com prazo definido.

## Exemplo
Um projeto legado pode bloquear apenas violações críticas enquanto corrige o restante por etapas planejadas.

## Limites e trade-offs
Bloquear tudo desde o início paralisa o time, e nunca bloquear permite que o passivo cresça sem visibilidade.

## Como verificar
Reduza a política a um critério que o passivo atual viola e confirme que o trabalho do pipeline falha como esperado.

## Conexões
- [[axe-browser-integration]] — Veja também: axe-core: integrar ao teste de navegador.
- [[axe-manual-complement]] — Veja também: axe-core: complementar com verificação humana.

## Fontes
- [axe-core — repositório oficial](https://github.com/dequelabs/axe-core) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
- [axe-core — JavaScript API](https://github.com/dequelabs/axe-core/blob/develop/doc/API.md) — chamada de análise, opções, etiquetas, impacto e formato do resultado; consultado em 2026-10-03.
