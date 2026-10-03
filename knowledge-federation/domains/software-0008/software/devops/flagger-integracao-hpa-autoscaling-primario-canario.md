---
id: software.devops.tranche07.000668
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

# Flux Flagger: coordenação de HorizontalPodAutoscaler (HPA) entre implantações primária e canário

## Em uma frase
Por meio do campo `spec.autoscalerRef`, o Flagger gerencia um `HorizontalPodAutoscaler` espelhado (`<nome>-primary`) para que a implantação primária e a canário escalem horizontalmente de forma independente e segura durante e após rollouts.

## Por que importa
Se um `HorizontalPodAutoscaler` (HPA) apontar apenas para o `Deployment` original enquanto o Flagger transfere 100% do tráfego de produção para o deployment gerenciado `<nome>-primary`, a aplicação em produção ficará sem autoscaling e cairá sob picos de carga. Segundo o README oficial do Flagger (`Canary CRD`), referenciar o HPA em `spec.autoscalerRef` instrui o Flagger a sincronizar automaticamente o escalonador horizontal entre o canário e o primário.

## Como funciona
Quando `spec.autoscalerRef` aponta para um `HorizontalPodAutoscaler` (`autoscaling/v2`), o Flagger cria na inicialização um HPA correspondente chamado `<nome>-primary` apontando para o deployment `<nome>-primary`. Durante o estado estacionário, o HPA primário escala os pods de produção normalmente com base no tráfego, enquanto o Deployment canário permanece com zero réplicas e seu HPA original fica inativo/pausado. Quando uma análise canário se inicia, o Flagger ativa o escalonamento do canário e, ao promover uma nova versão (incluindo eventuais alterações de `minReplicas`, `maxReplicas` ou métricas no HPA original), sincroniza a especificação atualizada do HPA para o `<nome>-primary`.

## Exemplo
```yaml
# Referência ao HorizontalPodAutoscaler v2 dentro do recurso Canary do Flagger
spec:
  targetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: podinfo
  autoscalerRef:
    apiVersion: autoscaling/v2
    kind: HorizontalPodAutoscaler
    name: podinfo
```

## Limites e trade-offs
Para que o Flagger não entre em conflito com ferramentas de GitOps (como Flux ou Argo CD) que tentam reconciliar o `replicas` do Deployment original para um número fixo (como `replicas: 3`) enquanto o Flagger o mantém em `0`, o manifesto do Deployment no Git deve omitir o campo `spec.replicas` quando gerenciado em conjunto com um HPA e o Flagger.

## Como verificar
Execute `kubectl get hpa -n test` após inicializar o `Canary` e confirme a existência tanto do HPA original `podinfo` quanto do HPA gerenciado `podinfo-primary` apontando para `Deployment/podinfo-primary`.

## Conexões
- [[flagger-alertas-notificacoes-slack-teams-discord-flux]] — Veja também: Flux Flagger: alertas de entregas progressivas para Slack, Microsoft Teams, Discord e Flux Notification API.
- [[flagger-configuracao-servico-port-discovery-timeouts-rewrites]] — Veja também: Flux Flagger: configuração de serviços ClusterIP, portDiscovery, timeouts e regras HTTP no Canary.
- [[flagger-entrega-progressiva-kubernetes-flux-cncf]] — Referência cruzada direta com flagger-entrega-progressiva-kubernetes-flux-cncf.
- [[flagger-crd-canary-ciclo-vida-promocao-configmaps-secrets]] — Referência cruzada direta com flagger-crd-canary-ciclo-vida-promocao-configmaps-secrets.

## Fontes
- [Flux Flagger GitHub — README.md (Canary CRD, Service Mesh/Ingress/Gateway API, Metrics & Webhooks)](https://raw.githubusercontent.com/fluxcd/flagger/main/README.md) — README oficial do Flux Flagger cobrindo a especificação do CRD Canary, estratégias Canary/A/B/Blue-Green, matriz de provedores de rede, MetricTemplates, webhooks e alertas; consultado em 2026-10-03.
- [Flux Flagger Official Documentation — How it works & Canary Promotion Lifecycle](https://docs.flagger.app/main/usage/how-it-works) — Documentação oficial de funcionamento da máquina de estados de análise e promoção canário do Flagger; consultado em 2026-10-03.
- [Flux Flagger — Official GitHub Repository](https://github.com/fluxcd/flagger) — Repositório oficial Apache-2.0 do Flagger na família GitOps Flux (CNCF Graduated); consultado em 2026-10-03.
