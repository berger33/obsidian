---
id: software.devops.tranche09.000846
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

# Kubernetes minikube: arquitetura de drivers multiplataforma (Docker/Podman containers, VMs KVM2/QEMU/VFKit/Hyper-V e bare-metal)

## Em uma frase
O `minikube` suporta três famílias de drivers (`--driver`): baseados em **containers** (`docker`, `podman`), baseados em **máquinas virtuais** (`kvm2`, `qemu`, `vfkit`, `krunkit`, `hyperkit`, `hyperv`, `virtualbox`, `vmware`) e **bare-metal** (`none`).

## Por que importa
Enquanto ferramentas como o `kind` operam exclusivamente com containers como nós, certos cenários de desenvolvimento e testes de infraestrutura (como carregar módulos de kernel específicos no nó, testar armazenamento de bloco real anexado a VMs, passthrough de GPU PCI ou isolamento completo de kernel no Linux/macOS/Windows) exigem rodar o cluster dentro de uma máquina virtual real.

## Como funciona
Quando o usuário executa `minikube start` sem especificar `--driver`, o `minikube` escolhe automaticamente o driver mais rápido e saudável disponível na plataforma (tipicamente o driver **`docker`**, que roda a imagem base `kicbase` — *Kubernetes in Container*). Caso o desenvolvedor necessite de um kernel isolado completo ou emulação de dispositivos de VM, basta passar **`minikube start --driver=kvm2`** (no Linux), **`--driver=qemu`** ou **`--driver=vfkit`** / **`--driver=krunkit`** (no macOS Apple Silicon) ou **`--driver=hyperv`** (no Windows), fazendo o `minikube` baixar a imagem ISO mínima do Minikube e provisionar a máquina virtual.

## Exemplo
```bash
# Iniciar um perfil minikube usando explicitamente o driver de container docker vs um perfil em máquina virtual kvm2
minikube start -p dev-container --driver=docker
minikube start -p dev-vm --driver=kvm2
```

## Limites e trade-offs
Os drivers baseados em container (`--driver=docker`) iniciam muito mais rápido e consomem menos memória RAM ociosa na máquina host, mas compartilham o kernel do host Linux (ou da VM do Docker Desktop); já os drivers baseados em máquina virtual (`kvm2`, `qemu`, `vfkit`, `hyperv`) oferecem isolamento completo de kernel e suporte a discos extras (`--extra-disks`), ao custo de boot ligeiramente mais longo e alocação fixa de RAM da VM.

## Como verificar
Execute `minikube status -p <perfil>` e `minikube ip -p <perfil>` para verificar o driver ativo, o estado do host/kubelet/apiserver e o endereço IP atribuído ao nó.

## Conexões
- [[minikube-gerenciamento-imagens-image-build-load-docker-env]] — Veja também: Kubernetes minikube: construção e carregamento de imagens locais (minikube image load, image build e docker-env).
- [[minikube-persistencia-volumes-storage-provisioner-csi]] — Veja também: Kubernetes minikube: provisionamento dinâmico de PersistentVolumes, StorageClass standard e snapshots CSI.
- [[minikube-clusters-locais-kubernetes-perfis-controles-basicos]] — Referência cruzada direta com minikube-clusters-locais-kubernetes-perfis-controles-basicos.
- [[minikube-addons-dashboard-gpu-mounts-container-runtimes]] — Referência cruzada direta com minikube-addons-dashboard-gpu-mounts-container-runtimes.

## Fontes
- [minikube GitHub — README.md (Local Kubernetes, Multi-Platform Drivers & Design Principles)](https://raw.githubusercontent.com/kubernetes/minikube/master/README.md) — README oficial do projeto minikube detalhando objetivos de simplicidade e conformidade com recursos do Kubernetes local; consultado em 2026-10-03.
- [minikube Official Documentation — Basic Controls (start/pause/stop/delete, kubectl Wrapper, Addons, service/tunnel & profiles)](https://minikube.sigs.k8s.io/docs/handbook/controls/) — Documentação oficial Basic Controls do minikube cobrindo ciclo de vida de clusters, perfis (-p), wrapper minikube kubectl --, addons (dashboard, ingress, metrics-server), minikube service, minikube tunnel e minikube node/image/cache; consultado em 2026-10-03.
- [Kubernetes minikube — Official GitHub Repository](https://github.com/kubernetes/minikube) — Repositório oficial Apache-2.0 do minikube; consultado em 2026-10-03.
