---
id: software.devops.tranche11.001034
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-11.md"
fontes: ["https://raw.githubusercontent.com/stakater/Reloader/master/README.md", "https://docs.stakater.com/reloader/latest/", "https://github.com/stakater/Reloader"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Reloader com GitOps (Argo CD / Flux) e Argo Rollouts: reload-strategy annotations e rollout-strategy restart

## Em uma frase
Para evitar *Configuration Drift* (`OutOfSync`) em ferramentas GitOps como o Argo CD e controlar entregas progressivas no **Argo Rollouts** (`--is-argo-rollouts=true`), o Reloader suporta a estratégia de reload baseada em anotações (`--reload-strategy=annotations`) e a anotação `reloader.stakater.com/rollout-strategy: "restart"`.

## Por que importa
Por padrão, quando o Reloader injeta ou modifica variáveis de ambiente (`env-vars`) ou o `pod template` de um recurso gerenciado pelo Argo CD ou Argo Rollouts, o controlador GitOps pode detectar a mutação no spec do workload como divergência em relação ao Git (*OutOfSync*). Ajustar a estratégia de reload e de rollout elimina esse atrito operacional.

## Como funciona
Conforme explicam o README oficial e o portal `docs.stakater.com/reloader/latest/`: (1) para compatibilidade com **Argo CD**, usa-se a estratégia de reload **`annotations`** (`--reload-strategy=annotations`), na qual o Reloader atualiza uma anotação no metadata do pod template em vez de adicionar variáveis de ambiente `STAKATER_*` na lista de containers; e (2) especificamente para recursos **`Argo Rollout`** (que exigem habilitar `--is-argo-rollouts=true` ou `reloader.isArgoRollouts: true` no Helm), o comportamento padrão (`reloader.stakater.com/rollout-strategy: "rollout"`) atualiza o pod template para acionar um rollout completo, mas você pode definir **`reloader.stakater.com/rollout-strategy: "restart"`** para deletar/reiniciar o pod diretamente sem modificar o pod template, evitando drift no GitOps.

## Exemplo
```yaml
# Configurar um recurso Argo Rollout para usar a estratégia restart sem modificar o pod template no GitOps
apiVersion: argoproj.io/v1alpha1
kind: Rollout
metadata:
  name: checkout-service
  annotations:
    reloader.stakater.com/auto: "true"
    reloader.stakater.com/rollout-strategy: "restart"
spec:
  replicas: 3
  strategy:
    canary:
      steps:
        - setWeight: 50
        - pause: { duration: 1m }
```

## Limites e trade-offs
Conforme ressalta a documentação oficial, a anotação `reloader.stakater.com/rollout-strategy: "restart"` aplica-se **exclusivamente** a recursos do **Argo Rollouts** (sendo ignorada por `Deployments`, `StatefulSets` e `DaemonSets` padrão do Kubernetes, que sempre realizam rolling update via atualização do pod template).

## Como verificar
Habilite `reloader.isArgoRollouts=true` e `reloader.reloadStrategy=annotations` no Helm chart do Reloader e verifique no painel do Argo CD que a aplicação permanece `Synced` após a rotação de um Secret.

## Conexões
- [[reloader-padroes-named-reload-search-match-ignore]] — Veja também: Controle granular no Reloader: recursos nomeados (reload), modo opt-in (search + match) e exclusão (ignore).
- [[reloader-integracao-secrets-store-csi-driver-podstatus]] — Veja também: Suporte do Reloader ao Secrets Store CSI Driver (SecretProviderClassPodStatus e --enable-csi-integration).
- [[reloader-controlador-kubernetes-rollout-configmaps-secrets]] — Referência cruzada direta com reloader-controlador-kubernetes-rollout-configmaps-secrets.

## Fontes
- [Stakater Reloader GitHub — README.md (Reloader v2 Operator SDK, Annotations, Search/Match, Argo Rollouts, Pause & CSI Support)](https://raw.githubusercontent.com/stakater/Reloader/master/README.md) — README oficial do stakater/Reloader detalhando anotações auto/named/search+match/ignore, estratégia restart para Argo Rollouts, alertas webhook, pause-period e integração com Secrets Store CSI Driver; consultado em 2026-10-03.
- [Stakater Reloader Official Documentation — Overview & Mechanics (Watch API, SHA1 Data Check, Workloads & GitOps)](https://docs.stakater.com/reloader/latest/) — Documentação oficial do Reloader explicando a detecção de mudança de dados reais via watch API, patch SHA1 no pod template, workloads suportados e integração com ESO, Sealed Secrets, cert-manager e Argo CD; consultado em 2026-10-03.
- [Stakater Reloader — Official GitHub Repository](https://github.com/stakater/Reloader) — Repositório oficial Apache-2.0 do Stakater Reloader; consultado em 2026-10-03.
