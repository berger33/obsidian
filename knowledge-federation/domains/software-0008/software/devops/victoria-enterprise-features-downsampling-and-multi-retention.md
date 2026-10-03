---
id: software.devops.tranche05.000419
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

# Recursos Enterprise do VictoriaMetrics: detecção de anomalias, múltiplas retenções e downsampling

## Em uma frase
O README oficial distingue claramente o que faz parte do núcleo Apache-2.0 (Single-node e Cluster completos) e o que é oferecido adicionalmente na versão **Enterprise** (avaliável gratuitamente via trial license com binários no GitHub Releases): **detecção de anomalias** (`Anomaly detection` para automação de regras de alerta sobre padrões complexos), **automação de backups**, **múltiplas retenções** (`Multiple retentions`, permitindo definir tempos de retenção diferentes para datasets distintos a fim de reduzir custos de armazenamento) e **downsampling** (reduzindo custos de disco e aumentando a performance de consultas sobre dados históricos de longo prazo).

## Por que importa
Conhecer a fronteira exata entre a edição open-source Apache-2.0 e os recursos Enterprise evita que arquitetos projetem políticas de múltiplas retenções por namespace ou downsampling nativo em clusters open-source sem planejar a licença correspondente ou uma topologia alternativa.

## Como funciona
No VictoriaMetrics open-source (Apache-2.0), caso precise de tempos de retenção distintos (por exemplo, 30 dias para métricas de alta frequência de desenvolvimento e 2 anos para métricas de negócio/SLO), separe-os em instâncias Single-node dedicadas com flags `-retentionPeriod` distintas, ou avalie a versão Enterprise se precisar de múltiplas retenções e downsampling dentro do mesmo cluster.

## Exemplo
Uma equipe de arquitetura utiliza duas instâncias Single-node Apache-2.0 com `-retentionPeriod=30d` e `-retentionPeriod=24m` roteadas por `relabeling` na ingestão para obter retenções diferenciadas sem custo de licenciamento proprietário.

## Limites e trade-offs
Não confunda a disponibilidade dos binários `-enterprise` na página do GitHub Releases com licença aberta: os recursos Enterprise exigem chave de licença válida (de avaliação ou comercial) após o período de teste.

## Como verificar
Verifique nos argumentos de inicialização do processo se está utilizando o binário open-source padrão Apache-2.0 e qual o valor configurado em `-retentionPeriod`.

## Conexões
- [[victoria-lts-releases-and-upgrade-procedures]] — Veja também: Lançamentos LTS (Long-Term Support), changelog rápido e procedimento seguro de upgrade.
- [[victoria-big-data-iot-and-industrial-telemetry-workloads]] — Veja também: Aplicação do VictoriaMetrics em cargas de Big Data, Kubernetes, IoT, carros conectados e telemetria industrial.

## Fontes
- [VictoriaMetrics GitHub — README.md (Single-Node & Cluster, MetricsQL, Protocols, Snapshots & Benchmarks)](https://raw.githubusercontent.com/VictoriaMetrics/VictoriaMetrics/master/README.md) — README oficial do VictoriaMetrics detalhando versões Single-node e Cluster sob licença Apache-2.0, armazenamento de longo prazo para Prometheus, linguagens PromQL e MetricsQL, snapshots instantâneos, 11 protocolos de ingestão, suporte a NFS (EFS/Filestore), recursos Enterprise/LTS e benchmarks de RAM e compressão.; consultado em 2026-10-03.
- [VictoriaMetrics Documentation — Key Concepts & Quick Start](https://docs.victoriametrics.com/victoriametrics/keyconcepts/) — Documentação oficial de conceitos fundamentais e início rápido do VictoriaMetrics.; consultado em 2026-10-03.
- [VictoriaMetrics — Official GitHub Repository](https://github.com/VictoriaMetrics/VictoriaMetrics) — Repositório principal Apache-2.0 do VictoriaMetrics com binários para single-node, cluster e vmutils.; consultado em 2026-10-03.
