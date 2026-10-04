---
id: software.devops.tranche07.000664
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

# Flux Flagger: matriz de integrações com Service Meshes, Ingress Controllers, Gateway API e SMI

## Em uma frase
O Flagger integra-se nativamente com Service Meshes (Istio, Linkerd, Kuma, Knative), Ingress Controllers (Contour, Gloo, NGINX, Skipper, Traefik, Apache APISIX), Kubernetes CNI e padrões Gateway API (`gatewayapi:v1`) e SMI.

## Por que importa
Organizações adotam diferentes camadas de rede em seus clusters Kubernetes — desde malhas completas como Istio e Linkerd até Ingress Controllers leves como NGINX, Traefik ou APISIX, ou a especificação oficial Kubernetes Gateway API. Segundo o README oficial do Flagger, o campo `spec.provider` abstrai essas diferenças, permitindo usar o mesmo CRD `Canary` independentemente da tecnologia de roteamento subjacente.

## Como funciona
De acordo com o valor configurado em `spec.provider` (`kubernetes`, `istio`, `linkerd`, `kuma`, `knative`, `nginx`, `contour`, `gloo`, `traefik`, `skipper`, `apisix`, `gatewayapi:v1`, `gatewayapi:v1beta1` ou `smi`), o reconciliador do Flagger gera automaticamente os objetos de rede específicos daquele provedor (por exemplo, `VirtualService` e `DestinationRule` no Istio, `TrafficSplit` no Linkerd/SMI, anotações canary de `Ingress` no NGINX, ou `HTTPRoute` com `backendRefs` ponderados na Gateway API) apontando para os serviços `<nome>-primary` e `<nome>-canary`.

## Exemplo
```yaml
# Configuração do provedor Gateway API v1 em um recurso Canary do Flagger
apiVersion: flagger.app/v1beta1
kind: Canary
metadata:
  name: podinfo
  namespace: test
spec:
  provider: gatewayapi:v1
  targetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: podinfo
  service:
    port: 9898
    gatewayRefs:
      - name: main-gateway
        namespace: infra-gateway
```

## Limites e trade-offs
Nem todos os provedores suportam todas as funcionalidades na matriz oficial do Flagger: por exemplo, `kubernetes` CNI suporta apenas Blue/Green com chaveamento de tráfego (sem pesos graduais nem A/B testing); Blue/Green com traffic mirroring é exclusivo do Istio; e para implementações da Gateway API e NGINX Ingress que não possuem as métricas L7 embutidas padrão, deve-se utilizar `MetricTemplates` customizados do Prometheus para verificar taxa de sucesso e duração de requisições.

## Como verificar
Execute `kubectl get httproutes,virtualservices,ingresses -n test` após a inicialização do `Canary` para confirmar que o Flagger gerou o recurso de roteamento nativo do provedor especificado em `spec.provider`.

## Conexões
- [[flagger-estrategias-canary-ab-testing-blue-green-mirroring]] — Veja também: Flux Flagger: estratégias de implantação Canary, A/B Testing e Blue/Green com Traffic Mirroring.
- [[flagger-analise-metricas-prometheus-metrictemplate-kpis]] — Veja também: Flux Flagger: validação de KPIs com verificações nativas e MetricTemplates customizados no Prometheus.
- [[flagger-entrega-progressiva-kubernetes-flux-cncf]] — Referência cruzada direta com flagger-entrega-progressiva-kubernetes-flux-cncf.

## Fontes
- [Flux Flagger GitHub — README.md (Canary CRD, Service Mesh/Ingress/Gateway API, Metrics & Webhooks)](https://raw.githubusercontent.com/fluxcd/flagger/main/README.md) — README oficial do Flux Flagger cobrindo a especificação do CRD Canary, estratégias Canary/A/B/Blue-Green, matriz de provedores de rede, MetricTemplates, webhooks e alertas; consultado em 2026-10-03.
- [Flux Flagger Official Documentation — How it works & Canary Promotion Lifecycle](https://docs.flagger.app/main/usage/how-it-works) — Documentação oficial de funcionamento da máquina de estados de análise e promoção canário do Flagger; consultado em 2026-10-03.
- [Flux Flagger — Official GitHub Repository](https://github.com/fluxcd/flagger) — Repositório oficial Apache-2.0 do Flagger na família GitOps Flux (CNCF Graduated); consultado em 2026-10-03.
