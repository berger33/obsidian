---
id: software.devops.tranche16.001555
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
fontes: ["https://raw.githubusercontent.com/openkruise/kruise/master/README.md", "https://openkruise.io/docs/user-manuals/cloneset/", "https://github.com/openkruise/kruise"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# OpenKruise Advanced StatefulSet: escalonamento paralelo, rollout não ordenado e atualização in-place

## Em uma frase
O `StatefulSet` avançado do OpenKruise (`apps.kruise.io/v1beta1`, `kind: StatefulSet`) é um substituto drop-in do `apps/v1 StatefulSet` que adiciona atualização *in-place*, rollout não ordenado (`UnorderedUpdate`), pausa de rollout (`paused: true`) e tolerância `maxUnavailable`.

## Por que importa
No `StatefulSet` nativo do Kubernetes, atualizar um cluster de 50 nós de banco de dados ou fila de mensagens de forma estritamente sequencial (`49 -> 0`) recriando cada Pod inteiro leva horas e trava completamente na primeira réplica que demorar a ficar pronta.

## Como funciona
Ao migrar `apiVersion` para `apps.kruise.io/v1beta1`, o administrador habilita `podManagementPolicy: Parallel` combinada com `updateStrategy.rollingUpdate.podUpdatePolicy: InPlaceIfPossible`, `maxUnavailable: 20%` e `unorderedUpdate: {priorityStrategy: ...}`. As réplicas são atualizadas in-place em paralelo sem perder seus volumes nem seus ordinais DNS (`pod-0`, `pod-1`).

## Exemplo
```yaml
apiVersion: apps.kruise.io/v1beta1
kind: StatefulSet
metadata:
  name: kafka-brokers
spec:
  replicas: 6
  serviceName: kafka-headless
  podManagementPolicy: Parallel
  updateStrategy:
    type: RollingUpdate
    rollingUpdate:
      podUpdatePolicy: InPlaceIfPossible
      maxUnavailable: 2
      unorderedUpdate:
        priorityStrategy:
          weightPriority:
            - weight: 100
              matchSelector:
                matchLabels:
                  role: follower
```

## Limites e trade-offs
Ao usar `unorderedUpdate` com `weightPriority`, é recomendável atribuir peso maior às réplicas `follower` e peso menor à réplica `leader` para que o líder do cluster stateful seja atualizado por último, evitando múltiplas eleições de líder durante o rollout.

## Como verificar
Inspecione `kubectl get asts kafka-brokers -o yaml` (atalho `asts` para Advanced StatefulSet) e monitore o progresso de `updatedReplicas` e `readyReplicas`.

## Conexões
- [[openkruise-cloneset-selective-pod-deletion-pods-to-delete-cost]] — Veja também: OpenKruise CloneSet: exclusão seletiva de Pods (`podsToDelete`) e sequência de prioridades de scale-down.
- [[openkruise-sidecarset-injecao-upgrade-independente-sidecars]] — Veja também: OpenKruise SidecarSet: injeção mutante e atualização in-place independente de containers sidecar.

## Fontes
- [OpenKruise GitHub — README.md (Advanced Workloads, In-Place Update, Sidecar Management, Multi-Domain & Application Protection)](https://raw.githubusercontent.com/openkruise/kruise/master/README.md) — README oficial do openkruise/kruise (CNCF Incubating) listando os controladores avançados de workload, operações aprimoradas e proteções de disponibilidade; consultado em 2026-10-03.
- [OpenKruise Official Documentation — CloneSet User Manual (Scale Features, PVC Templates, disablePVCReuse & Selective Pod Deletion)](https://openkruise.io/docs/user-manuals/cloneset/) — Manual oficial do CloneSet no OpenKruise detalhando suporte a PVCs, atualização in-place, podsToDelete e sequência de prioridades de deleção; consultado em 2026-10-03.
- [OpenKruise — Official GitHub Repository](https://github.com/openkruise/kruise) — Repositório oficial Apache-2.0 do OpenKruise na CNCF; consultado em 2026-10-03.
