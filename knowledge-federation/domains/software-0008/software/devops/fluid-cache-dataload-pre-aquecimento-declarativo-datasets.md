---
id: software.devops.tranche16.001575
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-16.md"
fontes: ["https://raw.githubusercontent.com/fluid-cloudnative/fluid/master/README.md", "https://raw.githubusercontent.com/fluid-cloudnative/fluid/master/docs/en/userguide/overview.md", "https://github.com/fluid-cloudnative/fluid"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Fluid: pré-carregamento declarativo de dados (`DataLoad`) antes da execução de treinamentos

## Em uma frase
O CRD `DataLoad` (`data.fluid.io/v1alpha1`) permite disparar jobs declarativos de pré-aquecimento (*cache warmup*) que carregam o dataset inteiro ou subpastas específicas do armazenamento remoto para os workers de cache do Fluid antes que os jobs de treinamento de GPU iniciem.

## Por que importa
Na primeira época (*epoch 1*) de um treinamento distribuído sobre um cache frio (*cold cache*), todos os workers sofrem cache miss simultâneo e precisam buscar os objetos no S3/HDFS, subutilizando GPUs caras durante a primeira passagem pelos dados.

## Como funciona
Ao aplicar um manifesto `DataLoad` apontando para `spec.dataset.name` (e opcionalmente `loadMetadata: true` e uma lista de `target` paths), o controlador do Fluid lança um Job distribuído que popula os blocos de dados na camada `MEM`/`SSD` dos workers do Runtime. O `DataLoad` também pode ser agendado por política `Cron` ou encadeado após outras operações de dados.

## Exemplo
```yaml
apiVersion: data.fluid.io/v1alpha1
kind: DataLoad
metadata:
  name: warmup-imagenet
  namespace: ai-workloads
spec:
  dataset:
    name: imagenet-train
    namespace: ai-workloads
  loadMetadata: true
  target:
    - path: /spark
      replicas: 2
```

## Limites e trade-offs
Se a soma do tamanho dos arquivos solicitados no `DataLoad` exceder a cota total (`quota * replicas`) configurada no `tieredstore` do Runtime, os blocos recém-carregados sofrerão evicção imediata (cache thrashing), reduzindo a eficácia do pré-aquecimento.

## Como verificar
Monitore `kubectl get dataload warmup-imagenet -n ai-workloads` até que `PHASE` atinja `Complete` e verifique em `kubectl get dataset imagenet-train -n ai-workloads` que `CACHED PERCENTAGE` subiu para `100.0%`.

## Conexões
- [[fluid-cache-co-orquestracao-data-affinity-scheduling-localidade]] — Veja também: Fluid: co-orquestração de dados e computação via agendamento por afinidade de cache (*Data-Affinity Scheduling*).
- [[fluid-cache-runtimes-pluggables-juicefs-jindo-vineyard-efc]] — Veja também: Fluid: arquitetura plugável de Runtimes de cache (`JuiceFSRuntime`, `JindoRuntime`, `VineyardRuntime`, `ThinRuntime`).

## Fontes
- [Fluid GitHub — README.md (CNCF Incubating Distributed Dataset Orchestrator, Dataset & Runtime Abstractions & Academic Papers)](https://raw.githubusercontent.com/fluid-cloudnative/fluid/master/README.md) — README oficial do fluid-cloudnative/fluid (CNCF Incubating) detalhando abstração de Dataset, Runtimes escaláveis de cache e operações automatizadas de dados; consultado em 2026-10-03.
- [Fluid Official Documentation — Overview (Computation-Storage Separation, AlluxioRuntime, Data Affinity Scheduling & Co-Orchestration)](https://raw.githubusercontent.com/fluid-cloudnative/fluid/master/docs/en/userguide/overview.md) — Guia oficial Overview do Fluid explicando a co-orquestração de dataset e aplicação, agendamento por afinidade de dados e isolamento por namespace; consultado em 2026-10-03.
- [Fluid — Official GitHub Repository](https://github.com/fluid-cloudnative/fluid) — Repositório oficial Apache-2.0 do Fluid na CNCF; consultado em 2026-10-03.
