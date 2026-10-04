---
id: software.testes.tranche18.001225
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
fontes: ["https://github.com/dequelabs/axe-core/blob/develop/doc/API.md", "https://github.com/dequelabs/axe-core"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# axe-core: acompanhar o passivo ao longo do tempo

## Em uma frase
Registrar a contagem por regra e por versão do código permite medir a evolução do passivo e comparar execuções.

## Por que importa
Números sem histórico não mostram tendência, e a comparação entre revisões identifica regressões introduzidas por mudanças recentes.

## Como funciona
Grave o relatório estruturado por execução, inclua a versão da biblioteca e compare a contagem por regra entre revisões.

## Exemplo
Uma nova biblioteca de componentes pode introduzir violações de rótulo que aparecem no relatório da revisão correspondente.

## Limites e trade-offs
Comparar execuções com versões diferentes da ferramenta mistura mudanças de regra com mudanças de código.

## Como verificar
Compare dois relatórios da mesma versão da ferramenta e confirme que a diferença de contagem corresponde à mudança de código.

## Conexões
- [[axe-manual-complement]] — Veja também: axe-core: complementar com verificação humana.
- [[axe-common-violations]] — Veja também: axe-core: corrigir violações frequentes.

## Fontes
- [axe-core — JavaScript API](https://github.com/dequelabs/axe-core/blob/develop/doc/API.md) — chamada de análise, opções, etiquetas, impacto e formato do resultado; consultado em 2026-10-03.
- [axe-core — repositório oficial](https://github.com/dequelabs/axe-core) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
