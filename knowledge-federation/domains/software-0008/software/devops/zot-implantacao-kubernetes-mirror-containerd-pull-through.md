---
id: software.devops.tranche13.001230
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

# Project Zot: Implantação no Kubernetes como Mirror OCI Local para containerd

## Em uma frase
Implantado no Kubernetes via Helm chart (`project-zot/helm-charts`), o `zot` com `extensions.sync` (`onDemand: true`) funciona como um registry mirror local de baixa latência para os nós `containerd` do cluster.

## Por que importa
Quando um Deployment de 200 réplicas escala ou um novo nó entra no cluster, buscar as mesmas imagens repetidamente através de links WAN ou NAT Gateways encarece o tráfego de rede e atrasa o startup dos Pods.

## Como funciona
Configurando `hosts.toml` no `containerd` dos nós para apontar os registros upstream (como `docker.io`, `ghcr.io`, `quay.io`) para o endpoint interno do `zot` com `onDemand: true`, a primeira requisição busca e armazena a imagem no `zot` local, e todas as requisições subsequentes dos demais nós são servidas diretamente dentro da rede local do cluster.

## Exemplo
```toml
# /etc/containerd/certs.d/ghcr.io/hosts.toml nos nos do cluster:
server = "https://ghcr.io"

[host."https://zot.registry-system.svc.cluster.local:5000"]
  capabilities = ["pull", "resolve"]
```

## Limites e trade-offs
Configurar o `zot` como mirror no `containerd` usando um `PersistentVolume` pequeno sem habilitar `"gc": true` e política de retenção faz o disco do mirror encher e interromper novos cacheamentos.

## Como verificar
Habilite sempre `"gc": true`, `"dedupe": true` e políticas de retenção por último pull no `zot` quando operá-lo como cache mirror de cluster.

## Conexões
- [[zot-extensoes-scrub-lint-metrics-eventos-observabilidade]] — Veja também: Project Zot: Verificação de Integridade de Blobs (scrub), Linting de Imagens (lint) e Métricas Prometheus.

## Fontes
- [Project Zot GitHub — README.md (OCI-Native Distribution & Image Spec Implementation, Single Binary & Built-in Extensions)](https://raw.githubusercontent.com/project-zot/zot/main/examples/README.md) — README oficial do project-zot/zot (Apache-2.0) detalhando a arquitetura OCI-only sem camadas Docker legadas, empacotamento em binário único com extensões embutidas e binário minimal; consultado em 2026-10-03.
- [Project Zot Official Examples — examples/README.md (Config Matrix: Storage, Auth, TLS, Sync, Search, Scrub, Lint & Metrics)](https://raw.githubusercontent.com/project-zot/zot/main/README.md) — Catálogo oficial de configurações do Zot cobrindo storage local/S3, deduplicação, GC, htpasswd/LDAP/OIDC/mTLS, RBAC, replicação on-demand e métricas; consultado em 2026-10-03.
- [Project Zot — Official GitHub Repository](https://github.com/project-zot/zot) — Repositório oficial CNCF Sandbox do Project Zot; consultado em 2026-10-03.
