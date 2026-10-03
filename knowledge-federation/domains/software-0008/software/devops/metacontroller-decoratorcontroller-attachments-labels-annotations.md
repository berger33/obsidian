---
id: software.devops.tranche18.001773
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-18.md"
fontes: ["https://metacontroller.github.io/metacontroller/concepts.html", "https://raw.githubusercontent.com/metacontroller/metacontroller/master/README.md", "https://github.com/metacontroller/metacontroller"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Metacontroller `DecoratorController`: anexação de comportamentos e recursos secundários a objetos existentes

## Em uma frase
O CRD **`DecoratorController`** (`metacontroller.k8s.io/v1alpha1`) permite anexar novos objetos filhos (*attachments*), labels, anotações ou status a recursos Kubernetes existentes (nativos ou CRDs) selecionados por `labelSelector` ou `annotationSelector`, sem que o recurso principal precise ser dono exclusivo de todos os objetos do tipo.

## Por que importa
No `CompositeController`, cada tipo de recurso pai é dono de sua própria árvore; porém, muitas vezes queremos "decorar" qualquer `StatefulSet` ou `Pod` que receba a anotação `service-per-pod: "true"` criando um `Service` dedicado para ele, sem substituir o controlador nativo do `StatefulSet`.

## Como funciona
No `DecoratorController`, `spec.resources` define quais objetos observar (com filtros opcionais de `annotationSelector` / `labelSelector`) e `spec.attachments` define quais tipos de recursos anexos o hook `sync` pode criar e gerenciar. Quando o objeto principal ou a anotação é removida, o Metacontroller limpa automaticamente os attachments via Garbage Collection.

## Exemplo
```yaml
apiVersion: metacontroller.k8s.io/v1alpha1
kind: DecoratorController
metadata:
  name: service-per-pod-decorator
spec:
  resources:
    - apiVersion: apps/v1
      resource: statefulsets
      annotationSelector:
        matchExpressions:
          - {key: service-per-pod-label, operator: Exists}
  attachments:
    - apiVersion: v1
      resource: services
      updateStrategy:
        method: InPlace
  hooks:
    sync:
      webhook:
        url: http://service-per-pod.metacontroller/sync
```

## Limites e trade-offs
O `DecoratorController` pode observar múltiplos tipos de recursos simultaneamente (por exemplo, tanto `Deployments` quanto `StatefulSets` que possuam uma determinada anotação de observabilidade ou backup).

## Como verificar
Adicione a anotação monitorada em um `StatefulSet` de teste e confirme que o `DecoratorController` cria imediatamente os `Services` anexos retornados pelo webhook.

## Conexões
- [[metacontroller-compositecontroller-parent-child-sync-hook-crd]] — Veja também: Metacontroller `CompositeController`: gerenciamento de recursos filhos (`childResources`) a partir de um `parentResource`.
- [[metacontroller-contrato-sync-webhook-request-response-json]] — Veja também: Metacontroller: contrato JSON de entrada e saída do webhook `sync` para reconciliação declarativa.

## Fontes
- [Metacontroller GitHub — README.md (Lightweight Custom Controllers via JSON Webhooks in Any Language)](https://metacontroller.github.io/metacontroller/concepts.html) — README oficial do metacontroller/metacontroller apresentando escrita de controladores sem boilerplate em qualquer linguagem e instalação via Kustomize/Helm; consultado em 2026-10-03.
- [Metacontroller Official Documentation — Concepts (Canonical Plural Resources, API Groups/Versions/Kinds, Lambda Controllers & Hooks)](https://raw.githubusercontent.com/metacontroller/metacontroller/master/README.md) — Documentação oficial de conceitos do Metacontroller explicando recursos plurais canônicos, CompositeController, DecoratorController e hooks sync/finalize/customize; consultado em 2026-10-03.
- [Metacontroller — Official GitHub Repository](https://github.com/metacontroller/metacontroller) — Repositório oficial Apache-2.0 do Metacontroller; consultado em 2026-10-03.
