---
id: software.criacao_ia.tranche02.000160
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

# Unreal Engine: inspecionar transições de IA com o Gameplay Debugger

## Em uma frase
O Gameplay Debugger da Unreal Engine exibe na tela o estado ativo de árvores de decisão, slots de Smart Objects e variáveis do Blackboard.

## Por que importa
Inspecionar os valores internos dos agentes diretamente no mundo tridimensional agiliza o diagnóstico de travamentos e transições erráticas.

## Como funciona
Pressione a tecla apóstrofo (') ou configure o atalho do `GameplayDebugger` durante o jogo para inspecionar o Pawn sob a mira, visualizando o histórico de tarefas do StateTree e percepções ativas.

## Exemplo
```text
// Painel visual do Gameplay Debugger na Unreal Engine
[Gameplay Debugger Category: AI]
StateTree State: Combat / Engage
Current Task: MoveToTarget (Running)
Smart Object Slot: None
Target Actor: BP_PlayerCharacter (Dist: 450cm)
```

## Limites e trade-offs
A renderização de muitas categorias do depurador pode poluir a visão da cena durante sessões de teste de combate intenso.

## Como verificar
Acione o depurador com o atalho oficial durante o modo Play e verifique se as informações de StateTree e percepção são atualizadas a cada tick.

## Conexões
- [[unreal-motion-warping-alinhar-interacoes-fisicas]] — Veja também: Unreal Engine: alinhar pontos de contato e saltos com Motion Warping.
- [[unreal-statetree-estruturar-hierarquia-de-estados]] — Conexão temática direta com unreal-statetree-estruturar-hierarquia-de-estados.
- [[unity-ia-visualizar-decisoes-com-gizmos-de-cena]] — Conexão temática direta com unity-ia-visualizar-decisoes-com-gizmos-de-cena.
- [[godot-depurar-vetores-de-ia-com-draw-line]] — Conexão temática direta com godot-depurar-vetores-de-ia-com-draw-line.

## Fontes
- [Unreal Engine 5 Documentation — StateTree](https://dev.epicgames.com/documentation/en-us/unreal-engine/statetree-in-unreal-engine) — Manual oficial do framework statetree, árvores de estados hierárquicas leves, evaluators e tasks. Consulta: 2026-10-04.
- [Unreal Engine 5 Documentation — Smart Objects](https://dev.epicgames.com/documentation/en-us/unreal-engine/smart-objects-in-unreal-engine) — Documentação cobrindo smart object definitions, slots de animação, subsistema de reserva e interação com ia. Consulta: 2026-10-04.
