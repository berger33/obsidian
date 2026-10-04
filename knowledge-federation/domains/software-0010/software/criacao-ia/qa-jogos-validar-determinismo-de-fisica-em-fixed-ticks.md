---
id: software.criacao_ia.tranche02.000187
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

# QA de Física: validar determinismo em replays com passos de tempo fixos

## Em uma frase
A validação do determinismo da simulação garante que replays e previsões de netcode por rollback funcionem sem dessincronizações.

## Por que importa
Variações infinitesimais em cálculos de ponto flutuante entre clientes provocam divergências cumulativas graves em jogos multiplayer com netcode determinístico.

## Como funciona
Grave as entradas de controle de uma partida, execute o replay por 10.000 ticks com passo de tempo fixo (`FixedUpdate` / `_physics_process`) e valide se o checksum do estado final é idêntico em todas as execuções.

## Exemplo
```csharp
// Validando checksum de estado fisico para deteccao de desync
ulong stateChecksum = CalculatePhysicsChecksum();
Assert.AreEqual(expectedChecksum, stateChecksum, "Dessincronizacao de fisica detectada no tick 10000");
```

## Limites e trade-offs
Funções matemáticas que dependem de instruções específicas da CPU (ex.: FMA) podem gerar resultados ligeiramente diferentes em arquiteturas heterogêneas (x86 vs ARM).

## Como verificar
Execute o replay de 10.000 ticks duas vezes em plataformas distintas e compare o hash de estado final gravado em log.

## Conexões
- [[qa-jogos-detectar-desbalanceamento-por-metricas-de-partida]] — Veja também: Análise de Jogos: detectar desbalanceamento de armas e classes em logs.
- [[qa-jogos-automatizar-fluxos-de-ui-e-inventario]] — Veja também: QA de UI: automatizar navegação em telas de inventário e menus.
- [[godot-sincronizar-consultas-com-o-mapa]] — Conexão temática direta com godot-sincronizar-consultas-com-o-mapa.
- [[qa-jogos-encapsular-loop-em-ambiente-gymnasium]] — Conexão temática direta com qa-jogos-encapsular-loop-em-ambiente-gymnasium.
- [[qa-jogos-isolar-cenarios-de-regressao-de-gameplay]] — Conexão temática direta com qa-jogos-isolar-cenarios-de-regressao-de-gameplay.

## Fontes
- [Farama Gymnasium Documentation — Environment Creation](https://gymnasium.farama.org/tutorials/gymnasium_basics/environment_creation/) — Guia padrão para criação de ambientes de reinforcement learning (step, reset, action/observation spaces). Consulta: 2026-10-04.
- [Unity Test Framework Manual](https://docs.unity3d.com/Packages/com.unity.test-framework@1.4/manual/index.html) — Documentação de testes de integração playmode, asserções de física e execução automatizada em ci. Consulta: 2026-10-04.
