---
id: software.testes.tranche07.000101
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
fontes: ["https://grafana.com/docs/k6/latest/using-k6/checks/", "https://grafana.com/docs/k6/latest/testing-guides/api-load-testing/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Correção funcional durante testes de carga", "Teste: Correção funcional durante testes de carga"]
lote: software-testes-2000-0001
---

# Correção funcional durante testes de carga

## Em uma frase
Verifique respostas e invariantes funcionais enquanto o sistema atende carga, sem confundir sucesso HTTP isolado com correção do fluxo.

## Por que importa
Um serviço pode manter latência aceitável e ainda devolver conteúdo incorreto, perder gravações ou misturar dados entre usuários sob concorrência.

## Como funciona
Inclua checks sobre status, campos essenciais, valores e efeitos observáveis; acompanhe em separado métricas de performance. Em k6, um check com falha é registrado, mas não encerra automaticamente a execução: thresholds sobre a métrica de checks podem transformar a taxa de falha em gate.

## Exemplo
Durante um fluxo de reserva, confirme que cada resposta corresponde ao item e ao usuário sem duplicar a reserva; ao final, reconcilie o número de operações aceitas com os registros do ambiente de teste.

## Limites e trade-offs
Checks excessivamente detalhados aumentam custo e podem deixar o gerador de carga como gargalo. Não inclua dados pessoais reais, e não trate um status 200 como prova suficiente de sucesso funcional.

## Como verificar
Injete uma resposta deliberadamente inválida em staging e confirme que o check acusa a falha e que o threshold configurado faz o job terminar como reprovado; valide também a taxa de checks falhos no relatório.

## Conexões
- [[schema-based-api-testing-schemathesis-openapi]] — aprofundamento relacionado.
- [[test-oracles-resultados-esperados]] — aprofundamento relacionado.

## Fontes
- [Grafana k6 — Checks](https://grafana.com/docs/k6/latest/using-k6/checks/) — checks validam condições e precisam de thresholds para falhar o ensaio; consultado em 2026-10-01.
- [Grafana k6 — API load testing](https://grafana.com/docs/k6/latest/testing-guides/api-load-testing/) — objectivos, desenho de carga e famílias de ensaio para APIs; consultado em 2026-10-01.
