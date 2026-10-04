---
id: software.devops.tranche16.001552
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

# OpenKruise CloneSet: atualização in-place de containers (`InPlaceIfPossible`) preservando IP e Pod sandbox

## Em uma frase
O `CloneSet` (`apps.kruise.io/v1alpha1`) é o controlador do OpenKruise para aplicações stateless e semi-stateful de larga escala que gerencia Pods diretamente (sem `ReplicaSet` intermediário) e suporta atualização *in-place* (`InPlaceIfPossible` e `InPlaceOnly`).

## Por que importa
Em um `Deployment` tradicional, atualizar a imagem da aplicação destrói o Pod antigo e agenda um novo Pod, trocando o IP do Pod, desconectando malhas de serviço ou registros de descoberta e exigindo reaquecimento de volumes locais.

## Como funciona
Quando `spec.updateStrategy.type: InPlaceIfPossible` está configurado no `CloneSet` e apenas campos mutáveis in-place (como `spec.template.spec.containers[x].image` ou metadados) são alterados, o controlador atualiza o hash da imagem no Pod existente e aciona o container runtime para trocar apenas aquele container. O Pod mantém exatamente o mesmo `uid`, o mesmo nome, o mesmo `podIP` e os mesmos volumes montados.

## Exemplo
```yaml
apiVersion: apps.kruise.io/v1alpha1
kind: CloneSet
metadata:
  name: order-service
spec:
  replicas: 6
  selector:
    matchLabels:
      app: order-service
  updateStrategy:
    type: InPlaceIfPossible
    inPlaceUpdateStrategy:
      gracePeriodSeconds: 10
  template:
    metadata:
      labels:
        app: order-service
    spec:
      containers:
        - name: app
          image: ghcr.io/org/order:v1.1.0
```

## Limites e trade-offs
Se a alteração no `template` modificar campos que o Kubernetes não permite mutar em um Pod vivo (como `resources.requests` em versões sem *In-Place Pod Vertical Scaling* ativo ou novos volumes), `InPlaceIfPossible` faz fallback automático para recriação do Pod, enquanto `InPlaceOnly` rejeita ou ignora a recriação.

## Como verificar
Atualize a tag da imagem no `CloneSet`, execute `kubectl get pods -l app=order-service -o wide` antes e depois do rollout e confirme que os nomes e IPs dos Pods permaneceram idênticos enquanto `RESTARTS` incrementou em `1`.

## Conexões
- [[openkruise-arquitetura-controladores-workloads-avancados-cncf]] — Veja também: OpenKruise: suíte CNCF de controladores avançados de workloads e atualizações in-place no Kubernetes.
- [[openkruise-cloneset-volumeclaimtemplates-pvc-por-pod-reuso]] — Veja também: OpenKruise CloneSet: suporte a `volumeClaimTemplates` por Pod e controle de reuso de PVCs (`disablePVCReuse`).

## Fontes
- [OpenKruise GitHub — README.md (Advanced Workloads, In-Place Update, Sidecar Management, Multi-Domain & Application Protection)](https://openkruise.io/docs/user-manuals/cloneset/) — README oficial do openkruise/kruise (CNCF Incubating) listando os controladores avançados de workload, operações aprimoradas e proteções de disponibilidade; consultado em 2026-10-03.
- [OpenKruise Official Documentation — CloneSet User Manual (Scale Features, PVC Templates, disablePVCReuse & Selective Pod Deletion)](https://raw.githubusercontent.com/openkruise/kruise/master/README.md) — Manual oficial do CloneSet no OpenKruise detalhando suporte a PVCs, atualização in-place, podsToDelete e sequência de prioridades de deleção; consultado em 2026-10-03.
- [OpenKruise — Official GitHub Repository](https://github.com/openkruise/kruise) — Repositório oficial Apache-2.0 do OpenKruise na CNCF; consultado em 2026-10-03.
