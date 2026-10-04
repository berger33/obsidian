---
id: software.criacao_ia.tranche02.000139
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

# Godot: propagar eventos sonoros para percepção auditiva de NPCs

## Em uma frase
A propagação de eventos de ruído permite que passos, tiros e explosões alertem NPCs mesmo fora de seu cone visual.

## Por que importa
Jogos de ação e furtividade exigem que os inimigos investiguem a origem de barulhos emitidos por ações do jogador no ambiente.

## Como funciona
Crie um singleton ou nó de gerenciamento de ruídos. Quando um disparo ocorre, o emissor notifica o sistema com a coordenada e intensidade do som, que alerta NPCs dentro do raio de audição.

## Exemplo
```gdscript
# Notificando o sistema de ruido ao disparar uma arma
func fire_weapon() -> void:
    NoiseManager.emit_noise(global_position, 25.0, "gunshot")
```

## Limites e trade-offs
Ruídos que atravessam paredes sólidas sem atenuação podem quebrar o realismo em cenários com múltiplas salas e portas fechadas.

## Como verificar
Adicione checagem de oclusão por raycast para atenuar a intensidade do som caso haja barreiras espessas entre o emissor e o ouvinte.

## Conexões
- [[godot-sincronizar-ia-com-animationtree]] — Veja também: Godot: sincronizar máquina de estados com o nó AnimationTree.
- [[godot-depurar-vetores-de-ia-com-draw-line]] — Veja também: Godot: depurar vetores e decisões de IA com funções _draw.
- [[godot-calcular-cone-de-visao-com-area3d-e-dot-product]] — Conexão temática direta com godot-calcular-cone-de-visao-com-area3d-e-dot-product.
- [[audio-ia-configurar-espacializacao-3d-e-atenuacao]] — Conexão temática direta com audio-ia-configurar-espacializacao-3d-e-atenuacao.

## Fontes
- [Godot Engine 4 Documentation — Advanced GDScript](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_advanced.html) — Manual oficial cobrindo padrões de scripts, nós virtuais, sinais e máquinas de estados hierárquicas. Consulta: 2026-10-04.
- [Godot Engine 4 Documentation — Advanced Vector Math](https://docs.godotengine.org/en/stable/tutorials/math/vectors_advanced.html) — Guia matemático cobrindo produtos escalares, forças de steering (seek/flee/pursuit) e orientação espacial. Consulta: 2026-10-04.
