---
id: software.devops.tranche14.001325
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-14.md"
fontes: ["https://headlamp.dev/docs/latest/installation/in-cluster/", "https://raw.githubusercontent.com/kubernetes-sigs/headlamp/main/README.md", "https://github.com/kubernetes-sigs/headlamp"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Headlamp: Gerenciamento de Plugins de UI In-Cluster via Sidecar (pluginsManager e Artifact Hub)

## Em uma frase
O Headlamp possui uma arquitetura rica de plugins de interface (publicados no **Artifact Hub** sob o tipo Headlamp plugin e no repositório `headlamp-k8s/plugins`, como integrações para Flux, Cert-Manager, Karpenter, Backstage e Prometheus) gerenciáveis in-cluster por um container sidecar (`pluginsManager`).

## Por que importa
Construir uma imagem Docker customizada do Headlamp toda vez que a equipe deseja adicionar ou atualizar um plugin do Flux ou Karpenter cria sobrecarga de manutenção de imagens.

## Como funciona
No `values.yaml` do Helm chart, habilita-se `config.watchPlugins: true` (para recarregamento dinâmico) e `pluginsManager.enabled: true`, declarando em `pluginsManager.configContent` a lista de pacotes do Artifact Hub (`source`, `version`) e opções de instalação paralela (`installOptions.parallel: true`, `maxConcurrent: 2`).

## Exemplo
```yaml
config:
  watchPlugins: true
pluginsManager:
  enabled: true
  configContent: |
    plugins:
      - name: flux
        source: https://artifacthub.io/packages/headlamp/headlamp-plugins/headlamp_flux
        version: 0.3.0
    installOptions:
      parallel: true
      maxConcurrent: 2
  baseImage: node:lts-alpine
```

## Limites e trade-offs
Omitir a versão (`version`) dos plugins ou deixar `watchPlugins: false` quando o sidecar `pluginsManager` instala novos pacotes em tempo de execução impede o carregamento previsível das extensões.

## Como verificar
Fixe versões explícitas dos plugins do Artifact Hub em `pluginsManager.configContent` e mantenha `config.watchPlugins: true`.

## Conexões
- [[headlamp-cluster-inventory-api-clusterprofile-secretreader]] — Veja também: Headlamp: Descoberta Dinâmica de Clusters via Cluster Inventory API (ClusterProfile e secretreader).
- [[headlamp-autenticacao-oidc-ingress-tls-passthrough-backend]] — Veja também: Headlamp: Autenticação OIDC Corporativa, Ingress e Terminação TLS no Backend.

## Fontes
- [Headlamp GitHub — README.md (Kubernetes SIG UI Web & Desktop App, RBAC-Aware Controls, Multi-Cluster & Plugins)](https://headlamp.dev/docs/latest/installation/in-cluster/) — README oficial do kubernetes-sigs/headlamp (Apache-2.0) detalhando funcionalidades multi-cluster, reflexão de permissões RBAC na UI, terminal/logs/editor e ecossistema de plugins no Artifact Hub; consultado em 2026-10-03.
- [Headlamp Official Documentation — In-Cluster Installation (Helm Chart, Cluster Inventory API, Multiple Kubeconfigs, TLS, OIDC & pluginsManager Sidecar)](https://raw.githubusercontent.com/kubernetes-sigs/headlamp/main/README.md) — Guia oficial de implantação in-cluster do Headlamp cobrindo Helm chart, descoberta via ClusterProfile/secretreader, variáveis KUBECONFIG e sidecar pluginsManager; consultado em 2026-10-03.
- [Headlamp — Official GitHub Repository](https://github.com/kubernetes-sigs/headlamp) — Repositório oficial do Headlamp no Kubernetes SIG UI; consultado em 2026-10-03.
