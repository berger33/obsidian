---
id: software.criacao_ia.tranche01.000050
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-01.md"
fontes: ["https://dev.epicgames.com/documentation/en-us/unreal-engine/behavior-tree-in-unreal-engine---overview", "https://dev.epicgames.com/documentation/en-us/unreal-engine/environment-query-system-quick-start-in-unreal-engine"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Unreal: depurar a decisão do NPC em runtime

## Em uma frase

Visualizar execução da árvore, valores do Blackboard e resultados EQS ajuda a localizar qual condição escolheu o comportamento.

## Por que importa

Depuração por estado observável reduz tentativa e erro baseada apenas no vídeo final do NPC.

## Como funciona

Ative ferramentas de debug da engine, selecione o AIController em execução e inspecione nós, chaves e itens candidatos em sequência.

## Exemplo

Se um bot fica parado, verifique primeiro se a Task está ativa, depois a chave de destino e o resultado da consulta espacial.

## Limites e trade-offs

Uma captura de uma única instância pode esconder problemas intermitentes, concorrência ou diferenças entre clientes.

## Como verificar

Reproduza o problema com a mesma cena, registre a transição de estado e compare duas condições limítrofes além do caso comum.

## Conexões
- [[unreal-eqs-enviar-resultado-a-behavior-tree]] — Unreal EQS: enviar resultado à Behavior Tree.
- [[godot-preparar-malha-de-navegacao]] — Godot: preparar malha de navegação.

## Fontes
- [Epic Games — Behavior Tree in Unreal Engine: Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/behavior-tree-in-unreal-engine---overview) — Apresenta estrutura de Behavior Trees, Blackboard e execução orientada a eventos na Unreal Engine. Consulta: 2026-10-04.
- [Epic Games — Environment Query System Quick Start](https://dev.epicgames.com/documentation/en-us/unreal-engine/environment-query-system-quick-start-in-unreal-engine) — Mostra a criação e execução de consultas EQS para selecionar posições do ambiente. Consulta: 2026-10-04.
