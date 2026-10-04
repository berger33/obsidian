---
id: software.seguranca.tranche02.000141
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-02.md"
fontes: ["https://raw.githubusercontent.com/authelia/authelia/master/README.md", "https://www.authelia.com/configuration/security/access-control/", "https://github.com/authelia/authelia"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Authelia: arquitetura do servidor open-source de autenticação, 2FA, controle de acesso (`ForwardAuth`) e provedor OpenID Connect 1.0

## Em uma frase
O **Authelia** (`authelia/authelia`, escrito em Go com selo **OpenSSF Best Practices Gold** e proveniência **SLSA Nível 3**) é um servidor open-source de autenticação e autorização que atua em conjunto com proxies reversos (**Traefik**, **NGINX**, **Caddy**, **HAProxy**, **Envoy**) via protocolo **ForwardAuth / AuthRequest**, além de funcionar como **Provedor OpenID Connect 1.0 Certificado**.

## Por que importa
Muitas ferramentas internas de infraestrutura e observabilidade (ou painéis legados) não possuem suporte a OIDC/SAML nem autenticação de dois fatores nativa; colocá-las atrás de um proxy reverso integrado ao Authelia adiciona SSO e 2FA (WebAuthn/TOTP) instantaneamente sem tocar no código da aplicação.

## Como funciona
Em cada requisição recebida pelo proxy reverso, o proxy faz uma sub-requisição leve para o endpoint `/api/authz/forward-auth` (ou `/api/authz/auth-request` / `/api/authz/ext-authz`) do Authelia: se a sessão e a regra de `access_control` permitirem, o Authelia responde HTTP `200 OK` injetando cabeçalhos confiáveis de identidade (`Remote-User`, `Remote-Groups`, `Remote-Name`, `Remote-Email`); caso contrário, redireciona o navegador para o portal de login e 2FA.

## Exemplo
```bash
# Validando o arquivo de configuração do Authelia antes de iniciar o container ou serviço:
authelia validate-config --config /config/configuration.yml
```

## Limites e trade-offs
Garanta que o proxy reverso **remova/sobrescreva** quaisquer cabeçalhos `Remote-User` e `Remote-Groups` enviados pelo cliente externo antes de repassar os cabeçalhos assinados pelo Authelia para o backend, evitando spoofing de cabeçalho!

## Como verificar
Execute `authelia --version` e `authelia validate-config -c configuration.yml`.

## Conexões
- [[authelia-access-control-policies-deny-bypass-one-factor-two-factor]] — Veja também: Authelia `access_control`: políticas `deny`, `bypass`, `one_factor` e `two_factor` e avaliação sequencial *first-match*.

## Fontes
- [Authelia Official Documentation — Access Control Configuration (Rules Evaluation Order, 7 Specificity Dimensions, Policy Levels & Subject/Network/Method Matching)](https://raw.githubusercontent.com/authelia/authelia/master/README.md) — Documentação oficial do motor de Controle de Acesso do Authelia detalhando default_policy, políticas bypass/one_factor/two_factor/deny, avaliação sequencial e as 7 dimensões de especificidade; consultado em 2026-10-03.
- [Authelia GitHub — README.md (Open-Source Authentication & Authorization Server, ForwardAuth Reverse Proxy Integrations & OIDC Provider)](https://www.authelia.com/configuration/security/access-control/) — README oficial do authelia/authelia descrevendo a arquitetura SSO/2FA acoplada a proxies reversos e provedor OpenID Connect; consultado em 2026-10-03.
- [Authelia — Official GitHub Repository](https://github.com/authelia/authelia) — Repositório oficial Apache-2.0 do Authelia; consultado em 2026-10-03.
