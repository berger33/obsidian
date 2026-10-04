---
id: software.devops.tranche14.001392
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

# crictl: Configuração de Endpoints (/etc/crictl.yaml, runtime-endpoint e image-endpoint)

## Em uma frase
Para operar sem atrasos ou avisos de depreciação, o `crictl` deve ter seus endpoints gRPC (`runtime-endpoint` e `image-endpoint`) explicitamente definidos no arquivo `/etc/crictl.yaml` (ou via variáveis `CONTAINER_RUNTIME_ENDPOINT`/`IMAGE_SERVICE_ENDPOINT` ou flags `-r`/`-i`).

## Por que importa
Conforme documentado oficialmente, o fallback antigo que tentava conectar sequencialmente em `unix:///run/containerd/containerd.sock`, `unix:///run/crio/crio.sock` e `unix:///var/run/cri-dockerd.sock` está depreciado e adiciona vários segundos de timeout a cada tentativa falha.

## Como funciona
Criando `/etc/crictl.yaml` (ou usando `crictl config --set runtime-endpoint=unix:///run/containerd/containerd.sock`), o `crictl` conecta-se instantaneamente ao socket correto com o `timeout` (padrão `2s`) e `max-retries` (padrão `3`) configurados.

## Exemplo
```yaml
runtime-endpoint: unix:///run/containerd/containerd.sock
image-endpoint: unix:///run/containerd/containerd.sock
timeout: 2
debug: false
pull-image-on-create: false
max-retries: 3
```

## Limites e trade-offs
Executar `sudo crictl ...` dependendo de variáveis de ambiente (`CONTAINER_RUNTIME_ENDPOINT` ou `GRPC_GO_REQUIRE_HANDSHAKE=off`) sem passar `sudo -E` faz o `sudo` limpar as variáveis de ambiente e cair no fallback lento.

## Como verificar
Configure os endpoints permanentemente em `/etc/crictl.yaml` em todos os nós do cluster (ou use `sudo -E` quando testar variáveis de ambiente).

## Conexões
- [[crictl-arquitetura-cli-kubelet-cri-container-runtime-interface]] — Veja também: crictl: Arquitetura da CLI Oficial para a Kubelet Container Runtime Interface (CRI).
- [[crictl-pods-ps-inspectp-inspect-depuracao-sandboxes-containers]] — Veja também: crictl: Inspeção de Pod Sandboxes e Containers nos Nós (pods, ps, inspectp e inspect).

## Fontes
- [cri-tools Official Documentation — docs/crictl.md (CRI CLI Commands, /etc/crictl.yaml, runtime-endpoint, stats/statsp/metricsp, checkpoint & OpenTelemetry Tracing)](https://raw.githubusercontent.com/kubernetes-sigs/cri-tools/master/docs/crictl.md) — Guia oficial completo do crictl detalhando todos os subcomandos de PodSandbox, containers, imagens e métricas CRI, configuração de /etc/crictl.yaml e flags de tracing/timeout; consultado em 2026-10-03.
- [kubernetes-sigs/cri-tools GitHub — README.md (Project Scope, Kubernetes Version Compatibility Matrix, crictl & critest Installation)](https://raw.githubusercontent.com/kubernetes-sigs/cri-tools/master/README.md) — README oficial do kubernetes-sigs/cri-tools explicando o escopo do crictl e do critest e a matriz de compatibilidade de versões minor com o Kubernetes; consultado em 2026-10-03.
- [Kubernetes SIG Node cri-tools — Official GitHub Repository](https://github.com/kubernetes-sigs/cri-tools) — Repositório oficial Apache-2.0 do cri-tools; consultado em 2026-10-03.
