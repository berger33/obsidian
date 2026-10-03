---
id: software.devops.tranche10.000915
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

# External Secrets Operator: personas (Cluster Operator vs App Developer), controle de acesso e múltiplos controladores

## Em uma frase
O ESO separa as responsabilidades entre **Cluster Operator** e **Application Developer** via RBAC e políticas de admissão (OPA/Kyverno), permitindo ainda isolar instâncias do controlador por meio do campo `spec.controller` no `SecretStore`.

## Por que importa
Como alerta a seção `Access Control` da documentação oficial (`external-secrets.io/latest/introduction/overview/`), o deployment do ESO roda no cluster com privilégios elevados para criar, ler e atualizar `Secret`s nos namespaces e acessar APIs externas de segredos; uma configuração frouxa de `SecretStore` permitiria que um desenvolvedor lesse segredos de outra equipe.

## Como funciona
A arquitetura de segurança recomendada na página `API Overview` estrutura-se em quatro camadas: (1) **Personas e RBAC**: o **Cluster Operator** instala o ESO, gerencia políticas de acesso e configura `ClusterSecretStores`, enquanto o **Application Developer** tem permissão RBAC apenas para criar `ExternalSecrets` em seu próprio namespace; (2) **Least Privilege no Provedor**: as credenciais entregues a cada `SecretStore` devem ter permissão mínima apenas sobre o prefixo daquela aplicação no cofre externo; (3) **Admission Control**: uso de **OPA Gatekeeper** ou **Kyverno** para validar quais chaves (`remoteRef.key`) cada namespace pode solicitar em um `ExternalSecret`; e (4) **Multiple Controllers**: é possível rodar múltiplos deployments do ESO no mesmo cluster, onde cada instância processa apenas `SecretStores` cujo campo **`spec.controller`** corresponda ao seu identificador.

## Exemplo
```yaml
# Vincular um SecretStore a uma instância específica do controlador ESO usando o campo spec.controller
apiVersion: external-secrets.io/v1
kind: SecretStore
metadata:
  name: pci-secretstore
  namespace: payments
spec:
  controller: pci-restricted-controller
  provider:
    vault:
      server: "https://vault.interno.empresa.com"
      path: "pci-kv"
      version: "v2"
```

## Limites e trade-offs
Conforme observa o passo 1 da seção `Behavior` da documentação oficial, se o `SecretStore` referenciado por um `ExternalSecret` não existir ou se o campo `spec.controller` do `SecretStore` não corresponder à instância do controlador ESO em execução, o controlador simplesmente ignorará aquele `ExternalSecret` sem processá-lo; verifique sempre a correspondência de `--controller-class` quando utilizar múltiplos controladores.

## Como verificar
Inspecione as ClusterRoles do ESO com `kubectl get clusterrole | grep external-secrets` e audite os `SecretStores` para confirmar o escopo mínimo das credenciais configuradas.

## Conexões
- [[externalsecrets-extracao-lote-datafrom-extract-find-rewrite]] — Veja também: External Secrets Operator: extração de múltiplas chaves com dataFrom (extract, find e rewrite).
- [[externalsecrets-provedores-suportados-aws-vault-gcp-azure-pulumi]] — Veja também: External Secrets Operator: integração multi-provedor (AWS, Vault, GCP, Azure, IBM, Akeyless, CyberArk e Pulumi ESC).
- [[externalsecrets-operador-kubernetes-sincronizacao-segredos-externos]] — Referência cruzada direta com externalsecrets-operador-kubernetes-sincronizacao-segredos-externos.
- [[externalsecrets-modelo-recursos-secretstore-externalsecret-clustersecretstore]] — Referência cruzada direta com externalsecrets-modelo-recursos-secretstore-externalsecret-clustersecretstore.

## Fontes
- [External Secrets Operator GitHub — README.md (Supported Providers, CNCF Governance & Release SBOMs)](https://raw.githubusercontent.com/external-secrets/external-secrets/main/README.md) — README oficial do External Secrets Operator (ESO) listando provedores suportados (AWS, Vault, GCP, Azure, IBM, Akeyless, CyberArk, Pulumi ESC) e anexação de SBOM e proveniência; consultado em 2026-10-03.
- [External Secrets Operator Documentation — API Overview (SecretStore, ClusterSecretStore, ExternalSecret, Reconciliation & Access Control)](https://external-secrets.io/latest/introduction/overview/) — Visão geral oficial da arquitetura e modelo de recursos do ESO detalhando SecretStore, ClusterSecretStore, ExternalSecret, ciclo de reconciliação de 5 passos, personas RBAC e múltiplos controladores; consultado em 2026-10-03.
- [External Secrets Operator — Official GitHub Repository](https://github.com/external-secrets/external-secrets) — Repositório oficial Apache-2.0 do projeto external-secrets/external-secrets; consultado em 2026-10-03.
