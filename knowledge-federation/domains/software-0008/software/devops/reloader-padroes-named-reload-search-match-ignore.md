---
id: software.devops.tranche11.001033
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

# Controle granular no Reloader: recursos nomeados (reload), modo opt-in (search + match) e exclusão (ignore)

## Em uma frase
Para cenários onde nem todo `ConfigMap` ou `Secret` deve reiniciar o pod, o Reloader oferece três mecanismos granulares: anotações por nome (**`secret.reloader.stakater.com/reload`** e **`configmap.reloader.stakater.com/reload`**), o par opt-in **`search: "true"` + `match: "true"`** e a anotação de bloqueio global **`reloader.stakater.com/ignore: "true"`**.

## Por que importa
Em clusters multi-tenant ou aplicações que montam dezenas de `ConfigMaps` (alguns lidos dinamicamente via hot-reload de disco pela própria aplicação e outros lidos apenas no boot via variáveis de ambiente), reiniciar o pod em toda alteração de qualquer ConfigMap gera rollouts desnecessários.

## Como funciona
Segundo o README oficial do Reloader: (1) **Named Resource Reload**: anotar o workload com `secret.reloader.stakater.com/reload: "db-secret,jwt-secret"` ou `configmap.reloader.stakater.com/reload: "app-config"` dispara o rollout apenas quando os recursos nomeados mudam, independentemente de como são usados no pod spec; (2) **Targeted Reload (`search` + `match`)**: o workload recebe `reloader.stakater.com/search: "true"` e somente os `ConfigMaps`/`Secrets` que estiverem simultaneamente referenciados pelo workload **e** anotados com `reloader.stakater.com/match: "true"` disparam restart; e (3) **Resource-Level Ignore**: anotar um `ConfigMap` ou `Secret` com **`reloader.stakater.com/ignore: "true"`** instrui o Reloader a ignorar completamente aquele recurso em todos os workloads do cluster.

## Exemplo
```yaml
# Padrão Search + Match: o Deployment só reinicia quando um Secret referenciado possui match: "true"
apiVersion: v1
kind: Secret
metadata:
  name: credenciais-rotativas
  annotations:
    reloader.stakater.com/match: "true"
type: Opaque
stringData:
  API_KEY: "valor-inicial"
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: worker-integracao
  annotations:
    reloader.stakater.com/search: "true"
```

## Limites e trade-offs
A anotação `reloader.stakater.com/ignore: "true"` aplicada em um `ConfigMap` ou `Secret` tem efeito global sobre aquele recurso: mesmo que um Deployment o liste explicitamente em `configmap.reloader.stakater.com/reload`, o Reloader pulará toda a lógica de reload para aquele recurso ignorado.

## Como verificar
Atualize um ConfigMap referenciado sem a anotação `match: "true"` em um Deployment com `search: "true"` e confirme que nenhuma nova revisão de `ReplicaSet` é criada; em seguida, atualize o Secret com `match: "true"` e confirme o rollout.

## Conexões
- [[reloader-anotacoes-auto-secret-configmap-regras-precedencia]] — Veja também: Descoberta automática no Reloader: anotações auto, tipadas (secret/configmap) e flag --auto-reload-all.
- [[reloader-integracao-gitops-argocd-argo-rollouts-estrategias]] — Veja também: Reloader com GitOps (Argo CD / Flux) e Argo Rollouts: reload-strategy annotations e rollout-strategy restart.
- [[reloader-controlador-kubernetes-rollout-configmaps-secrets]] — Referência cruzada direta com reloader-controlador-kubernetes-rollout-configmaps-secrets.

## Fontes
- [Stakater Reloader GitHub — README.md (Reloader v2 Operator SDK, Annotations, Search/Match, Argo Rollouts, Pause & CSI Support)](https://raw.githubusercontent.com/stakater/Reloader/master/README.md) — README oficial do stakater/Reloader detalhando anotações auto/named/search+match/ignore, estratégia restart para Argo Rollouts, alertas webhook, pause-period e integração com Secrets Store CSI Driver; consultado em 2026-10-03.
- [Stakater Reloader Official Documentation — Overview & Mechanics (Watch API, SHA1 Data Check, Workloads & GitOps)](https://docs.stakater.com/reloader/latest/) — Documentação oficial do Reloader explicando a detecção de mudança de dados reais via watch API, patch SHA1 no pod template, workloads suportados e integração com ESO, Sealed Secrets, cert-manager e Argo CD; consultado em 2026-10-03.
- [Stakater Reloader — Official GitHub Repository](https://github.com/stakater/Reloader) — Repositório oficial Apache-2.0 do Stakater Reloader; consultado em 2026-10-03.
