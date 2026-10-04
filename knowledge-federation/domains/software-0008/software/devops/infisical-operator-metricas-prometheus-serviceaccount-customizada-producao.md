---
id: software.devops.tranche20.001960
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

# Infisical Operator em Produção: métricas Prometheus (`/metrics`), `ServiceAccount` customizada e migração `v1alpha1` -> `v1beta1`

## Em uma frase
Para operar o Infisical Kubernetes Operator em produção com observabilidade e governança de identidade da nuvem (IRSA na AWS, Workload Identity no GKE/AKS), o chart Helm suporta trazer sua própria **`ServiceAccount`** (`controllerManager.serviceAccount.create: false`, a partir do chart `0.10.11+`) e expõe métricas **Prometheus** no endpoint `/metrics`.

## Por que importa
Quando os Pods do operador usam *AWS IAM Auth* ou *Kubernetes Auth* vinculado a uma `ServiceAccount` pré-provisionada pelo Terraform/IAM, criar uma ServiceAccount genérica nova pelo Helm impediria herdar as anotações de IAM Role.

## Como funciona
No `values.yaml` do chart `secrets-operator`, defina `controllerManager.serviceAccount.create: false` e `controllerManager.serviceAccount.name: my-existing-sa` (garantindo que a ServiceAccount já exista no namespace antes do `helm install`). Monitore também as métricas de reconciliação expostas pelo operador no Prometheus.

## Exemplo
```yaml
# values.yaml para o chart infisical-helm-charts/secrets-operator em produção:
controllerManager:
  serviceAccount:
    create: false
    name: infisical-operator-irsa-sa
scopedNamespaces:
  - prod-workloads
scopedRBAC: true
```

## Limites e trade-offs
Conforme documentado no guia oficial do operador, a `ServiceAccount` customizada informada em `controllerManager.serviceAccount.name` **deve existir previamente** no namespace de instalação antes de executar o `helm install`.

## Como verificar
Verifique a `ServiceAccount` em uso pelo Pod do operador com `kubectl get pod -n infisical-operator-system -o jsonpath='{.items[0].spec.serviceAccountName}'`.

## Conexões
- [[infisical-agent-vault-ai-agents-proxy-injecao-credenciais-kms]] — Veja também: Infisical `Infisical Agent`, `Agent Vault` (para IA) e `KMS`: injeção de segredos sem SDK e proteção contra exfiltração por LLMs.

## Fontes
- [Infisical GitHub — README.md (Open-Source Secret Management, PKI, KMS & PAM Platform, CLI, Leak Prevention, Honey Tokens & Agent Vault)](https://infisical.com/docs/integrations/platforms/kubernetes/overview) — README oficial do Infisical/infisical detalhando gerenciamento de segredos, Point-in-Time Recovery, Honey Tokens, Agent Vault, PKI, KMS e PAM; consultado em 2026-10-03.
- [Infisical Official Documentation — Kubernetes Operator Overview (v1beta1 InfisicalConnection/InfisicalAuth/InfisicalStaticSecret, Push/Dynamic Secrets & Auto-Reload)](https://raw.githubusercontent.com/Infisical/infisical/main/README.md) — Documentação oficial do Infisical Kubernetes Operator cobrindo instalação Cluster-wide vs Namespace-scoped, CRDs v1beta1, auto-reload e métricas Prometheus; consultado em 2026-10-03.
- [Infisical — Official GitHub Repository](https://github.com/Infisical/infisical) — Repositório oficial MIT do Infisical; consultado em 2026-10-03.
