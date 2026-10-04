---
id: software.devops.tranche14.001336
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

# PipeCD: Governança Multi-Tenant com Projects e Papéis RBAC (Viewer, Editor e Admin)

## Em uma frase
No Control Plane do PipeCD, as aplicações e agentes `piped` são organizados logicamente em **Projects**, cada qual com controle de acesso baseado em três papéis predefinidos mapeados a equipes do GitHub/SSO: **`Viewer`**, **`Editor`** e **`Admin`**.

## Por que importa
Em empresas com dezenas de squads e múltiplos clusters de nuvem, misturar todos os agentes `piped` sem isolamento por projeto permitiria que uma equipe disparasse ou cancelasse deploys de outra unidade de negócios.

## Como funciona
O papel **`Viewer`** possui permissão estritamente de leitura para visualizar a lista e os detalhes de aplicações e deployments; o **`Editor`** adiciona permissões operacionais para acionar sincronizações manuais, aprovar estágios `WAIT_APPROVAL` e cancelar deployments; e o **`Admin`** gerencia as configurações do Project, chaves de API e registro de agentes `piped`.

## Exemplo
```yaml
# Estrutura logica de permissoes de um Project no Control Plane do PipeCD:
# Viewer -> leitura de Applications, Deployments e Delivery Insights
# Editor -> Viewer + trigger/cancel/approve deployments
# Admin  -> Editor + gerenciar chaves de Piped, SSO teams e Project settings
```

## Limites e trade-offs
Mapear todos os desenvolvedores da organização diretamente ao grupo `Admin` do Project permite que qualquer usuário desative agentes `piped` ou altere provedores de plataforma.

## Como verificar
Conceda `Editor` para os engenheiros da squad responsável pelas aplicações do Project, `Viewer` para equipes transversais/auditoria e `Admin` apenas para a engenharia de plataforma.

## Conexões
- [[pipecd-automated-deployment-analysis-ada-prometheus-datadog-rollback]] — Veja também: PipeCD: Análise Automatizada de Deploy (ADA) com Analysis Providers e Auto-Rollback.
- [[pipecd-entrega-progressiva-canary-bluegreen-traffic-routing]] — Veja também: PipeCD: Entrega Progressiva (Canary e Blue/Green) em Kubernetes, Cloud Run e Lambda.

## Fontes
- [PipeCD Official Documentation — Core Concepts (Control Plane, Stateless Piped Agent, Projects, app.pipecd.yaml, Sync Strategies, Platform & Analysis Providers)](https://pipecd.dev/docs-v0.58.x/concepts/) — Documentação oficial de conceitos do PipeCD detalhando a arquitetura Control Plane + Piped stateless, papéis Viewer/Editor/Admin, Quick Sync vs Pipeline Sync, Platform Providers e Analysis Providers; consultado em 2026-10-03.
- [PipeCD GitHub — README.md (Unified Multi-Platform GitOps CD, Progressive Delivery, Built-in ADA & Delivery Insights)](https://raw.githubusercontent.com/pipe-cd/pipecd/master/README.md) — README oficial do pipe-cd/pipecd (CNCF Sandbox) explicando o fluxo GitOps sem exposição de credenciais externas, análise automática de deploy e métricas DORA no Delivery Insights; consultado em 2026-10-03.
- [PipeCD — Official GitHub Repository](https://github.com/pipe-cd/pipecd) — Repositório oficial Apache-2.0 do PipeCD; consultado em 2026-10-03.
