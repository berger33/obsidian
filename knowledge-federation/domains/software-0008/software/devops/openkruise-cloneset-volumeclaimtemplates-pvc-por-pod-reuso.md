---
id: software.devops.tranche16.001553
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

# OpenKruise CloneSet: suporte a `volumeClaimTemplates` por Pod e controle de reuso de PVCs (`disablePVCReuse`)

## Em uma frase
Diferentemente do `Deployment` nativo do Kubernetes, o `CloneSet` permite declarar `volumeClaimTemplates` para provisionar e associar automaticamente PersistentVolumeClaims dedicados a cada Pod sem impor a ordenação sequencial rígida de um `StatefulSet`.

## Por que importa
Muitas cargas de trabalho distribuídas ou workers com cache em disco precisam de um volume persistente individual por réplica, mas querem escalar e atualizar em paralelo sem os índices sequenciais (`-0`, `-1`, `-2`) que travam o `StatefulSet` quando um único Pod falha.

## Como funciona
Cada Pod e seus PVCs criados pelo `CloneSet` recebem o mesmo valor no label `apps.kruise.io/cloneset-instance-id`. Quando um Pod é atualizado via `in-place` ou deletado manualmente, os PVCs são preservados e reutilizados pelo novo Pod que assume o mesmo `instance-id`. Caso o nó sofra falha permanente e o volume local impeça a subida do Pod em outro nó, configurar `scaleStrategy.disablePVCReuse: true` faz o controlador deletar e recriar os PVCs automaticamente.

## Exemplo
```yaml
apiVersion: apps.kruise.io/v1alpha1
kind: CloneSet
metadata:
  name: cache-worker
spec:
  replicas: 4
  scaleStrategy:
    disablePVCReuse: true
  selector:
    matchLabels:
      app: cache-worker
  template:
    metadata:
      labels:
        app: cache-worker
    spec:
      containers:
        - name: worker
          image: ghcr.io/org/worker:v1.0
          volumeMounts:
            - name: workdir
              mountPath: /var/lib/worker
  volumeClaimTemplates:
    - metadata:
        name: workdir
      spec:
        accessModes: ["ReadWriteOnce"]
        resources:
          requests:
            storage: 20Gi
```

## Limites e trade-offs
Por padrão, se a imagem e o tamanho do `volumeClaimTemplates` mudarem simultaneamente com atualização `in-place`, o volume existente não é reconstruído; para forçar recriação do Pod e do volume ao alterar o template de PVC, habilita-se o feature-gate `RecreatePodWhenChangeVCTInCloneSetGate=true` (Kruise v1.7.0+).

## Como verificar
Inspecione os PVCs criados com `kubectl get pvc -l apps.kruise.io/cloneset-instance-id` e confirme a correspondência 1:1 com cada Pod do `CloneSet`.

## Conexões
- [[openkruise-cloneset-in-place-update-preservacao-ip-sandbox]] — Veja também: OpenKruise CloneSet: atualização in-place de containers (`InPlaceIfPossible`) preservando IP e Pod sandbox.
- [[openkruise-cloneset-selective-pod-deletion-pods-to-delete-cost]] — Veja também: OpenKruise CloneSet: exclusão seletiva de Pods (`podsToDelete`) e sequência de prioridades de scale-down.

## Fontes
- [OpenKruise GitHub — README.md (Advanced Workloads, In-Place Update, Sidecar Management, Multi-Domain & Application Protection)](https://openkruise.io/docs/user-manuals/cloneset/) — README oficial do openkruise/kruise (CNCF Incubating) listando os controladores avançados de workload, operações aprimoradas e proteções de disponibilidade; consultado em 2026-10-03.
- [OpenKruise Official Documentation — CloneSet User Manual (Scale Features, PVC Templates, disablePVCReuse & Selective Pod Deletion)](https://raw.githubusercontent.com/openkruise/kruise/master/README.md) — Manual oficial do CloneSet no OpenKruise detalhando suporte a PVCs, atualização in-place, podsToDelete e sequência de prioridades de deleção; consultado em 2026-10-03.
- [OpenKruise — Official GitHub Repository](https://github.com/openkruise/kruise) — Repositório oficial Apache-2.0 do OpenKruise na CNCF; consultado em 2026-10-03.
