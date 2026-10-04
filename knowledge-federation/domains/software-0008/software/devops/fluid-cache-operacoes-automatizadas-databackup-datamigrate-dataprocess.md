---
id: software.devops.tranche16.001577
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

# Fluid: automação de operações de dados (`DataBackup`, `DataMigrate` e `DataProcess`) e encadeamento em fluxo

## Em uma frase
Além do `DataLoad`, o Fluid provê CRDs declarativos para operações automatizadas sobre datasets (`DataBackup`, `DataMigrate` e `DataProcess`), permitindo encadear pipelines completos de preparação, pré-aquecimento e treinamento via campo `runAfter`.

## Por que importa
Em pipelines de MLOps, antes do treinamento iniciar é comum precisar copiar um lote bruto de um bucket externo (`DataMigrate`), executar um script de limpeza/tokenização (`DataProcess`), pré-aquecer o resultado em memória (`DataLoad`) e fazer backup dos metadados (`DataBackup`).

## Como funciona
Todas essas operações de dados compartilham uma abstração comum no Fluid e podem referenciar umas às outras por meio de `spec.runAfter` (`kind: DataMigrate | DataLoad | DataProcess`, `name: ...`), criando um workflow declarativo nativo em Kubernetes sem exigir um orquestrador de workflow externo apenas para preparar o cache.

## Exemplo
```yaml
apiVersion: data.fluid.io/v1alpha1
kind: DataProcess
metadata:
  name: tokenize-corpus
  namespace: ai-workloads
spec:
  dataset:
    name: llm-corpus
    namespace: ai-workloads
  processor:
    job:
      podSpec:
        restartPolicy: Never
        containers:
          - name: tokenizer
            image: ghcr.io/org/tokenizer:v1.0
            command: ["python", "clean.py", "/data/raw", "/data/clean"]
            volumeMounts:
              - name: data-vol
                mountPath: /data
```

## Limites e trade-offs
No `DataProcess`, o nome do volume especificado em `volumeMounts` do `podSpec` é vinculado automaticamente pelo controlador do Fluid ao PVC do `Dataset` alvo referenciado em `spec.dataset`.

## Como verificar
Inspecione `kubectl get dataprocess,dataload,datamigrate -n ai-workloads` e valide a execução sequencial governada por `runAfter`.

## Conexões
- [[fluid-cache-runtimes-pluggables-juicefs-jindo-vineyard-efc]] — Veja também: Fluid: arquitetura plugável de Runtimes de cache (`JuiceFSRuntime`, `JindoRuntime`, `VineyardRuntime`, `ThinRuntime`).
- [[fluid-cache-escalonamento-elastico-autoscale-clean-cache-policy]] — Veja também: Fluid: escalabilidade elástica de workers de cache e políticas de limpeza (`cleanCachePolicy`).

## Fontes
- [Fluid GitHub — README.md (CNCF Incubating Distributed Dataset Orchestrator, Dataset & Runtime Abstractions & Academic Papers)](https://raw.githubusercontent.com/fluid-cloudnative/fluid/master/README.md) — README oficial do fluid-cloudnative/fluid (CNCF Incubating) detalhando abstração de Dataset, Runtimes escaláveis de cache e operações automatizadas de dados; consultado em 2026-10-03.
- [Fluid Official Documentation — Overview (Computation-Storage Separation, AlluxioRuntime, Data Affinity Scheduling & Co-Orchestration)](https://raw.githubusercontent.com/fluid-cloudnative/fluid/master/docs/en/userguide/overview.md) — Guia oficial Overview do Fluid explicando a co-orquestração de dataset e aplicação, agendamento por afinidade de dados e isolamento por namespace; consultado em 2026-10-03.
- [Fluid — Official GitHub Repository](https://github.com/fluid-cloudnative/fluid) — Repositório oficial Apache-2.0 do Fluid na CNCF; consultado em 2026-10-03.
