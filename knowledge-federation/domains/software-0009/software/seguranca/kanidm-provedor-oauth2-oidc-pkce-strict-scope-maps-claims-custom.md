---
id: software.seguranca.tranche14.001315
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
fontes: ["https://raw.githubusercontent.com/kanidm/kanidm/master/README.md", "https://raw.githubusercontent.com/kanidm/kanidm/master/examples/server.toml"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Provedor **OAuth2 / OpenID Connect (OIDC)** no Kanidm: Obrigatoriedade de **PKCE (`S256`)**, **Scope Maps** Baseados em Grupos e **Claim Maps**

## Em uma frase
Como integrar aplicações Web e nativas (como Grafana, Nextcloud, GitLab, Argo CD, Proxmox, Kubernetes API Server ou aplicações próprias) ao provedor **OAuth2 / OIDC** do Kanidm e controlar com precisão quais grupos podem fazer login e quais *claims* cada usuário recebe no JWT?

## Por que importa
No Kanidm, você cria um cliente confidencial com **`kanidm system oauth2 create <nome> <displayname> <origin_url>`** (ou um cliente público para apps móveis/CLI com `create-public`). Por padrão de segurança estrito (**Strict Defaults**), o Kanidm **exige obrigatoriamente `PKCE` (*Proof Key for Code Exchange*, `RFC 7636` com `code_challenge_method = S256`) em todos os fluxos OAuth2** — bloqueando ataques de interceptação de código de autorização!

## Como funciona
E como funciona o controle de acesso à aplicação no Kanidm? Através dos **Scope Maps (`update-scope-map`)**: nenhuma conta do Kanidm consegue autenticar em um cliente OAuth2 até que pertença a um grupo mapeado para os escopos `openid` (e opcionalmente `email`, `profile`, `groups`) daquele cliente!

## Exemplo
```bash
# Criar um cliente OAuth2/OIDC confidencial no Kanidm, configurar o Redirect URL e autorizar apenas membros do grupo 'engenharia-sre' via Scope Map
kanidm system oauth2 create grafana "Grafana Prod" https://grafana.exemplo.br
kanidm system oauth2 add-redirect-url grafana https://grafana.exemplo.br/login/generic_oauth
kanidm system oauth2 update-scope-map grafana engenharia-sre openid profile email groups
kanidm system oauth2 get grafana
```

## Limites e trade-offs
E se você quiser que membros do grupo `sre-admins` recebam `"grafana_role": "Admin"` dentro do JWT, enquanto membros de `sre-viewers` recebam `"grafana_role": "Viewer"`? O Kanidm possui **Custom Claim Maps (`kanidm system oauth2 update-claim-map`)**, que injetam valores de *claims* específicos baseados diretamente nos grupos aos quais o usuário pertence — sem precisar escrever código!

## Como verificar
Apenas se você estiver integrando um sistema legado muito antigo que ainda não suporta `PKCE` ou exige algoritmos legados, o Kanidm oferece flags explícitas por cliente (`enable-pkce` / `warning-insecure-client-disable-pkce`), mantendo todos os demais clientes protegidos por padrão.

## Conexões
- [[kanidm-modelo-privilegios-separacao-admin-idm-admin-reauth-sudo]] — Veja também: Modelo de Privilégio Mínimo e **Reautenticação (`re-auth` Estilo `sudo`)** no Kanidm: Por que `admin` e `idm_admin` São Estritamente Separados?.
- [[kanidm-integracao-linux-pam-nss-kanidm-unixd-ssh-keys-tpm]] — Veja também: Autenticação Linux/Unix e Distribuição de Chaves SSH no Kanidm: Daemon **`kanidm_unixd`**, PAM/NSS, **Cache Offline Protegido por TPM 2.0** e **`kanidm_ssh_authorizedkeys`**.
- [[kanidm-arquitetura-idm-rust-banco-transacional-estrategia-zero-trust]] — Referência cruzada direta com kanidm-arquitetura-idm-rust-banco-transacional-estrategia-zero-trust.
- [[authentik-providers-oauth2-oidc-saml-scim-federacao-sso]] — Referência cruzada direta com authentik-providers-oauth2-oidc-saml-scim-federacao-sso.
- [[teleport-arquitetura-zero-trust-auth-proxy-agents-certificados-curtos]] — Referência cruzada direta com teleport-arquitetura-zero-trust-auth-proxy-agents-certificados-curtos.

## Fontes
- [Kanidm Official GitHub Repository (`kanidm/kanidm`)](https://raw.githubusercontent.com/kanidm/kanidm/master/README.md) — repositório oficial do servidor de gerenciamento de identidade Kanidm em Rust cobrindo WebAuthn/Passkeys, OAuth2/OIDC, LDAPS, RADIUS e clientes POSIX; consultado em 2026-10-03.
- [Kanidm Official Server Configuration Reference (`examples/server.toml`)](https://raw.githubusercontent.com/kanidm/kanidm/master/examples/server.toml) — especificação oficial de configuração do `kanidmd` (`server.toml`) cobrindo `bindaddress`, `ldapbindaddress`, TLS, `domain`, `origin`, `online_backup` e `trust_x_forward_for`; consultado em 2026-10-03.
