---
id: software.criacao_ia.tranche03.000251
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-03.md"
fontes: ["https://openusd.org/release/api/class_usd_stage.html", "https://openusd.org/release/glossary.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# OpenUSD: entender UsdStage como vista composta de layers

## Em uma frase
Um `UsdStage` apresenta uma cena composta de layers e arcs, não simplesmente o conteúdo isolado do arquivo root layer.

## Por que importa
Uma transformação visível no stage pode vir de referência, sublayer, variant, sessão ou override local. Editar o arquivo errado pode não alterar o valor composto, e salvar a camada equivocada pode misturar autoria de departamentos distintos.

## Como funciona
Abra um stage com root layer e, quando apropriado, session layer. Inspecione a origem das opinions e sua strength antes de mudar propriedades. A composição reúne prims e valores de múltiplas camadas em uma vista consultável; escolher `EditTarget` determina onde operações de autoria serão escritas, enquanto flattening é uma operação separada.

## Exemplo
Um artista vê a cor de uma malha em `usdview`, mas quer mudar apenas a variação de material do asset. Ele localiza a opinion responsável, escolhe a camada de trabalho ou variant edit context apropriado e confirma a camada exportada, em vez de sobrescrever a referência original.

## Limites e trade-offs
A aparência do stage depende dos arcs, resolver, load rules e seleções ativos. Leitura do valor composto não revela por si só a política de autoria desejada; stage cache e session layer também podem influenciar uma inspeção local.

## Como verificar
Inspecione root/session layers, prim stack e composition arcs; altere uma opinion numa camada temporária e observe strength e valor composto. Reabra o arquivo sem session layer para verificar quais alterações foram persistidas.

## Conexões
- [[openusd-load-rules-payloads-working-set]] — OpenUSD: tratar load rules como working set de payloads.

## Fontes
- [OpenUSD 26.08 — UsdStage API](https://openusd.org/release/api/class_usd_stage.html) — define operação e composição do stage a partir de layers e configuração Consulta: 2026-10-04.
- [OpenUSD 26.08 — Glossary](https://openusd.org/release/glossary.html) — define stage, composition, prims, layers e strength ordering Consulta: 2026-10-04.
