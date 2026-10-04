---
id: software.devops.tranche13.001229
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
fontes: ["https://raw.githubusercontent.com/project-zot/zot/main/examples/README.md", "https://raw.githubusercontent.com/project-zot/zot/main/README.md", "https://github.com/project-zot/zot"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Project Zot: Verificação de Integridade de Blobs (scrub), Linting de Imagens (lint) e Métricas Prometheus

## Em uma frase
O bloco `extensions` do `zot` inclui verificação periódica de integridade física de blobs em disco (`scrub`), validação de políticas de metadados de imagem no push (`lint`), exportação de métricas Prometheus (`metrics`) e gravação de eventos (`events`).

## Por que importa
Corrupção silenciosa de blocos em discos locais (bit rot) só é descoberta quando um nó tenta baixar uma camada antiga durante uma emergência e falha na verificação do digest SHA-256.

## Como funciona
A extensão `scrub` recalcula periodicamente em background os digests SHA-256 dos blobs armazenados e registra qualquer corrupção nos logs; a extensão `lint` permite exigir anotações OCI obrigatórias (como `org.opencontainers.image.licenses` ou autor) ao receber novos manifestos; e `metrics` expõe indicadores de latência HTTP, armazenamento e downloads no endpoint `/metrics`.

## Exemplo
```json
{
  "extensions": {
    "metrics": {
      "enable": true,
      "prometheus": {
        "path": "/metrics"
      }
    },
    "scrub": {
      "enable": true,
      "interval": "24h"
    }
  }
}
```

## Limites e trade-offs
Definir um `interval` muito curto na extensão `scrub` (como `15m`) em um registry de vários terabytes gera leitura contínua de disco e IOPS elevados no backend de armazenamento.

## Como verificar
Configure `scrub.interval` para ciclos diários ou semanais (`"24h"` ou `"168h"`) e monitore as métricas do `/metrics` no Prometheus.

## Conexões
- [[zot-storage-driver-s3-dynamodb-cache-fastrestart-cluster]] — Veja também: Project Zot: Backend S3, Cache Driver, fastRestart e Escalonamento Horizontal em Cluster.
- [[zot-implantacao-kubernetes-mirror-containerd-pull-through]] — Veja também: Project Zot: Implantação no Kubernetes como Mirror OCI Local para containerd.

## Fontes
- [Project Zot GitHub — README.md (OCI-Native Distribution & Image Spec Implementation, Single Binary & Built-in Extensions)](https://raw.githubusercontent.com/project-zot/zot/main/examples/README.md) — README oficial do project-zot/zot (Apache-2.0) detalhando a arquitetura OCI-only sem camadas Docker legadas, empacotamento em binário único com extensões embutidas e binário minimal; consultado em 2026-10-03.
- [Project Zot Official Examples — examples/README.md (Config Matrix: Storage, Auth, TLS, Sync, Search, Scrub, Lint & Metrics)](https://raw.githubusercontent.com/project-zot/zot/main/README.md) — Catálogo oficial de configurações do Zot cobrindo storage local/S3, deduplicação, GC, htpasswd/LDAP/OIDC/mTLS, RBAC, replicação on-demand e métricas; consultado em 2026-10-03.
- [Project Zot — Official GitHub Repository](https://github.com/project-zot/zot) — Repositório oficial CNCF Sandbox do Project Zot; consultado em 2026-10-03.
