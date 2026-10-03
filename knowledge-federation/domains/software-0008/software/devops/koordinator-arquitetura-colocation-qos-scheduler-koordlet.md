---
id: software.devops.tranche16.001561
tipo: tecnica
dominio: software
subdominio: devops
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-16.md"
fontes: ["https://raw.githubusercontent.com/koordinator-sh/koordinator/main/README.md", "https://koordinator.sh/docs/architecture/overview/", "https://github.com/koordinator-sh/koordinator"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Koordinator: arquitetura de co-localização híbrida baseada em QoS (`koord-scheduler`, `koord-manager` e `koordlet`)

## Em uma frase
O Koordinator (projeto CNCF Sandbox, escrito em Go) é um sistema de agendamento e gerenciamento de recursos baseado em QoS para Kubernetes projetado para co-localizar (*co-locate*) cargas de trabalho online sensíveis à latência (microsserviços) e jobs batch/IA nos mesmos nós, elevando a utilização real do cluster sem degradar SLOs.

## Por que importa
Nos clusters Kubernetes tradicionais, a utilização média de CPU frequentemente fica abaixo de 20%–30% porque as equipes dimensionam `requests` pelo pico máximo de tráfego, deixando recursos ociosos na maior parte do tempo que o `kube-scheduler` padrão não consegue reaproveitar com segurança para tarefas batch.

## Como funciona
A arquitetura do Koordinator divide-se no plano de controle (`koord-scheduler`, `koord-descheduler` e `koord-manager`) e no plano de nó (`koordlet` DaemonSet e opcionalmente `koord-runtime-proxy`). O `koordlet` mede o uso real dos Pods em tempo real, reclama os recursos alocados mas ociosos como recursos de *overcommit* (Mid/Batch/Free) e aplica isolamento fino de kernel (CPU, memória, cache L3, banda de memória e I/O) para proteger os serviços online.

## Exemplo
```bash
helm repo add koordinator-sh https://koordinator-sh.github.io/charts/
helm upgrade --install koordinator koordinator-sh/koordinator --namespace koordinator-system --create-namespace
kubectl get pods -n koordinator-system
```

## Limites e trade-offs
O Koordinator mantém total compatibilidade com workloads Kubernetes existentes: Pods que não especificam classes QoS do Koordinator continuam funcionando normalmente sob o modelo padrão `Guaranteed`, `Burstable` e `BestEffort` do Kubernetes.

## Como verificar
Verifique que `koord-scheduler`, `koord-descheduler`, `koord-manager` e o DaemonSet `koordlet` estão em estado `Running` no namespace `koordinator-system`.

## Conexões
- [[koordinator-modelo-qos-lse-lsr-ls-be-system-prioridades]] — Veja também: Koordinator: classes de QoS diferenciadas (`LSE`, `LSR`, `LS`, `BE` e `SYSTEM`) para cargas híbridas.

## Fontes
- [Koordinator GitHub — README.md (QoS-Based Scheduling System for Hybrid Orchestration Workloads on Kubernetes)](https://raw.githubusercontent.com/koordinator-sh/koordinator/main/README.md) — README oficial do koordinator-sh/koordinator apresentando os objetivos de utilização de recursos, redução de interferência e políticas de agendamento; consultado em 2026-10-03.
- [Koordinator Official Documentation — Architecture Overview (Koord-Scheduler, Koord-Descheduler, Koord-Manager, Koordlet & Koord-RuntimeProxy)](https://koordinator.sh/docs/architecture/overview/) — Visão geral oficial da arquitetura do Koordinator detalhando os componentes do control plane e do nó (Koordlet e Koord-RuntimeProxy); consultado em 2026-10-03.
- [Koordinator — Official GitHub Repository](https://github.com/koordinator-sh/koordinator) — Repositório oficial Apache-2.0 do Koordinator; consultado em 2026-10-03.
