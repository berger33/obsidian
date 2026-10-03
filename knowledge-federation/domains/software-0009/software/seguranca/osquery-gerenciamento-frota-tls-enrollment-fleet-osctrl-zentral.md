---
id: software.seguranca.tranche02.000188
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

# osquery Gerenciamento Centralizado de Frota (`TLS Enrollment`, `Fleet`, `osctrl` e `Zentral`): distribuição remota de configuração e Live Queries

## Em uma frase
Conforme listado na seção *Osquery fleet managers* do README oficial, o `osqueryd` possui plugins nativos de cliente **TLS (`--config_plugin=tls`, `--logger_plugin=tls`, `--distributed_plugin=tls`)** para conectar-se a servidores de gerenciamento de frota open-source como **[Fleet](https://github.com/fleetdm/fleet)**, **[osctrl](https://github.com/jmpsec/osctrl)** e **[Zentral](https://github.com/zentralopensource/zentral)**.

## Por que importa
Gerenciar arquivos `/etc/osquery/osquery.conf` estáticos em 5.000 notebooks e servidores impede rodar uma query emergencial em tempo real (*Live Query*) quando uma nova vulnerabilidade 0-day é anunciada.

## Como funciona
Com o protocolo TLS do osquery: 1) o agente autentica-se no servidor Fleet/osctrl usando `--enroll_secret_path` e recebe um `node_key` exclusivo; 2) baixa periodicamente a configuração e os Query Packs atualizados (`config_tls_endpoint`); 3) envia os logs de resultados e status (`logger_tls_endpoint`); e 4) busca e responde a **consultas distribuídas sob demanda (*Live Queries*)** em segundos (`distributed_tls_read_endpoint` / `write_endpoint`)!

## Exemplo
```bash
# Exemplo de flags no /etc/osquery/osquery.flags para conexão mútua/TLS com um servidor Fleet ou osctrl:
--tls_hostname=fleet.internal.corp
--tls_server_certs=/etc/osquery/certs/ca.crt
--enroll_secret_path=/etc/osquery/enroll_secret.txt
--config_plugin=tls
--logger_plugin=tls
--distributed_plugin=tls
--disable_distributed=false
--distributed_interval=10
```

## Limites e trade-offs
Proteja o arquivo `/etc/osquery/enroll_secret.txt` e o banco RocksDB (`/var/osquery/osquery.db`, onde o `node_key` é persistido) com permissão `0600` restrita ao usuário `root`.

## Como verificar
Verifique na tabela `osquery_info` e nos logs de status do agente que o TLS enrollment foi concluído com sucesso.

## Conexões
- [[osquery-auditoria-containers-docker-namespaces-systemd-linux-secops]] — Veja também: osquery para Segurança de Containers e Servidores Linux: tabelas `docker_containers`, `docker_images`, `process_namespaces` e `iptables`.
- [[osquery-integracao-yara-tabelas-yara-yara-events-varredura-memoria-arquivos]] — Veja também: osquery + `YARA` (`yara` e `yara_events`): busca de assinaturas de malware sob demanda e acoplada ao File Integrity Monitoring.

## Fontes
- [osquery GitHub — README.md (SQL-Powered OS Instrumentation, Interactive Shell osqueryi, Daemon osqueryd, Fleet Managers & Thrift Extensions)](https://raw.githubusercontent.com/osquery/osquery/master/README.md) — README oficial do osquery/osquery apresentando a arquitetura de tabelas virtuais SQLite multiplataforma, gerenciadores de frota TLS (Fleet, osctrl, Zentral) e extensões; consultado em 2026-10-03.
- [osquery Official Documentation — Using osqueryd (Configuration, Schedule, Differential vs Snapshot Logs, Query Packs, Discovery Queries & Watchdog)](https://osquery.readthedocs.io/en/stable/introduction/using-osqueryd/) — Documentação oficial de operação do daemon osqueryd detalhando o agendamento de queries, logs diferenciais no RocksDB, Query Packs, FIM e proteção de recursos via Watchdog; consultado em 2026-10-03.
- [osquery — Official GitHub Repository (Linux Foundation)](https://github.com/osquery/osquery) — Repositório oficial open-source do osquery; consultado em 2026-10-03.
