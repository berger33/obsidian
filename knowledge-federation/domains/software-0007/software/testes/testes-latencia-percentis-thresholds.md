---
id: software.testes.tranche07.000100
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
fontes: ["https://grafana.com/docs/k6/latest/using-k6/thresholds/", "https://grafana.com/docs/k6/latest/testing-guides/api-load-testing/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Thresholds de latência por percentil", "Teste: Thresholds de latência por percentil"]
lote: software-testes-2000-0001
---

# Thresholds de latência por percentil

## Em uma frase
Defina limites de desempenho sobre percentis de latência, taxa de erros e objetivos de serviço, em vez de depender apenas da média.

## Por que importa
A média pode permanecer aceitável enquanto uma fração de usuários sofre respostas muito lentas; a cauda da distribuição é relevante para fluxos críticos e SLOs.

## Como funciona
Escolha métricas e limites antes da execução e amarre-os à experiência esperada. Em k6, thresholds expressam critérios pass/fail sobre métricas; p95 ou p99 devem ser interpretados junto com taxa de erro, throughput e quantidade de amostras.

## Exemplo
Em um checkout, um perfil pode exigir p95 abaixo de 500 ms, p99 abaixo de 1,2 s e menos de 1% de respostas com falha, desde que esses números venham do SLO do produto e do perfil representativo.

## Limites e trade-offs
Percentis dependem de volume de amostras, mistura de endpoints, aquecimento e duração. Valores copiados de outro serviço ou de uma execução curta não constituem SLO universal.

## Como verificar
Confira que a ferramenta falha quando qualquer threshold obrigatório é violado, que as métricas correspondem ao endpoint relevante e que os relatórios preservam versão, ambiente e perfil de carga.

## Conexões
- [[performance-testing-modelagem-carga]] — aprofundamento relacionado.
- [[regression-test-prioritization-risco-impacto]] — aprofundamento relacionado.

## Fontes
- [Grafana k6 — Thresholds](https://grafana.com/docs/k6/latest/using-k6/thresholds/) — critérios pass/fail associados a métricas e SLOs; consultado em 2026-10-01.
- [Grafana k6 — API load testing](https://grafana.com/docs/k6/latest/testing-guides/api-load-testing/) — objetivos, desenho de carga e famílias de ensaio para APIs; consultado em 2026-10-01.
