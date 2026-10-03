---
id: software.devops.tranche14.001388
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

# nerdctl: Operações Multi-Plataforma (--all-platforms), Arquivos Híbridos OCI/Docker e Inspeção Nativa

## Em uma frase
O `nerdctl` oferece controle direto sobre os artefatos multi-arquitetura armazenados no Content Store do `containerd`, permitindo puxar e exportar todas as arquiteturas de uma imagem simultaneamente (`--all-platforms` ou `--platform=amd64,arm64`), salvar arquivos em formato duplo Docker/OCI (`nerdctl save`) e inspecionar os metadados brutos (`nerdctl container inspect --mode=native`).

## Por que importa
No Docker tradicional, `docker pull` e `docker save` operam por padrão apenas sobre a arquitetura da máquina host, dificultando exportar um tarball multi-arquitetura completo para transporte offline.

## Como funciona
No `nerdctl`, executar `nerdctl pull --all-platforms <imagem>` baixa os manifestos e blobs de todas as plataformas listadas no `Image Index`, e `nerdctl save --all-platforms` gera um arquivo tar compatível tanto com `docker load` quanto com leitores OCI.

## Exemplo
```bash
nerdctl pull --platform=linux/amd64,linux/arm64 alpine:3.20
nerdctl save --platform=linux/amd64,linux/arm64 -o alpine-multiarch.tar alpine:3.20
nerdctl image inspect --mode=native alpine:3.20
```

## Limites e trade-offs
Executar `nerdctl push --all-platforms` em uma imagem para a qual apenas a plataforma `linux/amd64` foi baixada localmente (sem rodar `nerdctl pull --all-platforms` antes) falha por falta dos blobs das demais plataformas no Content Store local.

## Como verificar
Execute sempre `nerdctl pull --all-platforms` (ou especifique as mesmas plataformas em `--platform`) antes de converter, salvar ou republicar imagens multi-arch.

## Conexões
- [[nerdctl-ipfs-p2p-image-distribution-offline-optional]] — Veja também: nerdctl: Distribuição P2P Opcional de Imagens OCI sobre IPFS (ipfs://CID e nerdctl ipfs).
- [[nerdctl-redes-multiplas-cni-rootfs-systemd-rro-bind-mounts]] — Veja também: nerdctl: Conexão Multi-Rede (--net), Execução Direta de Rootfs (--rootfs), Systemd e Bind-Mounts RRO.

## Fontes
- [nerdctl GitHub — README.md (Docker-Compatible CLI for containerd, Kubernetes Debugging in k8s.io, Rootless bypass4netns, Lazy-Pulling, ocicrypt, IPFS & Cosign)](https://raw.githubusercontent.com/containerd/nerdctl/main/README.md) — README oficial do containerd/nerdctl detalhando o uso com BuildKit/CNI, depuração de Kubernetes no namespace k8s.io, snapshotters (stargz, nydus, overlaybd, soci) e diferenciais frente ao Docker; consultado em 2026-10-03.
- [nerdctl Official Documentation — docs/command-reference.md (Container, Image, Compose, Namespace, AppArmor & IPFS Commands)](https://raw.githubusercontent.com/containerd/nerdctl/main/docs/command-reference.md) — Referência oficial completa de comandos e flags do nerdctl e nerdctl compose; consultado em 2026-10-03.
- [containerd nerdctl — Official GitHub Repository](https://github.com/containerd/nerdctl) — Repositório oficial Apache-2.0 do nerdctl; consultado em 2026-10-03.
