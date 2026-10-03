---
id: software.devops.tranche16.001579
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

# Fluid: modos de implantação FUSE (CSI HostMount vs Sidecar Serverless) e auto-recuperação de pontos de montagem

## Em uma frase
O Fluid suporta dois modos de entrega do cliente FUSE para os Pods consumidores: via DaemonSet CSI nos worker nodes padrão (com recuperação automática de mount point caso o Pod FUSE reinicie) e via injeção automática de container Sidecar para ambientes Serverless Kubernetes (como AWS Fargate, Alibaba ECI ou Virtual Kubelet).

## Por que importa
No Kubernetes tradicional, se o container que hospeda o daemon FUSE no nó sofrer crash ou for atualizado, todos os Pods de aplicação que já tinham o volume montado passam a receber o erro fatal `Transport endpoint is not connected` (`ENOTCONN`), exigindo recriação manual dos Pods de treinamento.

## Como funciona
No modo CSI padrão, o componente `csi-nodeplugin-fluid` monitora a saúde dos daemons FUSE e executa a recuperação automática da montagem (`mount point recovery`) propagando a nova conexão para os containers de aplicação sem derrubá-los. Já em nós Serverless (onde DaemonSets privilegiados não são permitidos), o webhook do Fluid injeta o cliente FUSE diretamente como um sidecar dentro do próprio Pod da aplicação.

## Exemplo
```bash
kubectl label namespace serverless-ai fluid.io/enable-injection=true
kubectl get pods -n fluid-system -l app=csi-nodeplugin-fluid
```

## Limites e trade-offs
No modo Sidecar para ambientes Serverless, se o container FUSE não dispuser de `/dev/fuse` exposto pelo provedor de container serverless, é necessário configurar o modo de acesso sem privilégios suportado pelo runtime específico (ou `Unprivileged` FUSE).

## Como verificar
Verifique nos logs do `csi-nodeplugin-fluid` o registro de monitoramento de pontos de montagem FUSE ativos no nó.

## Conexões
- [[fluid-cache-escalonamento-elastico-autoscale-clean-cache-policy]] — Veja também: Fluid: escalabilidade elástica de workers de cache e políticas de limpeza (`cleanCachePolicy`).
- [[fluid-cache-aceleracao-pvc-existente-isolamento-seguranca-namespace]] — Veja também: Fluid: aceleração de `PersistentVolumeClaim` existente (`pvc://`) e isolamento de dados por namespace.

## Fontes
- [Fluid GitHub — README.md (CNCF Incubating Distributed Dataset Orchestrator, Dataset & Runtime Abstractions & Academic Papers)](https://raw.githubusercontent.com/fluid-cloudnative/fluid/master/README.md) — README oficial do fluid-cloudnative/fluid (CNCF Incubating) detalhando abstração de Dataset, Runtimes escaláveis de cache e operações automatizadas de dados; consultado em 2026-10-03.
- [Fluid Official Documentation — Overview (Computation-Storage Separation, AlluxioRuntime, Data Affinity Scheduling & Co-Orchestration)](https://raw.githubusercontent.com/fluid-cloudnative/fluid/master/docs/en/userguide/overview.md) — Guia oficial Overview do Fluid explicando a co-orquestração de dataset e aplicação, agendamento por afinidade de dados e isolamento por namespace; consultado em 2026-10-03.
- [Fluid — Official GitHub Repository](https://github.com/fluid-cloudnative/fluid) — Repositório oficial Apache-2.0 do Fluid na CNCF; consultado em 2026-10-03.
