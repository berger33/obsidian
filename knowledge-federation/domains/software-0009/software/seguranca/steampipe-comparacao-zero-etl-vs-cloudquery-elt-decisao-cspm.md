---
id: software.seguranca.tranche10.000910
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/turbot/steampipe/main/README.md", "https://raw.githubusercontent.com/turbot/powerpipe/main/README.md", "https://steampipe.io/docs/reference/cli/overview"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Decisão Arquitetural de CSPM: Quando Usar **Steampipe (Zero-ETL Live SQL)** vs **CloudQuery (ELT Data Warehouse)** vs **Prowler**

## Em uma frase
Na construção de uma plataforma moderna de **Cloud Security Posture Management (CSPM)** e inventário de ativos, engenheiros de segurança frequentemente se perguntam quando usar **Steampipe**, quando usar **CloudQuery** e quando usar **Prowler**.

## Por que importa
Compare os três paradigmas arquiteturais: **(1) Steampipe (`turbot/steampipe`) — *Zero-ETL Live Query***: traduz queries SQL em chamadas de API **em tempo real sob demanda**, sem precisar manter um banco de dados externo nem sincronizar gigabytes de dados antes de fazer uma pergunta — imbatível para **investigação ad-hoc, resposta a incidentes ao vivo, ambientes de até dezenas de contas e execução rápida com Powerpipe**; **(2) CloudQuery (`cloudquery/cloudquery`) — *ELT para Data Warehouse***: extrai e sincroniza todo o inventário da nuvem em lote via Apache Arrow para **PostgreSQL, BigQuery, Snowflake, ClickHouse ou DuckDB** — imbatível quando você tem **centenas de contas com milhões de recursos, precisa de histórico temporal de meses/anos e quer cruzar ativos com logs do SIEM no mesmo Data Warehouse**; e **(3) Prowler**: scanner especializado com centenas de checagens prontas e remediações detalhadas por provedor!

## Como funciona
E o melhor: como o **Powerpipe** suporta conectar tanto no Steampipe quanto em um PostgreSQL/DuckDB populado pelo CloudQuery, você pode combinar ambos!

## Exemplo
```bash
# Exemplo de consulta rapida Zero-ETL no Steampipe via CLI exportando JSON para correlacao imediata com o inventario
steampipe query --output json \
  "SELECT name, account_id, region, versioning_enabled, mfa_delete FROM aws_s3_bucket WHERE NOT versioning_enabled;" \
  > /cases/cspm/unversioned_buckets_live.json
```

## Limites e trade-offs
Em resumo: use **Steampipe** para consultas interativas em tempo real e validação imediata pós-correção, e use **CloudQuery** para armazenar séries históricas de longo prazo do inventário multi-cloud no seu Data Warehouse!

## Como verificar
Valide o tempo de resposta de suas queries mais frequentes no Steampipe com `.timing on`.

## Conexões
- [[steampipe-snapshots-exportacao-relatorios-html-json-md-cicd]] — Veja também: Steampipe & Powerpipe em **CI/CD**: Snapshots Históricos (**`.pps`**, `--snapshot`), Exportação (`json`, `html`, `md`, `csv`, `asff`) e Exit Codes.
- [[steampipe-arquitetura-zero-etl-postgres-fdw-plugins-sql-cloud]] — Referência cruzada direta com steampipe-arquitetura-zero-etl-postgres-fdw-plugins-sql-cloud.
- [[cloudquery-arquitetura-elt-apache-arrow-inventario-ativos-cspm]] — Referência cruzada direta com cloudquery-arquitetura-elt-apache-arrow-inventario-ativos-cspm.

## Fontes
- [Turbot Steampipe Official GitHub — Zero-ETL SQL Engine & PostgreSQL FDW Architecture](https://raw.githubusercontent.com/turbot/steampipe/main/README.md) — repositório oficial do Steampipe cobrindo arquitetura Zero-ETL sobre PostgreSQL FDW, plugins multi-cloud e distribuições SQLite/Postgres; consultado em 2026-10-03.
- [Turbot Powerpipe Official GitHub — Dashboards & 5,000+ Compliance Benchmarks as Code in HCL](https://raw.githubusercontent.com/turbot/powerpipe/main/README.md) — repositório oficial do Powerpipe cobrindo execução de benchmarks CIS/NIST/PCI/SOC2/HIPAA e controles customizados em HCL; consultado em 2026-10-03.
- [Steampipe Official CLI & Exit Codes Reference Documentation](https://steampipe.io/docs/reference/cli/overview) — documentação oficial de subcomandos CLI (`query`, `service`, `plugin`), flags globais e códigos de saída do Steampipe; consultado em 2026-10-03.
