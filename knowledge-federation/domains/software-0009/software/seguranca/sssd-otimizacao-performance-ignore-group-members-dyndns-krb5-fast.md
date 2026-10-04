---
id: software.seguranca.tranche15.001409
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

# Tuning de Performance e Segurança de Rede no SSSD: **`ignore_group_members`**, Atualização Dinâmica de DNS Segura (**`dyndns_update` via GSS-TSIG**) e **Kerberos FAST**

## Em uma frase
Em empresas com dezenas de milhares de funcionários, um grupo LDAP como `todos-colaboradores` pode ter 40.000 membros. Quando alguém executa `id joao` ou `ls -l`, resolver e gravar os 40.000 membros daquele grupo no cache LDB pode demorar vários segundos! Como otimizar o **SSSD** para ambientes gigantescos e garantir que a atualização de DNS e o tráfego Kerberos sejam criptograficamente protegidos?

## Por que importa
Para grupos gigantescos, ative **`ignore_group_members = true`** (e **`subdomain_inherit = ignore_group_members`** em florestas AD) na seção `[domain/...]`: com essa opção ligada, quando o SSSD consulta um grupo, ele **não baixa os 40.000 membros do grupo**, mas continua respondendo com 100% de precisão a `id joao` e `initgroups("joao")` porque consulta os grupos de `joao` diretamente pelo atributo reverso **`memberOf` / `tokenGroups`** do próprio usuário!

## Como funciona
E para segurança de rede no domínio (`ipa` ou `ad`), o SSSD inclui: **(1) `dyndns_update = true`** — atualiza automaticamente os registros DNS `A`/`AAAA` e `PTR` da máquina no BIND/AD usando assinatura criptográfica **Kerberos `GSS-TSIG` (`RFC 3645`)**; e **(2) `krb5_use_fast = try` / `demand`** (protege a pré-autenticação Kerberos com armadura **FAST `RFC 6113`** usando a keytab da máquina)!

## Exemplo
```ini
# Otimizacao de performance para grandes diretorios (ignore_group_members) e ativacao de Kerberos FAST + DNS Dinamico GSS-TSIG no /etc/sssd/sssd.conf
[domain/CORP.EXEMPLO.BR]
ignore_group_members = true
subdomain_inherit = ignore_group_members
krb5_use_fast = demand
krb5_fast_principal = host/srv-app01.corp.exemplo.br@CORP.EXEMPLO.BR
dyndns_update = true
dyndns_refresh_interval = 43200
dyndns_update_ptr = true
dyndns_ttl = 3600
```

## Limites e trade-offs
Sempre que alterar **`ignore_group_members`** no `/etc/sssd/sssd.conf`, lembre-se de limpar/expirar o cache de grupos (`sss_cache -G`) e reiniciar o SSSD para que os grupos antigos armazenados sem membros (ou com membros) sejam reavaliados sob a nova política!

## Como verificar
Habilitar **`krb5_use_fast = demand`** em servidores que possuem `/etc/krb5.keytab` válida envolve toda troca de `AS-REQ` Kerberos dos usuários dentro de um túnel cifrado com a chave da máquina — impedindo completamente que um sniffer na sub-rede capture pacotes `AS-REQ` para quebrar senhas de usuários offline no Hashcat/John!

## Conexões
- [[sssd-isolamento-privilegios-rootless-socket-activation-infopipe-dbus]] — Veja também: Hardening do Próprio SSSD: Execução **Sem Privilégios (`user = sssd`)**, **Systemd Socket Activation**, **Application Domains** e Interface D-Bus **`InfoPipe` (`sssd_ifp`)**.
- [[sssd-diagnostico-sssctl-user-checks-logs-debug-level-auditoria]] — Veja também: Diagnóstico Avançado e Forense de Autenticação no SSSD com **`sssctl` (`user-checks`, `analyze`, `debug-level`)** e Logs `/var/log/sssd/*.log`.
- [[sssd-arquitetura-system-security-services-daemon-responders-providers-ldb]] — Referência cruzada direta com sssd-arquitetura-system-security-services-daemon-responders-providers-ldb.
- [[sssd-cache-offline-credenciais-sss-cache-invalidacao-troubleshooting]] — Referência cruzada direta com sssd-cache-offline-credenciais-sss-cache-invalidacao-troubleshooting.
- [[freeipa-autenticacao-2fa-otp-totp-hotp-passkeys-radius-pkinit]] — Referência cruzada direta com freeipa-autenticacao-2fa-otp-totp-hotp-passkeys-radius-pkinit.

## Fontes
- [Official SSSD GitHub Repository (`SSSD/sssd`)](https://raw.githubusercontent.com/SSSD/sssd/master/README.md) — repositório oficial do System Security Services Daemon cobrindo arquitetura de responders (`nss`, `pam`, `ssh`, `sudo`) e provedores (`ipa`, `ad`, `ldap`, `krb5`) com cache offline; consultado em 2026-10-03.
- [SSSD Official Configuration Reference (`src/examples/sssd-example.conf`)](https://raw.githubusercontent.com/SSSD/sssd/master/src/examples/sssd-example.conf) — configuração oficial de referência do `/etc/sssd/sssd.conf` detalhando domínios, `id_provider`, `auth_provider`, `access_provider`, `cache_credentials` e `enumerate = FALSE`; consultado em 2026-10-03.
