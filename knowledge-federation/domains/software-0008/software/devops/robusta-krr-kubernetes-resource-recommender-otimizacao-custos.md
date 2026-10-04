---
id: software.devops.tranche12.001168
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

# Robusta: Integração com KRR (Kubernetes Resource Recommender) para Otimização de CPU e Memória

## Em uma frase
O ecossistema Robusta inclui integração direta com o **KRR (Kubernetes Resource Recommender)**, uma ferramenta baseada em métricas históricas do Prometheus que calcula recomendações de `requests` e `limits` de CPU e memória para reduzir custos de nuvem e evitar OOMKills ou CPU throttling.

## Por que importa
Enquanto ferramentas baseadas apenas em VPA olham o estado local do cluster, o KRR consulta diretamente séries temporais do Prometheus, VictoriaMetrics ou Thanos (incluindo Managed Prometheus da AWS, GCP e Azure) para gerar relatórios sob demanda ou agendados.

## Como funciona
Executado via CLI ou integrado ao Robusta no cluster, o KRR analisa os percentis de consumo de CPU e o pico de memória de cada container ao longo de dias ou semanas e produz recomendações acionáveis que podem ser enviadas aos canais das equipes.

## Exemplo
```bash
# Verificar conectividade do Robusta com o Prometheus do cluster:
kubectl exec -it deployment/robusta-runner -c runner -- env | grep -i prometheus
```

## Limites e trade-offs
Aplicar recomendações de redução agressiva de memória baseadas em uma janela curta de métricas do Prometheus (como 24 horas) que não capturou o pico semanal ou mensal de processamento em lote causa `OOMKilled` no próximo pico de carga.

## Como verificar
Configure janelas históricas de pelo menos 7 a 14 dias no Prometheus ao avaliar recomendações do KRR e preserve margem de segurança para cargas sensíveis.

## Conexões
- [[robusta-holmesgpt-investigacao-causa-raiz-ia-mcp]] — Veja também: Robusta: Investigação Automática de Causa Raiz com HolmesGPT e Fontes de Dados Externas.
- [[robusta-integracao-prometheus-gerenciado-amp-gmp-azure-victoriametrics]] — Veja também: Robusta: Integração com kube-prometheus-stack, VictoriaMetrics, Thanos e Managed Prometheus (AWS, GCP, Azure).

## Fontes
- [Robusta GitHub — README.md (Prometheus Alert Enrichment, Smart Grouping, Playbooks, Change-Tracking, KRR & Sinks Matrix)](https://raw.githubusercontent.com/robusta-dev/robusta/master/README.md) — README oficial do robusta-dev/robusta detalhando enriquecimento de alertas Prometheus, Smart Grouping em threads, detecção sem PromQL, Change-Tracking, auto-remediação, KRR e matriz de integrações/sinks; consultado em 2026-10-03.
- [Robusta Official Documentation — Overview & HolmesGPT AI Root Cause Analysis](https://docs.robusta.dev/master/index.html) — Documentação oficial do Robusta e integração com HolmesGPT para investigação automática de causa raiz em alertas Kubernetes; consultado em 2026-10-03.
- [Robusta — Official GitHub Repository](https://github.com/robusta-dev/robusta) — Repositório oficial do Robusta; consultado em 2026-10-03.
