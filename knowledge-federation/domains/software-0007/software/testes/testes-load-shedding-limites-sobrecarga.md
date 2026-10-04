---
id: software.testes.tranche07.000131
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
fontes: ["https://sre.google/sre-book/addressing-cascading-failures/", "https://grafana.com/docs/k6/latest/testing-guides/api-load-testing/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Teste de load shedding e rejeição controlada", "Teste: Teste de load shedding e rejeição controlada"]
lote: software-testes-2000-0001
---

# Teste de load shedding e rejeição controlada

## Em uma frase
Examine se, sob sobrecarga, o sistema limita trabalho e rejeita solicitações de forma controlada antes de comprometer todos os recursos.

## Por que importa
Rejeição antecipada e limites de fila podem preservar operações prioritárias e reduzir falhas em cascata quando a capacidade disponível é menor que a demanda.

## Como funciona
Defina limites, classes de prioridade e respostas esperadas. Eleve carga em laboratório, observe queue depth, latência, erros e operações úteis; confira que pedidos recusados não ficam silenciosamente aceitos e que o sistema recupera ao cair a demanda.

## Exemplo
Sob pico simulado, o serviço recusa nova operação de baixa prioridade com resposta documentada, enquanto operações críticas completam e a fila permanece limitada; depois confirme que tráfego normal volta a ser atendido.

## Limites e trade-offs
Limite inadequado pode rejeitar trabalho essencial ou deslocar o gargalo para outro sistema. HTTP 429 não é a única estratégia e cada domínio precisa definir semântica de retry e prioridade.

## Como verificar
Registre taxa de rejeição por classe, duração de fila, throughput útil e recuperação; teste limites vizinhos e valide que clientes não repetem agressivamente a recusa.

## Conexões
- [[testes-spike-picos-abruptos]] — aprofundamento relacionado.
- [[timeouts-retries-backoff-jitter]] — aprofundamento relacionado.

## Fontes
- [Google SRE — Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/) — sobrecarga e falhas de dependência podem amplificar-se em cascata; consultado em 2026-10-01.
- [Grafana k6 — API load testing](https://grafana.com/docs/k6/latest/testing-guides/api-load-testing/) — objectivos, desenho de carga e famílias de ensaio para APIs; consultado em 2026-10-01.
