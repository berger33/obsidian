---
id: software.testes.tranche07.000133
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
fontes: ["https://sre.google/sre-book/addressing-cascading-failures/", "https://kubernetes.io/docs/concepts/workloads/pods/probes/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Teste de timeout e circuit breaker de dependência", "Teste: Teste de timeout e circuit breaker de dependência"]
lote: software-testes-2000-0001
---

# Teste de timeout e circuit breaker de dependência

## Em uma frase
Simule timeout e falha de serviço dependente para confirmar orçamento de espera, abertura do circuit breaker e recuperação controlada.

## Por que importa
Chamadas bloqueadas podem prender threads, conexões e memória, transformando falha localizada em esgotamento de recursos no chamador.

## Como funciona
No ambiente isolado, simule resposta lenta, conexão recusada e erro de aplicação separadamente. Confira deadline end-to-end, estados aberto/meio-aberto/fechado conforme implementação, fallback e recuperação sem tempestade de requisições.

## Exemplo
Faça um serviço de catálogo exceder o timeout do chamador; confirme resposta dentro do deadline, ausência de chamadas contínuas enquanto o circuito está aberto e uma sondagem limitada após o intervalo.

## Limites e trade-offs
Circuit breakers variam por biblioteca e podem não existir em todo serviço. Testes baseados em sleeps fixos são frágeis; não introduza falha em dependência compartilhada sem coordenar o impacto.

## Como verificar
Registre tempos e contagem de chamadas, observe recursos do chamador e prove transições de estado com relógio controlado ou tolerância definida; restaure dependência ao fim.

## Conexões
- [[timeouts-retries-backoff-jitter]] — aprofundamento relacionado.
- [[chaos-experiments-steady-state-blast-radius]] — aprofundamento relacionado.

## Fontes
- [Google SRE — Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/) — sobrecarga e falhas de dependência podem amplificar-se em cascata; consultado em 2026-10-01.
- [Kubernetes — Liveness, Readiness, and Startup Probes](https://kubernetes.io/docs/concepts/workloads/pods/probes/) — propósito distinto de startup, liveness e readiness e riscos de configuração; consultado em 2026-10-01.
