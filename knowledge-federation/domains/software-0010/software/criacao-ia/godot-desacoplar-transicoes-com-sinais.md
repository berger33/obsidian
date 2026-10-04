---
id: software.criacao_ia.tranche02.000132
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

# Godot: desacoplar transições de estado de IA com sinais

## Em uma frase
O desacoplamento via sinais permite que estados emitam intenções de mudança sem referenciar diretamente as classes dos estados vizinhos.

## Por que importa
Acoplar estados concretos entre si torna a IA rígida e dificulta a adição ou substituição de novos comportamentos no jogo.

## Como funciona
Os nós de estado emitem o sinal `transitioned(self, "NovoEstado")` quando uma condição é satisfeita. O controlador central da máquina intercepta o sinal, chama `exit()` no estado atual e ativa o próximo.

## Exemplo
```gdscript
# Emitindo intencao de transicao quando a saude fica critica
func physics_update(delta: float) -> void:
    if actor.health < 20:
        transitioned.emit(self, "FleeState")
```

## Limites e trade-offs
Sinais conectados incorretamente ou com nomes de estado tipados com erros de digitação causam falhas silenciosas em runtime.

## Como verificar
Monitore as emissões de sinal no depurador do Godot e certifique-se de que a máquina troca o nó ativo de maneira imediata e sem travamentos.

## Conexões
- [[godot-estruturar-maquina-de-estados-hierarquica]] — Veja também: Godot: estruturar máquina de estados hierárquica em GDScript.
- [[godot-implementar-steering-seek-e-flee]] — Veja também: Godot: implementar comportamentos de direção Seek e Flee.
- [[godot-selecionar-alvos-por-distancia-e-ameaca]] — Conexão temática direta com godot-selecionar-alvos-por-distancia-e-ameaca.
- [[unreal-statetree-estruturar-hierarquia-de-estados]] — Conexão temática direta com unreal-statetree-estruturar-hierarquia-de-estados.

## Fontes
- [Godot Engine 4 Documentation — Advanced GDScript](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_advanced.html) — Manual oficial cobrindo padrões de scripts, nós virtuais, sinais e máquinas de estados hierárquicas. Consulta: 2026-10-04.
- [Godot Engine 4 Documentation — Advanced Vector Math](https://docs.godotengine.org/en/stable/tutorials/math/vectors_advanced.html) — Guia matemático cobrindo produtos escalares, forças de steering (seek/flee/pursuit) e orientação espacial. Consulta: 2026-10-04.
