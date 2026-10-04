---
id: software.criacao_ia.tranche02.000184
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
fontes: ["https://gymnasium.farama.org/tutorials/gymnasium_basics/environment_creation/", "https://docs.unity3d.com/Packages/com.unity.test-framework@1.4/manual/index.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Telemetria de Jogos: gerar heatmaps de mortes e coordenadas de jogadores

## Em uma frase
A coleta de coordenadas de posicionamento e eventos de morte consolida mapas de calor que revelam gargalos de design no level design.

## Por que importa
Fases com picos abruptos de dificuldade ou trechos vazios frustram os jogadores sem que a equipe compreenda o motivo exato.

## Como funciona
Grave pontos tridimensionais `(x, y, z)` de mortes de bots e jogadores em um banco de dados analítico e projete uma textura de densidade sobre a visão superior (*top-down*) da fase no editor.

## Exemplo
```python
# Agregando coordenadas de morte em matriz de densidade para mapa de calor
import numpy as np

def generate_death_heatmap(death_coords: list[tuple[float, float]], grid_size: int = 100):
    heatmap, xedges, yedges = np.histogram2d(
        [c[0] for c in death_coords],
        [c[1] for c in death_coords],
        bins=grid_size
    )
    return heatmap
```

## Limites e trade-offs
Mapas de calor mostram onde os jogadores morrem, mas não explicam a causa raiz (se por falha de pulo, armadilha oculta ou inimigo desbalanceado).

## Como verificar
Gere a imagem de heatmap sobre a planta baixa da fase e confira visualmente a distribuição espacial dos pontos de concentração de mortes.

## Conexões
- [[qa-jogos-descobrir-colisoes-com-agentes-exploradores]] — Veja também: QA de Jogos: descobrir falhas de colisão com bots exploradores.
- [[qa-jogos-simular-carga-de-servidor-com-bots-leves]] — Veja também: QA Multiplayer: simular carga de servidor instanciando bots sintéticos.
- [[qa-jogos-detectar-desbalanceamento-por-metricas-de-partida]] — Conexão temática direta com qa-jogos-detectar-desbalanceamento-por-metricas-de-partida.
- [[godot-depurar-vetores-de-ia-com-draw-line]] — Conexão temática direta com godot-depurar-vetores-de-ia-com-draw-line.

## Fontes
- [Farama Gymnasium Documentation — Environment Creation](https://gymnasium.farama.org/tutorials/gymnasium_basics/environment_creation/) — Guia padrão para criação de ambientes de reinforcement learning (step, reset, action/observation spaces). Consulta: 2026-10-04.
- [Unity Test Framework Manual](https://docs.unity3d.com/Packages/com.unity.test-framework@1.4/manual/index.html) — Documentação de testes de integração playmode, asserções de física e execução automatizada em ci. Consulta: 2026-10-04.
