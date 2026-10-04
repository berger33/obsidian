---
id: software.testes.tranche08.000237
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-08.md"
fontes: ["https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/", "https://prometheus.io/docs/prometheus/latest/configuration/unit_testing_rules/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Prometheus: separar condição saudável de ausência de telemetria

## Em uma frase
Crie cenário para falha de scrape ou série ausente em separado do valor funcional que a aplicação publica.

## Por que importa
Um alerta baseado apenas em valor ruim pode ficar inativo quando justamente a métrica desaparece.

## Como funciona
Teste regra de serviço e regra de disponibilidade da métrica, contemplando ausência de target, série stale e valor válido conforme modelo de scrape.

## Exemplo
Endpoint de negócio reporta zero erros quando ativo; alerta distinto detecta que target deixou de ser raspado por tempo configurado.

## Limites e trade-offs
As regras dependem de discovery e scrape configuration; teste isolado de expressão não comprova que target foi descoberto.

## Como verificar
Remova série e target em ambiente de teste, valide comportamento esperado e inspecione `up` e alerta de aplicação separadamente.

## Conexões
- [[prometheus-alert-rule-unit-test-input-series]] — Veja também: Prometheus: testar alert rules com séries controladas.
- [[prometheus-vector-vazio-vs-zero]] — Veja também: Prometheus: diferenciar vetor vazio de valor zero.

## Fontes
- [Prometheus — Alerting rules](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/) — expressões, for duration, labels e annotations de alertas; consultado em 2026-10-02.
- [Prometheus — Unit testing for rules](https://prometheus.io/docs/prometheus/latest/configuration/unit_testing_rules/) — promtool, séries de entrada e assertions de PromQL/alertas; consultado em 2026-10-02.
