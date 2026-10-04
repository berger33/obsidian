---
id: software.seguranca.tranche02.000184
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
fontes: ["https://osquery.readthedocs.io/en/stable/introduction/using-osqueryd/", "https://raw.githubusercontent.com/osquery/osquery/master/README.md", "https://github.com/osquery/osquery"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# osquery `Query Packs`: agrupamento modular de queries de detecção com filtros `platform`, `version`, `shard` e `discovery`

## Em uma frase
No `osqueryd`, os **Query Packs** permitem organizar dezenas de queries temáticas (como `incident-response`, `it-compliance`, `ossec-rootkit`, `vuln-management`, `hardware-monitoring`) em arquivos JSON separados, aplicando filtros condicionais de **`platform`** (`linux`, `darwin`, `windows`, `posix`), **`version`** mínima do osquery, **`shard`** (amostragem percentual `1–100`) e **`discovery`** (queries SQL de pré-condição)!

## Por que importa
Você não quer executar queries de pacotes Debian (`deb_packages`) em um servidor RedHat/AlmaLinux ou em um MacBook, nem rodar uma query de auditoria de containers Docker em máquinas que nem possuem o daemon `dockerd` instalado.

## Como funciona
No bloco **`discovery`** de um Pack, você define uma lista de queries SQL; o `osqueryd` só executa as queries daquele Pack nos hosts onde **todas** as queries de `discovery` retornarem pelo menos uma linha (ex.: `SELECT pid FROM processes WHERE name = 'dockerd';`)!

## Exemplo
```json
{
  "platform": "linux",
  "shard": 100,
  "discovery": [
    "SELECT pid FROM processes WHERE name = 'containerd' OR name = 'dockerd' LIMIT 1;"
  ],
  "queries": {
    "running_containers_audit": {
      "query": "SELECT id, name, image, privileged, security_options FROM docker_containers;",
      "interval": 600
    }
  }
}
```

## Limites e trade-offs
Use o parâmetro **`"shard": 10`** ao implantar uma query nova em uma frota grande para testá-la inicialmente em apenas 10% das máquinas e medir seu impacto de CPU/memória na tabela `osquery_schedule`.

## Como verificar
Audite o custo de performance de cada query agendada consultando `SELECT name, executions, wall_time, user_time, system_time, average_memory FROM osquery_schedule;`.

## Conexões
- [[osquery-differential-logs-added-removed-vs-snapshot-queries-rocksdb]] — Veja também: osquery Logs Diferenciais (`added` / `removed` via RocksDB) vs `snapshot: true`: como o `osqueryd` detecta mudanças de estado sem inundar o SIEM.
- [[osquery-evented-tables-file-integrity-monitoring-fim-process-socket-events]] — Veja também: osquery Evented Tables e File Integrity Monitoring (`FIM`): captura em tempo real via `auditd`/`ebpf`/`inotify`/`EndpointSecurity`.

## Fontes
- [osquery GitHub — README.md (SQL-Powered OS Instrumentation, Interactive Shell osqueryi, Daemon osqueryd, Fleet Managers & Thrift Extensions)](https://osquery.readthedocs.io/en/stable/introduction/using-osqueryd/) — README oficial do osquery/osquery apresentando a arquitetura de tabelas virtuais SQLite multiplataforma, gerenciadores de frota TLS (Fleet, osctrl, Zentral) e extensões; consultado em 2026-10-03.
- [osquery Official Documentation — Using osqueryd (Configuration, Schedule, Differential vs Snapshot Logs, Query Packs, Discovery Queries & Watchdog)](https://raw.githubusercontent.com/osquery/osquery/master/README.md) — Documentação oficial de operação do daemon osqueryd detalhando o agendamento de queries, logs diferenciais no RocksDB, Query Packs, FIM e proteção de recursos via Watchdog; consultado em 2026-10-03.
- [osquery — Official GitHub Repository (Linux Foundation)](https://github.com/osquery/osquery) — Repositório oficial open-source do osquery; consultado em 2026-10-03.
