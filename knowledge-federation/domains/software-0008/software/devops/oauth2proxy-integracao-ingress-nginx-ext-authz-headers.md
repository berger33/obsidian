---
id: software.devops.tranche11.001027
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
fontes: ["https://raw.githubusercontent.com/oauth2-proxy/oauth2-proxy/master/README.md", "https://oauth2-proxy.github.io/oauth2-proxy/configuration/overview/", "https://github.com/oauth2-proxy/oauth2-proxy"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# OAuth2 Proxy como Middleware de Ingress (NGINX auth-url / Envoy ext_authz) e repasse de cabeçalhos de identidade

## Em uma frase
Em clusters Kubernetes, o OAuth2 Proxy pode operar em modo middleware integrado ao NGINX Ingress Controller (`auth-url` / `auth-signin`) ou Envoy/Traefik, validando sessões no endpoint `/oauth2/auth` e injetando cabeçalhos de identidade do usuário para múltiplos serviços upstream sem duplicar instâncias do proxy.

## Por que importa
Implantar um sidecar do OAuth2 Proxy dentro de cada pod de aplicação multiplica o consumo de memória e exige criar um `client_id` OIDC separado para cada microsserviço. No modo middleware centralizado integrado ao Ingress Controller, uma única implantação do OAuth2 Proxy protege dezenas de subdomínios internos com Single Sign-On compartilhado.

## Como funciona
Conforme descreve o README oficial sobre o modo middleware e extração de detalhes do usuário: (1) o Ingress Controller intercepta a requisição do cliente e faz uma sub-requisição interna para o endpoint `/oauth2/auth` do OAuth2 Proxy; (2) se a sessão for válida, o OAuth2 Proxy responde `202 Accepted` incluindo cabeçalhos com os dados extraídos do provedor (como username preferencial, e-mail, grupos e access/ID token, quando configurado); (3) o Ingress Controller copia esses cabeçalhos para a requisição enviada à aplicação upstream; e (4) se o usuário não estiver autenticado, o OAuth2 Proxy retorna `401 Unauthorized` e o Ingress redireciona o navegador para `/oauth2/start?rd=...`.

## Exemplo
```yaml
# Anotações em um Ingress NGINX delegando autenticação ao serviço central do OAuth2 Proxy
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: prometheus-interno
  annotations:
    nginx.ingress.kubernetes.io/auth-url: "https://auth-proxy.exemplo.com/oauth2/auth"
    nginx.ingress.kubernetes.io/auth-signin: "https://auth-proxy.exemplo.com/oauth2/start?rd=$escaped_request_uri"
    nginx.ingress.kubernetes.io/auth-response-headers: "X-Auth-Request-User,X-Auth-Request-Email,X-Auth-Request-Groups"
spec:
  ingressClassName: nginx
  rules:
    - host: prometheus.exemplo.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: prometheus-server
                port:
                  number: 9090
```

## Limites e trade-offs
Para que uma única instância central do OAuth2 Proxy em `auth-proxy.exemplo.com` autentique subdomínios irmãos (como `prometheus.exemplo.com` e `alertmanager.exemplo.com`), o domínio do cookie (`--cookie-domain=.exemplo.com`) e a lista de domínios permitidos para redirecionamento (`--whitelist-domain=.exemplo.com`) devem ser configurados explicitamente, evitando tanto loops de login quanto redirecionamentos abertos.

## Como verificar
Faça uma requisição `curl -i https://prometheus.exemplo.com` sem cookie para confirmar o redirecionamento `302` para `https://auth-proxy.exemplo.com/oauth2/start` e, após autenticar, confirme a presença dos cabeçalhos `X-Auth-Request-*` no upstream.

## Conexões
- [[oauth2proxy-imagens-distroless-alpine-arquiteturas-seguranca]] — Veja também: Imagens de container e segurança do OAuth2 Proxy: migração para Distroless (v7.6.0+), tags -alpine e histórico de segurança.
- [[oauth2proxy-provedores-especializados-entra-github-google-logingov]] — Veja também: Provedores especializados no OAuth2 Proxy: Google, Microsoft Entra ID, GitHub, login.gov e JWT Signing Keys.
- [[oauth2proxy-proxy-reverso-middleware-autenticacao-oidc-oauth2]] — Referência cruzada direta com oauth2proxy-proxy-reverso-middleware-autenticacao-oidc-oauth2.
- [[oauth2proxy-opcoes-provedor-oidc-claims-grupos-pkce-jwks]] — Referência cruzada direta com oauth2proxy-opcoes-provedor-oidc-claims-grupos-pkce-jwks.
- [[dex-arquitetura-ecossistema-argocd-oauth2proxy-clientes]] — Referência cruzada direta com dex-arquitetura-ecossistema-argocd-oauth2proxy-clientes.

## Fontes
- [OAuth2 Proxy GitHub — README.md (Architecture, Distroless & Alpine Images, Security & CNCF Sandbox)](https://raw.githubusercontent.com/oauth2-proxy/oauth2-proxy/master/README.md) — README oficial do oauth2-proxy/oauth2-proxy detalhando modos reverse proxy e middleware, migração para imagens base distroless na v7.6.0+, variantes -alpine e histórico de segurança; consultado em 2026-10-03.
- [OAuth2 Proxy Official Documentation — Configuration Overview (Precedence, Cookie Secret, --config-test & General Provider Options)](https://oauth2-proxy.github.io/oauth2-proxy/configuration/overview/) — Documentação oficial de configuração do OAuth2 Proxy (v7.15.x) cobrindo precedência CLI/Env/Config, geração de Cookie Secret AES, --config-test, PKCE S256, claims OIDC e flags de verificação; consultado em 2026-10-03.
- [OAuth2 Proxy — Official GitHub Repository](https://github.com/oauth2-proxy/oauth2-proxy) — Repositório oficial MIT do OAuth2 Proxy; consultado em 2026-10-03.
