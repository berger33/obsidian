---
id: software.kubernetes.pdb-disponibilidade.000001
tipo: conceito
dominio: software
subdominio: kubernetes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: aprovada
revisor: usuario-da-sessao
data_revisao_humana: 2026-10-02
fontes: ["https://kubernetes.io/docs/concepts/workloads/pods/disruptions/", "https://kubernetes.io/docs/tasks/run-application/configure-pdb/"]
tags: [dominio/software, subdominio/kubernetes, qualidade/candidata]
aliases: [PodDisruptionBudget, PDB, Kubernetes voluntary disruption]
lote: software-kubernetes-operacao-0005
---

# PodDisruptionBudget e disponibilidade no Kubernetes

## Em uma frase
Um PodDisruptionBudget limita quantas réplicas podem ficar indisponíveis simultaneamente em interrupções voluntárias mediadas pela API de eviction.

## Por que importa
Manutenção de nós, drenagem e outras operações voluntárias podem remover réplicas de uma aplicação. Um PDB comunica quantas instâncias o serviço tolera perder nesse tipo de operação e pode fazer a solicitação de eviction ser recusada temporariamente se ultrapassar o orçamento. Isso ajuda a proteger aplicações replicadas, desde que o seletor represente o conjunto correto de Pods.

## Como funciona
O PDB especifica uma disponibilidade mínima ou um máximo de indisponíveis para Pods selecionados. Ferramentas como `kubectl drain` usam a Eviction API, que verifica o orçamento e pode rejeitar uma solicitação até que haja capacidade. Interrupções involuntárias não podem ser impedidas pelo PDB, embora contem contra o orçamento. Exclusões diretas de Pods ou Deployments podem ignorar essa proteção. Pods indisponíveis durante um rollout contam contra o budget, mas Deployments e StatefulSets não são limitados por PDB ao executar seus próprios rolling updates; o comportamento do rollout é controlado pelo recurso de workload.

## Exemplo
Uma aplicação com cinco réplicas pode definir um orçamento que permita uma indisponibilidade voluntária por vez. Durante um drain, a primeira eviction pode ser aceita e a próxima aguardar uma réplica substituta ficar disponível. O orçamento precisa ser escolhido junto à capacidade real de atender tráfego e aos requisitos de quorum.

## Limites e trade-offs
PDB não é uma garantia de que a aplicação sempre manterá o número mínimo de réplicas e não substitui múltiplas réplicas distribuídas por nós ou zonas. Um seletor vazio ou incorreto pode atingir mais Pods do que o pretendido. Um budget restritivo pode bloquear manutenção; um permissivo pode não preservar disponibilidade suficiente. Rollout e interrupção voluntária são mecanismos de controle distintos.

## Como verificar
Teste drain em um ambiente de staging e confirme como a Eviction API reage antes e depois de uma réplica voltar a ficar disponível. Verifique se o seletor coincide com os labels do workload e se os valores continuam coerentes durante escala horizontal. Simule também interrupção involuntária e um rollout para não confundir o escopo do PDB.

## Conexões
- [[deployment-rolling-update-kubernetes]] — a estratégia do Deployment controla seu próprio rollout; PDB não a limita.
- [[probes-kubernetes-liveness-readiness-startup]] — readiness afeta a disponibilidade observada das réplicas.
- [[requests-limits-cpu-memoria-kubernetes]] — falta de recursos pode causar interrupções involuntárias.

## Fontes
- [Kubernetes — Disruptions](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/) — interrupções voluntárias/involuntárias e escopo dos PDBs; acesso em 2026-10-01.
- [Kubernetes — Configure a PodDisruptionBudget](https://kubernetes.io/docs/tasks/run-application/configure-pdb/) — configuração e opções do recurso; acesso em 2026-10-01.
