---
id: software.seguranca.tranche07.000697
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-07.md"
fontes: ["https://quay.github.io/clair/whatis.html", "https://raw.githubusercontent.com/quay/clair/main/README.md", "https://quay.github.io/claircore/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Clair v4: Modos de Implantação (`combo` vs Microsserviços `indexer`/`matcher`/`notifier`), Dimensionamento de PostgreSQL e Coordenação via `clair-lock`

## Em uma frase
O binário do Clair v4 (`clair -conf /etc/clair/config.yaml -mode <modo>`) pode ser iniciado em quatro modos operacionais definidos pela flag **`-mode`** (ou variável `CLAIR_MODE`): **`combo`** (roda `Indexer`, `Matcher` e `Notifier` dentro do mesmo processo Go), **`indexer`**, **`matcher`** e **`notifier`**.

## Por que importa
Para ambientes pequenos ou de homologação, o modo `-mode combo` simplifica a operação em um único Deployment; já em registros corporativos de grande porte (como um cluster Red Hat Quay atendendo milhares de builds por hora), separar em três Deployments Kubernetes distintos com três bancos de dados PostgreSQL lógicos dedicados (`indexer_db`, `matcher_db`, `notifier_db`) evita que um pico de indexação de camadas afete a latência de consultas de vulnerabilidades.

## Como funciona
Todas as réplicas do Clair v4 coordenam tarefas concorrentes (como garantir que duas réplicas do `Matcher` não rodem o mesmo Updater ao mesmo tempo, ou que duas réplicas do `Indexer` não indexem o mesmo manifesto simultaneamente) usando **PostgreSQL Advisory Locks** nativos sem precisar de Redis ou ZooKeeper externo!

## Exemplo
```yaml
# Exemplo de configuracao de banco de dados com TLS obrigatorio e pool de conexoes no config.yaml do Clair v4
http_listen_addr: "0.0.0.0:6060"
introspection_addr: "0.0.0.0:8089"
log_level: "info"
indexer:
  connstring: "host=pg-clair.internal.corp port=5432 dbname=clair_indexer user=clair_idx sslmode=verify-full"
  scanlock_retry: 10
  layer_scan_concurrency: 5
  migrations: true
```

## Limites e trade-offs
Se você usar um pooler de conexões como o *PgBouncer* na frente do PostgreSQL do Clair v4, configure-o obrigatoriamente em **`pool_mode = session`** (e **nunca** `transaction`), pois o Clair v4 depende de *PostgreSQL Session-Level Advisory Locks* para coordenar os workers e updaters!

## Como verificar
Verifique no endpoint de métricas Prometheus (`http://127.0.0.1:8089/metrics`) a ausência de erros de lock ou exaustão de conexões SQL.

## Conexões
- [[clair-cli-clairctl-client-submissao-manifestos-exportacao-offline]] — Veja também: Clair v4 (`clairctl`): Operação via Linha de Comando (`clairctl report`, `export-updaters` / `import-updaters`) para CI/CD e Ambientes *Air-Gapped*.
- [[clair-autenticacao-seguranca-api-psk-jwt-tls-introspeccao]] — Veja também: Clair v4: Hardening da API — Autenticação **JWT com Pre-Shared Key (`auth.psk`)**, TLS Mútuo e Isolamento da Porta de Introspecção.
- [[clair-arquitetura-analise-estatica-containers-claircore-indexer-matcher-notifier]] — Referência cruzada direta com clair-arquitetura-analise-estatica-containers-claircore-indexer-matcher-notifier.
- [[clair-integracao-project-quay-harbor-admission-controllers-vex]] — Referência cruzada direta com clair-integracao-project-quay-harbor-admission-controllers-vex.

## Fontes
- [Project Quay Clair v4 Official Documentation — What is ClairV4 & Architecture](https://quay.github.io/clair/whatis.html) — documentação oficial do Clair v4 cobrindo a separação ClairCore, Indexer (IndexReport), Matcher (VulnerabilityReport) e Notifier; consultado em 2026-10-03.
- [Project Quay Clair Official GitHub — Container Vulnerability Static Analysis](https://raw.githubusercontent.com/quay/clair/main/README.md) — repositório oficial do projeto Clair v4 e utilitário de linha de comando clairctl; consultado em 2026-10-03.
- [ClairCore Official Documentation — Layer Indexing & Vulnerability Matching Engine](https://quay.github.io/claircore/) — documentação oficial da biblioteca ClairCore para extração de pacotes de SO/linguagens e updaters de vulnerabilidades; consultado em 2026-10-03.
