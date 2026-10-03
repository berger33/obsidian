---
id: software.seguranca.tranche02.000187
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

# osquery para Segurança de Containers e Servidores Linux: tabelas `docker_containers`, `docker_images`, `process_namespaces` e `iptables`

## Em uma frase
Em servidores Linux e nós de clusters de containers, o osquery fornece tabelas nativas para auditar o runtime de containers e o isolamento do kernel: **`docker_containers`**, **`docker_container_mounts`**, **`docker_container_ports`**, **`docker_images`**, **`process_namespaces`** (identificando os namespaces `mnt`, `net`, `pid`, `user`, `ipc`, `uts`, `cgroup` de cada processo), **`systemd_units`**, **`sudoers`** e **`iptables`**.

## Por que importa
Um container mal configurado montando o socket `/var/run/docker.sock` ou o diretório raiz `/` do host com `privileged = 1` permite escape trivial para o sistema operacional hospedeiro.

## Como funciona
Com uma simples query SQL fazendo `JOIN` entre `docker_containers` e `docker_container_mounts`, o `osqueryd` detecta em toda a frota qualquer container privilegiado ou que monte caminhos sensíveis do host.

## Exemplo
```sql
-- Detectando containers em execução em modo privilegiado ou montando o docker.sock do host:
SELECT c.id, c.name, c.image, c.privileged, m.source, m.destination, m.rw
FROM docker_containers AS c
JOIN docker_container_mounts AS m USING (id)
WHERE c.privileged = 1 OR m.source LIKE '%docker.sock%';
```

## Limites e trade-offs
A tabela `processes` do Linux também inclui a coluna `cgroup_path`, permitindo identificar diretamente a qual Pod Kubernetes ou container um processo suspeito pertence mesmo sem consultar o daemon do Docker.

## Como verificar
Execute `osqueryi "SELECT pid, name, cgroup_path FROM processes LIMIT 10;"` para inspecionar os cgroups dos processos ativos.

## Conexões
- [[osquery-watchdog-protecao-recursos-cpu-memoria-denylist-queries]] — Veja também: osquery Resource Watchdog e Auto-Denylist: garantia de que o agente nunca degrade a CPU ou a memória do host de produção.
- [[osquery-gerenciamento-frota-tls-enrollment-fleet-osctrl-zentral]] — Veja também: osquery Gerenciamento Centralizado de Frota (`TLS Enrollment`, `Fleet`, `osctrl` e `Zentral`): distribuição remota de configuração e Live Queries.

## Fontes
- [osquery GitHub — README.md (SQL-Powered OS Instrumentation, Interactive Shell osqueryi, Daemon osqueryd, Fleet Managers & Thrift Extensions)](https://raw.githubusercontent.com/osquery/osquery/master/README.md) — README oficial do osquery/osquery apresentando a arquitetura de tabelas virtuais SQLite multiplataforma, gerenciadores de frota TLS (Fleet, osctrl, Zentral) e extensões; consultado em 2026-10-03.
- [osquery Official Documentation — Using osqueryd (Configuration, Schedule, Differential vs Snapshot Logs, Query Packs, Discovery Queries & Watchdog)](https://osquery.readthedocs.io/en/stable/introduction/using-osqueryd/) — Documentação oficial de operação do daemon osqueryd detalhando o agendamento de queries, logs diferenciais no RocksDB, Query Packs, FIM e proteção de recursos via Watchdog; consultado em 2026-10-03.
- [osquery — Official GitHub Repository (Linux Foundation)](https://github.com/osquery/osquery) — Repositório oficial open-source do osquery; consultado em 2026-10-03.
