---
id: software.testes.tranche10.000419
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-10.md"
fontes: ["https://grafana.com/docs/k6/latest/using-k6-browser/", "https://grafana.com/docs/k6/latest/using-k6/scenarios/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# k6: complementar teste de protocolo com teste de browser

## Em uma frase
O módulo browser do k6 combina automação de navegador com métricas de desempenho frontend para jornadas sintéticas.

## Por que importa
Um teste de carga útil precisa representar o modelo de chegada e transformar métricas em critérios de decisão explícitos. Uma carga de protocolo não reproduz renderização, interatividade e métricas específicas do navegador, enquanto o browser runner consome mais recursos.

## Como funciona
Modele cenários e executors a partir do comportamento esperado, segmente métricas com tags e use thresholds para declarar resultados. Use jornadas de browser para observar experiência frontend e teste de protocolo para escalar tráfego HTTP; relacione os resultados sem tratá-los como a mesma métrica.

## Exemplo
Um cenário browser sintético mede carregamento e interação de checkout; um cenário HTTP separado pressiona a API, e ambos são analisados junto a telemetria real quando disponível.

## Limites e trade-offs
Resultados dependem do perfil de workload, ambiente, capacidade geradora e métricas escolhidas; exemplos de thresholds não são SLOs universais. Métricas de browser são produzidas por um teste sintético, não por usuários reais; esse runner é mais custoso e não substitui carga de protocolo nem RUM.

## Como verificar
Identifique métricas frontend e de protocolo separadamente, valide dependências do browser e compare a jornada sintética com telemetria de usuários reais se a pergunta exigir RUM.

## Conexões
- [[k6-sleep-pacing-representar-think-time]] — Veja também: k6: modelar think time em vez de adicionar pausas arbitrárias.

## Fontes
- [Grafana k6 — Browser testing](https://grafana.com/docs/k6/latest/using-k6-browser/) — automação browser-level e métricas frontend produzidas por testes sintéticos; consultado em 2026-10-02.
- [Grafana k6 — Scenarios](https://grafana.com/docs/k6/latest/using-k6/scenarios/) — execução de workloads nomeados com executors e parâmetros; consultado em 2026-10-02.
