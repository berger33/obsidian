---
id: software.devops.tranche13.001270
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

# CNCF Distribution: Servidor de Debug, Métricas Prometheus, Health Checks e Graceful Shutdown (draintimeout)

## Em uma frase
Na seção `http.debug` e `health` do `config.yml`, o Distribution expõe um listener administrativo separado com métricas Prometheus (`http.debug.prometheus.enabled: true`), profiling pprof e verificações ativas de saúde de disco, HTTP e TCP que colocam o servidor em `503 Service Unavailable` caso o backend degrade.

## Por que importa
Se o sistema de arquivos ou o mount NFS onde o registry grava blobs ficar inacessível mas o processo HTTP principal continuar respondendo `200 OK` no load balancer, todos os pushes e pulls falharão silenciosamente.

## Como funciona
Configurando `http.draintimeout: 60s` (para aguardar o término de uploads em andamento antes de desligar o Pod no Kubernetes), `http.debug.addr: 0.0.0.0:5001` com `prometheus.enabled: true` (`path: /metrics`) e sondas em `health.storagedriver`, o Kubernetes monitora a saúde real do storage e coleta telemetria completa.

## Exemplo
```yaml
http:
  addr: 0.0.0.0:5000
  draintimeout: 60s
  debug:
    addr: 0.0.0.0:5001
    prometheus:
      enabled: true
      path: /metrics
health:
  storagedriver:
    enabled: true
    interval: 10s
    threshold: 3
```

## Limites e trade-offs
Expor a porta de `http.debug` (`5001`) no Ingress público junto com a porta `5000` vaza métricas internas e perfis de memória Go (`/debug/pprof`) sem autenticação.

## Como verificar
Mantenha a porta `5001` (`http.debug`) restrita exclusivamente à rede interna do cluster para coleta pelo Prometheus e sondas `livenessProbe`/`readinessProbe` do kubelet.

## Conexões
- [[distribution-notifications-webhooks-eventos-push-pull-delete]] — Veja também: CNCF Distribution: Sistema de Notificações por Webhook (notifications.endpoints) e Filas de Eventos.

## Fontes
- [CNCF Distribution Official Documentation — Configuration Reference (/etc/distribution/config.yml, REGISTRY_* Env Vars, Storage, Auth & Proxy)](https://distribution.github.io/distribution/about/configuration/) — Referência oficial de configuração do CNCF Distribution detalhando drivers de storage (filesystem, s3, gcs, azure), cache Redis, auth (token/JWKS/htpasswd), proxy pull-through, webhooks e OpenTelemetry; consultado em 2026-10-03.
- [CNCF Distribution GitHub — README.md (OCI Distribution Spec Implementation, registry:3 Image & Architecture)](https://raw.githubusercontent.com/distribution/distribution/main/README.md) — README oficial do distribution/distribution (Apache-2.0) explicando o papel do projeto como motor base do ecossistema de container registries; consultado em 2026-10-03.
- [CNCF Distribution — Official GitHub Repository](https://github.com/distribution/distribution) — Repositório oficial do CNCF Distribution; consultado em 2026-10-03.
