---
id: software.devops.tranche07.000671
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-07.md"
fontes: ["https://raw.githubusercontent.com/kubernetes-sigs/descheduler/master/README.md", "https://github.com/kubernetes-sigs/descheduler/blob/master/charts/descheduler/README.md", "https://github.com/kubernetes-sigs/descheduler"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kubernetes Descheduler: rebalanceamento contínuo de clusters via evicção coordenada com o kube-scheduler

## Em uma frase
O Descheduler para Kubernetes (`sigs.k8s.io/descheduler`) identifica pods agendados em nós subótimos devido a mudanças dinâmicas no cluster e os despeja (evicts) para que o `kube-scheduler` padrão os reagende em nós melhores.

## Por que importa
O `kube-scheduler` toma sua decisão apenas no instante exato em que um pod pendente aparece para agendamento. Como clusters Kubernetes são altamente dinâmicos — alguns nós ficam sobrecarregados ou subutilizados ao longo do tempo, labels e taints são adicionados ou removidos de nós, nós falham concentrando pods em outros servidores ou novos nós entram no cluster —, a decisão original de agendamento deixa de ser ideal, exigindo o Descheduler para restaurar o equilíbrio.

## Como funciona
Conforme documentado no README oficial do projeto, o Descheduler pode ser executado dentro do cluster como um `Job`, `CronJob` ou `Deployment` (ou instalado via Helm chart oficial e Kustomize), rodando como um pod crítico no namespace `kube-system` para evitar ser despejado por si mesmo ou pelo kubelet. Com base em uma `DeschedulerPolicy` configurável, ele avalia os nós e pods ativos e invoca a API de Eviction nos pods que devem ser movidos; o Descheduler **não agenda** diretamente os substitutos dos pods despejados, delegando essa responsabilidade inteiramente ao `kube-scheduler` padrão quando o controlador pai (Deployment, ReplicaSet, StatefulSet) recria o pod.

## Exemplo
```bash
# Instalação do Descheduler como CronJob usando Kustomize a partir do repositório oficial
kustomize build 'github.com/kubernetes-sigs/descheduler/kubernetes/cronjob?ref=release-1.34' | kubectl apply -f -

# Verificação dos pods e jobs do Descheduler no namespace kube-system
kubectl get cronjob,jobs,pods -n kube-system -l app=descheduler
```

## Limites e trade-offs
Como o Descheduler apenas despeja o pod e confia no `kube-scheduler` para reagendá-lo, se as estratégias do Descheduler estiverem desalinhadas com os predicados e prioridades do `kube-scheduler`, um pod despejado pode acabar sendo reagendado exatamente no mesmo nó de onde saiu (ou causar flapping contínuo entre dois nós), gerando disrupção sem ganho real de balanceamento.

## Como verificar
Execute o Descheduler como `Job` ou aguarde a execução do `CronJob` no namespace `kube-system` e inspecione `kubectl logs -n kube-system -l app=descheduler` para verificar a contagem de pods avaliados e despejados em cada ciclo.

## Conexões
- [[descheduler-politica-top-level-limites-eviccao-provedores-metricas]] — Veja também: Kubernetes Descheduler: configuração top-level da DeschedulerPolicy, limites de evicção e metricsProviders.
- [[descheduler-default-evictor-pod-protections-filtros]] — Referência cruzada direta com descheduler-default-evictor-pod-protections-filtros.

## Fontes
- [Kubernetes Descheduler GitHub — README.md (DeschedulerPolicy, DefaultEvictor & Strategy Plugins)](https://raw.githubusercontent.com/kubernetes-sigs/descheduler/master/README.md) — README oficial do Kubernetes Descheduler detalhando configurações top-level, DefaultEvictor com podProtections e plugins dos pontos de extensão Deschedule e Balance; consultado em 2026-10-03.
- [Kubernetes Descheduler Official Helm Chart — README.md](https://github.com/kubernetes-sigs/descheduler/blob/master/charts/descheduler/README.md) — Documentação oficial do Helm chart do Kubernetes Descheduler para implantação como CronJob, Job ou Deployment no kube-system; consultado em 2026-10-03.
- [Kubernetes Descheduler — Official GitHub Repository](https://github.com/kubernetes-sigs/descheduler) — Repositório oficial do projeto kubernetes-sigs/descheduler; consultado em 2026-10-03.
