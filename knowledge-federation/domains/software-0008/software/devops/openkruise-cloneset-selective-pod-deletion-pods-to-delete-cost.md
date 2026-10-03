---
id: software.devops.tranche16.001554
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
fontes: ["https://openkruise.io/docs/user-manuals/cloneset/", "https://raw.githubusercontent.com/openkruise/kruise/master/README.md", "https://github.com/openkruise/kruise"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# OpenKruise CloneSet: exclusão seletiva de Pods (`podsToDelete`) e sequência de prioridades de scale-down

## Em uma frase
Ao reduzir réplicas ou substituir instâncias específicas, o `CloneSet` permite escolher exatamente quais Pods serão removidos via `spec.scaleStrategy.podsToDelete` ou pelo label `apps.kruise.io/specified-delete: "true"`, além de seguir uma sequência de 8 critérios de ordenação de deleção.

## Por que importa
Em um `Deployment`, reduzir `replicas` de `10` para `9` escolhe o Pod a deletar por heurísticas internas do `ReplicaSet`, e em um `StatefulSet` remove obrigatoriamente o maior ordinal (`-9`), impedindo descomissionar cirurgicamente a réplica `-3` que está apresentando degradação ou que roda em um nó específico.

## Como funciona
Se o operador listar nomes de Pods em `spec.scaleStrategy.podsToDelete` (ou rotular o Pod com `apps.kruise.io/specified-delete: "true"`) e reduzir `replicas`, o `CloneSet` deleta primeiro os Pods especificados e limpa a lista automaticamente. Se `replicas` não for reduzido, o controlador deleta o Pod marcado e cria um substituto respeitando `maxUnavailable`, `maxSurge` e o hook de ciclo de vida `PreparingDelete`.

## Exemplo
```yaml
apiVersion: apps.kruise.io/v1alpha1
kind: CloneSet
metadata:
  name: order-service
spec:
  replicas: 5
  scaleStrategy:
    podsToDelete:
      - order-service-9m4hp
  selector:
    matchLabels:
      app: order-service
```

## Limites e trade-offs
Para os demais Pods não listados explicitamente, o `CloneSet` ordena a deleção avaliando: 1) sem nó < agendado; 2) Pending < Unknown < Running; 3) não Ready < Ready; 4) menor `controller.kubernetes.io/pod-deletion-cost`; 5) maior concentração de spread; 6) menor tempo Ready; 7) mais restarts; 8) mais novo < mais antigo.

## Como verificar
Aplique o label `kubectl label pod order-service-xyz apps.kruise.io/specified-delete=true` e observe a substituição controlada do Pod respeitando o orçamento de indisponibilidade do `CloneSet`.

## Conexões
- [[openkruise-cloneset-volumeclaimtemplates-pvc-por-pod-reuso]] — Veja também: OpenKruise CloneSet: suporte a `volumeClaimTemplates` por Pod e controle de reuso de PVCs (`disablePVCReuse`).
- [[openkruise-advanced-statefulset-parallel-in-place-unordered-ready]] — Veja também: OpenKruise Advanced StatefulSet: escalonamento paralelo, rollout não ordenado e atualização in-place.

## Fontes
- [OpenKruise GitHub — README.md (Advanced Workloads, In-Place Update, Sidecar Management, Multi-Domain & Application Protection)](https://openkruise.io/docs/user-manuals/cloneset/) — README oficial do openkruise/kruise (CNCF Incubating) listando os controladores avançados de workload, operações aprimoradas e proteções de disponibilidade; consultado em 2026-10-03.
- [OpenKruise Official Documentation — CloneSet User Manual (Scale Features, PVC Templates, disablePVCReuse & Selective Pod Deletion)](https://raw.githubusercontent.com/openkruise/kruise/master/README.md) — Manual oficial do CloneSet no OpenKruise detalhando suporte a PVCs, atualização in-place, podsToDelete e sequência de prioridades de deleção; consultado em 2026-10-03.
- [OpenKruise — Official GitHub Repository](https://github.com/openkruise/kruise) — Repositório oficial Apache-2.0 do OpenKruise na CNCF; consultado em 2026-10-03.
