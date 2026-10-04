---
id: software.seguranca.tranche03.000236
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

# Dex `staticClients` e `trustedPeers`: delegação de tokens entre serviços (*Cross-Client Trust*) com claims `aud` e `azp`

## Em uma frase
No Dex, cada aplicação cliente é cadastrada em **`staticClients`** (ou via API gRPC) com `id`, `name`, `secret` e `redirectURIs`, e pode declarar uma lista **`trustedPeers`** indicando quais outros clientes registrados têm permissão de solicitar ao Dex um `id_token` emitido **em nome deste cliente (`audience`)**!

## Por que importa
Em uma plataforma onde o usuário faz login no dashboard web (`client_id: web-portal`), mas o backend do `web-portal` precisa fazer chamadas autenticadas ao `kube-apiserver` (`client_id: kubernetes-kubectl`) em nome daquele usuário, o `kube-apiserver` rejeitaria um token cuja audiência (`aud`) fosse apenas `web-portal`.

## Como funciona
Configurando `trustedPeers: ["web-portal"]` no cliente `kubernetes-kubectl`, o `web-portal` pode solicitar o escopo especial **`audience:server:client_id:kubernetes-kubectl`**: o Dex emite então um `id_token` com **`"aud": "kubernetes-kubectl"`** e **`"azp": "web-portal"`** (*Authorized Party*), permitindo delegação segura e auditável entre serviços!

## Exemplo
```yaml
staticClients:
  - id: web-portal
    name: "Portal Interno de Engenharia"
    redirectURIs:
      - "https://portal.internal.corp/oauth2/callback"
    secretEnv: PORTAL_CLIENT_SECRET

  - id: kubernetes-kubectl
    name: "Kubernetes API Server"
    redirectURIs:
      - "http://localhost:8000"
    secretEnv: K8S_CLIENT_SECRET
    trustedPeers:
      - web-portal
```

## Limites e trade-offs
Use sempre `secretEnv` (que lê o segredo do cliente de uma variável de ambiente) em vez de `secret` literal em arquivos de configuração do Dex.

## Como verificar
Solicite o escopo `openid email groups audience:server:client_id:kubernetes-kubectl` a partir do `web-portal` e valide as claims `aud` e `azp` do JWT retornado.

## Conexões
- [[dexidp-conector-oidc-upstream-okta-entra-google-alerta-saml]] — Veja também: Dex Conector `OIDC` Upstream vs Alerta de Segurança sobre o Conector `SAML 2.0`.
- [[dexidp-scopes-offline-access-refresh-tokens-expiry-rotation]] — Veja também: Dex Escopos (`offline_access`, `groups`, `federated:id`) e Políticas de Expiração (`expiry`): controle de sessão e `refreshTokens`.

## Fontes
- [CNCF Dex GitHub — README.md (Federated OpenID Connect Provider, ID Tokens, Kubernetes Authentication & Connectors Matrix)](https://raw.githubusercontent.com/dexidp/dex/master/README.md) — README oficial do dexidp/dex detalhando a emissão de ID Tokens JWT, integração com Kubernetes/AWS STS e matriz de estabilidade e recursos dos conectores; consultado em 2026-10-03.
- [CNCF Dex Official Documentation — Connectors Reference (Upstream IdP Protocol Translation, Refresh Token & Groups Support)](https://dexidp.io/docs/connectors/) — Documentação oficial de conectores do Dex cobrindo configuração de LDAP, GitHub, GitLab, OIDC e limitações de protocolo; consultado em 2026-10-03.
- [CNCF Dex — Official GitHub Repository](https://github.com/dexidp/dex) — Repositório oficial Apache-2.0 do CNCF Dex; consultado em 2026-10-03.
