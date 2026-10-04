---
id: software.devops.tranche17.001605
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

# Karmada: estratégias de divisão de réplicas (`Duplicated` vs `Divided`, `StaticWeight` vs `DynamicWeight`)

## Em uma frase
Dentro de `spec.placement.replicaScheduling` de uma `PropagationPolicy`, o Karmada oferece os tipos `Duplicated` (espelha o total de réplicas em cada cluster) e `Divided` (divide o total de `spec.replicas` entre os clusters por peso estático `StaticWeight` ou capacidade livre `DynamicWeight`).

## Por que importa
Para um agente de monitoramento ou gateway regional, deseja-se ter `3` réplicas em cada um dos 3 clusters (`Duplicated` = 9 pods no total). Já para um serviço stateless escalado globalmente para `30` réplicas, deseja-se dividir essas `30` réplicas proporcionalmente (por exemplo `20` no cluster principal e `10` no secundário via `Divided`).

## Como funciona
Com `replicaSchedulingType: Divided` e `replicaDivisionPreference: Weighted`, o bloco `weightPreference.staticWeightList` atribui pesos numéricos aos clusters alvo (por exemplo peso `2` para `member1` e peso `1` para `member2`, dividindo 30 réplicas em 20 e 10). Se `dynamicWeight: AvailableReplicas` for escolhido, o `karmada-scheduler` consulta a capacidade alocável real de cada cluster membro para distribuir as réplicas proporcionalmente.

## Exemplo
```yaml
apiVersion: policy.karmada.io/v1alpha1
kind: PropagationPolicy
metadata:
  name: checkout-divided-weight
spec:
  resourceSelectors:
    - apiVersion: apps/v1
      kind: Deployment
      name: checkout
  placement:
    clusterAffinity:
      clusterNames: [member1, member2]
    replicaScheduling:
      replicaSchedulingType: Divided
      replicaDivisionPreference: Weighted
      weightPreference:
        staticWeightList:
          - targetCluster:
              clusterNames: [member1]
            weight: 2
          - targetCluster:
              clusterNames: [member2]
            weight: 1
```

## Limites e trade-offs
Quando `replicaSchedulingType: Divided` é usado com um número de réplicas que não divide exatamente pela soma dos pesos, o Karmada distribui o resto da divisão inteira priorizando os clusters de maior peso ou disponibilidade.

## Como verificar
Escale o `Deployment` `checkout` no `karmada-apiserver` para `9` réplicas e verifique que `member1` recebeu `6` réplicas e `member2` recebeu `3` réplicas.

## Conexões
- [[karmada-propagationpolicy-clusterpropagationpolicy-seletores-1-para-n]] — Veja também: Karmada: políticas de posicionamento `PropagationPolicy` e `ClusterPropagationPolicy` com mapeamento `1:N`.
- [[karmada-overridepolicy-especializacao-regional-image-overrider-plaintext]] — Veja também: Karmada: customização por cluster via `OverridePolicy` (`imageOverrider`, `plaintext`, `labelsOverrider`).

## Fontes
- [Karmada GitHub — README.md (Kubernetes Armada CNCF Incubating Multi-Cloud & Multi-Cluster Kubernetes Orchestration)](https://raw.githubusercontent.com/karmada-io/karmada/master/README.md) — README oficial do karmada-io/karmada (CNCF Incubating) apresentando capacidades multi-cluster, API compatível com Kubernetes nativo e políticas de propagação; consultado em 2026-10-03.
- [Karmada Official Documentation — Core Concepts: Architecture (Control Plane, PropagationPolicy, OverridePolicy, ResourceBinding, Work & Agent)](https://karmada.io/docs/core-concepts/architecture/) — Documentação oficial de arquitetura do Karmada detalhando API Server, Controller Manager, Karmada Scheduler, Execution Space e sincronização para member clusters; consultado em 2026-10-03.
- [Karmada — Official GitHub Repository](https://github.com/karmada-io/karmada) — Repositório oficial Apache-2.0 do projeto Karmada na CNCF; consultado em 2026-10-03.
