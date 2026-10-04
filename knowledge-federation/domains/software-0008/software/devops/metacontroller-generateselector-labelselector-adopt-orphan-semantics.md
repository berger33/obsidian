---
id: software.devops.tranche18.001778
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
fontes: ["https://raw.githubusercontent.com/metacontroller/metacontroller/master/README.md", "https://metacontroller.github.io/metacontroller/concepts.html", "https://github.com/metacontroller/metacontroller"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Metacontroller: seleção de filhos com `generateSelector: true` vs `labelSelector` customizado e semântica de adoção

## Em uma frase
No `CompositeController`, o campo `spec.generateSelector` controla se o Metacontroller deve gerenciar automaticamente um seletor de labels único por objeto pai (`controller-uid`) ou usar o `spec.selector` declarado pelo próprio usuário no objeto pai (como fazem `Deployment` e `StatefulSet`).

## Por que importa
Se você estiver criando um CRD de alto nível onde o usuário final não quer se preocupar em inventar `matchLabels` exclusivos para cada instância, forçar o usuário a escrever `spec.selector` adiciona ruído desnecessário ao manifesto.

## Como funciona
Quando `spec.generateSelector: true` é definido no `CompositeController`, o Metacontroller injeta e filtra automaticamente os recursos filhos pelo UID do objeto pai, eliminando a necessidade de `spec.selector` no Custom Resource. Já quando `generateSelector: false` (padrão), o Metacontroller usa `spec.selector` do pai e suporta semântica completa de *adopt/orphan* (adotando órfãos que batam com os labels ou liberando filhos cujos labels deixem de bater).

## Exemplo
```yaml
apiVersion: metacontroller.k8s.io/v1alpha1
kind: CompositeController
metadata:
  name: simple-app-controller
spec:
  generateSelector: true
  parentResource:
    apiVersion: apps.corp.io/v1
    resource: simpleapps
```

## Limites e trade-offs
Para a maioria dos novos Custom Resources de plataforma, habilitar `generateSelector: true` é a escolha mais segura porque impede colisões acidentais de labels entre duas instâncias criadas no mesmo namespace.

## Como verificar
Inspecione os labels injetados automaticamente nos recursos filhos criados por um `CompositeController` com `generateSelector: true`.

## Conexões
- [[metacontroller-estrategias-atualizacao-filhos-ondelete-recreate-inplace-rolling]] — Veja também: Metacontroller: estratégias de atualização de recursos filhos (`OnDelete`, `Recreate`, `InPlace`, `RollingRecreate`, `RollingInPlace`).
- [[metacontroller-jsonnet-python-javascript-hooks-configmap-sidecar]] — Veja também: Metacontroller: escrita de hooks declarativos enxutos em Jsonnet, Python ou Node.js montados via ConfigMap.

## Fontes
- [Metacontroller GitHub — README.md (Lightweight Custom Controllers via JSON Webhooks in Any Language)](https://raw.githubusercontent.com/metacontroller/metacontroller/master/README.md) — README oficial do metacontroller/metacontroller apresentando escrita de controladores sem boilerplate em qualquer linguagem e instalação via Kustomize/Helm; consultado em 2026-10-03.
- [Metacontroller Official Documentation — Concepts (Canonical Plural Resources, API Groups/Versions/Kinds, Lambda Controllers & Hooks)](https://metacontroller.github.io/metacontroller/concepts.html) — Documentação oficial de conceitos do Metacontroller explicando recursos plurais canônicos, CompositeController, DecoratorController e hooks sync/finalize/customize; consultado em 2026-10-03.
- [Metacontroller — Official GitHub Repository](https://github.com/metacontroller/metacontroller) — Repositório oficial Apache-2.0 do Metacontroller; consultado em 2026-10-03.
