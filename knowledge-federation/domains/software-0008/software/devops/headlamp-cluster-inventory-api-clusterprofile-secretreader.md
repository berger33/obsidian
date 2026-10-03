---
id: software.devops.tranche14.001324
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

# Headlamp: Descoberta Dinâmica de Clusters via Cluster Inventory API (ClusterProfile e secretreader)

## Em uma frase
Quando implantado in-cluster via Helm chart, o Headlamp pode descobrir clusters dinamicamente a partir de recursos **`ClusterProfile`** da **Cluster Inventory API**, habilitando `config.clusterInventory.enabled: true` e configurando um provedor de acesso como o `secretreader`.

## Por que importa
Em plataformas multi-cluster onde novos clusters efêmeros ou de clientes são criados e destruídos diariamente (via Cluster API ou Crossplane), editar e remontar arquivos `kubeconfig` estáticos no Deployment do Headlamp não escala.

## Como funciona
O Helm chart configura o `accessProvidersConfig` (por exemplo, executando `/access-plugins/secretreader/secretreader-plugin` com `apiVersion: client.authentication.k8s.io/v1`) e monta o binário do provedor usando um volume Kubernetes do tipo `image` (`registry.k8s.io/cluster-inventory-api/secretreader:v0.1.1`). Por padrão, o Headlamp observa todos os objetos `ClusterProfile` que não possuem a label `headlamp.dev/ignore` (`labelSelector: !headlamp.dev/ignore`).

## Exemplo
```yaml
config:
  clusterInventory:
    enabled: true
    accessProvidersConfig:
      providers:
        - name: secretreader
          execConfig:
            apiVersion: client.authentication.k8s.io/v1
            command: /access-plugins/secretreader/secretreader-plugin
            provideClusterInfo: true
    plugins:
      - name: secretreader
        image: registry.k8s.io/cluster-inventory-api/secretreader:v0.1.1
        mountPath: /access-plugins/secretreader
```

## Limites e trade-offs
Confundir a lista `config.clusterInventory.plugins` (que são volumes de imagem contendo binários de provedor de credenciais de cluster) com os plugins visuais de interface do Headlamp (`pluginsManager`) leva a erros de montagem no Pod.

## Como verificar
Configure provedores de credenciais da Cluster Inventory API em `config.clusterInventory.plugins` e use a label `headlamp.dev/ignore: "true"` nos `ClusterProfile` que não devem aparecer na UI.

## Conexões
- [[headlamp-multi-cluster-kubeconfig-separador-cluster-chooser]] — Veja também: Headlamp: Operação Multi-Cluster com Múltiplos Arquivos Kubeconfig.
- [[headlamp-plugins-manager-sidecar-artifacthub-extensoes]] — Veja também: Headlamp: Gerenciamento de Plugins de UI In-Cluster via Sidecar (pluginsManager e Artifact Hub).

## Fontes
- [Headlamp GitHub — README.md (Kubernetes SIG UI Web & Desktop App, RBAC-Aware Controls, Multi-Cluster & Plugins)](https://headlamp.dev/docs/latest/installation/in-cluster/) — README oficial do kubernetes-sigs/headlamp (Apache-2.0) detalhando funcionalidades multi-cluster, reflexão de permissões RBAC na UI, terminal/logs/editor e ecossistema de plugins no Artifact Hub; consultado em 2026-10-03.
- [Headlamp Official Documentation — In-Cluster Installation (Helm Chart, Cluster Inventory API, Multiple Kubeconfigs, TLS, OIDC & pluginsManager Sidecar)](https://raw.githubusercontent.com/kubernetes-sigs/headlamp/main/README.md) — Guia oficial de implantação in-cluster do Headlamp cobrindo Helm chart, descoberta via ClusterProfile/secretreader, variáveis KUBECONFIG e sidecar pluginsManager; consultado em 2026-10-03.
- [Headlamp — Official GitHub Repository](https://github.com/kubernetes-sigs/headlamp) — Repositório oficial do Headlamp no Kubernetes SIG UI; consultado em 2026-10-03.
