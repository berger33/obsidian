---
id: software.devops.tranche13.001269
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-13.md"
fontes: ["https://distribution.github.io/distribution/about/configuration/", "https://raw.githubusercontent.com/distribution/distribution/main/README.md", "https://github.com/distribution/distribution"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# CNCF Distribution: Sistema de Notificações por Webhook (notifications.endpoints) e Filas de Eventos

## Em uma frase
A seção `notifications` do Distribution emite eventos estruturados via HTTP Webhook sempre que manifestos ou blobs sofrem push, pull ou delete, permitindo acionar scanners de vulnerabilidades, conversores Nydus, pré-aquecimento Dragonfly ou auditoria de supply chain.

## Por que importa
Fazer polling contínuo na API `/v2/_catalog` e nas listas de tags para descobrir se uma nova imagem foi publicada é lento e ineficiente em registros grandes.

## Como funciona
Cada endpoint em `notifications.endpoints` define `name`, `url`, `headers` de autorização, `timeout`, `threshold`, `backoff` e filtros `ignore` (por `mediaTypes` ou `actions`, permitindo ignorar eventos `pull` de alto volume e notificar apenas `push` e `delete` de manifestos).

## Exemplo
```yaml
notifications:
  events:
    includereferences: true
  endpoints:
    - name: security-scanner-webhook
      url: https://scanner.internal.corp/api/v1/registry-events
      timeout: 500ms
      threshold: 5
      backoff: 1s
      ignore:
        actions:
          - pull
```

## Limites e trade-offs
Não incluir `"pull"` em `ignore.actions` de um webhook síncrono em um cluster movimentado gera milhares de chamadas HTTP por minuto para o receptor de eventos a cada camada baixada pelos nós.

## Como verificar
Ignore a ação `pull` (`ignore.actions: [pull]`) nos webhooks que precisam reagir apenas à publicação (`push`) ou remoção (`delete`) de imagens.

## Conexões
- [[distribution-pull-through-cache-proxy-remoteurl-docker-hub]] — Veja também: CNCF Distribution: Configuração de Pull-Through Cache (proxy.remoteurl) para Espelhamento de Registries.
- [[distribution-http-debug-prometheus-healthchecks-draintimeout]] — Veja também: CNCF Distribution: Servidor de Debug, Métricas Prometheus, Health Checks e Graceful Shutdown (draintimeout).

## Fontes
- [CNCF Distribution Official Documentation — Configuration Reference (/etc/distribution/config.yml, REGISTRY_* Env Vars, Storage, Auth & Proxy)](https://distribution.github.io/distribution/about/configuration/) — Referência oficial de configuração do CNCF Distribution detalhando drivers de storage (filesystem, s3, gcs, azure), cache Redis, auth (token/JWKS/htpasswd), proxy pull-through, webhooks e OpenTelemetry; consultado em 2026-10-03.
- [CNCF Distribution GitHub — README.md (OCI Distribution Spec Implementation, registry:3 Image & Architecture)](https://raw.githubusercontent.com/distribution/distribution/main/README.md) — README oficial do distribution/distribution (Apache-2.0) explicando o papel do projeto como motor base do ecossistema de container registries; consultado em 2026-10-03.
- [CNCF Distribution — Official GitHub Repository](https://github.com/distribution/distribution) — Repositório oficial do CNCF Distribution; consultado em 2026-10-03.
