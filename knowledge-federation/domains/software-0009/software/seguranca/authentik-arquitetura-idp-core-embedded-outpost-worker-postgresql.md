---
id: software.seguranca.tranche14.001301
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-14.md"
fontes: ["https://raw.githubusercontent.com/goauthentik/authentik/main/README.md", "https://docs.goauthentik.io/docs/core/architecture"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Arquitetura do **authentik (`goauthentik/authentik`)**: Core Server, **Embedded Outpost** em Go, **Worker** Assíncrono e **PostgreSQL**

## Em uma frase
Por que organizações modernas adotam o **authentik** como plataforma central de **Identity Provider (IdP) e Single Sign-On (SSO)** para substituir ou federar serviços como Okta, Auth0, Entra ID e Ping Identity em ambientes de nuvem e Kubernetes?

## Por que importa
O authentik unifica em uma única plataforma extensível todos os protocolos de identidade corporativos — **OAuth2 / OpenID Connect (OIDC)**, **SAML 2.0**, **LDAP**, **RADIUS**, **SCIM 2.0** e **ForwardAuth / Proxy Reverso** — eliminando silos de credenciais entre aplicações modernas e sistemas legados!

## Como funciona
Na arquitetura de execução do authentik, os componentes cooperam de forma desacoplada sobre um banco de dados **PostgreSQL**: **(1) O contêiner `server`**, que combina um roteador HTTP leve em Go, o **Core Server** (em Python/Django, responsável pela API REST/GraphQL, avaliação de políticas, execução de *Flows* e emissão de tokens OIDC/SAML) e o **Embedded Outpost** em Go (que permite usar *Proxy Providers* imediatamente sem implantar containers extras!); e **(2) O contêiner `worker`**, que processa tarefas em segundo plano (sincronização LDAP/SCIM, envio de e-mails, rotação de certificados Let's Encrypt, *Blueprints* e o motor de notificações de eventos)!

## Exemplo
```bash
# Verificar a saude dos endpoints de readiness e liveness do Core Server/Outpost do authentik
curl -sk https://sso.exemplo.br/-/health/live/
curl -sk https://sso.exemplo.br/-/health/ready/
```

## Limites e trade-offs
Nas versões recentes do authentik, o cache e a fila de mensagens migraram para utilizar diretamente o próprio **PostgreSQL** (com `LISTEN/NOTIFY` e tabelas de fila dedicadas), simplificando a topologia de alta disponibilidade ao remover a dependência obrigatória de um cluster Redis separado!

## Como verificar
Em implantações Kubernetes via Helm Chart oficial (`goauthentik/helm`), escale réplicas de `server` e `worker` horizontalmente apontando para um cluster PostgreSQL gerenciado com conexões TLS.

## Conexões
- [[authentik-motor-flows-stages-bindings-autenticacao-contextual]] — Veja também: O Motor de **Flows, Stages e Stage Bindings** no authentik: Construindo Jornadas de Autenticação, MFA Adaptativo, Enrollment e Recovery sem Código Fixo.
- [[authentik-providers-oauth2-oidc-saml-scim-federacao-sso]] — Referência cruzada direta com authentik-providers-oauth2-oidc-saml-scim-federacao-sso.
- [[kanidm-arquitetura-idm-rust-banco-transacional-estrategia-zero-trust]] — Referência cruzada direta com kanidm-arquitetura-idm-rust-banco-transacional-estrategia-zero-trust.

## Fontes
- [authentik Official GitHub Repository (`goauthentik/authentik`)](https://raw.githubusercontent.com/goauthentik/authentik/main/README.md) — repositório oficial do provedor de identidade open-source authentik cobrindo OAuth2/OIDC, SAML, LDAP, RADIUS, SCIM e Flows; consultado em 2026-10-03.
- [authentik Official Architecture Documentation (`docs.goauthentik.io/docs/core/architecture`)](https://docs.goauthentik.io/docs/core/architecture) — documentação arquitetural oficial do authentik detalhando Server (Go Router + Python/Django API), Workers, PostgreSQL, Outposts e Blueprints declarativos; consultado em 2026-10-03.
