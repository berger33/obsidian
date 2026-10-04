---
id: software.devops.tranche09.000840
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

# kind: compartilhamento de arquivos e dispositivos do host com os nós (extraMounts) e uso de registries locais

## Em uma frase
Na configuração de cada nó do `kind`, a lista `extraMounts` permite montar diretórios, sockets ou arquivos do sistema operacional hospedeiro (`hostPath`) para dentro do container do nó (`containerPath`), viabilizando volumes persistentes locais, compartilhamento de certificados e integração com registries.

## Por que importa
Como os Pods agendados dentro de um cluster `kind` enxergam como "host" (em volumes `hostPath`) o sistema de arquivos do container `kind-control-plane` / `kind-worker` e **não** o sistema de arquivos da máquina física do desenvolvedor, para compartilhar uma pasta de dados, certificados CA corporativos ou diretórios `/sys/kernel/debug` com os Pods é necessário mapeá-los primeiro do host físico para o container do nó.

## Como funciona
No arquivo `kind: Cluster` (`apiVersion: kind.x-k8s.io/v1alpha4`), cada entrada de nó em `nodes:` aceita o array **`extraMounts`**, onde cada item define `hostPath: /caminho/no/host/fisico`, `containerPath: /caminho/dentro/do/no/kind` e opções como `readOnly: true`, `selinuxRelabel` e `propagation` (`None`, `HostToContainer`, `Bidirectional`). Uma vez que o diretório está montado dentro do nó `kind`, qualquer Pod com um volume `hostPath` (ou `PersistentVolume` do `local-path-provisioner` do `kind`) apontando para aquele `containerPath` acessa diretamente os arquivos da máquina host.

## Exemplo
```yaml
# Configuração kind montando um diretório de dados do host físico dentro do nó worker via extraMounts
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
  - role: control-plane
  - role: worker
    extraMounts:
      - hostPath: /tmp/shared-host-data
        containerPath: /var/local-path-provisioner/shared
        readOnly: false
```

## Limites e trade-offs
No macOS e no Windows (onde o Docker Desktop, Podman Machine ou Rancher Desktop roda dentro de uma máquina virtual Linux), o `hostPath` especificado em `extraMounts` precisa estar em um diretório do usuário que já seja compartilhado entre o macOS/Windows e a VM do motor de containers (como `/Users/...` ou `/tmp`), caso contrário o container do nó verá um diretório vazio.

## Como verificar
Execute `docker exec -it kind-worker ls -la /var/local-path-provisioner/shared` para confirmar que os arquivos de `/tmp/shared-host-data` do host estão visíveis dentro do nó do `kind`.

## Conexões
- [[kind-customizacao-kubeadmconfigpatches-cni-rede-local]] — Veja também: kind: customização avançada do cluster com kubeadmConfigPatches, desativação da CNI padrão (kindnet) e redes dual-stack.
- [[kind-clusters-kubernetes-locais-containers-docker-arquitetura]] — Referência cruzada direta com kind-clusters-kubernetes-locais-containers-docker-arquitetura.
- [[kind-configuracao-multinode-control-plane-ha-port-mappings]] — Referência cruzada direta com kind-configuracao-multinode-control-plane-ha-port-mappings.
- [[minikube-addons-dashboard-gpu-mounts-container-runtimes]] — Referência cruzada direta com minikube-addons-dashboard-gpu-mounts-container-runtimes.

## Fontes
- [kind GitHub — README.md (Kubernetes IN Docker, Go Packages & Design Principles)](https://raw.githubusercontent.com/kubernetes-sigs/kind/main/README.md) — README oficial do projeto kind (Kubernetes SIGs, Apache-2.0) sobre execução de nós em containers para testes do próprio Kubernetes e CI/CD; consultado em 2026-10-03.
- [kind Official Documentation — Quick Start (Installation, Multi-Node Config, Building & Loading Images, Exporting Logs)](https://kind.sigs.k8s.io/docs/user/quick-start/) — Guia oficial Quick Start do kind cobrindo instalação, criação/exclusão de clusters, imagens kindest/node com digest SHA-256, topologia multi-nó kind.x-k8s.io/v1alpha4, kind build node-image, kind load docker-image/image-archive e kind export logs; consultado em 2026-10-03.
- [Kubernetes SIGs kind — Official GitHub Repository](https://github.com/kubernetes-sigs/kind) — Repositório oficial do kind mantido pelo Kubernetes SIG Testing; consultado em 2026-10-03.
