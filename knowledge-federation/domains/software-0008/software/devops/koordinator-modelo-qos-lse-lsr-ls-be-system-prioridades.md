---
id: software.devops.tranche16.001562
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

# Koordinator: classes de QoS diferenciadas (`LSE`, `LSR`, `LS`, `BE` e `SYSTEM`) para cargas híbridas

## Em uma frase
O Koordinator define cinco classes de Qualidade de Serviço (`koordinator.sh/qosClass`) — `SYSTEM`, `LSE` (*Latency-Sensitive Exclusive*), `LSR` (*Latency-Sensitive Reserved*), `LS` (*Latency-Sensitive*) e `BE` (*Best-Effort*) — para governar o isolamento físico e o compartilhamento de CPU, memória e cache nos nós.

## Por que importa
As três classes QoS nativas do Kubernetes (`Guaranteed`, `Burstable`, `BestEffort`) são inferidas apenas pela igualdade entre `requests` e `limits` e não distinguem se um workload é um motor de banco de dados de ultra-baixa latência, um microsserviço web elástico ou um job Spark offline tolerante a preempção.

## Como funciona
No modelo do Koordinator, `LSE` e `LSR` reservam núcleos de CPU dedicados para aplicações críticas de latência extrema; `LS` compartilha um pool de CPUs com garantias de cota e baixa latência de escalonamento; `BE` consome a capacidade ociosa reclamada (*reclaimed resources*) das cargas `LS`/`LSR` com supressão dinâmica imediata caso as cargas `LS` precisem de mais CPU; e `SYSTEM` protege daemons essenciais de infraestrutura.

## Exemplo
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: payment-gateway
  labels:
    koordinator.sh/qosClass: LS
spec:
  schedulerName: koord-scheduler
  containers:
    - name: gateway
      image: ghcr.io/org/gateway:v1.3
      resources:
        requests:
          cpu: "4"
          memory: "8Gi"
        limits:
          cpu: "4"
          memory: "8Gi"
```

## Limites e trade-offs
Pods da classe `BE` consomem recursos estendidos do tipo `kubernetes.io/batch-cpu` e `kubernetes.io/batch-memory` (calculados pelo `koordlet` a partir da folga dos nós) em vez dos recursos padrão `cpu` e `memory`.

## Como verificar
Inspecione o objeto `Node` (`kubectl describe node <node>`) e confirme a publicação dos recursos alocáveis estendidos `kubernetes.io/batch-cpu` e `kubernetes.io/batch-memory` calculados pelo Koordinator.

## Conexões
- [[koordinator-arquitetura-colocation-qos-scheduler-koordlet]] — Veja também: Koordinator: arquitetura de co-localização híbrida baseada em QoS (`koord-scheduler`, `koord-manager` e `koordlet`).
- [[koordinator-colocation-profile-injecao-automatica-sem-modificar-workloads]] — Veja também: Koordinator: adoção transparente de co-localização via `ClusterColocationProfile` sem alterar manifestos.

## Fontes
- [Koordinator GitHub — README.md (QoS-Based Scheduling System for Hybrid Orchestration Workloads on Kubernetes)](https://koordinator.sh/docs/architecture/overview/) — README oficial do koordinator-sh/koordinator apresentando os objetivos de utilização de recursos, redução de interferência e políticas de agendamento; consultado em 2026-10-03.
- [Koordinator Official Documentation — Architecture Overview (Koord-Scheduler, Koord-Descheduler, Koord-Manager, Koordlet & Koord-RuntimeProxy)](https://raw.githubusercontent.com/koordinator-sh/koordinator/main/README.md) — Visão geral oficial da arquitetura do Koordinator detalhando os componentes do control plane e do nó (Koordlet e Koord-RuntimeProxy); consultado em 2026-10-03.
- [Koordinator — Official GitHub Repository](https://github.com/koordinator-sh/koordinator) — Repositório oficial Apache-2.0 do Koordinator; consultado em 2026-10-03.
