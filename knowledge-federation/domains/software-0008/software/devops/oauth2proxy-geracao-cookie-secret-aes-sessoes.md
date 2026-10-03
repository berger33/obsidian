---
id: software.devops.tranche11.001023
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
fontes: ["https://oauth2-proxy.github.io/oauth2-proxy/configuration/overview/", "https://raw.githubusercontent.com/oauth2-proxy/oauth2-proxy/master/README.md", "https://github.com/oauth2-proxy/oauth2-proxy"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Geração segura do Cookie Secret no OAuth2 Proxy para criptografia AES de sessões

## Em uma frase
O OAuth2 Proxy exige um **`--cookie-secret`** criptograficamente forte (32 bytes codificados em Base64 URL-safe, ou 16/24/32 bytes para cifras AES-128/192/256) para assinar e criptografar os cookies de sessão dos usuários autenticados.

## Por que importa
Como o OAuth2 Proxy pode armazenar tokens OAuth2/OIDC diretamente em cookies criptografados no navegador do cliente (modo stateless sem Redis) ou identificadores de sessão para o backend Redis, um `cookie-secret` fraco, mal formatado (com quebras de linha ou caracteres Base64 não URL-safe `+` e `/`) ou divergente entre réplicas causa falha de inicialização ou invalidação de sessões.

## Como funciona
Na seção *Generating a Cookie Secret* da documentação oficial (`oauth2-proxy.github.io/oauth2-proxy/configuration/overview/`), o projeto fornece receitas exatas para gerar um segredo de 32 bytes codificado em Base64 URL-safe (substituindo `+` por `-` e `/` por `_`) usando Python (`base64.urlsafe_b64encode(os.urandom(32))`), Bash (`dd if=/dev/urandom bs=32 count=1`), OpenSSL (`openssl rand -base64 32 | tr -- '+/' '-_'`), PowerShell ou Terraform (`random_password` com `length = 32` e `override_special = "-_"`).

## Exemplo
```bash
# Gerar um cookie-secret de 32 bytes compatível com Base64 URL-safe usando OpenSSL ou Python conforme a documentação oficial
openssl rand -base64 32 | tr -- '+/' '-_'

python3 -c 'import os,base64; print(base64.urlsafe_b64encode(os.urandom(32)).decode())'
```

## Limites e trade-offs
Quando o OAuth2 Proxy roda com múltiplas réplicas atrás de um balanceador de carga sem *sticky sessions*, todas as réplicas devem compartilhar exatamente o mesmo `cookie-secret` (e, quando os tokens OIDC excedem o limite de 4 KB dos cookies de navegador, também um armazenamento de sessão compartilhado como Redis).

## Como verificar
Gere o segredo com o comando oficial, injete-o via `OAUTH2_PROXY_COOKIE_SECRET` e execute `oauth2-proxy --config-test` para confirmar que o tamanho do segredo AES é aceito sem erros.

## Conexões
- [[oauth2proxy-precedencia-configuracao-cli-env-toml-config-test]] — Veja também: Configuração do OAuth2 Proxy: ordem de precedência (CLI > variáveis de ambiente > arquivo TOML) e validação com --config-test.
- [[oauth2proxy-opcoes-provedor-oidc-claims-grupos-pkce-jwks]] — Veja também: Configuração OIDC no OAuth2 Proxy: claims customizadas (aud, email, groups), --allowed-group, PKCE (S256) e validação JWKS.
- [[oauth2proxy-proxy-reverso-middleware-autenticacao-oidc-oauth2]] — Referência cruzada direta com oauth2proxy-proxy-reverso-middleware-autenticacao-oidc-oauth2.
- [[externalsecrets-geradores-dinamicos-password-uuid-ecr-sts]] — Referência cruzada direta com externalsecrets-geradores-dinamicos-password-uuid-ecr-sts.

## Fontes
- [OAuth2 Proxy GitHub — README.md (Architecture, Distroless & Alpine Images, Security & CNCF Sandbox)](https://oauth2-proxy.github.io/oauth2-proxy/configuration/overview/) — README oficial do oauth2-proxy/oauth2-proxy detalhando modos reverse proxy e middleware, migração para imagens base distroless na v7.6.0+, variantes -alpine e histórico de segurança; consultado em 2026-10-03.
- [OAuth2 Proxy Official Documentation — Configuration Overview (Precedence, Cookie Secret, --config-test & General Provider Options)](https://raw.githubusercontent.com/oauth2-proxy/oauth2-proxy/master/README.md) — Documentação oficial de configuração do OAuth2 Proxy (v7.15.x) cobrindo precedência CLI/Env/Config, geração de Cookie Secret AES, --config-test, PKCE S256, claims OIDC e flags de verificação; consultado em 2026-10-03.
- [OAuth2 Proxy — Official GitHub Repository](https://github.com/oauth2-proxy/oauth2-proxy) — Repositório oficial MIT do OAuth2 Proxy; consultado em 2026-10-03.
