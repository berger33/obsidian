---
id: software.devops.tranche19.001806
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-19.md"
fontes: ["https://raw.githubusercontent.com/openfaas/faas/master/README.md", "https://raw.githubusercontent.com/openfaas/faas-netes/master/README.md", "https://github.com/openfaas/faas-netes"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# OpenFaaS Auto-Scaling: escalonamento horizontal por RPS/capacidade (`com.openfaas.scale.min`/`max`) e *scale-to-zero*

## Em uma frase
O OpenFaaS inclui auto-scaling nativo guiado pelas métricas HTTP coletadas pelo **Prometheus** embutido no namespace `openfaas`, escalando o número de réplicas de cada função entre `com.openfaas.scale.min` e `com.openfaas.scale.max` (incluindo *scale-to-zero*).

## Por que importa
Manter dezenas de funções raramente chamadas rodando com réplicas ociosas 24x7 desperdiça memória do cluster; por outro lado, funções críticas em horário de pico precisam escalar rapidamente por taxa de requisições por segundo (RPS) ou conexões inflight.

## Como funciona
O desenvolvedor aplica labels na função (em `stack.yaml` ou no CRD `Function`): `com.openfaas.scale.min: "2"`, `com.openfaas.scale.max: "15"`, `com.openfaas.scale.factor: "20"` e `com.openfaas.scale.zero: "true"`. Quando uma função escalada para `0` réplicas recebe uma chamada no Gateway, o Gateway retém a conexão brevemente enquanto instrui o `faas-netes` a subir `1` réplica e entrega a requisição sem erro.

## Exemplo
```yaml
functions:
  image-resizer:
    lang: python3-http
    handler: ./image-resizer
    image: ghcr.io/org/image-resizer:1.0.0
    labels:
      com.openfaas.scale.min: "1"
      com.openfaas.scale.max: "10"
      com.openfaas.scale.factor: "25"
      com.openfaas.scale.zero: "true"
```

## Limites e trade-offs
Para desabilitar completamente o auto-scaling em uma função específica que deve permanecer com número fixo de réplicas, defina `com.openfaas.scale.min` e `com.openfaas.scale.max` com exatamente o mesmo valor ou `com.openfaas.scale.factor: "0"`.

## Como verificar
Verifique os labels aplicados no Deployment da função em `openfaas-fn` e monitore as métricas `gateway_function_invocation_total` no Prometheus do OpenFaaS.

## Conexões
- [[openfaas-invocacao-assincrona-function-routes-nats-queue-worker-callback]] — Veja também: OpenFaaS Invocação Assíncrona: processamento em background via `/async-function/<name>`, NATS e `X-Callback-Url`.
- [[openfaas-gerenciamento-secrets-kubernetes-mounted-var-openfaas-secrets]] — Veja também: OpenFaaS Secrets: gerenciamento declarativo de segredos montados como arquivos em `/var/openfaas/secrets/`.

## Fontes
- [OpenFaaS GitHub — README.md (Serverless Functions Made Simple, Stack Architecture, Code Samples & Template Store)](https://raw.githubusercontent.com/openfaas/faas/master/README.md) — README oficial do openfaas/faas apresentando a arquitetura conceitual, uso da CLI faas-cli, templates de linguagem e auto-scaling; consultado em 2026-10-03.
- [OpenFaaS faas-netes GitHub — README.md (Kubernetes Provider, Controller vs Operator Function CRD, Readiness Lock & Helm Resources)](https://raw.githubusercontent.com/openfaas/faas-netes/master/README.md) — Documentação oficial do provedor faas-netes cobrindo modos controller e operator (Function CRD), readiness probe com arquivo .lock e dimensionamento; consultado em 2026-10-03.
- [OpenFaaS faas-netes — Official GitHub Repository](https://github.com/openfaas/faas-netes) — Repositório oficial do provedor Kubernetes faas-netes do OpenFaaS; consultado em 2026-10-03.
