---
id: software.devops.tranche20.001955
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-20.md"
fontes: ["https://infisical.com/docs/integrations/platforms/kubernetes/overview", "https://raw.githubusercontent.com/Infisical/infisical/main/README.md", "https://github.com/Infisical/infisical"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Infisical Auto-Reload no Kubernetes: reinicialização rolling automática de `Deployments` quando segredos mudam

## Em uma frase
O Infisical Kubernetes Operator suporta **auto-reload automático de `Deployments`**: sempre que um segredo sincronizado no Kubernetes é atualizado pelo operador (devido a uma edição no painel, rotação agendada ou expiração de lease dinâmico), o operador dispara um rolling restart automático dos `Deployments` dependentes.

## Por que importa
Por padrão no Kubernetes, quando o conteúdo de um `Secret` referenciado via `envFrom` ou `valueFrom.secretKeyRef` muda, os Pods que já estão rodando **não** recebem os novos valores nas variáveis de ambiente até serem recriados.

## Como funciona
Ao adicionar a anotação de auto-reload do Infisical (`secrets.infisical.com/auto-reload: "true"`) nos metadados do `Deployment`, o operador calcula o hash da revisão do `Secret` gerenciado e atualiza o `spec.template.metadata.annotations` do Deployment assim que detecta mudança no valor do segredo.

## Exemplo
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: payment-api
  namespace: app-prod
  annotations:
    secrets.infisical.com/auto-reload: "true"
spec:
  replicas: 3
  template:
    spec:
      containers:
        - name: api
          image: ghcr.io/org/payment-api:1.4.0
          envFrom:
            - secretRef:
                name: backend-env-secret
```

## Limites e trade-offs
Garanta que o `Deployment` anotado com `auto-reload: "true"` possua `readinessProbe` e `PodDisruptionBudget` adequados para que o rolling update acionado pela mudança de segredo ocorra com zero downtime.

## Como verificar
Altere um valor no Infisical, aguarde o ciclo de resync do operador e observe `kubectl rollout status deploy/payment-api -n app-prod`.

## Conexões
- [[infisical-push-secret-dynamic-secret-crds-leases-kubernetes]] — Veja também: Infisical `InfisicalPushSecret` e `InfisicalDynamicSecret`: envio de segredos gerados no cluster e leases dinâmicos.
- [[infisical-secret-scanning-leak-prevention-git-pre-commit-ci]] — Veja também: Infisical Secret Scanning e Leak Prevention (`infisical scan`): detecção preventiva de vazamentos em commits Git e pipelines CI.

## Fontes
- [Infisical GitHub — README.md (Open-Source Secret Management, PKI, KMS & PAM Platform, CLI, Leak Prevention, Honey Tokens & Agent Vault)](https://infisical.com/docs/integrations/platforms/kubernetes/overview) — README oficial do Infisical/infisical detalhando gerenciamento de segredos, Point-in-Time Recovery, Honey Tokens, Agent Vault, PKI, KMS e PAM; consultado em 2026-10-03.
- [Infisical Official Documentation — Kubernetes Operator Overview (v1beta1 InfisicalConnection/InfisicalAuth/InfisicalStaticSecret, Push/Dynamic Secrets & Auto-Reload)](https://raw.githubusercontent.com/Infisical/infisical/main/README.md) — Documentação oficial do Infisical Kubernetes Operator cobrindo instalação Cluster-wide vs Namespace-scoped, CRDs v1beta1, auto-reload e métricas Prometheus; consultado em 2026-10-03.
- [Infisical — Official GitHub Repository](https://github.com/Infisical/infisical) — Repositório oficial MIT do Infisical; consultado em 2026-10-03.
