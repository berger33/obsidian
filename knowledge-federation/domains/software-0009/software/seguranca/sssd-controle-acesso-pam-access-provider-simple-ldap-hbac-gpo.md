---
id: software.seguranca.tranche15.001405
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

# Provedores de Autorização (**`access_provider`**) no SSSD: Filtrando Quem Pode Fazer Login via **`simple` (`simple_allow_groups`)**, **`ldap` (`ldap_access_filter`)**, **`ipa` (HBAC)** e **`ad` (GPO)**

## Em uma frase
Atenção a uma armadilha clássica ao configurar o SSSD com `id_provider = ldap` e `auth_provider = krb5`: por padrão, se você não configurar um **`access_provider`** explícito, **qualquer conta ativa no diretório da empresa inteira (mesmo um estagiário do Marketing ou uma conta de teste!) que tenha uma senha Kerberos válida conseguirá fazer login via SSH no servidor de Banco de Dados de Produção**!

## Por que importa
Por quê? Porque **Autenticação (`auth_provider`: "Quem é você?") é diferente de Autorização (`access_provider`: "Você tem permissão para entrar NESTE servidor?")**!

## Como funciona
O SSSD oferece 4 motores de `access_provider` para trancar o acesso em cada servidor: **(1) `access_provider = simple`** — a forma mais rápida e direta para servidores standalone: você define **`simple_allow_groups = sre-admins, dba-prod`** (e/ou `simple_deny_groups`); **(2) `access_provider = ldap`** — aplica um filtro LDAP arbitrário (**`ldap_access_filter = (&(memberOf=cn=sre,ou=groups,dc=exemplo,dc=br)(!(employeeStatus=inativo)))`**) além de checar expiração de conta (`ldap_account_expire_policy = ad` / `shadow`); **(3) `access_provider = ipa`** (avalia regras HBAC do FreeIPA); e **(4) `access_provider = ad`** (avalia GPOs e expiração de conta do Active Directory)!

## Exemplo
```ini
# Configurar na secao [domain/...] do /etc/sssd/sssd.conf o bloqueio de login restrito exclusivamente ao grupo 'sre-producao'
access_provider = simple
simple_allow_groups = sre-producao
simple_deny_groups = contas-servico-sem-shell, terceiros-suspensos
```

## Limites e trade-offs
Qual é a regra de precedência no **`access_provider = simple`** quando você usa `simple_allow_groups` e `simple_deny_groups` juntos? **O `deny` vence sempre!** Se um usuário pertencer simultaneamente ao grupo `sre-producao` (`allow`) e ao grupo `terceiros-suspensos` (`deny`), o SSSD negará o login na fase `account` do PAM (`pam_sss.so`)!

## Como verificar
Teste qualquer regra de `access_provider` diretamente no terminal usando **`sssctl user-checks <usuario> --action=acct --service=sshd`**: ele executa a pilha `account` do PAM para aquele usuário e informa na hora se o acesso ao `sshd` está autorizado ou bloqueado!

## Conexões
- [[sssd-cache-offline-credenciais-sss-cache-invalidacao-troubleshooting]] — Veja também: Funcionamento do **Cache em Duas Camadas (`Memory Cache` + `LDB`)**, Autenticação Offline (`cache_credentials`) e Invalidação Cirúrgica com **`sss_cache`** no SSSD.
- [[sssd-autenticacao-smartcards-pkcs11-certmap-fido2-passkeys]] — Veja também: Autenticação **Passwordless** no Linux com SSSD: **Smartcards X.509 (`pam_cert_auth = True` / PKCS#11 `p11_child`)**, Regras de **`certmap`** e **Passkeys FIDO2 WebAuthn (`passkey_child`)**.
- [[sssd-arquitetura-system-security-services-daemon-responders-providers-ldb]] — Referência cruzada direta com sssd-arquitetura-system-security-services-daemon-responders-providers-ldb.
- [[freeipa-controle-acesso-hbac-host-based-access-control-regras-pam]] — Referência cruzada direta com freeipa-controle-acesso-hbac-host-based-access-control-regras-pam.

## Fontes
- [Official SSSD GitHub Repository (`SSSD/sssd`)](https://raw.githubusercontent.com/SSSD/sssd/master/README.md) — repositório oficial do System Security Services Daemon cobrindo arquitetura de responders (`nss`, `pam`, `ssh`, `sudo`) e provedores (`ipa`, `ad`, `ldap`, `krb5`) com cache offline; consultado em 2026-10-03.
- [SSSD Official Configuration Reference (`src/examples/sssd-example.conf`)](https://raw.githubusercontent.com/SSSD/sssd/master/src/examples/sssd-example.conf) — configuração oficial de referência do `/etc/sssd/sssd.conf` detalhando domínios, `id_provider`, `auth_provider`, `access_provider`, `cache_credentials` e `enumerate = FALSE`; consultado em 2026-10-03.
