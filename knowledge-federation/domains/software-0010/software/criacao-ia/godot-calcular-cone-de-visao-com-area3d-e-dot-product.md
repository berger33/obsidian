---
id: software.criacao_ia.tranche02.000135
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

# Godot: calcular cone de visão com Area3D e produto escalar

## Em uma frase
A detecção por cone de visão combina um gatilho de proximidade Area3D com cálculo de produto escalar vetorial (dot product).

## Por que importa
Verificar visibilidade apenas por distância permite que NPCs enxerguem alvos localizados completamente atrás de suas costas.

## Como funciona
Utilize uma `Area3D` para filtrar alvos dentro do raio máximo e use `Vector3.dot()` entre o vetor frontal do NPC e a direção até o alvo para testar o ângulo de visão.

## Exemplo
```gdscript
# Checagem de angulo de visao com produto escalar no Godot 4
func is_target_in_sight(target_pos: Vector3, view_angle_deg: float) -> bool:
    var to_target = (target_pos - global_position).normalized()
    var forward = -global_transform.basis.z.normalized()
    var angle_cos = cos(deg_to_rad(view_angle_deg * 0.5))
    return forward.dot(to_target) >= angle_cos
```

## Limites e trade-offs
O cálculo angular indica que o alvo está no campo de visão, mas não descarta a presença de paredes sólidas entre os dois personagens.

## Como verificar
Dispare um `RayCast3D` em direção ao alvo após a confirmação angular para checar oclusões geométricas do cenário.

## Conexões
- [[godot-combinar-wander-e-pursuit-com-predicao]] — Veja também: Godot: combinar navegação Wander e Pursuit com predição.
- [[godot-desviar-de-obstaculos-com-raycast3d-multiplos]] — Veja também: Godot: desviar de obstáculos com múltiplos sensores RayCast3D.
- [[godot-selecionar-alvos-por-distancia-e-ameaca]] — Conexão temática direta com godot-selecionar-alvos-por-distancia-e-ameaca.
- [[unity-animation-rigging-orientar-olhar-com-multi-aim]] — Conexão temática direta com unity-animation-rigging-orientar-olhar-com-multi-aim.

## Fontes
- [Godot Engine 4 Documentation — Advanced GDScript](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_advanced.html) — Manual oficial cobrindo padrões de scripts, nós virtuais, sinais e máquinas de estados hierárquicas. Consulta: 2026-10-04.
- [Godot Engine 4 Documentation — Advanced Vector Math](https://docs.godotengine.org/en/stable/tutorials/math/vectors_advanced.html) — Guia matemático cobrindo produtos escalares, forças de steering (seek/flee/pursuit) e orientação espacial. Consulta: 2026-10-04.
