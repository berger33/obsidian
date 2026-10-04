---
id: software.devops.tranche09.000834
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

# kind: configuração declarativa de clusters multi-nós, Control Plane HA e extraPortMappings (kind.x-k8s.io/v1alpha4)

## Em uma frase
Através de um arquivo de configuração (`apiVersion: kind.x-k8s.io/v1alpha4`, `kind: Cluster`) passado em `kind create cluster --config`, o `kind` provisiona topologias multi-nós (múltiplos `worker`s e múltiplos `control-plane`s em HA com load balancer) e mapeia portas para o host via `extraPortMappings`.

## Por que importa
Um cluster de nó único não permite testar afinidade/anti-afinidade entre nós (`topologySpreadConstraints`), drenagem de nós (`kubectl drain`), Kubernetes Descheduler, falha de um nó de control plane em HA ou roteamento de um Ingress Controller diretamente nas portas `80`/`443` do `localhost`. A seção `Configuring Your kind Cluster` do `Quick Start` oficial documenta todas essas configurações.

## Como funciona
No manifesto `kind: Cluster` (`apiVersion: kind.x-k8s.io/v1alpha4`), a lista **`nodes:`** define o papel de cada container nó: (1) **Multi-node**: um item `- role: control-plane` seguido de múltiplos itens `- role: worker`; (2) **Control-plane HA**: múltiplos itens `- role: control-plane` (por exemplo, 3 control-planes e 3 workers), fazendo o `kind` iniciar automaticamente um container extra de balanceador de carga HAProxy (`<cluster>-external-load-balancer`) na frente dos control-planes; e (3) **`extraPortMappings`**: dentro de um nó, mapeia portas do container do nó (`containerPort: 80`) para a máquina host (`hostPort: 80`, `listenAddress: "0.0.0.0"`, `protocol: tcp` ou `udp`), viabilizando acesso direto a `NodePort`, DaemonSets com `hostPort` ou Ingress Controllers.

## Exemplo
```yaml
# Arquivo kind-config.yaml criando um cluster com 1 control-plane (mapeando porta 80/443 para o host) e 2 workers
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
  - role: control-plane
    extraPortMappings:
      - containerPort: 80
        hostPort: 8080
        protocol: TCP
  - role: worker
  - role: worker
```

## Limites e trade-offs
Como os `extraPortMappings` são configurados na criação do container Docker do nó, você não pode adicionar novas portas mapeadas a um cluster `kind` depois que ele já foi criado sem recriar o cluster; além disso, em clusters com múltiplos nós workers, se um Ingress Controller rodar em um worker diferente daquele que tem o `extraPortMappings` (tipicamente o `control-plane`), deve-se usar seletores de nó (`nodeSelector: {"ingress-ready": "true"}`) conforme o guia de Ingress do `kind`.

## Como verificar
Crie o cluster com `kind create cluster --config kind-config.yaml`, execute `kubectl get nodes` para ver os 3 nós (`control-plane`, `worker`, `worker2`) e verifique com `docker port kind-control-plane` o mapeamento da porta `8080`.

## Conexões
- [[kind-carregamento-imagens-locais-load-docker-image-archive]] — Veja também: kind: carregamento direto de imagens locais para dentro do cluster (kind load docker-image e image-archive).
- [[kind-versoes-kubernetes-digests-sha256-feature-gates-proxy]] — Veja também: kind: fixação de versões do Kubernetes por digest SHA-256, habilitação de Feature Gates e uso de Proxy.
- [[kind-clusters-kubernetes-locais-containers-docker-arquitetura]] — Referência cruzada direta com kind-clusters-kubernetes-locais-containers-docker-arquitetura.

## Fontes
- [kind GitHub — README.md (Kubernetes IN Docker, Go Packages & Design Principles)](https://raw.githubusercontent.com/kubernetes-sigs/kind/main/README.md) — README oficial do projeto kind (Kubernetes SIGs, Apache-2.0) sobre execução de nós em containers para testes do próprio Kubernetes e CI/CD; consultado em 2026-10-03.
- [kind Official Documentation — Quick Start (Installation, Multi-Node Config, Building & Loading Images, Exporting Logs)](https://kind.sigs.k8s.io/docs/user/quick-start/) — Guia oficial Quick Start do kind cobrindo instalação, criação/exclusão de clusters, imagens kindest/node com digest SHA-256, topologia multi-nó kind.x-k8s.io/v1alpha4, kind build node-image, kind load docker-image/image-archive e kind export logs; consultado em 2026-10-03.
- [Kubernetes SIGs kind — Official GitHub Repository](https://github.com/kubernetes-sigs/kind) — Repositório oficial do kind mantido pelo Kubernetes SIG Testing; consultado em 2026-10-03.
