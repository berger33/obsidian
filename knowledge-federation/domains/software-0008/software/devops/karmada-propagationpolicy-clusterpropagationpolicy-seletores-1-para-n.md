---
id: software.devops.tranche17.001604
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

# Karmada: políticas de posicionamento `PropagationPolicy` e `ClusterPropagationPolicy` com mapeamento `1:N`

## Em uma frase
As APIs `PropagationPolicy` (namespaced) e `ClusterPropagationPolicy` (cluster-scoped) do grupo `policy.karmada.io/v1alpha1` definem onde e como um ou vários recursos Kubernetes devem ser distribuídos entre os clusters membros.

## Por que importa
No Kubernetes Federation legado, era necessário criar um wrapper proprietário (`FederatedDeployment`) para cada carga de trabalho. Separar a política de propagação (`PropagationPolicy`) do template nativo (`apps/v1 Deployment`) permite reutilizar uma única política para dezenas de microsserviços (`1:N`).

## Como funciona
Uma `PropagationPolicy` declara `spec.resourceSelectors` (selecionando objetos por `apiVersion`, `kind`, `name` ou `labelSelector`) e `spec.placement` (definindo `clusterAffinity`, `clusterTolerations`, `spreadConstraints` e `replicaScheduling`). Também é possível habilitar `propagateDeps: true` para propagar automaticamente `ConfigMaps`, `Secrets` e `ServiceAccounts` referenciados pelo `Deployment`.

## Exemplo
```yaml
apiVersion: policy.karmada.io/v1alpha1
kind: PropagationPolicy
metadata:
  name: multi-region-ha
  namespace: default
spec:
  propagateDeps: true
  resourceSelectors:
    - apiVersion: apps/v1
      kind: Deployment
      labelSelector:
        matchLabels:
          tier: frontend
  placement:
    clusterAffinity:
      clusterNames:
        - member-us-east
        - member-eu-west
```

## Limites e trade-offs
Se duas `PropagationPolicies` casarem com o mesmo recurso, o Karmada resolve o conflito avaliando `spec.priority` (explícita) ou a especificidade do seletor (correspondência por `name` exato precede `labelSelector`).

## Como verificar
Aplique a `PropagationPolicy` com `propagateDeps: true` e confirme nos clusters membros que tanto o `Deployment` quanto os `ConfigMaps` montados por ele foram criados automaticamente.

## Conexões
- [[karmada-modos-registro-clusters-push-vs-pull-karmada-agent]] — Veja também: Karmada: modos de registro de clusters membros (`Push` direto vs `Pull` via `karmada-agent`).
- [[karmada-replica-scheduling-duplicated-divided-static-dynamic-weight]] — Veja também: Karmada: estratégias de divisão de réplicas (`Duplicated` vs `Divided`, `StaticWeight` vs `DynamicWeight`).

## Fontes
- [Karmada GitHub — README.md (Kubernetes Armada CNCF Incubating Multi-Cloud & Multi-Cluster Kubernetes Orchestration)](https://raw.githubusercontent.com/karmada-io/karmada/master/README.md) — README oficial do karmada-io/karmada (CNCF Incubating) apresentando capacidades multi-cluster, API compatível com Kubernetes nativo e políticas de propagação; consultado em 2026-10-03.
- [Karmada Official Documentation — Core Concepts: Architecture (Control Plane, PropagationPolicy, OverridePolicy, ResourceBinding, Work & Agent)](https://karmada.io/docs/core-concepts/architecture/) — Documentação oficial de arquitetura do Karmada detalhando API Server, Controller Manager, Karmada Scheduler, Execution Space e sincronização para member clusters; consultado em 2026-10-03.
- [Karmada — Official GitHub Repository](https://github.com/karmada-io/karmada) — Repositório oficial Apache-2.0 do projeto Karmada na CNCF; consultado em 2026-10-03.
