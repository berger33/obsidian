---
id: software.devops.tranche14.001384
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

# nerdctl: Inicialização Instantânea (Lazy-Pulling) com Snapshotters Stargz, Nydus, OverlayBD e SOCI

## Em uma frase
O `nerdctl` permite experimentar e operar recursos avançados do `containerd` que permitem iniciar containers antes de baixar a imagem inteira (**lazy-pulling**) através da flag `--snapshotter=stargz|nydus|overlaybd|soci` e converter imagens com `nerdctl image convert`.

## Por que importa
Em cargas de trabalho com imagens de múltiplos gigabytes, o snapshotter padrão `overlayfs` exige aguardar o download e descompactação de 100% dos blobs antes de iniciar o processo do container.

## Como funciona
Configurando o remote snapshotter desejado no `containerd` e executando `nerdctl --snapshotter=stargz run` (ou `nydus`, `overlaybd`, `soci`), o `nerdctl` instrui o `containerd` a montar a raiz remotamente sob demanda; além disso, `nerdctl image convert --estargz --oci` converte imagens padrão para o formato otimizado eStargz.

## Exemplo
```bash
nerdctl image convert --estargz --oci alpine:latest ghcr.io/org/alpine:estargz
nerdctl --snapshotter=stargz run -it --rm ghcr.io/org/alpine:estargz sh
```

## Limites e trade-offs
Passar `--snapshotter=stargz` ou `--snapshotter=nydus` quando o respectivo daemon plugin de snapshotter não está registrado e ativo no `/etc/containerd/config.toml` falha ao montar o rootfs.

## Como verificar
Verifique os plugins de snapshotter ativos com `nerdctl info` antes de executar containers com `--snapshotter`.

## Conexões
- [[nerdctl-rootless-mode-bypass4netns-aceleracao-rede-apparmor]] — Veja também: nerdctl: Modo Rootless com containerd-rootless-setuptool.sh e Aceleração bypass4netns.
- [[nerdctl-compose-up-down-execucao-docker-compose-containerd]] — Veja também: nerdctl: Orquestração Multi-Container Compatível com Compose Spec (nerdctl compose).

## Fontes
- [nerdctl GitHub — README.md (Docker-Compatible CLI for containerd, Kubernetes Debugging in k8s.io, Rootless bypass4netns, Lazy-Pulling, ocicrypt, IPFS & Cosign)](https://raw.githubusercontent.com/containerd/nerdctl/main/README.md) — README oficial do containerd/nerdctl detalhando o uso com BuildKit/CNI, depuração de Kubernetes no namespace k8s.io, snapshotters (stargz, nydus, overlaybd, soci) e diferenciais frente ao Docker; consultado em 2026-10-03.
- [nerdctl Official Documentation — docs/command-reference.md (Container, Image, Compose, Namespace, AppArmor & IPFS Commands)](https://raw.githubusercontent.com/containerd/nerdctl/main/docs/command-reference.md) — Referência oficial completa de comandos e flags do nerdctl e nerdctl compose; consultado em 2026-10-03.
- [containerd nerdctl — Official GitHub Repository](https://github.com/containerd/nerdctl) — Repositório oficial Apache-2.0 do nerdctl; consultado em 2026-10-03.
