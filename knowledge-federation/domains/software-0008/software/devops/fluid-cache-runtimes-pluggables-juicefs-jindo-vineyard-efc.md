---
id: software.devops.tranche16.001576
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

# Fluid: arquitetura plugável de Runtimes de cache (`JuiceFSRuntime`, `JindoRuntime`, `VineyardRuntime`, `ThinRuntime`)

## Em uma frase
O Fluid define uma interface padrão de ciclo de vida de Runtime que suporta múltiplos motores de armazenamento e cache distribuído além do Alluxio, incluindo `JuiceFSRuntime`, `JindoRuntime`, `GooseFSRuntime`, `EFCOSRuntime`, `VineyardRuntime` (para dados intermediários em memória) e `ThinRuntime` (extensão genérica para qualquer sistema FUSE/CSI).

## Por que importa
Diferentes cargas de trabalho possuem padrões distintos de I/O: treinamentos de visão computacional com milhões de arquivos pequenos se beneficiam da separação de metadados do JuiceFS; pipelines nativos em OSS usam JindoFS; e grafos analíticos em memória compartilhada entre etapas de um DAG usam o CNCF Vineyard.

## Como funciona
O usuário mantém exatamente o mesmo CRD `Dataset` e a mesma interface de consumo via PVC nas aplicações, trocando apenas o CRD de Runtime pareado (por exemplo, aplicando um `JuiceFSRuntime` em vez de `AlluxioRuntime`). Com o `ThinRuntime` e `ThinRuntimeProfile`, engenheiros de plataforma podem integrar um cliente FUSE proprietário em minutos sem precisar recompilar o código Go do Fluid.

## Exemplo
```yaml
apiVersion: data.fluid.io/v1alpha1
kind: JuiceFSRuntime
metadata:
  name: llm-corpus
  namespace: ai-workloads
spec:
  replicas: 3
  tieredstore:
    levels:
      - mediumtype: SSD
        path: /mnt/nvme-cache
        quota: 100Gi
```

## Limites e trade-offs
Cada controlador de Runtime no Fluid é implantado de forma modular; no chart Helm do Fluid, apenas os controladores dos runtimes habilitados em `values.yaml` consomem recursos no namespace `fluid-system`.

## Como verificar
Verifique os CRDs de runtime instalados no cluster com `kubectl api-resources --api-group=data.fluid.io` e confirme a disponibilidade dos motores necessários.

## Conexões
- [[fluid-cache-dataload-pre-aquecimento-declarativo-datasets]] — Veja também: Fluid: pré-carregamento declarativo de dados (`DataLoad`) antes da execução de treinamentos.
- [[fluid-cache-operacoes-automatizadas-databackup-datamigrate-dataprocess]] — Veja também: Fluid: automação de operações de dados (`DataBackup`, `DataMigrate` e `DataProcess`) e encadeamento em fluxo.

## Fontes
- [Fluid GitHub — README.md (CNCF Incubating Distributed Dataset Orchestrator, Dataset & Runtime Abstractions & Academic Papers)](https://raw.githubusercontent.com/fluid-cloudnative/fluid/master/README.md) — README oficial do fluid-cloudnative/fluid (CNCF Incubating) detalhando abstração de Dataset, Runtimes escaláveis de cache e operações automatizadas de dados; consultado em 2026-10-03.
- [Fluid Official Documentation — Overview (Computation-Storage Separation, AlluxioRuntime, Data Affinity Scheduling & Co-Orchestration)](https://raw.githubusercontent.com/fluid-cloudnative/fluid/master/docs/en/userguide/overview.md) — Guia oficial Overview do Fluid explicando a co-orquestração de dataset e aplicação, agendamento por afinidade de dados e isolamento por namespace; consultado em 2026-10-03.
- [Fluid — Official GitHub Repository](https://github.com/fluid-cloudnative/fluid) — Repositório oficial Apache-2.0 do Fluid na CNCF; consultado em 2026-10-03.
