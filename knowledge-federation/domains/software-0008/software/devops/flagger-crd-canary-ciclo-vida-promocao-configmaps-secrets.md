---
id: software.devops.tranche07.000662
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

# Flux Flagger: anatomia do CRD Canary, sincronização de ConfigMaps/Secrets e máquina de estados

## Em uma frase
O recurso customizado `Canary` (`flagger.app/v1beta1`) define o `targetRef`, `autoscalerRef`, configuração de `service` e regras de `analysis` (`interval`, `threshold`, `maxWeight`, `stepWeight`), monitorando inclusive mudanças em `ConfigMaps` e `Secrets`.

## Por que importa
Muitos incidentes graves em produção não decorrem de uma nova imagem de container, mas sim de uma alteração incorreta em um `ConfigMap` ou `Secret` que é aplicada imediatamente a todos os pods existentes. De acordo com o README oficial do Flagger (`Canary CRD`), o operador rastreia todos os `ConfigMaps` e `Secrets` referenciados pelo Deployment e dispara automaticamente uma análise canário controlada quando qualquer um deles muda, promovendo código e configuração de forma atômica.

## Como funciona
Ao criar o objeto `Canary`, o Flagger clona o Deployment em `targetRef` para `<nome>-primary` (assim como clonagens `-primary` dos `ConfigMaps` e `Secrets` montados) e escala o Deployment original para zero. Quando uma nova versão de imagem, `ConfigMap` ou `Secret` é detectada no alvo, o Flagger escala a implantação canário, aguarda os pods ficarem prontos dentro de `progressDeadlineSeconds` (padrão `600s`) e, a cada `analysis.interval` (padrão `60s`), incrementa o peso de tráfego do canário em `stepWeight` até atingir `maxWeight`, validando as métricas a cada passo. Se o número de falhas atingir `threshold`, o Flagger aborta a entrega, zera o tráfego do canário e marca o rollout como `Failed`; se atingir `maxWeight` sem falhas, promove a nova especificação para o `<nome>-primary`, redireciona 100% do tráfego de volta ao primário e recolhe o canário para zero.

## Exemplo
```yaml
# Especificação essencial do CRD Canary do Flagger com targetRef, autoscalerRef e analysis
apiVersion: flagger.app/v1beta1
kind: Canary
metadata:
  name: podinfo
  namespace: test
spec:
  provider: istio
  targetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: podinfo
  progressDeadlineSeconds: 60
  autoscalerRef:
    apiVersion: autoscaling/v2
    kind: HorizontalPodAutoscaler
    name: podinfo
  service:
    port: 9898
    targetPort: 9898
    portDiscovery: true
  analysis:
    interval: 1m
    threshold: 10
    maxWeight: 50
    stepWeight: 5
```

## Limites e trade-offs
Durante a janela de análise e promoção (especialmente no momento em que o `<nome>-primary` recebe a atualização final antes do canário ser escalado de volta para zero), o cluster precisa ter capacidade livre de CPU e memória para acomodar simultaneamente as réplicas do primário e as réplicas do canário.

## Como verificar
Altere um valor no `ConfigMap` referenciado pelo Deployment `podinfo` e observe com `kubectl get canary podinfo -w` a transição automática de estado para `Progressing`, seguida pelo incremento gradual de `Canary Weight` até `Succeeded`.

## Conexões
- [[flagger-entrega-progressiva-kubernetes-flux-cncf]] — Veja também: Flux Flagger: operador CNCF Graduated de entrega progressiva para Kubernetes.
- [[flagger-estrategias-canary-ab-testing-blue-green-mirroring]] — Veja também: Flux Flagger: estratégias de implantação Canary, A/B Testing e Blue/Green com Traffic Mirroring.

## Fontes
- [Flux Flagger GitHub — README.md (Canary CRD, Service Mesh/Ingress/Gateway API, Metrics & Webhooks)](https://raw.githubusercontent.com/fluxcd/flagger/main/README.md) — README oficial do Flux Flagger cobrindo a especificação do CRD Canary, estratégias Canary/A/B/Blue-Green, matriz de provedores de rede, MetricTemplates, webhooks e alertas; consultado em 2026-10-03.
- [Flux Flagger Official Documentation — How it works & Canary Promotion Lifecycle](https://docs.flagger.app/main/usage/how-it-works) — Documentação oficial de funcionamento da máquina de estados de análise e promoção canário do Flagger; consultado em 2026-10-03.
- [Flux Flagger — Official GitHub Repository](https://github.com/fluxcd/flagger) — Repositório oficial Apache-2.0 do Flagger na família GitOps Flux (CNCF Graduated); consultado em 2026-10-03.
