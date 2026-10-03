---
id: software.devops.tranche10.000912
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/external-secrets/external-secrets/main/README.md", "https://external-secrets.io/latest/introduction/overview/", "https://github.com/external-secrets/external-secrets"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# External Secrets Operator: separação de responsabilidades entre SecretStore, ClusterSecretStore e ExternalSecret

## Em uma frase
O modelo de dados do ESO separa **como acessar** o provedor externo (`SecretStore` por namespace ou `ClusterSecretStore` global) de **quais dados buscar** e como montar o segredo final (`ExternalSecret`).

## Por que importa
Em organizações onde a equipe de plataforma gerencia a conectividade e o IAM com a nuvem/Vault e dezenas de equipes de desenvolvimento criam seus próprios microsserviços, misturar credenciais de autenticação do provedor com a lista de chaves de cada aplicação violaria a separação de responsabilidades. A página `API Overview` (`Resource model`) detalha o papel de cada recurso.

## Como funciona
O modelo divide-se em três CRDs principais em `external-secrets.io/v1`: (1) **`SecretStore` (namespaced)**: especifica como autenticar e acessar um provedor externo (ex.: `provider.aws.service: SecretsManager`, região `us-east-1` e credenciais/IRSA), sendo restrito ao próprio namespace; (2) **`ClusterSecretStore` (cluster-scoped)**: um gateway global de armazenamento de segredos que pode ser referenciado por `ExternalSecret`s de **qualquer** namespace autorizado do cluster; e (3) **`ExternalSecret` (namespaced)**: criado pelo desenvolvedor da aplicação, referencia um `SecretStore` ou `ClusterSecretStore` em `spec.secretStoreRef`, declara quais chaves buscar (`spec.data` ou `spec.dataFrom`) e serve como blueprint para gerar o `Secret` nativo (`spec.target`).

## Exemplo
```yaml
# Exemplo oficial de SecretStore (autenticação/acesso) separado do ExternalSecret (o que buscar)
apiVersion: external-secrets.io/v1
kind: SecretStore
metadata:
  name: secretstore-sample
  namespace: app-ns
spec:
  provider:
    aws:
      service: SecretsManager
      region: us-east-1
```

## Limites e trade-offs
Embora o `ClusterSecretStore` evite duplicar configurações de provedor em 50 namespaces diferentes, qualquer namespace que tenha permissão para referenciar aquele `ClusterSecretStore` poderia tentar buscar chaves de outras equipes no mesmo cofre externo se não houver restrição; por isso, em clusters multi-tenant compartilhados, utilize `conditions` de namespace no `ClusterSecretStore` ou prefira `SecretStore`s dedicados por namespace com papéis IAM/Vault isolados.

## Como verificar
Execute `kubectl get secretstore,clustersecretstore -A` e verifique que a coluna `STATUS` exibe `Valid` e `READY` exibe `True`.

## Conexões
- [[externalsecrets-operador-kubernetes-sincronizacao-segredos-externos]] — Veja também: External Secrets Operator (ESO): sincronização declarativa de gerenciadores de segredos externos com Kubernetes Secrets.
- [[externalsecrets-ciclo-reconciliacao-creationpolicy-templates]] — Veja também: External Secrets Operator: ciclo de reconciliação (refreshInterval), creationPolicy e templates de Secret.
- [[externalsecrets-seguranca-rbac-least-privilege-multi-controller]] — Referência cruzada direta com externalsecrets-seguranca-rbac-least-privilege-multi-controller.

## Fontes
- [External Secrets Operator GitHub — README.md (Supported Providers, CNCF Governance & Release SBOMs)](https://raw.githubusercontent.com/external-secrets/external-secrets/main/README.md) — README oficial do External Secrets Operator (ESO) listando provedores suportados (AWS, Vault, GCP, Azure, IBM, Akeyless, CyberArk, Pulumi ESC) e anexação de SBOM e proveniência; consultado em 2026-10-03.
- [External Secrets Operator Documentation — API Overview (SecretStore, ClusterSecretStore, ExternalSecret, Reconciliation & Access Control)](https://external-secrets.io/latest/introduction/overview/) — Visão geral oficial da arquitetura e modelo de recursos do ESO detalhando SecretStore, ClusterSecretStore, ExternalSecret, ciclo de reconciliação de 5 passos, personas RBAC e múltiplos controladores; consultado em 2026-10-03.
- [External Secrets Operator — Official GitHub Repository](https://github.com/external-secrets/external-secrets) — Repositório oficial Apache-2.0 do projeto external-secrets/external-secrets; consultado em 2026-10-03.
