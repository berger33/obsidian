---
id: software.devops.tranche14.001391
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
fontes: ["https://raw.githubusercontent.com/kubernetes-sigs/cri-tools/master/README.md", "https://raw.githubusercontent.com/kubernetes-sigs/cri-tools/master/docs/crictl.md", "https://github.com/kubernetes-sigs/cri-tools"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# crictl: Arquitetura da CLI Oficial para a Kubelet Container Runtime Interface (CRI)

## Em uma frase
O **`crictl`** (mantido pelo Kubernetes SIG Node no repositório `kubernetes-sigs/cri-tools`, GA desde a `v1.11.0`) é a interface de linha de comando oficial para inspecionar e depurar runtimes de container compatíveis com a **Kubelet Container Runtime Interface (CRI)** — como **containerd**, **CRI-O** e `cri-dockerd` — diretamente nos nós do cluster.

## Por que importa
Quando o `kube-apiserver` está inacessível ou um nó específico fica `NotReady`, o comando `kubectl` não consegue interagir diretamente com o runtime local daquele host para listar quais Pods e containers estão rodando ou travados.

## Como funciona
O `crictl` comunica-se diretamente via gRPC com o socket local do runtime usando exatamente o mesmo protocolo **CRI API** (`runtime/v1/api.proto`) utilizado pelo `kubelet`, acompanhando o ciclo de versões minor do Kubernetes (`1.x.y`).

## Exemplo
```bash
crictl version
crictl info
```

## Limites e trade-offs
Usar o `crictl` para criar e gerenciar Pods permanentes de produção por fora do Kubernetes (`crictl runp` / `crictl run`) falha porque a própria documentação oficial alerta que o `kubelet` remove automaticamente Pods que não existem no `kube-apiserver`.

## Como verificar
Utilize o `crictl` nos nós do cluster para **inspeção, diagnóstico e troubleshooting** e alinhe sempre a versão minor do `crictl` com a versão minor do Kubernetes.

## Conexões
- [[crictl-configuracao-etc-crictl-yaml-runtime-endpoint-image-endpoint]] — Veja também: crictl: Configuração de Endpoints (/etc/crictl.yaml, runtime-endpoint e image-endpoint).

## Fontes
- [cri-tools Official Documentation — docs/crictl.md (CRI CLI Commands, /etc/crictl.yaml, runtime-endpoint, stats/statsp/metricsp, checkpoint & OpenTelemetry Tracing)](https://raw.githubusercontent.com/kubernetes-sigs/cri-tools/master/README.md) — Guia oficial completo do crictl detalhando todos os subcomandos de PodSandbox, containers, imagens e métricas CRI, configuração de /etc/crictl.yaml e flags de tracing/timeout; consultado em 2026-10-03.
- [kubernetes-sigs/cri-tools GitHub — README.md (Project Scope, Kubernetes Version Compatibility Matrix, crictl & critest Installation)](https://raw.githubusercontent.com/kubernetes-sigs/cri-tools/master/docs/crictl.md) — README oficial do kubernetes-sigs/cri-tools explicando o escopo do crictl e do critest e a matriz de compatibilidade de versões minor com o Kubernetes; consultado em 2026-10-03.
- [Kubernetes SIG Node cri-tools — Official GitHub Repository](https://github.com/kubernetes-sigs/cri-tools) — Repositório oficial Apache-2.0 do cri-tools; consultado em 2026-10-03.
