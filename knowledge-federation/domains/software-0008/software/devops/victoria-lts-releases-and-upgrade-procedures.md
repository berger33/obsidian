---
id: software.devops.tranche05.000418
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

# Lançamentos LTS (Long-Term Support), changelog rápido e procedimento seguro de upgrade

## Em uma frase
O README oficial informa que o projeto evolui rapidamente (mantendo changelog detalhado em `docs.victoriametrics.com/victoriametrics/changelog/` e guia de atualização em `#how-to-upgrade-victoriametrics`) e disponibiliza publicamente linhas de **Long-Term Support (LTS)** (`docs.victoriametrics.com/victoriametrics/lts-releases/`), além de certificações formais de segurança para *Database Software Development* e *Software-Based Monitoring Services* (`victoriametrics.com/security/`).

## Por que importa
Em ambientes corporativos críticos com janelas de mudança controladas, acompanhar lançamentos semanais ou mensais de novas funcionalidades nem sempre é desejável; as linhas **LTS** oferecem estabilidade prolongada com backports de correções de bugs e segurança.

## Como funciona
Escolha uma linha de release **LTS** para clusters produtivos de missão crítica que priorizam estabilidade de longo prazo, e consulte sempre a seção `How to upgrade` e o `CHANGELOG` oficial antes de atualizar binários ou imagens Docker/Quay.

## Exemplo
Uma instituição financeira padroniza sua infraestrutura de monitoramento na versão LTS vigente do VictoriaMetrics, aplicando atualizações de patch LTS dentro de sua janela mensal de manutenção após revisar o changelog.

## Limites e trade-offs
Durante upgrades da versão Cluster, siga a ordem e as recomendações oficiais da documentação para atualizar `vmstorage`, `vminsert` e `vmselect` com degradação zero de disponibilidade.

## Como verificar
Verifique a versão exata em execução nos logs de inicialização ou na métrica `vm_app_version` após concluir o upgrade.

## Conexões
- [[victoria-stream-aggregation-and-relabeling-capabilities]] — Veja também: Agregação de stream em tempo real (alternativa ao StatsD) e relabeling de métricas no VictoriaMetrics.
- [[victoria-enterprise-features-downsampling-and-multi-retention]] — Veja também: Recursos Enterprise do VictoriaMetrics: detecção de anomalias, múltiplas retenções e downsampling.

## Fontes
- [VictoriaMetrics GitHub — README.md (Single-Node & Cluster, MetricsQL, Protocols, Snapshots & Benchmarks)](https://raw.githubusercontent.com/VictoriaMetrics/VictoriaMetrics/master/README.md) — README oficial do VictoriaMetrics detalhando versões Single-node e Cluster sob licença Apache-2.0, armazenamento de longo prazo para Prometheus, linguagens PromQL e MetricsQL, snapshots instantâneos, 11 protocolos de ingestão, suporte a NFS (EFS/Filestore), recursos Enterprise/LTS e benchmarks de RAM e compressão.; consultado em 2026-10-03.
- [VictoriaMetrics Documentation — Key Concepts & Quick Start](https://docs.victoriametrics.com/victoriametrics/keyconcepts/) — Documentação oficial de conceitos fundamentais e início rápido do VictoriaMetrics.; consultado em 2026-10-03.
- [VictoriaMetrics — Official GitHub Repository](https://github.com/VictoriaMetrics/VictoriaMetrics) — Repositório principal Apache-2.0 do VictoriaMetrics com binários para single-node, cluster e vmutils.; consultado em 2026-10-03.
