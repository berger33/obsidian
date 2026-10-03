---
id: software.devops.tranche14.001337
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

# PipeCD: Entrega Progressiva (Canary e Blue/Green) em Kubernetes, Cloud Run e Lambda

## Em uma frase
O PipeCD implementa pipelines declarativos de **Canary** e **Blue/Green** com divisão percentual de tráfego tanto em Kubernetes (via Services nativos, Istio, SMI ou Ingress) quanto em plataformas serverless gerenciadas como **GCP Cloud Run** e **AWS Lambda**.

## Por que importa
Executar Blue/Green ou Canary em Cloud Run ou Lambda manualmente requer calcular pesos de revisões/aliases e reverter rotas manualmente caso a nova revisão apresente erros.

## Como funciona
No `app.pipecd.yaml`, combinam-se estágios de rollout de variante (`K8S_CANARY_ROLLOUT` ou `CLOUDRUN_PROMOTE`) com estágios de roteamento percentual de tráfego (`K8S_TRAFFIC_ROUTING`), espera (`WAIT`), aprovação humana (`WAIT_APPROVAL`) e limpeza automática da variante canário.

## Exemplo
```yaml
apiVersion: pipecd.dev/v1beta1
kind: CloudRunApp
spec:
  name: checkout-serverless
  pipeline:
    stages:
      - name: CLOUDRUN_PROMOTE
        with:
          percentage: 20
      - name: WAIT
        with:
          duration: 5m
      - name: CLOUDRUN_PROMOTE
        with:
          percentage: 100
```

## Limites e trade-offs
Usar `K8S_TRAFFIC_ROUTING` baseado em Service nativo do Kubernetes esperando controle percentual exato de 1% quando o Deployment tem apenas 2 réplicas não tem granularidade de Pods suficiente (sem um service mesh/Ingress L7).

## Como verificar
Para controle fino de porcentagem de tráfego com poucas réplicas no Kubernetes, utilize o roteamento de tráfego do PipeCD integrado ao Istio ou Ingress.

## Conexões
- [[pipecd-projects-rbac-roles-viewer-editor-admin-multitenancy]] — Veja também: PipeCD: Governança Multi-Tenant com Projects e Papéis RBAC (Viewer, Editor e Admin).
- [[pipecd-drift-detection-reconciliacao-estado-git-vs-cluster]] — Veja também: PipeCD: Detecção Contínua de Configuration Drift e Visibilidade da Árvore de Recursos em Tempo Real.

## Fontes
- [PipeCD Official Documentation — Core Concepts (Control Plane, Stateless Piped Agent, Projects, app.pipecd.yaml, Sync Strategies, Platform & Analysis Providers)](https://raw.githubusercontent.com/pipe-cd/pipecd/master/README.md) — Documentação oficial de conceitos do PipeCD detalhando a arquitetura Control Plane + Piped stateless, papéis Viewer/Editor/Admin, Quick Sync vs Pipeline Sync, Platform Providers e Analysis Providers; consultado em 2026-10-03.
- [PipeCD GitHub — README.md (Unified Multi-Platform GitOps CD, Progressive Delivery, Built-in ADA & Delivery Insights)](https://pipecd.dev/docs-v0.58.x/concepts/) — README oficial do pipe-cd/pipecd (CNCF Sandbox) explicando o fluxo GitOps sem exposição de credenciais externas, análise automática de deploy e métricas DORA no Delivery Insights; consultado em 2026-10-03.
- [PipeCD — Official GitHub Repository](https://github.com/pipe-cd/pipecd) — Repositório oficial Apache-2.0 do PipeCD; consultado em 2026-10-03.
