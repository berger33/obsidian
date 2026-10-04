---
id: software.criacao_ia.tranche02.000186
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

# Análise de Jogos: detectar desbalanceamento de armas e classes em logs

## Em uma frase
O processamento estatístico de logs de partidas simuladas identifica armas, feitiços e arquétipos que dominam desproporcionalmente o meta.

## Por que importa
Itens desbalanceados (*overpowered*) reduzem a variedade estratégica do jogo e prejudicam a experiência competitiva.

## Como funciona
Colete métricas de taxa de vitória (*win rate*), dano por segundo médio (DPS) e frequência de escolha (*pick rate*) em milhares de partidas simuladas por bots, disparando alertas quando uma arma ultrapassar margens saudáveis.

## Exemplo
```python
# Verificando desbalanceamento estatistico de classes
for class_name, stats in class_metrics.items():
    win_rate = stats['wins'] / stats['total_matches']
    if win_rate > 0.58 or win_rate < 0.42:
        print(f"Alerta de desbalanceamento: Classe {class_name} com Win Rate de {win_rate:.2%}")
```

## Limites e trade-offs
Bots de teste podem usar táticas diferentes de jogadores humanos experientes, gerando dados enviesados para mecânicas que exigem reflexos rápidos.

## Como verificar
Processe um lote de 500 logs de partidas e verifique se as taxas de vitória de cada classe se mantêm no intervalo de equilíbrio desejado.

## Conexões
- [[qa-jogos-simular-carga-de-servidor-com-bots-leves]] — Veja também: QA Multiplayer: simular carga de servidor instanciando bots sintéticos.
- [[qa-jogos-validar-determinismo-de-fisica-em-fixed-ticks]] — Veja também: QA de Física: validar determinismo em replays com passos de tempo fixos.
- [[telemetria-jogos-gerar-heatmaps-de-morte-e-posicao]] — Conexão temática direta com telemetria-jogos-gerar-heatmaps-de-morte-e-posicao.
- [[unity-utility-ai-avaliar-decisoes-com-curvas]] — Conexão temática direta com unity-utility-ai-avaliar-decisoes-com-curvas.
- [[responses-api-avaliar-geracao-com-exemplos]] — Conexão temática direta com responses-api-avaliar-geracao-com-exemplos.

## Fontes
- [Farama Gymnasium Documentation — Environment Creation](https://gymnasium.farama.org/tutorials/gymnasium_basics/environment_creation/) — Guia padrão para criação de ambientes de reinforcement learning (step, reset, action/observation spaces). Consulta: 2026-10-04.
- [Unity Test Framework Manual](https://docs.unity3d.com/Packages/com.unity.test-framework@1.4/manual/index.html) — Documentação de testes de integração playmode, asserções de física e execução automatizada em ci. Consulta: 2026-10-04.
