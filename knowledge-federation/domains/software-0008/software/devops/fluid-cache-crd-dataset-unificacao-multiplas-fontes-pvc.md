---
id: software.devops.tranche16.001572
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

# Fluid: abstração unificada de dados heterogêneos via CRD `Dataset` e exposição transparente por PVC

## Em uma frase
O CRD `Dataset` (`data.fluid.io/v1alpha1`) abstrai uma ou múltiplas fontes de armazenamento subjacentes (*Under File Systems* — UFS, como buckets S3/OSS, HDFS, Ceph, NFS ou PVCs Kubernetes existentes) em uma visão unificada e isolada por namespace.

## Por que importa
Sem uma camada de abstração de datasets no Kubernetes, cientistas de dados precisam embutir SDKs proprietários de S3/HDFS, endpoints e credenciais de acesso diretamente no código de treinamento PyTorch/Spark, criando acoplamento rígido e "ilhas de dados".

## Como funciona
Ao declarar um `Dataset` de nome `imagenet` no namespace `ai-team`, o usuário especifica em `spec.mounts` as URIs de origem (`s3://...`, `hdfs://...`, `pvc://...`) e o `mountPoint` virtual. Quando vinculado a um `Runtime` de mesmo nome (`imagenet`), o Fluid cria automaticamente um `PersistentVolume` e um `PersistentVolumeClaim` chamado `imagenet` naquele namespace: qualquer Pod só precisa montar esse PVC padrão via POSIX sem conhecer o protocolo remoto.

## Exemplo
```yaml
apiVersion: data.fluid.io/v1alpha1
kind: Dataset
metadata:
  name: imagenet-train
  namespace: ai-workloads
spec:
  mounts:
    - mountPoint: https://mirrors.tuna.tsinghua.edu.cn/apache/spark/
      name: spark-releases
      path: /spark
  accessModes:
    - ReadOnlyMany
```

## Limites e trade-offs
Um objeto `Dataset` permanece na fase `NotBound` até que um objeto de Runtime correspondente (por exemplo um `AlluxioRuntime` ou `JuiceFSRuntime`) com exatamente o mesmo `metadata.name` e `metadata.namespace` seja criado no cluster.

## Como verificar
Execute `kubectl get dataset -n ai-workloads` e confirme que a coluna `PHASE` transita de `NotBound` para `Bound` assim que o Runtime pareado fica pronto.

## Conexões
- [[fluid-cache-arquitetura-orquestrador-datasets-aceleracao-cncf]] — Veja também: Fluid: arquitetura CNCF Incubating de abstração de Datasets e aceleração elástica de cache no Kubernetes.
- [[fluid-cache-alluxioruntime-tieredstore-mem-ssd-hdd-workers]] — Veja também: Fluid: aceleração de cache distribuído com `AlluxioRuntime` e armazenamento em camadas (`tieredstore`).

## Fontes
- [Fluid GitHub — README.md (CNCF Incubating Distributed Dataset Orchestrator, Dataset & Runtime Abstractions & Academic Papers)](https://raw.githubusercontent.com/fluid-cloudnative/fluid/master/docs/en/userguide/overview.md) — README oficial do fluid-cloudnative/fluid (CNCF Incubating) detalhando abstração de Dataset, Runtimes escaláveis de cache e operações automatizadas de dados; consultado em 2026-10-03.
- [Fluid Official Documentation — Overview (Computation-Storage Separation, AlluxioRuntime, Data Affinity Scheduling & Co-Orchestration)](https://raw.githubusercontent.com/fluid-cloudnative/fluid/master/README.md) — Guia oficial Overview do Fluid explicando a co-orquestração de dataset e aplicação, agendamento por afinidade de dados e isolamento por namespace; consultado em 2026-10-03.
- [Fluid — Official GitHub Repository](https://github.com/fluid-cloudnative/fluid) — Repositório oficial Apache-2.0 do Fluid na CNCF; consultado em 2026-10-03.
