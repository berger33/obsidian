---
id: software.devops.tranche02.000187
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
fontes: ["https://raw.githubusercontent.com/vectordotdev/vector/master/README.md", "https://vector.dev/docs/setup/quickstart/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Modelo declarativo do pipeline: coleta em sources, processamento em transforms e entrega em sinks

## Em uma frase
O README oficial organiza toda a navegação da ferramenta em torno dos três blocos de construção do grafo de dados do Vector: **Collect (`sources`)**, **Transform (`transforms`)** e **Route (`sinks`)**, com o catálogo unificado de integrações disponível em `vector.dev/components/`.

## Por que importa
Modelar o pipeline como um grafo acíclico direcionado (DAG) explícito entre `sources`, `transforms` e `sinks` torna visível de onde cada evento vem, quais transformações sofreu e para quais destinos é roteado.

## Como funciona
Conecte os identificadores de entrada (`inputs`) de cada `transform` e `sink` de forma modular, permitindo que uma única fonte alimente múltiplas rotas independentes (por exemplo, uma rota de métricas agregadas e outra de armazenamento de logs).

## Exemplo
Um pipeline recebe eventos de contêineres na `source`, aplica parsing e enriquecimento em uma `transform` e bifurca a saída para dois `sinks`: Grafana Loki para investigação interativa e Object Storage para retenção de conformidade.

## Limites e trade-offs
Evite criar cadeias excessivamente longas de `transforms` redundantes quando as operações puderem ser consolidadas em um único passo de transformação bem testado.

## Como verificar
Conferi a seção What is Vector? e os links de cabeçalho no README oficial de `vectordotdev/vector`.

## Conexões
- [[vector-correctness-tests-disk-buffer-logrotate-sighup]] — Veja também: Testes de corretude: persistência de buffer em disco, rotação de arquivos, truncamento, SIGHUP e JSON.
- [[vector-ci-workflows-nightly-integration-component-features]] — Veja também: Verificação contínua no repositório: Nightly, Integration/E2E Test Suite e Component Features.

## Fontes
- [Vector — GitHub README](https://raw.githubusercontent.com/vectordotdev/vector/master/README.md) — Visão geral do Vector (pipeline de observabilidade em Rust para agent e aggregator), princípios, 5 casos de uso, escala na comunidade (500 TB/dia) e tabelas de performance e corretude.; consultado em 2026-10-03.
- [Vector Documentation — Quickstart & Components](https://vector.dev/docs/setup/quickstart/) — Documentação oficial do Vector para configuração de sources, transforms e sinks referenciada no README.; consultado em 2026-10-03.
