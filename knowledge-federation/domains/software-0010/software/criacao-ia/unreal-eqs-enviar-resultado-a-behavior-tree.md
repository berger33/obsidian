---
id: software.criacao_ia.tranche01.000049
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

# Unreal EQS: enviar resultado à Behavior Tree

## Em uma frase

A saída de uma EQS query pode ser gravada no Blackboard para a árvore usar numa próxima tarefa.

## Por que importa

Integração explícita transforma análise do espaço em comportamento de movimento ou escolha do NPC.

## Como funciona

Execute a query em nó apropriado, associe item ou actor de saída à chave esperada e trate retorno vazio antes de mover.

## Exemplo

A árvore pede ponto de cobertura, verifica se `CoverLocation` foi preenchido e só então inicia `MoveTo`.

## Limites e trade-offs

Resultado da query pode ficar obsoleto se cenário, alvo ou navegação mudarem entre consulta e execução.

## Como verificar

Forçe uma query sem candidatos e outra com movimento bloqueado; confirme fallback e ausência de uso de destino antigo.

## Conexões
- [[unreal-eqs-compor-tests-e-pontuacao]] — Unreal EQS: compor Tests e pontuação.
- [[unreal-depurar-a-decisao-do-npc-em-runtime]] — Unreal: depurar a decisão do NPC em runtime.

## Fontes
- [Epic Games — Behavior Tree in Unreal Engine: Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/behavior-tree-in-unreal-engine---overview) — Apresenta estrutura de Behavior Trees, Blackboard e execução orientada a eventos na Unreal Engine. Consulta: 2026-10-04.
- [Epic Games — Environment Query System Quick Start](https://dev.epicgames.com/documentation/en-us/unreal-engine/environment-query-system-quick-start-in-unreal-engine) — Mostra a criação e execução de consultas EQS para selecionar posições do ambiente. Consulta: 2026-10-04.
