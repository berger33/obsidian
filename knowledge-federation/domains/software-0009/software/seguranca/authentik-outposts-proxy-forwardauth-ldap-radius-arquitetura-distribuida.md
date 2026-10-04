---
id: software.seguranca.tranche14.001305
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

# Arquitetura de **Outposts** no authentik: Protegendo Aplicações Sem SSO via **Proxy / ForwardAuth (Traefik, Nginx, Envoy)** e Gateways **LDAP / RADIUS**

## Em uma frase
E aquelas ferramentas internas de monitoramento, painéis administrativos legados, impressoras/NAS que só falam **LDAP**, ou redes Wi-Fi corporativas WPA2/WPA3-Enterprise e VPNs que exigem **RADIUS** — como protegê-los com o SSO e o MFA do authentik?

## Por que importa
Através dos **Outposts** do authentik!

## Como funciona
Um **Outpost** é um serviço leve escrito em **Go** (que pode rodar embutido no próprio servidor principal ou ser implantado como um container/pod remoto próximo às aplicações em outras VPCs/clusters Kubernetes, comunicando-se com o Core Server via WebSocket seguro com token de serviço) e que atua em **quatro personalidades**: **(1) `Proxy Outpost`** (implementando **Reverse Proxy** direto ou **ForwardAuth** para Traefik, Nginx `auth_request`, Caddy e Envoy/Istio — injetando cabeçalhos autenticados como `X-authentik-username`, `X-authentik-groups`, `X-authentik-email`, `X-authentik-jwt`!); **(2) `LDAP Outpost`** (expõe um servidor LDAPS na porta `636` que traduz `Bind` e `Search` LDAP para os Flows do authentik!); **(3) `RADIUS Outpost`** (UDP `1812`); e **(4) `RAC Outpost` (Remote Access Client para RDP/SSH/VNC HTML5 via Guacamole)**!

## Exemplo
```nginx
# Exemplo de uso do Proxy Outpost do authentik em modo ForwardAuth (auth_request) no Nginx para proteger uma aplicacao interna
location / {
    auth_request /outpost.goauthentik.io/auth/nginx;
    error_page 401 = @goauthentik_proxy_signin;
    auth_request_set $authentik_username $upstream_http_x_authentik_username;
    auth_request_set $authentik_groups   $upstream_http_x_authentik_groups;
    proxy_set_header X-Forwarded-User   $authentik_username;
    proxy_set_header X-Forwarded-Groups $authentik_groups;
    proxy_pass http://backend_interno:8080;
}
```

## Limites e trade-offs
Regra crítica de segurança ao usar **ForwardAuth (`X-authentik-*` / `X-Forwarded-User`)**: a aplicação backend (`http://backend_interno:8080`) **só deve aceitar conexões vindas do IP interno do Proxy Reverso (Nginx/Traefik)**! Se um atacante na rede interna puder conectar diretamente na porta `8080` do backend pulando o Nginx, ele próprio poderia forjar o cabeçalho `X-authentik-username: admin`!

## Como verificar
Quando o Outpost é implantado em um cluster Kubernetes onde o authentik tem permissão na API do K8s, o próprio Core Server gerencia, atualiza e injeta os `Deployments` e `Secrets` dos Outposts automaticamente!

## Conexões
- [[authentik-providers-oauth2-oidc-saml-scim-federacao-sso]] — Veja também: Provedores **OAuth2 / OIDC**, **SAML 2.0** e **SCIM 2.0** no authentik: Assinatura de JWTs, Property Mappings (Scopes) e Provisionamento Automático de Ciclo de Vida.
- [[authentik-blueprints-infraestrutura-como-codigo-gitops-automacao]] — Veja também: Identidade como Código (**Identity-as-Code**) no authentik com **Blueprints YAML**: Versionando Fluxos, Políticas, Provedores e RBAC via GitOps.
- [[authentik-arquitetura-idp-core-embedded-outpost-worker-postgresql]] — Referência cruzada direta com authentik-arquitetura-idp-core-embedded-outpost-worker-postgresql.
- [[arkime-seguranca-viewer-tls-reverse-proxy-headers-passwordsecret]] — Referência cruzada direta com arkime-seguranca-viewer-tls-reverse-proxy-headers-passwordsecret.

## Fontes
- [authentik Official GitHub Repository (`goauthentik/authentik`)](https://raw.githubusercontent.com/goauthentik/authentik/main/README.md) — repositório oficial do provedor de identidade open-source authentik cobrindo OAuth2/OIDC, SAML, LDAP, RADIUS, SCIM e Flows; consultado em 2026-10-03.
- [authentik Official Architecture Documentation (`docs.goauthentik.io/docs/core/architecture`)](https://docs.goauthentik.io/docs/core/architecture) — documentação arquitetural oficial do authentik detalhando Server (Go Router + Python/Django API), Workers, PostgreSQL, Outposts e Blueprints declarativos; consultado em 2026-10-03.
