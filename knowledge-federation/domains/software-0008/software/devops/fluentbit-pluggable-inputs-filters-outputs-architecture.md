---
id: software.devops.tranche02.000174
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-02.md"
fontes: ["https://raw.githubusercontent.com/fluent/fluent-bit/master/README.md", "https://docs.fluentbit.io/manual/pipeline/inputs"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Arquitetura modular plugável com mais de 70 plugins de Inputs, Filters e Outputs

## Em uma frase
As seções `Key Features` e `Plugins: Inputs, Filters, Outputs` do README explicam que o Fluent Bit é totalmente modular e conta com **mais de 70 plugins embutidos** (`70+ built-in plugins`) divididos em três estágios do pipeline: **Input Plugins** (`manual/pipeline/inputs`, para coletar logs, métricas e traces), **Filter Plugins** (`manual/pipeline/filters`, para enriquecer e transformar dados, como adicionar metadados de pods Kubernetes ou filtrar registros) e **Output Plugins** (`manual/pipeline/outputs`, para entregar dados a serviços externos).

## Por que importa
Estruturar o agente em Inputs, Filters e Outputs desacoplados permite que um único evento coletado no nó seja parseado, enriquecido com metadados do Kubernetes, filtrado de dados sensíveis e roteado simultaneamente para múltiplos destinos.

## Como funciona
Desenhe seus arquivos de configuração do Fluent Bit separando claramente as fontes (`Input`), as transformações e enriquecimentos (`Filter`) e os destinos (`Output`) consultando o catálogo oficial de plugins em `docs.fluentbit.io`.

## Exemplo
Um DaemonSet usa um plugin de Input para ler arquivos de log dos contêineres, um Filter para enriquecer com labels do pod no Kubernetes e dois Outputs para enviar os logs ao Grafana Loki e a um bucket de arquivamento.

## Limites e trade-offs
Filtros pesados de expressões regulares mal escritas aplicados a milhões de linhas por segundo podem aumentar o uso de CPU; teste e simplifique os filtros do pipeline.

## Como verificar
Conferi as seções Key Features e Plugins: Inputs, Filters, Outputs no README oficial de `fluent/fluent-bit`.

## Conexões
- [[fluentbit-release-cadence-v5-1-and-maintenance-policy]] — Veja também: Cadência de releases maiores a cada 3–4 meses, série v5.1 e guia MAINTENANCE.md.
- [[fluentbit-sql-stream-processing-analytics]] — Veja também: Processamento de streams com consultas SQL para análise e transformação em trânsito.

## Fontes
- [Fluent Bit — GitHub README](https://raw.githubusercontent.com/fluent/fluent-bit/master/README.md) — Visão geral do Fluent Bit (agente graduado na CNCF para Logs, Metrics e Traces), suporte multi-plataforma, ciclo de 3–4 meses (v5.1), 70+ plugins, SQL Stream Processing, extensibilidade C/Lua/Go e build CMake.; consultado em 2026-10-03.
- [Fluent Bit Official Documentation — Pipeline Inputs, Filters & Outputs](https://docs.fluentbit.io/manual/pipeline/inputs) — Documentação oficial dos plugins de Input, Filter e Output e guias de instalação do Fluent Bit.; consultado em 2026-10-03.
