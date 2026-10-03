---
id: software.devops.tranche14.001385
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
fontes: ["https://raw.githubusercontent.com/containerd/nerdctl/main/docs/command-reference.md", "https://raw.githubusercontent.com/containerd/nerdctl/main/README.md", "https://github.com/containerd/nerdctl"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# nerdctl: Orquestração Multi-Container Compatível com Compose Spec (nerdctl compose)

## Em uma frase
O subcomando `nerdctl compose` (`up`, `down`, `build`, `logs`, `ps`, `exec`, `pull`, `push`, `config`, `run`, `top`) implementa suporte nativo à especificação **Docker Compose** diretamente sobre o `containerd`, CNI e BuildKit.

## Por que importa
Desenvolvedores que migram suas estações Linux ou VMs macOS (**Lima** / **Rancher Desktop**) do Docker Desktop para `containerd` puro precisam continuar subindo pilhas locais definidas em `docker-compose.yaml` ou `compose.yaml`.

## Como funciona
Ao executar `nerdctl compose up -d`, o `nerdctl` analisa e valida o arquivo Compose (`nerdctl compose config`), cria a rede CNI isolada do projeto, os volumes e os containers no `containerd`, suportando inclusive verificação e assinatura de imagens com Cosign dentro do próprio Compose.

## Exemplo
```bash
nerdctl compose -f docker-compose.yaml config
nerdctl compose -f docker-compose.yaml up -d
nerdctl compose ps
nerdctl compose down
```

## Limites e trade-offs
Usar plugins de rede ou drivers de volume proprietários exclusivos do daemon `dockerd` dentro do `docker-compose.yaml` falha ao rodar sob `nerdctl compose`, que utiliza plugins CNI padrão.

## Como verificar
Valide sempre o arquivo com `nerdctl compose config` para confirmar a compatibilidade das diretivas do Compose com o `nerdctl`.

## Conexões
- [[nerdctl-lazy-pulling-snapshotters-stargz-nydus-overlaybd-soci]] — Veja também: nerdctl: Inicialização Instantânea (Lazy-Pulling) com Snapshotters Stargz, Nydus, OverlayBD e SOCI.
- [[nerdctl-cosign-assinatura-verificacao-ocicrypt-imagens-criptografadas]] — Veja também: nerdctl: Assinatura e Verificação Cosign (--sign/--verify) e Criptografia de Camadas (ocicrypt).

## Fontes
- [nerdctl GitHub — README.md (Docker-Compatible CLI for containerd, Kubernetes Debugging in k8s.io, Rootless bypass4netns, Lazy-Pulling, ocicrypt, IPFS & Cosign)](https://raw.githubusercontent.com/containerd/nerdctl/main/docs/command-reference.md) — README oficial do containerd/nerdctl detalhando o uso com BuildKit/CNI, depuração de Kubernetes no namespace k8s.io, snapshotters (stargz, nydus, overlaybd, soci) e diferenciais frente ao Docker; consultado em 2026-10-03.
- [nerdctl Official Documentation — docs/command-reference.md (Container, Image, Compose, Namespace, AppArmor & IPFS Commands)](https://raw.githubusercontent.com/containerd/nerdctl/main/README.md) — Referência oficial completa de comandos e flags do nerdctl e nerdctl compose; consultado em 2026-10-03.
- [containerd nerdctl — Official GitHub Repository](https://github.com/containerd/nerdctl) — Repositório oficial Apache-2.0 do nerdctl; consultado em 2026-10-03.
