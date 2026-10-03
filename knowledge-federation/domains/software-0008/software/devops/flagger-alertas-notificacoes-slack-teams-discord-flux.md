---
id: software.devops.tranche07.000667
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

# Flux Flagger: alertas de entregas progressivas para Slack, Microsoft Teams, Discord e Flux Notification API

## Em uma frase
O Flagger emite eventos Kubernetes e notificações em tempo real sobre o andamento, avisos e rollbacks de análises canário para Slack, Microsoft Teams, Discord, Rocket e Google Chat através de `AlertProvider` e `alerts` por Canary.

## Por que importa
Como a promoção ou o rollback automático de um lançamento canário no Flagger ocorre de forma autônoma em segundo plano ao longo de vários minutos, a equipe de desenvolvimento e o engenheiro de plantão precisam ser avisados imediatamente se um deploy falhar nas checagens de métricas P99 ou sofrer rollback automático. De acordo com o README oficial do Flagger, o bloco `spec.analysis.alerts` permite rotear alertas filtrados por severidade (`info`, `warn`, `error`) para diferentes canais de chat.

## Como funciona
O administrador declara objetos `AlertProvider` especificando o tipo de canal (`slack`, `msteams`, `discord`, `rocket`, `gchat`), o endereço do webhook (ou `secretRef` contendo a URL do webhook) e o canal de destino. Em seguida, dentro do recurso `Canary`, a seção `spec.analysis.alerts` vincula diferentes públicos a diferentes níveis de severidade via `providerRef`: por exemplo, enviando apenas erros críticos de rollback (`severity: error`) para o Slack da equipe de desenvolvimento, avisos de falha de métrica individual (`severity: warn`) para o Discord de QA, e todos os eventos informativos de início/sucesso (`severity: info`) para o MS Teams do plantão.

## Exemplo
```yaml
# Configuração de alertas por severidade dentro de um recurso Canary do Flagger
    alerts:
      - name: "dev team Slack"
        severity: error
        providerRef:
          name: dev-slack
          namespace: flagger
      - name: "qa team Discord"
        severity: warn
        providerRef:
          name: qa-discord
      - name: "on-call MS Teams"
        severity: info
        providerRef:
          name: on-call-msteams
```

## Limites e trade-offs
Configurar `severity: info` no canal principal de resposta a incidentes em um cluster com dezenas de deploys diários gera fadiga de alertas (pois cada novo rollout emite mensagens de início, avanço e conclusão); recomenda-se reservar `severity: error` para canais de plantão/incidentes e manter `severity: info` em canais dedicados de log de auditoria de releases.

## Como verificar
Aplique um `AlertProvider` válido vinculado ao recurso `Canary`, dispare uma atualização de imagem no Deployment alvo e confirme o recebimento das notificações no canal configurado e nos eventos do Kubernetes (`kubectl get events`).

## Conexões
- [[flagger-webhooks-testes-carga-conformidade-manual-gating]] — Veja também: Flux Flagger: webhooks de ciclo de vida, geração de tráfego com loadtester, Helm test e manual gating.
- [[flagger-integracao-hpa-autoscaling-primario-canario]] — Veja também: Flux Flagger: coordenação de HorizontalPodAutoscaler (HPA) entre implantações primária e canário.
- [[flagger-entrega-progressiva-kubernetes-flux-cncf]] — Referência cruzada direta com flagger-entrega-progressiva-kubernetes-flux-cncf.
- [[flagger-crd-canary-ciclo-vida-promocao-configmaps-secrets]] — Referência cruzada direta com flagger-crd-canary-ciclo-vida-promocao-configmaps-secrets.

## Fontes
- [Flux Flagger GitHub — README.md (Canary CRD, Service Mesh/Ingress/Gateway API, Metrics & Webhooks)](https://raw.githubusercontent.com/fluxcd/flagger/main/README.md) — README oficial do Flux Flagger cobrindo a especificação do CRD Canary, estratégias Canary/A/B/Blue-Green, matriz de provedores de rede, MetricTemplates, webhooks e alertas; consultado em 2026-10-03.
- [Flux Flagger Official Documentation — How it works & Canary Promotion Lifecycle](https://docs.flagger.app/main/usage/how-it-works) — Documentação oficial de funcionamento da máquina de estados de análise e promoção canário do Flagger; consultado em 2026-10-03.
- [Flux Flagger — Official GitHub Repository](https://github.com/fluxcd/flagger) — Repositório oficial Apache-2.0 do Flagger na família GitOps Flux (CNCF Graduated); consultado em 2026-10-03.
