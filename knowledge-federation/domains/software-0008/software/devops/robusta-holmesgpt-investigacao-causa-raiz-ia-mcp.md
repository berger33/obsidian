---
id: software.devops.tranche12.001167
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
fontes: ["https://raw.githubusercontent.com/robusta-dev/robusta/master/README.md", "https://docs.robusta.dev/master/index.html", "https://github.com/robusta-dev/holmesgpt"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Robusta: Investigação Automática de Causa Raiz com HolmesGPT e Fontes de Dados Externas

## Em uma frase
O Robusta integra-se nativamente ao **HolmesGPT** (`robusta-dev/holmesgpt`), um agente SRE open-source que investiga automaticamente alertas consultando logs, eventos Kubernetes, métricas Prometheus, traces, ferramentas de ITSM e servidores MCP para sintetizar a causa raiz do incidente.

## Por que importa
Em incidentes complexos que atravessam múltiplos serviços, correlacionar manualmente métricas Prometheus, eventos de nós, logs de pods e mudanças recentes leva dezenas de minutos durante os quais o serviço permanece degradado.

## Como funciona
Quando um alerta dispara (ou quando um engenheiro menciona o bot no Slack/Teams sob demanda), o HolmesGPT executa chamadas somente leitura às ferramentas autorizadas do cluster e de observabilidade para reunir evidências concretas e anexar uma análise fundamentada junto ao alerta enriquecido do Robusta.

## Exemplo
```bash
# Verificar se o componente HolmesGPT esta ativo junto ao Robusta:
kubectl get pods -A | grep -E "robusta|holmes"
```

## Limites e trade-offs
Enviar logs e payloads de alertas de produção para provedores de LLM externos sem filtrar dados pessoais (PII) ou segredos acidentalmente impressos nos logs de aplicação pode violar políticas de conformidade e privacidade.

## Como verificar
Configure políticas de sanitização de logs, utilize endpoints de modelo homologados pela segurança corporativa e mantenha as permissões do agente estritamente em modo somente leitura.

## Conexões
- [[robusta-change-tracking-correlacao-rollouts-config-alertas]] — Veja também: Robusta: Change-Tracking de Recursos Kubernetes para Correlação entre Deploys e Incidentes.
- [[robusta-krr-kubernetes-resource-recommender-otimizacao-custos]] — Veja também: Robusta: Integração com KRR (Kubernetes Resource Recommender) para Otimização de CPU e Memória.

## Fontes
- [Robusta GitHub — README.md (Prometheus Alert Enrichment, Smart Grouping, Playbooks, Change-Tracking, KRR & Sinks Matrix)](https://raw.githubusercontent.com/robusta-dev/robusta/master/README.md) — README oficial do robusta-dev/robusta detalhando enriquecimento de alertas Prometheus, Smart Grouping em threads, detecção sem PromQL, Change-Tracking, auto-remediação, KRR e matriz de integrações/sinks; consultado em 2026-10-03.
- [Robusta Official Documentation — Overview & HolmesGPT AI Root Cause Analysis](https://docs.robusta.dev/master/index.html) — Documentação oficial do Robusta e integração com HolmesGPT para investigação automática de causa raiz em alertas Kubernetes; consultado em 2026-10-03.
- [Robusta — Official GitHub Repository](https://github.com/robusta-dev/holmesgpt) — Repositório oficial do Robusta; consultado em 2026-10-03.
