---
id: software.devops.tranche10.000917
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

# External Secrets Operator: sincronização reversa de segredos do cluster para o cofre externo com PushSecret

## Em uma frase
Enquanto o `ExternalSecret` puxa segredos do provedor externo para o Kubernetes, o CRD **`PushSecret`** realiza o caminho inverso: lê um `Secret` existente dentro do Kubernetes e o publica automaticamente no gerenciador de segredos externo (`SecretStore`).

## Por que importa
Muitos operadores dentro do próprio cluster Kubernetes geram segredos localmente — por exemplo, certificados TLS emitidos pelo `cert-manager`, credenciais de banco criadas pelo operador CloudNativePG/Crossplane ou tokens de ServiceAccount — que precisam ser exportados com segurança para o AWS Secrets Manager ou HashiCorp Vault para consumo por sistemas fora do cluster (ou por outros clusters).

## Como funciona
O usuário cria um recurso **`PushSecret`** no mesmo namespace do `Secret` de origem, especificando: (1) **`spec.selector.secret.name`**: o nome do `Secret` nativo do Kubernetes que servirá de fonte; (2) **`spec.secretStoreRefs`**: a lista de `SecretStore`s ou `ClusterSecretStore`s de destino para onde o segredo deve ser enviado; (3) **`spec.data`**: o mapeamento entre a chave local (`match.secretKey`) e o caminho de destino no cofre remoto (`match.remoteRef.remoteKey` e opcionalmente `property`); e (4) **`spec.deletionPolicy`** (`Delete` ou `None`), que controla se o segredo remoto no cofre externo deve ser apagado quando o `PushSecret` for removido do cluster.

## Exemplo
```yaml
# Exemplo de PushSecret exportando um certificado ou chave gerada no cluster para o SecretStore remoto
apiVersion: external-secrets.io/v1alpha1
kind: PushSecret
metadata:
  name: push-tls-cert
  namespace: app-ns
spec:
  refreshInterval: 1h
  secretStoreRefs:
    - name: secretstore-sample
      kind: SecretStore
  selector:
    secret:
      name: app-tls-secret
  data:
    - match:
        secretKey: tls.crt
        remoteRef:
          remoteKey: prod/app/tls-cert
```

## Limites e trade-offs
Para que o `PushSecret` funcione, a identidade de autenticação configurada no `SecretStore` precisa ter permissões de **escrita/criação (`CreateSecret` / `PutSecretValue` / `write`)** no cofre externo; nunca reutilize para leitura comum de aplicações o mesmo `SecretStore` que possui permissão de escrita irrestrita no cofre se você quiser impedir que workloads sobrescrevam segredos corporativos.

## Como verificar
Execute `kubectl get pushsecret -n app-ns` e `kubectl describe pushsecret push-tls-cert -n app-ns` para confirmar que o segredo foi gravado com sucesso no provedor remoto (`Synced`).

## Conexões
- [[externalsecrets-provedores-suportados-aws-vault-gcp-azure-pulumi]] — Veja também: External Secrets Operator: integração multi-provedor (AWS, Vault, GCP, Azure, IBM, Akeyless, CyberArk e Pulumi ESC).
- [[externalsecrets-geradores-dinamicos-password-uuid-ecr-sts]] — Veja também: External Secrets Operator: geração dinâmica de segredos e tokens com Generators (Password, UUID, ECR, VaultDynamicSecret).
- [[externalsecrets-operador-kubernetes-sincronizacao-segredos-externos]] — Referência cruzada direta com externalsecrets-operador-kubernetes-sincronizacao-segredos-externos.
- [[externalsecrets-modelo-recursos-secretstore-externalsecret-clustersecretstore]] — Referência cruzada direta com externalsecrets-modelo-recursos-secretstore-externalsecret-clustersecretstore.

## Fontes
- [External Secrets Operator GitHub — README.md (Supported Providers, CNCF Governance & Release SBOMs)](https://raw.githubusercontent.com/external-secrets/external-secrets/main/README.md) — README oficial do External Secrets Operator (ESO) listando provedores suportados (AWS, Vault, GCP, Azure, IBM, Akeyless, CyberArk, Pulumi ESC) e anexação de SBOM e proveniência; consultado em 2026-10-03.
- [External Secrets Operator Documentation — API Overview (SecretStore, ClusterSecretStore, ExternalSecret, Reconciliation & Access Control)](https://external-secrets.io/latest/introduction/overview/) — Visão geral oficial da arquitetura e modelo de recursos do ESO detalhando SecretStore, ClusterSecretStore, ExternalSecret, ciclo de reconciliação de 5 passos, personas RBAC e múltiplos controladores; consultado em 2026-10-03.
- [External Secrets Operator — Official GitHub Repository](https://github.com/external-secrets/external-secrets) — Repositório oficial Apache-2.0 do projeto external-secrets/external-secrets; consultado em 2026-10-03.
