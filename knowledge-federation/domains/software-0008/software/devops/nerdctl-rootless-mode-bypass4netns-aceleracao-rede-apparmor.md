---
id: software.devops.tranche14.001383
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

# nerdctl: Modo Rootless com containerd-rootless-setuptool.sh e Aceleração bypass4netns

## Em uma frase
O `nerdctl` suporta execução **Rootless** completa (rodando tanto o daemon `containerd` quanto os containers sem privilégios de `root`), configurável com `containerd-rootless-setuptool.sh install`, e aceleração de rede de alto desempenho via **`bypass4netns`** (`--annotation nerdctl/bypass4netns=true`).

## Por que importa
Em containers rootless tradicionais, todo o tráfego de rede precisa passar por um roteador de espaço de usuário (`slirp4netns`), o que reduz drasticamente a vazão TCP e aumenta a latência.

## Como funciona
Com o `bypass4netns` habilitado via anotação, chamadas de socket (`connect`, `bind`, `sendto`) do container são interceptadas via `seccomp` SECCOMP_RET_USER_NOTIF para contornar a tradução lenta do `slirp4netns`, aproximando a performance de rede do host nativo sem abrir mão do isolamento rootless e de perfis AppArmor (`sudo nerdctl apparmor load`).

## Exemplo
```bash
containerd-rootless-setuptool.sh install
nerdctl run -d -p 8080:80 \
  --annotation nerdctl/bypass4netns=true \
  --name nginx-fast nginx:alpine
```

## Limites e trade-offs
Esperar que containers diferentes na mesma máquina se comuniquem diretamente pelos IPs internos da bridge quando `bypass4netns=true` sem habilitar o suporte de bind/subnet adequado pode causar falhas de roteamento inter-container.

## Como verificar
Teste a conectividade entre containers ao usar `nerdctl/bypass4netns=true` e carregue o perfil AppArmor com `sudo nerdctl apparmor load` quando usar `--security-opt apparmor=nerdctl-default`.

## Conexões
- [[nerdctl-namespaces-k8s-io-depuracao-builds-kubernetes-local]] — Veja também: nerdctl: Gerenciamento de Namespaces do containerd (--namespace k8s.io) e Builds Locais para Kubernetes.
- [[nerdctl-lazy-pulling-snapshotters-stargz-nydus-overlaybd-soci]] — Veja também: nerdctl: Inicialização Instantânea (Lazy-Pulling) com Snapshotters Stargz, Nydus, OverlayBD e SOCI.

## Fontes
- [nerdctl GitHub — README.md (Docker-Compatible CLI for containerd, Kubernetes Debugging in k8s.io, Rootless bypass4netns, Lazy-Pulling, ocicrypt, IPFS & Cosign)](https://raw.githubusercontent.com/containerd/nerdctl/main/README.md) — README oficial do containerd/nerdctl detalhando o uso com BuildKit/CNI, depuração de Kubernetes no namespace k8s.io, snapshotters (stargz, nydus, overlaybd, soci) e diferenciais frente ao Docker; consultado em 2026-10-03.
- [nerdctl Official Documentation — docs/command-reference.md (Container, Image, Compose, Namespace, AppArmor & IPFS Commands)](https://raw.githubusercontent.com/containerd/nerdctl/main/docs/command-reference.md) — Referência oficial completa de comandos e flags do nerdctl e nerdctl compose; consultado em 2026-10-03.
- [containerd nerdctl — Official GitHub Repository](https://github.com/containerd/nerdctl) — Repositório oficial Apache-2.0 do nerdctl; consultado em 2026-10-03.
