---
id: software.criacao_ia.tranche02.000138
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

# Godot: sincronizar máquina de estados com o nó AnimationTree

## Em uma frase
O nó AnimationTree permite realizar blend suave entre animações de locomoção e ações disparadas pela lógica de IA.

## Por que importa
Alterar animações diretamente via `AnimationPlayer.play()` causa cortes bruscos de pose e quebra o realismo visual dos personagens.

## Como funciona
Utilize uma `AnimationNodeStateMachine` dentro do `AnimationTree` e atualize os parâmetros de velocidade linear, direção e gatilhos de ataque através de código GDScript no estado correspondente.

## Exemplo
```gdscript
# Sincronizando velocidade e transicao de animacao no AnimationTree
func update_animation_parameters(current_vel: Vector3) -> void:
    var speed = current_vel.length()
    anim_tree.set("parameters/locomotion/blend_position", speed)
    if is_attacking:
        anim_tree.set("parameters/conditions/attack", true)
```

## Limites e trade-offs
Parâmetros com caminhos de string incorretos no `set()` falham silenciosamente se o nó de animação for renomeado no editor.

## Como verificar
Teste transições de marcha rápida para ataque e confira se a mesclagem de poses (cross-fade) ocorre suavemente durante a movimentação.

## Conexões
- [[godot-selecionar-alvos-por-distancia-e-ameaca]] — Veja também: Godot: selecionar alvos de combate por distância e ameaça.
- [[godot-propagar-eventos-sonoros-para-audicao-de-npcs]] — Veja também: Godot: propagar eventos sonoros para percepção auditiva de NPCs.
- [[godot-estruturar-maquina-de-estados-hierarquica]] — Conexão temática direta com godot-estruturar-maquina-de-estados-hierarquica.
- [[unity-playablegraph-mesclar-animacoes-procedurais]] — Conexão temática direta com unity-playablegraph-mesclar-animacoes-procedurais.
- [[blender-organizar-clips-como-actions]] — Conexão temática direta com blender-organizar-clips-como-actions.

## Fontes
- [Godot Engine 4 Documentation — Advanced GDScript](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_advanced.html) — Manual oficial cobrindo padrões de scripts, nós virtuais, sinais e máquinas de estados hierárquicas. Consulta: 2026-10-04.
- [Godot Engine 4 Documentation — Advanced Vector Math](https://docs.godotengine.org/en/stable/tutorials/math/vectors_advanced.html) — Guia matemático cobrindo produtos escalares, forças de steering (seek/flee/pursuit) e orientação espacial. Consulta: 2026-10-04.
