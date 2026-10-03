---
id: software.devops.tranche14.001393
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

# crictl: Inspeção de Pod Sandboxes e Containers nos Nós (pods, ps, inspectp e inspect)

## Em uma frase
Na arquitetura CRI do Kubernetes, cada Pod corresponde a um **PodSandbox** (gerenciado por `crictl pods` e `crictl inspectp`) dentro do qual rodam um ou mais containers de aplicação e init containers (gerenciados por `crictl ps` e `crictl inspect`).

## Por que importa
Diferente do `docker ps`, onde não existe o conceito nativo de Pod, depurar um problema de rede ou cgroup em um nó Kubernetes exige distinguir o estado do Sandbox do Pod (que detém o namespace de rede e o IP do Pod) do estado dos containers individuais.

## Como funciona
Com `crictl pods --name <nome> --namespace <ns>`, localiza-se o `POD ID` e seu estado (`SANDBOX_READY` ou `SANDBOX_NOTREADY`); com `crictl inspectp <pod-id>`, inspecionam-se o IP atribuído pelo CNI, os namespaces Linux e o cgroup path; e com `crictl ps -a --pod <pod-id>` e `crictl inspect <container-id>`, verificam-se o `exitCode`, o `reason` (`OOMKilled`, `Error`), os mounts e a especificação OCI completa.

## Exemplo
```bash
crictl pods --namespace kube-system
crictl ps -a --state Exited
crictl inspectp $(crictl pods -q --name coredns | head -n 1)
```

## Limites e trade-offs
Executar `crictl ps` sem a flag `-a` mostra apenas os containers atualmente em estado `Running`, escondendo justamente os containers que acabaram de falhar (`Exited`) em um `CrashLoopBackOff`.

## Como verificar
Use sempre `crictl ps -a` (ou `--state Exited`) para encontrar os containers que falharam e inspecionar seu código de saída e logs.

## Conexões
- [[crictl-configuracao-etc-crictl-yaml-runtime-endpoint-image-endpoint]] — Veja também: crictl: Configuração de Endpoints (/etc/crictl.yaml, runtime-endpoint e image-endpoint).
- [[crictl-logs-exec-attach-port-forward-troubleshooting-local]] — Veja também: crictl: Coleta de Logs, Execução de Comandos e Port-Forward Direto no Nó (logs, exec e port-forward).

## Fontes
- [cri-tools Official Documentation — docs/crictl.md (CRI CLI Commands, /etc/crictl.yaml, runtime-endpoint, stats/statsp/metricsp, checkpoint & OpenTelemetry Tracing)](https://raw.githubusercontent.com/kubernetes-sigs/cri-tools/master/docs/crictl.md) — Guia oficial completo do crictl detalhando todos os subcomandos de PodSandbox, containers, imagens e métricas CRI, configuração de /etc/crictl.yaml e flags de tracing/timeout; consultado em 2026-10-03.
- [kubernetes-sigs/cri-tools GitHub — README.md (Project Scope, Kubernetes Version Compatibility Matrix, crictl & critest Installation)](https://raw.githubusercontent.com/kubernetes-sigs/cri-tools/master/README.md) — README oficial do kubernetes-sigs/cri-tools explicando o escopo do crictl e do critest e a matriz de compatibilidade de versões minor com o Kubernetes; consultado em 2026-10-03.
- [Kubernetes SIG Node cri-tools — Official GitHub Repository](https://github.com/kubernetes-sigs/cri-tools) — Repositório oficial Apache-2.0 do cri-tools; consultado em 2026-10-03.
