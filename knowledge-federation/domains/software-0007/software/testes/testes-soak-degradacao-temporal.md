---
id: software.testes.tranche07.000107
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-07.md"
fontes: ["https://grafana.com/docs/k6/latest/testing-guides/test-types/soak-testing/", "https://grafana.com/docs/k6/latest/testing-guides/automated-performance-testing/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Soak test para degradação ao longo do tempo", "Teste: Soak test para degradação ao longo do tempo"]
lote: software-testes-2000-0001
---

# Soak test para degradação ao longo do tempo

## Em uma frase
Mantenha uma carga representativa por período prolongado para procurar degradação lenta que testes curtos não revelam.

## Por que importa
Vazamento de memória, crescimento de filas, acúmulo de conexões e rotinas periódicas podem aparecer somente após horas ou ciclos repetidos.

## Como funciona
Defina duração ligada ao risco, perfil de carga, janela de aquecimento e coleta de séries temporais. Observe tendências em uso de memória, GC, pools, espaço, latência, erros e operações periódicas; compare início e fim sob condições equivalentes.

## Exemplo
Mantenha uma API em carga normal por um turno de teste e verifique se a memória retorna ao patamar esperado após picos e se as conexões disponíveis não diminuem progressivamente.

## Limites e trade-offs
Duração longa não garante cobertura de todos os ciclos, e deriva ambiental pode confundir a interpretação. Use ambiente estável e confirme que o gerador não satura primeiro.

## Como verificar
Analise tendências e mudanças de distribuição, não apenas média final; registre reinícios, tarefas programadas e incidentes do ambiente para separar causas externas de regressões.

## Conexões
- [[performance-testing-modelagem-carga]] — aprofundamento relacionado.
- [[testes-flaky-determinismo]] — aprofundamento relacionado.

## Fontes
- [Grafana k6 — Soak testing](https://grafana.com/docs/k6/latest/testing-guides/test-types/soak-testing/) — degradação ao longo de uma duração prolongada; consultado em 2026-10-01.
- [Grafana k6 — Automated performance testing](https://grafana.com/docs/k6/latest/testing-guides/automated-performance-testing/) — uso repetível de testes de desempenho ao longo do ciclo de entrega; consultado em 2026-10-01.
