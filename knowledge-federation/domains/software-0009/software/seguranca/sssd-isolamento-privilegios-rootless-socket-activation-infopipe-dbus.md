---
id: software.seguranca.tranche15.001408
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

# Hardening do Próprio SSSD: Execução **Sem Privilégios (`user = sssd`)**, **Systemd Socket Activation**, **Application Domains** e Interface D-Bus **`InfoPipe` (`sssd_ifp`)**

## Em uma frase
Historicamente, daemons de autenticação no Linux rodavam inteiramente como `root`. Como a arquitetura moderna do **SSSD** reduz drasticamente sua superfície de ataque no host e permite que aplicações web/containers consultem atributos extras de usuários (como telefone, departamento, e-mail ou foto) sem fazer chamadas LDAP diretas?

## Por que importa
Primeiro, **Execução Não-Root (`Unprivileged SSSD`)**: os processos *Responders* (`sssd_nss`, `sssd_pam`, `sssd_ssh`, `sssd_sudo`) e *Data Providers* (`sssd_be`) rodam sob a conta de sistema dedicada de baixo privilégio **`sssd`** (`uid=sssd, gid=sssd`), isolando apenas operações específicas que exigem privilégios do kernel (como validar uma keytab Kerberos ou trocar UID no login) em pequenos binários auxiliares (`krb5_child`, `ldap_child`, `selinux_child`, `p11_child`) com **Linux Capabilities mínimas**!

## Como funciona
Segundo, **Systemd Socket Activation**: os *Responders* opcionais (`sssd-ssh.socket`, `sssd-sudo.socket`, `sssd-autofs.socket`, `sssd-pac.socket`) só são iniciados pelo `systemd` quando um cliente conecta ao respectivo socket UNIX! Terceiro, o responder **`InfoPipe` (`ifp` / `org.freedesktop.sssd.infopipe`)** expõe no barramento **D-Bus do sistema** uma API segura e controlada por ACL (`allowed_uids`) para aplicações consultarem atributos estendidos de usuários e grupos no cache do SSSD!

## Exemplo
```ini
# Habilitar o responder InfoPipe (ifp) no /etc/sssd/sssd.conf permitindo que apenas root e o servico web (uid 33) consultem atributos extras via D-Bus
[sssd]
services = nss, pam, ifp
domains = CORP.EXEMPLO.BR

[ifp]
allowed_uids = root, 33
user_attributes = +mail, +telephoneNumber, +departmentNumber
```

## Limites e trade-offs
Veja como a diretiva **`user_attributes = +mail, +telephoneNumber, +departmentNumber`** na seção `[ifp]` (combinada com `ldap_user_extra_attrs` no domínio) permite que uma aplicação local consulte no D-Bus (`dbus-send` / `busctl`) o e-mail e o departamento do usuário autenticado sem que a aplicação precise ter credenciais de leitura no servidor LDAP!

## Como verificar
Para contas que existem apenas para aplicações (e que não possuem `uidNumber`/`gidNumber` POSIX nem devem poder fazer login no Linux!), o SSSD também suporta **`domain_type = application`** (`[application/<nome>]`), expondo esses usuários apenas no `InfoPipe`/`pam` sem poluir o `/etc/passwd` (`nss`)!

## Conexões
- [[sssd-idp-externo-oauth2-oidc-device-flow-entra-id-keycloak-authentik]] — Veja também: Autenticação Direta de Desktops e Servidores Linux em **Provedores Cloud OAuth2 / OIDC (`id_provider = idp` — Entra ID, Keycloak, Okta, Authentik, Kanidm)** com SSSD.
- [[sssd-otimizacao-performance-ignore-group-members-dyndns-krb5-fast]] — Veja também: Tuning de Performance e Segurança de Rede no SSSD: **`ignore_group_members`**, Atualização Dinâmica de DNS Segura (**`dyndns_update` via GSS-TSIG**) e **Kerberos FAST**.
- [[sssd-arquitetura-system-security-services-daemon-responders-providers-ldb]] — Referência cruzada direta com sssd-arquitetura-system-security-services-daemon-responders-providers-ldb.
- [[sssd-configuracao-dominios-ipa-ad-ldap-krb5-enumeracao-performance]] — Referência cruzada direta com sssd-configuracao-dominios-ipa-ad-ldap-krb5-enumeracao-performance.

## Fontes
- [Official SSSD GitHub Repository (`SSSD/sssd`)](https://raw.githubusercontent.com/SSSD/sssd/master/README.md) — repositório oficial do System Security Services Daemon cobrindo arquitetura de responders (`nss`, `pam`, `ssh`, `sudo`) e provedores (`ipa`, `ad`, `ldap`, `krb5`) com cache offline; consultado em 2026-10-03.
- [SSSD Official Configuration Reference (`src/examples/sssd-example.conf`)](https://raw.githubusercontent.com/SSSD/sssd/master/src/examples/sssd-example.conf) — configuração oficial de referência do `/etc/sssd/sssd.conf` detalhando domínios, `id_provider`, `auth_provider`, `access_provider`, `cache_credentials` e `enumerate = FALSE`; consultado em 2026-10-03.
