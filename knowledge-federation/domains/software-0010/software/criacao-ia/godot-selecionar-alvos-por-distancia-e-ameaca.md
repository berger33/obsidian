---
id: software.criacao_ia.tranche02.000137
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

# Godot: selecionar alvos de combate por distância e ameaça

## Em uma frase
Um algoritmo de pontuação ponderada escolhe o alvo mais prioritário combinando distância, dano recebido e linha de visão.

## Por que importa
Atacar sempre o primeiro jogador avistado resulta em comportamentos ingênuos quando um atacante de longo alcance causa dano crítico.

## Como funciona
Mantenha uma lista de entidades percebidas e calcule um score para cada uma: `score = (peso_dist / dist) + (peso_dano * dano_recente)`. O NPC seleciona a entidade com maior pontuação acumulada.

## Exemplo
```gdscript
# Calculo de prioridade de alvo combinando distancia e ameaca
func evaluate_target_priority(target_data: Dictionary) -> float:
    var distance_score = 100.0 / max(global_position.distance_to(target_data.pos), 1.0)
    var threat_score = target_data.accumulated_damage * 2.5
    return distance_score + threat_score
```

## Limites e trade-offs
Pontuações muito voláteis podem fazer o NPC alternar de alvo a cada frame (efeito zigue-zague), sem completar ataques em nenhum deles.

## Como verificar
Aplique uma penalidade de troca de alvo (*hysteresis*) para exigir que um novo alvo supere significativamente o atual antes de trocar de foco.

## Conexões
- [[godot-desviar-de-obstaculos-com-raycast3d-multiplos]] — Veja também: Godot: desviar de obstáculos com múltiplos sensores RayCast3D.
- [[godot-sincronizar-ia-com-animationtree]] — Veja também: Godot: sincronizar máquina de estados com o nó AnimationTree.
- [[godot-calcular-cone-de-visao-com-area3d-e-dot-product]] — Conexão temática direta com godot-calcular-cone-de-visao-com-area3d-e-dot-product.
- [[unity-utility-ai-compor-fatores-de-saude-e-distancia]] — Conexão temática direta com unity-utility-ai-compor-fatores-de-saude-e-distancia.
- [[unreal-statetree-extrair-contexto-com-evaluators]] — Conexão temática direta com unreal-statetree-extrair-contexto-com-evaluators.

## Fontes
- [Godot Engine 4 Documentation — Advanced GDScript](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_advanced.html) — Manual oficial cobrindo padrões de scripts, nós virtuais, sinais e máquinas de estados hierárquicas. Consulta: 2026-10-04.
- [Godot Engine 4 Documentation — Advanced Vector Math](https://docs.godotengine.org/en/stable/tutorials/math/vectors_advanced.html) — Guia matemático cobrindo produtos escalares, forças de steering (seek/flee/pursuit) e orientação espacial. Consulta: 2026-10-04.
