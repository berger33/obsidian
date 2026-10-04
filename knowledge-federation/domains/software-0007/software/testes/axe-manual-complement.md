---
id: software.testes.tranche18.001224
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

# axe-core: complementar com verificação humana

## Em uma frase
A análise automática cobre parte dos critérios e não avalia experiência real com tecnologia assistiva nem ordem de foco percebida.

## Por que importa
Declarar conformidade apenas pelo resultado automático cria falsa garantia e deixa barreiras importantes sem verificação.

## Como funciona
Combine a análise com navegação por teclado, leitura por tecnologia assistiva e revisão de conteúdo, registrando o que ficou fora do alcance automático.

## Exemplo
Ordem de foco em formulário longo e clareza de mensagens de erro exigem julgamento que a análise estática não substitui.

## Limites e trade-offs
Itens marcados como aprovados indicam que nenhuma regra falhou, não que a experiência esteja adequada para todas as pessoas.

## Como verificar
Escolha um fluxo crítico e percorra-o apenas com teclado, comparando o observado com o resultado da análise automática.

## Conexões
- [[axe-ci-policy]] — Veja também: axe-core: definir política de bloqueio no pipeline.
- [[axe-baseline-and-history]] — Veja também: axe-core: acompanhar o passivo ao longo do tempo.

## Fontes
- [axe-core — JavaScript API](https://github.com/dequelabs/axe-core/blob/develop/doc/API.md) — chamada de análise, opções, etiquetas, impacto e formato do resultado; consultado em 2026-10-03.
- [axe-core — Rule descriptions](https://github.com/dequelabs/axe-core/blob/develop/doc/rule-descriptions.md) — catálogo de regras, etiquetas de norma e classificação por boas práticas; consultado em 2026-10-03.
