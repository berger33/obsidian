---
id: software.devops.tranche14.001356
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

# DevSpace: Substituição Temporária de Containers em Execução (replacePods) para Debug Remoto

## Em uma frase
No modo `devspace dev`, a configuração de desenvolvimento (`dev`) permite substituir temporariamente a imagem de produção de um Pod no cluster por uma imagem de desenvolvimento contendo compiladores, `dlv` (Delve para Go), `debugpy` ou `node --inspect`, sem alterar os manifestos originais versionados no Git.

## Por que importa
Imagens de produção seguras (distroless ou construídas com `apko`) não possuem shell (`/bin/sh`), gerenciador de pacotes nem ferramentas de debug, impossibilitando compilar ou anexar um debugger diretamente na imagem de produção.

## Como funciona
Ao iniciar `devspace dev`, o DevSpace intercepta o Deployment/Pod selecionado por `imageSelector` ou `labelSelector`, substitui a imagem pelo `devImage`, sobrescreve o `command` para aguardar conexões de debug ou rodar um watcher de hot-reload e reverte o Pod para a imagem original ao encerrar a sessão.

## Exemplo
```yaml
version: v2beta1
dev:
  backend:
    imageSelector: ghcr.io/org/backend
    devImage: golang:1.23-bookworm
    command: ["dlv", "debug", "./cmd/api", "--headless", "--listen=:2345", "--api-version=2"]
    ports:
      - port: "2345:2345"
```

## Limites e trade-offs
Deixar um Pod substituído por `devImage` rodando indefinidamente em um ambiente de staging após desconectar a máquina local deixa o serviço executando em modo debug.

## Como verificar
Encerre a sessão `devspace dev` limpa ou execute `devspace reset pods` para restaurar os Pods ao estado original de produção.

## Conexões
- [[devspace-variaveis-configuracao-profiles-dev-staging-prod]] — Veja também: DevSpace: Variáveis Dinâmicas de Configuração (vars) e Perfis de Ambiente (profiles).
- [[devspace-dependencies-monorepos-multi-repositorio-microsservicos]] — Veja também: DevSpace: Orquestração de Dependências Multi-Repositório e Monorepos (dependencies).

## Fontes
- [DevSpace GitHub — README.md (Client-Only Kubernetes Developer Tool, devspace.yaml, Hot Reloading, Parallel Image Building & Multi-Cluster Compatibility)](https://www.devspace.sh/docs/getting-started/introduction) — README oficial do devspace-sh/devspace (Apache-2.0, CNCF Sandbox) explicando a arquitetura client-only sobre kube-context, hot reloading com sync bidirecional, variáveis de configuração e automação de port-forwarding/logs; consultado em 2026-10-03.
- [DevSpace Official Documentation — Getting Started Introduction (Declarative Workflows, Team Standardization & Hot Reloading)](https://raw.githubusercontent.com/devspace-sh/devspace/main/README.md) — Introdução oficial da documentação do DevSpace 6.x detalhando o funcionamento do CLI sem componentes server-side obrigatórios e compatibilidade com clusters locais e gerenciados; consultado em 2026-10-03.
- [DevSpace — Official GitHub Repository](https://github.com/devspace-sh/devspace) — Repositório oficial do DevSpace; consultado em 2026-10-03.
