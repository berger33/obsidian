---
id: software.testes.tranche18.001218
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

# axe-core: selecionar regras por etiquetas

## Em uma frase
Cada regra possui etiquetas que indicam nível de conformidade e critério relacionado, e a análise pode ser restringida a elas.

## Por que importa
Restringir por etiqueta torna explícita a norma pretendida e evita misturar recomendações de boas práticas com requisitos de conformidade.

## Como funciona
Use a etiqueta do nível desejado, amplie para cobrir versões mais recentes da norma quando aplicável e separe boas práticas em conjunto próprio.

## Exemplo
Uma verificação de conformidade intermediária pode rodar as etiquetas correspondentes e deixar recomendações fora do bloqueio.

## Limites e trade-offs
Misturar regras experimentais ou de boas práticas com requisitos legais gera bloqueios indevidos e ruído na triagem.

## Como verificar
Liste as regras ativas em uma execução e confirme que todas pertencem à etiqueta declarada.

## Conexões
- [[axe-run-and-results]] — Veja também: axe-core: executar a análise e ler o resultado.
- [[axe-impact-levels]] — Veja também: axe-core: priorizar por impacto.

## Fontes
- [axe-core — JavaScript API](https://github.com/dequelabs/axe-core/blob/develop/doc/API.md) — chamada de análise, opções, etiquetas, impacto e formato do resultado; consultado em 2026-10-03.
- [axe-core — Rule descriptions](https://github.com/dequelabs/axe-core/blob/develop/doc/rule-descriptions.md) — catálogo de regras, etiquetas de norma e classificação por boas práticas; consultado em 2026-10-03.
