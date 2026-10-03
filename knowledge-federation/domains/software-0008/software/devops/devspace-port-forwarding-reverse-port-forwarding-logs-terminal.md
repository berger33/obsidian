---
id: software.devops.tranche14.001358
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

# DevSpace: Automação de Port-Forwarding, Reverse Port-Forwarding, Logs e Terminal Interativo

## Em uma frase
Durante o fluxo de trabalho diário, o DevSpace automatiza o **port-forwarding** (`localhost -> Pod`), o **reverse port-forwarding** (`Pod -> localhost`), o streaming agregado de logs de múltiplos containers e a abertura direta de terminal (`devspace enter`).

## Por que importa
Quando um container dentro do cluster precisa chamar um webhook ou serviço que está rodando localmente apenas na IDE do desenvolvedor na porta `3000`, o `kubectl port-forward` comum (que só encaminha no sentido máquina local -> Pod) não resolve.

## Como funciona
Configurando `ports` na seção `dev` do `devspace.yaml`, `port: "8080:8080"` encaminha a porta local para o Pod, enquanto `remotePort` em modo reverso expõe um serviço local da estação de trabalho para dentro do container no Kubernetes, com reconexão automática se a conexão cair.

## Exemplo
```bash
devspace enter
devspace logs -f
```

## Limites e trade-offs
Mapear a mesma porta local (como `8080:8080`) para dois serviços diferentes dentro do mesmo `devspace.yaml` causa erro de porta já em uso (`bind: address already in use`) na máquina local.

## Como verificar
Atribua portas locais distintas para cada microsserviço no `devspace.yaml` (por exemplo, `8080:80`, `8081:80`).

## Conexões
- [[devspace-dependencies-monorepos-multi-repositorio-microsservicos]] — Veja também: DevSpace: Orquestração de Dependências Multi-Repositório e Monorepos (dependencies).
- [[devspace-pipelines-customizados-commands-hooks-ci-cd]] — Veja também: DevSpace: Pipelines Declarativos Customizados (pipelines), Hooks e Comandos de Equipe (commands).

## Fontes
- [DevSpace GitHub — README.md (Client-Only Kubernetes Developer Tool, devspace.yaml, Hot Reloading, Parallel Image Building & Multi-Cluster Compatibility)](https://www.devspace.sh/docs/getting-started/introduction) — README oficial do devspace-sh/devspace (Apache-2.0, CNCF Sandbox) explicando a arquitetura client-only sobre kube-context, hot reloading com sync bidirecional, variáveis de configuração e automação de port-forwarding/logs; consultado em 2026-10-03.
- [DevSpace Official Documentation — Getting Started Introduction (Declarative Workflows, Team Standardization & Hot Reloading)](https://raw.githubusercontent.com/devspace-sh/devspace/main/README.md) — Introdução oficial da documentação do DevSpace 6.x detalhando o funcionamento do CLI sem componentes server-side obrigatórios e compatibilidade com clusters locais e gerenciados; consultado em 2026-10-03.
- [DevSpace — Official GitHub Repository](https://github.com/devspace-sh/devspace) — Repositório oficial do DevSpace; consultado em 2026-10-03.
