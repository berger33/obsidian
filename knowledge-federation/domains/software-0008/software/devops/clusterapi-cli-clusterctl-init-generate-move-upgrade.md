---
id: software.devops.tranche09.000829
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-09.md"
fontes: ["https://raw.githubusercontent.com/kubernetes-sigs/cluster-api/main/README.md", "https://cluster-api.sigs.k8s.io/user/quick-start.html", "https://github.com/kubernetes-sigs/cluster-api"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kubernetes Cluster API: operações de ciclo de vida do Management Cluster com a CLI clusterctl (init, generate, move, upgrade)

## Em uma frase
A ferramenta de linha de comando oficial `clusterctl` gerencia o ciclo de vida do próprio Management Cluster e seus provedores (`clusterctl init`, `upgrade`), gera manifestos de Workload Clusters (`generate cluster`), inspeciona árvores de saúde (`describe`) e migra a gestão entre clusters (`move`).

## Por que importa
Um desafio clássico de bootstrapping (o problema do ovo e da galinha) é: *"Se o Cluster API precisa de um Management Cluster Kubernetes para criar clusters Kubernetes, como eu crio o primeiro Management Cluster?"*. A CLI `clusterctl`, documentada no Quick Start do `Cluster API Book`, resolve esse fluxo com o comando `clusterctl move`.

## Como funciona
O fluxo de bootstrapping e operação com **`clusterctl`** compreende: (1) **`clusterctl init --infrastructure <provider>`**: instala os certificados, CRDs e controladores do Cluster API em um cluster Kubernetes existente (que pode ser um cluster temporário local criado com **`kind`** na máquina do administrador); (2) **`clusterctl generate cluster <nome> --kubernetes-version v1.35.0`**: renderiza os manifestos YAML do novo cluster; (3) **`clusterctl get kubeconfig <nome>`**: extrai o `kubeconfig` de administrador do Workload Cluster criado; (4) **`clusterctl move --to-kubeconfig <kubeconfig-destino>`**: transfere de forma atômica todos os CRDs, objetos `Cluster`/`Machine`, Secrets PKI e referências do cluster bootstrap (`kind`) para um Management Cluster definitivo em produção (permitindo destruir o cluster `kind` temporário); e (5) **`clusterctl upgrade plan` / `apply`**: atualiza as versões dos provedores CAPI.

## Exemplo
```bash
# Gerar o manifesto de um Workload Cluster, extrair seu kubeconfig e planejar upgrade dos providers CAPI
clusterctl generate cluster prod-01 --kubernetes-version v1.35.0 --control-plane-machine-count=3 --worker-machine-count=3 > prod-01.yaml
clusterctl get kubeconfig prod-01 > prod-01.kubeconfig
clusterctl upgrade plan
```

## Limites e trade-offs
Antes de executar `clusterctl move --to-kubeconfig <destino>`, o cluster de destino já precisa ter sido inicializado com `clusterctl init` contendo exatamente a mesma combinação (e versões compatíveis) de provedores de Infrastructure, Bootstrap e Control Plane que existem no cluster de origem, e todas as máquinas devem estar em estado estável (sem rollouts em andamento).

## Como verificar
Execute `clusterctl upgrade plan` no Management Cluster para verificar o contrato de API (`v1beta1` / `v1beta2`) e se há novas versões disponíveis para os provedores instalados.

## Conexões
- [[clusterapi-topologia-clusterclass-ponto-unico-controle]] — Veja também: Kubernetes Cluster API: reutilização de topologias e ponto único de controle com ClusterClass.
- [[clusterapi-integracao-talos-k3s-microvms-gitops-frota]] — Veja também: Kubernetes Cluster API: integração com provedores alternativos (Talos, K3s, MicroVMs) e gestão GitOps de frotas.
- [[clusterapi-arquitetura-declarativa-ciclo-vida-clusters-kubernetes]] — Referência cruzada direta com clusterapi-arquitetura-declarativa-ciclo-vida-clusters-kubernetes.
- [[clusterapi-provedores-infraestrutura-bootstrap-control-plane]] — Referência cruzada direta com clusterapi-provedores-infraestrutura-bootstrap-control-plane.
- [[kind-clusters-kubernetes-locais-containers-docker-arquitetura]] — Referência cruzada direta com kind-clusters-kubernetes-locais-containers-docker-arquitetura.

## Fontes
- [Cluster API GitHub — README.md (Declarative Kubernetes-style APIs, Goals, Non-Goals & Supported Providers)](https://raw.githubusercontent.com/kubernetes-sigs/cluster-api/main/README.md) — README oficial do Kubernetes Cluster API (CAPI) detalhando objetivos, escopo declarativo e lista de provedores de infraestrutura e bootstrap; consultado em 2026-10-03.
- [Cluster API Book — Concepts & Quick Start (Management/Workload Clusters, clusterctl, MachineDeployment & ClusterClass)](https://cluster-api.sigs.k8s.io/user/quick-start.html) — Documentação oficial do Cluster API cobrindo Management Cluster, Workload Cluster, Providers, Machine, MachineSet, MachineDeployment, Bootstrap com cloud-init, ClusterClass e comandos clusterctl; consultado em 2026-10-03.
- [Kubernetes SIGs Cluster API — Official GitHub Repository](https://github.com/kubernetes-sigs/cluster-api) — Repositório oficial Apache-2.0 do projeto kubernetes-sigs/cluster-api; consultado em 2026-10-03.
