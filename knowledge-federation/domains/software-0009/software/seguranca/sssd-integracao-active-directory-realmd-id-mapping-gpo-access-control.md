---
id: software.seguranca.tranche15.001403
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

# Integração Nativa **Linux + Active Directory (`id_provider = ad`)** no SSSD: Ingresso com `realm join`, **Mapeamento Determinístico SID-para-UID (`ldap_id_mapping`)** e **GPOs no Linux**

## Em uma frase
Quando um servidor Linux precisa ingressar diretamente em um domínio **Microsoft Active Directory** (sem FreeIPA intermediário), como o provedor **`id_provider = ad`** do **SSSD** resolve os dois maiores desafios históricos: **(1) Atribuir o mesmo `UID`/`GID` numérico Linux para um usuário do Windows em todos os servidores Linux** (mesmo que o Active Directory não tenha os atributos POSIX `uidNumber`/`gidNumber` preenchidos!) e **(2) Respeitar as políticas de acesso de `Group Policy Objects (GPOs)` do Windows no Linux**?

## Por que importa
Primeiro: com **`ldap_id_mapping = true`** (padrão no `id_provider = ad`), o SSSD utiliza um algoritmo determinístico de hash MurmurHash3 sobre o `domain SID` do Active Directory para reservar uma fatia de IDs (ex.: `200000` a `400000`) e soma o **`RID` (*Relative Identifier*, os últimos dígitos do `objectSID` do usuário no Windows)**! Assim, o usuário `S-1-5-21-...-1542` recebe exatamente o mesmo `UID` numérico em **100% dos servidores Linux da empresa**, sem que o administrador do AD precise editar atributos RFC2307!

## Como funciona
Segundo: com **`access_provider = ad`**, o SSSD baixa via SMB/CIFS (`SYSVOL`) as **GPOs vinculadas à Organizational Unit (OU) do computador Linux** no Active Directory e aplica automaticamente no Linux as diretivas **`Allow log on locally` / `Deny log on through Remote Desktop Services` (`ad_gpo_access_control = enforcing`)**!

## Exemplo
```bash
# Ingressar um servidor Linux no Active Directory usando realmd + SSSD, restrito a uma OU especifica, e auditar o mapeamento de ID do usuario
realm discover corp.empresa.br
realm join --user=admin.ad corp.empresa.br --computer-ou="OU=ServidoresLinux,DC=corp,DC=empresa,DC=br"
id carlos.silva@corp.empresa.br
sssctl user-checks carlos.silva@corp.empresa.br
```

## Limites e trade-offs
Por que você deve testar qualquer mudança nas GPOs do Active Directory usando inicialmente **`ad_gpo_access_control = permissive`** no `/etc/sssd/sssd.conf` antes de mudar para **`enforcing`**? Porque no modo `permissive`, o SSSD avalia as regras da GPO do Windows e grava no syslog/journal se o login seria negado, sem bloquear os administradores caso uma GPO de Windows Workstation tenha sido vinculada por engano à OU dos servidores Linux!

## Como verificar
Se o seu domínio Active Directory for muito grande e você quiser permitir login via SSH apenas para membros de dois grupos específicos do AD de forma imediata, você também pode usar `realm permit -g "SRE-Linux@corp.empresa.br"` (que configura `access_provider = simple` com `simple_allow_groups`).

## Conexões
- [[sssd-configuracao-dominios-ipa-ad-ldap-krb5-enumeracao-performance]] — Veja também: Configuração de Domínios no **`/etc/sssd/sssd.conf`**: Provedores `id_provider` / `auth_provider` (`ipa`, `ad`, `ldap`, `krb5`) e Por Que Manter **`enumerate = false`**!.
- [[sssd-cache-offline-credenciais-sss-cache-invalidacao-troubleshooting]] — Veja também: Funcionamento do **Cache em Duas Camadas (`Memory Cache` + `LDB`)**, Autenticação Offline (`cache_credentials`) e Invalidação Cirúrgica com **`sss_cache`** no SSSD.
- [[sssd-arquitetura-system-security-services-daemon-responders-providers-ldb]] — Referência cruzada direta com sssd-arquitetura-system-security-services-daemon-responders-providers-ldb.
- [[freeipa-trust-active-directory-cross-forest-idviews-kerberos-samba]] — Referência cruzada direta com freeipa-trust-active-directory-cross-forest-idviews-kerberos-samba.

## Fontes
- [Official SSSD GitHub Repository (`SSSD/sssd`)](https://raw.githubusercontent.com/SSSD/sssd/master/README.md) — repositório oficial do System Security Services Daemon cobrindo arquitetura de responders (`nss`, `pam`, `ssh`, `sudo`) e provedores (`ipa`, `ad`, `ldap`, `krb5`) com cache offline; consultado em 2026-10-03.
- [SSSD Official Configuration Reference (`src/examples/sssd-example.conf`)](https://raw.githubusercontent.com/SSSD/sssd/master/src/examples/sssd-example.conf) — configuração oficial de referência do `/etc/sssd/sssd.conf` detalhando domínios, `id_provider`, `auth_provider`, `access_provider`, `cache_credentials` e `enumerate = FALSE`; consultado em 2026-10-03.
