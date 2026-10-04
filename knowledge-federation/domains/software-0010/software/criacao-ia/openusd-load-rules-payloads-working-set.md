---
id: software.criacao_ia.tranche03.000252
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
fontes: ["https://openusd.org/release/api/class_usd_stage_load_rules.html", "https://openusd.org/release/api/class_usd_stage.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# OpenUSD: tratar load rules como working set de payloads

## Em uma frase
Load rules determinam quais payload arcs estão carregados no stage, permitindo limitar a cena composta ao conjunto necessário para a tarefa atual.

## Por que importa
Stages de produção podem conter muito mais descrição do que o viewport, conversor ou job de render precisa. Carregar tudo sem necessidade aumenta memória e tempo de composição, enquanto descarregar um payload reduz conteúdo visível sem apagar a autoria no arquivo.

## Como funciona
Use APIs de load/unload ou `UsdStageLoadRules` para definir comportamento por prim e carregar ou descarregar payloads de forma explícita. `LoadAll` e `LoadNone` estabelecem políticas amplas; regras por caminho refinam o conjunto de trabalho. Salve as regras apropriadas no código da aplicação se cada job precisar de estado de carregamento reproduzível.

## Exemplo
Um editor de mundo abre primeiro uma planta de cenário com payloads descarregados, mostra bounds e estrutura dos prims, e carrega apenas o bairro sob edição. O sistema registra os caminhos carregados para que uma imagem de revisão possa ser reproduzida.

## Limites e trade-offs
Load rules control payloads, não substituem política de asset resolution nem garantem que todas as dependências externas estejam disponíveis. Um payload descarregado pode ocultar dados que uma operação posterior espera encontrar; não confunda unload com apagar ou desativar prim.

## Como verificar
Compare travessia e memória sob LoadNone e LoadAll, inspecione estado carregado de cada prim e reabra o stage com as mesmas regras. Teste referências e payloads aninhados em caminhos de asset ausentes.

## Conexões
- [[openusd-stage-composed-view-layers]] — OpenUSD: entender UsdStage como vista composta de layers.
- [[openusd-reference-versus-payload]] — OpenUSD: escolher reference ou payload para composição diferida.

## Fontes
- [OpenUSD 26.08 — UsdStageLoadRules API](https://openusd.org/release/api/class_usd_stage_load_rules.html) — define regras de carregamento por stage e seleção de payloads Consulta: 2026-10-04.
- [OpenUSD 26.08 — UsdStage API](https://openusd.org/release/api/class_usd_stage.html) — documenta Load, Unload e políticas de carga para um stage Consulta: 2026-10-04.
