---
id: software.criacao_ia.tranche02.000136
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

# Godot: desviar de obstáculos com múltiplos sensores RayCast3D

## Em uma frase
Sensores RayCast3D múltiplos em leque permitem que agentes desviem de obstáculos dinâmicos em tempo real sem recalcular o mapa global.

## Por que importa
O recálculo frequente de malha de navegação em runtime é custoso em cenários com muitas caixas, barris e portas móveis.

## Como funciona
Configure um feixe central e sensores laterais angulados em 30 e 45 graus. Ao detectar colisão nos raios laterais, adicione uma força de repulsão perpendicular ao vetor de movimento.

## Exemplo
```gdscript
# Adicionando forca de repulsao lateral ao detectar obstaculo
func get_avoidance_force() -> Vector3:
    if left_ray.is_colliding():
        return global_transform.basis.x * avoidance_strength
    if right_ray.is_colliding():
        return -global_transform.basis.x * avoidance_strength
    return Vector3.ZERO
```

## Limites e trade-offs
Feixes de raio muito esparsos podem deixar passar quinas finas de malhas ou obstáculos menores que o diâmetro da cápsula do personagem.

## Como verificar
Ajuste o comprimento e o espaçamento angular dos raios para garantir que o agente não fique preso em esquinas durante perseguições.

## Conexões
- [[godot-calcular-cone-de-visao-com-area3d-e-dot-product]] — Veja também: Godot: calcular cone de visão com Area3D e produto escalar.
- [[godot-selecionar-alvos-por-distancia-e-ameaca]] — Veja também: Godot: selecionar alvos de combate por distância e ameaça.
- [[godot-implementar-steering-seek-e-flee]] — Conexão temática direta com godot-implementar-steering-seek-e-flee.
- [[godot-distinguir-caminho-de-evasao-local]] — Conexão temática direta com godot-distinguir-caminho-de-evasao-local.
- [[godot-depurar-vetores-de-ia-com-draw-line]] — Conexão temática direta com godot-depurar-vetores-de-ia-com-draw-line.

## Fontes
- [Godot Engine 4 Documentation — Advanced GDScript](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_advanced.html) — Manual oficial cobrindo padrões de scripts, nós virtuais, sinais e máquinas de estados hierárquicas. Consulta: 2026-10-04.
- [Godot Engine 4 Documentation — Advanced Vector Math](https://docs.godotengine.org/en/stable/tutorials/math/vectors_advanced.html) — Guia matemático cobrindo produtos escalares, forças de steering (seek/flee/pursuit) e orientação espacial. Consulta: 2026-10-04.
