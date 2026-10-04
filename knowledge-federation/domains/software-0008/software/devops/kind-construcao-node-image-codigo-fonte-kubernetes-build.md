---
id: software.devops.tranche09.000836
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
fontes: ["https://raw.githubusercontent.com/kubernetes-sigs/kind/main/README.md", "https://kind.sigs.k8s.io/docs/user/quick-start/", "https://github.com/kubernetes-sigs/kind"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# kind: construção de imagens de nó customizadas (kind build node-image) a partir de source, release, url ou file

## Em uma frase
O comando `kind build node-image` constrói imagens `kindest/node` customizadas sobre a `base-image` do `kind`, suportando 4 modos (`--type` a partir do kind v0.24+): `source` (código-fonte local do Kubernetes), `release` (versão oficial ex.: `v1.30.0`), `url` e `file` (tarballs `kubernetes-server-linux-*.tar.gz`).

## Por que importa
Contribuidores do próprio projeto Kubernetes que acabaram de alterar o código Go do `kubelet` ou do `kube-apiserver` localmente precisam testar sua alteração imediatamente em um cluster real; da mesma forma, equipes que testam builds específicos ou releases recém-publicadas precisam gerar uma `node-image` sob demanda. A seção `Building Images` do `Quick Start` oficial do `kind` documenta os quatro modos de `kind build node-image`.

## Como funciona
O `kind` executa clusters usando a **`node-image`** (que contém os artefatos do Kubernetes como `kubeadm`, `kubelet`, `kubectl` e imagens de control plane), a qual por sua vez é construída sobre a **`base-image`** (que instala `systemd`, `containerd` e todas as dependências de SO necessárias para o Kubernetes rodar dentro de um container). A partir do `kind v0.24+`, o comando `kind build node-image` suporta quatro tipos explícitos via `--type`: (1) `--type source /caminho/para/k8s.io/kubernetes` (compila o código-fonte local do Kubernetes usando Docker + buildx); (2) `--type release v1.30.0` (baixa os tarballs oficiais daquela versão); (3) `--type url https://dl.k8s.io/.../kubernetes-server-linux-arm64.tar.gz`; e (4) `--type file $HOME/Downloads/kubernetes-server-linux-amd64.tar.gz`.

## Exemplo
```bash
# Construir uma node-image customizada a partir de uma release oficial ou tarball e iniciar o cluster com ela
kind build node-image --type release v1.30.0 --image kindest/node:custom-v1.30.0
kind create cluster --image kindest/node:custom-v1.30.0
```

## Limites e trade-offs
Conforme adverte a seção `Settings for Docker Desktop` do `Quick Start` oficial do `kind`, se você estiver compilando o código-fonte do Kubernetes (`kind build node-image --type source`) no macOS ou Windows usando Docker Desktop, a máquina virtual do Docker precisa de **no mínimo 6 GB de RAM dedicados (sendo 8 GB recomendados)**, caso contrário a compilação do Kubernetes dentro do container falhará por falta de memória (OOM).

## Como verificar
Após executar `kind build node-image`, rode `docker images kindest/node` para confirmar a criação da imagem local e inicie um cluster de teste apontando `--image` para a tag construída.

## Conexões
- [[kind-versoes-kubernetes-digests-sha256-feature-gates-proxy]] — Veja também: kind: fixação de versões do Kubernetes por digest SHA-256, habilitação de Feature Gates e uso de Proxy.
- [[kind-exportacao-logs-diagnostico-ci-troubleshooting]] — Veja também: kind: exportação estruturada de logs do cluster e dos nós para diagnóstico em CI (kind export logs).
- [[kind-clusters-kubernetes-locais-containers-docker-arquitetura]] — Referência cruzada direta com kind-clusters-kubernetes-locais-containers-docker-arquitetura.

## Fontes
- [kind GitHub — README.md (Kubernetes IN Docker, Go Packages & Design Principles)](https://raw.githubusercontent.com/kubernetes-sigs/kind/main/README.md) — README oficial do projeto kind (Kubernetes SIGs, Apache-2.0) sobre execução de nós em containers para testes do próprio Kubernetes e CI/CD; consultado em 2026-10-03.
- [kind Official Documentation — Quick Start (Installation, Multi-Node Config, Building & Loading Images, Exporting Logs)](https://kind.sigs.k8s.io/docs/user/quick-start/) — Guia oficial Quick Start do kind cobrindo instalação, criação/exclusão de clusters, imagens kindest/node com digest SHA-256, topologia multi-nó kind.x-k8s.io/v1alpha4, kind build node-image, kind load docker-image/image-archive e kind export logs; consultado em 2026-10-03.
- [Kubernetes SIGs kind — Official GitHub Repository](https://github.com/kubernetes-sigs/kind) — Repositório oficial do kind mantido pelo Kubernetes SIG Testing; consultado em 2026-10-03.
