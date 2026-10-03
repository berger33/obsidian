---
id: software.devops.tranche14.001381
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

# nerdctl: CLI Compatível com Docker para containerd, BuildKit e CNI Plugins

## Em uma frase
O **nerdctl** (`containerd/nerdctl`, subprojeto oficial do **containerd** na CNCF) é uma interface de linha de comando compatível com a sintaxe e UX do `docker` (`nerdctl run`, `nerdctl build`, `nerdctl compose up`) que opera diretamente sobre o **containerd** sem precisar do daemon `dockerd`.

## Por que importa
Desde que o Kubernetes removeu o `dockershim` e adotou o `containerd` como runtime padrão nos nós, engenheiros que precisam construir imagens, rodar containers ou depurar nós ficam sem a ergonomia familiar da CLI do Docker se usarem apenas a ferramenta de baixo nível `ctr`.

## Como funciona
O `nerdctl` integra o `containerd` aos **CNI plugins** (para redes como `bridge` `10.4.0.0/24`), ao **BuildKit (`buildkitd`)** (para `nerdctl build`) e ao **RootlessKit** (para execução sem root), sendo distribuído em duas variantes: o pacote mínimo `nerdctl-<VERSION>` e o pacote completo `nerdctl-full-<VERSION>` (que já embute containerd, runc, CNI, BuildKit e RootlessKit).

## Exemplo
```bash
nerdctl version
nerdctl info
nerdctl run -it --rm alpine uname -a
```

## Limites e trade-offs
Tentar executar `nerdctl build` quando o daemon `buildkitd` não está instalado ou em execução no host falha porque a construção de Dockerfiles no `nerdctl` é delegada ao BuildKit.

## Como verificar
Instale o pacote `nerdctl-full` (ou inicie o serviço `buildkit.service`) para habilitar `nerdctl build` e `nerdctl builder prune`.

## Conexões
- [[nerdctl-namespaces-k8s-io-depuracao-builds-kubernetes-local]] — Veja também: nerdctl: Gerenciamento de Namespaces do containerd (--namespace k8s.io) e Builds Locais para Kubernetes.

## Fontes
- [nerdctl GitHub — README.md (Docker-Compatible CLI for containerd, Kubernetes Debugging in k8s.io, Rootless bypass4netns, Lazy-Pulling, ocicrypt, IPFS & Cosign)](https://raw.githubusercontent.com/containerd/nerdctl/main/README.md) — README oficial do containerd/nerdctl detalhando o uso com BuildKit/CNI, depuração de Kubernetes no namespace k8s.io, snapshotters (stargz, nydus, overlaybd, soci) e diferenciais frente ao Docker; consultado em 2026-10-03.
- [nerdctl Official Documentation — docs/command-reference.md (Container, Image, Compose, Namespace, AppArmor & IPFS Commands)](https://raw.githubusercontent.com/containerd/nerdctl/main/docs/command-reference.md) — Referência oficial completa de comandos e flags do nerdctl e nerdctl compose; consultado em 2026-10-03.
- [containerd nerdctl — Official GitHub Repository](https://github.com/containerd/nerdctl) — Repositório oficial Apache-2.0 do nerdctl; consultado em 2026-10-03.
