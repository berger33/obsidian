---
id: software.devops.tranche17.001608
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

# Karmada: failover automático de cluster e de aplicação com reagendamento de réplicas e preservação de estado

## Em uma frase
O Karmada implementa failover automático tanto no nível de **Cluster** (quando um cluster membro inteiro fica `NotReady`/inacessível) quanto no nível de **Aplicação** (quando os Pods em um cluster saudável falham continuamente em atingir `Ready`).

## Por que importa
Em uma arquitetura multi-cluster ativa-ativa com réplicas divididas (`Divided`), se um cluster membro perder conectividade ou sofrer esgotamento de recursos, um terço da capacidade global da aplicação desaparece até que um operador intervenha manualmente.

## Como funciona
Quando um cluster membro falha nas sondagens de saúde, o Karmada aplica taints automáticos (`cluster.karmada.io/not-ready` ou `unreachable`). Passado o tempo de tolerância (`tolerationSeconds`) ou acionado o `failover` na `PropagationPolicy` (com modos de purga `Directly`, `Graciously` ou `Never` e `statePreservation`), o `karmada-scheduler` migra automaticamente as réplicas daquele cluster para outros clusters saudáveis compatíveis.

## Exemplo
```yaml
apiVersion: policy.karmada.io/v1alpha1
kind: PropagationPolicy
metadata:
  name: resilient-api-policy
spec:
  resourceSelectors:
    - apiVersion: apps/v1
      kind: Deployment
      name: api-gateway
  failover:
    cluster:
      purgeMode: Graciously
  placement:
    clusterTolerations:
      - key: cluster.karmada.io/not-ready
        operator: Exists
        effect: NoExecute
        tolerationSeconds: 60
```

## Limites e trade-offs
No modo `purgeMode: Graciously`, o Karmada aguarda que as novas réplicas fiquem `Ready` no cluster de destino antes de remover o `Work` do cluster em falha, prevenindo queda momentânea da capacidade global.

## Como verificar
Simule a indisponibilidade de um cluster membro em laboratório e observe em `kubectl get resourcebinding api-gateway-deployment -o yaml` a realocação automática das réplicas após `60s`.

## Conexões
- [[karmada-spreadconstraints-alta-disponibilidade-multi-dimensao-regiao-az]] — Veja também: Karmada: restrições de espalhamento multi-dimensional (`spreadConstraints`) por provedor, região, zona e cluster.
- [[karmada-resource-interpreter-framework-crds-customizados-lua]] — Veja também: Karmada: *Resource Interpreter Framework* e customização em Lua para CRDs de terceiros.

## Fontes
- [Karmada GitHub — README.md (Kubernetes Armada CNCF Incubating Multi-Cloud & Multi-Cluster Kubernetes Orchestration)](https://raw.githubusercontent.com/karmada-io/karmada/master/README.md) — README oficial do karmada-io/karmada (CNCF Incubating) apresentando capacidades multi-cluster, API compatível com Kubernetes nativo e políticas de propagação; consultado em 2026-10-03.
- [Karmada Official Documentation — Core Concepts: Architecture (Control Plane, PropagationPolicy, OverridePolicy, ResourceBinding, Work & Agent)](https://karmada.io/docs/core-concepts/architecture/) — Documentação oficial de arquitetura do Karmada detalhando API Server, Controller Manager, Karmada Scheduler, Execution Space e sincronização para member clusters; consultado em 2026-10-03.
- [Karmada — Official GitHub Repository](https://github.com/karmada-io/karmada) — Repositório oficial Apache-2.0 do projeto Karmada na CNCF; consultado em 2026-10-03.
