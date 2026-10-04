---
id: software.devops.tranche14.001394
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

# crictl: Coleta de Logs, Execução de Comandos e Port-Forward Direto no Nó (logs, exec e port-forward)

## Em uma frase
Os subcomandos `crictl logs`, `crictl exec`, `crictl attach` e `crictl port-forward` permitem interagir diretamente com os containers e Pods em um nó específico sem passar pelo `kube-apiserver`.

## Por que importa
Quando o `kube-apiserver`, o `etcd` (rodando como Static Pod) ou o plugin CNI do nó estão fora do ar, `kubectl logs` e `kubectl exec` falham por indisponibilidade da API ou da rede do cluster.

## Como funciona
Conectado ao nó via SSH ou console serial, o engenheiro executa `crictl ps -a` para localizar o container do `kube-apiserver` ou `etcd` e roda `crictl logs --tail=100 -f <container-id>` para ler a causa raiz da falha diretamente do arquivo de log gerenciado pelo CRI.

## Exemplo
```bash
CONTAINER_ID=$(crictl ps -a --name kube-apiserver -q | head -n 1)
crictl logs --tail=50 "$CONTAINER_ID"
```

## Limites e trade-offs
Tentar passar o nome ou ID do **Pod** (`POD ID` retornado por `crictl pods`) para `crictl logs` ou `crictl exec` falha porque esses comandos operam sobre o **`CONTAINER ID`** (retornado por `crictl ps`).

## Como verificar
Obtenha primeiro o `CONTAINER ID` com `crictl ps -a` antes de invocar `crictl logs` ou `crictl exec`, e use o `POD ID` para `crictl port-forward`.

## Conexões
- [[crictl-pods-ps-inspectp-inspect-depuracao-sandboxes-containers]] — Veja também: crictl: Inspeção de Pod Sandboxes e Containers nos Nós (pods, ps, inspectp e inspect).
- [[crictl-images-pull-rmi-inspecti-imagefsinfo-gestao-disco]] — Veja também: crictl: Gestão de Imagens e Diagnóstico de Disco no Nó (images, inspecti, imagefsinfo, pull e rmi).

## Fontes
- [cri-tools Official Documentation — docs/crictl.md (CRI CLI Commands, /etc/crictl.yaml, runtime-endpoint, stats/statsp/metricsp, checkpoint & OpenTelemetry Tracing)](https://raw.githubusercontent.com/kubernetes-sigs/cri-tools/master/docs/crictl.md) — Guia oficial completo do crictl detalhando todos os subcomandos de PodSandbox, containers, imagens e métricas CRI, configuração de /etc/crictl.yaml e flags de tracing/timeout; consultado em 2026-10-03.
- [kubernetes-sigs/cri-tools GitHub — README.md (Project Scope, Kubernetes Version Compatibility Matrix, crictl & critest Installation)](https://raw.githubusercontent.com/kubernetes-sigs/cri-tools/master/README.md) — README oficial do kubernetes-sigs/cri-tools explicando o escopo do crictl e do critest e a matriz de compatibilidade de versões minor com o Kubernetes; consultado em 2026-10-03.
- [Kubernetes SIG Node cri-tools — Official GitHub Repository](https://github.com/kubernetes-sigs/cri-tools) — Repositório oficial Apache-2.0 do cri-tools; consultado em 2026-10-03.
