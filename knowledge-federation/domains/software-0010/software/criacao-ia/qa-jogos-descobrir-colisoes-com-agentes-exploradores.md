---
id: software.criacao_ia.tranche02.000183
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

# QA de Jogos: descobrir falhas de colisão com bots exploradores

## Em uma frase
Agentes de aprendizado orientados por novidade exploram todos os cantos do mapa para identificar fendas na geometria e colisores vazados.

## Por que importa
Jogadores encontram atalhos ilegais e quedas fora do mapa (*out of bounds*) que passam despercebidos por testadores humanos.

## Como funciona
Treine agentes utilizando recompensas baseadas em bônus de curiosidade (RND / ICM). Quando o agente atinge posições fora do volume delimitador válido do mapa, registre o evento como falha crítica de colisão.

## Exemplo
```python
# Registrando anomalia de colisao quando o agente sai dos limites do mapa
if current_pos.y < -10.0 or not map_bounding_box.contains(current_pos):
    log_bug_report("Out of bounds detectado", current_pos, agent_trajectory)
```

## Limites e trade-offs
Agentes exploradores podem despender tempo excessivo travados em áreas com portas trancadas se não receberem dicas de navegação.

## Como verificar
Inicie uma campanha de 1.000 episódios de exploração e inspecione o arquivo de log para checar se algum ponto de saída inválida foi registrado.

## Conexões
- [[qa-jogos-encapsular-loop-em-ambiente-gymnasium]] — Veja também: IA de Testes: encapsular loop de gameplay como ambiente Farama Gymnasium.
- [[telemetria-jogos-gerar-heatmaps-de-morte-e-posicao]] — Veja também: Telemetria de Jogos: gerar heatmaps de mortes e coordenadas de jogadores.
- [[godot-preparar-malha-de-navegacao]] — Conexão temática direta com godot-preparar-malha-de-navegacao.

## Fontes
- [Farama Gymnasium Documentation — Environment Creation](https://gymnasium.farama.org/tutorials/gymnasium_basics/environment_creation/) — Guia padrão para criação de ambientes de reinforcement learning (step, reset, action/observation spaces). Consulta: 2026-10-04.
- [Unity Test Framework Manual](https://docs.unity3d.com/Packages/com.unity.test-framework@1.4/manual/index.html) — Documentação de testes de integração playmode, asserções de física e execução automatizada em ci. Consulta: 2026-10-04.
