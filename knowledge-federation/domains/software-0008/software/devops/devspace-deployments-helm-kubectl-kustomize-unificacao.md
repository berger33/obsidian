---
id: software.devops.tranche14.001354
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

# DevSpace: Unificação de Deployments com Helm Charts, Manifestos Kubectl e Kustomize

## Em uma frase
Na seção `deployments` do `devspace.yaml`, uma aplicação pode combinar múltiplos métodos de implantação na mesma execução — como **Helm charts** (locais ou remotos, inclusive usando o chart genérico `component-chart`), manifestos brutos via **`kubectl`** e overlays **Kustomize**.

## Por que importa
Um projeto real frequentemente precisa subir um banco Redis via Helm chart oficial da Bitnami, aplicar CRDs brutas via `kubectl` e implantar o serviço principal via Kustomize.

## Como funciona
O DevSpace executa os deployments na ordem configurada (ou concorrentemente), injeta as tags das imagens recém-construídas nos campos correspondentes de cada chart/manifesto e permite remover todos os recursos implantados com um único comando `devspace purge`.

## Exemplo
```yaml
version: v2beta1
deployments:
  redis:
    helm:
      chart:
        name: redis
        repo: https://charts.bitnami.com/bitnami
  app:
    kubectl:
      manifests:
        - k8s/deployment.yaml
        - k8s/service.yaml
```

## Limites e trade-offs
Encerrar o trabalho em um namespace temporário sem rodar `devspace purge` (ou deletar o namespace) mantém os Deployments e PVCs consumindo CPU e memória no cluster compartilhado.

## Como verificar
Execute `devspace purge` ao concluir os testes para limpar todas as releases Helm e manifestos aplicados pelo `devspace.yaml`.

## Conexões
- [[devspace-images-build-paralelo-kaniko-buildkit-docker-tags]] — Veja também: DevSpace: Build Paralelo de Imagens, Tagging Automático e Suporte a Docker, BuildKit e Kaniko.
- [[devspace-variaveis-configuracao-profiles-dev-staging-prod]] — Veja também: DevSpace: Variáveis Dinâmicas de Configuração (vars) e Perfis de Ambiente (profiles).

## Fontes
- [DevSpace GitHub — README.md (Client-Only Kubernetes Developer Tool, devspace.yaml, Hot Reloading, Parallel Image Building & Multi-Cluster Compatibility)](https://www.devspace.sh/docs/getting-started/introduction) — README oficial do devspace-sh/devspace (Apache-2.0, CNCF Sandbox) explicando a arquitetura client-only sobre kube-context, hot reloading com sync bidirecional, variáveis de configuração e automação de port-forwarding/logs; consultado em 2026-10-03.
- [DevSpace Official Documentation — Getting Started Introduction (Declarative Workflows, Team Standardization & Hot Reloading)](https://raw.githubusercontent.com/devspace-sh/devspace/main/README.md) — Introdução oficial da documentação do DevSpace 6.x detalhando o funcionamento do CLI sem componentes server-side obrigatórios e compatibilidade com clusters locais e gerenciados; consultado em 2026-10-03.
- [DevSpace — Official GitHub Repository](https://github.com/devspace-sh/devspace) — Repositório oficial do DevSpace; consultado em 2026-10-03.
