---
id: software.devops.tranche07.000615
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
fontes: ["https://raw.githubusercontent.com/grafana/pyroscope/main/README.md", "https://grafana.com/docs/pyroscope/latest/reference-pyroscope-v2-architecture/about-pyroscope-v2-architecture.md", "https://github.com/grafana/pyroscope"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Grafana Pyroscope: instrumentação e coleta de perfis via SDKs, Grafana Alloy e OpenTelemetry eBPF Profiler

## Em uma frase
O Grafana Pyroscope recebe dados de profiling por push direto dos SDKs de linguagens, por pull/push via Grafana Alloy ou via protocolo OTLP a partir do OpenTelemetry eBPF profiler.

## Por que importa
Ambientes políglotas de microsserviços combinam aplicações que podem ser instrumentadas no código-fonte (Go, Java, Python, Ruby, Node.js, .NET, Rust) com binários nativos ou serviços legados onde alterar o código é inviável. Segundo o README oficial do Pyroscope, suportar múltiplos métodos de coleta — SDKs, Grafana Alloy e OTLP/eBPF — permite adotar continuous profiling em todo o cluster sem lacunas de visibilidade.

## Como funciona
Existem três caminhos principais para enviar perfis ao Pyroscope Server: (1) instrumentação com os Pyroscope Language SDKs embutidos na aplicação, que coletam amostras de CPU, alocações de heap, goroutines ou mutexes e fazem push periódico para o servidor; (2) coleta via agente Grafana Alloy rodando no host ou como DaemonSet no Kubernetes, que pode fazer scrape (pull) de endpoints `/debug/pprof` de aplicações Go ou receber perfis via push e encaminhá-los ao Pyroscope; e (3) ingestão nativa sobre OTLP a partir de fontes compatíveis com OpenTelemetry, destacando-se o OpenTelemetry eBPF profiler, que captura pilhas de execução de todo o sistema operacional e containers diretamente no kernel Linux com zero alteração de código.

## Exemplo
```go
// Exemplo de instrumentação push em Golang com o SDK do Grafana Pyroscope
package main

import "github.com/grafana/pyroscope-go"

func main() {
    pyroscope.Start(pyroscope.Config{
        ApplicationName: "servico.pagamentos.api",
        ServerAddress:   "http://pyroscope:4040",
        Tags:            map[string]string{"env": "prod", "region": "sa-east-1"},
        ProfileTypes: []pyroscope.ProfileType{
            pyroscope.ProfileCPU,
            pyroscope.ProfileAllocObjects,
            pyroscope.ProfileAllocSpace,
        },
    })
}
```

## Limites e trade-offs
O profiling via eBPF não exige recompilar nem reiniciar aplicações e cobre código C/C++/Rust/Go/kernel de forma transparente, porém exige privilégios elevados no nó Linux e símbolos de depuração ou frame pointers disponíveis para reconstruir pilhas legíveis; já os SDKs de linguagem fornecem tipos de perfil semânticos específicos do runtime (como alocações de objetos gerenciados, garbage collection e locks), mas exigem atualização de dependências em cada repositório.

## Como verificar
Após configurar o SDK, o Grafana Alloy ou o OpenTelemetry eBPF profiler, verifique na interface do Grafana se o `service_name` ou `ApplicationName` aparece listado com amostras recentes de CPU e memória.

## Conexões
- [[pyroscope-caminho-leitura-query-frontend-backend-flame-graphs]] — Veja também: Grafana Pyroscope v2: caminho de leitura com Query-Frontend, Query-Backend e geração paralela de Flame Graphs.
- [[pyroscope-grafana-profiles-drilldown-exploracao-queryless]] — Veja também: Grafana Pyroscope: visualização e análise sem consultas com Grafana Profiles Drilldown.
- [[pyroscope-continuous-profiling-arquitetura-v2-object-storage]] — Referência cruzada direta com pyroscope-continuous-profiling-arquitetura-v2-object-storage.
- [[pyroscope-caminho-escrita-distributor-segment-writer-metastore]] — Referência cruzada direta com pyroscope-caminho-escrita-distributor-segment-writer-metastore.

## Fontes
- [Grafana Pyroscope GitHub — README.md (Pyroscope 2.0, SDKs, Alloy & Profiles Drilldown)](https://raw.githubusercontent.com/grafana/pyroscope/main/README.md) — README oficial do Grafana Pyroscope 2.0 detalhando casos de uso proativos e reativos, coleta via SDKs/Grafana Alloy/OpenTelemetry eBPF e visualização no Grafana Profiles Drilldown; consultado em 2026-10-03.
- [Grafana Pyroscope Documentation — About the Pyroscope v2 architecture](https://grafana.com/docs/pyroscope/latest/reference-pyroscope-v2-architecture/about-pyroscope-v2-architecture.md) — Documentação oficial da arquitetura Pyroscope v2 com escrita direta em object storage via distributor e segment-writer, consenso Raft no metastore, compaction-workers e query-frontend/query-backend; consultado em 2026-10-03.
- [Grafana Pyroscope — Official GitHub Repository](https://github.com/grafana/pyroscope) — Repositório oficial AGPL-3.0 do Grafana Pyroscope; consultado em 2026-10-03.
