---
id: software.devops.tranche16.001571
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

# Fluid: arquitetura CNCF Incubating de abstração de Datasets e aceleração elástica de cache no Kubernetes

## Em uma frase
O Fluid (projeto CNCF Incubating, escrito em Go) é um orquestrador e acelerador nativo de Kubernetes para *datasets* distribuídos que reconstrói a localidade de dados em arquiteturas de separação entre computação e armazenamento para cargas de IA/ML e Big Data.

## Por que importa
Na arquitetura cloud-native moderna, os dados residem em object stores remotos (S3, OSS, GCS, Ceph, HDFS) separados dos nós de computação efêmeros. Treinar modelos de Deep Learning lendo milhões de pequenos arquivos pela rede a cada época (*epoch*) deixa GPUs caras ociosas aguardando I/O remoto.

## Como funciona
O Fluid introduz dois Custom Resources centrais (`data.fluid.io/v1alpha1`): `Dataset` (que define a origem lógica dos dados e pontos de montagem) e `Runtime` (como `AlluxioRuntime`, `JuiceFSRuntime`, `JindoRuntime`, `EFCOSRuntime` ou `VineyardRuntime`, que provisiona um cluster de cache distribuído usando discos NVMe/SSD e RAM dos próprios nós Kubernetes), expondo o conjunto acelerado como um `PersistentVolumeClaim` padrão via CSI.

## Exemplo
```bash
helm repo add fluid https://fluid-cloudnative.github.io/charts
helm upgrade --install fluid fluid/fluid --namespace fluid-system --create-namespace
kubectl get pods -n fluid-system
```

## Limites e trade-offs
O Fluid requer um cluster Kubernetes com suporte a CSI (*Container Storage Interface*), pois o plugin `csi-nodeplugin-fluid` monta o sistema de arquivos FUSE do motor de cache selecionado dentro dos Pods das aplicações consumidoras.

## Como verificar
Verifique os controladores `dataset-controller`, os controladores de runtime ativos e o DaemonSet `csi-nodeplugin-fluid` no namespace `fluid-system` após a instalação.

## Conexões
- [[fluid-cache-crd-dataset-unificacao-multiplas-fontes-pvc]] — Veja também: Fluid: abstração unificada de dados heterogêneos via CRD `Dataset` e exposição transparente por PVC.

## Fontes
- [Fluid GitHub — README.md (CNCF Incubating Distributed Dataset Orchestrator, Dataset & Runtime Abstractions & Academic Papers)](https://raw.githubusercontent.com/fluid-cloudnative/fluid/master/README.md) — README oficial do fluid-cloudnative/fluid (CNCF Incubating) detalhando abstração de Dataset, Runtimes escaláveis de cache e operações automatizadas de dados; consultado em 2026-10-03.
- [Fluid Official Documentation — Overview (Computation-Storage Separation, AlluxioRuntime, Data Affinity Scheduling & Co-Orchestration)](https://raw.githubusercontent.com/fluid-cloudnative/fluid/master/docs/en/userguide/overview.md) — Guia oficial Overview do Fluid explicando a co-orquestração de dataset e aplicação, agendamento por afinidade de dados e isolamento por namespace; consultado em 2026-10-03.
- [Fluid — Official GitHub Repository](https://github.com/fluid-cloudnative/fluid) — Repositório oficial Apache-2.0 do Fluid na CNCF; consultado em 2026-10-03.
