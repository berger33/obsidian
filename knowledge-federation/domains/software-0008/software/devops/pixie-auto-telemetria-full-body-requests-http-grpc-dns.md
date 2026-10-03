---
id: software.devops.tranche14.001302
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
fontes: ["https://raw.githubusercontent.com/pixie-io/pixie/main/README.md", "https://docs.px.dev/about-pixie/what-is-pixie/", "https://github.com/pixie-io/pixie"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Pixie: Auto-Telemetria eBPF de Requisições Full-Body (HTTP, gRPC e DNS) sem Sidecars

## Em uma frase
Por meio de probes eBPF no kernel Linux (`kprobes` e `uprobes` sobre bibliotecas TLS como OpenSSL e runtime Go), o Pixie captura automaticamente requisições e respostas **full-body** (cabeçalhos e payload completo) de protocolos de aplicação como HTTP, HTTP/2, gRPC e DNS.

## Por que importa
Quando uma chamada entre dois microsserviços falha esporadicamente com `HTTP 500` ou `gRPC Internal`, métricas agregadas mostram apenas a taxa de erro, sem revelar qual payload JSON ou query string causou a falha.

## Como funciona
Os agentes PEM interceptam as chamadas de sistema de leitura/escrita de sockets e funções de criptografia TLS no espaço de usuário/kernel, correlacionam os pacotes com os metadados de Pod/Service/Namespace do Kubernetes e expõem as requisições completas em tabelas consultáveis como `http_events` e `dns_events`.

## Exemplo
```bash
# Consultar requisicoes HTTP capturadas em tempo real no cluster via CLI px:
px run px/http_data
px run px/dns_data
```

## Limites e trade-offs
A captura full-body em memória local opera como um buffer circular nos PEMs; portanto, dados brutos antigos são sobrescritos conforme novas requisições chegam se não forem exportados via plugin OpenTelemetry.

## Como verificar
Utilize scripts como `px/http_data` durante incidentes ativos para inspecionar payloads de erro em tempo real sem precisar reiniciar Pods em modo debug.

## Conexões
- [[pixie-arquitetura-ebpf-pem-vizier-pixie-cloud-cncf]] — Veja também: Pixie: Arquitetura de Observabilidade eBPF (PEM, Vizier e Pixie Cloud) na CNCF.
- [[pixie-pxl-query-language-pythonic-dataframes-scripts]] — Veja também: Pixie: Linguagem de Consulta PxL (Pixie Language) Baseada em DataFrames Pythonicos.

## Fontes
- [Pixie Official Documentation — Pixie Overview & Architecture (PEM, Vizier, Pixie Cloud, CLI & eBPF Auto-Telemetry)](https://raw.githubusercontent.com/pixie-io/pixie/main/README.md) — Visão geral e arquitetura oficial do Pixie detalhando o Pixie Edge Module (PEM), Vizier, Pixie Cloud, coleta eBPF sem instrumentação manual e linguagem PxL; consultado em 2026-10-03.
- [Pixie GitHub — README.md (Network Monitoring, Service Performance, Database Query Profiling, Continuous Profiling, bpftrace & Dynamic Go Logging)](https://docs.px.dev/about-pixie/what-is-pixie/) — README oficial do pixie-io/pixie (CNCF Sandbox) documentando casos de uso de monitoramento de rede/DNS/TCP drops, profiling de queries SQL, Flame Graphs, bpftrace distribuído e Dynamic Go Logging; consultado em 2026-10-03.
- [Pixie — Official GitHub Repository](https://github.com/pixie-io/pixie) — Repositório oficial do Pixie na CNCF; consultado em 2026-10-03.
