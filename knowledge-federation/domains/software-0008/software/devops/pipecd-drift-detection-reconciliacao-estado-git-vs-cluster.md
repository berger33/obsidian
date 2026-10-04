---
id: software.devops.tranche14.001338
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

# PipeCD: Detecção Contínua de Configuration Drift e Visibilidade da Árvore de Recursos em Tempo Real

## Em uma frase
Os agentes `piped` monitoram continuamente os recursos em execução nos clusters e provedores de plataforma, comparando-os com o estado declarado no commit mais recente do Git para detectar e exibir **Configuration Drift** (desvio de configuração) em tempo real na interface do PipeCD.

## Por que importa
Quando alguém executa um `kubectl edit`, `kubectl scale` ou altera um recurso manualmente no console da nuvem durante um incidente, a mudança manual diverge silenciosamente do repositório Git.

## Como funciona
O `piped` calcula o diff estrutural entre o manifesto renderizado do Git e o estado vivo no cluster, sinaliza a aplicação como `OUT_OF_SYNC` na UI (mostrando exatamente quais linhas divergiram) e permite reconciliar ou acionar notificações para Slack/Webhook.

## Exemplo
```bash
# Verificar no repositorio Git o estado desejado que o piped compara contra o cluster:
git log -n 1 --oneline -- apps/payment-api/
```

## Limites e trade-offs
Ignorar alertas de `OUT_OF_SYNC` por dias faz com que o próximo deploy legítimo via Git sobrescreva abruptamente ajustes manuais emergenciais (como um aumento manual de limite de memória) que nunca foram portados para o Git.

## Como verificar
Toda alteração emergencial feita no cluster deve ser imediatamente refletida em um Pull Request no repositório Git monitorado pelo PipeCD.

## Conexões
- [[pipecd-entrega-progressiva-canary-bluegreen-traffic-routing]] — Veja também: PipeCD: Entrega Progressiva (Canary e Blue/Green) em Kubernetes, Cloud Run e Lambda.
- [[pipecd-integracao-ci-pipectl-event-watcher-image-update]] — Veja também: PipeCD: Integração entre Pipelines de CI e PipeCD via pipectl e Event Watcher.

## Fontes
- [PipeCD Official Documentation — Core Concepts (Control Plane, Stateless Piped Agent, Projects, app.pipecd.yaml, Sync Strategies, Platform & Analysis Providers)](https://raw.githubusercontent.com/pipe-cd/pipecd/master/README.md) — Documentação oficial de conceitos do PipeCD detalhando a arquitetura Control Plane + Piped stateless, papéis Viewer/Editor/Admin, Quick Sync vs Pipeline Sync, Platform Providers e Analysis Providers; consultado em 2026-10-03.
- [PipeCD GitHub — README.md (Unified Multi-Platform GitOps CD, Progressive Delivery, Built-in ADA & Delivery Insights)](https://pipecd.dev/docs-v0.58.x/concepts/) — README oficial do pipe-cd/pipecd (CNCF Sandbox) explicando o fluxo GitOps sem exposição de credenciais externas, análise automática de deploy e métricas DORA no Delivery Insights; consultado em 2026-10-03.
- [PipeCD — Official GitHub Repository](https://github.com/pipe-cd/pipecd) — Repositório oficial Apache-2.0 do PipeCD; consultado em 2026-10-03.
