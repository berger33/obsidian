---
id: software.seguranca.tranche14.001385
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
fontes: ["https://raw.githubusercontent.com/freeipa/freeipa/master/README.md", "https://raw.githubusercontent.com/freeipa/freeipa/master/BUILD.txt"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Autenticação Multifator (**2FA / MFA**) e **Passwordless** no FreeIPA: Tokens **TOTP/HOTP (`otptoken`)**, **Passkeys FIDO2**, **Smartcards (`PKINIT`)** e **RADIUS Proxy**

## Em uma frase
Como exigir **Autenticação de Dois Fatores (2FA)** ou **Passkeys / Smartcards (`PIV` / `YubiKey`)** para login SSH e console em toda a frota Linux gerenciada pelo **FreeIPA**, e como funciona a autenticação **Kerberos FAST (`Flexible Authentication Secure Tunneling` — `RFC 6113`)** que protege o segundo fator?

## Por que importa
O FreeIPA suporta nativamente no próprio diretório LDAP (sem precisar de servidores externos!): **(1) Tokens OTP (`TOTP RFC 6238` e `HOTP RFC 4226`)** gerenciados via `ipa otptoken-add` (ou criados pelo próprio usuário no Web UI lendo o QR Code no FreeOTP/Authenticator/YubiKey!); **(2) Passkeys FIDO2 / WebAuthn (`ipa passkeyconfig-mod` / `user-add-passkey`)** integradas ao SSSD moderno; **(3) Smartcards X.509 (`Kerberos PKINIT`)**; e **(4) Proxy RADIUS (`radiusproxy`)** para delegar o 2FA a um servidor RADIUS externo!

## Como funciona
Quando você marca no perfil do usuário (ou globalmente em `ipa config-mod --user-auth-type=otp --user-auth-type=passkey`) que o tipo de autenticação é **`otp`** (`Password + OTP`), o SSSD utiliza um túnel blindado **Kerberos FAST (`Anonymous PKINIT` ou ticket de máquina `host/...` como armadura)** para enviar `Senha + Código OTP` ao KDC sem exposição a ataques de dicionário offline!

## Exemplo
```bash
# Habilitar a exigencia de autenticacao 2FA (OTP) para um usuario administrativo no FreeIPA e gerar um token TOTP com QR Code no terminal
ipa user-mod carlos.admin --user-auth-type=otp
ipa otptoken-add --type=totp --owner=carlos.admin --desc="YubiKey/Authenticator Carlos" --qrcode
```

## Limites e trade-offs
E o que acontece quando um usuário com `user-auth-type=otp` precisa fazer **`kinit`** diretamente na linha de comando (fora do prompt automático do SSSD)? Como o Kerberos exige uma armadura **FAST (*Flexible Authentication Secure Tunneling*)** para proteger a transmissão do código OTP, basta primeiro obter um ticket anônimo ou de máquina (`kinit -n` para criar o cache de armadura) e em seguida rodar **`kinit -T <ccache_armadura> carlos.admin`**!

## Como verificar
No login via **SSH (`sshd`)**, como o SSSD já possui a chave Kerberos `host/servidor@REALM` na `/etc/krb5.keytab` local, o próprio SSSD monta o túnel FAST automaticamente nos bastidores e pede no prompt do SSH: `First Factor:` (senha) seguido de `Second Factor:` (código TOTP de 6 dígitos)!

## Conexões
- [[freeipa-pki-dogtag-certmonger-auto-renovacao-mtls-subca]] — Veja também: PKI Corporativa Integrada (**Dogtag CA & KRA**) e Renovação Automática de Certificados em Hosts Linux com **`certmonger` (`ipa-getcert`)** no FreeIPA.
- [[freeipa-ssh-chaves-publicas-ldap-hostkeys-known-hosts-sssd]] — Veja também: Segurança de **SSH Centralizada** no FreeIPA: Chaves Públicas de Usuário no LDAP (`ipaSshPubKey`), Verificação Automática de **Host Keys (`known_hosts`)** e **Kerberos GSSAPI**.
- [[freeipa-arquitetura-identidade-linux-389ds-kerberos-dogtag-pki-dns]] — Referência cruzada direta com freeipa-arquitetura-identidade-linux-389ds-kerberos-dogtag-pki-dns.

## Fontes
- [FreeIPA Official GitHub Repository (`freeipa/freeipa`)](https://raw.githubusercontent.com/freeipa/freeipa/master/README.md) — repositório oficial do projeto FreeIPA cobrindo integração de 389 Directory Server, MIT Kerberos, Dogtag PKI, BIND DNS, SSSD, HBAC, Sudo e Active Directory Trusts; consultado em 2026-10-03.
- [FreeIPA Official Build & Management Architecture Guide (`BUILD.txt`)](https://raw.githubusercontent.com/freeipa/freeipa/master/BUILD.txt) — documentação técnica oficial do FreeIPA detalhando `ipa-server-install`, autenticação Kerberos (`kinit admin`), framework de gerenciamento CLI/WebUI (`ipa`) e validação de API; consultado em 2026-10-03.
