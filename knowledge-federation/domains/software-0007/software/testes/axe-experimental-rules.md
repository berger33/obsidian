---
id: software.testes.tranche18.001221
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

# axe-core: tratar regras experimentais

## Em uma frase
Regras marcadas como experimentais não rodam por padrão e precisam ser nomeadas explicitamente para entrar na análise.

## Por que importa
Essas regras cobrem casos ainda em maturação, e ativá-las cedo pode antecipar problemas que a norma exige sem gerar falso bloqueio.

## Como funciona
Ative regras experimentais em execução separada, avalie o resultado antes de bloquear e registre a decisão.

## Exemplo
Um time pode rodar a análise completa com as regras experimentais e comparar o resultado com a análise padrão antes de adotá-las.

## Limites e trade-offs
Habilitar tudo de uma vez mistura sinal maduro com rascunho, e o bloqueio por regra não estável reduz a confiança na esteira.

## Como verificar
Ative uma regra experimental e confirme que o resultado dela aparece identificado separadamente na saída.

## Conexões
- [[axe-configuration-and-exclusions]] — Veja também: axe-core: configurar regras e excluir trechos.
- [[axe-browser-integration]] — Veja também: axe-core: integrar ao teste de navegador.

## Fontes
- [axe-core — JavaScript API](https://github.com/dequelabs/axe-core/blob/develop/doc/API.md) — chamada de análise, opções, etiquetas, impacto e formato do resultado; consultado em 2026-10-03.
- [axe-core — Rule descriptions](https://github.com/dequelabs/axe-core/blob/develop/doc/rule-descriptions.md) — catálogo de regras, etiquetas de norma e classificação por boas práticas; consultado em 2026-10-03.
