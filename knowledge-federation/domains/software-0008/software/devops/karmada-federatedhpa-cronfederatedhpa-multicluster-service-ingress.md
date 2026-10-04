---
id: software.devops.tranche17.001610
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-17.md"
fontes: ["https://raw.githubusercontent.com/karmada-io/karmada/master/README.md", "https://karmada.io/docs/core-concepts/architecture/", "https://github.com/karmada-io/karmada"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Karmada: autoescalonamento multi-cluster (`FederatedHPA`, `CronFederatedHPA`) e descoberta `MultiClusterService`

## Em uma frase
Para fechar o ciclo operacional multi-cluster, o Karmada provê o `FederatedHPA` (autoescalonamento horizontal baseado em métricas agregadas de múltiplos clusters), o `CronFederatedHPA` (escalonamento programado por horário) e os recursos `MultiClusterService` / `MultiClusterIngress`.

## Por que importa
Usar um `HorizontalPodAutoscaler` isolado dentro de cada cluster membro entra em conflito direto com o controlador central do Karmada (que sobrescreveria `spec.replicas` no `Work`), além de impedir o escalonamento coordenado quando a capacidade de um cluster específico se esgota.

## Como funciona
O `FederatedHPA` (`autoscaling.karmada.io/v1alpha1`) consulta métricas de todos os clusters membros através do `karmada-metrics-adapter`, ajusta o total global de réplicas no `karmada-apiserver` e deixa o `karmada-scheduler` distribuir a nova carga entre os clusters com capacidade livre. Já o `MultiClusterService` (`networking.karmada.io/v1alpha1`) sincroniza `EndpointSlices` entre clusters produtores e consumidores.

## Exemplo
```yaml
apiVersion: autoscaling.karmada.io/v1alpha1
kind: FederatedHPA
metadata:
  name: checkout-fhpa
  namespace: default
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: checkout
  minReplicas: 4
  maxReplicas: 40
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
```

## Limites e trade-offs
Nunca aplique um `autoscaling/v2 HorizontalPodAutoscaler` local no cluster membro sobre um `Deployment` cujo número de réplicas já esteja sendo governado em modo `Divided` pelo Karmada; utilize sempre o `FederatedHPA` no plano de controle do Karmada.

## Como verificar
Execute `kubectl --context karmada-apiserver get fhpa checkout-fhpa` para verificar a leitura da métrica agregada (`TARGETS`) e o ajuste de `REPLICAS` globais.

## Conexões
- [[karmada-resource-interpreter-framework-crds-customizados-lua]] — Veja também: Karmada: *Resource Interpreter Framework* e customização em Lua para CRDs de terceiros.

## Fontes
- [Karmada GitHub — README.md (Kubernetes Armada CNCF Incubating Multi-Cloud & Multi-Cluster Kubernetes Orchestration)](https://raw.githubusercontent.com/karmada-io/karmada/master/README.md) — README oficial do karmada-io/karmada (CNCF Incubating) apresentando capacidades multi-cluster, API compatível com Kubernetes nativo e políticas de propagação; consultado em 2026-10-03.
- [Karmada Official Documentation — Core Concepts: Architecture (Control Plane, PropagationPolicy, OverridePolicy, ResourceBinding, Work & Agent)](https://karmada.io/docs/core-concepts/architecture/) — Documentação oficial de arquitetura do Karmada detalhando API Server, Controller Manager, Karmada Scheduler, Execution Space e sincronização para member clusters; consultado em 2026-10-03.
- [Karmada — Official GitHub Repository](https://github.com/karmada-io/karmada) — Repositório oficial Apache-2.0 do projeto Karmada na CNCF; consultado em 2026-10-03.
