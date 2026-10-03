---
id: software.devops.tranche14.001382
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

# nerdctl: Gerenciamento de Namespaces do containerd (--namespace k8s.io) e Builds Locais para Kubernetes

## Em uma frase
Diferente do Docker (que possui um único espaço global de containers e imagens), o `containerd` isola recursos por **namespaces** (`nerdctl namespace ls`), e todos os containers e imagens do Kubernetes residem no namespace **`k8s.io`** do `containerd` (independentemente do namespace lógico do Kubernetes).

## Por que importa
Rodar `nerdctl ps` ou `nerdctl images` sem flags consulta o namespace `default` do `containerd`, fazendo parecer que nenhum container ou imagem do Kubernetes existe no nó.

## Como funciona
Passando `--namespace k8s.io` (ou `-n k8s.io`), o engenheiro lista os containers reais dos Pods (`nerdctl -n k8s.io ps -a`), lê logs (`nerdctl -n k8s.io logs -f`) e pode construir ou carregar imagens diretamente no cache do Kubernetes (`nerdctl -n k8s.io build -t foo .` ou `nerdctl -n k8s.io load < image.tar`) para uso imediato com `imagePullPolicy: Never`.

## Exemplo
```bash
nerdctl namespace ls
nerdctl --namespace k8s.io ps -a
nerdctl --namespace k8s.io build -t local-app:dev .
```

## Limites e trade-offs
Construir uma imagem com `nerdctl build -t local-app:dev .` (no namespace `default`) e tentar usá-la em um Pod Kubernetes com `imagePullPolicy: Never` falha com `ErrImageNeverPull` porque o kubelet enxerga apenas o namespace `k8s.io`.

## Como verificar
Passe sempre `--namespace k8s.io` ao executar `nerdctl build` ou `nerdctl load` de imagens destinadas ao cluster Kubernetes local.

## Conexões
- [[nerdctl-arquitetura-cli-docker-compatible-containerd-buildkit]] — Veja também: nerdctl: CLI Compatível com Docker para containerd, BuildKit e CNI Plugins.
- [[nerdctl-rootless-mode-bypass4netns-aceleracao-rede-apparmor]] — Veja também: nerdctl: Modo Rootless com containerd-rootless-setuptool.sh e Aceleração bypass4netns.

## Fontes
- [nerdctl GitHub — README.md (Docker-Compatible CLI for containerd, Kubernetes Debugging in k8s.io, Rootless bypass4netns, Lazy-Pulling, ocicrypt, IPFS & Cosign)](https://raw.githubusercontent.com/containerd/nerdctl/main/README.md) — README oficial do containerd/nerdctl detalhando o uso com BuildKit/CNI, depuração de Kubernetes no namespace k8s.io, snapshotters (stargz, nydus, overlaybd, soci) e diferenciais frente ao Docker; consultado em 2026-10-03.
- [nerdctl Official Documentation — docs/command-reference.md (Container, Image, Compose, Namespace, AppArmor & IPFS Commands)](https://raw.githubusercontent.com/containerd/nerdctl/main/docs/command-reference.md) — Referência oficial completa de comandos e flags do nerdctl e nerdctl compose; consultado em 2026-10-03.
- [containerd nerdctl — Official GitHub Repository](https://github.com/containerd/nerdctl) — Repositório oficial Apache-2.0 do nerdctl; consultado em 2026-10-03.
