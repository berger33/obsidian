---
id: software.devops.tranche17.001609
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

# Karmada: *Resource Interpreter Framework* e customização em Lua para CRDs de terceiros

## Em uma frase
O *Resource Interpreter Framework* do Karmada ensina o plano de controle a extrair contagem de réplicas, dependências, revisões e saúde de qualquer Custom Resource Definition (como `Argo Rollout`, `Kyverno Policy`, `Kafka` ou CRDs internos) por meio de hooks declarativos em Lua (`ResourceInterpreterCustomization`) ou webhooks.

## Por que importa
O Karmada conhece nativamente os campos de `Deployment`, `StatefulSet`, `DaemonSet`, `Job` e `Pod`, mas um CRD customizado pode guardar seu número de réplicas em `.spec.workers.count` e seu status em `.status.readyWorkers`. Sem um interpretador, o Karmada não saberia dividir réplicas (`Divided`) daquele CRD.

## Como funciona
O engenheiro cria um objeto `ResourceInterpreterCustomization` (`config.karmada.io/v1alpha1`) apontando para o `target` (`apiVersion` e `kind` do CRD) e escreve scripts Lua enxutos para `replicaResource` (retornando réplicas e requisitos por réplica), `reviseReplica` (atualizando o campo de réplicas no cluster membro) e `healthInterpretation`.

## Exemplo
```yaml
apiVersion: config.karmada.io/v1alpha1
kind: ResourceInterpreterCustomization
metadata:
  name: custom-worker-interpreter
spec:
  target:
    apiVersion: workload.example.io/v1alpha1
    kind: WorkerPool
  customizations:
    replicaResource:
      luaScript: >
        function GetReplicas(obj)
          return obj.spec.workerCount, obj.spec.template.spec.containers[1].resources
        end
    reviseReplica:
      luaScript: >
        function ReviseReplica(obj, desiredReplica)
          obj.spec.workerCount = desiredReplica
          return obj
        end
```

## Limites e trade-offs
Os scripts Lua do `ResourceInterpreterCustomization` rodam em uma VM Lua determinística embutida diretamente no `karmada-controller-manager` e no `karmada-scheduler`, sem exigir implantação de servidores HTTP de webhook externos.

## Como verificar
Teste os scripts Lua antes de aplicá-los no cluster usando o subcomando `karmadactl interpret` contra um manifesto de exemplo do CRD.

## Conexões
- [[karmada-failover-automatico-cluster-application-taints-eviction]] — Veja também: Karmada: failover automático de cluster e de aplicação com reagendamento de réplicas e preservação de estado.
- [[karmada-federatedhpa-cronfederatedhpa-multicluster-service-ingress]] — Veja também: Karmada: autoescalonamento multi-cluster (`FederatedHPA`, `CronFederatedHPA`) e descoberta `MultiClusterService`.

## Fontes
- [Karmada GitHub — README.md (Kubernetes Armada CNCF Incubating Multi-Cloud & Multi-Cluster Kubernetes Orchestration)](https://raw.githubusercontent.com/karmada-io/karmada/master/README.md) — README oficial do karmada-io/karmada (CNCF Incubating) apresentando capacidades multi-cluster, API compatível com Kubernetes nativo e políticas de propagação; consultado em 2026-10-03.
- [Karmada Official Documentation — Core Concepts: Architecture (Control Plane, PropagationPolicy, OverridePolicy, ResourceBinding, Work & Agent)](https://karmada.io/docs/core-concepts/architecture/) — Documentação oficial de arquitetura do Karmada detalhando API Server, Controller Manager, Karmada Scheduler, Execution Space e sincronização para member clusters; consultado em 2026-10-03.
- [Karmada — Official GitHub Repository](https://github.com/karmada-io/karmada) — Repositório oficial Apache-2.0 do projeto Karmada na CNCF; consultado em 2026-10-03.
