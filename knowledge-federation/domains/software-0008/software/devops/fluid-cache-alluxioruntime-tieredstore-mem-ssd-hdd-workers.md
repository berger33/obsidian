---
id: software.devops.tranche16.001573
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
fontes: ["https://raw.githubusercontent.com/fluid-cloudnative/fluid/master/docs/en/userguide/overview.md", "https://raw.githubusercontent.com/fluid-cloudnative/fluid/master/README.md", "https://github.com/fluid-cloudnative/fluid"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Fluid: aceleração de cache distribuído com `AlluxioRuntime` e armazenamento em camadas (`tieredstore`)

## Em uma frase
O `AlluxioRuntime` (`data.fluid.io/v1alpha1`) é o motor clássico de cache distribuído gerenciado pelo Fluid, orquestrando Pods `master`, `worker` e `fuse` do Alluxio com armazenamento hierárquico em camadas (`MEM`, `SSD`, `HDD`).

## Por que importa
Configurar manualmente um cluster Alluxio sobre Kubernetes — dimensionando masters Raft, workers com volumes de cache hostPath/emptyDir, daemons FUSE e sincronização de metadados UFS — exige dezenas de manifestos complexos.

## Como funciona
Com o `AlluxioRuntime`, o engenheiro define apenas `spec.replicas` (número de workers de cache) e `spec.tieredstore.levels` (por exemplo `mediumtype: MEM` ou `SSD`, `path: /dev/shm` ou `/var/lib/cache`, `quota: 20Gi`, `high: "0.95"`, `low: "0.7"`). O controlador do Fluid provisiona o StatefulSet de masters, os workers de cache e gerencia o ciclo de vida do volume CSI correspondente.

## Exemplo
```yaml
apiVersion: data.fluid.io/v1alpha1
kind: AlluxioRuntime
metadata:
  name: imagenet-train
  namespace: ai-workloads
spec:
  replicas: 2
  tieredstore:
    levels:
      - mediumtype: MEM
        path: /dev/shm
        quota: 4Gi
        high: "0.95"
        low: "0.7"
```

## Limites e trade-offs
Os parâmetros `high` e `low` do `tieredstore` definem as marcas d'água de evicção de cache: quando o uso da camada atinge `95%` (`high`), o worker despeja blocos menos usados até reduzir a ocupação para `70%` (`low`).

## Como verificar
Execute `kubectl get dataset,alluxioruntime,pvc -n ai-workloads` e verifique o percentual de dados em cache (`CACHED` e `CACHED PERCENTAGE`) reportado pelo `Dataset`.

## Conexões
- [[fluid-cache-crd-dataset-unificacao-multiplas-fontes-pvc]] — Veja também: Fluid: abstração unificada de dados heterogêneos via CRD `Dataset` e exposição transparente por PVC.
- [[fluid-cache-co-orquestracao-data-affinity-scheduling-localidade]] — Veja também: Fluid: co-orquestração de dados e computação via agendamento por afinidade de cache (*Data-Affinity Scheduling*).

## Fontes
- [Fluid GitHub — README.md (CNCF Incubating Distributed Dataset Orchestrator, Dataset & Runtime Abstractions & Academic Papers)](https://raw.githubusercontent.com/fluid-cloudnative/fluid/master/docs/en/userguide/overview.md) — README oficial do fluid-cloudnative/fluid (CNCF Incubating) detalhando abstração de Dataset, Runtimes escaláveis de cache e operações automatizadas de dados; consultado em 2026-10-03.
- [Fluid Official Documentation — Overview (Computation-Storage Separation, AlluxioRuntime, Data Affinity Scheduling & Co-Orchestration)](https://raw.githubusercontent.com/fluid-cloudnative/fluid/master/README.md) — Guia oficial Overview do Fluid explicando a co-orquestração de dataset e aplicação, agendamento por afinidade de dados e isolamento por namespace; consultado em 2026-10-03.
- [Fluid — Official GitHub Repository](https://github.com/fluid-cloudnative/fluid) — Repositório oficial Apache-2.0 do Fluid na CNCF; consultado em 2026-10-03.
