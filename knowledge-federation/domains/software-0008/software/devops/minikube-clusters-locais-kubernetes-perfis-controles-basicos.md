---
id: software.devops.tranche09.000841
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
fontes: ["https://raw.githubusercontent.com/kubernetes/minikube/master/README.md", "https://minikube.sigs.k8s.io/docs/handbook/controls/", "https://github.com/kubernetes/minikube"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kubernetes minikube: implementação de clusters Kubernetes locais em macOS, Linux e Windows e controles básicos

## Em uma frase
O `minikube` (`kubernetes/minikube`, projeto do Kubernetes SIG Cluster Lifecycle) implementa um cluster Kubernetes local no macOS, Linux e Windows com foco em ser a ferramenta mais completa para desenvolvimento local de aplicações Kubernetes.

## Por que importa
Desenvolvedores de aplicações precisam testar seus manifestos Kubernetes localmente usando recursos reais do Kubernetes — como `LoadBalancer`, `NodePort`, `PersistentVolumes`, `Ingress`, `Dashboard` e múltiplos runtimes de container (`containerd`, `CRI-O`, `Docker`) — tanto em VMs quanto em containers. O README oficial e a página `Basic controls` (`minikube.sigs.k8s.io/docs/handbook/controls/`) documentam o ciclo de vida completo do `minikube`.

## Como funciona
Com um único comando **`minikube start`**, o `minikube` detecta e provisiona um ambiente local (container ou máquina virtual via drivers como `docker`, `kvm2`, `qemu`, `hyperkit`, `vfkit`, `hyperv` ou `virtualbox`), instala a versão estável mais recente do Kubernetes (ou a especificada em `--kubernetes-version`) e configura automaticamente o contexto do `kubectl`. O operador pode pausar/parar o cluster com **`minikube stop`**, destruí-lo com **`minikube delete`** (ou remover todos os clusters e perfis locais com **`minikube delete --all`**) e atualizar o cluster existente executando **`minikube start --kubernetes-version=latest`**.

## Exemplo
```bash
# Iniciar um cluster minikube local, verificar o status e executar um segundo cluster isolado usando perfil (-p)
minikube start
minikube status
minikube start -p cluster2
```

## Limites e trade-offs
Conforme observa explicitamente a página oficial `Basic controls` (`minikube.sigs.k8s.io/docs/handbook/controls/`), o recurso de rodar múltiplos clusters locais simultâneos usando perfis (**`minikube start -p cluster2`**) **não funciona** se o `minikube` estiver usando o driver bare-metal (`--driver=none`), pois o driver `none` instala o Kubernetes diretamente no sistema operacional do host sem isolamento de container ou VM.

## Como verificar
Execute `minikube profile list` para listar todos os perfis de clusters locais criados na máquina e seus respectivos drivers, IPs e status.

## Conexões
- [[minikube-exposicao-servicos-service-nodeport-tunnel-loadbalancer]] — Veja também: Kubernetes minikube: acesso a serviços locais NodePort (minikube service) e LoadBalancer (minikube tunnel).
- [[minikube-addons-dashboard-gpu-mounts-container-runtimes]] — Referência cruzada direta com minikube-addons-dashboard-gpu-mounts-container-runtimes.
- [[kind-clusters-kubernetes-locais-containers-docker-arquitetura]] — Referência cruzada direta com kind-clusters-kubernetes-locais-containers-docker-arquitetura.

## Fontes
- [minikube GitHub — README.md (Local Kubernetes, Multi-Platform Drivers & Design Principles)](https://raw.githubusercontent.com/kubernetes/minikube/master/README.md) — README oficial do projeto minikube detalhando objetivos de simplicidade e conformidade com recursos do Kubernetes local; consultado em 2026-10-03.
- [minikube Official Documentation — Basic Controls (start/pause/stop/delete, kubectl Wrapper, Addons, service/tunnel & profiles)](https://minikube.sigs.k8s.io/docs/handbook/controls/) — Documentação oficial Basic Controls do minikube cobrindo ciclo de vida de clusters, perfis (-p), wrapper minikube kubectl --, addons (dashboard, ingress, metrics-server), minikube service, minikube tunnel e minikube node/image/cache; consultado em 2026-10-03.
- [Kubernetes minikube — Official GitHub Repository](https://github.com/kubernetes/minikube) — Repositório oficial Apache-2.0 do minikube; consultado em 2026-10-03.
