---
id: software.seguranca.tranche02.000150
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

# Authelia Gestão Segura de Segredos (`_FILE` e Templates): injeção de credenciais via arquivos Kubernetes Secrets sem expor texto claro

## Em uma frase
Para evitar gravar chaves privadas JWKS, senhas de banco/LDAP e segredos de sessão dentro do arquivo `configuration.yml`, o Authelia suporta duas abordagens seguras: 1) variáveis de ambiente terminadas no sufixo **`_FILE`** (ex.: `AUTHELIA_IDENTITY_VALIDATION_RESET_PASSWORD_JWT_SECRET_FILE=/run/secrets/jwt_secret`), que leem o valor diretamente de um arquivo montado de um *Kubernetes Secret* ou *Docker Secret*; e 2) **Configuration Templates** (`X_AUTHELIA_CONFIG_FILTERS=template`).

## Por que importa
Passar segredos diretamente em variáveis de ambiente normais (`AUTHELIA_SESSION_SECRET=...`) expõe os valores para qualquer processo ou dump de `kubectl describe pod` / `/proc/<pid>/environ`; usar o sufixo `_FILE` lê o segredo diretamente de um volume `tmpfs` em memória com permissão `0400`.

## Como funciona
Com `X_AUTHELIA_CONFIG_FILTERS=template`, você também pode usar funções de template Go dentro do `configuration.yml` (como `{{ secret "/run/secrets/ldap_password" }}` ou `{{ env "HOSTNAME" }}`).

## Exemplo
```bash
# Iniciando o Authelia com filtro de templates habilitado e segredos montados em arquivos somente-leitura:
export X_AUTHELIA_CONFIG_FILTERS="template"
export AUTHELIA_SESSION_SECRET_FILE="/run/secrets/authelia_session_secret"
export AUTHELIA_STORAGE_ENCRYPTION_KEY_FILE="/run/secrets/authelia_storage_key"
authelia --config /config/configuration.yml
```

## Limites e trade-offs
Nunca misture para a mesma chave de configuração a definição no YAML, a variável de ambiente normal e a variável `_FILE` ao mesmo tempo: defina os segredos exclusivamente via `_FILE` ou template `secret`.

## Como verificar
Execute `authelia validate-config --config /config/configuration.yml` com `X_AUTHELIA_CONFIG_FILTERS=template` para validar a expansão dos templates.

## Conexões
- [[authelia-openid-connect-provider-clients-authorization-policies-pkce]] — Veja também: Authelia como Provedor OpenID Connect 1.0 (`identity_providers.oidc`): proteção de aplicações nativas OIDC (Grafana, Argo CD, GitLab).

## Fontes
- [Authelia Official Documentation — Access Control Configuration (Rules Evaluation Order, 7 Specificity Dimensions, Policy Levels & Subject/Network/Method Matching)](https://raw.githubusercontent.com/authelia/authelia/master/README.md) — Documentação oficial do motor de Controle de Acesso do Authelia detalhando default_policy, políticas bypass/one_factor/two_factor/deny, avaliação sequencial e as 7 dimensões de especificidade; consultado em 2026-10-03.
- [Authelia GitHub — README.md (Open-Source Authentication & Authorization Server, ForwardAuth Reverse Proxy Integrations & OIDC Provider)](https://www.authelia.com/configuration/security/access-control/) — README oficial do authelia/authelia descrevendo a arquitetura SSO/2FA acoplada a proxies reversos e provedor OpenID Connect; consultado em 2026-10-03.
- [Authelia — Official GitHub Repository](https://github.com/authelia/authelia) — Repositório oficial Apache-2.0 do Authelia; consultado em 2026-10-03.
