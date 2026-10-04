---
id: software.devops.tranche18.001780
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

# Metacontroller: instalação via Kustomize/Helm, métricas de reconciliação e migração a partir do projeto GKE original

## Em uma frase
O projeto comunitário `metacontroller/metacontroller` oferece instalação oficial via **Kustomize** (`manifests/production`) e **Helm**, exportando métricas Prometheus detalhadas da fila de trabalho e das chamadas de webhook HTTP.

## Por que importa
Clusters que ainda rodam a versão legada `GoogleCloudPlatform/metacontroller` (arquivada) não recebem suporte às versões recentes da API do Kubernetes nem melhorias de performance e observabilidade da versão comunitária v4+.

## Como funciona
O Metacontroller comunitário roda como um `StatefulSet` (`metacontroller-0` no namespace `metacontroller`), requerendo permissões RBAC para observar os recursos gerenciados e gerenciar seus filhos. A migração a partir da versão legada do GKE consiste em atualizar os CRDs de `metacontroller.k8s.io/v1alpha1` e substituir o workload pelo manifesto de produção atual.

## Exemplo
```bash
helm install metacontroller oci://ghcr.io/metacontroller/metacontroller-helm \
  --version v4.11.20 \
  --namespace metacontroller --create-namespace
kubectl logs -n metacontroller sts/metacontroller --tail=30
```

## Limites e trade-offs
Certifique-se de que a `ServiceAccount` associada ao `StatefulSet` do Metacontroller possua permissões RBAC (`get`, `list`, `watch`, `create`, `update`, `patch`, `delete`) para todos os tipos de `parentResource`, `childResources` e `attachments` que você registrar.

## Como verificar
Verifique o estado do `sts/metacontroller` e consulte os logs estruturados do controlador para auditar o registro dinâmico dos seus controladores.

## Conexões
- [[metacontroller-jsonnet-python-javascript-hooks-configmap-sidecar]] — Veja também: Metacontroller: escrita de hooks declarativos enxutos em Jsonnet, Python ou Node.js montados via ConfigMap.

## Fontes
- [Metacontroller GitHub — README.md (Lightweight Custom Controllers via JSON Webhooks in Any Language)](https://raw.githubusercontent.com/metacontroller/metacontroller/master/README.md) — README oficial do metacontroller/metacontroller apresentando escrita de controladores sem boilerplate em qualquer linguagem e instalação via Kustomize/Helm; consultado em 2026-10-03.
- [Metacontroller Official Documentation — Concepts (Canonical Plural Resources, API Groups/Versions/Kinds, Lambda Controllers & Hooks)](https://metacontroller.github.io/metacontroller/concepts.html) — Documentação oficial de conceitos do Metacontroller explicando recursos plurais canônicos, CompositeController, DecoratorController e hooks sync/finalize/customize; consultado em 2026-10-03.
- [Metacontroller — Official GitHub Repository](https://github.com/metacontroller/metacontroller) — Repositório oficial Apache-2.0 do Metacontroller; consultado em 2026-10-03.
