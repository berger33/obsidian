---
id: software.devops.tranche05.000409
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-05.md"
fontes: ["https://raw.githubusercontent.com/grafana/tempo/main/README.md", "https://grafana.com/docs/tempo/latest/getting-started/", "https://github.com/grafana/tempo"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Operações administrativas e inspeção de blocos de armazenamento com tempo-cli

## Em uma frase
Ao lado do `tempo-vulture`, o README oficial destaca o **`tempo-cli`** (`github.com/grafana/tempo/tree/main/cmd/tempo-cli`, documentado em `grafana.com/docs/tempo/latest/operations/tempo_cli/`) como o utilitário de linha de comando oficial que concentra todas as funcionalidades administrativas, de diagnóstico e de manutenção relacionadas ao Tempo. Com o `tempo-cli`, operadores podem listar e inspecionar blocos de traces diretamente no bucket de object storage, analisar metadados de compactação, depurar arquivos Parquet e verificar o estado interno do backend fora do fluxo normal de consultas HTTP.

## Por que importa
Quando ocorre um problema de custo inesperado de armazenamento, crescimento anormal de blocos ou lentidão em uma janela específica de tempo no bucket S3/GCS, inspecionar os blocos diretamente pelo `tempo-cli` permite auditar tamanhos, contagens de spans e níveis de compactação sem sobrecarregar os queriers de produção.

## Como funciona
Inclua o binário `tempo-cli` nas caixas de ferramentas (jumpboxes/pods de manutenção) dos operadores de observabilidade para auditoria de buckets, depuração de blocos Parquet e diagnóstico operacional descrito em `operations/tempo_cli/`.

## Exemplo
Para investigar por que o tamanho do bucket dobrou após o deploy de um novo microsserviço, o engenheiro utiliza o `tempo-cli` para inspecionar as estatísticas dos blocos recentes e identifica um serviço emitindo spans com atributos de payload gigante.

## Limites e trade-offs
Conceda ao `tempo-cli` credenciais somente-leitura ao bucket de produção durante operações de diagnóstico e inspeção, restringindo permissões de escrita/exclusão de objetos apenas a procedimentos de manutenção aprovados.

## Como verificar
Execute `tempo-cli` apontando para um bucket ou diretório de blocos de teste e confirme a listagem e leitura dos metadados dos blocos do Tempo.

## Conexões
- [[tempo-tempo-vulture-consistency-checking-tool]] — Veja também: Monitoramento contínuo de consistência de ponta a ponta com tempo-vulture.
- [[tempo-agplv3-licensing-and-grafana-ui-issue-routing]] — Veja também: Licenciamento AGPL-3.0-only, exceções em LICENSING.md e roteamento de issues de UI para o Grafana.

## Fontes
- [Grafana Tempo GitHub — README.md (Object Storage Tracing, Traces Drilldown, TraceQL & Apache Parquet)](https://raw.githubusercontent.com/grafana/tempo/main/README.md) — README oficial do Grafana Tempo detalhando operação exclusiva sobre armazenamento de objetos (S3, GCS, Azure ou disco local), integração com Grafana/Prometheus/Loki, app Traces Drilldown, linguagem TraceQL e TraceQL metrics, formato padrão Apache Parquet (Tempo 2.0), compatibilidade OpenTelemetry/Jaeger/Zipkin/Kafka e utilitários tempo-vulture e tempo-cli.; consultado em 2026-10-03.
- [Grafana Tempo Documentation — Getting Started](https://grafana.com/docs/tempo/latest/getting-started/) — Guia oficial de início rápido e operação do Grafana Tempo.; consultado em 2026-10-03.
- [Grafana Tempo — Official GitHub Repository](https://github.com/grafana/tempo) — Repositório oficial do Grafana Tempo distribuído sob AGPL-3.0-only (com exceções Apache-2.0 em LICENSING.md).; consultado em 2026-10-03.
