---
id: software.devops.tranche16.001566
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

# Koordinator: detecção de interferência e supressão dinâmica de cargas batch pelo `koordlet` QoS Manager

## Em uma frase
O `koordlet` executa em cada nó um loop contínuo de *Resource Profiling*, *Interference Detection* e *QoS Manager* que monitora picos repentinos de consumo das cargas online (`LS`/`LSR`) e suprime instantaneamente (ou despeja) cargas `BE` locais para preservar o SLO.

## Por que importa
O modelo de overcommit de recursos assume que as aplicações online não usam 100% da CPU o tempo todo; porém, durante um pico súbito de tráfego (flash crowd), a aplicação online reclamará seus recursos imediatamente — em milissegundos ou segundos, rápido demais para depender de uma reação centralizada do control plane.

## Como funciona
Quando o módulo de *Resource Profiling* e *Interference Detection* do `koordlet` detecta aumento de utilização dos Pods `LS`, aumento de atraso de agendamento de CPU (*CPU scheduling delay*), contenção de alocação de memória ou I/O de disco acima da linha d'água configurada no `NodeSLO`, o *QoS Manager* reduz imediatamente a cota de CPU (`cpu.cfs_quota_us` / `cpuset`) dos containers `BE` naquele nó e, se a pressão persistir, evicta seletivamente os Pods `BE` de menor prioridade.

## Exemplo
```yaml
apiVersion: slo.koordinator.sh/v1alpha1
kind: NodeSLO
metadata:
  name: default-node-slo
spec:
  resourceUsedThresholdWithBE:
    enable: true
    cpuSuppressThresholdPercent: 65
    cpuSuppressPolicy: cpuset
    memoryEvictThresholdPercent: 75
```

## Limites e trade-offs
Definir `cpuSuppressThresholdPercent` muito alto (por exemplo acima de 85%) reduz a margem de segurança para absorver rajadas sub-segundo de tráfego nas aplicações `LS` antes que ocorra *CPU throttling*.

## Como verificar
Inspecione o `ConfigMap` `slo-controller-config` em `koordinator-system` e os objetos `NodeSLO` (`kubectl get nodeslo -o yaml`) para auditar os limiares de supressão e evicção ativos.

## Conexões
- [[koordinator-orquestracao-fina-cpu-numa-topology-llc-isolamento]] — Veja também: Koordinator: orquestração fina de CPU, topologia NUMA e isolamento de cache L3 (`LLC`) e banda de memória.
- [[koordinator-resource-reservation-crd-descheduling-preempcao]] — Veja também: Koordinator: reserva explícita de recursos de nó via CRD `Reservation` e `NodeReservation`.

## Fontes
- [Koordinator GitHub — README.md (QoS-Based Scheduling System for Hybrid Orchestration Workloads on Kubernetes)](https://koordinator.sh/docs/architecture/overview/) — README oficial do koordinator-sh/koordinator apresentando os objetivos de utilização de recursos, redução de interferência e políticas de agendamento; consultado em 2026-10-03.
- [Koordinator Official Documentation — Architecture Overview (Koord-Scheduler, Koord-Descheduler, Koord-Manager, Koordlet & Koord-RuntimeProxy)](https://raw.githubusercontent.com/koordinator-sh/koordinator/main/README.md) — Visão geral oficial da arquitetura do Koordinator detalhando os componentes do control plane e do nó (Koordlet e Koord-RuntimeProxy); consultado em 2026-10-03.
- [Koordinator — Official GitHub Repository](https://github.com/koordinator-sh/koordinator) — Repositório oficial Apache-2.0 do Koordinator; consultado em 2026-10-03.
