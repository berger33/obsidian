---
id: software.seguranca.tranche02.000185
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

# osquery Evented Tables e File Integrity Monitoring (`FIM`): captura em tempo real via `auditd`/`ebpf`/`inotify`/`EndpointSecurity`

## Em uma frase
Além de fazer polling periódico no momento do `SELECT`, o `osqueryd` possui um **Event Publisher/Subscriber Framework** que escuta APIs de eventos do kernel em tempo real (`inotify`/`auditd`/`eBPF` no Linux, `EndpointSecurity`/`FSEvents` no macOS, `ETW` no Windows) e grava os eventos no RocksDB para consulta nas tabelas **`file_events`**, **`process_events`**, **`socket_events`** e **`user_events`**!

## Por que importa
Se um invasor criar um binário temporário, executá-lo por 2 segundos e apagá-lo imediatamente, uma query tradicional que faz polling na tabela `processes` a cada 5 minutos nunca verá o processo; já as tabelas baseadas em eventos (`process_events` e `file_events`) capturam a execução e a alteração do arquivo no exato instante em que ocorreram.

## Como funciona
Para habilitar **File Integrity Monitoring (FIM)** em diretórios críticos (atendendo requisitos PCI-DSS 11.5), basta declarar a seção `file_paths` no `osquery.conf` e agendar uma query sobre `file_events` (que já calcula automaticamente os hashes `md5`, `sha1` e `sha256` do arquivo modificado).

## Exemplo
```json
{
  "file_paths": {
    "system_binaries": [
      "/bin/%%",
      "/sbin/%%",
      "/usr/bin/%%",
      "/usr/sbin/%%"
    ],
    "critical_configs": [
      "/etc/passwd",
      "/etc/shadow",
      "/etc/sudoers",
      "/etc/ssh/sshd_config"
    ]
  },
  "schedule": {
    "fim_events": {
      "query": "SELECT target_path, action, uid, sha256, time FROM file_events;",
      "interval": 60
    }
  }
}
```

## Limites e trade-offs
Na sintaxe de `file_paths` do osquery, um único `%` casa arquivos e pastas em um nível, enquanto **`%%`** casa recursivamente todos os subdiretórios abaixo daquele caminho; use `exclude_paths` para excluir diretórios ruidosos de cache/logs.

## Como verificar
Verifique se os coletores de eventos estão ativos consultando `SELECT name, publisher, type, subscriptions, events, active FROM osquery_events;`.

## Conexões
- [[osquery-query-packs-organizacao-modular-discovery-queries-platform-version]] — Veja também: osquery `Query Packs`: agrupamento modular de queries de detecção com filtros `platform`, `version`, `shard` e `discovery`.
- [[osquery-watchdog-protecao-recursos-cpu-memoria-denylist-queries]] — Veja também: osquery Resource Watchdog e Auto-Denylist: garantia de que o agente nunca degrade a CPU ou a memória do host de produção.

## Fontes
- [osquery GitHub — README.md (SQL-Powered OS Instrumentation, Interactive Shell osqueryi, Daemon osqueryd, Fleet Managers & Thrift Extensions)](https://osquery.readthedocs.io/en/stable/introduction/using-osqueryd/) — README oficial do osquery/osquery apresentando a arquitetura de tabelas virtuais SQLite multiplataforma, gerenciadores de frota TLS (Fleet, osctrl, Zentral) e extensões; consultado em 2026-10-03.
- [osquery Official Documentation — Using osqueryd (Configuration, Schedule, Differential vs Snapshot Logs, Query Packs, Discovery Queries & Watchdog)](https://raw.githubusercontent.com/osquery/osquery/master/README.md) — Documentação oficial de operação do daemon osqueryd detalhando o agendamento de queries, logs diferenciais no RocksDB, Query Packs, FIM e proteção de recursos via Watchdog; consultado em 2026-10-03.
- [osquery — Official GitHub Repository (Linux Foundation)](https://github.com/osquery/osquery) — Repositório oficial open-source do osquery; consultado em 2026-10-03.
