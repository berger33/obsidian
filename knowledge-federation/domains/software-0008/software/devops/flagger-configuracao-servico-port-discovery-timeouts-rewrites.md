---
id: software.devops.tranche07.000669
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

# Flux Flagger: configuração de serviços ClusterIP, portDiscovery, timeouts e regras HTTP no Canary

## Em uma frase
O bloco `spec.service` do CRD `Canary` governa a geração dos serviços `ClusterIP` (`-primary`, `-canary` e `-apex`), descoberta automática de portas (`portDiscovery`) e políticas L7 de roteamento (`match`, `rewrite`, `timeout`, `retries`).

## Por que importa
Microsserviços reais frequentemente expõem múltiplas portas além da porta HTTP principal (como uma porta de métricas Prometheus, uma porta de healthcheck administrativa ou uma porta gRPC) e exigem timeouts e reescritas de URI específicos no Service Mesh ou Ingress. De acordo com o README oficial do Flagger, o bloco `spec.service` centraliza a geração tanto dos Services Kubernetes quanto das regras HTTP do provedor de malha/ingress.

## Como funciona
Quando o Flagger reconcilia `spec.service`, ele cria três serviços `ClusterIP`: `<nome>-primary` (selecionando os pods primários), `<nome>-canary` (selecionando os pods canário) e `<nome>` (o serviço apex). O administrador define `port` (porta do ClusterIP), `targetPort` (nome ou número da porta do container) e `portName` (`http` ou `grpc`, padrão `http`). Quando `portDiscovery: true` (padrão `false`) é habilitado, o Flagger inspeciona o pod template do Deployment e adiciona automaticamente todas as demais portas declaradas nos containers aos serviços ClusterIP gerados. Além disso, os campos `match` (ex.: `uri.prefix`), `rewrite` e `timeout` (ex.: `5s`) são propagados diretamente para o `VirtualService`, `HTTPRoute` ou `Ingress`.

## Exemplo
```yaml
# Configuração detalhada de spec.service com portDiscovery, match, rewrite e timeout no Flagger
  service:
    name: podinfo
    port: 9898
    targetPort: 9898
    portName: http
    portDiscovery: true
    match:
      - uri:
          prefix: /
    rewrite:
      uri: /
    timeout: 5s
```

## Limites e trade-offs
Se `portDiscovery` for mantido no valor padrão `false` e os pods expuserem uma porta secundária (como `9090` para métricas ou `8081` para administração) que outros serviços do cluster tentam acessar via Service Kubernetes, essas portas secundárias não existirão nos serviços `<nome>-primary` e `<nome>-canary` a menos que `portDiscovery: true` ou `port` explícito seja configurado.

## Como verificar
Execute `kubectl get svc -n test` após a criação do `Canary` e inspecione com `kubectl describe svc podinfo-primary -n test` se a porta principal e as portas descobertas via `portDiscovery: true` estão mapeadas para os endpoints corretos.

## Conexões
- [[flagger-integracao-hpa-autoscaling-primario-canario]] — Veja também: Flux Flagger: coordenação de HorizontalPodAutoscaler (HPA) entre implantações primária e canário.
- [[flagger-monitoramento-operacional-skip-analysis-session-affinity]] — Veja também: Flux Flagger: operação em produção com skipAnalysis, afinidade de sessão em Gateway API e compatibilidade GitOps Toolkit.
- [[flagger-entrega-progressiva-kubernetes-flux-cncf]] — Referência cruzada direta com flagger-entrega-progressiva-kubernetes-flux-cncf.
- [[flagger-crd-canary-ciclo-vida-promocao-configmaps-secrets]] — Referência cruzada direta com flagger-crd-canary-ciclo-vida-promocao-configmaps-secrets.
- [[flagger-integracao-service-mesh-ingress-gateway-api-smi]] — Referência cruzada direta com flagger-integracao-service-mesh-ingress-gateway-api-smi.

## Fontes
- [Flux Flagger GitHub — README.md (Canary CRD, Service Mesh/Ingress/Gateway API, Metrics & Webhooks)](https://raw.githubusercontent.com/fluxcd/flagger/main/README.md) — README oficial do Flux Flagger cobrindo a especificação do CRD Canary, estratégias Canary/A/B/Blue-Green, matriz de provedores de rede, MetricTemplates, webhooks e alertas; consultado em 2026-10-03.
- [Flux Flagger Official Documentation — How it works & Canary Promotion Lifecycle](https://docs.flagger.app/main/usage/how-it-works) — Documentação oficial de funcionamento da máquina de estados de análise e promoção canário do Flagger; consultado em 2026-10-03.
- [Flux Flagger — Official GitHub Repository](https://github.com/fluxcd/flagger) — Repositório oficial Apache-2.0 do Flagger na família GitOps Flux (CNCF Graduated); consultado em 2026-10-03.
