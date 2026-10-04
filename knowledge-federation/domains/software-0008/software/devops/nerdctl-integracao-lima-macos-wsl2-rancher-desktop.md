---
id: software.devops.tranche14.001390
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

# nerdctl: Integração Nativa com Lima (macOS), Rancher Desktop e WSL2

## Em uma frase
Em estações de trabalho macOS e Windows, o `nerdctl` é a CLI padrão das máquinas virtuais Linux gerenciadas pelo projeto **Lima (`limactl`)** (como `lima nerdctl run ...`) e pelo **Rancher Desktop** (no modo `containerd`).

## Por que importa
Desenvolvedores em Macs com Apple Silicon (`arm64`) ou Intel precisam de uma alternativa open-source que execute containers Linux com compartilhamento rápido de diretórios e encaminhamento automático de portas para `127.0.0.1` no host macOS.

## Como funciona
O Lima inicia uma VM Linux leve com `containerd` e `nerdctl-full` pré-configurados, permitindo que o desenvolvedor execute `lima nerdctl run -d -p 127.0.0.1:8080:80 nginx:alpine` diretamente do terminal do macOS e acesse `localhost:8080` no navegador nativo.

## Exemplo
```bash
limactl list
lima nerdctl version
lima nerdctl run -d --name web -p 127.0.0.1:8080:80 nginx:alpine
```

## Limites e trade-offs
Tentar instalar o binário Linux do `nerdctl` diretamente no macOS sem uma VM Linux (como o Lima) não funciona para containers Linux porque o `containerd` para containers Linux requer o kernel Linux.

## Como verificar
No macOS, instale e utilize o `nerdctl` através do **Lima** (`brew install lima && limactl start`) ou **Rancher Desktop**/**Colima**.

## Conexões
- [[nerdctl-redes-multiplas-cni-rootfs-systemd-rro-bind-mounts]] — Veja também: nerdctl: Conexão Multi-Rede (--net), Execução Direta de Rootfs (--rootfs), Systemd e Bind-Mounts RRO.

## Fontes
- [nerdctl GitHub — README.md (Docker-Compatible CLI for containerd, Kubernetes Debugging in k8s.io, Rootless bypass4netns, Lazy-Pulling, ocicrypt, IPFS & Cosign)](https://raw.githubusercontent.com/containerd/nerdctl/main/README.md) — README oficial do containerd/nerdctl detalhando o uso com BuildKit/CNI, depuração de Kubernetes no namespace k8s.io, snapshotters (stargz, nydus, overlaybd, soci) e diferenciais frente ao Docker; consultado em 2026-10-03.
- [nerdctl Official Documentation — docs/command-reference.md (Container, Image, Compose, Namespace, AppArmor & IPFS Commands)](https://raw.githubusercontent.com/containerd/nerdctl/main/docs/command-reference.md) — Referência oficial completa de comandos e flags do nerdctl e nerdctl compose; consultado em 2026-10-03.
- [containerd nerdctl — Official GitHub Repository](https://github.com/containerd/nerdctl) — Repositório oficial Apache-2.0 do nerdctl; consultado em 2026-10-03.
