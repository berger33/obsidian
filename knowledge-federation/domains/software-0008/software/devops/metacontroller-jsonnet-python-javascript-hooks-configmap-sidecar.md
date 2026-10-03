---
id: software.devops.tranche18.001779
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

# Metacontroller: escrita de hooks declarativos enxutos em Jsonnet, Python ou Node.js montados via ConfigMap

## Em uma frase
Como os hooks do Metacontroller são simples servidores HTTP stateless que transformam JSON em JSON, é prática comum empacotar o código do controlador em um `ConfigMap` e executá-lo em um Deployment leve de **Jsonnet**, **Python** ou **Node.js** no próprio namespace do Metacontroller.

## Por que importa
Em linguagens de templating de dados como **Jsonnet**, transformar o objeto JSON `{parent, children}` na estrutura JSON `{status, children}` exige apenas uma expressão funcional de 20 linhas sem precisar manter imagens de container compiladas customizadas.

## Como funciona
O administrador cria um `ConfigMap` com o script (`sync.py` ou `sync.jsonnet`), monta-o em um Pod com um servidor HTTP mínimo e aponta `webhook.url` para o `Service` local (`http://my-hook.metacontroller/sync`), configurando opcionalmente `webhook.timeout` e `resyncPeriodSeconds` no controlador.

## Exemplo
```yaml
apiVersion: metacontroller.k8s.io/v1alpha1
kind: CompositeController
metadata:
  name: cron-sync-controller
spec:
  resyncPeriodSeconds: 300
  parentResource:
    apiVersion: ops.corp.io/v1
    resource: envsyncs
  hooks:
    sync:
      webhook:
        url: http://envsync-hook.metacontroller:8080/sync
        timeout: 10s
```

## Limites e trade-offs
O parâmetro `resyncPeriodSeconds` força o Metacontroller a invocar o webhook `sync` periodicamente mesmo que nenhum objeto Kubernetes tenha mudado, sendo útil para controladores que sincronizam estado com sistemas externos.

## Como verificar
Configure `resyncPeriodSeconds` e `timeout` no seu controlador e monitore a latência das chamadas de webhook através das métricas Prometheus expostas pelo Metacontroller.

## Conexões
- [[metacontroller-generateselector-labelselector-adopt-orphan-semantics]] — Veja também: Metacontroller: seleção de filhos com `generateSelector: true` vs `labelSelector` customizado e semântica de adoção.
- [[metacontroller-observabilidade-metricas-logging-migracao-gke-helm]] — Veja também: Metacontroller: instalação via Kustomize/Helm, métricas de reconciliação e migração a partir do projeto GKE original.

## Fontes
- [Metacontroller GitHub — README.md (Lightweight Custom Controllers via JSON Webhooks in Any Language)](https://raw.githubusercontent.com/metacontroller/metacontroller/master/README.md) — README oficial do metacontroller/metacontroller apresentando escrita de controladores sem boilerplate em qualquer linguagem e instalação via Kustomize/Helm; consultado em 2026-10-03.
- [Metacontroller Official Documentation — Concepts (Canonical Plural Resources, API Groups/Versions/Kinds, Lambda Controllers & Hooks)](https://metacontroller.github.io/metacontroller/concepts.html) — Documentação oficial de conceitos do Metacontroller explicando recursos plurais canônicos, CompositeController, DecoratorController e hooks sync/finalize/customize; consultado em 2026-10-03.
- [Metacontroller — Official GitHub Repository](https://github.com/metacontroller/metacontroller) — Repositório oficial Apache-2.0 do Metacontroller; consultado em 2026-10-03.
