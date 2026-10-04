---
id: software.devops.tranche07.000620
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

# Grafana Pyroscope: uso proativo e reativo de continuous profiling para otimizar CPU, memória e I/O

## Em uma frase
O Grafana Pyroscope atende tanto casos de uso proativos (redução contínua de CPU/memória e prevenção de latência) quanto reativos (resolução de incidentes em produção com detalhe em nível de linha de código).

## Por que importa
Ferramentas tradicionais de APM (traces) mostram qual requisição HTTP ou chamada RPC demorou, e métricas mostram que o uso de CPU de um pod subiu para 95%, mas nenhuma das duas revela qual função interna, expressão regular ou alocação em loop está consumindo os ciclos de processador. Conforme o README oficial do Grafana Pyroscope, o continuous profiling preenche essa lacuna fornecendo visibilidade contínua sobre o comportamento interno do código em produção.

## Como funciona
No fluxo **proativo**, equipes de engenharia analisam flame graphs agregados ao longo de dias ou semanas para identificar as funções mais quentes (top CPU consumers, maiores alocadores de memória heap ou pontos de bloqueio de I/O) em toda a frota, priorizando refatorações que reduzem diretamente a conta de computação em nuvem e previnem degradações de latência em horários de pico. No fluxo **reativo**, durante um incidente ativo de alta utilização de CPU, vazamento de memória (memory leak) ou contenção de threads, o engenheiro de plantão abre o Grafana Profiles Drilldown na janela exata do alerta e inspeciona o flame graph até o nível da linha de código que originou a anomalia, sem precisar reproduzir o problema localmente nem anexar um profiler manual ao container em crise.

## Exemplo
```bash
# Expor e coletar perfis de CPU de 30 segundos de um serviço Go instrumentado para análise no Pyroscope
curl -s "http://localhost:4040/ready"

# Exemplo de verificação de endpoint pprof local que o Grafana Alloy coleta continuamente para o Pyroscope
curl -s http://localhost:6060/debug/pprof/profile?seconds=5 > cpu.pprof
```

## Limites e trade-offs
Para que o profiling contínuo seja seguro em produção 24x7, os profilers utilizam amostragem estatística de baixo overhead (tipicamente 1% a 2% de CPU, como 100 Hz para amostras de pilha de CPU); isso significa que funções ultrarrápidas executadas raramente podem não aparecer nas amostras estatísticas, sendo o continuous profiling ideal para gargalos sistêmicos de recursos e não um substituto para tracing distribuído de transações individuais.

## Como verificar
Compare o flame graph de um serviço antes e depois de uma otimização de código usando a funcionalidade de comparação (diff) no Grafana Profiles Drilldown e valide a queda correspondente na largura da função otimizada e na métrica de CPU do pod.

## Conexões
- [[pyroscope-migracao-v1-para-v2-sem-perda-dados]] — Veja também: Grafana Pyroscope: migração da arquitetura v1 (ingesters com disco) para v2 (object storage direto).
- [[pyroscope-continuous-profiling-arquitetura-v2-object-storage]] — Referência cruzada direta com pyroscope-continuous-profiling-arquitetura-v2-object-storage.
- [[pyroscope-coleta-perfis-sdks-grafana-alloy-opentelemetry-ebpf]] — Referência cruzada direta com pyroscope-coleta-perfis-sdks-grafana-alloy-opentelemetry-ebpf.
- [[pyroscope-grafana-profiles-drilldown-exploracao-queryless]] — Referência cruzada direta com pyroscope-grafana-profiles-drilldown-exploracao-queryless.

## Fontes
- [Grafana Pyroscope GitHub — README.md (Pyroscope 2.0, SDKs, Alloy & Profiles Drilldown)](https://raw.githubusercontent.com/grafana/pyroscope/main/README.md) — README oficial do Grafana Pyroscope 2.0 detalhando casos de uso proativos e reativos, coleta via SDKs/Grafana Alloy/OpenTelemetry eBPF e visualização no Grafana Profiles Drilldown; consultado em 2026-10-03.
- [Grafana Pyroscope Documentation — About the Pyroscope v2 architecture](https://grafana.com/docs/pyroscope/latest/reference-pyroscope-v2-architecture/about-pyroscope-v2-architecture.md) — Documentação oficial da arquitetura Pyroscope v2 com escrita direta em object storage via distributor e segment-writer, consenso Raft no metastore, compaction-workers e query-frontend/query-backend; consultado em 2026-10-03.
- [Grafana Pyroscope — Official GitHub Repository](https://github.com/grafana/pyroscope) — Repositório oficial AGPL-3.0 do Grafana Pyroscope; consultado em 2026-10-03.
