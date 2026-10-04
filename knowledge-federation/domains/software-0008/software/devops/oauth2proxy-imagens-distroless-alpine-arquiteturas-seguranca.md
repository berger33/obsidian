---
id: software.devops.tranche11.001026
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

# Imagens de container e segurança do OAuth2 Proxy: migração para Distroless (v7.6.0+), tags -alpine e histórico de segurança

## Em uma frase
Desde a versão **`v7.6.0`**, a imagem de container padrão do OAuth2 Proxy (`quay.io/oauth2-proxy/oauth2-proxy`) utiliza **`GoogleContainerTools/distroless`** como base em vez de Alpine Linux para reduzir dependências instaladas e superfície de ataque, mantendo imagens sufixadas com **`-alpine`** para depuração e arquiteturas específicas como `armv6`.

## Por que importa
Como o OAuth2 Proxy fica exposto diretamente na borda da rede recebendo tráfego não autenticado da internet antes mesmo das aplicações internas, minimizar binários, pacotes de sistema e shells dentro da imagem do container é uma defesa em profundidade essencial contra exploração de vulnerabilidades.

## Como funciona
Conforme documenta a seção *Releases / Images* do README oficial (`oauth2-proxy/oauth2-proxy`): (1) binários compilados são publicados no GitHub para todas as principais arquiteturas, incluindo arquiteturas corporativas como `ppc64le` e `s390x`; (2) a partir da `v7.6.0`, a imagem padrão `quay.io/oauth2-proxy/oauth2-proxy:v7.x.y` é baseada em `distroless` (menor e sem shell/apk), enquanto `quay.io/oauth2-proxy/oauth2-proxy:v7.x.y-alpine` continua disponível para quem precisa de ferramentas de debug ou suporte a `armv6`; (3) imagens *nightly* (`quay.io/oauth2-proxy/oauth2-proxy-nightly`) são construídas da branch `master` apenas para testes e **não** devem ser usadas em produção; e (4) o projeto alerta fortemente contra o uso de versões antigas (`v6.0.0` e anteriores) devido à vulnerabilidade histórica de *open redirect* (`GHSA-5m6c-jp6f-2vcv`).

## Exemplo
```yaml
# Especificação de container Kubernetes usando a imagem oficial Distroless do OAuth2 Proxy com SecurityContext restritivo
containers:
  - name: oauth2-proxy
    image: quay.io/oauth2-proxy/oauth2-proxy:v7.15.0
    args:
      - --config=/etc/oauth2-proxy/oauth2-proxy.cfg
    securityContext:
      allowPrivilegeEscalation: false
      readOnlyRootFilesystem: true
      runAsNonRoot: true
      capabilities:
        drop: ["ALL"]
```

## Limites e trade-offs
Como a imagem padrão pós-`v7.6.0` é `distroless`, scripts de inicialização ou healthchecks baseados em `sh`/`wget`/`curl` dentro do próprio container falharão; utilize sempre probes HTTP nativas do kubelet (`httpGet` em `/ping`) nas especificações `livenessProbe` e `readinessProbe`.

## Como verificar
Inspecione a imagem com `docker inspect quay.io/oauth2-proxy/oauth2-proxy:v7.15.0` e valide que a probe HTTP do Kubernetes responde `200 OK` no endpoint `/ping` do OAuth2 Proxy.

## Conexões
- [[oauth2proxy-flags-seguranca-oidc-nonce-issuer-ca-files]] — Veja também: Segurança de validação OIDC no OAuth2 Proxy: verificação de nonce, email verificado, issuer multi-tenant e CAs privadas.
- [[oauth2proxy-integracao-ingress-nginx-ext-authz-headers]] — Veja também: OAuth2 Proxy como Middleware de Ingress (NGINX auth-url / Envoy ext_authz) e repasse de cabeçalhos de identidade.
- [[oauth2proxy-proxy-reverso-middleware-autenticacao-oidc-oauth2]] — Referência cruzada direta com oauth2proxy-proxy-reverso-middleware-autenticacao-oidc-oauth2.
- [[polaris-motor-politicas-validacao-remediacao-kubernetes]] — Referência cruzada direta com polaris-motor-politicas-validacao-remediacao-kubernetes.

## Fontes
- [OAuth2 Proxy GitHub — README.md (Architecture, Distroless & Alpine Images, Security & CNCF Sandbox)](https://raw.githubusercontent.com/oauth2-proxy/oauth2-proxy/master/README.md) — README oficial do oauth2-proxy/oauth2-proxy detalhando modos reverse proxy e middleware, migração para imagens base distroless na v7.6.0+, variantes -alpine e histórico de segurança; consultado em 2026-10-03.
- [OAuth2 Proxy Official Documentation — Configuration Overview (Precedence, Cookie Secret, --config-test & General Provider Options)](https://oauth2-proxy.github.io/oauth2-proxy/configuration/overview/) — Documentação oficial de configuração do OAuth2 Proxy (v7.15.x) cobrindo precedência CLI/Env/Config, geração de Cookie Secret AES, --config-test, PKCE S256, claims OIDC e flags de verificação; consultado em 2026-10-03.
- [OAuth2 Proxy — Official GitHub Repository](https://github.com/oauth2-proxy/oauth2-proxy) — Repositório oficial MIT do OAuth2 Proxy; consultado em 2026-10-03.
