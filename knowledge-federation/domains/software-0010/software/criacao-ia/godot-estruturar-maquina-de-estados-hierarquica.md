---
id: software.criacao_ia.tranche02.000131
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
fontes: ["https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_advanced.html", "https://docs.godotengine.org/en/stable/tutorials/math/vectors_advanced.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Godot: estruturar máquina de estados hierárquica em GDScript

## Em uma frase
A máquina de estados hierárquica (HFSM) organiza comportamentos complexos de IA em árvores de nós especializados no Godot.

## Por que importa
Agrupar sub-estados dentro de macro-estados (ex.: Patrulha, Combate, Fuga) evita a explosão combinatória de transições em NPCs sofisticados.

## Como funciona
Crie uma estrutura de nós onde a raiz da HFSM delega o ciclo `_physics_process` para o nó de estado ativo. Cada estado estende uma classe base `State` implementando métodos virtuais `enter()`, `exit()` e `physics_update()`.

## Exemplo
```gdscript
# Exemplo de classe base de estado em GDScript no Godot 4
class_name EnemyState
extends Node

signal transitioned(new_state_name: String)

func enter() -> void:
    pass

func exit() -> void:
    pass

func physics_update(_delta: float) -> void:
    pass
```

## Limites e trade-offs
Estruturas hierárquicas profundas demandam gerenciamento rigoroso de sinais para evitar vazamento de memória ou transições duplicadas.

## Como verificar
Instancie a máquina de estados em um CharacterBody3D, simule gatilhos de transição e confirme nos logs a ordem correta de execução dos métodos de entrada e saída.

## Conexões
- [[godot-desacoplar-transicoes-com-sinais]] — Veja também: Godot: desacoplar transições de estado de IA com sinais.
- [[godot-sincronizar-ia-com-animationtree]] — Conexão temática direta com godot-sincronizar-ia-com-animationtree.
- [[unity-utility-ai-avaliar-decisoes-com-curvas]] — Conexão temática direta com unity-utility-ai-avaliar-decisoes-com-curvas.

## Fontes
- [Godot Engine 4 Documentation — Advanced GDScript](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_advanced.html) — Manual oficial cobrindo padrões de scripts, nós virtuais, sinais e máquinas de estados hierárquicas. Consulta: 2026-10-04.
- [Godot Engine 4 Documentation — Advanced Vector Math](https://docs.godotengine.org/en/stable/tutorials/math/vectors_advanced.html) — Guia matemático cobrindo produtos escalares, forças de steering (seek/flee/pursuit) e orientação espacial. Consulta: 2026-10-04.
