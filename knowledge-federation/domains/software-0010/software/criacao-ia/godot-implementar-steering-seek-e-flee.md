---
id: software.criacao_ia.tranche02.000133
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

# Godot: implementar comportamentos de direção Seek e Flee

## Em uma frase
Os comportamentos de steering Seek e Flee calculam vetores de aceleração contínuos para perseguição e evasão suave de alvos.

## Por que importa
Mover entidades com teleporte ou interpolação linear simples resulta em movimentação mecânica e antinatural para inimigos e criaturas.

## Como funciona
Calcule a velocidade desejada subtraindo a posição atual da posição do alvo para Seek (ou o inverso para Flee), multiplicando pela velocidade máxima e aplicando uma força de steering limitada.

## Exemplo
```gdscript
# Calculo de steering behavior Seek em GDScript
func calculate_seek_force(target_pos: Vector3, current_vel: Vector3, max_speed: float, max_force: float) -> Vector3:
    var desired = (target_pos - global_position).normalized() * max_speed
    var steer = desired - current_vel
    return steer.limit_length(max_force)
```

## Limites e trade-offs
Forças de steering excessivamente altas geram oscilações bruscas ao redor do alvo quando o agente chega muito próximo da coordenada de parada.

## Como verificar
Aplique a força resultante na velocidade do `CharacterBody3D`, chame `move_and_slide()` e observe se a trajetória de aproximação faz curvas suaves.

## Conexões
- [[godot-desacoplar-transicoes-com-sinais]] — Veja também: Godot: desacoplar transições de estado de IA com sinais.
- [[godot-combinar-wander-e-pursuit-com-predicao]] — Veja também: Godot: combinar navegação Wander e Pursuit com predição.
- [[godot-desviar-de-obstaculos-com-raycast3d-multiplos]] — Conexão temática direta com godot-desviar-de-obstaculos-com-raycast3d-multiplos.
- [[godot-aplicar-velocidade-de-avoidance]] — Conexão temática direta com godot-aplicar-velocidade-de-avoidance.

## Fontes
- [Godot Engine 4 Documentation — Advanced GDScript](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_advanced.html) — Manual oficial cobrindo padrões de scripts, nós virtuais, sinais e máquinas de estados hierárquicas. Consulta: 2026-10-04.
- [Godot Engine 4 Documentation — Advanced Vector Math](https://docs.godotengine.org/en/stable/tutorials/math/vectors_advanced.html) — Guia matemático cobrindo produtos escalares, forças de steering (seek/flee/pursuit) e orientação espacial. Consulta: 2026-10-04.
