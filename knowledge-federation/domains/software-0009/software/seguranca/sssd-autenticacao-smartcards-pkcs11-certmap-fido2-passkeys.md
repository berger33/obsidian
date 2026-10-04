---
id: software.seguranca.tranche15.001406
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

# Autenticação **Passwordless** no Linux com SSSD: **Smartcards X.509 (`pam_cert_auth = True` / PKCS#11 `p11_child`)**, Regras de **`certmap`** e **Passkeys FIDO2 WebAuthn (`passkey_child`)**

## Em uma frase
Como configurar estações de trabalho e servidores Linux para autenticar usuários no console (`gdm`, `login`), no `sudo` e no `sshd` usando **Smartcards Físicos (`PIV` / `YubiKey` / Cartão ICP-Brasil X.509)** ou **Passkeys FIDO2 / WebAuthn** integrados ao diretório central via **SSSD**?

## Por que importa
Para **Smartcards X.509 (PKCS#11)**, o SSSD possui o processo auxiliar **`p11_child`** (baseado em `p11-kit` e OpenSC): ao definir **`pam_cert_auth = True`** na seção `[pam]` do `/etc/sssd/sssd.conf` e colocar a Autoridade Certificadora em `/etc/sssd/pki/sssd_auth_ca_db.pem`, o SSSD detecta o cartão inserido na leitora USB, pede o **PIN do Smartcard**, valida a assinatura criptográfica com a chave privada interna do chip, checa OCSP/CRL (`certificate_verification = ocsp_dgst:sha256`) e mapeia o certificado para o usuário do LDAP/AD através de regras **`[certmap/<dominio>/<regra>]`**!

## Como funciona
E a partir do SSSD 2.8+, o processo auxiliar **`passkey_child`** (baseado na `libfido2`) trouxe suporte nativo a **Passkeys FIDO2 / WebAuthn** registradas no FreeIPA, Active Directory ou localmente!

## Exemplo
```ini
# Habilitar autenticacao por Smartcard X.509 (PKCS#11) no /etc/sssd/sssd.conf com verificacao OCSP e regra de mapeamento de Subject/SAN (certmap)
[pam]
pam_cert_auth = True

[sssd]
certificate_verification = ocsp_dgst:sha256

[certmap/CORP.EXEMPLO.BR/regra_upn_smartcard]
matchrule = <EKU>msScLogin
maprule = (userPrincipalName={subject_nt_principal})
```

## Limites e trade-offs
Veja como funcionam a **`matchrule`** e a **`maprule`** na seção `[certmap/...]` acima: a `matchrule = <EKU>msScLogin` filtra apenas certificados na YubiKey/Smartcard que possuam o *Extended Key Usage* de Smartcard Logon, e a `maprule = (userPrincipalName={subject_nt_principal})` extrai o UPN do `SubjectAlternativeName` do certificado X.509 e localiza o usuário exato no Active Directory / LDAP!

## Como verificar
Use o utilitário **`sssctl cert-show <cert_base64>`** e **`sssctl cert-eval-rule`** para testar suas expressões `matchrule` e `maprule` contra um certificado X.509 real antes de aplicá-las em produção.

## Conexões
- [[sssd-controle-acesso-pam-access-provider-simple-ldap-hbac-gpo]] — Veja também: Provedores de Autorização (**`access_provider`**) no SSSD: Filtrando Quem Pode Fazer Login via **`simple` (`simple_allow_groups`)**, **`ldap` (`ldap_access_filter`)**, **`ipa` (HBAC)** e **`ad` (GPO)**.
- [[sssd-idp-externo-oauth2-oidc-device-flow-entra-id-keycloak-authentik]] — Veja também: Autenticação Direta de Desktops e Servidores Linux em **Provedores Cloud OAuth2 / OIDC (`id_provider = idp` — Entra ID, Keycloak, Okta, Authentik, Kanidm)** com SSSD.
- [[sssd-arquitetura-system-security-services-daemon-responders-providers-ldb]] — Referência cruzada direta com sssd-arquitetura-system-security-services-daemon-responders-providers-ldb.
- [[yubikey-gerenciamento-piv-smartcard-x509-slots-9a-9c-9d-9e-pkcs11]] — Referência cruzada direta com yubikey-gerenciamento-piv-smartcard-x509-slots-9a-9c-9d-9e-pkcs11.
- [[freeipa-autenticacao-2fa-otp-totp-hotp-passkeys-radius-pkinit]] — Referência cruzada direta com freeipa-autenticacao-2fa-otp-totp-hotp-passkeys-radius-pkinit.

## Fontes
- [Official SSSD GitHub Repository (`SSSD/sssd`)](https://raw.githubusercontent.com/SSSD/sssd/master/README.md) — repositório oficial do System Security Services Daemon cobrindo arquitetura de responders (`nss`, `pam`, `ssh`, `sudo`) e provedores (`ipa`, `ad`, `ldap`, `krb5`) com cache offline; consultado em 2026-10-03.
- [SSSD Official Configuration Reference (`src/examples/sssd-example.conf`)](https://raw.githubusercontent.com/SSSD/sssd/master/src/examples/sssd-example.conf) — configuração oficial de referência do `/etc/sssd/sssd.conf` detalhando domínios, `id_provider`, `auth_provider`, `access_provider`, `cache_credentials` e `enumerate = FALSE`; consultado em 2026-10-03.
