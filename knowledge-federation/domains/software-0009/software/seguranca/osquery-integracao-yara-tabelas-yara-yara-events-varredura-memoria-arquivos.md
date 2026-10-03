---
id: software.seguranca.tranche02.000189
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

# osquery + `YARA` (`yara` e `yara_events`): busca de assinaturas de malware sob demanda e acoplada ao File Integrity Monitoring

## Em uma frase
O osquery integra nativamente o motor **[YARA](https://virustotal.github.io/yara/)** (a ferramenta padrão de pesquisa e classificação de malware por padrões binários e textuais) através da tabela sob demanda **`yara`** e da tabela orientada a eventos **`yara_events`** (que dispara regras YARA automaticamente sempre que o File Integrity Monitoring detecta um arquivo novo ou modificado)!

## Por que importa
Hashes SHA-256 mudam completamente se o invasor alterar um único byte do binário; regras YARA detectam famílias inteiras de web shells, *cryptominers*, *infostealers* e *backdoors* pelas suas strings, sequências de opcodes e estrutura ELF/PE/Mach-O.

## Como funciona
Configurando a seção `yara` no `osquery.conf` (mapeando grupos de assinaturas `.yar` aos caminhos monitorados em `file_paths`), qualquer arquivo gravado em `/tmp`, `/var/www` ou `/usr/local/bin` é escaneado instantaneamente contra suas regras YARA e registrado em `yara_events`.

## Exemplo
```sql
-- Escaneando um binário suspeito sob demanda contra uma regra YARA inline ou arquivo de regras via osqueryi:
SELECT path, matches, count, siggroup, sigfile
FROM yara
WHERE path = '/tmp/suspicious_binary'
  AND sigfile = '/etc/osquery/yara/linux_malware.yar';
```

## Limites e trade-offs
Restrinja as regras YARA acopladas ao FIM (`yara_events`) a diretórios de executáveis, uploads web e pastas temporárias, evitando varrer arquivos de banco de dados de múltiplos gigabytes a cada escrita.

## Como verificar
Teste a tabela `yara` no `osqueryi` passando `sigrule` inline contra um arquivo de teste inofensivo.

## Conexões
- [[osquery-gerenciamento-frota-tls-enrollment-fleet-osctrl-zentral]] — Veja também: osquery Gerenciamento Centralizado de Frota (`TLS Enrollment`, `Fleet`, `osctrl` e `Zentral`): distribuição remota de configuração e Live Queries.
- [[osquery-extensoes-thrift-sdk-go-python-logger-plugins-aws-kinesis-kafka]] — Veja também: osquery Extensions (`Thrift` API) e Logger Plugins (`filesystem`, `syslog`, `aws_kinesis`, `aws_firehose`, `kafka_producer`).

## Fontes
- [osquery GitHub — README.md (SQL-Powered OS Instrumentation, Interactive Shell osqueryi, Daemon osqueryd, Fleet Managers & Thrift Extensions)](https://osquery.readthedocs.io/en/stable/introduction/using-osqueryd/) — README oficial do osquery/osquery apresentando a arquitetura de tabelas virtuais SQLite multiplataforma, gerenciadores de frota TLS (Fleet, osctrl, Zentral) e extensões; consultado em 2026-10-03.
- [osquery Official Documentation — Using osqueryd (Configuration, Schedule, Differential vs Snapshot Logs, Query Packs, Discovery Queries & Watchdog)](https://raw.githubusercontent.com/osquery/osquery/master/README.md) — Documentação oficial de operação do daemon osqueryd detalhando o agendamento de queries, logs diferenciais no RocksDB, Query Packs, FIM e proteção de recursos via Watchdog; consultado em 2026-10-03.
- [osquery — Official GitHub Repository (Linux Foundation)](https://github.com/osquery/osquery) — Repositório oficial open-source do osquery; consultado em 2026-10-03.
