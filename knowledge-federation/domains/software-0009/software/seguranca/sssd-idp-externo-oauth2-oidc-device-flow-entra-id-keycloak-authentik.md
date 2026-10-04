---
id: software.seguranca.tranche15.001407
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-15.md"
fontes: ["https://raw.githubusercontent.com/SSSD/sssd/master/README.md", "https://raw.githubusercontent.com/SSSD/sssd/master/src/examples/sssd-example.conf"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Autenticação Direta de Desktops e Servidores Linux em **Provedores Cloud OAuth2 / OIDC (`id_provider = idp` — Entra ID, Keycloak, Okta, Authentik, Kanidm)** com SSSD

## Em uma frase
E para organizações Cloud-Native que aposentaram completamente servidores LDAP e Kerberos locais e mantêm 100% das suas identidades em um **IdP OAuth2 / OpenID Connect (como Microsoft Entra ID / Azure AD, Keycloak, Authentik, Kanidm ou Okta)**? Como fazer login SSH e no desktop Linux usando diretamente o IdP OIDC?

## Por que importa
As versões modernas do SSSD introduziram o provedor nativo **`id_provider = idp` (`sssd-idp` com `oidc_child`)**!

## Como funciona
Usando o fluxo padronizado **OAuth 2.0 Device Authorization Grant (`RFC 8628` — *Device Flow*)**, quando o usuário tenta fazer login via SSH ou no GDM do Linux, o SSSD solicita um código curto ao IdP OIDC e exibe no prompt: **`Authenticate at https://idp.exemplo.br/device with code ABCD-EFGH`**! O usuário abre o link no celular ou navegador autenticado com sua Passkey/MFA corporativa, aprova o login e o SSSD valida o token JWT OIDC e cria a sessão POSIX local!

## Exemplo
```ini
# Configurar um dominio OAuth2/OIDC (id_provider = idp) no /etc/sssd/sssd.conf para autenticar logins Linux via RFC 8628 Device Authorization Grant
[domain/oidc.exemplo.br]
id_provider = idp
idp_type = openid
idp_client_id = linux-workstations-client
idp_client_secret = SegredoClienteOIDCLinux2026
idp_token_endpoint = https://sso.exemplo.br/application/o/token/
idp_userinfo_endpoint = https://sso.exemplo.br/application/o/userinfo/
idp_device_auth_endpoint = https://sso.exemplo.br/application/o/device/
idp_id_scope = openid profile email groups
```

## Limites e trade-offs
Por que o fluxo **OAuth 2.0 Device Flow (`RFC 8628`)** usado pelo `sssd-idp` no login SSH é muito mais seguro do que pedir para o usuário digitar sua senha do SSO no terminal SSH? Porque **a senha e a Passkey FIDO2 do usuário jamais passam pelo servidor SSH remoto**: toda a autenticação WebAuthn/MFA ocorre diretamente entre o navegador do usuário e o IdP OIDC (`sso.exemplo.br`)!

## Como verificar
Para o Microsoft Entra ID (`idp_type = entra_id`), o `sssd-idp` consulta automaticamente a Microsoft Graph API para resolver grupos e atributos de usuário.

## Conexões
- [[sssd-autenticacao-smartcards-pkcs11-certmap-fido2-passkeys]] — Veja também: Autenticação **Passwordless** no Linux com SSSD: **Smartcards X.509 (`pam_cert_auth = True` / PKCS#11 `p11_child`)**, Regras de **`certmap`** e **Passkeys FIDO2 WebAuthn (`passkey_child`)**.
- [[sssd-isolamento-privilegios-rootless-socket-activation-infopipe-dbus]] — Veja também: Hardening do Próprio SSSD: Execução **Sem Privilégios (`user = sssd`)**, **Systemd Socket Activation**, **Application Domains** e Interface D-Bus **`InfoPipe` (`sssd_ifp`)**.
- [[sssd-arquitetura-system-security-services-daemon-responders-providers-ldb]] — Referência cruzada direta com sssd-arquitetura-system-security-services-daemon-responders-providers-ldb.
- [[authentik-providers-oauth2-oidc-saml-scim-federacao-sso]] — Referência cruzada direta com authentik-providers-oauth2-oidc-saml-scim-federacao-sso.
- [[kanidm-provedor-oauth2-oidc-pkce-strict-scope-maps-claims-custom]] — Referência cruzada direta com kanidm-provedor-oauth2-oidc-pkce-strict-scope-maps-claims-custom.

## Fontes
- [Official SSSD GitHub Repository (`SSSD/sssd`)](https://raw.githubusercontent.com/SSSD/sssd/master/README.md) — repositório oficial do System Security Services Daemon cobrindo arquitetura de responders (`nss`, `pam`, `ssh`, `sudo`) e provedores (`ipa`, `ad`, `ldap`, `krb5`) com cache offline; consultado em 2026-10-03.
- [SSSD Official Configuration Reference (`src/examples/sssd-example.conf`)](https://raw.githubusercontent.com/SSSD/sssd/master/src/examples/sssd-example.conf) — configuração oficial de referência do `/etc/sssd/sssd.conf` detalhando domínios, `id_provider`, `auth_provider`, `access_provider`, `cache_credentials` e `enumerate = FALSE`; consultado em 2026-10-03.
