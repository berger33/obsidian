---
id: software.seguranca.tranche15.001401
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

# Arquitetura do **SSSD (`SSSD/sssd` — *System Security Services Daemon*)**: Responders (`nss`, `pam`, `ssh`, `sudo`, `autofs`), Backends Plugáveis e Cache Offline **`ldb`**

## Em uma frase
Como os sistemas operacionais Linux corporativos modernos (RHEL, Fedora, Ubuntu, Debian, SUSE, AlmaLinux, Rocky Linux) se conectam simultaneamente a diretórios remotos (**FreeIPA, Microsoft Active Directory, 389-ds/OpenLDAP, Kerberos e Provedores OAuth2/OIDC**) sem travar os comandos locais (`ls -l`, `id`, `sudo`, `ssh`) quando o link de rede oscila e permitindo que usuários façam login no notebook mesmo desconectados da rede corporativa?

## Por que importa
Através do **SSSD (*System Security Services Daemon*)**! Diferente da arquitetura legada dos anos 2000 (onde cada processo chamava `nss_ldap` e `pam_ldap` abrindo dezenas de conexões TCP diretas ao servidor LDAP!), o **SSSD** atua como um intermediário inteligente em espaço de usuário dividido em duas camadas comunicando-se via sockets UNIX locais: **(1) `Responders` de Front-End (`sssd_nss`, `sssd_pam`, `sssd_ssh`, `sssd_sudo`, `sssd_autofs`, `sssd_pac`, `sssd_ifp`)** que atendem instantaneamente o sistema operacional; e **(2) `Data Providers` de Back-End (`sssd_be`)** que falam com **IPA, Active Directory (`ad`), LDAP (`ldap`), Kerberos (`krb5`) ou IdP OIDC**!

## Como funciona
No coração entre os *Responders* e os *Providers* reside o **Banco de Dados de Cache Local Baseado em `LDB` (`/var/lib/sss/db/cache_<dominio>.ldb`)**: ele armazena em cache de dois níveis (memória `mmap` ultrarrápida em `/var/lib/sss/mc/` + disco `ldb` transacional) as identidades POSIX, grupos, regras `sudo`, mapas `autofs`, regras HBAC e hashes de credenciais (`cache_credentials = true`) para operação 100% resiliente offline!

## Exemplo
```bash
# Inspecionar o status do SSSD, dos dominios conectados (online/offline) e verificar as permissoes estritas de /etc/sssd/sssd.conf
sssctl domain-list
sssctl domain-status exemplo.br
stat -c "%a %U:%G %n" /etc/sssd/sssd.conf
```

## Limites e trade-offs
Regra de segurança obrigatória do daemon SSSD: o arquivo **`/etc/sssd/sssd.conf`** (e quaisquer fragmentos em `/etc/sssd/conf.d/*.conf`) **DEVE pertencer a `root:root` (ou usuário `sssd`) com permissão estrita `0600` (`chmod 0600 /etc/sssd/sssd.conf`)**! Se a permissão for mais aberta (ex.: `0644`), o SSSD se recusa a iniciar por design para evitar exposição de parâmetros de bind ou domínios!

## Como verificar
Use sempre **`sssctl config-check`** após editar `/etc/sssd/sssd.conf` para validar a sintaxe e detectar opções com erros de digitação antes de reiniciar o serviço `sssd`.

## Conexões
- [[sssd-configuracao-dominios-ipa-ad-ldap-krb5-enumeracao-performance]] — Veja também: Configuração de Domínios no **`/etc/sssd/sssd.conf`**: Provedores `id_provider` / `auth_provider` (`ipa`, `ad`, `ldap`, `krb5`) e Por Que Manter **`enumerate = false`**!.
- [[sssd-cache-offline-credenciais-sss-cache-invalidacao-troubleshooting]] — Referência cruzada direta com sssd-cache-offline-credenciais-sss-cache-invalidacao-troubleshooting.
- [[freeipa-arquitetura-identidade-linux-389ds-kerberos-dogtag-pki-dns]] — Referência cruzada direta com freeipa-arquitetura-identidade-linux-389ds-kerberos-dogtag-pki-dns.

## Fontes
- [Official SSSD GitHub Repository (`SSSD/sssd`)](https://raw.githubusercontent.com/SSSD/sssd/master/README.md) — repositório oficial do System Security Services Daemon cobrindo arquitetura de responders (`nss`, `pam`, `ssh`, `sudo`) e provedores (`ipa`, `ad`, `ldap`, `krb5`) com cache offline; consultado em 2026-10-03.
- [SSSD Official Configuration Reference (`src/examples/sssd-example.conf`)](https://raw.githubusercontent.com/SSSD/sssd/master/src/examples/sssd-example.conf) — configuração oficial de referência do `/etc/sssd/sssd.conf` detalhando domínios, `id_provider`, `auth_provider`, `access_provider`, `cache_credentials` e `enumerate = FALSE`; consultado em 2026-10-03.
