---
id: software.devops.tranche09.000833
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

# kind: carregamento direto de imagens locais para dentro do cluster (kind load docker-image e image-archive)

## Em uma frase
O comando `kind load docker-image <imagem>` (e `kind load image-archive <arquivo.tar>`) copia imagens construídas na máquina host diretamente para o `containerd` interno dos nós do cluster `kind`, eliminando a necessidade de enviar imagens para um registry remoto durante o desenvolvimento.

## Por que importa
Como os "nós" do `kind` são containers isolados que possuem seu próprio daemon `containerd` interno separado do daemon Docker do host, fazer apenas `docker build -t meu-app:v1 .` no host **não** torna a imagem visível para os Pods agendados dentro do `kind`. Além disso, usar a tag `:latest` causa falhas silenciosas de pull. A seção `Loading an Image Into Your Cluster` do `Quick Start` oficial explica tanto o comando `kind load` quanto a armadilha da `imagePullPolicy`.

## Como funciona
Após construir uma imagem localmente com `docker build -t my-custom-image:unique-tag ./my-image-dir`, o desenvolvedor executa **`kind load docker-image my-custom-image:unique-tag`** (adicionando `--name <cluster>` caso o cluster não tenha o nome padrão `kind`, ou passando múltiplas imagens na mesma linha). O `kind` exporta a imagem do Docker do host e a importa via `ctr` para dentro de todos os nós do cluster (também é possível carregar um arquivo `.tar` diretamente com **`kind load image-archive /my-image-archive.tar`**). Para inspecionar as imagens presentes dentro de um nó do `kind`, executa-se `docker exec -it <node-name> crictl images` (ex.: `kind-control-plane`).

## Exemplo
```bash
# Construir imagem com tag explícita (não :latest), carregá-la no cluster kind e verificar com crictl images no nó
docker build -t my-app:v1.0.0 .
kind load docker-image my-app:v1.0.0
docker exec -it kind-control-plane crictl images | grep my-app
```

## Limites e trade-offs
Conforme alerta a nota oficial do `Quick Start` do `kind`, a política de pull padrão do Kubernetes é `IfNotPresent` **a menos que a tag da imagem seja `:latest` ou omitida**, caso em que a política padrão passa a ser **`Always`**; se você carregar `my-app:latest` com `kind load docker-image`, o `kubelet` ainda tentará puxar `my-app:latest` do Docker Hub pela internet e falhará com `ErrImagePull` / `ImagePullBackOff`! Portanto, **nunca use a tag `:latest`** (use uma tag específica como `:v1.0.0` ou `:dev`) e/ou defina explicitamente `imagePullPolicy: IfNotPresent` ou `imagePullPolicy: Never` no Pod.

## Como verificar
Execute `docker exec -it kind-control-plane crictl images` para confirmar que a imagem carregada com `kind load docker-image` consta no armazenamento local do nó.

## Conexões
- [[kind-gerenciamento-clusters-contextos-kubeconfig-delete]] — Veja também: kind: gerenciamento de múltiplos clusters (--name), regras de merge do KUBECONFIG e deleção idempotente.
- [[kind-configuracao-multinode-control-plane-ha-port-mappings]] — Veja também: kind: configuração declarativa de clusters multi-nós, Control Plane HA e extraPortMappings (kind.x-k8s.io/v1alpha4).
- [[kind-clusters-kubernetes-locais-containers-docker-arquitetura]] — Referência cruzada direta com kind-clusters-kubernetes-locais-containers-docker-arquitetura.
- [[ko-integracao-kubernetes-ko-resolve-apply-delete-uri]] — Referência cruzada direta com ko-integracao-kubernetes-ko-resolve-apply-delete-uri.

## Fontes
- [kind GitHub — README.md (Kubernetes IN Docker, Go Packages & Design Principles)](https://raw.githubusercontent.com/kubernetes-sigs/kind/main/README.md) — README oficial do projeto kind (Kubernetes SIGs, Apache-2.0) sobre execução de nós em containers para testes do próprio Kubernetes e CI/CD; consultado em 2026-10-03.
- [kind Official Documentation — Quick Start (Installation, Multi-Node Config, Building & Loading Images, Exporting Logs)](https://kind.sigs.k8s.io/docs/user/quick-start/) — Guia oficial Quick Start do kind cobrindo instalação, criação/exclusão de clusters, imagens kindest/node com digest SHA-256, topologia multi-nó kind.x-k8s.io/v1alpha4, kind build node-image, kind load docker-image/image-archive e kind export logs; consultado em 2026-10-03.
- [Kubernetes SIGs kind — Official GitHub Repository](https://github.com/kubernetes-sigs/kind) — Repositório oficial do kind mantido pelo Kubernetes SIG Testing; consultado em 2026-10-03.
