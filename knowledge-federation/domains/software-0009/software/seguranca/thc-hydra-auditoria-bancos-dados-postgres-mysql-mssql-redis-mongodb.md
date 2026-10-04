---
id: software.seguranca.tranche16.001575
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-16.md"
fontes: ["https://raw.githubusercontent.com/vanhauser-thc/thc-hydra/master/README", "https://raw.githubusercontent.com/vanhauser-thc/thc-hydra/master/hydra.1"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Auditando Autenticação de Bancos de Dados (**PostgreSQL, MySQL/MariaDB, MS-SQL, Redis, MongoDB e Oracle**) com o THC-Hydra

## Em uma frase
Durante uma avaliação de segurança interna, portas de bancos de dados como **PostgreSQL (`5432`)**, **MySQL/MariaDB (`3306`)**, **MS-SQL (`1433`)**, **Redis (`6379`)** e **Oracle (`1521`)** são frequentemente encontradas expostas para sub-redes de aplicação inteiras. Como usar os módulos nativos de banco de dados do **THC-Hydra** para verificar se contas administrativas (`postgres`, `root`, `sa`, `default`) usam senhas padrão ou fracas?

## Por que importa
O Hydra possui clientes binários nativos de protocolo para cada um desses bancos (não exigindo instalar clientes pesados completos): **(1) `postgres`** (aceita o nome do banco inicial como opção de módulo, padrão `template1`); **(2) `mysql`**.

## Como funciona
**(3) `mssql`**; **(4) `redis`** (testa tanto `AUTH <senha>` legado quanto `AUTH <usuario> <senha>` de ACLs do Redis 6+!); e **(5) `oracle-listener` / `oracle-sid` / `oracle`**!

## Exemplo
```bash
# Testar se instancias PostgreSQL e Redis de homologacao aceitam credenciais padrao ou senha nula (-e ns) parando no primeiro acerto (-f)
hydra -l postgres -e ns -P ./senhas_padrao_db.txt -f -t 4 postgres://192.0.2.50:5432/postgres
hydra -p SenhaPadraoRedis123 -f -t 4 redis://192.0.2.50:6379
```

## Limites e trade-offs
Por que incluir sempre **`-e ns`** (`n` = senha em branco / sem senha, `s` = senha igual ao nome do usuário `postgres:postgres` / `sa:sa` / `root:root`) ao auditar bancos de dados de desenvolvimento, homologação ou containers Docker esquecidos? Porque imagens oficiais de container subidas rapidamente por desenvolvedores com `POSTGRES_PASSWORD=postgres` ou instâncias Redis sem `requirepass` são uma das causas mais frequentes de comprometimento inicial em ambientes cloud e Kubernetes!

## Como verificar
E do lado defensivo (Hardening de Bancos de Dados): **(1)** Configure `pg_hba.conf` no PostgreSQL exigindo **`scram-sha-256`** ou certificados TLS (`clientcert=verify-full`) restrito às sub-redes exatas dos Pods de aplicação; **(2)** Desative a conta `sa` no MS-SQL priorizando autenticação Kerberos/AD; e **(3)** Configure ACLs nominais e TLS no Redis.

## Conexões
- [[thc-hydra-controle-concorrencia-tasks-t-timeouts-w-restore-sessao-r]] — Veja também: Controle de Concorrência (**`-t` vs. `-T`**), Pausa Entre Tentativas (**`-W` / `-c`**), Retomada de Sessão (**`-R` `hydra.restore`**) e Saída JSON (**`-b json -o`**) no THC-Hydra.
- [[thc-hydra-auditoria-protocolos-infraestrutura-ssh-sshkey-rdp-smb-snmp]] — Veja também: Auditando Protocolos de Infraestrutura e Gerência no THC-Hydra: **`ssh` / `sshkey`**, **`rdp`**, **`smb`**, **`snmp` (Community Strings v1/v2c/v3)** e **`cisco-enable`**.
- [[thc-hydra-arquitetura-auditoria-autenticacao-rede-paralela-modulos]] — Referência cruzada direta com thc-hydra-arquitetura-auditoria-autenticacao-rede-paralela-modulos.
- [[thc-hydra-modos-credenciais-password-spraying-u-colon-file-e-nsr]] — Referência cruzada direta com thc-hydra-modos-credenciais-password-spraying-u-colon-file-e-nsr.

## Fontes
- [THC-Hydra Official Documentation (`vanhauser-thc/thc-hydra/master/README`)](https://raw.githubusercontent.com/vanhauser-thc/thc-hydra/master/README) — documentação oficial do THC-Hydra detalhando protocolos suportados, sintaxe URI `PROTOCOL://TARGET:PORT/OPTIONS`, listas `-M` e inspeção de módulos `hydra -U`; consultado em 2026-10-03.
- [Official `hydra(1)` Manpage Specification (`vanhauser-thc/thc-hydra/master/hydra.1`)](https://raw.githubusercontent.com/vanhauser-thc/thc-hydra/master/hydra.1) — manpage oficial `hydra(1)` detalhando flags `-l`/`-L`, `-p`/`-P`, `-C`, `-e nsr`, `-u`, `-f`/`-F`, `-t`/`-T`, `-w`/`-W`/`-c`, `-R`, `-b json` e o utilitário `pw-inspector`; consultado em 2026-10-03.
