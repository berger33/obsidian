---
id: software.seguranca.tranche03.000238
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-03.md"
fontes: ["https://raw.githubusercontent.com/dexidp/dex/master/README.md", "https://dexidp.io/docs/connectors/", "https://github.com/dexidp/dex"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Dex Backends de Armazenamento (`storage`): `kubernetes` (CRDs nativos) vs `postgres` / `mysql` / `etcd` em Alta Disponibilidade

## Em uma frase
O Dex armazena códigos de autorização temporários, sessões de `refresh_token`, chaves criptográficas JWKS em rotação e clientes dinâmicos em um backend configurável na seção **`storage`** (`kubernetes`, `postgres`, `mysql`, `sqlite3`, `etcd` ou `memory`).

## Por que importa
Executar múltiplas réplicas do Dex para Alta Disponibilidade (HA) usando `storage.type: memory` ou `sqlite3` local faz com que cada pod gere chaves JWKS diferentes e desconheça os códigos de autorização emitidos pelas outras réplicas, quebrando os fluxos de login!

## Como funciona
Quando o Dex roda dentro de um cluster Kubernetes, o backend **`storage.type: kubernetes`** (`inCluster: true`) cria e gerencia automaticamente Custom Resource Definitions (`signingkeys.dex.coreos.com`, `authrequests.dex.coreos.com`, `refreshtokens.dex.coreos.com`, `oauth2clients.dex.coreos.com`) no próprio `etcd` do Kubernetes, permitindo rodar 3+ réplicas stateless do Dex sem provisionar banco externo!

## Exemplo
```yaml
# Configuração de storage PostgreSQL com TLS para implantações do Dex fora do Kubernetes ou de altíssimo volume:
storage:
  type: postgres
  config:
    host: postgres.internal.corp
    port: 5432
    database: dex
    user: dex_user
    password: $DEX_POSTGRES_PASSWORD
    ssl:
      mode: verify-full
      caFile: /etc/dex/certs/db-ca.crt
```

## Limites e trade-offs
Se usar `storage.type: kubernetes`, proteja o namespace onde o Dex roda com RBAC estrito para que nenhum outro ServiceAccount ou usuário possa listar ou ler os CRDs `signingkeys.dex.coreos.com` (que contêm as chaves privadas de assinatura JWKS) e `refreshtokens.dex.coreos.com`!

## Como verificar
Execute `kubectl get crd | grep dex.coreos.com` para verificar os recursos criados pelo backend Kubernetes do Dex.

## Conexões
- [[dexidp-scopes-offline-access-refresh-tokens-expiry-rotation]] — Veja também: Dex Escopos (`offline_access`, `groups`, `federated:id`) e Políticas de Expiração (`expiry`): controle de sessão e `refreshTokens`.
- [[dexidp-grpc-api-mtls-gerenciamento-dinamico-clientes-revogacao]] — Veja também: Dex API Administrativa `gRPC` com `mTLS`: criação dinâmica de clientes OAuth2 e revogação de Refresh Tokens.

## Fontes
- [CNCF Dex GitHub — README.md (Federated OpenID Connect Provider, ID Tokens, Kubernetes Authentication & Connectors Matrix)](https://raw.githubusercontent.com/dexidp/dex/master/README.md) — README oficial do dexidp/dex detalhando a emissão de ID Tokens JWT, integração com Kubernetes/AWS STS e matriz de estabilidade e recursos dos conectores; consultado em 2026-10-03.
- [CNCF Dex Official Documentation — Connectors Reference (Upstream IdP Protocol Translation, Refresh Token & Groups Support)](https://dexidp.io/docs/connectors/) — Documentação oficial de conectores do Dex cobrindo configuração de LDAP, GitHub, GitLab, OIDC e limitações de protocolo; consultado em 2026-10-03.
- [CNCF Dex — Official GitHub Repository](https://github.com/dexidp/dex) — Repositório oficial Apache-2.0 do CNCF Dex; consultado em 2026-10-03.
