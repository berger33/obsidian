---
id: software.devops.tranche14.001340
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
fontes: ["https://raw.githubusercontent.com/pipe-cd/pipecd/master/README.md", "https://pipecd.dev/docs-v0.58.x/concepts/", "https://github.com/pipe-cd/pipecd"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# PipeCD: Delivery Insights e Medição Nativa de Métricas DORA (Deployment Frequency, Lead Time, MTTR e CFR)

## Em uma frase
O Control Plane do PipeCD inclui um painel nativo de **Delivery Insights** que calcula automaticamente as quatro métricas **DORA** (**Deployment Frequency**, **Lead Time for Changes**, **Mean Time to Restore — MTTR** e **Change Failure Rate — CFR**) para todas as aplicações gerenciadas.

## Por que importa
Coletar métricas DORA com planilhas ou scripts externos que tentam correlacionar commits do GitHub com jobs de CI falha porque o CI não sabe se o deploy em produção realmente concluiu com sucesso ou sofreu rollback automático.

## Como funciona
Como o PipeCD controla todo o ciclo de vida do deployment (do commit no Git até a conclusão dos estágios de rollout ou rollback por falha no `ANALYSIS`), ele registra com precisão a frequência de entregas, a taxa de falha de mudanças e o tempo de recuperação por projeto e aplicação.

## Exemplo
```bash
# Exemplo de consulta via pipectl para listar deployments recentes e seus status:
pipectl deployment list \
  --address=https://pipecd.internal.corp \
  --api-key="$PIPECTL_API_KEY"
```

## Limites e trade-offs
Avaliar métricas de Deployment Frequency somando deploys de ambientes efêmeros de desenvolvimento (`dev`) junto com deploys de produção (`prod`) distorce os indicadores reais de entrega de valor.

## Como verificar
Padronize labels de ambiente (`env: production`, `env: staging`) nos arquivos `app.pipecd.yaml` para filtrar os Delivery Insights por ambiente produtivo.

## Conexões
- [[pipecd-integracao-ci-pipectl-event-watcher-image-update]] — Veja também: PipeCD: Integração entre Pipelines de CI e PipeCD via pipectl e Event Watcher.

## Fontes
- [PipeCD Official Documentation — Core Concepts (Control Plane, Stateless Piped Agent, Projects, app.pipecd.yaml, Sync Strategies, Platform & Analysis Providers)](https://raw.githubusercontent.com/pipe-cd/pipecd/master/README.md) — Documentação oficial de conceitos do PipeCD detalhando a arquitetura Control Plane + Piped stateless, papéis Viewer/Editor/Admin, Quick Sync vs Pipeline Sync, Platform Providers e Analysis Providers; consultado em 2026-10-03.
- [PipeCD GitHub — README.md (Unified Multi-Platform GitOps CD, Progressive Delivery, Built-in ADA & Delivery Insights)](https://pipecd.dev/docs-v0.58.x/concepts/) — README oficial do pipe-cd/pipecd (CNCF Sandbox) explicando o fluxo GitOps sem exposição de credenciais externas, análise automática de deploy e métricas DORA no Delivery Insights; consultado em 2026-10-03.
- [PipeCD — Official GitHub Repository](https://github.com/pipe-cd/pipecd) — Repositório oficial Apache-2.0 do PipeCD; consultado em 2026-10-03.
