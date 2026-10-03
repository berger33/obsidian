---
id: software.seguranca.tranche02.000186
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

# osquery Resource Watchdog e Auto-Denylist: garantia de que o agente nunca degrade a CPU ou a memória do host de produção

## Em uma frase
Para garantir que uma query SQL pesada nunca comprometa a estabilidade de um servidor de produção, o `osqueryd` executa por padrão um processo **Watchdog** pai que monitora continuamente um processo **Worker** filho: se o Worker ultrapassar os limites estritos de memória RAM (`--watchdog_memory_limit`, ex.: `200` MB) ou utilização sustentada de CPU (`--watchdog_utilization_limit`), o Watchdog mata o Worker instantaneamente!

## Por que importa
Em agentes de segurança tradicionais (EDR/AV), um bug ou loop em uma regra pode consumir 100% de CPU e derrubar a aplicação de negócio; no osquery, o Watchdog isola e interrompe a query infratora.

## Como funciona
Mais importante ainda: antes de executar qualquer query agendada, o Worker grava no RocksDB qual query está prestes a rodar; se o Watchdog matar o Worker durante a execução daquela query, o novo Worker **coloca aquela query específica em *denylist* (quarentena) por 24 horas**, impedindo loops de crash!

## Exemplo
```bash
# Iniciando o osqueryd com limites estritos do Watchdog (nível normal ou restrito):
osqueryd \
  --config_path=/etc/osquery/osquery.conf \
  --watchdog_level=0 \
  --watchdog_memory_limit=250 \
  --watchdog_utilization_limit=90
```

## Limites e trade-offs
Monitore regularmente na sua frota a coluna `denylisted` da tabela **`osquery_schedule`** (`SELECT name, denylisted FROM osquery_schedule WHERE denylisted = 1;`) para identificar quais queries foram colocadas em quarentena pelo Watchdog e otimizá-las.

## Como verificar
Execute `SELECT * FROM osquery_schedule;` para verificar que `denylisted = 0` em todas as suas queries.

## Conexões
- [[osquery-evented-tables-file-integrity-monitoring-fim-process-socket-events]] — Veja também: osquery Evented Tables e File Integrity Monitoring (`FIM`): captura em tempo real via `auditd`/`ebpf`/`inotify`/`EndpointSecurity`.
- [[osquery-auditoria-containers-docker-namespaces-systemd-linux-secops]] — Veja também: osquery para Segurança de Containers e Servidores Linux: tabelas `docker_containers`, `docker_images`, `process_namespaces` e `iptables`.

## Fontes
- [osquery GitHub — README.md (SQL-Powered OS Instrumentation, Interactive Shell osqueryi, Daemon osqueryd, Fleet Managers & Thrift Extensions)](https://osquery.readthedocs.io/en/stable/introduction/using-osqueryd/) — README oficial do osquery/osquery apresentando a arquitetura de tabelas virtuais SQLite multiplataforma, gerenciadores de frota TLS (Fleet, osctrl, Zentral) e extensões; consultado em 2026-10-03.
- [osquery Official Documentation — Using osqueryd (Configuration, Schedule, Differential vs Snapshot Logs, Query Packs, Discovery Queries & Watchdog)](https://raw.githubusercontent.com/osquery/osquery/master/README.md) — Documentação oficial de operação do daemon osqueryd detalhando o agendamento de queries, logs diferenciais no RocksDB, Query Packs, FIM e proteção de recursos via Watchdog; consultado em 2026-10-03.
- [osquery — Official GitHub Repository (Linux Foundation)](https://github.com/osquery/osquery) — Repositório oficial open-source do osquery; consultado em 2026-10-03.
