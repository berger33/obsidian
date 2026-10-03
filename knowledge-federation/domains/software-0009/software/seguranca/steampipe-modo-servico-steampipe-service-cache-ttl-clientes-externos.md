---
id: software.seguranca.tranche10.000908
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

# Steampipe **`steampipe service`**: Operação como Daemon PostgreSQL (`:9193`), Controle de **Cache TTL (`--cache-ttl`)** e Conexão via `psql` / Grafana / Metabase

## Em uma frase
Em vez de subir e derrubar a instância embutida do Postgres a cada execução de `steampipe query`, o subcomando **`steampipe service start`** inicia o banco de dados PostgreSQL do Steampipe em background (escutando por padrão em `127.0.0.1:9193`, usuário `steampipe`)!

## Por que importa
Com o `steampipe service` rodando, dois recursos corporativos entram em cena: **(1) Cache Inteligente de Resultados (`--cache` / `--cache-ttl <segundos>`, padrão `300s`)**, que evita bater repetidamente nas APIs da AWS/GCP e estourar limites de *Rate Limiting* quando um dashboard ou analista roda várias queries sobre as mesmas tabelas; e **(2) Conexão Direta de Qualquer Cliente PostgreSQL Externo** (`psql`, **DBeaver**, **Grafana**, **Metabase**, **Superset** ou scripts Python `psycopg`)!

## Como funciona
Para exibir a string de conexão e a senha gerada para a instância local, basta executar **`steampipe service status --show-password`**!

## Exemplo
```bash
# Iniciar o servico background do Steampipe com cache TTL de 15 minutos (900s) e inspecionar a string de conexao Postgres
steampipe service start --cache-ttl 900
steampipe service status --show-password
```

## Limites e trade-offs
Atenção de segurança ao usar a flag **`--database-listen network`** (que faz o Postgres do Steampipe escutar em `0.0.0.0:9193` em vez de apenas `localhost`): qualquer pessoa que consiga conectar na porta `9193` poderá consultar todas as credenciais de nuvem configuradas nos arquivos `.spc` do servidor! Mantenha o listener restrito a `local` (`127.0.0.1`) ou proteja-o com firewall/TLS e autenticação forte.

## Como verificar
Limpe o cache em memória quando quiser forçar uma leitura fresca das APIs após aplicar uma correção executando `.cache clear` no shell interativo.

## Conexões
- [[steampipe-auditoria-postura-github-supply-chain-branch-protection-actions]] — Veja também: Steampipe Plugin **`github`**: Auditoria SQL de **Supply Chain, Repositórios Públicos, Branch Protection, Segredos e GitHub Actions**.
- [[steampipe-snapshots-exportacao-relatorios-html-json-md-cicd]] — Veja também: Steampipe & Powerpipe em **CI/CD**: Snapshots Históricos (**`.pps`**, `--snapshot`), Exportação (`json`, `html`, `md`, `csv`, `asff`) e Exit Codes.
- [[steampipe-arquitetura-zero-etl-postgres-fdw-plugins-sql-cloud]] — Referência cruzada direta com steampipe-arquitetura-zero-etl-postgres-fdw-plugins-sql-cloud.
- [[cloudquery-arquitetura-elt-apache-arrow-inventario-ativos-cspm]] — Referência cruzada direta com cloudquery-arquitetura-elt-apache-arrow-inventario-ativos-cspm.

## Fontes
- [Turbot Steampipe Official GitHub — Zero-ETL SQL Engine & PostgreSQL FDW Architecture](https://raw.githubusercontent.com/turbot/steampipe/main/README.md) — repositório oficial do Steampipe cobrindo arquitetura Zero-ETL sobre PostgreSQL FDW, plugins multi-cloud e distribuições SQLite/Postgres; consultado em 2026-10-03.
- [Turbot Powerpipe Official GitHub — Dashboards & 5,000+ Compliance Benchmarks as Code in HCL](https://raw.githubusercontent.com/turbot/powerpipe/main/README.md) — repositório oficial do Powerpipe cobrindo execução de benchmarks CIS/NIST/PCI/SOC2/HIPAA e controles customizados em HCL; consultado em 2026-10-03.
- [Steampipe Official CLI & Exit Codes Reference Documentation](https://steampipe.io/docs/reference/cli/overview) — documentação oficial de subcomandos CLI (`query`, `service`, `plugin`), flags globais e códigos de saída do Steampipe; consultado em 2026-10-03.
