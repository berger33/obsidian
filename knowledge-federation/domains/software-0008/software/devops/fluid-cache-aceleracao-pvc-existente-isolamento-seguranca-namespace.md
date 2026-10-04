---
id: software.devops.tranche16.001580
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

# Fluid: aceleração de `PersistentVolumeClaim` existente (`pvc://`) e isolamento de dados por namespace

## Em uma frase
O Fluid pode acelerar um `PersistentVolumeClaim` já existente no cluster (como um volume NFS corporativo lento ou um disco de rede compartilhado) simplesmente apontando `mountPoint: pvc://<nome-do-pvc>` no CRD `Dataset`, mantendo o isolamento de acesso por namespace Kubernetes.

## Por que importa
Equipes frequentemente armazenam datasets em um servidor NFS legado já montado via PVC no Kubernetes; quando 50 Pods de treinamento tentam ler esse mesmo PVC simultaneamente, o servidor NFS satura sua placa de rede e trava todas as cargas.

## Como funciona
Ao criar um `Dataset` com `mountPoint: pvc://nfs-shared-dataset` e associá-lo a um `AlluxioRuntime` ou `JuiceFSRuntime`, o Fluid monta o PVC original nos workers de cache e expõe um novo PVC acelerado para os Pods de treinamento. As leituras repetidas passam a ser servidas diretamente da RAM/NVMe local dos nós do cluster, aliviando o armazenamento NFS de origem.

## Exemplo
```yaml
apiVersion: data.fluid.io/v1alpha1
kind: Dataset
metadata:
  name: accelerated-nfs
  namespace: ai-workloads
spec:
  mounts:
    - mountPoint: pvc://legacy-nfs-pvc
      name: nfs-data
```

## Limites e trade-offs
O PVC de origem (`legacy-nfs-pvc`) deve estar no mesmo namespace que o `Dataset` (`ai-workloads`) e suportar montagem pelos múltiplos Pods do Runtime (tipicamente `ReadWriteMany` ou `ReadOnlyMany`).

## Como verificar
Compare o throughput de leitura (`dd` ou benchmark PyTorch DataLoader) lendo diretamente de `legacy-nfs-pvc` versus lendo do novo PVC `accelerated-nfs` após a primeira passagem de cache.

## Conexões
- [[fluid-cache-recuperacao-automatica-fuse-sidecar-serverless-csi]] — Veja também: Fluid: modos de implantação FUSE (CSI HostMount vs Sidecar Serverless) e auto-recuperação de pontos de montagem.

## Fontes
- [Fluid GitHub — README.md (CNCF Incubating Distributed Dataset Orchestrator, Dataset & Runtime Abstractions & Academic Papers)](https://raw.githubusercontent.com/fluid-cloudnative/fluid/master/README.md) — README oficial do fluid-cloudnative/fluid (CNCF Incubating) detalhando abstração de Dataset, Runtimes escaláveis de cache e operações automatizadas de dados; consultado em 2026-10-03.
- [Fluid Official Documentation — Overview (Computation-Storage Separation, AlluxioRuntime, Data Affinity Scheduling & Co-Orchestration)](https://raw.githubusercontent.com/fluid-cloudnative/fluid/master/docs/en/userguide/overview.md) — Guia oficial Overview do Fluid explicando a co-orquestração de dataset e aplicação, agendamento por afinidade de dados e isolamento por namespace; consultado em 2026-10-03.
- [Fluid — Official GitHub Repository](https://github.com/fluid-cloudnative/fluid) — Repositório oficial Apache-2.0 do Fluid na CNCF; consultado em 2026-10-03.
