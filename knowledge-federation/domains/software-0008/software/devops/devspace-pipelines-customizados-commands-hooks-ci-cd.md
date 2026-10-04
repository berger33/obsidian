---
id: software.devops.tranche14.001359
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

# DevSpace: Pipelines Declarativos Customizados (pipelines), Hooks e Comandos de Equipe (commands)

## Em uma frase
O `devspace.yaml` na versão `v2beta1` utiliza um motor de **pipelines** em shell POSIX integrado (`pipelines:` e `commands:`), permitindo customizar completamente o comportamento de `devspace dev`, `devspace deploy`, `devspace build` e criar novos comandos de projeto (`devspace run <comando>`).

## Por que importa
Scripts de preparação de banco de dados (migrations), geração de código gRPC/Protobuf e testes de integração costumam ficar soltos fora do fluxo de deploy do Kubernetes.

## Como funciona
Dentro de `pipelines:`, o engenheiro orquestra funções nativas do motor DevSpace (`build_images --all`, `create_deployments --all`, `start_dev --all`, `run_dependencies --all`) combinadas com lógica condicional bash, e expõe atalhos padronizados para toda a equipe em `commands:`.

## Exemplo
```yaml
version: v2beta1
pipelines:
  deploy:
    run: |
      run_dependencies --all
      build_images --all
      create_deployments --all
commands:
  migrate:
    command: kubectl exec deploy/backend -- ./app migrate up
```

## Limites e trade-offs
Sobrescrever o pipeline `dev` ou `deploy` esquecendo de chamar `build_images` ou `create_deployments` faz com que o comando rode sem atualizar os containers no cluster.

## Como verificar
Inspecione os pipelines disponíveis com `devspace list commands` e mantenha os passos essenciais (`build_images`, `create_deployments`) explícitos nos pipelines customizados.

## Conexões
- [[devspace-port-forwarding-reverse-port-forwarding-logs-terminal]] — Veja também: DevSpace: Automação de Port-Forwarding, Reverse Port-Forwarding, Logs e Terminal Interativo.
- [[devspace-paridade-local-kind-minikube-vs-clusters-remotos-ci]] — Veja também: DevSpace: Paridade de Workflow entre Clusters Locais (kind/minikube), Dev Clusters Remotos e CI/CD.

## Fontes
- [DevSpace GitHub — README.md (Client-Only Kubernetes Developer Tool, devspace.yaml, Hot Reloading, Parallel Image Building & Multi-Cluster Compatibility)](https://raw.githubusercontent.com/devspace-sh/devspace/main/README.md) — README oficial do devspace-sh/devspace (Apache-2.0, CNCF Sandbox) explicando a arquitetura client-only sobre kube-context, hot reloading com sync bidirecional, variáveis de configuração e automação de port-forwarding/logs; consultado em 2026-10-03.
- [DevSpace Official Documentation — Getting Started Introduction (Declarative Workflows, Team Standardization & Hot Reloading)](https://www.devspace.sh/docs/getting-started/introduction) — Introdução oficial da documentação do DevSpace 6.x detalhando o funcionamento do CLI sem componentes server-side obrigatórios e compatibilidade com clusters locais e gerenciados; consultado em 2026-10-03.
- [DevSpace — Official GitHub Repository](https://github.com/devspace-sh/devspace) — Repositório oficial do DevSpace; consultado em 2026-10-03.
