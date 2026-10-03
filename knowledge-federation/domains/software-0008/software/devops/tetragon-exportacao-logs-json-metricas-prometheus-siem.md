---
id: software.devops.tranche07.000630
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
fontes: ["https://raw.githubusercontent.com/cilium/tetragon/main/README.md", "https://tetragon.io/docs/overview/", "https://github.com/cilium/tetragon"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Cilium Tetragon: exportação de eventos JSON com rotação, filtros de exportação e métricas Prometheus

## Em uma frase
O Cilium Tetragon exporta eventos de segurança estruturados em JSON (para stdout/arquivos com rotação e filtros de allowlist/denylist) e métricas operacionais e de políticas para o Prometheus.

## Por que importa
Para que a observabilidade em eBPF alimente pipelines corporativos de detecção e resposta (SIEM, SOAR, Grafana Loki, Elasticsearch ou Splunk) sem saturar a rede nem o armazenamento de logs, o agente precisa filtrar, rotacionar e exportar os eventos de forma estruturada e expor métricas de saúde do próprio subsistema eBPF. Conforme a documentação oficial do Tetragon, o componente integra-se nativamente a sistemas de métricas, logging e tracing.

## Como funciona
No DaemonSet do Kubernetes, o pod do Tetragon escreve os eventos de segurança em um arquivo JSON rotacionado (por exemplo, `/var/run/tetragon/tetragon.log`) e utiliza um container sidecar leve (`export-stdout`) para transmitir esse fluxo ao `stdout` do pod, onde coletores padrão como Fluent Bit, Vector ou Grafana Alloy podem coletá-lo e enviá-lo ao SIEM/Loki. Para controlar o volume de dados exportados, o administrador configura listas de permissão (`exportAllowList`) e de bloqueio (`exportDenyList`) baseadas em tipos de evento, namespaces, nomes de binários ou expressões regulares. Simultaneamente, o Tetragon expõe um endpoint `/metrics` para o Prometheus contendo contadores de eventos por tipo, estatísticas de erros ou perdas em mapas/ring buffers eBPF e contadores de ações de enforcement (`Sigkill`/`Override`) disparadas por `TracingPolicy`.

## Exemplo
```yaml
# Trecho de values.yaml do Helm chart do Tetragon configurando filtros de exportação e métricas Prometheus
tetragon:
  prometheus:
    enabled: true
    port: 2112
  exportAllowList: |-
    {"event_set":["PROCESS_EXEC","PROCESS_EXIT","PROCESS_KPROBE"]}
  exportDenyList: |-
    {"health_check":true}
    {"namespace":["", "kube-system"]}
```

## Limites e trade-offs
Embora os filtros `exportAllowList` e `exportDenyList` reduzam drasticamente o volume de logs JSON gravados em disco e enviados à rede (economizando custos de ingestão no SIEM), a filtragem de exportação ocorre no agente em user space; para eventos de altíssima frequência (como syscalls de leitura/escrita ou pacotes), o filtro principal deve sempre ser definido dentro dos `selectors` da `TracingPolicy` para que o descarte ocorra no próprio eBPF no kernel.

## Como verificar
Consulte o endpoint de métricas do Tetragon (`curl -s http://localhost:2112/metrics | grep tetragon_`) para verificar contadores de eventos processados e confirme nos logs do container `export-stdout` que eventos de health check ou namespaces excluídos na `exportDenyList` não estão sendo emitidos.

## Conexões
- [[tetragon-implantacao-kubernetes-linux-docker-standalone]] — Veja também: Cilium Tetragon: implantação em Kubernetes (DaemonSet) e em hosts Linux via Docker ou pacotes nativos.
- [[tetragon-ebpf-observabilidade-seguranca-runtime-enforcement]] — Referência cruzada direta com tetragon-ebpf-observabilidade-seguranca-runtime-enforcement.
- [[tetragon-tetra-cli-inspecao-eventos-filtros-kubernetes]] — Referência cruzada direta com tetragon-tetra-cli-inspecao-eventos-filtros-kubernetes.

## Fontes
- [Cilium Tetragon GitHub — README.md (Process Lifecycle, TracingPolicy & Tetra CLI)](https://raw.githubusercontent.com/cilium/tetragon/main/README.md) — README oficial do Cilium Tetragon cobrindo eventos process_exec/process_exit, rastreamento genérico com kprobes/tracepoints/uprobes via TracingPolicy e casos de uso em Kubernetes e Linux; consultado em 2026-10-03.
- [Cilium Tetragon Official Documentation — Overview & eBPF Real-Time Enforcement](https://tetragon.io/docs/overview/) — Visão geral técnica do Cilium Tetragon detalhando filtragem e bloqueio síncrono em eBPF dentro do kernel Linux e enriquecimento com identidades do Kubernetes; consultado em 2026-10-03.
- [Cilium Tetragon — Official GitHub Repository](https://github.com/cilium/tetragon) — Repositório oficial do Cilium Tetragon na CNCF; consultado em 2026-10-03.
