---
id: software.devops.tranche07.000616
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
fontes: ["https://raw.githubusercontent.com/grafana/pyroscope/main/README.md", "https://grafana.com/docs/pyroscope/latest/reference-pyroscope-v2-architecture/", "https://github.com/grafana/pyroscope"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Grafana Pyroscope: visualização e análise sem consultas com Grafana Profiles Drilldown

## Em uma frase
O Grafana Profiles Drilldown (anteriormente Explore Profiles) fornece uma experiência visual queryless no Grafana para explorar perfis de CPU, memória e I/O e comparar flame graphs entre janelas e versões.

## Por que importa
Diferentemente de métricas e logs, muitos engenheiros de software não dominam sintaxes específicas de consulta de perfis e precisam encontrar rapidamente qual função ou linha de código causou uma regressão de CPU após um deploy. De acordo com o README oficial do Grafana Pyroscope, o Grafana Profiles Drilldown vem pré-instalado no Grafana Cloud e no Grafana OSS como a forma padrão e intuitiva de visualizar e analisar dados de profiling sem precisar escrever queries.

## Como funciona
Conectado a uma fonte de dados Pyroscope, o aplicativo Grafana Profiles Drilldown descobre automaticamente todos os serviços instrumentados, tipos de perfil disponíveis (CPU time, memory allocations, in-use space, goroutines, mutex contention) e rótulos de metadados (`namespace`, `pod`, `version`, `region`). O usuário navega visualmente selecionando o serviço e o tipo de perfil, filtra por rótulos com cliques, inspeciona séries temporais de consumo ao lado do flame graph correspondente, foca em funções específicas (top table / flame graph) e utiliza a visão de diff para comparar o comportamento de duas versões de código ou dois intervalos de tempo lado a lado.

## Exemplo
```bash
# Subir ambiente local com Pyroscope na porta 4040 para inspeção imediata no Grafana Profiles Drilldown
brew install pyroscope-io/brew/pyroscope
brew services start pyroscope

# Validar que a porta HTTP 4040 do Pyroscope está pronta para conexão como Data Source no Grafana
curl -I http://localhost:4040/ready
```

## Limites e trade-offs
Para que a exploração no Grafana Profiles Drilldown permita comparar versões de deploy ou isolar pods problemáticos sem ruído, os clientes de instrumentação (SDKs ou Grafana Alloy) devem anexar rótulos estáticos de baixa cardinalidade (como `service_git_ref`, `version`, `namespace`, `env`); anexar rótulos de cardinalidade ilimitada (como `request_id` ou `user_id` diretamente como tags de série de perfil) fragmenta os segmentos e degrada a agregação visual.

## Como verificar
Abra o Grafana, acesse a seção **Drilldown > Profiles** (ou Explore Profiles), selecione o datasource do Pyroscope e confirme a renderização interativa dos gráficos de série temporal e dos flame graphs por serviço.

## Conexões
- [[pyroscope-coleta-perfis-sdks-grafana-alloy-opentelemetry-ebpf]] — Veja também: Grafana Pyroscope: instrumentação e coleta de perfis via SDKs, Grafana Alloy e OpenTelemetry eBPF Profiler.
- [[pyroscope-formatos-bloco-indice-metadados-distribuicao-dados]] — Veja também: Grafana Pyroscope v2: formato de blocos, distribuição adaptativa de dados e índice de metadados.
- [[pyroscope-continuous-profiling-arquitetura-v2-object-storage]] — Referência cruzada direta com pyroscope-continuous-profiling-arquitetura-v2-object-storage.
- [[pyroscope-caminho-leitura-query-frontend-backend-flame-graphs]] — Referência cruzada direta com pyroscope-caminho-leitura-query-frontend-backend-flame-graphs.

## Fontes
- [Grafana Pyroscope GitHub — README.md (Pyroscope 2.0, SDKs, Alloy & Profiles Drilldown)](https://raw.githubusercontent.com/grafana/pyroscope/main/README.md) — README oficial do Grafana Pyroscope 2.0 detalhando casos de uso proativos e reativos, coleta via SDKs/Grafana Alloy/OpenTelemetry eBPF e visualização no Grafana Profiles Drilldown; consultado em 2026-10-03.
- [Grafana Pyroscope Documentation — About the Pyroscope v2 architecture](https://grafana.com/docs/pyroscope/latest/reference-pyroscope-v2-architecture/) — Documentação oficial da arquitetura Pyroscope v2 com escrita direta em object storage via distributor e segment-writer, consenso Raft no metastore, compaction-workers e query-frontend/query-backend; consultado em 2026-10-03.
- [Grafana Pyroscope — Official GitHub Repository](https://github.com/grafana/pyroscope) — Repositório oficial AGPL-3.0 do Grafana Pyroscope; consultado em 2026-10-03.
