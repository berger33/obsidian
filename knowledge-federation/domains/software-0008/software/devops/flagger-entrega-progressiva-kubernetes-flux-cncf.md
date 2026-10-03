---
id: software.devops.tranche07.000661
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

# Flux Flagger: operador CNCF Graduated de entrega progressiva para Kubernetes

## Em uma frase
O Flagger (projeto graduado da CNCF e parte da família de ferramentas GitOps do Flux, sob licença Apache-2.0) é um operador de entrega progressiva que automatiza lançamentos em Kubernetes deslocando tráfego gradualmente enquanto mede métricas e executa testes.

## Por que importa
Em um `Deployment` padrão do Kubernetes com `RollingUpdate`, assim que o novo pod passa no `readinessProbe` básico, o controlador substitui rapidamente todas as réplicas antigas sem verificar se a nova versão causou aumento na taxa de erros HTTP 500 ou degradação na latência P99 sob tráfego real. Segundo o README oficial do Flagger, a ferramenta reduz o risco de introduzir novas versões em produção ao automatizar análises de KPIs e rollbacks imediatos.

## Como funciona
O Flagger recebe como entrada um `Deployment` Kubernetes (e opcionalmente um `HorizontalPodAutoscaler`) por meio do recurso customizado `Canary` (`apiVersion: flagger.app/v1beta1`) e cria e gerencia automaticamente uma série de objetos no cluster: deployments primário (`<nome>-primary`) e canário, serviços `ClusterIP` (`-primary`, `-canary`, `-apex`) e rotas de Service Mesh ou Ingress. O controlador monitora continuamente tanto a imagem do container quanto os `ConfigMaps` e `Secrets` referenciados pelo Deployment; qualquer alteração nesses objetos dispara uma nova análise canário que sincroniza código e configuração apenas se as verificações de métricas e webhooks forem aprovadas.

## Exemplo
```bash
# Instalar o Flagger e monitorar o progresso dos recursos Canary no cluster Kubernetes
kubectl get canaries -A
kubectl describe canary podinfo -n test
```

## Limites e trade-offs
Como o Flagger assume o controle do roteamento e cria um deployment `<nome>-primary` espelhado a partir do `Deployment` alvo original, durante o estado estacionário (quando nenhum lançamento está ocorrendo) as réplicas do Deployment alvo original são mantidas em `0` e todo o tráfego de produção é atendido pelo `<nome>-primary`; equipes que não conhecem esse funcionamento podem estranhar ver `0/0` réplicas no Deployment original.

## Como verificar
Execute `kubectl get canaries -n test` e confirme que o recurso `Canary` atingiu o status `Initialized` (e `Succeeded` após uma promoção) e que o deployment `<nome>-primary` está atendendo o tráfego.

## Conexões
- [[flagger-crd-canary-ciclo-vida-promocao-configmaps-secrets]] — Veja também: Flux Flagger: anatomia do CRD Canary, sincronização de ConfigMaps/Secrets e máquina de estados.
- [[flagger-estrategias-canary-ab-testing-blue-green-mirroring]] — Referência cruzada direta com flagger-estrategias-canary-ab-testing-blue-green-mirroring.
- [[flagger-analise-metricas-prometheus-metrictemplate-kpis]] — Referência cruzada direta com flagger-analise-metricas-prometheus-metrictemplate-kpis.

## Fontes
- [Flux Flagger GitHub — README.md (Canary CRD, Service Mesh/Ingress/Gateway API, Metrics & Webhooks)](https://raw.githubusercontent.com/fluxcd/flagger/main/README.md) — README oficial do Flux Flagger cobrindo a especificação do CRD Canary, estratégias Canary/A/B/Blue-Green, matriz de provedores de rede, MetricTemplates, webhooks e alertas; consultado em 2026-10-03.
- [Flux Flagger Official Documentation — How it works & Canary Promotion Lifecycle](https://docs.flagger.app/main/usage/how-it-works) — Documentação oficial de funcionamento da máquina de estados de análise e promoção canário do Flagger; consultado em 2026-10-03.
- [Flux Flagger — Official GitHub Repository](https://github.com/fluxcd/flagger) — Repositório oficial Apache-2.0 do Flagger na família GitOps Flux (CNCF Graduated); consultado em 2026-10-03.
