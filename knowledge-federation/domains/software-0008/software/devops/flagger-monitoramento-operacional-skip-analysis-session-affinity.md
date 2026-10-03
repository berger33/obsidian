---
id: software.devops.tranche07.000670
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

# Flux Flagger: operação em produção com skipAnalysis, afinidade de sessão em Gateway API e compatibilidade GitOps Toolkit

## Em uma frase
O Flagger oferece controles operacionais como `skipAnalysis: true` para promoções emergenciais diretas, suporte a afinidade de sessão em lançamentos canário via Gateway API e integração contínua com o GitOps Toolkit do Flux v2.

## Por que importa
Durante a mitigação de uma vulnerabilidade crítica ou incidente severo em produção (hotfix), aguardar 20 minutos de passos graduais de análise canário é inaceitável; da mesma forma, aplicações stateful de borda que usam Gateway API exigem afinidade de sessão (sticky sessions) durante o deslocamento de pesos para que um mesmo cliente não alterne entre as versões primária e canário a cada clique. O README oficial do Flagger documenta tanto o controle `skipAnalysis` quanto os recursos de Gateway API e roadmap do GitOps Toolkit.

## Como funciona
Quando `spec.skipAnalysis: true` (padrão `false`) é definido no manifesto `Canary`, o Flagger ignora a avaliação gradual de métricas e webhooks e promove imediatamente a nova versão do Deployment, `ConfigMap` e `Secret` diretamente para o `<nome>-primary`. Para cenários com `provider: gatewayapi:v1`, conforme a tabela de recursos de Networking Interface do README do Flagger, há suporte a implantações canário com afinidade de sessão (`Canary deployments with session affinity`), garantindo persistência de roteamento entre primário e canário. Além disso, o próprio operador Flagger expõe métricas Prometheus sobre o status de todos os canários e integra-se ao ecossistema Flux v2 (`kstatus`, eventos compatíveis com Flux notification API).

## Exemplo
```bash
# Aplicar promoção imediata de emergência ignorando a análise gradual (skipAnalysis: true) via patch ou GitOps
kubectl patch canary podinfo -n test --type=merge -p '{"spec":{"skipAnalysis":true}}'

# Verificar métricas operacionais expostas pelo próprio controlador do Flagger na porta 8080
kubectl port-forward -n flagger-system deploy/flagger 8080:8080 &
curl -s http://localhost:8080/metrics | grep flagger_canary_
```

## Limites e trade-offs
Habilitar `skipAnalysis: true` para aplicar um hotfix emergencial desativa toda a rede de proteção de validação de métricas e rollback automático; se não for revertido para `skipAnalysis: false` no repositório Git logo após o incidente, os próximos lançamentos rotineiros continuarão indo direto para 100% do tráfego sem análise canário.

## Como verificar
Consulte as métricas `flagger_canary_status` e `flagger_canary_weight` no endpoint `/metrics` do controlador Flagger e confirme que o status do recurso `Canary` reflete fielmente as promoções e o peso atual de tráfego.

## Conexões
- [[flagger-configuracao-servico-port-discovery-timeouts-rewrites]] — Veja também: Flux Flagger: configuração de serviços ClusterIP, portDiscovery, timeouts e regras HTTP no Canary.
- [[flagger-entrega-progressiva-kubernetes-flux-cncf]] — Referência cruzada direta com flagger-entrega-progressiva-kubernetes-flux-cncf.
- [[flagger-integracao-service-mesh-ingress-gateway-api-smi]] — Referência cruzada direta com flagger-integracao-service-mesh-ingress-gateway-api-smi.

## Fontes
- [Flux Flagger GitHub — README.md (Canary CRD, Service Mesh/Ingress/Gateway API, Metrics & Webhooks)](https://raw.githubusercontent.com/fluxcd/flagger/main/README.md) — README oficial do Flux Flagger cobrindo a especificação do CRD Canary, estratégias Canary/A/B/Blue-Green, matriz de provedores de rede, MetricTemplates, webhooks e alertas; consultado em 2026-10-03.
- [Flux Flagger Official Documentation — How it works & Canary Promotion Lifecycle](https://docs.flagger.app/main/usage/how-it-works) — Documentação oficial de funcionamento da máquina de estados de análise e promoção canário do Flagger; consultado em 2026-10-03.
- [Flux Flagger — Official GitHub Repository](https://github.com/fluxcd/flagger) — Repositório oficial Apache-2.0 do Flagger na família GitOps Flux (CNCF Graduated); consultado em 2026-10-03.
