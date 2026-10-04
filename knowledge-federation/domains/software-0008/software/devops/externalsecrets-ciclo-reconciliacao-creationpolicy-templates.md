---
id: software.devops.tranche10.000913
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

# External Secrets Operator: ciclo de reconciliação (refreshInterval), creationPolicy e templates de Secret

## Em uma frase
Durante a reconciliação de um `ExternalSecret`, o ESO instancia o cliente do `SecretStore`, busca e decodifica as chaves na frequência definida por `refreshInterval` e cria ou atualiza o `Kind=Secret` usando `target.creationPolicy` e `target.template`.

## Por que importa
Muitas aplicações legado ou Helm charts de terceiros não aceitam chaves de segredo nos mesmos nomes gravados no AWS Secrets Manager ou no Vault — elas exigem um arquivo `config.json`, uma string de conexão `DATABASE_URL` montada a partir de usuário/senha ou um Secret do tipo `kubernetes.io/tls` / `kubernetes.io/dockerconfigjson`.

## Como funciona
Conforme descreve a seção `Behavior` em `external-secrets.io/latest/introduction/overview/`, o ESO reconcilia o `ExternalSecret` em 5 passos: (1) usa `spec.secretStoreRef` para localizar o `SecretStore`/`ClusterSecretStore`; (2) instancia o cliente da API externa; (3) busca os segredos solicitados em `spec.data` (`remoteRef.key`, `version`, `property`) ou `spec.dataFrom` (`extract`); (4) cria/atualiza o `Kind=Secret` definido em **`spec.target.name`** aplicando **`spec.target.creationPolicy`** (`Owner` — o padrão, que define `ownerReference` para apagar o Secret quando o ExternalSecret for removido; `Orphan`; `Merge` — injeta chaves em um Secret existente; ou `None`) e renderizando **`spec.target.template`**; e (5) reexecuta a sincronização a cada **`spec.refreshInterval`** (ex.: `1h0m0s`).

## Exemplo
```yaml
# Exemplo oficial de ExternalSecret (v1) buscando propriedade específica e sincronizando a cada 1 hora
apiVersion: external-secrets.io/v1
kind: ExternalSecret
metadata:
  name: database-credentials
  namespace: app-ns
spec:
  refreshInterval: 1h0m0s
  secretStoreRef:
    name: secretstore-sample
    kind: SecretStore
  target:
    name: db-secret-k8s
    creationPolicy: Owner
  data:
    - secretKey: db-password
      remoteRef:
        key: prod/database/postgres
        property: password
```

## Limites e trade-offs
Configurar um `refreshInterval` extremamente baixo (por exemplo, `1s` ou `5s`) em centenas de `ExternalSecret`s que apontam para provedores de nuvem tarifados por chamada de API (como AWS Secrets Manager ou GCP Secret Manager) gerará milhões de requisições mensais à API da nuvem, podendo causar throttling (rate limit) e custos inesperados na fatura; use intervalos razoáveis (como `15m` ou `1h`) e anote o recurso para forçar refresh imediato quando necessário.

## Como verificar
Inspecione o status de sincronização com `kubectl get externalsecret database-credentials -n app-ns` confirmando `STATUS: SecretSynced` e `READY: True`.

## Conexões
- [[externalsecrets-modelo-recursos-secretstore-externalsecret-clustersecretstore]] — Veja também: External Secrets Operator: separação de responsabilidades entre SecretStore, ClusterSecretStore e ExternalSecret.
- [[externalsecrets-extracao-lote-datafrom-extract-find-rewrite]] — Veja também: External Secrets Operator: extração de múltiplas chaves com dataFrom (extract, find e rewrite).
- [[externalsecrets-operador-kubernetes-sincronizacao-segredos-externos]] — Referência cruzada direta com externalsecrets-operador-kubernetes-sincronizacao-segredos-externos.

## Fontes
- [External Secrets Operator GitHub — README.md (Supported Providers, CNCF Governance & Release SBOMs)](https://raw.githubusercontent.com/external-secrets/external-secrets/main/README.md) — README oficial do External Secrets Operator (ESO) listando provedores suportados (AWS, Vault, GCP, Azure, IBM, Akeyless, CyberArk, Pulumi ESC) e anexação de SBOM e proveniência; consultado em 2026-10-03.
- [External Secrets Operator Documentation — API Overview (SecretStore, ClusterSecretStore, ExternalSecret, Reconciliation & Access Control)](https://external-secrets.io/latest/introduction/overview/) — Visão geral oficial da arquitetura e modelo de recursos do ESO detalhando SecretStore, ClusterSecretStore, ExternalSecret, ciclo de reconciliação de 5 passos, personas RBAC e múltiplos controladores; consultado em 2026-10-03.
- [External Secrets Operator — Official GitHub Repository](https://github.com/external-secrets/external-secrets) — Repositório oficial Apache-2.0 do projeto external-secrets/external-secrets; consultado em 2026-10-03.
