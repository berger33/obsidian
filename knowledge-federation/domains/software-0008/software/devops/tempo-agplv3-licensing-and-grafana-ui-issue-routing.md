---
id: software.devops.tranche05.000410
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

# Licenciamento AGPL-3.0-only, exceções em LICENSING.md e roteamento de issues de UI para o Grafana

## Em uma frase
As seções *Getting help* e *License* do README oficial estabelecem duas diretrizes importantes de governança: (1) o Grafana Tempo é distribuído sob a licença **`AGPL-3.0-only`** (`LICENSE`), existindo exceções específicas sob Apache-2.0 detalhadas no arquivo `LICENSING.md`; e (2) bugs, problemas e sugestões de funcionalidades do backend devem ser abertos em `github.com/grafana/tempo/issues/new/choose` (com suporte comunitário no fórum `community.grafana.com/c/grafana-tempo/40` e no canal `#tempo` do Slack do Grafana), enquanto **problemas de interface gráfica (UI issues) devem ser abertos diretamente no repositório do Grafana** (`github.com/grafana/grafana/issues/new/choose`).

## Por que importa
Equipes de conformidade jurídica e open-source precisam distinguir claramente componentes sob `AGPL-3.0-only` (como o Tempo atual) de componentes sob Apache-2.0 na matriz de licenças da empresa, e engenheiros precisam saber onde reportar bugs de visualização de traces (repositório `grafana/grafana`) versus bugs de ingestão/TraceQL (repositório `grafana/tempo`).

## Como funciona
Registre a licença `AGPL-3.0-only` e as exceções de `LICENSING.md` no inventário de governança ao adotar o Grafana Tempo, e direcione issues de visualização no navegador para `grafana/grafana` e issues de motor de busca/armazenamento para `grafana/tempo`.

## Exemplo
Ao encontrar um bug visual na renderização do gráfico de flamegraph de um trace no navegador, o desenvolvedor verifica que o JSON retornado pela API do Tempo está correto e abre a issue diretamente em `grafana/grafana` conforme orientado no README do Tempo.

## Limites e trade-offs
Não presuma que todos os projetos do ecossistema Grafana possuem a mesma licença; verifique sempre os arquivos `LICENSE` e `LICENSING.md` de cada repositório ao empacotar ou redistribuir componentes.

## Como verificar
Consulte os arquivos `LICENSE` e `LICENSING.md` na raiz do repositório `grafana/tempo` para validar os termos de licenciamento aplicáveis ao seu cenário de uso.

## Conexões
- [[tempo-tempo-cli-operations-and-block-inspection]] — Veja também: Operações administrativas e inspeção de blocos de armazenamento com tempo-cli.

## Fontes
- [Grafana Tempo GitHub — README.md (Object Storage Tracing, Traces Drilldown, TraceQL & Apache Parquet)](https://raw.githubusercontent.com/grafana/tempo/main/README.md) — README oficial do Grafana Tempo detalhando operação exclusiva sobre armazenamento de objetos (S3, GCS, Azure ou disco local), integração com Grafana/Prometheus/Loki, app Traces Drilldown, linguagem TraceQL e TraceQL metrics, formato padrão Apache Parquet (Tempo 2.0), compatibilidade OpenTelemetry/Jaeger/Zipkin/Kafka e utilitários tempo-vulture e tempo-cli.; consultado em 2026-10-03.
- [Grafana Tempo Documentation — Getting Started](https://grafana.com/docs/tempo/latest/getting-started/) — Guia oficial de início rápido e operação do Grafana Tempo.; consultado em 2026-10-03.
- [Grafana Tempo — Official GitHub Repository](https://github.com/grafana/tempo) — Repositório oficial do Grafana Tempo distribuído sob AGPL-3.0-only (com exceções Apache-2.0 em LICENSING.md).; consultado em 2026-10-03.
