---
id: software.devops.tranche16.001560
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

# OpenKruise: proteção contra deleção em cascata (`Deletion Protection`) e `PodUnavailableBudget` (`PUB`)

## Em uma frase
Na camada de proteção de disponibilidade e SLA, o OpenKruise implementa o webhook de *Deletion Protection* (`policy.kruise.io/delete-protection`) e o recurso `PodUnavailableBudget` (`policy.kruise.io/v1alpha1`).

## Por que importa
O `PodDisruptionBudget` (`PDB`) nativo do Kubernetes protege aplicações apenas contra evicções voluntárias que usam a Eviction API (como `kubectl drain`), mas não intercepta um `kubectl delete pod` direto, uma atualização in-place concorrente ou um `kubectl delete namespace` acidental que apague workloads inteiros em produção.

## Como funciona
Com o label `policy.kruise.io/delete-protection: Always` (ou `Cascading`), o webhook do OpenKruise rejeita a exclusão de `Namespace`, `CustomResourceDefinition`, `Deployment`, `StatefulSet` ou `CloneSet` enquanto `Cascading` impedir apagar objetos que ainda possuam Pods ativos (`replicas > 0`). Já o `PodUnavailableBudget` intercepta via webhook tanto evicções quanto deleções diretas de Pods e atualizações in-place, garantindo que o número de Pods disponíveis nunca caia abaixo de `minAvailable` (ou `maxUnavailable`).

## Exemplo
```yaml
apiVersion: policy.kruise.io/v1alpha1
kind: PodUnavailableBudget
metadata:
  name: order-service-pub
  namespace: prod
spec:
  selector:
    matchLabels:
      app: order-service
  maxUnavailable: 10%
```

## Limites e trade-offs
Se um nó inteiro sofrer falha de hardware abrupta (queda física), os Pods naquele nó ficam indisponíveis fora do controle de admissão da API; o `PodUnavailableBudget` contabilizará essa indisponibilidade e bloqueará novas alterações voluntárias até que a capacidade mínima seja restaurada.

## Como verificar
Tente deletar diretamente um lote de Pods acima de `maxUnavailable` com `kubectl delete pod` em um workload protegido por `PodUnavailableBudget` e confirme que o webhook bloqueia a operação excedente.

## Conexões
- [[openkruise-imagepulljob-containerrecreaterequest-operacoes-no]] — Veja também: OpenKruise: pré-aquecimento de imagens (`ImagePullJob`) e reinício cirúrgico (`ContainerRecreateRequest`).

## Fontes
- [OpenKruise GitHub — README.md (Advanced Workloads, In-Place Update, Sidecar Management, Multi-Domain & Application Protection)](https://raw.githubusercontent.com/openkruise/kruise/master/README.md) — README oficial do openkruise/kruise (CNCF Incubating) listando os controladores avançados de workload, operações aprimoradas e proteções de disponibilidade; consultado em 2026-10-03.
- [OpenKruise Official Documentation — CloneSet User Manual (Scale Features, PVC Templates, disablePVCReuse & Selective Pod Deletion)](https://openkruise.io/docs/user-manuals/cloneset/) — Manual oficial do CloneSet no OpenKruise detalhando suporte a PVCs, atualização in-place, podsToDelete e sequência de prioridades de deleção; consultado em 2026-10-03.
- [OpenKruise — Official GitHub Repository](https://github.com/openkruise/kruise) — Repositório oficial Apache-2.0 do OpenKruise na CNCF; consultado em 2026-10-03.
