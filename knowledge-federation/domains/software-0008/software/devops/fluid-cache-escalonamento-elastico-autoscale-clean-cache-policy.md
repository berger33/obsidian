---
id: software.devops.tranche16.001578
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

# Fluid: escalabilidade elástica de workers de cache e políticas de limpeza (`cleanCachePolicy`)

## Em uma frase
Os Runtimes do Fluid suportam escalonamento elástico manual (`kubectl scale`) e automático (via HPA sobre a sub-resource `/scale` do Runtime) do número de workers de cache, além de políticas configuráveis de desalocação de cache (`cleanCachePolicy`) ao encerrar os Pods consumidores.

## Por que importa
Manter um cluster de cache ocupando centenas de gigabytes de RAM e NVMe 24x7 para um dataset que só é lido por jobs de treinamento noturnos desperdiça recursos que poderiam ser usados por outras cargas durante o dia.

## Como funciona
O operador pode escalar um `AlluxioRuntime` ou `JuiceFSRuntime` (`kubectl scale alluxioruntime imagenet-train --replicas=6`) antes de uma bateria pesada de treinamentos e reduzi-lo a `0` ou usar políticas de limpeza automática quando nenhum Pod estiver montando o PVC, liberando a memória e o SSD dos nós Kubernetes.

## Exemplo
```bash
kubectl scale alluxioruntime imagenet-train -n ai-workloads --replicas=4
kubectl get alluxioruntime imagenet-train -n ai-workloads
```

## Limites e trade-offs
Reduzir `replicas` de um Runtime de cache com dados que foram gravados apenas no cache local (*write-back* ainda não persistido no UFS remoto) pode causar perda de dados se o flush não tiver sido concluído antes do scale-down.

## Como verificar
Monitore o campo `READY` dos workers em `kubectl get alluxioruntime -n ai-workloads` e a capacidade `CACHE CAPACITY` em `kubectl get dataset -n ai-workloads` após o escalonamento.

## Conexões
- [[fluid-cache-operacoes-automatizadas-databackup-datamigrate-dataprocess]] — Veja também: Fluid: automação de operações de dados (`DataBackup`, `DataMigrate` e `DataProcess`) e encadeamento em fluxo.
- [[fluid-cache-recuperacao-automatica-fuse-sidecar-serverless-csi]] — Veja também: Fluid: modos de implantação FUSE (CSI HostMount vs Sidecar Serverless) e auto-recuperação de pontos de montagem.

## Fontes
- [Fluid GitHub — README.md (CNCF Incubating Distributed Dataset Orchestrator, Dataset & Runtime Abstractions & Academic Papers)](https://raw.githubusercontent.com/fluid-cloudnative/fluid/master/README.md) — README oficial do fluid-cloudnative/fluid (CNCF Incubating) detalhando abstração de Dataset, Runtimes escaláveis de cache e operações automatizadas de dados; consultado em 2026-10-03.
- [Fluid Official Documentation — Overview (Computation-Storage Separation, AlluxioRuntime, Data Affinity Scheduling & Co-Orchestration)](https://raw.githubusercontent.com/fluid-cloudnative/fluid/master/docs/en/userguide/overview.md) — Guia oficial Overview do Fluid explicando a co-orquestração de dataset e aplicação, agendamento por afinidade de dados e isolamento por namespace; consultado em 2026-10-03.
- [Fluid — Official GitHub Repository](https://github.com/fluid-cloudnative/fluid) — Repositório oficial Apache-2.0 do Fluid na CNCF; consultado em 2026-10-03.
