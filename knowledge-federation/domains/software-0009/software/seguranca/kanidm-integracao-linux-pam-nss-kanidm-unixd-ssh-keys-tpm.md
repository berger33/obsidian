---
id: software.seguranca.tranche14.001316
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

# Autenticação Linux/Unix e Distribuição de Chaves SSH no Kanidm: Daemon **`kanidm_unixd`**, PAM/NSS, **Cache Offline Protegido por TPM 2.0** e **`kanidm_ssh_authorizedkeys`**

## Em uma frase
Um dos maiores diferenciais técnicos do **Kanidm** frente ao Keycloak, Authentik e Authelia é a sua integração nativa de primeira classe com **servidores e estações de trabalho Linux / FreeBSD / Unix**!

## Por que importa
Como funciona a arquitetura Unix do Kanidm? **(1) Distribuição Centralizada de Chaves Públicas SSH**: cada usuário cadastra suas chaves públicas SSH (`ssh-ed25519` / `sk-ssh-ed25519@openssh.com`) na sua própria conta do Kanidm; nos servidores Linux, o `sshd_config` chama `AuthorizedKeysCommand /usr/sbin/kanidm_ssh_authorizedkeys %u`, que consulta o daemon local **`kanidm_unixd`** e retorna em milissegundos apenas as chaves válidas se o usuário tiver permissão de login naquele servidor! Quando um funcionário sai da empresa e sua conta é desativada ou expirada no Kanidm, **seu acesso SSH é revogado instantaneamente em toda a frota de servidores**!

## Como funciona
**(2) Autenticação PAM/NSS e Cache Offline Vinculado ao TPM 2.0**: o daemon `kanidm_unixd` resolve UIDs/GIDs/grupos POSIX (`nsswitch.conf`) e autentica sessões PAM (`pam_kanidm.so`) podendo **selar chaves de autenticação offline diretamente dentro do chip de hardware TPM 2.0 da máquina Linux** — permitindo que notebooks corporativos autentiquem com segurança mesmo quando estão sem internet no avião!

## Exemplo
```bash
# Inspecionar o status do daemon local kanidm_unixd e testar a busca de chaves publicas SSH de um usuario POSIX no Linux
kanidm_unix status
kanidm_ssh_authorizedkeys ana.silva
```

## Limites e trade-offs
Para habilitar atributos POSIX (`gidnumber`, `shell`, `unix password` / PIN offline) em contas e grupos do Kanidm, basta estender a conta e o grupo com **`kanidm person posix set <usuario> --shell /bin/bash`** e **`kanidm group posix set <grupo>`**!

## Como verificar
No arquivo `/etc/kanidm/unixd` de cada servidor Linux, a diretiva **`pam_allowed_login_groups = ["sre_prod_ssh"]`** garante que apenas membros do grupo autorizado possam abrir sessão SSH ou console naquela máquina específica (**Host-Based Access Control**).

## Conexões
- [[kanidm-provedor-oauth2-oidc-pkce-strict-scope-maps-claims-custom]] — Veja também: Provedor **OAuth2 / OpenID Connect (OIDC)** no Kanidm: Obrigatoriedade de **PKCE (`S256`)**, **Scope Maps** Baseados em Grupos e **Claim Maps**.
- [[kanidm-gateway-ldaps-read-only-service-accounts-api-tokens]] — Veja também: Gateway **LDAPS Somente-Leitura (`:636`)** e **Service Accounts** no Kanidm: Integrando Sistemas Legados sem Expor o Diretório a Escritas LDAP.
- [[kanidm-arquitetura-idm-rust-banco-transacional-estrategia-zero-trust]] — Referência cruzada direta com kanidm-arquitetura-idm-rust-banco-transacional-estrategia-zero-trust.
- [[pam-arquitetura-pluggable-authentication-modules-grupos-auth-account]] — Referência cruzada direta com pam-arquitetura-pluggable-authentication-modules-grupos-auth-account.

## Fontes
- [Kanidm Official GitHub Repository (`kanidm/kanidm`)](https://raw.githubusercontent.com/kanidm/kanidm/master/README.md) — repositório oficial do servidor de gerenciamento de identidade Kanidm em Rust cobrindo WebAuthn/Passkeys, OAuth2/OIDC, LDAPS, RADIUS e clientes POSIX; consultado em 2026-10-03.
- [Kanidm Official Server Configuration Reference (`examples/server.toml`)](https://raw.githubusercontent.com/kanidm/kanidm/master/examples/server.toml) — especificação oficial de configuração do `kanidmd` (`server.toml`) cobrindo `bindaddress`, `ldapbindaddress`, TLS, `domain`, `origin`, `online_backup` e `trust_x_forward_for`; consultado em 2026-10-03.
