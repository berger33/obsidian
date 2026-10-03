---
id: software.devops.tranche07.000636
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
fontes: ["https://raw.githubusercontent.com/inspektor-gadget/inspektor-gadget/main/README.md", "https://www.inspektor-gadget.io/docs/latest/gadgets/", "https://github.com/inspektor-gadget/inspektor-gadget"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Inspektor Gadget: catálogo de Gadgets para rastreamento (trace), top consumidores, snapshots e profiling

## Em uma frase
O catálogo de Gadgets do Inspektor Gadget (hospedado na árvore `/gadgets` e no Artifact Hub) abrange ferramentas de `trace` (DNS, TCP, exec, open, mount), `top` (arquivos, bloco, rede), `snapshot` (processos, sockets) e `profile`.

## Por que importa
Em vez de escrever código C eBPF do zero durante uma indisponibilidade em produção, equipes de SRE e DevOps precisam de um canivete suíço de ferramentas prontas e testadas que cubram os principais subsistemas do kernel Linux (rede, sistema de arquivos, processos, memória e escalonador). Segundo a documentação oficial do Inspektor Gadget, muitos dos Gadgets in-tree evoluíram dos clássicos utilitários BCC (BPF Compiler Collection) e `cilium/ebpf`, adaptados para o modelo de imagens OCI enriquecidas com Kubernetes.

## Como funciona
Os Gadgets são organizados por padrão de observação: (1) **`trace_*`** (como `trace_open`, `trace_exec`, `trace_dns`, `trace_tcp`, `trace_mount`, `trace_oomkill`, `trace_signal`) emitem um fluxo contínuo de eventos cada vez que a ação ocorre no kernel; (2) **`top_*`** (como `top_file`, `top_blockio`, `top_tcp`) agregam contadores em mapas eBPF no kernel e exibem periodicamente os maiores consumidores por pod/container; (3) **`snapshot_*`** (como `snapshot_process`, `snapshot_socket`) utilizam iteradores BPF do kernel para capturar uma fotografia instantânea de todas as tarefas ou sockets ativos; e (4) **`profile_*`** (como `profile_cpu`, `profile_blockio`, `profile_tcprtt`) amostram pilhas ou histogramas de latência para diagnóstico de performance.

## Exemplo
```bash
# Rastrear requisições e respostas DNS em tempo real em todos os namespaces do cluster Kubernetes
kubectl gadget run trace_dns:latest -A

# Capturar um snapshot instantâneo de todos os sockets TCP/UDP abertos nos pods de um namespace
kubectl gadget run snapshot_socket:latest -n producao
```

## Limites e trade-offs
Gadgets da categoria `trace_*` que monitoram eventos de alta frequência (como `trace_open` ou `trace_tcp` em todo o cluster com `-A`) geram fluxo intenso de eventos por segundo; para diagnóstico focado sem ruído, recomenda-se começar com Gadgets agregadores (`top_*` ou `profile_*`) para identificar o pod anômalo e, em seguida, rodar `trace_*` filtrado estritamente por `--podname`.

## Como verificar
Execute `kubectl gadget run snapshot_process:latest -n kube-system` e confirme o retorno imediato da lista de processos em execução dentro dos pods do `kube-system` com seus respectivos PIDs e comandos.

## Conexões
- [[inspektor-modos-operacao-kubectl-gadget-ig-linux-gadgetctl]] — Veja também: Inspektor Gadget: modos de operação com kubectl-gadget, binário ig, kubectl debug node e cliente remoto gadgetctl.
- [[inspektor-exportacao-telemetria-opentelemetry-prometheus-declarativa]] — Veja também: Inspektor Gadget: coleta e exportação declarativa de métricas e logs eBPF para OpenTelemetry e Prometheus.
- [[inspektor-framework-ebpf-inspecao-kubernetes-linux]] — Referência cruzada direta com inspektor-framework-ebpf-inspecao-kubernetes-linux.
- [[inspektor-enriquecimento-kernel-kubernetes-filtragem-ebpf]] — Referência cruzada direta com inspektor-enriquecimento-kernel-kubernetes-filtragem-ebpf.

## Fontes
- [Inspektor Gadget GitHub — README.md (OCI Gadgets, Enrichment, WASM & Operations)](https://raw.githubusercontent.com/inspektor-gadget/inspektor-gadget/main/README.md) — README oficial do Inspektor Gadget detalhando empacotamento de programas eBPF em imagens OCI, enriquecimento bidirecional Kubernetes, módulos WebAssembly, operadores e requisitos de kernel Linux >= 5.10 com BTF; consultado em 2026-10-03.
- [Inspektor Gadget Official Documentation — Gadgets Catalog & Reference](https://www.inspektor-gadget.io/docs/latest/gadgets/) — Documentação oficial dos Gadgets (trace, top, snapshot, profile) e modos de execução com kubectl-gadget, ig e gadgetctl; consultado em 2026-10-03.
- [Inspektor Gadget — Official GitHub Repository](https://github.com/inspektor-gadget/inspektor-gadget) — Repositório oficial do Inspektor Gadget na CNCF; consultado em 2026-10-03.
