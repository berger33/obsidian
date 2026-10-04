---
id: software.devops.tranche11.001022
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

# Configuração do OAuth2 Proxy: ordem de precedência (CLI > variáveis de ambiente > arquivo TOML) e validação com --config-test

## Em uma frase
O `oauth2-proxy` pode ser configurado via **opções de linha de comando**, **variáveis de ambiente** ou **arquivo de configuração (`--config`)**, seguindo ordem decrescente de precedência (CLI sobrescreve variáveis de ambiente, que por sua vez sobrescrevem o arquivo de configuração), e oferece a flag **`--config-test`** para validar a configuração em pipelines de CI/CD.

## Por que importa
Em implantações Kubernetes e GitOps, é comum manter parâmetros estruturais (como `upstreams`, `provider` e `email_domains`) em um arquivo de configuração montado via `ConfigMap` (`--config=/etc/oauth2-proxy.cfg`) enquanto segredos (`client_secret`, `cookie_secret`) são injetados via variáveis de ambiente (`OAUTH2_PROXY_CLIENT_SECRET`). Compreender a precedência e as regras de pluralização no arquivo evita que configurações sejam silenciosamente ignoradas.

## Como funciona
Conforme documenta a página oficial *Configuration Overview* (`oauth2-proxy.github.io/oauth2-proxy/configuration/overview/`): (1) qualquer argumento de linha de comando pode ser especificado no arquivo de configuração substituindo hífens (`-`) por sublinhados (`_`); (2) se um argumento de CLI aceita múltiplos valores (como `--allowed-group` ou `--oidc-extra-audience`), a chave correspondente no arquivo de configuração deve ser escrita **no plural** (adicionando `s` no final, como `allowed_groups` ou `oidc_extra_audiences`); e (3) a flag **`--config-test`** testa a validade da configuração e encerra o processo imediatamente, sendo ideal para etapas de linting em CI/CD.

## Exemplo
```bash
# Validar um arquivo de configuração do OAuth2 Proxy em um pipeline de CI/CD usando --config-test
oauth2-proxy --config=/etc/oauth2-proxy.cfg --config-test
```

## Limites e trade-offs
Se você definir uma flag na linha de comando do container no Deployment Kubernetes (por exemplo, `--email-domain=*`), qualquer tentativa de alterar esse valor apenas via variável de ambiente (`OAUTH2_PROXY_EMAIL_DOMAINS`) ou no arquivo `oauth2-proxy.cfg` não terá efeito, pois a flag de CLI tem a maior precedência.

## Como verificar
Execute `oauth2-proxy --config=./oauth2-proxy.cfg --config-test` antes do deploy para garantir código de saída `0` e ausência de chaves inválidas ou parâmetros obrigatórios faltantes.

## Conexões
- [[oauth2proxy-proxy-reverso-middleware-autenticacao-oidc-oauth2]] — Veja também: OAuth2 Proxy: proxy reverso e middleware de autenticação OAuth2/OIDC (projeto CNCF Sandbox).
- [[oauth2proxy-geracao-cookie-secret-aes-sessoes]] — Veja também: Geração segura do Cookie Secret no OAuth2 Proxy para criptografia AES de sessões.
- [[oauth2proxy-opcoes-provedor-oidc-claims-grupos-pkce-jwks]] — Referência cruzada direta com oauth2proxy-opcoes-provedor-oidc-claims-grupos-pkce-jwks.

## Fontes
- [OAuth2 Proxy GitHub — README.md (Architecture, Distroless & Alpine Images, Security & CNCF Sandbox)](https://oauth2-proxy.github.io/oauth2-proxy/configuration/overview/) — README oficial do oauth2-proxy/oauth2-proxy detalhando modos reverse proxy e middleware, migração para imagens base distroless na v7.6.0+, variantes -alpine e histórico de segurança; consultado em 2026-10-03.
- [OAuth2 Proxy Official Documentation — Configuration Overview (Precedence, Cookie Secret, --config-test & General Provider Options)](https://raw.githubusercontent.com/oauth2-proxy/oauth2-proxy/master/README.md) — Documentação oficial de configuração do OAuth2 Proxy (v7.15.x) cobrindo precedência CLI/Env/Config, geração de Cookie Secret AES, --config-test, PKCE S256, claims OIDC e flags de verificação; consultado em 2026-10-03.
- [OAuth2 Proxy — Official GitHub Repository](https://github.com/oauth2-proxy/oauth2-proxy) — Repositório oficial MIT do OAuth2 Proxy; consultado em 2026-10-03.
