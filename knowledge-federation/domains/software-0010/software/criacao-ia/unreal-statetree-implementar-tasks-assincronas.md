---
id: software.criacao_ia.tranche02.000153
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-02.md"
fontes: ["https://dev.epicgames.com/documentation/en-us/unreal-engine/statetree-in-unreal-engine", "https://dev.epicgames.com/documentation/en-us/unreal-engine/smart-objects-in-unreal-engine"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Unreal Engine: implementar tarefas atômicas com StateTree Tasks

## Em uma frase
As StateTree Tasks encapsulam ações executáveis específicas como movimentação, disparo de animações e uso de itens de gameplay.

## Por que importa
Dividir o comportamento em tarefas atômicas e reutilizáveis simplifica a montagem de novos arquétipos de inimigos e NPCs no projeto.

## Como funciona
Implemente `UStateTreeTaskBase` definindo `EnterState()`, `Tick()` e `ExitState()`. Retorne `EStateTreeRunStatus::Running` enquanto a ação estiver em progresso e `Succeeded` ou `Failed` ao término.

## Exemplo
```cpp
// Retornando status de execucao em uma StateTree Task
EStateTreeRunStatus FStateTreeMoveToTask::EnterState(FStateTreeExecutionContext& Context, const FStateTreeTransitionResult& Transition) const
{
    // Iniciar navegacao do AI Controller em direcao ao alvo
    return EStateTreeRunStatus::Running;
}
```

## Limites e trade-offs
Tarefas que esquecem de retornar `Succeeded` ou `Failed` mantêm o estado preso infinitamente no status `Running`, impedindo transições posteriores.

## Como verificar
Simule a interrupção da tarefa por dano externo e certifique-se de que o método `ExitState()` limpa corretamente os timers e componentes alocados.

## Conexões
- [[unreal-statetree-extrair-contexto-com-evaluators]] — Veja também: Unreal Engine: extrair contexto e dados de mundo com StateTree Evaluators.
- [[unreal-smart-objects-configurar-slots-de-interacao]] — Veja também: Unreal Engine: configurar Smart Object Definitions e slots de animação.
- [[unreal-statetree-estruturar-hierarquia-de-estados]] — Conexão temática direta com unreal-statetree-estruturar-hierarquia-de-estados.
- [[unreal-encapsular-acao-em-tasks]] — Conexão temática direta com unreal-encapsular-acao-em-tasks.
- [[unreal-smart-objects-conectar-a-tarefas-do-statetree]] — Conexão temática direta com unreal-smart-objects-conectar-a-tarefas-do-statetree.

## Fontes
- [Unreal Engine 5 Documentation — StateTree](https://dev.epicgames.com/documentation/en-us/unreal-engine/statetree-in-unreal-engine) — Manual oficial do framework statetree, árvores de estados hierárquicas leves, evaluators e tasks. Consulta: 2026-10-04.
- [Unreal Engine 5 Documentation — Smart Objects](https://dev.epicgames.com/documentation/en-us/unreal-engine/smart-objects-in-unreal-engine) — Documentação cobrindo smart object definitions, slots de animação, subsistema de reserva e interação com ia. Consulta: 2026-10-04.
