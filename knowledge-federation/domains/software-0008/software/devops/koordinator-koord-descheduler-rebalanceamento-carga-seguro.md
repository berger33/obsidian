---
id: software.devops.tranche16.001568
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
fontes: ["https://koordinator.sh/docs/architecture/overview/", "https://raw.githubusercontent.com/koordinator-sh/koordinator/main/README.md", "https://github.com/koordinator-sh/koordinator"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Koordinator: `koord-descheduler` com migração segura apoiada em `Reservation` e balanceamento de carga

## Em uma frase
O `koord-descheduler` estende o Descheduler comunitário do Kubernetes com um framework determinístico de migração segura (`MigrationController`) e plugins de desagendamento baseados em carga real (`LowNodeLoad`).

## Por que importa
Desagendar um Pod em produção usando o descheduler tradicional apaga o Pod imediatamente (`Evict`) sem garantir que exista espaço livre em outro nó para agendá-lo, podendo reduzir a capacidade ativa do serviço se o novo Pod ficar preso em `Pending`.

## Como funciona
No `koord-descheduler`, o controlador de migração (via CRD `PodMigrationJob`) primeiro cria uma `Reservation` no cluster e aguarda que o `koord-scheduler` confirme a reserva de recursos em um nó saudável e menos carregado. Somente após os recursos do destino estarem garantidos (`Reservation Available`), o `koord-descheduler` evicta o Pod de origem para que o substituto assuma imediatamente a vaga reservada.

## Exemplo
```yaml
apiVersion: scheduling.koordinator.sh/v1alpha1
kind: PodMigrationJob
metadata:
  name: migrate-hot-pod-01
spec:
  podRef:
    namespace: prod
    name: checkout-7d9c8b-x4k2p
  mode: ReservationFirst
  ttl: 5m
```

## Limites e trade-offs
O modo `ReservationFirst` exige que o workload do Pod migrado seja agendado pelo `koord-scheduler`, pois o `kube-scheduler` padrão não reconhece nem consome objetos `Reservation`.

## Como verificar
Crie um `PodMigrationJob` com `mode: ReservationFirst` e acompanhe `kubectl get podmigrationjob migrate-hot-pod-01 -o wide` para observar as fases de reserva de recursos, evicção e alocação do novo Pod.

## Conexões
- [[koordinator-resource-reservation-crd-descheduling-preempcao]] — Veja também: Koordinator: reserva explícita de recursos de nó via CRD `Reservation` e `NodeReservation`.
- [[koordinator-koord-runtime-proxy-interceptacao-cri-cgroup-kernel]] — Veja também: Koordinator: interceptação de requisições CRI via `koord-runtime-proxy` para políticas avançadas de kernel.

## Fontes
- [Koordinator GitHub — README.md (QoS-Based Scheduling System for Hybrid Orchestration Workloads on Kubernetes)](https://koordinator.sh/docs/architecture/overview/) — README oficial do koordinator-sh/koordinator apresentando os objetivos de utilização de recursos, redução de interferência e políticas de agendamento; consultado em 2026-10-03.
- [Koordinator Official Documentation — Architecture Overview (Koord-Scheduler, Koord-Descheduler, Koord-Manager, Koordlet & Koord-RuntimeProxy)](https://raw.githubusercontent.com/koordinator-sh/koordinator/main/README.md) — Visão geral oficial da arquitetura do Koordinator detalhando os componentes do control plane e do nó (Koordlet e Koord-RuntimeProxy); consultado em 2026-10-03.
- [Koordinator — Official GitHub Repository](https://github.com/koordinator-sh/koordinator) — Repositório oficial Apache-2.0 do Koordinator; consultado em 2026-10-03.
