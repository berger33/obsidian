---
id: software.devops.tranche20.001952
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

# Infisical Kubernetes Operator: modos de instalação `Cluster-wide` vs `Namespace-scoped` (`scopedNamespaces` e `scopedRBAC`)

## Em uma frase
O **Infisical Kubernetes Operator** (instalado via Helm chart `infisical-helm-charts/secrets-operator` e testado em EKS, GKE, AKS, OKE e OpenShift nas versões Kubernetes 1.29 a 1.33+) é um conjunto de controladores Kubernetes que sincroniza segredos bidirecionalmente entre o Infisical e o cluster e gerencia leases dinâmicos.

## Por que importa
Em clusters multi-tenant onde equipes de produto compartilham o mesmo cluster Kubernetes, um operador único com `ClusterRole` para ler e escrever `Secrets` em todos os namespaces pode violar políticas de isolamento estritas.

## Como funciona
Conforme documentado no guia oficial do operador, você pode escolher entre dois modos de instalação no Helm: 1) **Cluster-wide** (padrão, onde o operador observa CRDs em todos os namespaces); ou 2) **Namespace-scoped** (`--set scopedNamespaces=ns1 --set scopedRBAC=true`), que restringe as permissões RBAC do operador exclusivamente aos namespaces listados.

## Exemplo
```bash
helm repo add infisical-helm-charts 'https://dl.cloudsmith.io/public/infisical/helm-charts/helm/charts/'
helm repo update

# Instalação restrita a uma lista específica de namespaces com RBAC de escopo reduzido:
helm install infisical-operator infisical-helm-charts/secrets-operator \
  --namespace infisical-operator-system \
  --create-namespace \
  --set "scopedNamespaces={app-staging,app-prod}" \
  --set scopedRBAC=true
```

## Limites e trade-offs
Se você instalar múltiplas instâncias separadas do operador (uma por namespace), defina `installCRDs: true` apenas na **primeira** instalação e `installCRDs: false` nas instalações subsequentes para evitar conflitos de propriedade sobre os CRDs cluster-wide.

## Como verificar
Verifique o Pod do operador em execução com `kubectl get pods -n infisical-operator-system`.

## Conexões
- [[infisical-arquitetura-open-source-secrets-pki-kms-pam-platform]] — Veja também: Infisical: arquitetura da plataforma open-source de gerenciamento de segredos, PKI, KMS e acesso privilegiado (PAM).
- [[infisical-crds-v1beta1-infisicalconnection-infisicalauth-staticsecret]] — Veja também: Infisical Operator API `v1beta1`: desacoplamento entre `InfisicalConnection`, `InfisicalAuth` e `InfisicalStaticSecret`.

## Fontes
- [Infisical GitHub — README.md (Open-Source Secret Management, PKI, KMS & PAM Platform, CLI, Leak Prevention, Honey Tokens & Agent Vault)](https://infisical.com/docs/integrations/platforms/kubernetes/overview) — README oficial do Infisical/infisical detalhando gerenciamento de segredos, Point-in-Time Recovery, Honey Tokens, Agent Vault, PKI, KMS e PAM; consultado em 2026-10-03.
- [Infisical Official Documentation — Kubernetes Operator Overview (v1beta1 InfisicalConnection/InfisicalAuth/InfisicalStaticSecret, Push/Dynamic Secrets & Auto-Reload)](https://raw.githubusercontent.com/Infisical/infisical/main/README.md) — Documentação oficial do Infisical Kubernetes Operator cobrindo instalação Cluster-wide vs Namespace-scoped, CRDs v1beta1, auto-reload e métricas Prometheus; consultado em 2026-10-03.
- [Infisical — Official GitHub Repository](https://github.com/Infisical/infisical) — Repositório oficial MIT do Infisical; consultado em 2026-10-03.
