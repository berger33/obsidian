---
id: software.criacao_ia.tranche02.000134
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

# Godot: combinar navegação Wander e Pursuit com predição

## Em uma frase
A combinação de deslocamento aleatório suave (Wander) e perseguição preditiva (Pursuit) enriquece a movimentação de patrulha e caça.

## Por que importa
Inimigos que perseguem apenas a posição atual do jogador parecem lentos e previsíveis em jogos de ação com movimentação rápida.

## Como funciona
O algoritmo de Pursuit calcula onde o alvo estará no futuro projetando a velocidade do alvo multiplicada pelo tempo de interceptação estimado, guiando o agente para esse ponto futuro.

## Exemplo
```gdscript
# Calculo de Pursuit preditivo com base na velocidade do alvo
func calculate_pursuit_target(target: CharacterBody3D, max_speed: float) -> Vector3:
    var distance = global_position.distance_to(target.global_position)
    var look_ahead = distance / max_speed
    return target.global_position + (target.velocity * look_ahead)
```

## Limites e trade-offs
Estimativas de predição muito longas fazem o agente perseguir paredes ou curvas que o alvo nunca percorrerá se mudar de direção repentinamente.

## Como verificar
Posicione um alvo móvel na cena e verifique se o agente corta a curva para interceptar o jogador em vez de segui-lo em linha reta atrasada.

## Conexões
- [[godot-implementar-steering-seek-e-flee]] — Veja também: Godot: implementar comportamentos de direção Seek e Flee.
- [[godot-calcular-cone-de-visao-com-area3d-e-dot-product]] — Veja também: Godot: calcular cone de visão com Area3D e produto escalar.
- [[godot-controlar-a-chegada-ao-waypoint]] — Conexão temática direta com godot-controlar-a-chegada-ao-waypoint.

## Fontes
- [Godot Engine 4 Documentation — Advanced GDScript](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_advanced.html) — Manual oficial cobrindo padrões de scripts, nós virtuais, sinais e máquinas de estados hierárquicas. Consulta: 2026-10-04.
- [Godot Engine 4 Documentation — Advanced Vector Math](https://docs.godotengine.org/en/stable/tutorials/math/vectors_advanced.html) — Guia matemático cobrindo produtos escalares, forças de steering (seek/flee/pursuit) e orientação espacial. Consulta: 2026-10-04.
