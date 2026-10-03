---
id: software.devops.tranche07.000637
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

# Inspektor Gadget: coleta e exportação declarativa de métricas e logs eBPF para OpenTelemetry e Prometheus

## Em uma frase
O Inspektor Gadget permite coletar dados de baixo nível do kernel com eBPF e exportá-los continuamente para ferramentas de observabilidade (OpenTelemetry, Prometheus, JSON) via linha de comando ou arquivos de configuração declarativos.

## Por que importa
Usar o Inspektor Gadget apenas em sessões interativas de terminal ajuda durante o troubleshooting manual, mas não preserva métricas históricas de latência de rede, I/O de disco ou eventos de segurança para correlação em dashboards e alertas. Conforme destacado na lista de recursos do README oficial do Inspektor Gadget, o framework suporta exportar dados coletados pelos Gadgets para ferramentas de observabilidade com um comando simples ou via configuração declarativa (modo headless/manifesto).

## Como funciona
Os operadores de exportação do Inspektor Gadget (como os operadores de métricas e logs OpenTelemetry / Prometheus) mapeiam os campos estruturados produzidos pelos mapas e buffers eBPF de um Gadget para métricas (contadores, gauges, histogramas) ou registros de log OTLP. O operador de plataforma pode definir um manifesto YAML declarativo especificando quais imagens OCI de Gadgets devem rodar continuamente em segundo plano, quais filtros de enriquecimento aplicar e para qual endpoint OTLP (`otel-metrics` / `otel-logs`) ou scrape endpoint Prometheus os dados devem ser exportados, transformando qualquer Gadget em um coletor permanente de telemetria eBPF.

## Exemplo
```bash
# Executar um Gadget exportando eventos diretamente em formato JSON estruturado para integração com pipelines de log
kubectl gadget run trace_exec:latest -A -o json
```

## Limites e trade-offs
Ao exportar métricas de Gadgets eBPF para o Prometheus ou OpenTelemetry, incluir campos de alta cardinalidade do evento (como números de PID efêmeros, portas de origem aleatórias ou caminhos completos de arquivos temporários) como atributos/rótulos de métrica causará explosão de séries temporais no banco de métricas (como Prometheus ou Mimir); apenas rótulos limitados (como `k8s.namespace`, `k8s.podName`, código de erro ou operação) devem ser mapeados para dimensões de métricas.

## Como verificar
Execute um Gadget com saída estruturada (`-o json` ou configuração de exportação OTel) e valide que cada registro emitido contém os atributos de enriquecimento Kubernetes e os campos tipados do evento eBPF.

## Conexões
- [[inspektor-catalogo-gadgets-trace-top-snapshot-profile]] — Veja também: Inspektor Gadget: catálogo de Gadgets para rastreamento (trace), top consumidores, snapshots e profiling.
- [[inspektor-seguranca-verificacao-assinaturas-sbom-restricao-gadgets]] — Veja também: Inspektor Gadget: verificação de assinaturas de imagens OCI, SBOMs e restrição de Gadgets permitidos.
- [[inspektor-framework-ebpf-inspecao-kubernetes-linux]] — Referência cruzada direta com inspektor-framework-ebpf-inspecao-kubernetes-linux.
- [[inspektor-webassembly-wasm-pos-processamento-operadores]] — Referência cruzada direta com inspektor-webassembly-wasm-pos-processamento-operadores.

## Fontes
- [Inspektor Gadget GitHub — README.md (OCI Gadgets, Enrichment, WASM & Operations)](https://raw.githubusercontent.com/inspektor-gadget/inspektor-gadget/main/README.md) — README oficial do Inspektor Gadget detalhando empacotamento de programas eBPF em imagens OCI, enriquecimento bidirecional Kubernetes, módulos WebAssembly, operadores e requisitos de kernel Linux >= 5.10 com BTF; consultado em 2026-10-03.
- [Inspektor Gadget Official Documentation — Gadgets Catalog & Reference](https://www.inspektor-gadget.io/docs/latest/gadgets/) — Documentação oficial dos Gadgets (trace, top, snapshot, profile) e modos de execução com kubectl-gadget, ig e gadgetctl; consultado em 2026-10-03.
- [Inspektor Gadget — Official GitHub Repository](https://github.com/inspektor-gadget/inspektor-gadget) — Repositório oficial do Inspektor Gadget na CNCF; consultado em 2026-10-03.
