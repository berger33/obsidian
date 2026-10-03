---
id: software.seguranca.tranche03.000237
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

# Dex Escopos (`offline_access`, `groups`, `federated:id`) e Políticas de Expiração (`expiry`): controle de sessão e `refreshTokens`

## Em uma frase
O Dex controla o ciclo de vida das credenciais emitidas através do bloco **`expiry`** no `config.yaml`, governando o tempo de vida dos códigos de autorização, dos `idTokens` (padrão `24h`), das chaves de assinatura (`signingKeys`, ex.: `6h`) e a política de expiração e rotação de **`refreshTokens`** (`disableRotation`, `reuseInterval`, `validIfNotUsedFor`, `absoluteLifetime`).

## Por que importa
Deixar um `id_token` JWT válido por 24 horas sem possibilidade de revogação antes do `exp` amplia a janela de risco caso o token vaze; é muito mais seguro definir `idTokens: "15m"` ou `"1h"` e renovar via `refresh_token` (`scope: offline_access`), que pode ser revogado a qualquer momento no armazenamento do Dex!

## Como funciona
Por padrão, o Dex rotaciona o `refresh_token` a cada uso, mas permite configurar `reuseInterval` (ex.: `5s`) para evitar falhas quando múltiplas abas ou processos clientes tentam usar o mesmo `refresh_token` simultaneamente.

## Exemplo
```yaml
expiry:
  signingKeys: "6h"
  idTokens: "1h"
  authRequests: "24h"
  deviceRequests: "5m"
  refreshTokens:
    disableRotation: false
    reuseInterval: "5s"
    validIfNotUsedFor: "168h" # Expira após 7 dias de inatividade
    absoluteLifetime: "720h"  # Expira obrigatoriamente após 30 dias
```

## Limites e trade-offs
Desative o banco de senhas estáticas de teste (**`enablePasswordDB: false`**) e remova qualquer entrada `staticPasswords` antes de subir o Dex em ambientes de staging ou produção.

## Como verificar
Verifique o campo `exp - iat` de um `id_token` emitido pelo Dex confirmando que corresponde ao valor configurado em `expiry.idTokens`.

## Conexões
- [[dexidp-staticclients-trustedpeers-cross-client-trust-aud-azp]] — Veja também: Dex `staticClients` e `trustedPeers`: delegação de tokens entre serviços (*Cross-Client Trust*) com claims `aud` e `azp`.
- [[dexidp-storage-backends-kubernetes-crd-postgres-sqlite-etcd]] — Veja também: Dex Backends de Armazenamento (`storage`): `kubernetes` (CRDs nativos) vs `postgres` / `mysql` / `etcd` em Alta Disponibilidade.

## Fontes
- [CNCF Dex GitHub — README.md (Federated OpenID Connect Provider, ID Tokens, Kubernetes Authentication & Connectors Matrix)](https://raw.githubusercontent.com/dexidp/dex/master/README.md) — README oficial do dexidp/dex detalhando a emissão de ID Tokens JWT, integração com Kubernetes/AWS STS e matriz de estabilidade e recursos dos conectores; consultado em 2026-10-03.
- [CNCF Dex Official Documentation — Connectors Reference (Upstream IdP Protocol Translation, Refresh Token & Groups Support)](https://dexidp.io/docs/connectors/) — Documentação oficial de conectores do Dex cobrindo configuração de LDAP, GitHub, GitLab, OIDC e limitações de protocolo; consultado em 2026-10-03.
- [CNCF Dex — Official GitHub Repository](https://github.com/dexidp/dex) — Repositório oficial Apache-2.0 do CNCF Dex; consultado em 2026-10-03.
