---
id: software.seguranca.tranche15.001402
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

# Configuração de Domínios no **`/etc/sssd/sssd.conf`**: Provedores `id_provider` / `auth_provider` (`ipa`, `ad`, `ldap`, `krb5`) e Por Que Manter **`enumerate = false`**!

## Em uma frase
Ao configurar uma seção **`[domain/<NOME>]`** no `/etc/sssd/sssd.conf` (conforme documentado no `sssd-example.conf` oficial), quais são as combinações recomendadas de `id_provider` e `auth_provider`, e por que a diretiva **`enumerate = false`** vem desativada por padrão?

## Por que importa
O SSSD separa os papéis em provedores independentes dentro do domínio: **`id_provider`** (busca UIDs, GIDs e membros de grupos: `ipa`, `ad`, `ldap`), **`auth_provider`** (valida senhas/tickets/2FA: `ipa`, `ad`, `krb5`, `ldap`), **`access_provider`** (avalia autorização de login: `ipa` HBAC, `ad` GPO, `simple`, `ldap`) e **`chpass_provider`** (troca de senha)!

## Como funciona
E atenção ao aviso explícito do `sssd-example.conf` sobre **`enumerate = false`**: se você mudar `enumerate = true` em um diretório corporativo com 50.000 usuários e 10.000 grupos, o SSSD tentará baixar e atualizar periodicamente **o diretório LDAP inteiro**, sobrecarregando a CPU do servidor LDAP e a rede! Com **`enumerate = false`** (o padrão recomendado!), o SSSD busca e armazena no cache **sob demanda (*On-Demand Lookup*)** apenas os usuários e grupos efetivamente consultados naquela máquina!

## Exemplo
```ini
# Configuracao segura de /etc/sssd/sssd.conf conectando a um dominio LDAP/Kerberos com cache offline e enumeracao desativada
[sssd]
services = nss, pam, ssh, sudo
domains = CORP.EXEMPLO.BR

[domain/CORP.EXEMPLO.BR]
id_provider = ldap
auth_provider = krb5
chpass_provider = krb5
ldap_schema = rfc2307bis
ldap_uri = ldaps://ldap01.corp.exemplo.br, ldaps://ldap02.corp.exemplo.br
ldap_search_base = dc=corp,dc=exemplo,dc=br
ldap_sasl_mech = GSSAPI
krb5_server = kdc01.corp.exemplo.br, kdc02.corp.exemplo.br
krb5_realm = CORP.EXEMPLO.BR
enumerate = false
cache_credentials = true
```

## Limites e trade-offs
Repare na diferença documentada entre **`ldap_schema = rfc2307`** e **`ldap_schema = rfc2307bis`** (usado pelo Active Directory, 389-ds e FreeIPA modernos): no `rfc2307` antigo, os membros de um grupo são salvos apenas como strings de login no atributo `memberUid` (não permitindo grupos aninhados!), enquanto no **`rfc2307bis`** os membros são salvos como *Distinguished Names (`DN`)* completos no atributo `member`, permitindo **aninhamento de grupos (`Nested Groups` até o limite `ldap_group_nesting_level`)**!

## Como verificar
Em conexões com `id_provider = ldap` sem Kerberos GSSAPI, exija sempre **`ldaps://`** ou **`ldap_id_use_start_tls = true`** com `ldap_tls_reqcert = demand` para impedir vazamento de metadados de identidade em texto claro.

## Conexões
- [[sssd-arquitetura-system-security-services-daemon-responders-providers-ldb]] — Veja também: Arquitetura do **SSSD (`SSSD/sssd` — *System Security Services Daemon*)**: Responders (`nss`, `pam`, `ssh`, `sudo`, `autofs`), Backends Plugáveis e Cache Offline **`ldb`**.
- [[sssd-integracao-active-directory-realmd-id-mapping-gpo-access-control]] — Veja também: Integração Nativa **Linux + Active Directory (`id_provider = ad`)** no SSSD: Ingresso com `realm join`, **Mapeamento Determinístico SID-para-UID (`ldap_id_mapping`)** e **GPOs no Linux**.

## Fontes
- [Official SSSD GitHub Repository (`SSSD/sssd`)](https://raw.githubusercontent.com/SSSD/sssd/master/README.md) — repositório oficial do System Security Services Daemon cobrindo arquitetura de responders (`nss`, `pam`, `ssh`, `sudo`) e provedores (`ipa`, `ad`, `ldap`, `krb5`) com cache offline; consultado em 2026-10-03.
- [SSSD Official Configuration Reference (`src/examples/sssd-example.conf`)](https://raw.githubusercontent.com/SSSD/sssd/master/src/examples/sssd-example.conf) — configuração oficial de referência do `/etc/sssd/sssd.conf` detalhando domínios, `id_provider`, `auth_provider`, `access_provider`, `cache_credentials` e `enumerate = FALSE`; consultado em 2026-10-03.
