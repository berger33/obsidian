---
id: software.devops.tranche14.001355
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

# DevSpace: Variáveis Dinâmicas de Configuração (vars) e Perfis de Ambiente (profiles)

## Em uma frase
O DevSpace torna o `devspace.yaml` altamente reutilizável entre desenvolvedores e ambientes (dev, staging e produção) por meio de **variáveis de configuração (`vars`)** e **perfis (`profiles`)** que aplicam patches ou substituem configurações em tempo de execução via flag `-p / --profile`.

## Por que importa
Manter arquivos de pipeline completamente duplicados para desenvolvimento local, ambiente de preview por PR e deploy de produção faz com que ajustes na topologia da aplicação fiquem dessincronizados.

## Como funciona
Com `vars`, cada desenvolvedor pode ter um subdomínio ou sufixo próprio (`${DEVSPACE_USERNAME}`), enquanto `profiles` (ativados com `devspace deploy -p production`) substituem o `Dockerfile` de desenvolvimento por uma imagem otimizada de produção e ajustam réplicas e limites de recursos.

## Exemplo
```bash
devspace print -p production
devspace deploy -p production --var REPLICAS=3
```

## Limites e trade-offs
Aplicar um perfil (`-p`) complexo sem inspecionar o YAML final renderizado pode ocultar substituições indesejadas de variáveis ou patches.

## Como verificar
Use sempre `devspace print -p <perfil>` para visualizar e validar o `devspace.yaml` final resolvido antes de executar `devspace deploy -p <perfil>`.

## Conexões
- [[devspace-deployments-helm-kubectl-kustomize-unificacao]] — Veja também: DevSpace: Unificação de Deployments com Helm Charts, Manifestos Kubectl e Kustomize.
- [[devspace-replace-pods-container-desenvolvimento-debug-remoto]] — Veja também: DevSpace: Substituição Temporária de Containers em Execução (replacePods) para Debug Remoto.

## Fontes
- [DevSpace GitHub — README.md (Client-Only Kubernetes Developer Tool, devspace.yaml, Hot Reloading, Parallel Image Building & Multi-Cluster Compatibility)](https://raw.githubusercontent.com/devspace-sh/devspace/main/README.md) — README oficial do devspace-sh/devspace (Apache-2.0, CNCF Sandbox) explicando a arquitetura client-only sobre kube-context, hot reloading com sync bidirecional, variáveis de configuração e automação de port-forwarding/logs; consultado em 2026-10-03.
- [DevSpace Official Documentation — Getting Started Introduction (Declarative Workflows, Team Standardization & Hot Reloading)](https://www.devspace.sh/docs/getting-started/introduction) — Introdução oficial da documentação do DevSpace 6.x detalhando o funcionamento do CLI sem componentes server-side obrigatórios e compatibilidade com clusters locais e gerenciados; consultado em 2026-10-03.
- [DevSpace — Official GitHub Repository](https://github.com/devspace-sh/devspace) — Repositório oficial do DevSpace; consultado em 2026-10-03.
