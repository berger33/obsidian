---
id: software.devops.tranche05.000417
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
fontes: ["https://raw.githubusercontent.com/VictoriaMetrics/VictoriaMetrics/master/README.md", "https://docs.victoriametrics.com/victoriametrics/keyconcepts/", "https://github.com/VictoriaMetrics/VictoriaMetrics"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Agregação de stream em tempo real (alternativa ao StatsD) e relabeling de métricas no VictoriaMetrics

## Em uma frase
O README oficial destaca que o VictoriaMetrics oferece **poderosa agregação de stream (powerful stream aggregation)** — podendo ser usado diretamente como uma alternativa moderna ao **StatsD** — bem como capacidades integradas de **relabeling de métricas** e limitação de cardinalidade. Com a agregação de stream na entrada, métricas de alta frequência ou de múltiplas instâncias efêmeras podem ser agregadas em janelas de tempo antes mesmo de serem gravadas individualmente, reduzindo drasticamente o número de séries armazenadas.

## Por que importa
Quando milhares de pods efêmeros ou funções serverless emitem métricas individuais por instância, armazenar cada série bruta com o label `pod_name` multiplica o custo de armazenamento e torna as consultas de soma global mais lentas. A agregação de stream calcula somas, contagens, médias e quantis em fluxo contínuo.

## Como funciona
Configure regras de agregação de stream e relabeling para descartar rótulos efêmeros desnecessários ou pré-agregar métricas de alta cardinalidade na camada de ingestão antes do armazenamento de longo prazo.

## Exemplo
Uma frota de 5.000 workers efêmeros envia contadores de tarefas processadas para o pipeline do VictoriaMetrics; a agregação de stream consolida as métricas por `service` e `region` a cada 30 segundos, reduzindo o total de séries gravadas em 99%.

## Limites e trade-offs
Ao descartar labels de instância individual durante a agregação de stream, mantenha as séries brutas apenas se precisar depurar um host específico, ou envie tanto a série agregada (com retenção longa) quanto a série detalhada (com retenção curta).

## Como verificar
Verifique nas métricas internas de ingestão e no resultado das consultas que as séries agregadas por stream são geradas nos intervalos configurados.

## Conexões
- [[victoria-ram-footprint-and-compression-benchmarks]] — Veja também: Eficiência de memória RAM, compressão de dados (7x a 70x) e controle de alta cardinalidade.
- [[victoria-lts-releases-and-upgrade-procedures]] — Veja também: Lançamentos LTS (Long-Term Support), changelog rápido e procedimento seguro de upgrade.

## Fontes
- [VictoriaMetrics GitHub — README.md (Single-Node & Cluster, MetricsQL, Protocols, Snapshots & Benchmarks)](https://raw.githubusercontent.com/VictoriaMetrics/VictoriaMetrics/master/README.md) — README oficial do VictoriaMetrics detalhando versões Single-node e Cluster sob licença Apache-2.0, armazenamento de longo prazo para Prometheus, linguagens PromQL e MetricsQL, snapshots instantâneos, 11 protocolos de ingestão, suporte a NFS (EFS/Filestore), recursos Enterprise/LTS e benchmarks de RAM e compressão.; consultado em 2026-10-03.
- [VictoriaMetrics Documentation — Key Concepts & Quick Start](https://docs.victoriametrics.com/victoriametrics/keyconcepts/) — Documentação oficial de conceitos fundamentais e início rápido do VictoriaMetrics.; consultado em 2026-10-03.
- [VictoriaMetrics — Official GitHub Repository](https://github.com/VictoriaMetrics/VictoriaMetrics) — Repositório principal Apache-2.0 do VictoriaMetrics com binários para single-node, cluster e vmutils.; consultado em 2026-10-03.
