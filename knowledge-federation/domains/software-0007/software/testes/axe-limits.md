---
id: software.testes.tranche18.001227
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

# axe-core: reconhecer limites da ferramenta

## Em uma frase
A biblioteca detecta uma parte dos problemas de acessibilidade e não substitui avaliação com pessoas usuárias nem revisão de conteúdo.

## Por que importa
Tratar a ferramenta como cobertura completa leva a conformidade aparente e a barreiras reais sem tratamento.

## Como funciona
Use a análise como rede de proteção contínua e mantenha avaliações periódicas com pessoas e critérios que a automação não alcança.

## Exemplo
Textos alternativos presentes porém pouco descritivos passam pela regra estrutural sem informar quem depende de leitura assistida.

## Limites e trade-offs
Uma página sem violações pode continuar inutilizável por problemas de fluxo, linguagem ou interação não previstos nas regras.

## Como verificar
Escolha uma página sem violações e verifique com leitor de tela se as tarefas principais são concluíveis sem apoio visual.

## Conexões
- [[axe-common-violations]] — Veja também: axe-core: corrigir violações frequentes.

## Fontes
- [axe-core — JavaScript API](https://github.com/dequelabs/axe-core/blob/develop/doc/API.md) — chamada de análise, opções, etiquetas, impacto e formato do resultado; consultado em 2026-10-03.
- [axe-core — Rule descriptions](https://github.com/dequelabs/axe-core/blob/develop/doc/rule-descriptions.md) — catálogo de regras, etiquetas de norma e classificação por boas práticas; consultado em 2026-10-03.
