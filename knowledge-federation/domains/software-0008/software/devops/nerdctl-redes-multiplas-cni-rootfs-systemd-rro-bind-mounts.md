---
id: software.devops.tranche14.001389
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-14.md"
fontes: ["https://raw.githubusercontent.com/containerd/nerdctl/main/README.md", "https://raw.githubusercontent.com/containerd/nerdctl/main/docs/command-reference.md", "https://github.com/containerd/nerdctl"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# nerdctl: Conexão Multi-Rede (--net), Execução Direta de Rootfs (--rootfs), Systemd e Bind-Mounts RRO

## Em uma frase
O `nerdctl run` implementa recursos de runtime de baixo nível que frequentemente chegam ao `nerdctl` antes do Docker: conexão simultânea a múltiplas redes CNI na criação (`--net foo --net bar`), execução de um diretório de rootfs desembrulhado sem imagem (`--rootfs <DIR>`), suporte a `systemd` dentro do container (`--systemd=always`) e montagens **Recursive Read-Only (RRO)**.

## Por que importa
Montagens bind normais (`-v /mnt:/mnt:ro`) marcam apenas o ponto de montagem superior como somente leitura no Linux, deixando submontagens filhas (`/mnt/submount`) graváveis se não for aplicado o atributo RRO do kernel Linux 5.12+.

## Como funciona
Com `--mount type=bind,src=...,dst=...,ro,rro=true`, o `nerdctl` aplica proteção somente leitura recursiva em toda a subárvore de montagem; já `--systemd=always` configura automaticamente os mounts de cgroup/tmpfs e sinais necessários para rodar o `systemd` como PID 1 de forma limpa.

## Exemplo
```bash
nerdctl network create net-front
nerdctl network create net-back
nerdctl run -d --name gateway --net net-front --net net-back nginx:alpine
```

## Limites e trade-offs
Usar `rro=true` em nós Linux com kernel antigo (anterior ao Linux 5.12) ou versión antiga do `runc`/`crun` falha porque o suporte a `MOUNT_ATTR_RDONLY` recursivo depende da syscall `mount_setattr` do kernel.

## Como verificar
Verifique a versão do kernel (`uname -r`) e do `runc` em `nerdctl version` ao utilizar bind-mounts Recursive Read-Only.

## Conexões
- [[nerdctl-multi-platform-pull-save-load-oci-archives-inspect-native]] — Veja também: nerdctl: Operações Multi-Plataforma (--all-platforms), Arquivos Híbridos OCI/Docker e Inspeção Nativa.
- [[nerdctl-integracao-lima-macos-wsl2-rancher-desktop]] — Veja também: nerdctl: Integração Nativa com Lima (macOS), Rancher Desktop e WSL2.

## Fontes
- [nerdctl GitHub — README.md (Docker-Compatible CLI for containerd, Kubernetes Debugging in k8s.io, Rootless bypass4netns, Lazy-Pulling, ocicrypt, IPFS & Cosign)](https://raw.githubusercontent.com/containerd/nerdctl/main/README.md) — README oficial do containerd/nerdctl detalhando o uso com BuildKit/CNI, depuração de Kubernetes no namespace k8s.io, snapshotters (stargz, nydus, overlaybd, soci) e diferenciais frente ao Docker; consultado em 2026-10-03.
- [nerdctl Official Documentation — docs/command-reference.md (Container, Image, Compose, Namespace, AppArmor & IPFS Commands)](https://raw.githubusercontent.com/containerd/nerdctl/main/docs/command-reference.md) — Referência oficial completa de comandos e flags do nerdctl e nerdctl compose; consultado em 2026-10-03.
- [containerd nerdctl — Official GitHub Repository](https://github.com/containerd/nerdctl) — Repositório oficial Apache-2.0 do nerdctl; consultado em 2026-10-03.
