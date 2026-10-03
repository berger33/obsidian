---
id: software.devops.tranche09.000832
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

# kind: gerenciamento de múltiplos clusters (--name), regras de merge do KUBECONFIG e deleção idempotente

## Em uma frase
O `kind` permite criar múltiplos clusters isolados na mesma máquina via `--name <nome>` (criando o contexto `kind-<nome>` no `kubectl`), segue as regras padrão de merge da variável `$KUBECONFIG` (ou isolamento via `--kubeconfig`) e oferece deleção idempotente com `kind delete cluster`.

## Por que importa
Em testes de integração multi-cluster (como testar service mesh multi-cluster, replicação de banco ou migração `clusterctl move`), o desenvolvedor precisa rodar dois ou três clusters Kubernetes simultaneamente na mesma máquina e entender como o `kind` grava credenciais no arquivo `kubeconfig` e limpa recursos em scripts de CI. A seção `Interacting With Your Cluster` e `Deleting a Cluster` do `Quick Start` oficial explica essas regras.

## Como funciona
Quando `kind create cluster` é executado sem `--name`, o cluster recebe o nome padrão `kind` e o contexto do `kubectl` é gravado como **`kind-kind`**. Passando `--name kind-2`, cria-se um segundo cluster independente com contexto **`kind-kind-2`**. Para o armazenamento do `kubeconfig`: (1) se `$KUBECONFIG` não estiver definida, o `kind` grava em `${HOME}/.kube/config`; (2) se `$KUBECONFIG` contiver uma lista de caminhos separados por `:` (ou `;` no Windows), os arquivos são mesclados; e (3) se a flag **`--kubeconfig <arquivo>`** for passada na criação, apenas aquele arquivo específico é usado sem nenhum merge. Para destruir um cluster, `kind delete cluster [--name <nome>]` remove os containers e volumes: **por design, pedir para deletar um cluster que não existe não retorna erro**, garantindo limpeza idempotente em scripts de CI.

## Exemplo
```bash
# Criar um cluster dedicado gravando o kubeconfig em um arquivo isolado e limpá-lo de forma idempotente
kind create cluster --name ci-test --kubeconfig ./ci-kubeconfig.yaml
kubectl --kubeconfig ./ci-kubeconfig.yaml get nodes
kind delete cluster --name ci-test
```

## Limites e trade-offs
Se você definir a variável de ambiente `KIND_EXPERIMENTAL_PROVIDER=docker`, `KIND_EXPERIMENTAL_PROVIDER=podman` ou `KIND_EXPERIMENTAL_PROVIDER=nerdctl` para desativar a auto-detecção de runtime do `kind`, certifique-se de usar a mesma variável tanto no `kind create cluster` quanto no `kind get clusters` e `kind delete cluster`, caso contrário o `kind` procurará os containers no provedor errado.

## Como verificar
Execute `kind get clusters` após `kind delete cluster --name ci-test` para confirmar que o cluster foi removido e rode `kind delete cluster --name ci-test` uma segunda vez para verificar que o código de saída continua sendo `0` (idempotência).

## Conexões
- [[kind-clusters-kubernetes-locais-containers-docker-arquitetura]] — Veja também: kind (Kubernetes IN Docker): execução de clusters Kubernetes locais usando containers como nós.
- [[kind-carregamento-imagens-locais-load-docker-image-archive]] — Veja também: kind: carregamento direto de imagens locais para dentro do cluster (kind load docker-image e image-archive).
- [[minikube-clusters-locais-kubernetes-perfis-controles-basicos]] — Referência cruzada direta com minikube-clusters-locais-kubernetes-perfis-controles-basicos.

## Fontes
- [kind GitHub — README.md (Kubernetes IN Docker, Go Packages & Design Principles)](https://raw.githubusercontent.com/kubernetes-sigs/kind/main/README.md) — README oficial do projeto kind (Kubernetes SIGs, Apache-2.0) sobre execução de nós em containers para testes do próprio Kubernetes e CI/CD; consultado em 2026-10-03.
- [kind Official Documentation — Quick Start (Installation, Multi-Node Config, Building & Loading Images, Exporting Logs)](https://kind.sigs.k8s.io/docs/user/quick-start/) — Guia oficial Quick Start do kind cobrindo instalação, criação/exclusão de clusters, imagens kindest/node com digest SHA-256, topologia multi-nó kind.x-k8s.io/v1alpha4, kind build node-image, kind load docker-image/image-archive e kind export logs; consultado em 2026-10-03.
- [Kubernetes SIGs kind — Official GitHub Repository](https://github.com/kubernetes-sigs/kind) — Repositório oficial do kind mantido pelo Kubernetes SIG Testing; consultado em 2026-10-03.
