---
id: software.testes.tranche07.000103
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
fontes: ["https://grafana.com/docs/k6/latest/testing-guides/test-types/smoke-testing/", "https://grafana.com/docs/k6/latest/testing-guides/api-load-testing/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Smoke test de API com carga mínima", "Teste: Smoke test de API com carga mínima"]
lote: software-testes-2000-0001
---

# Smoke test de API com carga mínima

## Em uma frase
Use uma execução curta e de baixa carga para confirmar que o script, os endpoints principais e o ambiente respondem antes de testes maiores.

## Por que importa
Um smoke test detecta configuração quebrada, credenciais ausentes, dados inválidos ou indisponibilidade básica com baixo risco de consumir recursos.

## Como funciona
Mantenha poucos usuários, duração curta e uma seleção de operações representativas. Verifique conectividade, resposta funcional e dependências necessárias; trate o ensaio como pré-condição para carga mais intensa, não como medição de capacidade.

## Exemplo
Antes de um stress test em staging, rode um fluxo de autenticação e consulta com carga mínima. Se o endpoint falha ou o script não valida o corpo esperado, interrompa a sequência e corrija a preparação.

## Limites e trade-offs
Passar com carga mínima não demonstra comportamento em pico, latência de cauda ou estabilidade prolongada. O termo smoke não define uma configuração numérica universal.

## Como verificar
Confirme que o teste termina dentro do limite previsto, todos os checks essenciais passam e os dados preparados existem; inclua uma falha de configuração conhecida para provar que o gate a detecta.

## Conexões
- [[performance-testing-modelagem-carga]] — aprofundamento relacionado.
- [[test-planning-objetivos-escopo-comunicacao]] — aprofundamento relacionado.

## Fontes
- [Grafana k6 — Smoke testing](https://grafana.com/docs/k6/latest/testing-guides/test-types/smoke-testing/) — carga pequena para verificar se o sistema funciona no cenário básico; consultado em 2026-10-01.
- [Grafana k6 — API load testing](https://grafana.com/docs/k6/latest/testing-guides/api-load-testing/) — objectivos, desenho de carga e famílias de ensaio para APIs; consultado em 2026-10-01.
