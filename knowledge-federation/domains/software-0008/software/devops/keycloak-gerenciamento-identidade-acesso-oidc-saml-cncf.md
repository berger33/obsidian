---
id: software.devops.tranche11.001001
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
fontes: ["https://raw.githubusercontent.com/keycloak/keycloak/main/README.md", "https://www.keycloak.org/guides", "https://www.keycloak.org/server/configuration-production"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Keycloak: plataforma open-source CNCF de gerenciamento de identidade e acesso (IAM) com OpenID Connect, OAuth 2.0 e SAML 2.0

## Em uma frase
O Keycloak é uma plataforma open-source de gerenciamento de identidade e acesso (IAM), mantida sob governança da CNCF e licenciada sob Apache 2.0, que provê autenticação centralizada (Single Sign-On), federação de usuários, autorização granular e gerenciamento de sessões utilizando protocolos padronizados como OpenID Connect (OIDC), OAuth 2.0 e SAML 2.0.

## Por que importa
Construir autenticação própria em cada microsserviço ou painel interno de plataforma dispersa credenciais, dificulta a adoção de MFA/WebAuthn e impede o Single Sign-On corporativo. O Keycloak centraliza o ciclo de vida de identidades para aplicações web, APIs, CLIs (`kubectl`, Argo CD, Grafana, Harbor) e servidores Model Context Protocol (MCP) sem acoplar o código de negócio ao armazenamento de senhas.

## Como funciona
Conforme documentado no repositório oficial (`keycloak/keycloak`) e no portal de guias, o servidor Keycloak (distribuído via `quay.io/keycloak/keycloak` e operado pela CLI `bin/kc.sh`) organiza identidades em **Realms** isolados. Dentro de cada Realm, administradores configuram **Clients** (aplicações que solicitam autenticação OIDC/SAML), **Identity Providers** (brokering com provedores externos OIDC/SAML/redes sociais) e **User Federation** (sincronização com diretórios LDAP e Active Directory). Para desenvolvimento rápido, `bin/kc.sh start-dev` (ou `docker run quay.io/keycloak/keycloak start-dev`) sobe uma instância pronta para testes locais.

## Exemplo
```bash
# Iniciar o Keycloak em modo de desenvolvimento local via container oficial
docker run --rm -p 8080:8080 \
  -e KC_BOOTSTRAP_ADMIN_USERNAME=admin \
  -e KC_BOOTSTRAP_ADMIN_PASSWORD=admin \
  quay.io/keycloak/keycloak:latest start-dev
```

## Limites e trade-offs
O modo `start-dev` desabilita exigências estritas de HTTPS, utiliza banco de dados embarcado H2/dev-file e expõe configurações voltadas à ergonomia local; ele jamais deve ser exposto em produção, onde o comando `kc.sh start` exige TLS, hostname explícito, banco de dados relacional externo e cache distribuído.

## Como verificar
Com o container em execução, consulte o endpoint de descoberta OIDC do realm padrão (`curl -s http://localhost:8080/realms/master/.well-known/openid-configuration | jq .issuer`) para confirmar a emissão de metadados OpenID Connect.

## Conexões
- [[keycloak-configuracao-producao-tls-hostname-v2-reverse-proxy]] — Veja também: Keycloak em produção: TLS, Hostname v2, separação da URL administrativa e configuração de Reverse Proxy.
- [[keycloak-operator-kubernetes-crds-realm-import-clients]] — Referência cruzada direta com keycloak-operator-kubernetes-crds-realm-import-clients.
- [[dex-provedor-identidade-federado-openid-connect-cncf]] — Referência cruzada direta com dex-provedor-identidade-federado-openid-connect-cncf.

## Fontes
- [Keycloak Official Documentation — Configuring Keycloak for production & Guides](https://raw.githubusercontent.com/keycloak/keycloak/main/README.md) — Guias oficiais de configuração do Keycloak para produção (TLS, Hostname v2, reverse proxy, http-max-queued-requests, --server-async-bootstrap, JGroups/Infinispan, Operator, OpenTelemetry e especificações modernas); consultado em 2026-10-03.
- [Keycloak GitHub — README.md & Official Documentation Portal](https://www.keycloak.org/guides) — README oficial do projeto CNCF keycloak/keycloak (Apache-2.0) e índice de guias de servidor, operator, observabilidade e segurança de aplicações; consultado em 2026-10-03.
- [Keycloak — Official Guides & Server Reference](https://www.keycloak.org/server/configuration-production) — Portal oficial de guias do Keycloak; consultado em 2026-10-03.
