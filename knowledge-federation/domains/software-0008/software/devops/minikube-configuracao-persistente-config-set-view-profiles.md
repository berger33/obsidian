---
id: software.devops.tranche09.000849
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

# Kubernetes minikube: configurações persistentes de perfil (minikube config set, view e unset)

## Em uma frase
O subcomando `minikube config` (`set`, `get`, `view`, `unset`) permite salvar preferências padrão persistentes (como `driver`, `cpus`, `memory`, `container-runtime` e `kubernetes-version`) para que o desenvolvedor não precise repetir flags em todo `minikube start`.

## Por que importa
Se a estação de trabalho do desenvolvedor exige sempre usar `cpus=4`, `memory=8192`, `driver=docker` e `container-runtime=containerd`, esquecer de passar uma dessas flags ao criar um novo cluster ou perfil faz o `minikube` usar os valores mínimos padrão (`2 CPUs` e `~2 GB RAM`), causando pressão de recursos nos pods.

## Como funciona
As configurações salvas com **`minikube config set <propriedade> <valor>`** são persistidas no arquivo de configuração global do usuário (`~/.minikube/config/config.json`). A partir desse momento, qualquer chamada futura a `minikube start` para criar um novo cluster aplicará automaticamente os valores definidos. O usuário pode listar todas as customizações ativas com **`minikube config view`** e remover uma preferência voltando ao padrão de fábrica com **`minikube config unset <propriedade>`**.

## Exemplo
```bash
# Definir padrões persistentes de memória, CPUs e container-runtime no minikube e visualizar a configuração salva
minikube config set memory 6144
minikube config set cpus 4
minikube config set container-runtime containerd
minikube config view
```

## Limites e trade-offs
Executar `minikube config set memory 6144` altera o valor padrão para novos clusters, mas **não redimensiona a quente** uma máquina virtual ou container de um cluster que já está criado e em execução; para aplicar a nova quantidade de memória/CPU a um cluster existente, é necessário parar e recriar (ou reiniciar conforme o suporte do driver) o perfil correspondente.

## Como verificar
Execute `minikube config view` para confirmar as propriedades gravadas e verifique com `kubectl describe node minikube` a capacidade de CPU e memória alocada após recriar o cluster.

## Conexões
- [[minikube-diagnostico-logs-ssh-ip-pause-unpause]] — Veja também: Kubernetes minikube: diagnóstico e economia de recursos com minikube logs, ssh, ip, pause e unpause.
- [[minikube-kubectl-embutido-node-add-multinode-topologias]] — Veja também: Kubernetes minikube: kubectl embutido na versão exata do cluster (minikube kubectl --) e gerenciamento multi-nós (minikube node).
- [[minikube-clusters-locais-kubernetes-perfis-controles-basicos]] — Referência cruzada direta com minikube-clusters-locais-kubernetes-perfis-controles-basicos.
- [[minikube-customizacao-apiserver-kubelet-codespaces-ci]] — Referência cruzada direta com minikube-customizacao-apiserver-kubelet-codespaces-ci.
- [[minikube-drivers-execucao-docker-kvm2-qemu-vfkit-none]] — Referência cruzada direta com minikube-drivers-execucao-docker-kvm2-qemu-vfkit-none.

## Fontes
- [minikube GitHub — README.md (Local Kubernetes, Multi-Platform Drivers & Design Principles)](https://raw.githubusercontent.com/kubernetes/minikube/master/README.md) — README oficial do projeto minikube detalhando objetivos de simplicidade e conformidade com recursos do Kubernetes local; consultado em 2026-10-03.
- [minikube Official Documentation — Basic Controls (start/pause/stop/delete, kubectl Wrapper, Addons, service/tunnel & profiles)](https://minikube.sigs.k8s.io/docs/handbook/controls/) — Documentação oficial Basic Controls do minikube cobrindo ciclo de vida de clusters, perfis (-p), wrapper minikube kubectl --, addons (dashboard, ingress, metrics-server), minikube service, minikube tunnel e minikube node/image/cache; consultado em 2026-10-03.
- [Kubernetes minikube — Official GitHub Repository](https://github.com/kubernetes/minikube) — Repositório oficial Apache-2.0 do minikube; consultado em 2026-10-03.
