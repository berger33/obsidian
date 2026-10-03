---
id: software.devops.tranche11.001039
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
fontes: ["https://docs.stakater.com/reloader/latest/", "https://raw.githubusercontent.com/stakater/Reloader/master/README.md", "https://github.com/stakater/Reloader"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Mecânica interna do Reloader: comparação de dados reais (SHA1) versus metadados e estratégias de patch no Pod Template

## Em uma frase
Ao receber um evento de atualização da watch API do Kubernetes, o Reloader calcula e compara se os **dados (`data` / `binaryData`)** do `ConfigMap` ou `Secret` realmente mudaram (ignorando alterações apenas em labels ou annotations) e aplica o patch no `pod template` usando o hash **SHA1** do recurso.

## Por que importa
Controladores GitOps (como Argo CD e Flux), operadores de backup (como Velero) e ferramentas de auditoria frequentemente adicionam ou atualizam labels e annotations nos objetos `ConfigMap` e `Secret` sem alterar seus valores de configuração. Se o Reloader reagisse a qualquer mudança de `metadata.resourceVersion`, todo sync de metadados causaria reinicializações em massa no cluster.

## Como funciona
Conforme explica a seção *How it works* da documentação oficial (`docs.stakater.com/reloader/latest/`): (1) um `ConfigMap` ou `Secret` é atualizado na API do Kubernetes; (2) o Reloader recebe o evento via watch API e verifica se o conteúdo de dados realmente mudou em comparação ao estado anterior; (3) somente se houve alteração de dados, o Reloader localiza os workloads anotados que dependem daquele recurso; e (4) aplica um patch no `spec.template` do workload — seja injetando/atualizando uma variável de ambiente contendo o hash SHA1 do recurso (estratégia `env-vars`), seja atualizando uma anotação no pod template (estratégia `annotations`). O controller-manager do Kubernetes detecta a diferença no `spec.template` e executa o rolling restart.

## Exemplo
```bash
# Inspecionar o pod template de um Deployment após um reload para ver a mutação aplicada pelo Reloader
kubectl get deployment api-pagamentos -o yaml | grep -E "STAKATER|reloader.stakater.com"
```

## Limites e trade-offs
A estratégia padrão baseada em variáveis de ambiente (`env-vars`) adiciona uma variável `STAKATER_<RESOURCE>_<TYPE>` com o hash SHA1 no container; embora inofensiva para a maioria das aplicações, ela altera a lista de variáveis de ambiente do container (o que pode acusar diff no Argo CD se não for usada a estratégia `annotations`).

## Como verificar
Adicione apenas uma label arbitrária a um `ConfigMap` observado (`kubectl label configmap api-config teste=123`) e confirme que o Reloader **não** reinicia os pods porque o campo `data` permaneceu idêntico.

## Conexões
- [[reloader-evolucao-v2-operator-sdk-workloads-suportados]] — Veja também: Arquitetura do Reloader v2 (Operator SDK) e matriz de workloads suportados (Deployment, StatefulSet, DaemonSet, CronJob, Job e DeploymentConfig).
- [[reloader-integracao-pilha-segredos-eso-sealedsecrets-certmanager]] — Veja também: Integração do Reloader com a pilha de segredos: External Secrets Operator, Sealed Secrets, cert-manager e Vault.
- [[reloader-controlador-kubernetes-rollout-configmaps-secrets]] — Referência cruzada direta com reloader-controlador-kubernetes-rollout-configmaps-secrets.
- [[reloader-integracao-gitops-argocd-argo-rollouts-estrategias]] — Referência cruzada direta com reloader-integracao-gitops-argocd-argo-rollouts-estrategias.

## Fontes
- [Stakater Reloader GitHub — README.md (Reloader v2 Operator SDK, Annotations, Search/Match, Argo Rollouts, Pause & CSI Support)](https://docs.stakater.com/reloader/latest/) — README oficial do stakater/Reloader detalhando anotações auto/named/search+match/ignore, estratégia restart para Argo Rollouts, alertas webhook, pause-period e integração com Secrets Store CSI Driver; consultado em 2026-10-03.
- [Stakater Reloader Official Documentation — Overview & Mechanics (Watch API, SHA1 Data Check, Workloads & GitOps)](https://raw.githubusercontent.com/stakater/Reloader/master/README.md) — Documentação oficial do Reloader explicando a detecção de mudança de dados reais via watch API, patch SHA1 no pod template, workloads suportados e integração com ESO, Sealed Secrets, cert-manager e Argo CD; consultado em 2026-10-03.
- [Stakater Reloader — Official GitHub Repository](https://github.com/stakater/Reloader) — Repositório oficial Apache-2.0 do Stakater Reloader; consultado em 2026-10-03.
