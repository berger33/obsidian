---
id: software.devops.tranche11.001021
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

# OAuth2 Proxy: proxy reverso e middleware de autenticação OAuth2/OIDC (projeto CNCF Sandbox)

## Em uma frase
O OAuth2 Proxy (`oauth2-proxy/oauth2-proxy`, projeto CNCF Sandbox sob licença MIT) é um proxy reverso standalone e componente de middleware que protege aplicações web e serviços internos com autenticação OAuth2 e OpenID Connect (OIDC), extraindo informações de identidade e grupos do usuário e encaminhando-as como cabeçalhos HTTP para as aplicações upstream.

## Por que importa
Muitas ferramentas críticas de DevOps e observabilidade (como dashboards internos, Prometheus UI, Alertmanager, Jaeger UI ou aplicações legadas) não possuem suporte nativo a OAuth2/OIDC. O OAuth2 Proxy adiciona uma camada padronizada de Single Sign-On e controle de acesso por grupos na frente de qualquer serviço HTTP sem modificar uma linha de código da aplicação protegida.

## Como funciona
Conforme descreve o README oficial (`oauth2-proxy/oauth2-proxy`), a ferramenta opera em dois modos arquiteturais: (1) **Standalone Reverse Proxy**: intercepta diretamente todas as requisições destinadas à aplicação, redireciona usuários não autenticados para o provedor OAuth2/OIDC (como Keycloak, Dex, Google, Microsoft Entra ID, GitHub ou `login.gov`) e, após validar o token, encaminha a requisição ao upstream anexando cabeçalhos de identidade; ou (2) **Middleware (ext_authz / auth_request)**: integra-se a proxies reversos e Ingress Controllers existentes (como NGINX Ingress `auth-url`, Envoy `ext_authz` ou Traefik `ForwardAuth`) para autenticar múltiplas aplicações de maneira centralizada.

## Exemplo
```bash
# Executar o OAuth2 Proxy protegendo um serviço upstream local (http://127.0.0.1:8080) usando um provedor OIDC
oauth2-proxy \
  --provider=oidc \
  --oidc-issuer-url=https://dex.exemplo.com/dex \
  --client-id=meu-portal \
  --client-secret="${OAUTH2_PROXY_CLIENT_SECRET}" \
  --cookie-secret="${OAUTH2_PROXY_COOKIE_SECRET}" \
  --email-domain="exemplo.com" \
  --upstream=http://127.0.0.1:8080/ \
  --http-address=0.0.0.0:4180
```

## Limites e trade-offs
Quando o OAuth2 Proxy é usado como proxy reverso ou middleware injetando cabeçalhos HTTP de identidade (como `X-Forwarded-User`, `X-Forwarded-Email` e `X-Forwarded-Groups`), a aplicação upstream nunca deve ser acessível diretamente pela rede externa sem passar pelo proxy; caso contrário, um atacante poderia forjar esses cabeçalhos HTTP diretamente.

## Como verificar
Invoque `oauth2-proxy --version` e faça uma requisição sem cookie de sessão (`curl -i http://localhost:4180/`) para confirmar a resposta de redirecionamento (`302 Found` ou tela de sign-in) exigindo autenticação OAuth2/OIDC.

## Conexões
- [[oauth2proxy-precedencia-configuracao-cli-env-toml-config-test]] — Veja também: Configuração do OAuth2 Proxy: ordem de precedência (CLI > variáveis de ambiente > arquivo TOML) e validação com --config-test.
- [[oauth2proxy-geracao-cookie-secret-aes-sessoes]] — Referência cruzada direta com oauth2proxy-geracao-cookie-secret-aes-sessoes.
- [[dex-arquitetura-ecossistema-argocd-oauth2proxy-clientes]] — Referência cruzada direta com dex-arquitetura-ecossistema-argocd-oauth2proxy-clientes.

## Fontes
- [OAuth2 Proxy GitHub — README.md (Architecture, Distroless & Alpine Images, Security & CNCF Sandbox)](https://raw.githubusercontent.com/oauth2-proxy/oauth2-proxy/master/README.md) — README oficial do oauth2-proxy/oauth2-proxy detalhando modos reverse proxy e middleware, migração para imagens base distroless na v7.6.0+, variantes -alpine e histórico de segurança; consultado em 2026-10-03.
- [OAuth2 Proxy Official Documentation — Configuration Overview (Precedence, Cookie Secret, --config-test & General Provider Options)](https://oauth2-proxy.github.io/oauth2-proxy/configuration/overview/) — Documentação oficial de configuração do OAuth2 Proxy (v7.15.x) cobrindo precedência CLI/Env/Config, geração de Cookie Secret AES, --config-test, PKCE S256, claims OIDC e flags de verificação; consultado em 2026-10-03.
- [OAuth2 Proxy — Official GitHub Repository](https://github.com/oauth2-proxy/oauth2-proxy) — Repositório oficial MIT do OAuth2 Proxy; consultado em 2026-10-03.
