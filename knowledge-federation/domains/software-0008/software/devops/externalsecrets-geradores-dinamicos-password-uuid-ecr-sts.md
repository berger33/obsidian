---
id: software.devops.tranche10.000918
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

# External Secrets Operator: geração dinâmica de segredos e tokens com Generators (Password, UUID, ECR, VaultDynamicSecret)

## Em uma frase
O ESO inclui recursos **Generators** (`sourceRef.generatorRef` no `ExternalSecret`) capazes de produzir senhas aleatórias fortes (`Password`), `UUID`s, tokens temporários de registry (`ECRAuthorizationToken`, `ACR`, `GCR`) ou segredos dinâmicos (`VaultDynamicSecret`) sem depender de valores estáticos pré-gravados.

## Por que importa
Nem todo segredo que um pod precisa no Kubernetes é um valor estático armazenado manualmente: para puxar imagens de um registry privado AWS ECR (cujo token de login expira a cada 12 horas) ou gerar uma senha aleatória inicial para um banco de dados local, um gerador dinâmico automatiza a emissão e a renovação diretamente pelo `ExternalSecret`.

## Como funciona
Em vez de apontar um item de `spec.dataFrom` para uma chave estática em um `SecretStore`, o `ExternalSecret` referencia um CRD de **Generator** em **`dataFrom[].sourceRef.generatorRef`** (como `kind: Password`, `kind: UUID`, `kind: Fake`, `kind: ECRAuthorizationToken` ou `kind: VaultDynamicSecret`). A cada ciclo de `refreshInterval` do `ExternalSecret`, o ESO invoca o gerador — por exemplo, chamando a API `GetAuthorizationToken` da AWS ECR para obter um novo token válido por 12 horas — e atualiza o `Secret` do Kubernetes.

## Exemplo
```yaml
# Exemplo de Generator Password combinado com um ExternalSecret para gerar uma senha criptográfica forte
apiVersion: generators.external-secrets.io/v1alpha1
kind: Password
metadata:
  name: db-strong-pass-gen
  namespace: app-ns
spec:
  length: 32
  digits: 6
  symbols: 6
  noUpper: false
  allowRepeat: true
```

## Limites e trade-offs
Atenção ao usar geradores aleatórios puros (como `kind: Password` ou `kind: UUID`) em um `ExternalSecret`: se `refreshInterval` estiver definido como `1h` (o padrão), o gerador criará uma **nova senha aleatória diferente a cada 1 hora** sobrescrevendo o `Secret`! Para gerar uma senha aleatória apenas uma única vez na criação inicial e nunca mais trocá-la automaticamente, defina **`refreshInterval: "0"`** no `ExternalSecret`.

## Como verificar
Crie o gerador `Password` e um `ExternalSecret` com `refreshInterval: "0"`, aplique no cluster e verifique com `kubectl get secret <nome> -o jsonpath='{.data.password}' | base64 -d | wc -c` a senha de 32 caracteres gerada.

## Conexões
- [[externalsecrets-pushsecret-sincronizacao-reversa-kubernetes-para-cofre]] — Veja também: External Secrets Operator: sincronização reversa de segredos do cluster para o cofre externo com PushSecret.
- [[externalsecrets-cadeia-suprimentos-sbom-proveniencia-arquitetura-deployments]] — Veja também: External Secrets Operator: arquitetura de componentes no cluster (core controller, webhook, cert-controller) e SBOMs de release.
- [[externalsecrets-operador-kubernetes-sincronizacao-segredos-externos]] — Referência cruzada direta com externalsecrets-operador-kubernetes-sincronizacao-segredos-externos.
- [[externalsecrets-ciclo-reconciliacao-creationpolicy-templates]] — Referência cruzada direta com externalsecrets-ciclo-reconciliacao-creationpolicy-templates.
- [[vault-segredos-dinamicos-leases-renovacao-revogacao]] — Referência cruzada direta com vault-segredos-dinamicos-leases-renovacao-revogacao.

## Fontes
- [External Secrets Operator GitHub — README.md (Supported Providers, CNCF Governance & Release SBOMs)](https://raw.githubusercontent.com/external-secrets/external-secrets/main/README.md) — README oficial do External Secrets Operator (ESO) listando provedores suportados (AWS, Vault, GCP, Azure, IBM, Akeyless, CyberArk, Pulumi ESC) e anexação de SBOM e proveniência; consultado em 2026-10-03.
- [External Secrets Operator Documentation — API Overview (SecretStore, ClusterSecretStore, ExternalSecret, Reconciliation & Access Control)](https://external-secrets.io/latest/introduction/overview/) — Visão geral oficial da arquitetura e modelo de recursos do ESO detalhando SecretStore, ClusterSecretStore, ExternalSecret, ciclo de reconciliação de 5 passos, personas RBAC e múltiplos controladores; consultado em 2026-10-03.
- [External Secrets Operator — Official GitHub Repository](https://github.com/external-secrets/external-secrets) — Repositório oficial Apache-2.0 do projeto external-secrets/external-secrets; consultado em 2026-10-03.
