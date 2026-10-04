---
id: software.testes.tranche07.000139
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
fontes: ["https://kubernetes.io/docs/concepts/workloads/pods/probes/", "https://sre.google/sre-book/addressing-cascading-failures/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Teste de startup, liveness e readiness probes", "Teste: Teste de startup, liveness e readiness probes"]
lote: software-testes-2000-0001
---

# Teste de startup, liveness e readiness probes

## Em uma frase
Teste cada probe segundo seu propósito: permitir inicialização, reiniciar processo travado ou retirar temporariamente tráfego de instância não pronta.

## Por que importa
Combinar sinais diferentes em uma probe pode causar reinícios desnecessários ou enviar tráfego a uma instância incapaz de atender.

## Como funciona
Simule inicialização lenta, deadlock isolado e indisponibilidade temporária; confirme thresholds e efeitos esperados. Readiness deve controlar elegibilidade de tráfego, liveness deve indicar falha irrecuperável, e startup pode postergar as outras até inicialização.

## Exemplo
Faça uma instância demorar para carregar cache e depois responda; ela não deve reiniciar repetidamente antes da startup probe passar. Em seguida simule estado não pronto e valide retirada de endpoints sem reinício automático.

## Limites e trade-offs
Liveness mal configurada pode aumentar falhas em cascata sob carga; readiness dependente de serviço externo pode retirar todas as réplicas. Use probes de baixo custo e teste em carga.

## Como verificar
Observe eventos do kubelet, reinícios, EndpointSlices e tráfego; injete uma falha por vez e prove que cada probe produz a ação documentada, inclusive recuperação.

## Conexões
- [[probes-kubernetes-liveness-readiness-startup]] — aprofundamento relacionado.
- [[testes-kubernetes-rolling-update-disponibilidade]] — aprofundamento relacionado.

## Fontes
- [Kubernetes — Liveness, Readiness, and Startup Probes](https://kubernetes.io/docs/concepts/workloads/pods/probes/) — propósito distinto de startup, liveness e readiness e riscos de configuração; consultado em 2026-10-01.
- [Google SRE — Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/) — sobrecarga e falhas de dependência podem amplificar-se em cascata; consultado em 2026-10-01.
