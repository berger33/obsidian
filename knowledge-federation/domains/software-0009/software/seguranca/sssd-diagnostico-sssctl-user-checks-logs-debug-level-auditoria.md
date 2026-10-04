---
id: software.seguranca.tranche15.001410
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

# Diagnóstico Avançado e Forense de Autenticação no SSSD com **`sssctl` (`user-checks`, `analyze`, `debug-level`)** e Logs `/var/log/sssd/*.log`

## Em uma frase
Quando um login SSH ou regra `sudo` falha em um servidor integrado ao LDAP/Active Directory/FreeIPA, como diagnosticar em 30 segundos se o problema está na resolução de identidade (`NSS`), na validação de senha/Kerberos (`PAM auth`), na regra de acesso HBAC/GPO (`PAM account`) ou na comunicação TLS/GSSAPI com o controlador de domínio — sem precisar reiniciar o SSSD em produção?

## Por que importa
Usando a suíte de diagnóstico oficial **`sssctl`**!

## Como funciona
Veja os 4 subcomandos essenciais do `sssctl` para todo engenheiro Linux/SecOps: **(1) `sssctl user-checks <usuario> -s sshd`** — testa de ponta a ponta a resolução `getpwnam()`, os grupos, o InfoPipe e simula a pilha PAM para o serviço `sshd`; **(2) `sssctl debug-level 9`** — altera dinamicamente em memória o nível de log (`0` a `9`) de todos os processos do SSSD a quente sem reiniciar o serviço!; **(3) `sssctl logs-fetch` / `sssctl logs-remove`**; e **(4) `sssctl analyze request show <id>`**! O subcomando **`sssctl analyze`** rastreia uma requisição individual pelo seu **`CID` (*Client ID*)** cruzando automaticamente os arquivos `/var/log/sssd/sssd_nss.log`, `sssd_pam.log`, `sssd_<dominio>.log`, `krb5_child.log` e `ldap_child.log`!

## Exemplo
```bash
# Elevar o nivel de debug do SSSD a quente para 7, testar a autenticacao/autorizacao do usuario e rastrear a requisicao com sssctl analyze
sssctl debug-level 7
sssctl user-checks ana.silva --action=acct --service=sshd
sssctl analyze request list
sssctl debug-level 2
```

## Limites e trade-offs
Por que o **`sssctl analyze`** é uma revolução no troubleshooting do SSSD? Porque antes dele, o administrador precisava abrir 5 arquivos de log diferentes em `/var/log/sssd/` e tentar correlacionar timestamps manualmente no milissegundo; com `sssctl analyze request list` e `sssctl analyze request show 1`, a ferramenta monta a árvore cronológica exata da chamada desde a entrada no `sssd_pam` até a query LDAP no `sssd_be` e o resultado do `krb5_child`!

## Como verificar
Lembre-se de sempre voltar o nível de log para o padrão (**`sssctl debug-level 2`** ou `0x0070`) após terminar o diagnóstico para não encher a partição `/var/log` em servidores com alto volume de logins.

## Conexões
- [[sssd-otimizacao-performance-ignore-group-members-dyndns-krb5-fast]] — Veja também: Tuning de Performance e Segurança de Rede no SSSD: **`ignore_group_members`**, Atualização Dinâmica de DNS Segura (**`dyndns_update` via GSS-TSIG**) e **Kerberos FAST**.
- [[sssd-arquitetura-system-security-services-daemon-responders-providers-ldb]] — Referência cruzada direta com sssd-arquitetura-system-security-services-daemon-responders-providers-ldb.
- [[sssd-cache-offline-credenciais-sss-cache-invalidacao-troubleshooting]] — Referência cruzada direta com sssd-cache-offline-credenciais-sss-cache-invalidacao-troubleshooting.

## Fontes
- [Official SSSD GitHub Repository (`SSSD/sssd`)](https://raw.githubusercontent.com/SSSD/sssd/master/README.md) — repositório oficial do System Security Services Daemon cobrindo arquitetura de responders (`nss`, `pam`, `ssh`, `sudo`) e provedores (`ipa`, `ad`, `ldap`, `krb5`) com cache offline; consultado em 2026-10-03.
- [SSSD Official Configuration Reference (`src/examples/sssd-example.conf`)](https://raw.githubusercontent.com/SSSD/sssd/master/src/examples/sssd-example.conf) — configuração oficial de referência do `/etc/sssd/sssd.conf` detalhando domínios, `id_provider`, `auth_provider`, `access_provider`, `cache_credentials` e `enumerate = FALSE`; consultado em 2026-10-03.
