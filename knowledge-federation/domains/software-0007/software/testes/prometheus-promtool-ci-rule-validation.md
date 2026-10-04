---
id: software.testes.tranche08.000239
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
fontes: ["https://prometheus.io/docs/prometheus/latest/configuration/unit_testing_rules/", "https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Prometheus: executar promtool no CI para regras versionadas

## Em uma frase
Execute validação sintática e testes de regras no mesmo pipeline que protege alterações de dashboards e alertas.

## Por que importa
Consulta inválida ou expectativa quebrada pode ser detectada antes do deploy, reduzindo risco de regressão operacional.

## Como funciona
Inclua versão de promtool compatível, valide arquivos de regra e execute arquivos de teste declarados; publique falha com contexto suficiente.

## Exemplo
Pull request altera recording rule; job executa promtool check e test sobre fixtures da regra antes de liberar merge.

## Limites e trade-offs
CI valida artefato local, não estado do servidor, roteamento ou silenciamento configurado após deploy.

## Como verificar
Introduza regra inválida e cenário esperado incompatível para confirmar falhas; registre versão da ferramenta e evite depender de binário flutuante.

## Conexões
- [[prometheus-alert-rule-unit-test-input-series]] — Veja também: Prometheus: testar alert rules com séries controladas.
- [[prometheus-recording-rule-expression-output]] — Veja também: Prometheus: testar recording rules e série resultante.

## Fontes
- [Prometheus — Unit testing for rules](https://prometheus.io/docs/prometheus/latest/configuration/unit_testing_rules/) — promtool, séries de entrada e assertions de PromQL/alertas; consultado em 2026-10-02.
- [Prometheus — Recording rules](https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/) — avaliação e regras de gravação; consultado em 2026-10-02.
