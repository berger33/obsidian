---
id: software.devops.tranche17.001601
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-17.md"
fontes: ["https://raw.githubusercontent.com/karmada-io/karmada/master/README.md", "https://karmada.io/docs/core-concepts/architecture/", "https://github.com/karmada-io/karmada"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Karmada: arquitetura de plano de controle multi-cluster CNCF Graduated (`apiserver`, `controller-manager` e `scheduler`)

## Em uma frase
O Karmada (*Kubernetes Armada*, projeto CNCF Graduated evoluído do Kubernetes Federation v1/v2) é um sistema de orquestração multi-cloud e multi-cluster que permite executar aplicações cloud-native em múltiplos clusters Kubernetes sem modificar os manifestos originais da aplicação.

## Por que importa
Em arquiteturas multi-região e multi-nuvem, gerenciar dezenas de clusters independentes aplicando manifestos cluster por cluster fragmenta a operação e impede failover automático ou divisão proporcional de réplicas entre provedores.

## Como funciona
O Control Plane do Karmada possui seu próprio `karmada-apiserver` (compatível com a API nativa do Kubernetes), `etcd`, `karmada-scheduler` e `karmada-controller-manager`. O usuário submete um `Deployment` ou `Service` padrão para o `karmada-apiserver` junto a políticas de propagação e override; os controladores internos (`Cluster`, `Policy`, `Binding` e `Execution`) traduzem e distribuem os objetos para os clusters membros.

## Exemplo
```bash
kubectl --kubeconfig ~/.kube/karmada.config config use-context karmada-apiserver
kubectl --kubeconfig ~/.kube/karmada.config get clusters
```

## Limites e trade-offs
O `karmada-config` expõe dois contextos distintos: `karmada-apiserver` (plano de controle federado onde recursos e políticas são aplicados) e `karmada-host` (o cluster hospedeiro subjacente que executa os Pods dos componentes do Karmada).

## Como verificar
Execute `kubectl get clusters` no contexto `karmada-apiserver` e confirme que todos os clusters membros aparecem com condição `READY: True`.

## Conexões
- [[karmada-pipeline-propagacao-resourcebinding-work-execution]] — Veja também: Karmada: fluxo de propagação em quatro estágios (`PropagationPolicy` -> `ResourceBinding` -> `Work` -> Member Cluster).

## Fontes
- [Karmada GitHub — README.md (Kubernetes Armada CNCF Incubating Multi-Cloud & Multi-Cluster Kubernetes Orchestration)](https://raw.githubusercontent.com/karmada-io/karmada/master/README.md) — README oficial do karmada-io/karmada (CNCF Incubating) apresentando capacidades multi-cluster, API compatível com Kubernetes nativo e políticas de propagação; consultado em 2026-10-03.
- [Karmada Official Documentation — Core Concepts: Architecture (Control Plane, PropagationPolicy, OverridePolicy, ResourceBinding, Work & Agent)](https://karmada.io/docs/core-concepts/architecture/) — Documentação oficial de arquitetura do Karmada detalhando API Server, Controller Manager, Karmada Scheduler, Execution Space e sincronização para member clusters; consultado em 2026-10-03.
- [Karmada — Official GitHub Repository](https://github.com/karmada-io/karmada) — Repositório oficial Apache-2.0 do projeto Karmada na CNCF; consultado em 2026-10-03.
