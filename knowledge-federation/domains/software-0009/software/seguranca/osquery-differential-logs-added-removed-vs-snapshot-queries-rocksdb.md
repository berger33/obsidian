---
id: software.seguranca.tranche02.000183
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

# osquery Logs Diferenciais (`added` / `removed` via RocksDB) vs `snapshot: true`: como o `osqueryd` detecta mudanças de estado sem inundar o SIEM

## Em uma frase
Conforme explicado na documentação oficial do `osqueryd` (`osquery.readthedocs.io/en/stable/introduction/using-osqueryd/`), o comportamento padrão de uma query agendada no `schedule` é gerar **Logs Diferenciais (*Differential Logs*)**: na primeira execução, o `osqueryd` armazena o resultado no banco embarcado **RocksDB** local; nas execuções seguintes (a cada `interval` segundos), ele compara o resultado novo com o anterior e **só emite log se uma linha foi adicionada (`"action": "added"`) ou removida (`"action": "removed"`)**!

## Por que importa
Se 10.000 servidores enviassem a lista completa de todos os 200 processos e 50 módulos de kernel a cada 60 segundos para o SIEM, o volume de rede e indexação seria proibitivo; com logs diferenciais, se nada mudou no host, **zero bytes são logados**.

## Como funciona
Quando você realmente precisa do retrato completo do estado atual (por exemplo, um inventário diário de pacotes instalados a cada 86.400s), basta adicionar **`"snapshot": true`** na definição da query: ela emitirá um evento `"action": "snapshot"` com todas as linhas atuais sem calcular diff.

## Exemplo
```json
{
  "schedule": {
    "kernel_modules_diff": {
      "query": "SELECT name, size, status FROM kernel_modules;",
      "interval": 300,
      "description": "Emite alerta diferencial (added/removed) apenas quando um módulo de kernel muda."
    },
    "daily_installed_packages_snapshot": {
      "query": "SELECT name, version, arch FROM deb_packages;",
      "interval": 86400,
      "snapshot": true
    }
  }
}
```

## Limites e trade-offs
Evite incluir colunas altamente voláteis que mudam a cada segundo (como `system_time`, `resident_size` ou tempo de CPU) em queries diferenciais normais, pois isso faria toda linha parecer "removida e adicionada" em todo ciclo!

## Como verificar
Valide o arquivo de configuração executando `osqueryd --config_path /etc/osquery/osquery.conf --config_check`.

## Conexões
- [[osquery-osqueryi-vs-osqueryd-shell-interativo-daemon-agendamento]] — Veja também: osquery `osqueryi` vs `osqueryd`: exploração interativa ad-hoc versus monitoramento contínuo agendado por daemon.
- [[osquery-query-packs-organizacao-modular-discovery-queries-platform-version]] — Veja também: osquery `Query Packs`: agrupamento modular de queries de detecção com filtros `platform`, `version`, `shard` e `discovery`.

## Fontes
- [osquery GitHub — README.md (SQL-Powered OS Instrumentation, Interactive Shell osqueryi, Daemon osqueryd, Fleet Managers & Thrift Extensions)](https://osquery.readthedocs.io/en/stable/introduction/using-osqueryd/) — README oficial do osquery/osquery apresentando a arquitetura de tabelas virtuais SQLite multiplataforma, gerenciadores de frota TLS (Fleet, osctrl, Zentral) e extensões; consultado em 2026-10-03.
- [osquery Official Documentation — Using osqueryd (Configuration, Schedule, Differential vs Snapshot Logs, Query Packs, Discovery Queries & Watchdog)](https://raw.githubusercontent.com/osquery/osquery/master/README.md) — Documentação oficial de operação do daemon osqueryd detalhando o agendamento de queries, logs diferenciais no RocksDB, Query Packs, FIM e proteção de recursos via Watchdog; consultado em 2026-10-03.
- [osquery — Official GitHub Repository (Linux Foundation)](https://github.com/osquery/osquery) — Repositório oficial open-source do osquery; consultado em 2026-10-03.
