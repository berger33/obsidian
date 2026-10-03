---
id: software.devops.tranche07.000673
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

# Kubernetes Descheduler: plugin DefaultEvictor, políticas podProtections e filtros de nodeFit e minReplicas

## Em uma frase
O plugin `DefaultEvictor` atua nos extension points `filter` e `preEvictionFilter`, governando quais pods podem ser despejados por meio da estrutura `podProtections` (`defaultDisabled` e `extraEnabled`), `nodeFit`, `minReplicas`, `minPodAge` e `noEvictionPolicy`.

## Por que importa
Despejar inadvertidamente pods críticos de sistema (como `kube-dns`), pods gerenciados por `DaemonSet`, pods com armazenamento local (`emptyDir`/hostPath) ou pods que não possuem outro nó compatível disponível no cluster causaria perda de dados ou pods travados em estado `Pending`. De acordo com o README oficial do Descheduler, o `DefaultEvictor` protege esses workloads por padrão e substitui flags booleanas antigas (agora depreciadas) pela configuração estruturada `podProtections`.

## Como funciona
Por padrão, o `DefaultEvictor` protege contra evicção quatro categorias de pods, que só podem ser despejadas se listadas explicitamente em `podProtections.defaultDisabled`: `"PodsWithLocalStorage"`, `"DaemonSetPods"`, `"SystemCriticalPods"` e `"FailedBarePods"` (substituindo as flags depreciadas `evictLocalStoragePods`, `evictDaemonSetPods`, `evictSystemCriticalPods` e `evictFailedBarePods`). De forma complementar, o administrador pode ativar proteções adicionais em `podProtections.extraEnabled`: `"PodsWithPVC"` (com filtro opcional por `protectedStorageClasses`), `"PodsWithoutPDB"` (protege pods que não possuem `PodDisruptionBudget`) e `"PodsWithResourceClaims"`. Além disso, `nodeFit: true` verifica se existe pelo menos um outro nó no cluster onde o pod cabe antes de despejá-lo, `minReplicas` ignora controladores com poucas réplicas, `minPodAge` protege pods recém-criados e `noEvictionPolicy` (`Preferred` ou `Mandatory`) respeita a anotação `descheduler.alpha.kubernetes.io/prefer-no-eviction`.

## Exemplo
```yaml
# Configuração recomendada do DefaultEvictor com podProtections, nodeFit e minReplicas
profiles:
  - name: DefaultProfile
    pluginConfig:
      - name: "DefaultEvictor"
        args:
          nodeFit: true
          minReplicas: 2
          minPodAge: "10m"
          podProtections:
            extraEnabled:
              - "PodsWithoutPDB"
              - "PodsWithPVC"
            config:
              PodsWithPVC:
                protectedStorageClasses:
                  - name: local-nvme-sc
```

## Limites e trade-offs
Manter `nodeFit: false` (o valor padrão) significa que o Descheduler pode despejar um pod que viola uma regra mesmo quando todos os demais nós do cluster estão cheios ou incompatíveis, deixando o pod substituto em estado `Pending`; por isso, habilitar `nodeFit: true` e `extraEnabled: ["PodsWithoutPDB"]` é altamente recomendado em clusters de produção.

## Como verificar
Inspecione os logs do Descheduler em nível verboso para confirmar que pods com PVCs das classes protegidas, pods sem PDB ou pods que não passariam no `nodeFit` são filtrados pelo `DefaultEvictor` antes da chamada de evicção.

## Conexões
- [[descheduler-politica-top-level-limites-eviccao-provedores-metricas]] — Veja também: Kubernetes Descheduler: configuração top-level da DeschedulerPolicy, limites de evicção e metricsProviders.
- [[descheduler-pontos-extensao-deschedule-balance-perfis]] — Veja também: Kubernetes Descheduler: arquitetura de perfis e pontos de extensão Deschedule versus Balance.
- [[descheduler-rebalanceamento-pods-kubernetes-kube-scheduler]] — Referência cruzada direta com descheduler-rebalanceamento-pods-kubernetes-kube-scheduler.

## Fontes
- [Kubernetes Descheduler GitHub — README.md (DeschedulerPolicy, DefaultEvictor & Strategy Plugins)](https://raw.githubusercontent.com/kubernetes-sigs/descheduler/master/README.md) — README oficial do Kubernetes Descheduler detalhando configurações top-level, DefaultEvictor com podProtections e plugins dos pontos de extensão Deschedule e Balance; consultado em 2026-10-03.
- [Kubernetes Descheduler Official Helm Chart — README.md](https://github.com/kubernetes-sigs/descheduler/blob/master/charts/descheduler/README.md) — Documentação oficial do Helm chart do Kubernetes Descheduler para implantação como CronJob, Job ou Deployment no kube-system; consultado em 2026-10-03.
- [Kubernetes Descheduler — Official GitHub Repository](https://github.com/kubernetes-sigs/descheduler) — Repositório oficial do projeto kubernetes-sigs/descheduler; consultado em 2026-10-03.
