---
id: software.devops.tranche09.000831
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
fontes: ["https://raw.githubusercontent.com/kubernetes-sigs/kind/main/README.md", "https://kind.sigs.k8s.io/docs/user/quick-start/", "https://github.com/kubernetes-sigs/kind"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# kind (Kubernetes IN Docker): execução de clusters Kubernetes locais usando containers como nós

## Em uma frase
O `kind` (`kubernetes-sigs/kind`, sigla para *Kubernetes IN Docker*) é uma ferramenta certificada pela CNCF que executa clusters Kubernetes locais usando containers (`docker`, `podman` ou `nerdctl`) como "nós" inicializados com `kubeadm`.

## Por que importa
O `kind` foi projetado originalmente pelo Kubernetes SIG-Testing para testar o próprio código-fonte do Kubernetes em pipelines de integração contínua sem exigir máquinas virtuais pesadas ou infraestrutura de nuvem, tornando-se rapidamente o padrão da indústria tanto para testes automatizados em CI quanto para desenvolvimento local e bootstrapping do Cluster API. O README oficial e o `Quick Start` (`kind.sigs.k8s.io`) detalham sua arquitetura.

## Como funciona
Conforme documenta o README oficial, o `kind` consiste em: (1) pacotes Go (`pkg/cluster`, `pkg/build`) que implementam a criação de clusters e construção de imagens; (2) a interface de linha de comando **`kind`**; e (3) imagens de container especiais (**`base-image`** e **`node-image`**, publicadas no Docker Hub como **`kindest/node`**) projetadas para rodar `systemd`, `containerd`, `kubelet` e os componentes do Kubernetes dentro de um container privilegiado. Quando o usuário executa `kind create cluster`, o `kind` detecta automaticamente o runtime instalado (`docker`, `podman` ou `nerdctl`), inicia o(s) container(s) `kindest/node` e faz o bootstrap de cada "nó" com **`kubeadm`**.

## Exemplo
```bash
# Criar um cluster Kubernetes local com o nome padrão (kind), aguardar até 60s pela prontidão e listar os clusters
kind create cluster --wait 60s
kind get clusters
kubectl cluster-info --context kind-kind
```

## Limites e trade-offs
Conforme documentado no guia oficial `Quick Start`, ao usar `--wait` no `kind create cluster`, é obrigatório especificar a unidade de tempo (ex.: `--wait 30s` ou `--wait 5m`); além disso, o `podman` e o `nerdctl` operam em modo **rootless** por padrão, o que exige configuração adicional de delegação de cgroup v2 (`Delegate=yes` no systemd para CPU/memória/pids) no host Linux para que os containers `kindest/node` funcionem plenamente.

## Como verificar
Execute `kind get clusters` e `docker ps --filter "label=io.x-k8s.kind.cluster"` para verificar o container `kind-control-plane` em execução e o contexto `kind-kind` no `kubectl`.

## Conexões
- [[kind-gerenciamento-clusters-contextos-kubeconfig-delete]] — Veja também: kind: gerenciamento de múltiplos clusters (--name), regras de merge do KUBECONFIG e deleção idempotente.
- [[kind-carregamento-imagens-locais-load-docker-image-archive]] — Referência cruzada direta com kind-carregamento-imagens-locais-load-docker-image-archive.
- [[kind-configuracao-multinode-control-plane-ha-port-mappings]] — Referência cruzada direta com kind-configuracao-multinode-control-plane-ha-port-mappings.

## Fontes
- [kind GitHub — README.md (Kubernetes IN Docker, Go Packages & Design Principles)](https://raw.githubusercontent.com/kubernetes-sigs/kind/main/README.md) — README oficial do projeto kind (Kubernetes SIGs, Apache-2.0) sobre execução de nós em containers para testes do próprio Kubernetes e CI/CD; consultado em 2026-10-03.
- [kind Official Documentation — Quick Start (Installation, Multi-Node Config, Building & Loading Images, Exporting Logs)](https://kind.sigs.k8s.io/docs/user/quick-start/) — Guia oficial Quick Start do kind cobrindo instalação, criação/exclusão de clusters, imagens kindest/node com digest SHA-256, topologia multi-nó kind.x-k8s.io/v1alpha4, kind build node-image, kind load docker-image/image-archive e kind export logs; consultado em 2026-10-03.
- [Kubernetes SIGs kind — Official GitHub Repository](https://github.com/kubernetes-sigs/kind) — Repositório oficial do kind mantido pelo Kubernetes SIG Testing; consultado em 2026-10-03.
