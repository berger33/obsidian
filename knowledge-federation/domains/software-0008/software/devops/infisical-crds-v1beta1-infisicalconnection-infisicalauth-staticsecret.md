---
id: software.devops.tranche20.001953
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

# Infisical Operator API `v1beta1`: desacoplamento entre `InfisicalConnection`, `InfisicalAuth` e `InfisicalStaticSecret`

## Em uma frase
A versão recomendada **`v1beta1`** da API do Infisical Kubernetes Operator separa a configuração de conectividade e de autenticação em Custom Resources reutilizáveis — **`InfisicalConnection`** e **`InfisicalAuth`** — referenciados pelo recurso **`InfisicalStaticSecret`** (que substitui o legado `InfisicalSecret` da `v1alpha1`).

## Por que importa
Na API antiga `v1alpha1`, cada objeto `InfisicalSecret` precisava repetir a URL do servidor Infisical e a configuração de autenticação da *Machine Identity*, dificultando a manutenção quando dezenas de segredos compartilhavam a mesma identidade.

## Como funciona
Com a API `v1beta1`: 1) `InfisicalConnection` define o `hostAPI` e certificados TLS da instância Infisical; 2) `InfisicalAuth` define o método de autenticação da Machine Identity (como *Kubernetes Auth* ou *Universal Auth*); e 3) múltiplos recursos `InfisicalStaticSecret` referenciam ambos para sincronizar pastas/ambientes distintos em `Secrets` nativos do Kubernetes.

## Exemplo
```yaml
apiVersion: secrets.infisical.com/v1beta1
kind: InfisicalStaticSecret
metadata:
  name: backend-prod-secrets
  namespace: app-prod
spec:
  connectionRef:
    name: infisical-cloud-conn
  authRef:
    name: k8s-machine-identity-auth
  projectSlug: "payments-platform"
  envSlug: "prod"
  secretsPath: "/backend"
  destination:
    secretName: "backend-env-secret"
    secretType: Opaque
```

## Limites e trade-offs
Para novas implantações, utilize sempre os CRDs **`v1beta1`** (`InfisicalConnection`, `InfisicalAuth`, `InfisicalStaticSecret`), pois o recurso monolítico `InfisicalSecret` (`v1alpha1`) está marcado para deprecação.

## Como verificar
Execute `kubectl get infisicalconnections,infisicalauths,infisicalstaticsecrets -A` para auditar os recursos `v1beta1` ativos.

## Conexões
- [[infisical-kubernetes-operator-arquitetura-cluster-wide-vs-namespaced]] — Veja também: Infisical Kubernetes Operator: modos de instalação `Cluster-wide` vs `Namespace-scoped` (`scopedNamespaces` e `scopedRBAC`).
- [[infisical-push-secret-dynamic-secret-crds-leases-kubernetes]] — Veja também: Infisical `InfisicalPushSecret` e `InfisicalDynamicSecret`: envio de segredos gerados no cluster e leases dinâmicos.

## Fontes
- [Infisical GitHub — README.md (Open-Source Secret Management, PKI, KMS & PAM Platform, CLI, Leak Prevention, Honey Tokens & Agent Vault)](https://infisical.com/docs/integrations/platforms/kubernetes/overview) — README oficial do Infisical/infisical detalhando gerenciamento de segredos, Point-in-Time Recovery, Honey Tokens, Agent Vault, PKI, KMS e PAM; consultado em 2026-10-03.
- [Infisical Official Documentation — Kubernetes Operator Overview (v1beta1 InfisicalConnection/InfisicalAuth/InfisicalStaticSecret, Push/Dynamic Secrets & Auto-Reload)](https://raw.githubusercontent.com/Infisical/infisical/main/README.md) — Documentação oficial do Infisical Kubernetes Operator cobrindo instalação Cluster-wide vs Namespace-scoped, CRDs v1beta1, auto-reload e métricas Prometheus; consultado em 2026-10-03.
- [Infisical — Official GitHub Repository](https://github.com/Infisical/infisical) — Repositório oficial MIT do Infisical; consultado em 2026-10-03.
