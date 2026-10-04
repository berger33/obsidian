---
id: software.devops.tranche09.000847
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

# Kubernetes minikube: provisionamento dinâmico de PersistentVolumes, StorageClass standard e snapshots CSI

## Em uma frase
O `minikube` habilita por padrão o addon `storage-provisioner` e a `StorageClass` padrão `standard` (`k8s.io/minikube-hostpath`), atendendo automaticamente `PersistentVolumeClaims` (`PVCs`) e suportando snapshots de volume via driver CSI hostpath (`csi-hostpath-driver`).

## Por que importa
Aplicações stateful (bancos de dados PostgreSQL, MySQL, Redis, filas Kafka/RabbitMQ e plataformas como Bytebase ou Mimir) declaradas em StatefulSets ou Helm charts criam objetos `PersistentVolumeClaim` (`PVC`); se o cluster local não possuir um provisionador dinâmico de armazenamento ativo por padrão, todos os Pods stateful ficarão travados eternamente em `Pending`. O README oficial do `minikube` destaca o suporte nativo a `Persistent Volumes`.

## Como funciona
Logo na criação do cluster (`minikube start`), os addons **`default-storageclass`** e **`storage-provisioner`** já vêm ativados por padrão. Sempre que um usuário aplica um `PersistentVolumeClaim` sem especificar `storageClassName` (ou especificando `storageClassName: standard`), o provisionador do `minikube` cria automaticamente um `PersistentVolume` apoiado em um diretório persistente dentro do nó (`/tmp/hostpath-provisioner/...`, que sobrevive a `minikube stop` e `minikube start`). Para testar recursos avançados da Container Storage Interface (como `VolumeSnapshot`, clonagem e expansão de volumes CSI), basta habilitar os addons **`volumesnapshots`** e **`csi-hostpath-driver`**.

## Exemplo
```bash
# Verificar a StorageClass padrão ativa no minikube e habilitar suporte a CSI Hostpath e VolumeSnapshots
kubectl get storageclass
minikube addons enable volumesnapshots
minikube addons enable csi-hostpath-driver
```

## Limites e trade-offs
O provisionador padrão `k8s.io/minikube-hostpath` (`StorageClass: standard`) é projetado para clusters de nó único; se você iniciar um cluster `minikube` multi-nós (`minikube start --nodes 3`) e quiser provisionar volumes em múltiplos nós ou usar `VolumeSnapshots`, deve habilitar o addon `csi-hostpath-driver` (ou `storage-provisioner-rancher` / `local-path`) conforme documentado no guia de Persistent Volumes do `minikube`.

## Como verificar
Crie um `PersistentVolumeClaim` simples de `1Gi` no cluster `minikube` e execute `kubectl get pvc,pv` para confirmar que o status muda imediatamente para `Bound`.

## Conexões
- [[minikube-drivers-execucao-docker-kvm2-qemu-vfkit-none]] — Veja também: Kubernetes minikube: arquitetura de drivers multiplataforma (Docker/Podman containers, VMs KVM2/QEMU/VFKit/Hyper-V e bare-metal).
- [[minikube-diagnostico-logs-ssh-ip-pause-unpause]] — Veja também: Kubernetes minikube: diagnóstico e economia de recursos com minikube logs, ssh, ip, pause e unpause.
- [[minikube-clusters-locais-kubernetes-perfis-controles-basicos]] — Referência cruzada direta com minikube-clusters-locais-kubernetes-perfis-controles-basicos.
- [[minikube-addons-dashboard-gpu-mounts-container-runtimes]] — Referência cruzada direta com minikube-addons-dashboard-gpu-mounts-container-runtimes.
- [[k3s-componentes-embutidos-containerd-flannel-traefik-klipper]] — Referência cruzada direta com k3s-componentes-embutidos-containerd-flannel-traefik-klipper.

## Fontes
- [minikube GitHub — README.md (Local Kubernetes, Multi-Platform Drivers & Design Principles)](https://raw.githubusercontent.com/kubernetes/minikube/master/README.md) — README oficial do projeto minikube detalhando objetivos de simplicidade e conformidade com recursos do Kubernetes local; consultado em 2026-10-03.
- [minikube Official Documentation — Basic Controls (start/pause/stop/delete, kubectl Wrapper, Addons, service/tunnel & profiles)](https://minikube.sigs.k8s.io/docs/handbook/controls/) — Documentação oficial Basic Controls do minikube cobrindo ciclo de vida de clusters, perfis (-p), wrapper minikube kubectl --, addons (dashboard, ingress, metrics-server), minikube service, minikube tunnel e minikube node/image/cache; consultado em 2026-10-03.
- [Kubernetes minikube — Official GitHub Repository](https://github.com/kubernetes/minikube) — Repositório oficial Apache-2.0 do minikube; consultado em 2026-10-03.
