---
id: software.devops.tranche16.001558
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

# OpenKruise: distribuição multi-domínio elástica com `WorkloadSpread` e `UnitedDeployment`

## Em uma frase
Para gerenciar aplicações distribuídas entre múltiplos domínios de falha ou pools heterogêneos (zonas de disponibilidade, arquiteturas x86/ARM, nós on-demand vs spot ou Virtual Kubelet), o OpenKruise oferece o `WorkloadSpread` e o `UnitedDeployment`.

## Por que importa
As `topologySpreadConstraints` nativas do Kubernetes distribuem Pods de maneira simétrica, mas não permitem facilmente definir cotas numéricas ou percentuais por subconjunto (por exemplo: manter exatamente 20 réplicas fixas em nós on-demand e transbordar todo o restante do autoescalonamento para nós spot ou elásticos).

## Como funciona
O `WorkloadSpread` atua de forma não intrusiva por webhook sobre workloads existentes (`Deployment`, `CloneSet`, `ReplicaSet`, `Job`), dividindo as réplicas em `subsets` com `maxReplicas` e injetando `nodeSelector`, `affinity` e `tolerations` específicas em cada fatia. Já o `UnitedDeployment` é um workload guarda-chuva que cria e reconcilia múltiplos sub-workloads (`StatefulSet`, `CloneSet` ou `Deployment`) dedicados por domínio.

## Exemplo
```yaml
apiVersion: apps.kruise.io/v1alpha1
kind: WorkloadSpread
metadata:
  name: checkout-spread
spec:
  targetReference:
    apiVersion: apps/v1
    kind: Deployment
    name: checkout
  subsets:
    - name: on-demand-baseline
      maxReplicas: 10
      requiredNodeSelectorTerm:
        matchExpressions:
          - key: node.kubernetes.io/capacity
            operator: In
            values: ["on-demand"]
    - name: spot-elastic
      requiredNodeSelectorTerm:
        matchExpressions:
          - key: node.kubernetes.io/capacity
            operator: In
            values: ["spot"]
```

## Limites e trade-offs
Na lista `subsets` do `WorkloadSpread`, os Pods são alocados sequencialmente do primeiro subset até atingir seu `maxReplicas`, transbordando para o subset seguinte (cujo último item geralmente omite `maxReplicas` para absorver o crescimento ilimitado do HPA).

## Como verificar
Escale o `Deployment` `checkout` de `8` para `25` réplicas e verifique com `kubectl get pods -o wide` que exatamente 10 Pods foram alocados no pool `on-demand` e 15 no pool `spot`.

## Conexões
- [[openkruise-container-launch-priority-job-sidecar-terminator]] — Veja também: OpenKruise: ordenação de partida (`Container Launch Priority`) e encerramento de sidecars em Jobs (`Sidecar Terminator`).
- [[openkruise-imagepulljob-containerrecreaterequest-operacoes-no]] — Veja também: OpenKruise: pré-aquecimento de imagens (`ImagePullJob`) e reinício cirúrgico (`ContainerRecreateRequest`).

## Fontes
- [OpenKruise GitHub — README.md (Advanced Workloads, In-Place Update, Sidecar Management, Multi-Domain & Application Protection)](https://raw.githubusercontent.com/openkruise/kruise/master/README.md) — README oficial do openkruise/kruise (CNCF Incubating) listando os controladores avançados de workload, operações aprimoradas e proteções de disponibilidade; consultado em 2026-10-03.
- [OpenKruise Official Documentation — CloneSet User Manual (Scale Features, PVC Templates, disablePVCReuse & Selective Pod Deletion)](https://openkruise.io/docs/user-manuals/cloneset/) — Manual oficial do CloneSet no OpenKruise detalhando suporte a PVCs, atualização in-place, podsToDelete e sequência de prioridades de deleção; consultado em 2026-10-03.
- [OpenKruise — Official GitHub Repository](https://github.com/openkruise/kruise) — Repositório oficial Apache-2.0 do OpenKruise na CNCF; consultado em 2026-10-03.
