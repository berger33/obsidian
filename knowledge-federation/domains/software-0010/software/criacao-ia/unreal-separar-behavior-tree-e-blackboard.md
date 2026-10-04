---
id: software.criacao_ia.tranche01.000041
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

# Unreal: separar Behavior Tree e Blackboard

## Em uma frase

A Behavior Tree organiza decisões em nós e o Blackboard guarda valores que esses nós consultam ou atualizam.

## Por que importa

Separar controle de estado torna a lógica de um NPC mais legível e permite compartilhar dados sem codificar todo comportamento num único Blueprint.

## Como funciona

Crie um Blackboard com chaves tipadas para alvo, destino e estado, e ligue-o à árvore executada pelo AIController.

## Exemplo

Um guarda consulta uma chave `TargetActor`, escolhe patrulha se ela estiver vazia e perseguição quando houver alvo válido.

## Limites e trade-offs

Chaves sem dono claro e nomes inconsistentes dificultam rastrear alterações e podem deixar estados obsoletos.

## Como verificar

Inspecione em runtime quais nós leem cada chave e confirme que seus valores são definidos e limpos nas transições esperadas.

## Conexões
- [[ml-agents-avaliar-o-modelo-em-inferencia]] — ML-Agents: avaliar o modelo em inferência.
- [[unreal-compor-sequence-e-selector]] — Unreal: compor Sequence e Selector.

## Fontes
- [Epic Games — Behavior Tree in Unreal Engine: Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/behavior-tree-in-unreal-engine---overview) — Apresenta estrutura de Behavior Trees, Blackboard e execução orientada a eventos na Unreal Engine. Consulta: 2026-10-04.
- [Epic Games — Environment Query System Quick Start](https://dev.epicgames.com/documentation/en-us/unreal-engine/environment-query-system-quick-start-in-unreal-engine) — Mostra a criação e execução de consultas EQS para selecionar posições do ambiente. Consulta: 2026-10-04.
