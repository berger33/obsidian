---
id: software.devops.tranche14.001352
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
fontes: ["https://www.devspace.sh/docs/getting-started/introduction", "https://raw.githubusercontent.com/devspace-sh/devspace/main/README.md", "https://github.com/devspace-sh/devspace"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# DevSpace: Desenvolvimento com Hot Reloading e Sincronização Bidirecional de Arquivos (devspace dev)

## Em uma frase
O comando `devspace dev` substitui o ciclo lento de reconstruir imagens Docker e recriar Pods a cada alteração de código por **sincronização bidirecional de arquivos em tempo real** (`sync`) combinada com **hot reloading** dentro do container em execução no Kubernetes.

## Por que importa
Esperar de 3 a 8 minutos para compilar uma imagem, enviá-la ao registry e aguardar o rollout do Pod para testar a mudança de uma única linha de código inviabiliza o desenvolvimento cloud-native.

## Como funciona
Durante `devspace dev`, o DevSpace injeta um helper leve no container de desenvolvimento, monitora alterações de arquivos na IDE local e sincroniza imediatamente os deltas com o sistema de arquivos do container no cluster, além de iniciar automaticamente port-forwarding, streaming de logs ou um terminal interativo.

## Exemplo
```yaml
version: v2beta1
dev:
  api:
    imageSelector: ghcr.io/org/api
    sync:
      - path: ./src:/app/src
        excludePaths:
          - node_modules/
          - .git/
    ports:
      - port: "8080:8080"
```

## Limites e trade-offs
Não incluir pastas volumosas de dependências locais (como `node_modules/`, `.git/` ou `target/`) em `excludePaths` na configuração de `sync` transfere milhares de arquivos pequenos pela rede ao iniciar a sessão.

## Como verificar
Exclua sempre diretórios de dependências e artefatos de build em `excludePaths` para manter a sincronização instantânea.

## Conexões
- [[devspace-arquitetura-client-only-devspace-yaml-kubernetes-cncf]] — Veja também: DevSpace: Arquitetura Client-Only para Desenvolvimento Kubernetes (devspace.yaml) na CNCF.
- [[devspace-images-build-paralelo-kaniko-buildkit-docker-tags]] — Veja também: DevSpace: Build Paralelo de Imagens, Tagging Automático e Suporte a Docker, BuildKit e Kaniko.

## Fontes
- [DevSpace GitHub — README.md (Client-Only Kubernetes Developer Tool, devspace.yaml, Hot Reloading, Parallel Image Building & Multi-Cluster Compatibility)](https://www.devspace.sh/docs/getting-started/introduction) — README oficial do devspace-sh/devspace (Apache-2.0, CNCF Sandbox) explicando a arquitetura client-only sobre kube-context, hot reloading com sync bidirecional, variáveis de configuração e automação de port-forwarding/logs; consultado em 2026-10-03.
- [DevSpace Official Documentation — Getting Started Introduction (Declarative Workflows, Team Standardization & Hot Reloading)](https://raw.githubusercontent.com/devspace-sh/devspace/main/README.md) — Introdução oficial da documentação do DevSpace 6.x detalhando o funcionamento do CLI sem componentes server-side obrigatórios e compatibilidade com clusters locais e gerenciados; consultado em 2026-10-03.
- [DevSpace — Official GitHub Repository](https://github.com/devspace-sh/devspace) — Repositório oficial do DevSpace; consultado em 2026-10-03.
