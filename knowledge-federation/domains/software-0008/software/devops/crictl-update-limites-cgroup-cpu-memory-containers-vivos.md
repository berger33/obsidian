---
id: software.devops.tranche14.001398
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-14.md"
fontes: ["https://raw.githubusercontent.com/kubernetes-sigs/cri-tools/master/docs/crictl.md", "https://raw.githubusercontent.com/kubernetes-sigs/cri-tools/master/README.md", "https://github.com/kubernetes-sigs/cri-tools"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# crictl: Atualização Dinâmica de Limites de Cgroup (crictl update) e Tracing OpenTelemetry

## Em uma frase
O subcomando `crictl update` permite atualizar em tempo real os limites de recursos de cgroup (`--cpu-period`, `--cpu-quota`, `--cpu-shares`, `--memory`, `--cpuset-cpus`, `--cpuset-mems`) de um ou mais containers em execução via API CRI, e as flags globais `--enable-tracing` e `--tracing-endpoint` exportam traces OpenTelemetry das chamadas gRPC do `crictl`.

## Por que importa
Durante a depuração de performance do próprio runtime CRI ou testes de redimensionamento in-place de containers no nó, é necessário verificar como o runtime aplica alterações de cgroup e quanto tempo cada RPC gRPC leva.

## Como funciona
Passando `--enable-tracing --tracing-endpoint 127.0.0.1:4317`, o `crictl` emite spans OpenTelemetry de cada operação CRI; e com `crictl update --memory 536870912 <container-id>`, solicita ao runtime o ajuste imediato do limite de memória do cgroup.

## Exemplo
```bash
crictl --enable-tracing --tracing-endpoint 127.0.0.1:4317 pods
crictl update --memory 536870912 "$CONTAINER_ID"
```

## Limites e trade-offs
Alterar limites de um container gerenciado pelo Kubernetes manualmente via `crictl update` sem atualizar a spec do Pod no `kube-apiserver` pode ser sobrescrito pelo `kubelet` na próxima reconciliação de recursos.

## Como verificar
Para redimensionamento persistente em clusters Kubernetes, utilize o recurso nativo *In-Place Pod Vertical Scaling* na API do Kubernetes e use `crictl inspect` para verificar se os limites foram aplicados no runtime.

## Conexões
- [[crictl-checkpoint-events-runtime-config-live-updates]] — Veja também: crictl: Checkpoint de Containers (checkpoint), Stream de Eventos (events) e Runtime Config.
- [[crictl-execucao-sandboxes-containers-json-yaml-runp-create-start]] — Veja também: crictl: Teste Isolado de Runtimes CRI sem Kubelet usando Arquivos JSON/YAML (runp, create, start e run).

## Fontes
- [cri-tools Official Documentation — docs/crictl.md (CRI CLI Commands, /etc/crictl.yaml, runtime-endpoint, stats/statsp/metricsp, checkpoint & OpenTelemetry Tracing)](https://raw.githubusercontent.com/kubernetes-sigs/cri-tools/master/docs/crictl.md) — Guia oficial completo do crictl detalhando todos os subcomandos de PodSandbox, containers, imagens e métricas CRI, configuração de /etc/crictl.yaml e flags de tracing/timeout; consultado em 2026-10-03.
- [kubernetes-sigs/cri-tools GitHub — README.md (Project Scope, Kubernetes Version Compatibility Matrix, crictl & critest Installation)](https://raw.githubusercontent.com/kubernetes-sigs/cri-tools/master/README.md) — README oficial do kubernetes-sigs/cri-tools explicando o escopo do crictl e do critest e a matriz de compatibilidade de versões minor com o Kubernetes; consultado em 2026-10-03.
- [Kubernetes SIG Node cri-tools — Official GitHub Repository](https://github.com/kubernetes-sigs/cri-tools) — Repositório oficial Apache-2.0 do cri-tools; consultado em 2026-10-03.
