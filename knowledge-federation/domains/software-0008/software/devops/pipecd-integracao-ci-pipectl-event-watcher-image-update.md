---
id: software.devops.tranche14.001339
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

# PipeCD: Integração entre Pipelines de CI e PipeCD via pipectl e Event Watcher

## Em uma frase
O PipeCD separa claramente as responsabilidades de **CI** (testar código e construir/publicar o artefato OCI) e **CD** (implantar o artefato via GitOps), integrando os dois mundos através da CLI **`pipectl`** e do mecanismo de **Event Watcher**.

## Por que importa
Dar permissão de escrita irrestrita (SSH key ou Personal Access Token) em dezenas de pipelines de CI apenas para que o job de build faça `git commit` e `git push` da nova tag de imagem no repositório de manifestos cria conflitos de `git push` concorrentes.

## Como funciona
Em vez de o runner de CI fazer `git push` diretamente, o job de CI executa `pipectl event register` emitindo um evento com a nova tag/digest da imagem para o Control Plane do PipeCD; o `piped` (com Event Watcher configurado) detecta o evento, atualiza automaticamente o manifesto no repositório Git de forma serializada e dispara o pipeline de deploy.

## Exemplo
```bash
pipectl event register \
  --address=https://pipecd.internal.corp \
  --api-key="$PIPECTL_API_KEY" \
  --name=image-pushed \
  --data="ghcr.io/org/payment-api:v1.9.2" \
  --labels="app=payment-api,env=staging"
```

## Limites e trade-offs
Usar uma chave de API (`--api-key`) com permissão de leitura/escrita total no Control Plane dentro do pipeline de CI viola o princípio do menor privilégio.

## Como verificar
Gere uma API Key no PipeCD com papel restrito exclusivamente para registro de eventos (`EVENT_REGISTRAR`) para uso pelo `pipectl` nos runners de CI.

## Conexões
- [[pipecd-drift-detection-reconciliacao-estado-git-vs-cluster]] — Veja também: PipeCD: Detecção Contínua de Configuration Drift e Visibilidade da Árvore de Recursos em Tempo Real.
- [[pipecd-delivery-insights-metricas-dora-lead-time-mttr-cfr]] — Veja também: PipeCD: Delivery Insights e Medição Nativa de Métricas DORA (Deployment Frequency, Lead Time, MTTR e CFR).

## Fontes
- [PipeCD Official Documentation — Core Concepts (Control Plane, Stateless Piped Agent, Projects, app.pipecd.yaml, Sync Strategies, Platform & Analysis Providers)](https://raw.githubusercontent.com/pipe-cd/pipecd/master/README.md) — Documentação oficial de conceitos do PipeCD detalhando a arquitetura Control Plane + Piped stateless, papéis Viewer/Editor/Admin, Quick Sync vs Pipeline Sync, Platform Providers e Analysis Providers; consultado em 2026-10-03.
- [PipeCD GitHub — README.md (Unified Multi-Platform GitOps CD, Progressive Delivery, Built-in ADA & Delivery Insights)](https://pipecd.dev/docs-v0.58.x/concepts/) — README oficial do pipe-cd/pipecd (CNCF Sandbox) explicando o fluxo GitOps sem exposição de credenciais externas, análise automática de deploy e métricas DORA no Delivery Insights; consultado em 2026-10-03.
- [PipeCD — Official GitHub Repository](https://github.com/pipe-cd/pipecd) — Repositório oficial Apache-2.0 do PipeCD; consultado em 2026-10-03.
