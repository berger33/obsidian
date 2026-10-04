---
id: software.seguranca.tranche02.000190
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

# osquery Extensions (`Thrift` API) e Logger Plugins (`filesystem`, `syslog`, `aws_kinesis`, `aws_firehose`, `kafka_producer`)

## Em uma frase
Conforme destacado no README oficial, a arquitetura do osquery permite criar **Extensões externas (`*.ext`)** em Go, Python ou C++ comunicando-se com o `osqueryd` via socket local **Apache Thrift**, além de enviar os logs diretamente para **`filesystem`**, **`syslog`**, **`aws_kinesis`**, **`aws_firehose`**, **`aws_s3`** ou **`kafka_producer`** sem precisar de agente coletor intermediário.

## Por que importa
Quando sua equipe precisa expor como tabela SQL um subsistema interno proprietário (ou executar ações controladas) sem recompilar o binário oficial do osquery, o SDK de Extensões (ex.: `osquery-go`) permite registrar novas tabelas virtuais em poucos minutos.

## Como funciona
Por segurança, o `osqueryd` verifica que todo binário de extensão carregado via `--extensions_autoload` pertença ao usuário `root` e não tenha permissão de escrita para outros usuários (evitando sequestro de extensão por usuários locais).

## Exemplo
```bash
# Listando os plugins de logger e config compilados no binário osqueryi/osqueryd:
osqueryi "SELECT name, type, active FROM osquery_registry WHERE registry = 'logger';"
```

## Limites e trade-offs
Ao usar `filesystem` logger (`--logger_path=/var/log/osquery`), o osquery grava `osqueryd.results.log` (JSON linha-a-linha pronto para Vector, Fluent Bit ou Wazuh) e `osqueryd.snapshots.log`.

## Como verificar
Inspecione as últimas linhas de `/var/log/osquery/osqueryd.results.log` com `jq .` para validar o schema de saída.

## Conexões
- [[osquery-integracao-yara-tabelas-yara-yara-events-varredura-memoria-arquivos]] — Veja também: osquery + `YARA` (`yara` e `yara_events`): busca de assinaturas de malware sob demanda e acoplada ao File Integrity Monitoring.

## Fontes
- [osquery GitHub — README.md (SQL-Powered OS Instrumentation, Interactive Shell osqueryi, Daemon osqueryd, Fleet Managers & Thrift Extensions)](https://raw.githubusercontent.com/osquery/osquery/master/README.md) — README oficial do osquery/osquery apresentando a arquitetura de tabelas virtuais SQLite multiplataforma, gerenciadores de frota TLS (Fleet, osctrl, Zentral) e extensões; consultado em 2026-10-03.
- [osquery Official Documentation — Using osqueryd (Configuration, Schedule, Differential vs Snapshot Logs, Query Packs, Discovery Queries & Watchdog)](https://osquery.readthedocs.io/en/stable/introduction/using-osqueryd/) — Documentação oficial de operação do daemon osqueryd detalhando o agendamento de queries, logs diferenciais no RocksDB, Query Packs, FIM e proteção de recursos via Watchdog; consultado em 2026-10-03.
- [osquery — Official GitHub Repository (Linux Foundation)](https://github.com/osquery/osquery) — Repositório oficial open-source do osquery; consultado em 2026-10-03.
