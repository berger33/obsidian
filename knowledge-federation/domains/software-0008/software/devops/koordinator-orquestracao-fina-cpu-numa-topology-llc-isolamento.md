---
id: software.devops.tranche16.001565
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

# Koordinator: orquestração fina de CPU, topologia NUMA e isolamento de cache L3 (`LLC`) e banda de memória

## Em uma frase
O Koordinator implementa orquestração fina de CPU (*Fine-Grained CPU Orchestration*) no `koord-scheduler` e no `koordlet`, alinhando alocação de CPUs físicas, Hyper-Threads, nós NUMA e partições de Last Level Cache (`LLC`) / Memory Bandwidth Allocation (`MBA`) via Intel RDT ou ARM MPAM.

## Por que importa
O `CPU Manager` estático padrão do kubelet exige que o Pod seja `Guaranteed` com `requests` inteiros de CPU e não coordena o alinhamento NUMA entre múltiplos Pods nem evita que tarefas batch (`BE`) poluam o cache L3 dos núcleos dedicados às aplicações de baixa latência (`LSE`/`LSR`).

## Como funciona
O `koord-scheduler` mantém a topologia detalhada de sockets, nós NUMA e pares lógicos SMT de cada servidor no CRD `NodeResourceTopology`, alocando CPUs com políticas como `PCPUs` (evitando compartilhar o mesmo núcleo físico com outra carga sensível) e `NUMAAffinity`. No nó, o `koordlet` aplica `cpuset.cpus` nos cgroups e configura grupos `resctrl` do kernel Linux para restringir o percentual de cache L3 e banda de memória acessível pelos Pods `BE`.

## Exemplo
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: low-latency-trading
  labels:
    koordinator.sh/qosClass: LSE
  annotations:
    scheduling.koordinator.sh/numa-topology-spec: '{"numaTopologyPolicy":"Restricted"}'
spec:
  schedulerName: koord-scheduler
  containers:
    - name: engine
      image: ghcr.io/org/trading-engine:v2.0
      resources:
        requests:
          cpu: "8"
          memory: "16Gi"
        limits:
          cpu: "8"
          memory: "16Gi"
```

## Limites e trade-offs
O isolamento de cache L3 (`CAT`) e banda de memória (`MBA`) via sistema de arquivos `/sys/fs/resctrl` requer suporte de hardware (como Intel Xeon com Resource Director Technology) e kernel Linux com parâmetros `rdt=` habilitados.

## Como verificar
Inspecione `kubectl get noderesourcetopology <node> -o yaml` para verificar a descoberta dos nós NUMA e o mapa de CPUs reservadas pelo `koord-scheduler`.

## Conexões
- [[koordinator-koord-scheduler-load-aware-scheduling-prevencao-hotspots]] — Veja também: Koordinator: agendamento sensível à carga real (`Load-Aware Scheduling`) no `koord-scheduler`.
- [[koordinator-koordlet-qos-manager-supressao-dinamica-interferencia]] — Veja também: Koordinator: detecção de interferência e supressão dinâmica de cargas batch pelo `koordlet` QoS Manager.

## Fontes
- [Koordinator GitHub — README.md (QoS-Based Scheduling System for Hybrid Orchestration Workloads on Kubernetes)](https://koordinator.sh/docs/architecture/overview/) — README oficial do koordinator-sh/koordinator apresentando os objetivos de utilização de recursos, redução de interferência e políticas de agendamento; consultado em 2026-10-03.
- [Koordinator Official Documentation — Architecture Overview (Koord-Scheduler, Koord-Descheduler, Koord-Manager, Koordlet & Koord-RuntimeProxy)](https://raw.githubusercontent.com/koordinator-sh/koordinator/main/README.md) — Visão geral oficial da arquitetura do Koordinator detalhando os componentes do control plane e do nó (Koordlet e Koord-RuntimeProxy); consultado em 2026-10-03.
- [Koordinator — Official GitHub Repository](https://github.com/koordinator-sh/koordinator) — Repositório oficial Apache-2.0 do Koordinator; consultado em 2026-10-03.
