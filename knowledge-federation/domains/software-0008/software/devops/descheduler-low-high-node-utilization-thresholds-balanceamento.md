---
id: software.devops.tranche07.000675
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

# Kubernetes Descheduler: estratégias de balanceamento de recursos LowNodeUtilization e HighNodeUtilization

## Em uma frase
Os plugins de balanceamento `LowNodeUtilization` (espalhamento de carga de nós sobrecarregados para nós subutilizados) e `HighNodeUtilization` (compactação/bin-packing de nós subutilizados) usam `thresholds` e `targetThresholds` de CPU, memória e pods.

## Por que importa
Em clusters com número fixo de nós ou logo após a entrada de novos nós vazios, alguns servidores acumulam 85% de alocação enquanto outros ficam em 15% (`LowNodeUtilization`); inversamente, em clusters elásticos com Cluster Autoscaler sob baixa demanda, espalhar poucos pods em muitos nós impede o scale-down das máquinas subutilizadas (`HighNodeUtilization`). Segundo o README oficial do Descheduler, essas duas estratégias opostas de `balance` resolvem ambos os cenários.

## Como funciona
No **`LowNodeUtilization`**, configuram-se dois patamares sob `nodeResourceUtilizationThresholds`: `thresholds` (limite inferior) e `targetThresholds` (limite superior) em porcentagem de capacidade alocável para `cpu`, `memory`, `pods` e recursos estendidos. Um nó cujo uso está abaixo de `thresholds` para **todos** os recursos é considerado subutilizado; um nó cujo uso está acima de `targetThresholds` para **qualquer** recurso é considerado sobreutilizado; nós entre as duas faixas são considerados adequadamente utilizados. O plugin despeja pods dos nós sobreutilizados na esperança de que sejam reagendados nos nós subutilizados. Já o **`HighNodeUtilization`** atua na direção oposta (compactação): identifica nós subutilizados abaixo de `thresholds` e despeja seus pods para que se concentrem nos demais nós mais cheios, liberando nós vazios para remoção pelo autoscaler.

## Exemplo
```yaml
# Configuração do plugin LowNodeUtilization para balancear CPU, memória e contagem de pods entre nós
  - name: "LowNodeUtilization"
    args:
      thresholds:
        cpu: 20
        memory: 20
        pods: 20
      targetThresholds:
        cpu: 50
        memory: 50
        pods: 50
```

## Limites e trade-offs
Nunca habilite `LowNodeUtilization` e `HighNodeUtilization` simultaneamente para o mesmo conjunto de nós sem compreendê-los, pois o primeiro tenta espalhar carga enquanto o segundo tenta compactar carga; além disso, se `HighNodeUtilization` for usado em conjunto com o `kube-scheduler` padrão configurado com `LeastAllocated` (espalhamento padrão), os pods despejados de nós vazios voltarão a ser espalhados a menos que o scheduler utilize perfil `MostAllocated`.

## Como verificar
Monitore a distribuição de `kubectl top nodes` e `kubectl describe nodes` (seção `Allocated resources`) antes e depois do ciclo do Descheduler para validar que a diferença de alocação entre os nós convergiu para a faixa entre `thresholds` e `targetThresholds`.

## Conexões
- [[descheduler-pontos-extensao-deschedule-balance-perfis]] — Veja também: Kubernetes Descheduler: arquitetura de perfis e pontos de extensão Deschedule versus Balance.
- [[descheduler-remove-duplicates-topology-spread-constraints]] — Veja também: Kubernetes Descheduler: espalhamento de réplicas com RemoveDuplicates e RemovePodsViolatingTopologySpreadConstraint.
- [[descheduler-rebalanceamento-pods-kubernetes-kube-scheduler]] — Referência cruzada direta com descheduler-rebalanceamento-pods-kubernetes-kube-scheduler.
- [[descheduler-politica-top-level-limites-eviccao-provedores-metricas]] — Referência cruzada direta com descheduler-politica-top-level-limites-eviccao-provedores-metricas.

## Fontes
- [Kubernetes Descheduler GitHub — README.md (DeschedulerPolicy, DefaultEvictor & Strategy Plugins)](https://raw.githubusercontent.com/kubernetes-sigs/descheduler/master/README.md) — README oficial do Kubernetes Descheduler detalhando configurações top-level, DefaultEvictor com podProtections e plugins dos pontos de extensão Deschedule e Balance; consultado em 2026-10-03.
- [Kubernetes Descheduler Official Helm Chart — README.md](https://github.com/kubernetes-sigs/descheduler/blob/master/charts/descheduler/README.md) — Documentação oficial do Helm chart do Kubernetes Descheduler para implantação como CronJob, Job ou Deployment no kube-system; consultado em 2026-10-03.
- [Kubernetes Descheduler — Official GitHub Repository](https://github.com/kubernetes-sigs/descheduler) — Repositório oficial do projeto kubernetes-sigs/descheduler; consultado em 2026-10-03.
