---
id: software.seguranca.tranche15.001404
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

# Funcionamento do **Cache em Duas Camadas (`Memory Cache` + `LDB`)**, Autenticação Offline (`cache_credentials`) e Invalidação Cirúrgica com **`sss_cache`** no SSSD

## Em uma frase
Por que, às vezes, você adiciona um usuário a um novo grupo no servidor LDAP/Active Directory/FreeIPA, mas ao rodar `id usuario` imediatamente em um servidor Linux o grupo novo ainda não aparece por alguns minutos? E como forçar a atualização imediata sem apagar o cache offline inteiro?

## Por que importa
Para entregar performance de microssegundos sem bombardear o servidor LDAP a cada chamada `getpwnam()` / `initgroups()`, o **SSSD** mantém duas camadas de cache com tempos de expiração configuráveis: **(1) O Fast Memory Cache (`/var/lib/sss/mc/passwd`, `group`, `initgroups`)**, lido diretamente pela biblioteca `libnss_sss.so` no espaço de memória do processo sem nem sequer acordar o daemon `sssd_nss` (`memcache_timeout = 300` segundos)!; e **(2) O Cache Persistente em Disco `LDB` (`/var/lib/sss/db/cache_<dom>.ldb`)**, controlado por `entry_cache_timeout = 5400` segundos!

## Como funciona
Quando você precisa que uma mudança de grupo, usuário, regra `sudo` ou chave SSH recém-feita no diretório central entre em vigor imediatamente em um servidor específico, basta executar **`sss_cache -u <usuario>`** (ou **`sss_cache -E`** para marcar todas as entradas como expiradas)!

## Exemplo
```bash
# Expirar cirurgicamente o cache de um usuario ou grupo especifico no SSSD (forçando releitura imediata no LDAP/AD) e inspecionar os timestamps do cache
sss_cache -u ana.silva
sss_cache -g sre-admins
sssctl user-show ana.silva
```

## Limites e trade-offs
Qual é a enorme vantagem de rodar **`sss_cache -E`** (ou `sssctl cache-expire -E`) em vez de parar o SSSD e apagar manualmente os arquivos `/var/lib/sss/db/*.ldb` com `rm -f`? **`sss_cache -E` NÃO apaga os dados do disco**: ele apenas zera o timestamp de validade (`dataExpireTimestamp`) das entradas! Assim, se o servidor LDAP estiver online, o SSSD busca os dados novos na hora; mas se o servidor LDAP estiver fora do ar naquele momento, **o SSSD continua servindo as entradas e permitindo login offline (`cache_credentials = true`)** em vez de trancar todo mundo para fora da máquina!

## Como verificar
Para proteger os hashes de senha armazenados no cache offline (`cachedPassword`), o SSSD utiliza hashing lento com sal e permite limitar por quantos dias uma credencial cacheada pode ser usada sem contato com o KDC/LDAP através de **`offline_credentials_expiration`** no `[pam]`.

## Conexões
- [[sssd-integracao-active-directory-realmd-id-mapping-gpo-access-control]] — Veja também: Integração Nativa **Linux + Active Directory (`id_provider = ad`)** no SSSD: Ingresso com `realm join`, **Mapeamento Determinístico SID-para-UID (`ldap_id_mapping`)** e **GPOs no Linux**.
- [[sssd-controle-acesso-pam-access-provider-simple-ldap-hbac-gpo]] — Veja também: Provedores de Autorização (**`access_provider`**) no SSSD: Filtrando Quem Pode Fazer Login via **`simple` (`simple_allow_groups`)**, **`ldap` (`ldap_access_filter`)**, **`ipa` (HBAC)** e **`ad` (GPO)**.
- [[sssd-arquitetura-system-security-services-daemon-responders-providers-ldb]] — Referência cruzada direta com sssd-arquitetura-system-security-services-daemon-responders-providers-ldb.
- [[sssd-configuracao-dominios-ipa-ad-ldap-krb5-enumeracao-performance]] — Referência cruzada direta com sssd-configuracao-dominios-ipa-ad-ldap-krb5-enumeracao-performance.
- [[sssd-diagnostico-sssctl-user-checks-logs-debug-level-auditoria]] — Referência cruzada direta com sssd-diagnostico-sssctl-user-checks-logs-debug-level-auditoria.

## Fontes
- [Official SSSD GitHub Repository (`SSSD/sssd`)](https://raw.githubusercontent.com/SSSD/sssd/master/README.md) — repositório oficial do System Security Services Daemon cobrindo arquitetura de responders (`nss`, `pam`, `ssh`, `sudo`) e provedores (`ipa`, `ad`, `ldap`, `krb5`) com cache offline; consultado em 2026-10-03.
- [SSSD Official Configuration Reference (`src/examples/sssd-example.conf`)](https://raw.githubusercontent.com/SSSD/sssd/master/src/examples/sssd-example.conf) — configuração oficial de referência do `/etc/sssd/sssd.conf` detalhando domínios, `id_provider`, `auth_provider`, `access_provider`, `cache_credentials` e `enumerate = FALSE`; consultado em 2026-10-03.
