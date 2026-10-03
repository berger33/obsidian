---
id: software.devops.tranche07.000665
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

# Flux Flagger: validação de KPIs com verificações nativas e MetricTemplates customizados no Prometheus

## Em uma frase
Durante a análise canário, o Flagger valida indicadores de nível de serviço (SLIs) através das verificações nativas `request-success-rate` e `request-duration` e de consultas customizadas definidas em recursos `MetricTemplate`.

## Por que importa
Deslocar tráfego em passos de 5% só protege a produção se o operador souber medir objetivamente se o novo pod está saudável tanto em métricas HTTP de camada 7 quanto em métricas de negócio e infraestrutura (como conexões de banco de dados, filas pendentes ou erros gRPC). Segundo o README oficial do Flagger, o bloco `spec.analysis.metrics` avalia cada métrica contra `thresholdRange` (`min` / `max`) a cada ciclo e incrementa o contador de falhas se os limites forem violados.

## Como funciona
O Flagger inclui duas verificações embutidas para Prometheus na maioria dos provedores de Service Mesh e Ingress: `request-success-rate` (porcentagem mínima de respostas não-5xx, por exemplo `min: 99`) e `request-duration` (latência máxima P99 em milissegundos, por exemplo `max: 500`). Para qualquer outra métrica — ou para implementar checagens de sucesso e latência em provedores Gateway API e NGINX —, o engenheiro cria um CRD `MetricTemplate` contendo a consulta PromQL parametrizada (com variáveis como `{{ target }}`, `{{ namespace }}`, `{{ interval }}`) e a referencia em `spec.analysis.metrics[].templateRef`.

## Exemplo
```yaml
# Definição de métricas nativas e referência a MetricTemplate customizado em um Canary do Flagger
    metrics:
      - name: request-success-rate
        thresholdRange:
          min: 99
        interval: 1m
      - name: request-duration
        thresholdRange:
          max: 500
        interval: 30s
      - name: "database connections"
        templateRef:
          name: db-connections
        thresholdRange:
          min: 2
          max: 100
        interval: 1m
```

## Limites e trade-offs
Se a implantação canário não receber nenhuma requisição durante a janela de análise (por exemplo, em um ambiente de homologação sem tráfego de usuários reais e sem webhook de `flagger-loadtester`), as consultas PromQL de taxa de sucesso `rate(...)` retornarão vazio (`NaN`/no data), o que o Flagger trata como falha de verificação de métrica, levando ao rollback do rollout por ausência de tráfego de validação.

## Como verificar
Durante um rollout canário, acompanhe os eventos do recurso com `kubectl describe canary <nome>` para confirmar que as checagens `request-success-rate`, `request-duration` e os `MetricTemplates` estão retornando valores dentro do `thresholdRange`.

## Conexões
- [[flagger-integracao-service-mesh-ingress-gateway-api-smi]] — Veja também: Flux Flagger: matriz de integrações com Service Meshes, Ingress Controllers, Gateway API e SMI.
- [[flagger-webhooks-testes-carga-conformidade-manual-gating]] — Veja também: Flux Flagger: webhooks de ciclo de vida, geração de tráfego com loadtester, Helm test e manual gating.
- [[flagger-entrega-progressiva-kubernetes-flux-cncf]] — Referência cruzada direta com flagger-entrega-progressiva-kubernetes-flux-cncf.

## Fontes
- [Flux Flagger GitHub — README.md (Canary CRD, Service Mesh/Ingress/Gateway API, Metrics & Webhooks)](https://raw.githubusercontent.com/fluxcd/flagger/main/README.md) — README oficial do Flux Flagger cobrindo a especificação do CRD Canary, estratégias Canary/A/B/Blue-Green, matriz de provedores de rede, MetricTemplates, webhooks e alertas; consultado em 2026-10-03.
- [Flux Flagger Official Documentation — How it works & Canary Promotion Lifecycle](https://docs.flagger.app/main/usage/how-it-works) — Documentação oficial de funcionamento da máquina de estados de análise e promoção canário do Flagger; consultado em 2026-10-03.
- [Flux Flagger — Official GitHub Repository](https://github.com/fluxcd/flagger) — Repositório oficial Apache-2.0 do Flagger na família GitOps Flux (CNCF Graduated); consultado em 2026-10-03.
