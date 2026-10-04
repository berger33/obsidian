---
id: software.devops.tranche11.001032
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

# Descoberta automática no Reloader: anotações auto, tipadas (secret/configmap) e flag --auto-reload-all

## Em uma frase
O Reloader oferece descoberta automática de dependências via anotação **`reloader.stakater.com/auto: "true"`** (ou suas variantes restritas `secret.reloader.stakater.com/auto: "true"` e `configmap.reloader.stakater.com/auto: "true"`), além do modo global `--auto-reload-all` no controlador com opt-out por workload.

## Por que importa
Em clusters com centenas de microsserviços que consomem `ConfigMaps` e `Secrets` via `envFrom`, `valueFrom` ou `volumes`, listar manualmente o nome de cada recurso em anotações é propenso a esquecimentos quando um desenvolvedor adiciona um novo Secret ao pod spec. O modo `auto` descobre automaticamente todas as referências presentes na especificação do pod.

## Como funciona
Conforme a seção *Automatic Reload* e *Annotation Behavior Rules* do README oficial: (1) **`reloader.stakater.com/auto: "true"`** reinicia o workload quando qualquer `ConfigMap` ou `Secret` referenciado no pod spec mudar; (2) **`secret.reloader.stakater.com/auto: "true"`** restringe o reload automático apenas aos `Secrets` referenciados; (3) **`configmap.reloader.stakater.com/auto: "true"`** restringe apenas aos `ConfigMaps` referenciados; (4) se tanto `auto` quanto suas versões tipadas forem usadas simultaneamente, basta que uma delas seja `"true"` para disparar o reload; e (5) se a flag **`--auto-reload-all`** estiver habilitada no controlador, todos os workloads do cluster são tratados como `auto: "true"`, exceto aqueles que definirem explicitamente `reloader.stakater.com/auto: "false"`.

## Exemplo
```yaml
# Deployment com descoberta automática habilitada para qualquer ConfigMap ou Secret referenciado no pod spec
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-pagamentos
  annotations:
    reloader.stakater.com/auto: "true"
spec:
  replicas: 2
  selector:
    matchLabels:
      app: api-pagamentos
  template:
    metadata:
      labels:
        app: api-pagamentos
    spec:
      containers:
        - name: app
          image: ghcr.io/exemplo/api-pagamentos:v1.4.0
          envFrom:
            - configMapRef:
                name: api-config
            - secretRef:
                name: api-db-secret
```

## Limites e trade-offs
Conforme documentado nas regras de compatibilidade, `reloader.stakater.com/auto` e `reloader.stakater.com/search` **não podem ser usadas juntas** no mesmo workload — se ambas estiverem presentes, a anotação `auto` tem precedência e ignora o filtro `search`.

## Como verificar
Edite o valor de uma chave em `api-config` (`kubectl patch configmap api-config -p '{"data":{"LOG_LEVEL":"debug"}}'`) e observe o início imediato do rollout em `kubectl rollout status deployment/api-pagamentos`.

## Conexões
- [[reloader-controlador-kubernetes-rollout-configmaps-secrets]] — Veja também: Stakater Reloader: controlador Kubernetes para rollout automático de workloads após alterações em ConfigMaps e Secrets.
- [[reloader-padroes-named-reload-search-match-ignore]] — Veja também: Controle granular no Reloader: recursos nomeados (reload), modo opt-in (search + match) e exclusão (ignore).
- [[reloader-pausa-deployments-pause-period-alertas-webhook]] — Referência cruzada direta com reloader-pausa-deployments-pause-period-alertas-webhook.

## Fontes
- [Stakater Reloader GitHub — README.md (Reloader v2 Operator SDK, Annotations, Search/Match, Argo Rollouts, Pause & CSI Support)](https://raw.githubusercontent.com/stakater/Reloader/master/README.md) — README oficial do stakater/Reloader detalhando anotações auto/named/search+match/ignore, estratégia restart para Argo Rollouts, alertas webhook, pause-period e integração com Secrets Store CSI Driver; consultado em 2026-10-03.
- [Stakater Reloader Official Documentation — Overview & Mechanics (Watch API, SHA1 Data Check, Workloads & GitOps)](https://docs.stakater.com/reloader/latest/) — Documentação oficial do Reloader explicando a detecção de mudança de dados reais via watch API, patch SHA1 no pod template, workloads suportados e integração com ESO, Sealed Secrets, cert-manager e Argo CD; consultado em 2026-10-03.
- [Stakater Reloader — Official GitHub Repository](https://github.com/stakater/Reloader) — Repositório oficial Apache-2.0 do Stakater Reloader; consultado em 2026-10-03.
