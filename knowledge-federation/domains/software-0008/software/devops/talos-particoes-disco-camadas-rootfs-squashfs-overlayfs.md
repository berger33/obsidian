---
id: software.devops.tranche09.000803
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
fontes: ["https://raw.githubusercontent.com/siderolabs/talos/main/README.md", "https://docs.siderolabs.com/talos/v1.9/learn-more/architecture", "https://github.com/siderolabs/talos"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Talos Linux: layout das 6 partições de disco (EFI, BIOS, BOOT, META, STATE, EPHEMERAL) e 3 camadas de filesystem

## Em uma frase
O Talos Linux particiona o disco em seis partições rotuladas (`EFI`, `BIOS`, `BOOT`, `META`, `STATE` e `EPHEMERAL`) e estrutura o sistema de arquivos raiz em três camadas: imagem `SquashFS` somente-leitura em memória, `tmpfs` (incluindo `/system`) e `overlayfs` sobre `/var` (XFS).

## Por que importa
Compreender exatamente o que é imutável, o que é recriado a cada boot e o que persiste no disco (`/var` e `STATE`) é essencial para planejar armazenamento de nós Kubernetes, backups do `etcd` e procedimentos de reset no Talos. A página `Architecture` (`docs.siderolabs.com/talos/v1.9/learn-more/architecture`) detalha tanto as seis partições quanto as três camadas do filesystem.

## Como funciona
O disco de um nó Talos contém 6 partições: (1) **`EFI`** (dados de boot EFI); (2) **`BIOS`** (segundo estágio do GRUB); (3) **`BOOT`** (bootloader, `initramfs` e kernel); (4) **`META`** (metadados do nó, como IDs); (5) **`STATE`** (configuração da máquina, identidade de descoberta do cluster e dados do KubeSpan); e (6) **`EPHEMERAL`** (formatada em XFS e montada em `/var`). Já o sistema de arquivos raiz opera em **3 camadas**: (a) na base, uma imagem **`SquashFS` somente-leitura** montada via loop device em memória; (b) na segunda camada, sistemas **`tmpfs`** recriados do zero a cada boot (incluindo `/system`, onde o Talos grava `/system/etc/hosts` e `/system/etc/resolv.conf` e faz bind-mount sobre `/etc/hosts` e `/etc/resolv.conf` para manter o resto de `/etc` 100% read-only); e (c) na terceira camada, montagens **`overlayfs`** (como `/etc/kubernetes`) apoiadas no XFS de `/var`, que também armazena os dados do `etcd`, `kubelet` e `containerd`.

## Exemplo
```bash
# Listar os discos e as partições (EFI, BIOS, BOOT, META, STATE, EPHEMERAL) de um nó Talos via API
talosctl -n 10.0.0.10 get disks
talosctl -n 10.0.0.10 mounts
```

## Limites e trade-offs
O conteúdo de `/var` (partição `EPHEMERAL`) sobrevive a reboots normais e a upgrades do sistema operacional Talos, mas é completamente apagado em um `talosctl reset` (a menos que a flag `--system-labels-to-wipe` seja usada para limpar apenas partições específicas, como `STATE`, preservando `EPHEMERAL`); por isso, a filosofia do Talos trata a partição gravável como efêmera, exigindo que todos os dados nela sejam replicados (como o `etcd` em HA) ou reconstruíveis.

## Como verificar
Execute `talosctl -n <ip-do-no> mounts` para inspecionar o loop device do `squashfs` na raiz `/`, os `tmpfs` em `/system` e a partição XFS `EPHEMERAL` montada em `/var`.

## Conexões
- [[talos-filosofia-machined-pid1-sem-systemd-sem-shell-ssh]] — Veja também: Talos Linux: reescrita do userspace em Go a partir do PID 1 (machined) sem systemd, GNU utilities ou SSH.
- [[talos-configuracao-declarativa-yaml-unica-machineconfig]] — Veja também: Talos Linux: configuração declarativa unificada da máquina e do Kubernetes em um único manifesto YAML.
- [[talos-linux-sistema-operacional-imutavel-api-kubernetes]] — Referência cruzada direta com talos-linux-sistema-operacional-imutavel-api-kubernetes.
- [[talos-atualizacoes-atomicas-upgrades-reset-ciclo-vida]] — Referência cruzada direta com talos-atualizacoes-atomicas-upgrades-reset-ciclo-vida.

## Fontes
- [Talos Linux Documentation — What is Talos (Immutability, Minimalism, Ephemerality & API-Driven Management)](https://raw.githubusercontent.com/siderolabs/talos/main/README.md) — Visão geral oficial do Talos Linux detalhando ausência de shell/SSH, cerca de 12 binários no sistema de arquivos, partições efêmeras criptografadas com KMS/TPM e recomendações CIS/NIST; consultado em 2026-10-03.
- [Talos Linux Documentation — Architecture & Design Philosophy (PID 1 machined, squashfs, udevd, containerd & COSI)](https://docs.siderolabs.com/talos/v1.9/learn-more/architecture) — Documentação oficial de arquitetura e filosofia do Talos Linux explicando o binário init machined (PID 1), montagem do rootfs squashfs, serviços em containers containerd e sistema de recursos COSI; consultado em 2026-10-03.
- [Sidero Labs Talos — Official GitHub README.md](https://github.com/siderolabs/talos) — README oficial do repositório siderolabs/talos; consultado em 2026-10-03.
