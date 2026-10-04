---
id: software.criacao_ia.tranche02.000157
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

# Unreal Engine: simular multidões com arquitetura ECS MassEntity e Mass AI

## Em uma frase
O Mass AI utiliza uma arquitetura baseada em dados e entidades (ECS) para simular dezenas de milhares de agentes com altíssimo desempenho.

## Por que importa
Tentar simular centenas de atores clássicos baseados em `AActor` e `Character` sobrecarrega a CPU devido ao overhead de hierarquia e componentes pesados.

## Como funciona
Defina fragmentos de dados (`FMassFragment`) e processadores (`UMassProcessor`) que operam em arrays contínuos de memória na CPU, executando regras de locomoção e desvio de multidões de forma vetorizada.

## Exemplo
```cpp
// Exemplo de Fragmento de Dados leve para MassEntity
USTRUCT()
struct FMassCrowdAgentFragment : public FMassFragment
{
    GENERATED_BODY()
    FVector DesiredVelocity;
    float MaxSpeed;
};
```

## Limites e trade-offs
Agentes MassEntity não possuem malhas esqueléticas e colisões completas por padrão, exigindo sistemas de representação visual híbridos (*Mass Visualization*).

## Como verificar
Gere 5.000 agentes de teste na cena e monitore o frame time da CPU no painel `stat Mass` para verificar a estabilidade do processamento em lote.

## Conexões
- [[unreal-smart-objects-conectar-a-tarefas-do-statetree]] — Veja também: Unreal Engine: conectar navegação a Smart Objects via StateTree Tasks.
- [[unreal-gas-acionar-habilidades-pelo-ai-controller]] — Veja também: Unreal Engine: acionar Gameplay Abilities a partir de decisões do AIController.
- [[unreal-statetree-estruturar-hierarquia-de-estados]] — Conexão temática direta com unreal-statetree-estruturar-hierarquia-de-estados.
- [[qa-jogos-simular-carga-de-servidor-com-bots-leves]] — Conexão temática direta com qa-jogos-simular-carga-de-servidor-com-bots-leves.
- [[godot-aplicar-velocidade-de-avoidance]] — Conexão temática direta com godot-aplicar-velocidade-de-avoidance.

## Fontes
- [Unreal Engine 5 Documentation — StateTree](https://dev.epicgames.com/documentation/en-us/unreal-engine/statetree-in-unreal-engine) — Manual oficial do framework statetree, árvores de estados hierárquicas leves, evaluators e tasks. Consulta: 2026-10-04.
- [Unreal Engine 5 Documentation — Smart Objects](https://dev.epicgames.com/documentation/en-us/unreal-engine/smart-objects-in-unreal-engine) — Documentação cobrindo smart object definitions, slots de animação, subsistema de reserva e interação com ia. Consulta: 2026-10-04.
