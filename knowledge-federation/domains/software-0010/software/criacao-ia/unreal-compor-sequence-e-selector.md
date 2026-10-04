---
id: software.criacao_ia.tranche01.000042
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

# Unreal: compor Sequence e Selector

## Em uma frase

Nós compostos expressam se subtarefas precisam concluir em ordem ou se alternativas devem ser tentadas até uma funcionar.

## Por que importa

A composição explícita reduz condições implícitas espalhadas e ajuda designers a alterar prioridade de comportamento com segurança.

## Como funciona

Use Sequence para passos dependentes e Selector para alternativas ordenadas; escolha prioridade deliberada quando dois ramos puderem ser executáveis.

## Exemplo

Um NPC verifica munição, mira e atira numa sequência; se não houver inimigo, um selector passa para procurar cobertura ou patrulhar.

## Limites e trade-offs

Ordem de ramos altera o resultado, e uma sequência longa pode bloquear escolhas urgentes se não houver mecanismos de interrupção.

## Como verificar

Teste cada ramo isoladamente, altere condições de entrada e confira o nó ativo quando as alternativas competem.

## Conexões
- [[unreal-separar-behavior-tree-e-blackboard]] — Unreal: separar Behavior Tree e Blackboard.
- [[unreal-usar-decorators-como-condicoes]] — Unreal: usar Decorators como condições.

## Fontes
- [Epic Games — Behavior Tree in Unreal Engine: Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/behavior-tree-in-unreal-engine---overview) — Apresenta estrutura de Behavior Trees, Blackboard e execução orientada a eventos na Unreal Engine. Consulta: 2026-10-04.
- [Epic Games — Environment Query System Quick Start](https://dev.epicgames.com/documentation/en-us/unreal-engine/environment-query-system-quick-start-in-unreal-engine) — Mostra a criação e execução de consultas EQS para selecionar posições do ambiente. Consulta: 2026-10-04.
