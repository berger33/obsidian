---
id: software.devops.tranche04.000373
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/cri-o/cri-o/main/README.md", "https://cri-o.github.io/cri-o", "https://github.com/cri-o/cri-o"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Arquitetura interna do CRI-O: runc, container-libs/image, container-libs/storage e CNI

## Em uma frase
Para cumprir a especificação CRI usando os melhores projetos do ecossistema OCI, o CRI-O integra quatro pilares documentados no README oficial: **Runtime** via **`runc`** (`opencontainers/runc`, ou qualquer implementação compatível com a `runtime-spec` OCI como `crun`) e `oci-runtime-tools`; **Images** via biblioteca **`container-libs/image`** (`containers/container-libs/tree/main/image`) para pull, transporte e verificação; **Storage** via biblioteca **`container-libs/storage`** (`containers/container-libs/tree/main/storage`) para gerenciamento de camadas e sistemas de arquivos copy-on-write (como `overlay` ou `btrfs`); e **Networking** através do padrão **CNI** (`containernetworking/cni`).

## Por que importa
Por compartilhar as mesmas bibliotecas fundamentais (`container-libs/image` e `container-libs/storage`) e arquivos de configuração que o Podman, Buildah e Skopeo, administradores encontram semântica idêntica de armazenamento em `/var/lib/containers/storage` e políticas de registro.

## Como funciona
Padronize o driver de armazenamento (`storage_driver`) e o driver de cgroups (`cgroup_driver = "systemd"`) entre o CRI-O e o Kubelet em todos os nós para evitar conflitos de contabilidade de memória e CPU.

## Exemplo
Quando o Kubelet solicita a criação de um PodSandbox via gRPC, o CRI-O usa `container-libs/image` e `container-libs/storage` para preparar o rootfs, configura a rede do pod invocando os plugins CNI e delega ao `runc`/`crun` a criação dos processos isolados.

## Limites e trade-offs
Nunca misture `cgroup_driver` diferente entre o Kubelet (por exemplo `systemd`) e o CRI-O (por exemplo `cgroupfs`) no mesmo nó, pois isso causa instabilidade severa no gerenciamento de recursos sob pressão.

## Como verificar
Execute `sudo crio status info` no nó e confirme que `cgroup driver` (como `systemd`), `storage driver` e `storage root` (`/var/lib/containers/storage`) estão alinhados à configuração do Kubelet.

## Conexões
- [[crio-kubernetes-version-matching-and-n-minus-2-skew-policy]] — Veja também: Matriz de compatibilidade CRI-O 1.x.y com o Kubernetes e política de version skew n-2.
- [[crio-configuration-files-crio-conf-policy-registries-and-storage]] — Veja também: Arquivos de configuração do CRI-O: crio.conf, policy.json, registries.conf e storage.conf.

## Fontes
- [CRI-O GitHub — README.md (Kubernetes Compatibility Matrix, Scope, Config & HTTP Status API)](https://raw.githubusercontent.com/cri-o/cri-o/main/README.md) — README oficial do CRI-O detalhando alinhamento de versões 1.x.y e política de version skew n-2 com o Kubernetes, escopo estrito de implementação da CRI para o Kubelet, bibliotecas OCI (runc, container-libs/image, container-libs/storage, CNI), arquivos crio.conf, policy.json, registries.conf, storage.conf e API de status via crio status e socket /var/run/crio/crio.sock.; consultado em 2026-10-03.
- [CRI-O — Official Release Notes & Documentation Portal](https://cri-o.github.io/cri-o) — Portal oficial de notas de versão e relatórios de dependências do CRI-O mantido pelos desenvolvedores do projeto.; consultado em 2026-10-03.
- [CRI-O — Official GitHub Repository](https://github.com/cri-o/cri-o) — Repositório oficial Apache-2.0 do CRI-O na CNCF.; consultado em 2026-10-03.
