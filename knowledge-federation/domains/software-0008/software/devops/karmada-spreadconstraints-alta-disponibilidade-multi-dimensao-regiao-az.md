---
id: software.devops.tranche17.001607
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

# Karmada: restrições de espalhamento multi-dimensional (`spreadConstraints`) por provedor, região, zona e cluster

## Em uma frase
Dentro de `spec.placement.spreadConstraints`, o Karmada permite exigir que uma carga de trabalho seja distribuída entre múltiplos domínios de falha (`spreadByField`: `cluster`, `region`, `zone`, `provider` ou `spreadByLabel`) com limites `minGroups` e `maxGroups`.

## Por que importa
Apenas selecionar "quaisquer 3 clusters" por label pode acidentalmente escolher 3 clusters localizados na mesma região (`us-east-1`) do mesmo provedor de nuvem; se aquela região inteira cair, a aplicação sai do ar.

## Como funciona
Ao declarar dois itens em `spreadConstraints` — um com `spreadByField: provider` (`minGroups: 2`) e outro com `spreadByField: cluster` (`minGroups: 3`, `maxGroups: 3`) — o `karmada-scheduler` garante matematicamente que os 3 clusters escolhidos estejam divididos entre pelo menos 2 provedores de nuvem distintos.

## Exemplo
```yaml
apiVersion: policy.karmada.io/v1alpha1
kind: PropagationPolicy
metadata:
  name: geo-redundant-placement
spec:
  resourceSelectors:
    - apiVersion: apps/v1
      kind: Deployment
      name: core-ledger
  placement:
    spreadConstraints:
      - spreadByField: region
        minGroups: 2
        maxGroups: 2
      - spreadByField: cluster
        minGroups: 2
        maxGroups: 4
```

## Limites e trade-offs
Para que `spreadByField: region`, `zone` ou `provider` funcione, os objetos `Cluster` registrados no Karmada devem ter suas respectivas propriedades de topologia preenchidas (via flags do `karmadactl join/register` ou especificação do objeto `Cluster`).

## Como verificar
Verifique `kubectl get clusters -o custom-columns=NAME:.metadata.name,PROVIDER:.spec.provider,REGION:.spec.region,ZONE:.spec.zone` antes de aplicar políticas multi-dimensionais.

## Conexões
- [[karmada-overridepolicy-especializacao-regional-image-overrider-plaintext]] — Veja também: Karmada: customização por cluster via `OverridePolicy` (`imageOverrider`, `plaintext`, `labelsOverrider`).
- [[karmada-failover-automatico-cluster-application-taints-eviction]] — Veja também: Karmada: failover automático de cluster e de aplicação com reagendamento de réplicas e preservação de estado.

## Fontes
- [Karmada GitHub — README.md (Kubernetes Armada CNCF Incubating Multi-Cloud & Multi-Cluster Kubernetes Orchestration)](https://raw.githubusercontent.com/karmada-io/karmada/master/README.md) — README oficial do karmada-io/karmada (CNCF Incubating) apresentando capacidades multi-cluster, API compatível com Kubernetes nativo e políticas de propagação; consultado em 2026-10-03.
- [Karmada Official Documentation — Core Concepts: Architecture (Control Plane, PropagationPolicy, OverridePolicy, ResourceBinding, Work & Agent)](https://karmada.io/docs/core-concepts/architecture/) — Documentação oficial de arquitetura do Karmada detalhando API Server, Controller Manager, Karmada Scheduler, Execution Space e sincronização para member clusters; consultado em 2026-10-03.
- [Karmada — Official GitHub Repository](https://github.com/karmada-io/karmada) — Repositório oficial Apache-2.0 do projeto Karmada na CNCF; consultado em 2026-10-03.
