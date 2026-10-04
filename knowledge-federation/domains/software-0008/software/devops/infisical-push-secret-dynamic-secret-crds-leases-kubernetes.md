---
id: software.devops.tranche20.001954
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

# Infisical `InfisicalPushSecret` e `InfisicalDynamicSecret`: envio de segredos gerados no cluster e leases dinâmicos

## Em uma frase
Além de puxar segredos estáticos do Infisical para o cluster, o operador oferece dois CRDs especializados: **`InfisicalPushSecret`** (que empurra segredos gerados dentro do Kubernetes para o Infisical) e **`InfisicalDynamicSecret`** (que gera credenciais efêmeras sob demanda no Infisical, cria leases com TTL e atualiza o `Secret` do Kubernetes automaticamente antes do vencimento).

## Por que importa
Às vezes um operador dentro do Kubernetes (como o `cert-manager` ou um operador de banco de dados CloudNativePG) gera uma credencial ou certificado que precisa ser exportado para o Infisical para uso externo (`InfisicalPushSecret`); em outros casos, um Pod precisa de credenciais de banco dinâmicas renovadas continuamente (`InfisicalDynamicSecret`).

## Como funciona
Quando um `InfisicalDynamicSecret` é aplicado, o controlador solicita uma nova credencial ao *Dynamic Secret Producer* do Infisical (PostgreSQL, MySQL, RabbitMQ, AWS IAM), grava o usuário/senha no `Secret` Kubernetes de destino e monitora o lease para renová-lo ou recriá-lo automaticamente.

## Exemplo
```yaml
apiVersion: secrets.infisical.com/v1alpha1
kind: InfisicalDynamicSecret
metadata:
  name: pg-dynamic-creds
  namespace: app-prod
spec:
  managedSecretReference:
    secretName: pg-ephemeral-secret
    secretNamespace: app-prod
```

## Limites e trade-offs
Combine `InfisicalDynamicSecret` com o auto-reload de Deployments do operador para que os Pods recebam as novas credenciais sempre que um lease atingir seu `maxTTL` e for rotacionado.

## Como verificar
Inspecione as condições de status e o lease ativo com `kubectl describe infisicaldynamicsecret pg-dynamic-creds -n app-prod`.

## Conexões
- [[infisical-crds-v1beta1-infisicalconnection-infisicalauth-staticsecret]] — Veja também: Infisical Operator API `v1beta1`: desacoplamento entre `InfisicalConnection`, `InfisicalAuth` e `InfisicalStaticSecret`.
- [[infisical-auto-reload-deployments-annotations-rollout-zero-downtime]] — Veja também: Infisical Auto-Reload no Kubernetes: reinicialização rolling automática de `Deployments` quando segredos mudam.

## Fontes
- [Infisical GitHub — README.md (Open-Source Secret Management, PKI, KMS & PAM Platform, CLI, Leak Prevention, Honey Tokens & Agent Vault)](https://infisical.com/docs/integrations/platforms/kubernetes/overview) — README oficial do Infisical/infisical detalhando gerenciamento de segredos, Point-in-Time Recovery, Honey Tokens, Agent Vault, PKI, KMS e PAM; consultado em 2026-10-03.
- [Infisical Official Documentation — Kubernetes Operator Overview (v1beta1 InfisicalConnection/InfisicalAuth/InfisicalStaticSecret, Push/Dynamic Secrets & Auto-Reload)](https://raw.githubusercontent.com/Infisical/infisical/main/README.md) — Documentação oficial do Infisical Kubernetes Operator cobrindo instalação Cluster-wide vs Namespace-scoped, CRDs v1beta1, auto-reload e métricas Prometheus; consultado em 2026-10-03.
- [Infisical — Official GitHub Repository](https://github.com/Infisical/infisical) — Repositório oficial MIT do Infisical; consultado em 2026-10-03.
