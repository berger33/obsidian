---
id: software.seguranca.tranche05.000407
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-05.md"
fontes: ["https://raw.githubusercontent.com/sqlmapproject/sqlmap/master/README.md", "https://github.com/sqlmapproject/sqlmap/wiki/Usage", "https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-pt-BR.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# sqlmap: Auditoria de Privilégios Excessivos de SGBD (`--is-dba`, `--privileges`, `--roles` e Vetores de File/OS Access)

## Em uma frase
O `sqlmap` inclui verificações específicas para auditar se a conta de banco de dados utilizada pela aplicação web possui privilégios administrativos excessivos (`--current-user`, `--is-dba`, `--privileges`, `--roles`), demonstrando como contas superusuário transformam um SQL Injection em comprometimento do sistema operacional.

## Por que importa
Se a aplicação web conecta-se ao PostgreSQL como `postgres` (`SUPERUSER`), ao MySQL com `FILE`/`GRANT OPTION` ou ao MSSQL como `sa` (`sysadmin` com `xp_cmdshell`), qualquer falha de SQL Injection permite leitura de arquivos do servidor (`--file-read`) ou execução remota de comandos.

## Como funciona
Ao executar `--current-user --is-dba`, o `sqlmap` consulta os catálogos de sistema do SGBD (ex.: `pg_user.usesuper` no PostgreSQL, `IS_SRVROLEMEMBER('sysadmin')` no MSSQL ou `USER_ROLE_PRIVS` no Oracle) e confirma se o princípio de privilégio mínimo foi violado na configuração da string de conexão.

## Exemplo
```bash
# Auditar exclusivamente o usuário atual da conexão do banco e se ele possui privilégio de DBA
python3 sqlmap.py -u "https://staging.internal.corp/invoices?invoice_id=88" \
  -p invoice_id --current-user --is-dba --privileges --batch
```

## Limites e trade-offs
Aplicações web nunca devem conectar-se ao banco com contas `SUPERUSER`/`DBA`; crie usuários dedicados restritos apenas a `SELECT`, `INSERT`, `UPDATE`, `DELETE` nas tabelas do schema da aplicação e desative `xp_cmdshell` e `local_infile`.

## Como verificar
Valide no banco de dados que `SELECT usesuper FROM pg_user WHERE usename = current_user;` retorna `false` (`current user is DBA: False`).

## Conexões
- [[sqlmap-exfiltracao-out-of-band-dns-domain-time-based-blind]] — Veja também: sqlmap: Aceleração de Blind SQL Injection via Exfiltração *Out-of-Band* DNS (`--dns-domain`).
- [[sqlmap-otimizacao-threads-keep-alive-null-connection-rate-delay]] — Veja também: sqlmap: Otimização de Rede (`-o`, `--keep-alive`, `--null-connection`, `--predict-output`) e Controle de Taxa (`--delay`).
- [[sqlmap-arquitetura-motor-deteccao-sql-injection-tecnicas-beustq]] — Referência cruzada direta com sqlmap-arquitetura-motor-deteccao-sql-injection-tecnicas-beustq.
- [[sqlmap-validacao-remediacao-prepared-statements-ci-non-interactive]] — Referência cruzada direta com sqlmap-validacao-remediacao-prepared-statements-ci-non-interactive.

## Fontes
- [sqlmap Official GitHub — README & Architecture](https://raw.githubusercontent.com/sqlmapproject/sqlmap/master/README.md) — documentação oficial do projeto sqlmap cobrindo arquitetura, instalação e escopo; consultado em 2026-10-03.
- [sqlmap Official Wiki — Usage & Switches Reference](https://github.com/sqlmapproject/sqlmap/wiki/Usage) — manual oficial de opções da CLI, técnicas BEUSTQ, --level, --risk, --tamper e OOB DNS; consultado em 2026-10-03.
- [sqlmap Official Documentation — Portuguese Reference](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-pt-BR.md) — referência oficial traduzida do sqlmap; consultado em 2026-10-03.
