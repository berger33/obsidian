---
id: software.devops.tranche11.001010
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-11.md"
fontes: ["https://www.keycloak.org/guides", "https://raw.githubusercontent.com/keycloak/keycloak/main/README.md", "https://www.keycloak.org/server/configuration-production"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Integração do Keycloak com infraestrutura: Distribution Registry (OCI), Apache mod_auth_openidc / mod_auth_mellon e Adapters

## Em uma frase
O Keycloak protege tanto aplicações modernas quanto infraestrutura de plataforma por meio de integrações nativas com registros de containers **Distribution Registry (Docker/OCI Registry v2)**, módulos **Apache HTTPD (`mod_auth_openidc` e `mod_auth_mellon`)**, clientes de autorização (`authz client` / `policy enforcer`) e bibliotecas adaptadoras para JavaScript e Node.js.

## Por que importa
Nem todo sistema em uma plataforma corporativa é uma SPA moderna que implementa OIDC nativamente: registros de imagens OCI (`Distribution Registry`), servidores web Apache legados e aplicações corporativas Java/WildFly precisam delegar autenticação e controle de acesso de pull/push ao mesmo provedor central de identidade.

## Como funciona
Conforme os guias da seção *Securing applications* (`keycloak.org/guides`), o Keycloak suporta: (1) **Distribution Registry**: atua como servidor de token compatível com a especificação Docker Registry v2 Token Authentication, emitindo tokens assinados que autorizam ações `pull` e `push` por repositório; (2) **Apache HTTPD**: integra-se via `mod_auth_openidc` (para OpenID Connect) ou `mod_auth_mellon` (para SAML 2.0) atuando como gatekeeper na frente de aplicações internas; e (3) **Keycloak Authorization Client e Policy Enforcer**: avaliam permissões granulares baseadas em recursos, escopos e políticas diretamente no servidor Keycloak (UMA 2.0 / Fine-grained Authorization).

## Exemplo
```apache
# Exemplo de configuração do módulo Apache mod_auth_openidc apontando para um Realm do Keycloak
OIDCProviderMetadataURL https://auth.exemplo.com/realms/plataforma/.well-known/openid-configuration
OIDCClientID apache-portal-interno
OIDCClientSecret "${OIDC_CLIENT_SECRET}"
OIDCRedirectURI https://portal.exemplo.com/oauth2/callback
OIDCCryptoPassphrase "${OIDC_CRYPTO_PASSPHRASE}"

<Location />
   AuthType openid-connect
   Require valid-user
</Location>
```

## Limites e trade-offs
Quando você protege aplicações usando módulos de servidor web (`mod_auth_openidc`) ou proxies reversos de autenticação (como o `oauth2-proxy`), a aplicação backend recebe a identidade do usuário por variáveis de ambiente ou cabeçalhos HTTP; portanto, a aplicação backend não deve aceitar conexões diretas que contornem o proxy autenticador.

## Como verificar
Acesse a rota protegida sem sessão ativa e confirme o redirecionamento HTTP `302` para o endpoint `/protocol/openid-connect/auth` do realm configurado no Keycloak.

## Conexões
- [[keycloak-automacao-admin-rest-api-cli-export-import-realms]] — Veja também: Automação no Keycloak: Admin REST API, Admin Client, registro de clientes via CLI e importação/exportação de Realms.
- [[keycloak-gerenciamento-identidade-acesso-oidc-saml-cncf]] — Referência cruzada direta com keycloak-gerenciamento-identidade-acesso-oidc-saml-cncf.
- [[oauth2proxy-proxy-reverso-middleware-autenticacao-oidc-oauth2]] — Referência cruzada direta com oauth2proxy-proxy-reverso-middleware-autenticacao-oidc-oauth2.

## Fontes
- [Keycloak Official Documentation — Configuring Keycloak for production & Guides](https://www.keycloak.org/guides) — Guias oficiais de configuração do Keycloak para produção (TLS, Hostname v2, reverse proxy, http-max-queued-requests, --server-async-bootstrap, JGroups/Infinispan, Operator, OpenTelemetry e especificações modernas); consultado em 2026-10-03.
- [Keycloak GitHub — README.md & Official Documentation Portal](https://raw.githubusercontent.com/keycloak/keycloak/main/README.md) — README oficial do projeto CNCF keycloak/keycloak (Apache-2.0) e índice de guias de servidor, operator, observabilidade e segurança de aplicações; consultado em 2026-10-03.
- [Keycloak — Official Guides & Server Reference](https://www.keycloak.org/server/configuration-production) — Portal oficial de guias do Keycloak; consultado em 2026-10-03.
