---
id: software.devops.tranche17.001615
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
fontes: ["https://raw.githubusercontent.com/clusternet/clusternet/main/README.md", "https://clusternet.io/docs/introduction/", "https://github.com/clusternet/clusternet"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Clusternet: overrides em dois estágios (`Globalization` e `Localization`) com prioridades e rollback

## Em uma frase
O Clusternet separa as customizações de configuração em dois CRDs com escopos distintos — `Globalization` (cluster-scoped, aplica overrides globais em múltiplos namespaces) e `Localization` (namespaced, aplica overrides restritos a um namespace) — com prioridades numéricas (`priority: 0..1000`) para suportar rollouts canário entre clusters e rollback instantâneo.

## Por que importa
Em um sistema simples de um único nível de override, uma regra global de infraestrutura (como injetar proxy corporativo) e um ajuste específico da equipe da aplicação (como alterar a tag da imagem em apenas um cluster canário) sobrescrevem-se mutuamente sem ordem clara.

## Como funciona
O Clusternet avalia primeiro todas as `Globalizations` aplicáveis em ordem crescente de `spec.priority` (valores maiores têm precedência e são aplicados por último) e, em seguida, avalia todas as `Localizations` também em ordem de `spec.priority`, suportando formatos `Helm`, `JSONPatch`, `MergePatch`, `FieldJSONPatch` e `FieldMergePatch`. Para fazer um rollout canário ou reverter uma mudança, basta criar ou remover um objeto `Localization` de prioridade superior (ex.: `priority: 600`) sem tocar na configuração base.

## Exemplo
```yaml
apiVersion: apps.clusternet.io/v1alpha1
kind: Localization
metadata:
  name: canary-image-override
  namespace: clusternet-abcde
spec:
  priority: 600
  overridePolicy: ApplyLater
  overrides:
    - name: bump-canary-tag
      type: JSONPatch
      value: '[{"op": "replace", "path": "/spec/template/spec/containers/0/image", "value": "ghcr.io/org/web:v2.0-rc1"}]'
  feed:
    apiVersion: apps/v1
    kind: Deployment
    name: web-frontend
    namespace: default
```

## Limites e trade-offs
Em `spec.overridePolicy`, `ApplyLater` retém a aplicação do novo override até a próxima atualização da `Subscription` ou confirmação manual, enquanto `ApplyNow` propaga a mudança imediatamente para o `Description` do cluster filho.

## Como verificar
Execute `kubectl get description -n clusternet-abcde -o yaml` para verificar o manifesto final resultante após a fusão de `Globalization` e `Localization`.

## Conexões
- [[clusternet-subscription-scheduling-replication-dividing-static-dynamic]] — Veja também: Clusternet: agendamento multi-cluster via CRD `Subscription` (`Replication`, `Static` e `Dynamic` Dividing).
- [[clusternet-helm-charts-oci-registries-distribuicao-multi-cluster]] — Veja também: Clusternet: distribuição nativa de Helm Charts e artefatos OCI via CRD `HelmChart` e `HelmRelease`.

## Fontes
- [Clusternet GitHub — README.md (Managing Kubernetes Clusters as Easily as Visiting the Internet, Hub/Agent/Scheduler Architecture)](https://raw.githubusercontent.com/clusternet/clusternet/main/README.md) — README oficial do clusternet/clusternet detalhando descoberta automática, conexão Dual Sockets, coordenação multi-cluster e roteamento multi-estágio; consultado em 2026-10-03.
- [Clusternet Official Documentation — Introduction (Cluster Registration, App Delivery via Subscription/Localization/Globalization & Shadow APIs)](https://clusternet.io/docs/introduction/) — Introdução oficial do Clusternet cobrindo registro de clusters, entrega de aplicações multi-cluster, Localization, Globalization e APIs shadow; consultado em 2026-10-03.
- [Clusternet — Official GitHub Repository](https://github.com/clusternet/clusternet) — Repositório oficial Apache-2.0 do Clusternet; consultado em 2026-10-03.
