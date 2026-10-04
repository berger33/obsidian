---
id: software.devops.tranche18.001771
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

# Metacontroller: arquitetura de *Controller-Controller* para escrever operadores Kubernetes como Lambda Hooks JSON

## Em uma frase
O **Metacontroller** (iniciado originalmente no Google Cloud Platform / GKE e mantido pela comunidade sob Apache 2.0) é um add-on leve para Kubernetes que permite escrever e implantar controladores customizados na forma de simples scripts/webhooks HTTP que recebem o estado atual em JSON e devolvem o estado desejado em JSON.

## Por que importa
Construir e manter um controlador completo em Go com `client-go`, Informers, caches em memória, filas de trabalho (`workqueues`) e lógica de concorrência otimista para cada pequena abstração interna de plataforma multiplica o custo de manutenção.

## Como funciona
Assim como o `kube-controller-manager` hospeda vários controladores nativos, o Metacontroller é um servidor "controlador de controladores" (*controller-controller*) que observa objetos de sua própria API (`CompositeController` e `DecoratorController`) e executa todos os loops de reconciliação, watches, caches, adoção/orfanato e Garbage Collection em nome do usuário, invocando apenas a função de negócio (*Lambda Hook*) via HTTP/JSON.

## Exemplo
```bash
kubectl apply -k https://github.com/metacontroller/metacontroller/manifests/production
kubectl get pods -n metacontroller
```

## Limites e trade-offs
Como o contrato entre o Metacontroller e o seu hook é puramente HTTP + JSON, você pode escrever controladores Kubernetes em **Python**, **JavaScript/Node.js**, **Jsonnet**, **Go**, **Ruby** ou **Rust** sem importar nenhuma biblioteca cliente do Kubernetes.

## Como verificar
Instale o Metacontroller e verifique com `kubectl get crds | grep metacontroller.k8s.io` o registro de `compositecontrollers` e `decoratorcontrollers`.

## Conexões
- [[metacontroller-compositecontroller-parent-child-sync-hook-crd]] — Veja também: Metacontroller `CompositeController`: gerenciamento de recursos filhos (`childResources`) a partir de um `parentResource`.

## Fontes
- [Metacontroller GitHub — README.md (Lightweight Custom Controllers via JSON Webhooks in Any Language)](https://raw.githubusercontent.com/metacontroller/metacontroller/master/README.md) — README oficial do metacontroller/metacontroller apresentando escrita de controladores sem boilerplate em qualquer linguagem e instalação via Kustomize/Helm; consultado em 2026-10-03.
- [Metacontroller Official Documentation — Concepts (Canonical Plural Resources, API Groups/Versions/Kinds, Lambda Controllers & Hooks)](https://metacontroller.github.io/metacontroller/concepts.html) — Documentação oficial de conceitos do Metacontroller explicando recursos plurais canônicos, CompositeController, DecoratorController e hooks sync/finalize/customize; consultado em 2026-10-03.
- [Metacontroller — Official GitHub Repository](https://github.com/metacontroller/metacontroller) — Repositório oficial Apache-2.0 do Metacontroller; consultado em 2026-10-03.
