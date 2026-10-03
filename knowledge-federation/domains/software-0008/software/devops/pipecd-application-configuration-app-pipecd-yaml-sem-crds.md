---
id: software.devops.tranche14.001332
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

# PipeCD: Contrato Declarativo app.pipecd.yaml sem Alteração de Manifestos ou CRDs no Cluster

## Em uma frase
No PipeCD, cada aplicação reside em um **Application Directory** dentro do repositório Git contendo seus manifestos nativos intactos e um único arquivo declarativo de configuração de pipeline chamado por padrão `app.pipecd.yaml`.

## Por que importa
Muitos controladores de entrega progressiva exigem substituir o recurso nativo `kind: Deployment` do Kubernetes por uma CRD proprietária (como `Rollout`) ou instalar dezenas de CRDs no cluster.

## Como funciona
O PipeCD trabalha diretamente com os manifestos padrão do Kubernetes (YAML puro, Helm ou Kustomize), módulos Terraform ou definições Cloud Run/ECS: o arquivo `app.pipecd.yaml` define apenas o tipo (`kind: KubernetesApp`, `TerraformApp`, etc.), os estágios do pipeline (`stages`) e os gatilhos de sincronização.

## Exemplo
```yaml
apiVersion: pipecd.dev/v1beta1
kind: KubernetesApp
spec:
  name: payment-api
  labels:
    env: production
  pipeline:
    stages:
      - name: K8S_CANARY_ROLLOUT
        with:
          replicas: 10%
      - name: K8S_PRIMARY_ROLLOUT
      - name: K8S_CANARY_CLEAN
```

## Limites e trade-offs
Colocar múltiplas aplicações independentes misturadas na mesma pasta do Git sem separar um **Application Directory** por aplicação causa conflito na detecção de alterações por commit.

## Como verificar
Mantenha exatamente um diretório Git por aplicação contendo seu próprio `app.pipecd.yaml` e seus respectivos manifestos.

## Conexões
- [[pipecd-arquitetura-control-plane-piped-stateless-gitops]] — Veja também: PipeCD: Arquitetura GitOps Unificada com Control Plane Central e Agentes Piped Stateless.
- [[pipecd-sync-strategies-quick-sync-pipeline-sync-auto]] — Veja também: PipeCD: Estratégias de Sincronização (Quick Sync, Pipeline Sync e Auto Sync).

## Fontes
- [PipeCD Official Documentation — Core Concepts (Control Plane, Stateless Piped Agent, Projects, app.pipecd.yaml, Sync Strategies, Platform & Analysis Providers)](https://pipecd.dev/docs-v0.58.x/concepts/) — Documentação oficial de conceitos do PipeCD detalhando a arquitetura Control Plane + Piped stateless, papéis Viewer/Editor/Admin, Quick Sync vs Pipeline Sync, Platform Providers e Analysis Providers; consultado em 2026-10-03.
- [PipeCD GitHub — README.md (Unified Multi-Platform GitOps CD, Progressive Delivery, Built-in ADA & Delivery Insights)](https://raw.githubusercontent.com/pipe-cd/pipecd/master/README.md) — README oficial do pipe-cd/pipecd (CNCF Sandbox) explicando o fluxo GitOps sem exposição de credenciais externas, análise automática de deploy e métricas DORA no Delivery Insights; consultado em 2026-10-03.
- [PipeCD — Official GitHub Repository](https://github.com/pipe-cd/pipecd) — Repositório oficial Apache-2.0 do PipeCD; consultado em 2026-10-03.
