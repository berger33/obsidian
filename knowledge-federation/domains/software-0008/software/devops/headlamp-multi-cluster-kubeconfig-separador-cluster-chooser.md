---
id: software.devops.tranche14.001323
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

# Headlamp: Operação Multi-Cluster com Múltiplos Arquivos Kubeconfig

## Em uma frase
O Headlamp suporta gerenciamento **multi-cluster** nativo tanto no aplicativo Desktop quanto no modo in-cluster, permitindo alternar entre clusters ou montar múltiplos arquivos `kubeconfig` simultaneamente separados por dois-pontos (`:`).

## Por que importa
Equipes de plataforma que administram clusters de desenvolvimento, homologação e múltiplas regiões de produção precisam comparar workloads sem abrir dezenas de janelas de navegador separadas.

## Como funciona
Por padrão no modo in-cluster, o Headlamp utiliza a ServiceAccount do namespace onde foi implantado e gera um contexto chamado `main`. Para conectar clusters adicionais, monta-se o arquivo em `/home/headlamp/.config/Headlamp/kubeconfigs/config`, passa-se o argumento `-kubeconfig` ou define-se a variável de ambiente `KUBECONFIG=/caminho/cluster1:/caminho/cluster2` via `values.env` do Helm chart.

## Exemplo
```yaml
# Exemplo de values.yaml do Helm chart com multiplos arquivos kubeconfig:
env:
  - name: KUBECONFIG
    value: "/home/headlamp/.config/Headlamp/kubeconfigs/cluster-a:/home/headlamp/.config/Headlamp/kubeconfigs/cluster-b"
```

## Limites e trade-offs
Usar o separador de caminhos do Windows (`;`) na variável `KUBECONFIG` dentro do container Linux do Headlamp impede o carregamento dos múltiplos arquivos.

## Como verificar
No container Linux do Headlamp, separe sempre múltiplos caminhos na variável `KUBECONFIG` usando dois-pontos (`:`).

## Conexões
- [[headlamp-rbac-ui-dinamica-serviceaccount-tokens-permissoes]] — Veja também: Headlamp: Controles de UI Orientados por RBAC e Acesso via ServiceAccount Tokens.
- [[headlamp-cluster-inventory-api-clusterprofile-secretreader]] — Veja também: Headlamp: Descoberta Dinâmica de Clusters via Cluster Inventory API (ClusterProfile e secretreader).

## Fontes
- [Headlamp GitHub — README.md (Kubernetes SIG UI Web & Desktop App, RBAC-Aware Controls, Multi-Cluster & Plugins)](https://headlamp.dev/docs/latest/installation/in-cluster/) — README oficial do kubernetes-sigs/headlamp (Apache-2.0) detalhando funcionalidades multi-cluster, reflexão de permissões RBAC na UI, terminal/logs/editor e ecossistema de plugins no Artifact Hub; consultado em 2026-10-03.
- [Headlamp Official Documentation — In-Cluster Installation (Helm Chart, Cluster Inventory API, Multiple Kubeconfigs, TLS, OIDC & pluginsManager Sidecar)](https://raw.githubusercontent.com/kubernetes-sigs/headlamp/main/README.md) — Guia oficial de implantação in-cluster do Headlamp cobrindo Helm chart, descoberta via ClusterProfile/secretreader, variáveis KUBECONFIG e sidecar pluginsManager; consultado em 2026-10-03.
- [Headlamp — Official GitHub Repository](https://github.com/kubernetes-sigs/headlamp) — Repositório oficial do Headlamp no Kubernetes SIG UI; consultado em 2026-10-03.
