---
id: software.seguranca.tranche13.001288
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-13.md"
fontes: ["https://raw.githubusercontent.com/linux-pam/linux-pam/master/README", "https://raw.githubusercontent.com/linux-pam/linux-pam/master/modules/pam_faillock/faillock.conf.5.xml"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Autenticação Multifator (**MFA**) no Linux-PAM para **`sshd`** e **`sudo`**: Integrando Chaves de Hardware **FIDO2 (`pam_u2f.so`)** e **TOTP (`pam_google_authenticator.so`)**

## Em uma frase
Como exigir um segundo fator de autenticação (**MFA**: toque em uma chave de hardware **YubiKey FIDO2** ou código **TOTP de 6 dígitos**) tanto ao conectar via **SSH** quanto ao elevar privilégios localmente com **`sudo`** em servidores Linux?

## Por que importa
Integrando na pilha `auth` de `/etc/pam.d/sshd` ou `/etc/pam.d/sudo` um dos dois módulos MFA padrão do ecossistema Linux-PAM: **(1) `pam_u2f.so` (Yubico `libpam-u2f`)** — valida criptograficamente chaves de segurança físicas **FIDO2 / WebAuthn / U2F** registradas em `/etc/Yubico/u2f_keys` (com `cue` para avisar no terminal *"Please touch the device."* e `origin=pam://hostname`), exigindo toque físico humano no token USB/NFC a cada comando `sudo`!; ou **(2) `pam_google_authenticator.so` (`libpam-google-authenticator`)** — valida códigos **TOTP (`RFC 6238`)**!

## Como funciona
Para habilitar **Chave Pública SSH + MFA via PAM** no OpenSSH (`sshd_config`), você combina **`AuthenticationMethods publickey,keyboard-interactive:pam`** com **`UsePAM yes`** e **`KbdInteractiveAuthentication yes`** no `/etc/ssh/sshd_config`, e coloca apenas o módulo MFA (`pam_u2f.so` ou `pam_google_authenticator.so`) na pilha `auth` de `/etc/pam.d/sshd`!

## Exemplo
```text
# Exemplo em /etc/pam.d/sudo exigindo toque fisico na chave de hardware FIDO2/YubiKey (pam_u2f.so) antes de validar a senha do sudo
auth    required    pam_u2f.so authfile=/etc/Yubico/u2f_keys cue pinverification=1
```

## Limites e trade-offs
Ao usar **`pam_google_authenticator.so`** em servidores onde contas de automação sem TOTP ainda estão migrando, evite usar a flag `nullok` em produção definitiva: exija que 100% dos usuários humanos possuam o segredo TOTP provisionado (em um diretório protegido pelo root como `/etc/security/totp/${USER}` com permissão `0400`, para que nem mesmo um processo comprometido rodando como o próprio usuário possa ler a semente TOTP!).

## Como verificar
Gerar e registrar as chaves FIDO2 para o `pam_u2f.so` é feito com o utilitário oficial **`pamu2fcfg > /etc/Yubico/u2f_keys`** (registrando sempre uma chave principal e uma chave de backup separada por `:`).

## Conexões
- [[pam-auditoria-rastreabilidade-pam-loginuid-auditd-pam-tty-audit]] — Veja também: Rastreabilidade Imutável de Identidade no Linux: Como o **`pam_loginuid.so`** Preserva o **`auid` (*Audit UID*)** Original Mesmo Após `sudo su -`!.
- [[pam-isolamento-namespaces-pam-namespace-polimorfico-tmp-var-tmp]] — Veja também: Diretórios Polimórficos por Usuário com **`pam_namespace.so` (`/etc/security/namespace.conf`)**: Isolando `/tmp` e `/var/tmp` em Servidores Multiusuário.
- [[pam-arquitetura-pluggable-authentication-modules-grupos-auth-account]] — Referência cruzada direta com pam-arquitetura-pluggable-authentication-modules-grupos-auth-account.
- [[keepassxc-autenticacao-multifator-yubikey-hmac-sha1-keyfile]] — Referência cruzada direta com keepassxc-autenticacao-multifator-yubikey-hmac-sha1-keyfile.

## Fontes
- [Linux-PAM Official Repository README (`linux-pam/linux-pam`)](https://raw.githubusercontent.com/linux-pam/linux-pam/master/README) — documentação oficial do projeto Linux-PAM cobrindo arquitetura da biblioteca `libpam`, grupos de gerenciamento, flags de controle e módulos de segurança; consultado em 2026-10-03.
- [Linux-PAM Official `faillock.conf(5)` Manual Specification](https://raw.githubusercontent.com/linux-pam/linux-pam/master/modules/pam_faillock/faillock.conf.5.xml) — especificação oficial do módulo `pam_faillock` e `/etc/security/faillock.conf` (`dir`, `audit`, `silent`, `deny`, `fail_interval`, `unlock_time`, `even_deny_root`, `root_unlock_time`); consultado em 2026-10-03.
