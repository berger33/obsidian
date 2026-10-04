---
id: software.devops.tranche17.001660
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
fontes: ["https://raw.githubusercontent.com/superedge/superedge/main/README.md", "https://raw.githubusercontent.com/superedge/superedge/main/docs/components/lite-apiserver.md", "https://github.com/superedge/superedge"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# SuperEdge: atualizações graduais por região com `StatefulSetGrid` e templates diferenciados por `NodeUnit`

## Em uma frase
Os recursos `DeploymentGrid` e `StatefulSetGrid` do SuperEdge permitem definir um `defaultTemplate` global e sobrescrever templates específicos por `NodeUnit` no mapa `templates`, viabilizando atualizações canário (*canary rollout*) região por região.

## Por que importa
Atualizar simultaneamente o software de controle em 300 fábricas ou praças de pedágio é inaceitável; a engenharia precisa testar a versão `v2.3` apenas na `toll-station-01` por 24 horas mantendo as outras 299 unidades na versão `v2.2`.

## Como funciona
No `DeploymentGrid` ou `StatefulSetGrid`, todas as unidades usam `spec.defaultTemplate` (com `image: app:v2.2`), exceto as unidades explicitamente chaveadas no mapa `spec.templates` (por exemplo `toll-station-01` apontando para um template com `image: app:v2.3`), permitindo promover gradualmente cada site no mesmo manifesto declarativo.

## Exemplo
```yaml
apiVersion: superedge.io/v1
kind: StatefulSetGrid
metadata:
  name: edge-collector-grid
  namespace: default
spec:
  gridUniqKey: superedge.io/nodeunit
  defaultTemplate:
    serviceName: collector-svc
    replicas: 1
    selector:
      matchLabels:
        app: collector
    template:
      metadata:
        labels:
          app: collector
      spec:
        containers:
          - name: collector
            image: ghcr.io/org/collector:v2.2
```

## Limites e trade-offs
Para que um `StatefulSetGrid` funcione corretamente na borda, o `Service` headless associado (`serviceName`) deve ser gerenciado por um `ServiceGrid` correspondente no mesmo namespace.

## Como verificar
Execute `kubectl get statefulsets -l superedge.io/grid-key=superedge.io/nodeunit` e confirme a criação de um `StatefulSet` independente para cada `NodeUnit`.

## Conexões
- [[superedge-edgeadm-instalacao-offline-conversao-cluster-nativo]] — Veja também: SuperEdge `edgeadm`: instalação one-click offline de clusters de borda e conversão de clusters Kubernetes nativos.

## Fontes
- [SuperEdge GitHub — README.md (Kubernetes-Native Edge Container Management System, Kins L4/L5 Autonomy, ServiceGroup & Edge-Health)](https://raw.githubusercontent.com/superedge/superedge/main/README.md) — README oficial do superedge/superedge detalhando componentes de nuvem e borda, níveis de autonomia L3/L4/L5 (Kins), DeploymentGrid/ServiceGrid, tunnel e edgeadm; consultado em 2026-10-03.
- [SuperEdge Official Documentation — Components: lite-apiserver (TLS CN Reverse Proxy, Bolt/Badger/File Cache & Certificate Rotation)](https://raw.githubusercontent.com/superedge/superedge/main/docs/components/lite-apiserver.md) — Documentação técnica oficial do componente lite-apiserver no SuperEdge cobrindo proxy por Common Name X.509, motores de cache local e autonomia L3; consultado em 2026-10-03.
- [SuperEdge — Official GitHub Repository](https://github.com/superedge/superedge) — Repositório oficial Apache-2.0 do SuperEdge; consultado em 2026-10-03.
