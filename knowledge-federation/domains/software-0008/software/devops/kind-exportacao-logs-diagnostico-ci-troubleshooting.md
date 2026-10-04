---
id: software.devops.tranche09.000837
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

# kind: exportação estruturada de logs do cluster e dos nós para diagnóstico em CI (kind export logs)

## Em uma frase
O comando `kind export logs [<diretorio>] [--name <cluster>]` coleta e exporta automaticamente uma árvore completa de diagnóstico contendo informações do host Docker e, para cada nó do cluster, `journal.log`, `kubelet.log`, `inspect.json`, versão do Kubernetes e logs de todos os containers e pods.

## Por que importa
Quando um teste end-to-end falha em um runner efêmero de CI (como GitHub Actions ou Prow), o cluster `kind` será destruído logo ao final do job; se o pipeline não exportar todos os logs do `kubelet`, do `systemd` (`journal.log`), do `containerd` e de todos os pods antes de encerrar o runner, torna-se impossível diagnosticar por que o teste falhou. A seção `Exporting Cluster Logs` do `Quick Start` oficial do `kind` documenta essa ferramenta nativa.

## Como funciona
Ao executar **`kind export logs ./ci-artifacts/kind-logs`** (ou sem argumento de caminho para exportar para um diretório temporário `/tmp/...` impresso na saída), o `kind` conecta-se ao runtime de containers e a cada container nó do cluster (`kind-control-plane`, `kind-worker`, etc.) e extrai uma árvore padronizada de arquivos: na raiz grava `docker-info.txt` (informações do host de containers) e, dentro do subdiretório de cada nó (`kind-control-plane/`), grava `containers/`, `docker.log` / `containerd`, `inspect.json`, `journal.log`, `kubelet.log`, `kubernetes-version.txt` e o diretório `pods/` com os logs de todos os pods que rodaram naquele nó.

## Exemplo
```bash
# Exportar todos os logs do cluster kind e de seus nós para um diretório de artefatos de CI
kind export logs ./kind-ci-logs --name kind
ls -la ./kind-ci-logs/kind-control-plane/
```

## Limites e trade-offs
Em pipelines de CI/CD (como GitHub Actions), o passo que executa `kind export logs ./kind-ci-logs` seguido do upload de artefatos deve sempre ser configurado com a condição `if: always()` (ou `if: failure()`), garantindo que a coleta ocorra mesmo quando o passo anterior de testes de integração falhar e antes que o job encerre ou execute `kind delete cluster`.

## Como verificar
Execute `kind export logs ./logs-teste` em um cluster local ativo e inspecione a presença de `kubelet.log`, `journal.log` e `pods/` dentro de `./logs-teste/kind-control-plane/`.

## Conexões
- [[kind-construcao-node-image-codigo-fonte-kubernetes-build]] — Veja também: kind: construção de imagens de nó customizadas (kind build node-image) a partir de source, release, url ou file.
- [[kind-instalacao-reprodutivel-make-gimme-go-install-binarios]] — Veja também: kind: instalação via binários de release, go install e compilação reprodutível sem Go pré-instalado (make build com gimme).
- [[kind-clusters-kubernetes-locais-containers-docker-arquitetura]] — Referência cruzada direta com kind-clusters-kubernetes-locais-containers-docker-arquitetura.
- [[kind-gerenciamento-clusters-contextos-kubeconfig-delete]] — Referência cruzada direta com kind-gerenciamento-clusters-contextos-kubeconfig-delete.

## Fontes
- [kind GitHub — README.md (Kubernetes IN Docker, Go Packages & Design Principles)](https://raw.githubusercontent.com/kubernetes-sigs/kind/main/README.md) — README oficial do projeto kind (Kubernetes SIGs, Apache-2.0) sobre execução de nós em containers para testes do próprio Kubernetes e CI/CD; consultado em 2026-10-03.
- [kind Official Documentation — Quick Start (Installation, Multi-Node Config, Building & Loading Images, Exporting Logs)](https://kind.sigs.k8s.io/docs/user/quick-start/) — Guia oficial Quick Start do kind cobrindo instalação, criação/exclusão de clusters, imagens kindest/node com digest SHA-256, topologia multi-nó kind.x-k8s.io/v1alpha4, kind build node-image, kind load docker-image/image-archive e kind export logs; consultado em 2026-10-03.
- [Kubernetes SIGs kind — Official GitHub Repository](https://github.com/kubernetes-sigs/kind) — Repositório oficial do kind mantido pelo Kubernetes SIG Testing; consultado em 2026-10-03.
