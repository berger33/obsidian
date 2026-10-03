---
id: software.devops.tranche10.000916
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

# External Secrets Operator: integração multi-provedor (AWS, Vault, GCP, Azure, IBM, Akeyless, CyberArk e Pulumi ESC)

## Em uma frase
Conforme lista o README oficial do projeto, o ESO integra dezenas de sistemas externos sob a mesma especificação de `ExternalSecret`, incluindo **AWS Secrets Manager / Parameter Store**, **HashiCorp Vault**, **Google Cloud Secret Manager**, **Azure Key Vault**, **IBM Cloud Secrets Manager**, **Akeyless**, **CyberArk** e **Pulumi ESC**.

## Por que importa
Empresas que operam em arquiteturas multi-cloud ou híbridas (por exemplo, clusters EKS na AWS, AKS no Azure e clusters on-premises com HashiCorp Vault) costumam sofrer porque os manifestos Helm das aplicações precisam mudar dependendo da nuvem onde o cluster roda. Com o ESO, o manifesto `ExternalSecret` da aplicação permanece o mesmo, mudando apenas o `SecretStore` subjacente.

## Como funciona
Cada provedor suportado é configurado sob uma chave específica dentro de `spec.provider` no `SecretStore` ou `ClusterSecretStore` (ex.: `spec.provider.aws`, `spec.provider.vault`, `spec.provider.gcpsm`, `spec.provider.azurekv`, `spec.provider.ibm`, `spec.provider.akeyless`, `spec.provider.conjur`, `spec.provider.pulumi`). Além de autenticação por `secretRef` (chaves estáticas guardadas em um Secret de bootstrap), os provedores principais suportam autenticação nativa sem chave estática vinculada à identidade do pod no Kubernetes — como **AWS IRSA / Pod Identity**, **GCP Workload Identity**, **Azure Workload Identity** e **Vault Kubernetes Auth**.

## Exemplo
```yaml
# Exemplo de ClusterSecretStore integrando o Google Cloud Secret Manager (gcpsm) ao cluster Kubernetes
apiVersion: external-secrets.io/v1
kind: ClusterSecretStore
metadata:
  name: gcp-secret-store
spec:
  provider:
    gcpsm:
      projectID: meu-projeto-gcp-prod
```

## Limites e trade-offs
Embora a estrutura do `ExternalSecret` seja portátil entre provedores, a semântica de nomes de chaves (`remoteRef.key`) e versões (`remoteRef.version`) segue as regras do provedor configurado no `SecretStore` (por exemplo, o Azure Key Vault não permite barras `/` nem underscores `_` no nome do segredo, aceitando apenas caracteres alfanuméricos e hifens `-`); padronize convenções de nomenclatura compatíveis se planeja migrar entre provedores.

## Como verificar
Execute `kubectl describe clustersecretstore <nome>` para verificar se o provedor autenticou com sucesso na API externa (`Status: Valid`, `Reason: StoreConfigured`).

## Conexões
- [[externalsecrets-seguranca-rbac-least-privilege-multi-controller]] — Veja também: External Secrets Operator: personas (Cluster Operator vs App Developer), controle de acesso e múltiplos controladores.
- [[externalsecrets-pushsecret-sincronizacao-reversa-kubernetes-para-cofre]] — Veja também: External Secrets Operator: sincronização reversa de segredos do cluster para o cofre externo com PushSecret.
- [[externalsecrets-operador-kubernetes-sincronizacao-segredos-externos]] — Referência cruzada direta com externalsecrets-operador-kubernetes-sincronizacao-segredos-externos.
- [[externalsecrets-modelo-recursos-secretstore-externalsecret-clustersecretstore]] — Referência cruzada direta com externalsecrets-modelo-recursos-secretstore-externalsecret-clustersecretstore.
- [[vault-integracao-kubernetes-auth-injector-csi-eso]] — Referência cruzada direta com vault-integracao-kubernetes-auth-injector-csi-eso.

## Fontes
- [External Secrets Operator GitHub — README.md (Supported Providers, CNCF Governance & Release SBOMs)](https://raw.githubusercontent.com/external-secrets/external-secrets/main/README.md) — README oficial do External Secrets Operator (ESO) listando provedores suportados (AWS, Vault, GCP, Azure, IBM, Akeyless, CyberArk, Pulumi ESC) e anexação de SBOM e proveniência; consultado em 2026-10-03.
- [External Secrets Operator Documentation — API Overview (SecretStore, ClusterSecretStore, ExternalSecret, Reconciliation & Access Control)](https://external-secrets.io/latest/introduction/overview/) — Visão geral oficial da arquitetura e modelo de recursos do ESO detalhando SecretStore, ClusterSecretStore, ExternalSecret, ciclo de reconciliação de 5 passos, personas RBAC e múltiplos controladores; consultado em 2026-10-03.
- [External Secrets Operator — Official GitHub Repository](https://github.com/external-secrets/external-secrets) — Repositório oficial Apache-2.0 do projeto external-secrets/external-secrets; consultado em 2026-10-03.
