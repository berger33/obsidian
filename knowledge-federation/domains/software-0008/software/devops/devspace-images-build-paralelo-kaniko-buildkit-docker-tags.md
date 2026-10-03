---
id: software.devops.tranche14.001353
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
fontes: ["https://raw.githubusercontent.com/devspace-sh/devspace/main/README.md", "https://www.devspace.sh/docs/getting-started/introduction", "https://github.com/devspace-sh/devspace"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# DevSpace: Build Paralelo de Imagens, Tagging Automático e Suporte a Docker, BuildKit e Kaniko

## Em uma frase
A seção `images` do `devspace.yaml` automatiza a construção paralela e o tagging automático (por hash de conteúdo/contexto ou timestamp) de múltiplas imagens de container, suportando o daemon Docker local, BuildKit ou **builds in-cluster com Kaniko** quando não há Docker instalado na máquina.

## Por que importa
Construir 5 imagens de microsserviços sequencialmente e lembrar de atualizar a tag de cada imagem nos valores do Helm chart ou nos manifestos Kubernetes manualmente gera erros de implantação com imagens antigas em cache.

## Como funciona
O DevSpace calcula se o contexto de arquivos da imagem mudou (pulando builds desnecessários), constrói as imagens modificadas em paralelo e substitui automaticamente a referência da imagem com a nova tag gerada em todos os manifestos `deployments` ou Helm charts antes de aplicá-los.

## Exemplo
```yaml
version: v2beta1
images:
  backend:
    image: ghcr.io/org/backend
    dockerfile: ./Dockerfile
    rebuildStrategy: ignoreContextChanges
  worker:
    image: ghcr.io/org/worker
    dockerfile: ./cmd/worker/Dockerfile
```

## Limites e trade-offs
Usar tags fixas como `:latest` fora do controle do DevSpace com `imagePullPolicy: IfNotPresent` faz o Kubernetes reutilizar a imagem antiga em cache no nó mesmo após um novo build.

## Como verificar
Deixe o DevSpace gerenciar o tagging automático das entradas declaradas em `images:` para garantir que o Kubernetes puxe exatamente a versão recém-construída.

## Conexões
- [[devspace-dev-hot-reloading-file-sync-bidirecional-containers]] — Veja também: DevSpace: Desenvolvimento com Hot Reloading e Sincronização Bidirecional de Arquivos (devspace dev).
- [[devspace-deployments-helm-kubectl-kustomize-unificacao]] — Veja também: DevSpace: Unificação de Deployments com Helm Charts, Manifestos Kubectl e Kustomize.

## Fontes
- [DevSpace GitHub — README.md (Client-Only Kubernetes Developer Tool, devspace.yaml, Hot Reloading, Parallel Image Building & Multi-Cluster Compatibility)](https://raw.githubusercontent.com/devspace-sh/devspace/main/README.md) — README oficial do devspace-sh/devspace (Apache-2.0, CNCF Sandbox) explicando a arquitetura client-only sobre kube-context, hot reloading com sync bidirecional, variáveis de configuração e automação de port-forwarding/logs; consultado em 2026-10-03.
- [DevSpace Official Documentation — Getting Started Introduction (Declarative Workflows, Team Standardization & Hot Reloading)](https://www.devspace.sh/docs/getting-started/introduction) — Introdução oficial da documentação do DevSpace 6.x detalhando o funcionamento do CLI sem componentes server-side obrigatórios e compatibilidade com clusters locais e gerenciados; consultado em 2026-10-03.
- [DevSpace — Official GitHub Repository](https://github.com/devspace-sh/devspace) — Repositório oficial do DevSpace; consultado em 2026-10-03.
