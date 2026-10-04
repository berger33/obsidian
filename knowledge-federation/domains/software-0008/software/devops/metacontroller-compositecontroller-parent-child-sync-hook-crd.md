---
id: software.devops.tranche18.001772
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

# Metacontroller `CompositeController`: gerenciamento de recursos filhos (`childResources`) a partir de um `parentResource`

## Em uma frase
O CRD **`CompositeController`** (`metacontroller.k8s.io/v1alpha1`) modela o padrão onde um objeto pai (tipicamente um Custom Resource, como um `BlueGreenDeployment` ou `IndexedJob`) é composto e gerencia o ciclo de vida de vários objetos filhos (`Deployments`, `Services`, `Pods`, `ConfigMaps`).

## Por que importa
Esse é o mesmo padrão arquitetural usado pelos controladores nativos do Kubernetes (como um `Deployment` que gerencia `ReplicaSets` ou um `StatefulSet` que gerencia `Pods` e `PVCs`), mas sem exigir programação de API do Kubernetes.

## Como funciona
No manifesto do `CompositeController`, o engenheiro declara `spec.parentResource` (usando sempre o nome canônico plural em minúsculas do recurso, ex.: `indexedjobs`), a lista `spec.childResources` e o endpoint `spec.hooks.sync.webhook.url`. A cada mudança no pai ou nos filhos, o Metacontroller envia `{parent, children}` em JSON para o webhook e aplica o `{status, children}` retornado.

## Exemplo
```yaml
apiVersion: metacontroller.k8s.io/v1alpha1
kind: CompositeController
metadata:
  name: webapp-composite-controller
spec:
  generateSelector: true
  parentResource:
    apiVersion: ctl.corp.io/v1
    resource: webapps
  childResources:
    - apiVersion: apps/v1
      resource: deployments
      updateStrategy:
        method: InPlace
    - apiVersion: v1
      resource: services
      updateStrategy:
        method: InPlace
  hooks:
    sync:
      webhook:
        url: http://webapp-hook.metacontroller/sync
```

## Limites e trade-offs
Quando o Metacontroller pede o nome de um recurso (`resource`) no spec do controlador, utilize sempre a forma canônica **plural e em minúsculas** (ex.: `replicasets`, `deployments`, `services`), enquanto dentro dos manifestos JSON retornados pelo hook usa-se o `kind` em `UpperCamelCase` (`ReplicaSet`, `Deployment`).

## Como verificar
Aplique um `CompositeController` e verifique nos logs do Pod `metacontroller-0` o início automático dos watches para o recurso pai e para os recursos filhos.

## Conexões
- [[metacontroller-arquitetura-lambda-controllers-webhooks-json]] — Veja também: Metacontroller: arquitetura de *Controller-Controller* para escrever operadores Kubernetes como Lambda Hooks JSON.
- [[metacontroller-decoratorcontroller-attachments-labels-annotations]] — Veja também: Metacontroller `DecoratorController`: anexação de comportamentos e recursos secundários a objetos existentes.

## Fontes
- [Metacontroller GitHub — README.md (Lightweight Custom Controllers via JSON Webhooks in Any Language)](https://metacontroller.github.io/metacontroller/concepts.html) — README oficial do metacontroller/metacontroller apresentando escrita de controladores sem boilerplate em qualquer linguagem e instalação via Kustomize/Helm; consultado em 2026-10-03.
- [Metacontroller Official Documentation — Concepts (Canonical Plural Resources, API Groups/Versions/Kinds, Lambda Controllers & Hooks)](https://raw.githubusercontent.com/metacontroller/metacontroller/master/README.md) — Documentação oficial de conceitos do Metacontroller explicando recursos plurais canônicos, CompositeController, DecoratorController e hooks sync/finalize/customize; consultado em 2026-10-03.
- [Metacontroller — Official GitHub Repository](https://github.com/metacontroller/metacontroller) — Repositório oficial Apache-2.0 do Metacontroller; consultado em 2026-10-03.
