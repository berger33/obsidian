---
id: software.devops.tranche14.001335
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

# PipeCD: Análise Automatizada de Deploy (ADA) com Analysis Providers e Auto-Rollback

## Em uma frase
O PipeCD inclui **Automated Deployment Analysis (ADA)** diretamente como um estágio (`ANALYSIS`) do pipeline de deploy, consultando **Analysis Providers** externos como **Prometheus**, **Datadog**, **Google Cloud Monitoring (Stackdriver)** e **AWS CloudWatch**, além de logs e requisições HTTP.

## Por que importa
Fazer rollout canário de 10% do tráfego usando apenas uma pausa fixa (`WAIT`) sem avaliar automaticamente a taxa de erro 5xx ou a latência p99 exige que um engenheiro fique olhando gráficos manualmente durante cada deploy.

## Como funciona
No estágio `ANALYSIS` do `app.pipecd.yaml`, declara-se a query de métricas (por exemplo, PromQL no Prometheus) e o limiar esperado; se a métrica violar o limiar durante a janela de observação do canário, o `piped` aborta o pipeline imediatamente e executa o **auto-rollback** automático para o estado anterior estável.

## Exemplo
```yaml
pipeline:
  stages:
    - name: K8S_CANARY_ROLLOUT
      with:
        replicas: 10%
    - name: ANALYSIS
      with:
        duration: 10m
        metrics:
          - provider: prometheus-prod
            query: 'sum(rate(http_requests_total{status=~"5.."}[1m])) < 0.01'
            expected:
              max: 0.01
            interval: 1m
```

## Limites e trade-offs
Configurar uma janela `duration` curta demais (como `30s`) no estágio `ANALYSIS` quando o intervalo de scrape do Prometheus é de `30s` ou `60s` avalia pontos de dados insuficientes e deixa regressões passarem.

## Como verificar
Defina `duration` de pelo menos 5 a 10 minutos no estágio `ANALYSIS` para capturar múltiplos ciclos de coleta sob tráfego real.

## Conexões
- [[pipecd-platform-providers-kubernetes-terraform-ecs-cloudrun-lambda]] — Veja também: PipeCD: Platform Providers Multi-Cloud (Kubernetes, Terraform, AWS ECS, GCP Cloud Run e Lambda).
- [[pipecd-projects-rbac-roles-viewer-editor-admin-multitenancy]] — Veja também: PipeCD: Governança Multi-Tenant com Projects e Papéis RBAC (Viewer, Editor e Admin).

## Fontes
- [PipeCD Official Documentation — Core Concepts (Control Plane, Stateless Piped Agent, Projects, app.pipecd.yaml, Sync Strategies, Platform & Analysis Providers)](https://pipecd.dev/docs-v0.58.x/concepts/) — Documentação oficial de conceitos do PipeCD detalhando a arquitetura Control Plane + Piped stateless, papéis Viewer/Editor/Admin, Quick Sync vs Pipeline Sync, Platform Providers e Analysis Providers; consultado em 2026-10-03.
- [PipeCD GitHub — README.md (Unified Multi-Platform GitOps CD, Progressive Delivery, Built-in ADA & Delivery Insights)](https://raw.githubusercontent.com/pipe-cd/pipecd/master/README.md) — README oficial do pipe-cd/pipecd (CNCF Sandbox) explicando o fluxo GitOps sem exposição de credenciais externas, análise automática de deploy e métricas DORA no Delivery Insights; consultado em 2026-10-03.
- [PipeCD — Official GitHub Repository](https://github.com/pipe-cd/pipecd) — Repositório oficial Apache-2.0 do PipeCD; consultado em 2026-10-03.
