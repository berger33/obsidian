---
id: software.devops.tranche07.000663
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

# Flux Flagger: estratégias de implantação Canary, A/B Testing e Blue/Green com Traffic Mirroring

## Em uma frase
O Flagger implementa múltiplas estratégias de entrega progressiva: lançamentos Canary (deslocamento gradual de peso), A/B Testing (roteamento por cabeçalhos HTTP e cookies) e Blue/Green (chaveamento de tráfego ou espelhamento/shadowing).

## Por que importa
Nem toda aplicação pode receber divisão percentual aleatória de tráfego: frontends web que exigem consistência visual para um mesmo usuário logado precisam de A/B testing baseado em cookies ou headers, enquanto aplicações em clusters sem Service Mesh ou Ingress com suporte a pesos precisam de validação Blue/Green tradicional ou espelhamento de tráfego (traffic mirroring) sem impacto nas respostas de produção. O README oficial do Flagger documenta a matriz completa de estratégias suportadas.

## Como funciona
A estratégia é determinada pelos parâmetros em `spec.analysis`: (1) **Canary (weighted traffic)**: utiliza `stepWeight` e `maxWeight` para deslocar percentuais crescentes de tráfego em provedores de Service Mesh, Ingress ou Gateway API; (2) **A/B Testing**: utiliza `iterations` em conjunto com `match` (condições de cabeçalhos HTTP ou cookies de sessão) para rotear 100% dos usuários que atendem ao critério para o canário durante `N` ciclos de avaliação; (3) **Blue/Green (traffic switch)**: funciona até mesmo com CNI padrão do Kubernetes (`provider: kubernetes`), executando testes de conformidade e carga contra o serviço `-canary` em `iterations` antes de virar a chave do seletor Kubernetes de uma só vez para o primário atualizado; e (4) **Blue/Green com Traffic Mirroring**: suportado no Istio, duplica uma cópia sombra do tráfego real de produção para o canário sem afetar os clientes enquanto mede taxas de sucesso e latência.

## Exemplo
```yaml
# Trecho de spec.analysis no Flagger para estratégia A/B Testing roteando por Header HTTP ou Cookie
  analysis:
    interval: 1m
    iterations: 10
    threshold: 2
    match:
      - headers:
          x-canary:
            exact: "insider"
      - headers:
          cookie:
            regex: "^(.*?;)?(type=insider)(;.*)?$"
```

## Limites e trade-offs
O espelhamento de tráfego (Blue/Green traffic mirroring) só deve ser habilitado em serviços idempotentes de leitura ou cujos efeitos colaterais em bancos de dados e filas externas estejam isolados/mockados na versão canário, pois cada requisição de produção será processada duas vezes (uma pelo primário e outra em segundo plano pelo canário).

## Como verificar
Inspecione os recursos de roteamento gerados pelo Flagger (como `VirtualService` do Istio ou `HTTPRoute` da Gateway API) durante um rollout ativo para confirmar a presença das regras de peso (`weight`), cabeçalhos (`match`) ou espelhamento (`mirror`).

## Conexões
- [[flagger-crd-canary-ciclo-vida-promocao-configmaps-secrets]] — Veja também: Flux Flagger: anatomia do CRD Canary, sincronização de ConfigMaps/Secrets e máquina de estados.
- [[flagger-integracao-service-mesh-ingress-gateway-api-smi]] — Veja também: Flux Flagger: matriz de integrações com Service Meshes, Ingress Controllers, Gateway API e SMI.
- [[flagger-entrega-progressiva-kubernetes-flux-cncf]] — Referência cruzada direta com flagger-entrega-progressiva-kubernetes-flux-cncf.

## Fontes
- [Flux Flagger GitHub — README.md (Canary CRD, Service Mesh/Ingress/Gateway API, Metrics & Webhooks)](https://raw.githubusercontent.com/fluxcd/flagger/main/README.md) — README oficial do Flux Flagger cobrindo a especificação do CRD Canary, estratégias Canary/A/B/Blue-Green, matriz de provedores de rede, MetricTemplates, webhooks e alertas; consultado em 2026-10-03.
- [Flux Flagger Official Documentation — How it works & Canary Promotion Lifecycle](https://docs.flagger.app/main/usage/how-it-works) — Documentação oficial de funcionamento da máquina de estados de análise e promoção canário do Flagger; consultado em 2026-10-03.
- [Flux Flagger — Official GitHub Repository](https://github.com/fluxcd/flagger) — Repositório oficial Apache-2.0 do Flagger na família GitOps Flux (CNCF Graduated); consultado em 2026-10-03.
