---
id: software.devops.tranche14.001331
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

# PipeCD: Arquitetura GitOps Unificada com Control Plane Central e Agentes Piped Stateless

## Em uma frase
O **PipeCD** (`pipe-cd/pipecd`, projeto **CNCF Sandbox**) é uma plataforma de entrega contínua (CD) estilo GitOps que oferece uma experiência unificada de implantação e análise progressiva para múltiplas plataformas (`KUBERNETES`, `TERRAFORM`, `CLOUDRUN`, `LAMBDA` e `ECS`) sem expor credenciais de cluster para fora da rede de destino.

## Por que importa
Ferramentas de CD que operam exclusivamente para Kubernetes obrigam equipes a manter pipelines totalmente diferentes no Jenkins/GitHub Actions para módulos Terraform, funções AWS Lambda e serviços Cloud Run.

## Como funciona
A arquitetura do PipeCD separa o **Control Plane** (centralizado, responsável pela UI web, autenticação SSO/RBAC, armazenamento de metadados, métricas de insights e API gRPC) do **`piped`** (um único binário stateless executado como agente dentro do cluster ou VPC de destino que faz pull outbound para o Control Plane e aplica os manifestos do Git localmente).

## Exemplo
```bash
# Verificar o Deployment do agente stateless piped no cluster Kubernetes:
kubectl -n pipecd get pods -l app.kubernetes.io/name=piped
```

## Limites e trade-offs
Acreditar que o Control Plane do PipeCD precisa de acesso de rede direto à API privada do cluster Kubernetes ou às chaves IAM da AWS é incorreto: é o agente `piped` que inicia a conexão gRPC de saída para o Control Plane.

## Como verificar
Mantenha todas as credenciais de nuvem e do Kubernetes restritas ao ambiente local onde o agente `piped` executa.

## Conexões
- [[pipecd-application-configuration-app-pipecd-yaml-sem-crds]] — Veja também: PipeCD: Contrato Declarativo app.pipecd.yaml sem Alteração de Manifestos ou CRDs no Cluster.

## Fontes
- [PipeCD Official Documentation — Core Concepts (Control Plane, Stateless Piped Agent, Projects, app.pipecd.yaml, Sync Strategies, Platform & Analysis Providers)](https://pipecd.dev/docs-v0.58.x/concepts/) — Documentação oficial de conceitos do PipeCD detalhando a arquitetura Control Plane + Piped stateless, papéis Viewer/Editor/Admin, Quick Sync vs Pipeline Sync, Platform Providers e Analysis Providers; consultado em 2026-10-03.
- [PipeCD GitHub — README.md (Unified Multi-Platform GitOps CD, Progressive Delivery, Built-in ADA & Delivery Insights)](https://raw.githubusercontent.com/pipe-cd/pipecd/master/README.md) — README oficial do pipe-cd/pipecd (CNCF Sandbox) explicando o fluxo GitOps sem exposição de credenciais externas, análise automática de deploy e métricas DORA no Delivery Insights; consultado em 2026-10-03.
- [PipeCD — Official GitHub Repository](https://github.com/pipe-cd/pipecd) — Repositório oficial Apache-2.0 do PipeCD; consultado em 2026-10-03.
