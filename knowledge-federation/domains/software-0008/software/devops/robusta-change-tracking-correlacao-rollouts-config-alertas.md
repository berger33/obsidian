---
id: software.devops.tranche12.001166
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-12.md"
fontes: ["https://raw.githubusercontent.com/robusta-dev/robusta/master/README.md", "https://docs.robusta.dev/master/index.html", "https://github.com/robusta-dev/robusta"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Robusta: Change-Tracking de Recursos Kubernetes para Correlação entre Deploys e Incidentes

## Em uma frase
O recurso de Change-Tracking do Robusta monitora alterações auditáveis em recursos do Kubernetes (como `Deployments`, `DaemonSets`, `StatefulSets` e `ConfigMaps`), registrando diffs do que mudou no cluster para correlacionar imediatamente picos de alertas com rollouts recentes.

## Por que importa
A maioria dos incidentes em produção ocorre minutos após uma mudança de imagem, variável de ambiente ou limite de recursos, mas equipes diferentes muitas vezes não sabem que um deploy acabou de acontecer quando o alerta dispara.

## Como funciona
O Robusta detecta atualizações na especificação dos workloads, calcula o diff exato dos campos alterados (como tag de imagem antiga vs. nova) e publica eventos de mudança nos sinks configurados ou na timeline de investigação, permitindo correlacionar o início do alerta com o rollout exato.

## Exemplo
```bash
# Inspecionar logs de eventos de mudanca processados pelo runner:
kubectl logs deployment/robusta-runner -c runner | grep -i "change"
```

## Limites e trade-offs
Rastrear mudanças em recursos que sofrem atualizações constantes de anotações por controladores internos sem filtrar campos ruidosos gera excesso de eventos de mudança irrelevantes.

## Como verificar
Configure os filtros de Change-Tracking para focar em mudanças significativas de especificação de workloads (`spec.template`) e correlacione os eventos com as janelas de alerta.

## Conexões
- [[robusta-auto-remediacao-self-healing-playbooks-seguranca]] — Veja também: Robusta: Auto-Remediação (Self-Healing) e Ações Interativas sobre Alertas Kubernetes.
- [[robusta-holmesgpt-investigacao-causa-raiz-ia-mcp]] — Veja também: Robusta: Investigação Automática de Causa Raiz com HolmesGPT e Fontes de Dados Externas.

## Fontes
- [Robusta GitHub — README.md (Prometheus Alert Enrichment, Smart Grouping, Playbooks, Change-Tracking, KRR & Sinks Matrix)](https://raw.githubusercontent.com/robusta-dev/robusta/master/README.md) — README oficial do robusta-dev/robusta detalhando enriquecimento de alertas Prometheus, Smart Grouping em threads, detecção sem PromQL, Change-Tracking, auto-remediação, KRR e matriz de integrações/sinks; consultado em 2026-10-03.
- [Robusta Official Documentation — Overview & HolmesGPT AI Root Cause Analysis](https://docs.robusta.dev/master/index.html) — Documentação oficial do Robusta e integração com HolmesGPT para investigação automática de causa raiz em alertas Kubernetes; consultado em 2026-10-03.
- [Robusta — Official GitHub Repository](https://github.com/robusta-dev/robusta) — Repositório oficial do Robusta; consultado em 2026-10-03.
