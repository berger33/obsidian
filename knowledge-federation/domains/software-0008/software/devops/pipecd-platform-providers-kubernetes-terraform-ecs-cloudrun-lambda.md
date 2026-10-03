---
id: software.devops.tranche14.001334
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
fontes: ["https://pipecd.dev/docs-v0.58.x/concepts/", "https://raw.githubusercontent.com/pipe-cd/pipecd/master/README.md", "https://github.com/pipe-cd/pipecd"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# PipeCD: Platform Providers Multi-Cloud (Kubernetes, Terraform, AWS ECS, GCP Cloud Run e Lambda)

## Em uma frase
No modelo conceitual do PipeCD, o **Platform Provider** (anteriormente chamado de Cloud Provider na configuração do `piped`) define em qual plataforma e ambiente uma aplicação deve ser implantada, suportando nativamente **`KUBERNETES`**, **`TERRAFORM`**, **`ECS`**, **`CLOUDRUN`** e **`LAMBDA`**.

## Por que importa
Em arquiteturas modernas, um mesmo produto frequentemente combina microsserviços no EKS/GKE (`KUBERNETES`), infraestrutura de banco e filas no `TERRAFORM` e workers serverless no `CLOUDRUN` ou `LAMBDA`.

## Como funciona
Um único agente `piped` pode declarar múltiplos `platformProviders` em seu arquivo de configuração, permitindo que a mesma interface web, o mesmo modelo de aprovação manual (`WAIT_APPROVAL`) e o mesmo fluxo de Pull Request gerenciem todos os cinco tipos de workload.

## Exemplo
```yaml
apiVersion: pipecd.dev/v1beta1
kind: Piped
spec:
  projectID: prod-project
  pipedID: piped-multi-platform
  platformProviders:
    - name: k8s-prod
      type: KUBERNETES
    - name: infra-tf
      type: TERRAFORM
    - name: serverless-run
      type: CLOUDRUN
```

## Limites e trade-offs
Renomear o campo `name` de um `platformProvider` na configuração do `piped` sem atualizar as aplicações vinculadas a ele no Control Plane faz com que novos deployments daquelas aplicações fiquem sem executor disponível.

## Como verificar
Mantenha os nomes dos `platformProviders` estáveis e associe cada aplicação ao provider correspondente do seu ambiente.

## Conexões
- [[pipecd-sync-strategies-quick-sync-pipeline-sync-auto]] — Veja também: PipeCD: Estratégias de Sincronização (Quick Sync, Pipeline Sync e Auto Sync).
- [[pipecd-automated-deployment-analysis-ada-prometheus-datadog-rollback]] — Veja também: PipeCD: Análise Automatizada de Deploy (ADA) com Analysis Providers e Auto-Rollback.

## Fontes
- [PipeCD Official Documentation — Core Concepts (Control Plane, Stateless Piped Agent, Projects, app.pipecd.yaml, Sync Strategies, Platform & Analysis Providers)](https://pipecd.dev/docs-v0.58.x/concepts/) — Documentação oficial de conceitos do PipeCD detalhando a arquitetura Control Plane + Piped stateless, papéis Viewer/Editor/Admin, Quick Sync vs Pipeline Sync, Platform Providers e Analysis Providers; consultado em 2026-10-03.
- [PipeCD GitHub — README.md (Unified Multi-Platform GitOps CD, Progressive Delivery, Built-in ADA & Delivery Insights)](https://raw.githubusercontent.com/pipe-cd/pipecd/master/README.md) — README oficial do pipe-cd/pipecd (CNCF Sandbox) explicando o fluxo GitOps sem exposição de credenciais externas, análise automática de deploy e métricas DORA no Delivery Insights; consultado em 2026-10-03.
- [PipeCD — Official GitHub Repository](https://github.com/pipe-cd/pipecd) — Repositório oficial Apache-2.0 do PipeCD; consultado em 2026-10-03.
