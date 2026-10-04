---
id: software.devops.tranche19.001805
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

# OpenFaaS Invocação Assíncrona: processamento em background via `/async-function/<name>`, NATS e `X-Callback-Url`

## Em uma frase
Toda função implantada no OpenFaaS ganha automaticamente dois endpoints no Gateway: `/function/<nome>` (para execução síncrona imediata) e **`/async-function/<nome>`** (para enfileiramento assíncrono em background processado pelo `queue-worker` sobre NATS).

## Por que importa
Quando um webhook externo (como GitHub, Stripe ou Slack) exige resposta HTTP `202 Accepted` em menos de 3 segundos, mas o processamento real leva 45 segundos, executar de forma síncrona causaria timeout no emissor.

## Como funciona
Ao enviar um `POST` para `/async-function/<nome>` (opcionalmente passando o cabeçalho HTTP `X-Callback-Url: https://meu-receptor/webhook`), o Gateway grava o payload na fila NATS, retorna `202 Accepted` imediatamente com `X-Call-Id` e o `queue-worker` consome a mensagem, invoca a função e posta o resultado final na `X-Callback-Url`.

## Exemplo
```bash
curl -i -X POST http://127.0.0.1:8080/async-function/nodeinfo \
  -H "X-Callback-Url: http://webhook-receiver.default.svc.cluster.local:8080/done" \
  -d "processar em background"
```

## Limites e trade-offs
No dimensionamento de recursos do chart `openfaas`, ajuste `queueWorker.resources` e o limite de concorrência (`max_inflight`) do `queue-worker` para controlar a pressão exercida sobre os Pods das funções.

## Como verificar
Invoque `/async-function/<nome>` com `curl -i`, confirme o código HTTP `202 Accepted` e acompanhe `kubectl logs -n openfaas deploy/queue-worker`.

## Conexões
- [[openfaas-watchdog-http-mode-readiness-lock-file-timeouts]] — Veja também: OpenFaaS `of-watchdog` e Probes de Saúde: gerenciamento do arquivo `.lock` de readiness e timeouts de leitura/escrita.
- [[openfaas-autoscaling-prometheus-alertmanager-scale-min-max-zero]] — Veja também: OpenFaaS Auto-Scaling: escalonamento horizontal por RPS/capacidade (`com.openfaas.scale.min`/`max`) e *scale-to-zero*.

## Fontes
- [OpenFaaS GitHub — README.md (Serverless Functions Made Simple, Stack Architecture, Code Samples & Template Store)](https://raw.githubusercontent.com/openfaas/faas/master/README.md) — README oficial do openfaas/faas apresentando a arquitetura conceitual, uso da CLI faas-cli, templates de linguagem e auto-scaling; consultado em 2026-10-03.
- [OpenFaaS faas-netes GitHub — README.md (Kubernetes Provider, Controller vs Operator Function CRD, Readiness Lock & Helm Resources)](https://raw.githubusercontent.com/openfaas/faas-netes/master/README.md) — Documentação oficial do provedor faas-netes cobrindo modos controller e operator (Function CRD), readiness probe com arquivo .lock e dimensionamento; consultado em 2026-10-03.
- [OpenFaaS faas-netes — Official GitHub Repository](https://github.com/openfaas/faas-netes) — Repositório oficial do provedor Kubernetes faas-netes do OpenFaaS; consultado em 2026-10-03.
