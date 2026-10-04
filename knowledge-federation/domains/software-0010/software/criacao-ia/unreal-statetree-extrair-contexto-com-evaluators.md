---
id: software.criacao_ia.tranche02.000152
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

# Unreal Engine: extrair contexto e dados de mundo com StateTree Evaluators

## Em uma frase
Os Evaluators do StateTree extraem e atualizam continuamente variáveis do mundo e da entidade no início de cada avaliação.

## Por que importa
Centralizar a coleta de dados de sensores e estado da entidade em Evaluators evita leituras redundantes de propriedades dentro das tarefas individuais.

## Como funciona
Crie uma classe C++ ou Blueprint herdando de `UStateTreeEvaluatorBase`, implemente o método `Tick()` para consultar distâncias e alvos e armazene os valores nos parâmetros de contexto da árvore.

## Exemplo
```cpp
// Exemplo de StateTree Evaluator em C++ na UE5
USTRUCT()
struct FStateTreeTargetEvaluator : public FStateTreeEvaluatorCommonBase
{
    GENERATED_BODY()

    virtual void Tick(FStateTreeExecutionContext& Context, const float DeltaTime) const override
    {
        // Consultar posicao do jogador e atualizar variavel de contexto
    }
};
```

## Limites e trade-offs
Evaluators executam em cada ciclo de avaliação; rotinas pesadas de busca espacial dentro do `Tick` de um Evaluator degradam o frame rate da CPU.

## Como verificar
Inspecione os tempos de processamento com o comando de console `stat StateTree` para checar se a coleta de dados não introduz gargalos.

## Conexões
- [[unreal-statetree-estruturar-hierarquia-de-estados]] — Veja também: Unreal Engine: estruturar hierarquia de estados leves no StateTree.
- [[unreal-statetree-implementar-tasks-assincronas]] — Veja também: Unreal Engine: implementar tarefas atômicas com StateTree Tasks.
- [[unreal-eqs-gerar-candidatos-espaciais]] — Conexão temática direta com unreal-eqs-gerar-candidatos-espaciais.
- [[unity-utility-ai-compor-fatores-de-saude-e-distancia]] — Conexão temática direta com unity-utility-ai-compor-fatores-de-saude-e-distancia.

## Fontes
- [Unreal Engine 5 Documentation — StateTree](https://dev.epicgames.com/documentation/en-us/unreal-engine/statetree-in-unreal-engine) — Manual oficial do framework statetree, árvores de estados hierárquicas leves, evaluators e tasks. Consulta: 2026-10-04.
- [Unreal Engine 5 Documentation — Smart Objects](https://dev.epicgames.com/documentation/en-us/unreal-engine/smart-objects-in-unreal-engine) — Documentação cobrindo smart object definitions, slots de animação, subsistema de reserva e interação com ia. Consulta: 2026-10-04.
