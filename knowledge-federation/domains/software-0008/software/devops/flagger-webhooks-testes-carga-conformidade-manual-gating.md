---
id: software.devops.tranche07.000666
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-07.md"
fontes: ["https://raw.githubusercontent.com/fluxcd/flagger/main/README.md", "https://docs.flagger.app/main/usage/how-it-works", "https://github.com/fluxcd/flagger"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Flux Flagger: webhooks de ciclo de vida, geração de tráfego com loadtester, Helm test e manual gating

## Em uma frase
O Flagger suporta webhooks HTTP em múltiplas fases do lançamento (`pre-rollout`, `rollout`, `confirm-rollout`, `post-rollout`, `rollback`) para executar testes de conformidade (Helm/ smoke tests), testes de carga (`flagger-loadtester`) e aprovação manual (manual gating).

## Por que importa
Em ambientes de baixa movimentação noturna ou clusters de staging, não há tráfego orgânico suficiente para gerar métricas estatisticamente válidas no Prometheus durante a janela canário; além disso, equipes críticas frequentemente exigem rodar uma suíte de testes de aceitação antes de abrir tráfego ou exigir aprovação humana (gate manual) antes da promoção. O README oficial do Flagger demonstra como os `webhooks` resolvem esses cenários.

## Como funciona
Na lista `spec.analysis.webhooks`, o Flagger faz chamadas HTTP POST para serviços externos ou para o componente oficial `flagger-loadtester` / `flagger-helmtester` em momentos específicos da máquina de estados: (1) webhooks `pre-rollout` executam testes de conformidade ou smoke tests (como `helm test run podinfo -n test`) contra a instância canário antes de rotear qualquer tráfego real; (2) webhooks `rollout` geram tráfego sintético contínuo durante a análise (por exemplo, executando `hey -z 1m -q 10 -c 2` via `flagger-loadtester`) para alimentar as métricas L7; e (3) webhooks de gating manual permitem pausar, aprovar ou retomar (`approve/pause/resume`) a promoção do rollout.

## Exemplo
```yaml
# Configuração de webhooks de conformidade (pre-rollout com helmv3) e teste de carga (rollout com hey) no Flagger
    webhooks:
      - name: "conformance test"
        type: pre-rollout
        url: http://flagger-helmtester.test/
        timeout: 5m
        metadata:
          type: "helmv3"
          cmd: "test run podinfo -n test"
      - name: "load test"
        type: rollout
        url: http://flagger-loadtester.test/
        metadata:
          cmd: "hey -z 1m -q 10 -c 2 http://podinfo.test:9898/"
```

## Limites e trade-offs
O serviço `flagger-loadtester` executa comandos arbitrários passados no campo `metadata.cmd` do webhook (como utilitários `hey`, `curl`, `grpc_health_probe` ou `helm`); portanto, em clusters compartilhados, o pod do `flagger-loadtester` deve ter uma `ServiceAccount` com RBAC estritamente mínimo e ser isolado por `NetworkPolicy` para evitar que usuários mal-intencionados abusem da execução de comandos via manifesto `Canary`.

## Como verificar
Verifique os logs do pod `flagger-loadtester` (`kubectl logs deploy/flagger-loadtester -n test`) durante uma análise canário ativa para confirmar o recebimento do payload do webhook e a execução bem-sucedida dos comandos `pre-rollout` e `rollout`.

## Conexões
- [[flagger-analise-metricas-prometheus-metrictemplate-kpis]] — Veja também: Flux Flagger: validação de KPIs com verificações nativas e MetricTemplates customizados no Prometheus.
- [[flagger-alertas-notificacoes-slack-teams-discord-flux]] — Veja também: Flux Flagger: alertas de entregas progressivas para Slack, Microsoft Teams, Discord e Flux Notification API.
- [[flagger-entrega-progressiva-kubernetes-flux-cncf]] — Referência cruzada direta com flagger-entrega-progressiva-kubernetes-flux-cncf.

## Fontes
- [Flux Flagger GitHub — README.md (Canary CRD, Service Mesh/Ingress/Gateway API, Metrics & Webhooks)](https://raw.githubusercontent.com/fluxcd/flagger/main/README.md) — README oficial do Flux Flagger cobrindo a especificação do CRD Canary, estratégias Canary/A/B/Blue-Green, matriz de provedores de rede, MetricTemplates, webhooks e alertas; consultado em 2026-10-03.
- [Flux Flagger Official Documentation — How it works & Canary Promotion Lifecycle](https://docs.flagger.app/main/usage/how-it-works) — Documentação oficial de funcionamento da máquina de estados de análise e promoção canário do Flagger; consultado em 2026-10-03.
- [Flux Flagger — Official GitHub Repository](https://github.com/fluxcd/flagger) — Repositório oficial Apache-2.0 do Flagger na família GitOps Flux (CNCF Graduated); consultado em 2026-10-03.
