---
id: software.criacao_ia.tranche01.000045
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

# Unreal: escolher aborts de observadores

## Em uma frase

Aborts definem quando uma mudança numa condição monitorada interrompe tarefas ativas ou ramos de menor prioridade.

## Por que importa

Interrupção responsiva permite que NPC reaja a alvo recém-detectado sem esperar o término de rotina longa.

## Como funciona

Configure escopo de abort no decorator com base na hierarquia e prioridade dos ramos que devem ceder a execução.

## Exemplo

Um ramo de combate aborta patrulha quando o Blackboard recebe alvo, enquanto perda de visão pode fazer o NPC voltar à busca.

## Limites e trade-offs

Abortar demais pode causar comportamento oscilante e iniciar/cancelar tarefas repetidamente.

## Como verificar

Mude a chave durante uma tarefa em curso e confirme qual ramo interrompe, qual continua e se a decisão permanece estável.

## Conexões
- [[unreal-encapsular-acao-em-tasks]] — Unreal: encapsular ação em Tasks.
- [[unreal-eqs-gerar-candidatos-espaciais]] — Unreal EQS: gerar candidatos espaciais.

## Fontes
- [Epic Games — Behavior Tree in Unreal Engine: Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/behavior-tree-in-unreal-engine---overview) — Apresenta estrutura de Behavior Trees, Blackboard e execução orientada a eventos na Unreal Engine. Consulta: 2026-10-04.
- [Epic Games — Environment Query System Quick Start](https://dev.epicgames.com/documentation/en-us/unreal-engine/environment-query-system-quick-start-in-unreal-engine) — Mostra a criação e execução de consultas EQS para selecionar posições do ambiente. Consulta: 2026-10-04.
