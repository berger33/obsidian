---
id: software.devops.tranche14.001357
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

# DevSpace: Orquestração de Dependências Multi-Repositório e Monorepos (dependencies)

## Em uma frase
A seção `dependencies` do `devspace.yaml` permite referenciar outros projetos que também possuem um `devspace.yaml` (em outras pastas de um monorepo ou em repositórios Git externos fixados por branch/tag), construindo e implantando toda a árvore de microsserviços dependentes com um único comando.

## Por que importa
Quando um desenvolvedor do serviço de `checkout` precisa que os serviços de `auth` e `catalog` estejam rodando no seu namespace pessoal de desenvolvimento, clonar e implantar manualmente cada repositório dependente demora horas.

## Como funciona
O DevSpace resolve o grafo de `dependencies` recursivamente, constrói as imagens necessárias e executa os pipelines das dependências antes de subir o serviço principal.

## Exemplo
```yaml
version: v2beta1
dependencies:
  auth-service:
    source:
      git: https://github.com/org/auth-service.git
      branch: main
  shared-db:
    source:
      path: ../shared-db
```

## Limites e trade-offs
Criar dependências circulares entre dois arquivos `devspace.yaml` ou apontar para branches instáveis sem fixar tag/revision pode quebrar o bootstrap do ambiente.

## Como verificar
Mantenha o grafo de `dependencies` acíclico e fixe tags ou commits estáveis para dependências de repositórios Git externos.

## Conexões
- [[devspace-replace-pods-container-desenvolvimento-debug-remoto]] — Veja também: DevSpace: Substituição Temporária de Containers em Execução (replacePods) para Debug Remoto.
- [[devspace-port-forwarding-reverse-port-forwarding-logs-terminal]] — Veja também: DevSpace: Automação de Port-Forwarding, Reverse Port-Forwarding, Logs e Terminal Interativo.

## Fontes
- [DevSpace GitHub — README.md (Client-Only Kubernetes Developer Tool, devspace.yaml, Hot Reloading, Parallel Image Building & Multi-Cluster Compatibility)](https://raw.githubusercontent.com/devspace-sh/devspace/main/README.md) — README oficial do devspace-sh/devspace (Apache-2.0, CNCF Sandbox) explicando a arquitetura client-only sobre kube-context, hot reloading com sync bidirecional, variáveis de configuração e automação de port-forwarding/logs; consultado em 2026-10-03.
- [DevSpace Official Documentation — Getting Started Introduction (Declarative Workflows, Team Standardization & Hot Reloading)](https://www.devspace.sh/docs/getting-started/introduction) — Introdução oficial da documentação do DevSpace 6.x detalhando o funcionamento do CLI sem componentes server-side obrigatórios e compatibilidade com clusters locais e gerenciados; consultado em 2026-10-03.
- [DevSpace — Official GitHub Repository](https://github.com/devspace-sh/devspace) — Repositório oficial do DevSpace; consultado em 2026-10-03.
