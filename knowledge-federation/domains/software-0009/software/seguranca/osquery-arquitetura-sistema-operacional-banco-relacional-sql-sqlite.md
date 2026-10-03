---
id: software.seguranca.tranche02.000181
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-02.md"
fontes: ["https://raw.githubusercontent.com/osquery/osquery/master/README.md", "https://osquery.readthedocs.io/en/stable/introduction/using-osqueryd/", "https://github.com/osquery/osquery"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# osquery: arquitetura do framework que expõe o sistema operacional (`Linux`, `macOS`, `Windows`) como um banco relacional SQL

## Em uma frase
O **osquery** (`osquery/osquery`, projeto da Linux Foundation licenciado sob Apache 2.0 / GPL-2.0) é um framework de instrumentação, monitoramento de segurança e analytics de sistema operacional de alta performance que expõe o estado do **Linux**, **macOS** e **Windows** como um **banco de dados relacional consultável via SQL (motor SQLite embutido com tabelas virtuais)**.

## Por que importa
Investigar um incidente ou auditar 5.000 máquinas escrevendo scripts bash diferentes para `ps`, `netstat`/`ss`, `lsof`, `lsmod`, `crontab` no Linux, `Get-Process` no Windows e `launchctl` no macOS é frágil e difícil de parsear.

## Como funciona
No osquery, conceitos do sistema operacional são abstraídos em mais de 270 **tabelas virtuais SQL** (`processes`, `listening_ports`, `process_open_sockets`, `users`, `logged_in_users`, `kernel_modules`, `crontab`, `launchd`, `systemd_units`, `hash`, `file`), geradas sob demanda no momento do `SELECT` com `JOIN` nativo entre tabelas!

## Exemplo
```sql
-- Identificando processos em execução cujo binário original foi deletado do disco (técnica clássica de malware):
SELECT pid, name, path, cmdline, uid
FROM processes
WHERE on_disk = 0;

-- Cruzando portas TCP/UDP abertas em 0.0.0.0 com o nome e caminho do processo responsável:
SELECT DISTINCT p.pid, p.name, p.path, lp.port, lp.protocol
FROM listening_ports AS lp
JOIN processes AS p USING (pid)
WHERE lp.address = '0.0.0.0';
```

## Limites e trade-offs
Como as tabelas do osquery são *virtual tables* geradas em tempo real via chamadas de API do kernel/SO (e não dados duplicados em disco), evite fazer `SELECT * FROM file;` ou `SELECT * FROM hash;` sem cláusula `WHERE path = ...` ou `WHERE directory = ...`!

## Como verificar
Execute `osqueryi --version` e rode as queries acima no shell interativo `osqueryi`.

## Conexões
- [[osquery-osqueryi-vs-osqueryd-shell-interativo-daemon-agendamento]] — Veja também: osquery `osqueryi` vs `osqueryd`: exploração interativa ad-hoc versus monitoramento contínuo agendado por daemon.

## Fontes
- [osquery GitHub — README.md (SQL-Powered OS Instrumentation, Interactive Shell osqueryi, Daemon osqueryd, Fleet Managers & Thrift Extensions)](https://raw.githubusercontent.com/osquery/osquery/master/README.md) — README oficial do osquery/osquery apresentando a arquitetura de tabelas virtuais SQLite multiplataforma, gerenciadores de frota TLS (Fleet, osctrl, Zentral) e extensões; consultado em 2026-10-03.
- [osquery Official Documentation — Using osqueryd (Configuration, Schedule, Differential vs Snapshot Logs, Query Packs, Discovery Queries & Watchdog)](https://osquery.readthedocs.io/en/stable/introduction/using-osqueryd/) — Documentação oficial de operação do daemon osqueryd detalhando o agendamento de queries, logs diferenciais no RocksDB, Query Packs, FIM e proteção de recursos via Watchdog; consultado em 2026-10-03.
- [osquery — Official GitHub Repository (Linux Foundation)](https://github.com/osquery/osquery) — Repositório oficial open-source do osquery; consultado em 2026-10-03.
