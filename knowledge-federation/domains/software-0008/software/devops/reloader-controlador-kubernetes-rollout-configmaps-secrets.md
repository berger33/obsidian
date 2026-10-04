---
id: software.devops.tranche11.001031
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

# Stakater Reloader: controlador Kubernetes para rollout automático de workloads após alterações em ConfigMaps e Secrets

## Em uma frase
O Stakater Reloader (`stakater/Reloader`, Apache-2.0, com a versão v2 reconstruída sobre o Operator SDK) é um controlador Kubernetes que observa alterações em `ConfigMaps`, `Secrets` e segredos montados via CSI, disparando automaticamente rolling restarts nos workloads dependentes (`Deployment`, `StatefulSet`, `DaemonSet`, `Argo Rollout`, `CronJob`, `Job` e `DeploymentConfig`).

## Por que importa
No Kubernetes padrão, atualizar os dados de um `ConfigMap` ou `Secret` (por exemplo, quando o External Secrets Operator, o Bitnami Sealed Secrets ou o cert-manager rotaciona uma senha de banco ou certificado TLS) **não** reinicia os pods em execução, e variáveis de ambiente injetadas na inicialização permanecem estáticas com o valor antigo. O Reloader elimina essa defasagem sem exigir mudanças no código da aplicação.

## Como funciona
Conforme descrevem o README oficial e a documentação em `docs.stakater.com/reloader/latest/`, o Reloader utiliza a **watch API** do Kubernetes para receber eventos em tempo real quando um `ConfigMap` ou `Secret` é modificado. Ele verifica se os **dados (`data`)** realmente mudaram (ignorando alterações puras de metadados) e, caso positivo, localiza todos os workloads com anotações correspondentes e aplica um patch no `pod template` (injetando uma variável de ambiente com o hash SHA1 do recurso ou atualizando uma anotação). O Kubernetes detecta a mudança no template do pod e executa um `RollingUpdate` seguro respeitando `maxUnavailable` e `PodDisruptionBudgets`.

## Exemplo
```bash
# Instalar o Stakater Reloader no cluster Kubernetes utilizando o Helm chart oficial
helm repo add stakater https://stakater.github.io/stakater-charts
helm repo update
helm install reloader stakater/reloader \
  --namespace reloader \
  --create-namespace
```

## Limites e trade-offs
Como o Reloader aciona um rolling restart dos pods sempre que o conteúdo de um `ConfigMap` ou `Secret` observado muda, aplicações sem `readinessProbe` configurada ou com apenas uma réplica sem `PodDisruptionBudget` podem sofrer breve indisponibilidade durante o restart automático.

## Como verificar
Verifique se o controlador está em execução com `kubectl -n reloader get pods` e inspecione a métrica Prometheus `reloader_reload_executed_total` após atualizar um `ConfigMap` de teste.

## Conexões
- [[reloader-anotacoes-auto-secret-configmap-regras-precedencia]] — Veja também: Descoberta automática no Reloader: anotações auto, tipadas (secret/configmap) e flag --auto-reload-all.
- [[reloader-padroes-named-reload-search-match-ignore]] — Referência cruzada direta com reloader-padroes-named-reload-search-match-ignore.
- [[externalsecrets-operador-kubernetes-sincronizacao-segredos-externos]] — Referência cruzada direta com externalsecrets-operador-kubernetes-sincronizacao-segredos-externos.

## Fontes
- [Stakater Reloader GitHub — README.md (Reloader v2 Operator SDK, Annotations, Search/Match, Argo Rollouts, Pause & CSI Support)](https://raw.githubusercontent.com/stakater/Reloader/master/README.md) — README oficial do stakater/Reloader detalhando anotações auto/named/search+match/ignore, estratégia restart para Argo Rollouts, alertas webhook, pause-period e integração com Secrets Store CSI Driver; consultado em 2026-10-03.
- [Stakater Reloader Official Documentation — Overview & Mechanics (Watch API, SHA1 Data Check, Workloads & GitOps)](https://docs.stakater.com/reloader/latest/) — Documentação oficial do Reloader explicando a detecção de mudança de dados reais via watch API, patch SHA1 no pod template, workloads suportados e integração com ESO, Sealed Secrets, cert-manager e Argo CD; consultado em 2026-10-03.
- [Stakater Reloader — Official GitHub Repository](https://github.com/stakater/Reloader) — Repositório oficial Apache-2.0 do Stakater Reloader; consultado em 2026-10-03.
