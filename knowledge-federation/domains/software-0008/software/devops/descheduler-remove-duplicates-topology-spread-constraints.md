---
id: software.devops.tranche07.000676
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

# Kubernetes Descheduler: espalhamento de réplicas com RemoveDuplicates e RemovePodsViolatingTopologySpreadConstraint

## Em uma frase
Os plugins de balanceamento `RemoveDuplicates` e `RemovePodsViolatingTopologySpreadConstraint` garantem a alta disponibilidade das aplicações despejando réplicas concentradas no mesmo nó ou que violem restrições de distribuição topológica entre zonas e nós.

## Por que importa
Quando um nó worker falha temporariamente em um cluster Kubernetes, os pods de um `Deployment` ou `StatefulSet` que rodavam nele são recriados nos nós sobreviventes, fazendo com que múltiplas réplicas do mesmo serviço acabem empilhadas no mesmo nó ou na mesma zona de disponibilidade; quando o nó que falhou volta a ficar `Ready`, o Kubernetes não move os pods de volta sozinho. O README oficial do Descheduler documenta os plugins `RemoveDuplicates` e `RemovePodsViolatingTopologySpreadConstraint` para corrigir esse desbalanceamento.

## Como funciona
O plugin **`RemoveDuplicates`** verifica se existe mais de um pod associado ao mesmo `ReplicaSet` (RS), `ReplicationController` (RC), `StatefulSet` ou `Job` rodando no mesmo nó; se houver duplicatas e outros nós estiverem disponíveis, os pods extras são despejados para melhorar o espalhamento (aceitando o parâmetro opcional `excludeOwnerKinds`, onde incluir `ReplicaSet` exclui pods criados por Deployments). Já o plugin **`RemovePodsViolatingTopologySpreadConstraint`** inspeciona os pods que declaram `spec.topologySpreadConstraints` (por exemplo, `maxSkew: 1` por `topology.kubernetes.io/zone` ou `kubernetes.io/hostname`) e despeja o número mínimo de pods dos domínios sobrecarregados para restaurar o `maxSkew` exigido.

## Exemplo
```yaml
# Configuração dos plugins RemoveDuplicates e RemovePodsViolatingTopologySpreadConstraint no perfil
    pluginConfig:
      - name: "RemoveDuplicates"
        args:
          excludeOwnerKinds:
            - "Job"
      - name: "RemovePodsViolatingTopologySpreadConstraint"
        args:
          constraints:
            - DoNotSchedule
            - ScheduleAnyway
    plugins:
      balance:
        enabled:
          - "RemoveDuplicates"
          - "RemovePodsViolatingTopologySpreadConstraint"
```

## Limites e trade-offs
Se um `Deployment` possuir mais réplicas do que o número total de nós disponíveis no cluster (por exemplo, 10 réplicas em um cluster de 4 nós), sempre haverá múltiplas réplicas no mesmo nó; o `RemoveDuplicates` calcula o teto ideal por nó para evitar despejos inúteis, mas exige atenção especial quando combinado com afinidades restritivas de nó.

## Como verificar
Verifique a distribuição de pods de um Deployment com `kubectl get pods -o wide` após simular a drenagem (`kubectl drain`) e retorno (`kubectl uncordon`) de um nó e rodar um ciclo do Descheduler.

## Conexões
- [[descheduler-low-high-node-utilization-thresholds-balanceamento]] — Veja também: Kubernetes Descheduler: estratégias de balanceamento de recursos LowNodeUtilization e HighNodeUtilization.
- [[descheduler-violacoes-affinity-anti-affinity-node-taints]] — Veja também: Kubernetes Descheduler: correção de violações de afinidade, anti-afinidade e taints de nós.
- [[descheduler-rebalanceamento-pods-kubernetes-kube-scheduler]] — Referência cruzada direta com descheduler-rebalanceamento-pods-kubernetes-kube-scheduler.
- [[descheduler-pontos-extensao-deschedule-balance-perfis]] — Referência cruzada direta com descheduler-pontos-extensao-deschedule-balance-perfis.

## Fontes
- [Kubernetes Descheduler GitHub — README.md (DeschedulerPolicy, DefaultEvictor & Strategy Plugins)](https://raw.githubusercontent.com/kubernetes-sigs/descheduler/master/README.md) — README oficial do Kubernetes Descheduler detalhando configurações top-level, DefaultEvictor com podProtections e plugins dos pontos de extensão Deschedule e Balance; consultado em 2026-10-03.
- [Kubernetes Descheduler Official Helm Chart — README.md](https://github.com/kubernetes-sigs/descheduler/blob/master/charts/descheduler/README.md) — Documentação oficial do Helm chart do Kubernetes Descheduler para implantação como CronJob, Job ou Deployment no kube-system; consultado em 2026-10-03.
- [Kubernetes Descheduler — Official GitHub Repository](https://github.com/kubernetes-sigs/descheduler) — Repositório oficial do projeto kubernetes-sigs/descheduler; consultado em 2026-10-03.
