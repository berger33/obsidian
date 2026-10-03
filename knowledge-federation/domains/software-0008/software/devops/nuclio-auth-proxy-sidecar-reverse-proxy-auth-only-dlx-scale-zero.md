---
id: software.devops.tranche19.001824
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
fontes: ["https://raw.githubusercontent.com/nuclio/nuclio/development/docs/concepts/architecture.md", "https://raw.githubusercontent.com/nuclio/nuclio/development/README.md", "https://github.com/nuclio/nuclio"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Nuclio no Kubernetes: autenticação de funções com `auth-proxy` sidecar (`reverse-proxy` vs `auth-only` no DLX)

## Em uma frase
Em implantações Kubernetes onde `authentication.functionAuthenticationEnabled` está habilitado na configuração da plataforma, cada Pod de função Nuclio executa dois containers: o **processor** (escutando apenas em loopback `127.0.0.1`) e o sidecar **`auth-proxy`** (ponto de entrada voltado ao cluster).

## Por que importa
Se o container processor ficasse exposto diretamente na rede do cluster sem camada de autenticação padronizada — ou se qualquer requisição não autenticada pudesse acordar funções em *scale-to-zero* (DLX) gastando GPUs — o cluster ficaria vulnerável a abuso.

## Como funciona
O `auth-proxy` opera em dois modos complementares: 1) **`reverse-proxy`** (roda como sidecar dentro de cada Pod de função, autenticando toda requisição HTTP antes de repassá-la ao processor em loopback); e 2) **`auth-only`** (roda junto ao Pod **DLX** de scale-to-zero, expondo um endpoint `/auth` que o DLX consulta para autenticar a chamada **antes** de escalar a função de 0 para 1 réplica).

## Exemplo
```bash
# O caminho /__internal/health é sempre liberado sem autenticação para probes do kubelet:
kubectl exec <nuclio-fn-pod> -c nuclio -- wget -qO- http://127.0.0.1:8080/__internal/health
```

## Limites e trade-offs
O caminho `/__internal/health` é sempre permitido sem autenticação pelo `auth-proxy` para que as `livenessProbe` e `readinessProbe` do `kubelet` continuem verificando o processor.

## Como verificar
Ative `functionAuthenticationEnabled` em um ambiente de teste e inspecione os 2 containers do Pod da função com `kubectl describe pod`.

## Conexões
- [[nuclio-blocking-vs-non-blocking-allocator-workers-sync-async]] — Veja também: Nuclio: alocação de EventProcessors em dois níveis (`Blocking Allocator` vs `Non-blocking Allocator`) para modos Sync e Async.
- [[nuclio-nuctl-cli-build-deploy-invoke-function-yaml-kaniko]] — Veja também: Nuclio `nuctl` CLI e Builder Kaniko: construção segura de imagens de função in-cluster e deploy declarativo.

## Fontes
- [Nuclio GitHub — README.md (High-Performance Serverless for Real-Time Events, Data Processing, GPUs, Kaniko & Kubernetes)](https://raw.githubusercontent.com/nuclio/nuclio/development/docs/concepts/architecture.md) — README oficial do nuclio/nuclio apresentando integração com Jupyter/Kubeflow/MLRun, suporte a GPUs, builder Kaniko e fluxo de deploy; consultado em 2026-10-03.
- [Nuclio Official Documentation — Architecture (Function Processors, Event-Source Listeners, Native/SHMEM/Shell Runtimes, Allocators & Auth-Proxy)](https://raw.githubusercontent.com/nuclio/nuclio/development/README.md) — Documentação oficial de arquitetura do Nuclio detalhando o Function Processor, Blocking vs Non-blocking Allocator, Data Bindings e sidecar auth-proxy; consultado em 2026-10-03.
- [Nuclio — Official GitHub Repository](https://github.com/nuclio/nuclio) — Repositório oficial Apache-2.0 do projeto Nuclio; consultado em 2026-10-03.
