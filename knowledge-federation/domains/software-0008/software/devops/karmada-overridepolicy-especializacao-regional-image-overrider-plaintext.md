---
id: software.devops.tranche17.001606
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

# Karmada: customização por cluster via `OverridePolicy` (`imageOverrider`, `plaintext`, `labelsOverrider`)

## Em uma frase
A API `OverridePolicy` (e `ClusterOverridePolicy`, em `policy.karmada.io/v1alpha1`) permite aplicar mutações específicas para cada cluster, nuvem ou região no momento em que o `Binding Controller` gera o objeto `Work`, sem alterar o manifesto base.

## Por que importa
Mesmo quando a aplicação é idêntica em todos os clusters, detalhes de infraestrutura variam: o cluster na AWS usa a `StorageClass` `gp3` e um registry ECR regional, enquanto o cluster no GCP usa `standard-rwo` e Artifact Registry.

## Como funciona
O `OverridePolicy` suporta `overrideRules` direcionadas por `targetCluster`. Dentro de `overriders`, o Karmada oferece operadores semânticos prontos — como `imageOverrider` (para substituir, adicionar ou remover `Registry`, `Repository` ou `Tag`), `commandOverrider`, `argsOverrider`, `labelsOverrider`, `annotationsOverrider` — além de `plaintext` (patches JSONPatch `add`, `replace`, `remove` por `path`).

## Exemplo
```yaml
apiVersion: policy.karmada.io/v1alpha1
kind: OverridePolicy
metadata:
  name: regional-registry-override
spec:
  resourceSelectors:
    - apiVersion: apps/v1
      kind: Deployment
      name: checkout
  overrideRules:
    - targetCluster:
        clusterNames: [member-cn]
      overriders:
        imageOverrider:
          - component: Registry
            operator: replace
            value: registry.cn-hangzhou.aliyuncs.com
```

## Limites e trade-offs
As regras dentro de `overrideRules` são avaliadas em ordem sequencial de declaração; se múltiplas `OverridePolicies` se aplicarem ao mesmo recurso, `ClusterOverridePolicy` é processada antes de `OverridePolicy`.

## Como verificar
Inspecione o objeto `Work` gerado em `karmada-es-member-cn` (`kubectl get work -n karmada-es-member-cn -o yaml`) e confirme que a imagem do container teve o domínio do registry substituído.

## Conexões
- [[karmada-replica-scheduling-duplicated-divided-static-dynamic-weight]] — Veja também: Karmada: estratégias de divisão de réplicas (`Duplicated` vs `Divided`, `StaticWeight` vs `DynamicWeight`).
- [[karmada-spreadconstraints-alta-disponibilidade-multi-dimensao-regiao-az]] — Veja também: Karmada: restrições de espalhamento multi-dimensional (`spreadConstraints`) por provedor, região, zona e cluster.

## Fontes
- [Karmada GitHub — README.md (Kubernetes Armada CNCF Incubating Multi-Cloud & Multi-Cluster Kubernetes Orchestration)](https://raw.githubusercontent.com/karmada-io/karmada/master/README.md) — README oficial do karmada-io/karmada (CNCF Incubating) apresentando capacidades multi-cluster, API compatível com Kubernetes nativo e políticas de propagação; consultado em 2026-10-03.
- [Karmada Official Documentation — Core Concepts: Architecture (Control Plane, PropagationPolicy, OverridePolicy, ResourceBinding, Work & Agent)](https://karmada.io/docs/core-concepts/architecture/) — Documentação oficial de arquitetura do Karmada detalhando API Server, Controller Manager, Karmada Scheduler, Execution Space e sincronização para member clusters; consultado em 2026-10-03.
- [Karmada — Official GitHub Repository](https://github.com/karmada-io/karmada) — Repositório oficial Apache-2.0 do projeto Karmada na CNCF; consultado em 2026-10-03.
