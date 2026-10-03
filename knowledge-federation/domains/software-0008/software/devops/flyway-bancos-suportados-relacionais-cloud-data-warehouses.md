---
id: software.devops.tranche08.000753
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-08.md"
fontes: ["https://raw.githubusercontent.com/flyway/flyway/main/README.md", "https://documentation.red-gate.com/flyway/getting-started-with-flyway", "https://github.com/flyway/flyway"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Redgate Flyway: ecossistema de mais de 50 bancos de dados relacionais, distribuídos e data warehouses suportados

## Em uma frase
O Flyway suporta mais de 50 motores de bancos de dados, abrangendo SGBDs relacionais clássicos (PostgreSQL, MySQL, MariaDB, Oracle, SQL Server, DB2), bancos SQL distribuídos (CockroachDB, YugabyteDB, TiDB, Google Cloud Spanner) e plataformas analíticas/cloud (Snowflake, BigQuery, Redshift, Databricks, ClickHouse, DuckDB).

## Por que importa
Organizações modernas raramente possuem apenas um banco relacional: é comum operar PostgreSQL ou Aurora no transacional (OLTP), ClickHouse ou DuckDB em telemetria/analytics e Snowflake ou Google BigQuery no data warehouse corporativo; usar uma ferramenta de migração diferente para cada tecnologia fragmenta os pipelines de DevOps. A seção `Supported Databases` do README oficial do Flyway lista toda a matriz suportada.

## Como funciona
O motor do Flyway abstrai as particularidades de dialeto SQL, suporte a transações DDL, mecanismos de lock da tabela `flyway_schema_history` e parsers de scripts específicos para cada plataforma suportada (incluindo delimitadores de procedures PL/SQL no Oracle, `GO` no SQL Server, pacotes modulares como `flyway-database-postgresql`, `flyway-mysql`, `flyway-sqlserver`, `flyway-database-oracle` e conectores para MongoDB, Cassandra, Snowflake, BigQuery e Spanner). Assim, o mesmo fluxo de trabalho (`info`, `validate`, `migrate`) opera de maneira uniforme tanto em bancos transacionais quanto em data warehouses analíticos.

## Exemplo
```xml
<!-- No Flyway moderno (Maven), adicionar flyway-core junto ao módulo específico do banco (ex.: PostgreSQL) -->
<dependencies>
    <dependency>
        <groupId>org.flywaydb</groupId>
        <artifactId>flyway-core</artifactId>
    </dependency>
    <dependency>
        <groupId>org.flywaydb</groupId>
        <artifactId>flyway-database-postgresql</artifactId>
    </dependency>
</dependencies>
```

## Limites e trade-offs
Nem todos os bancos suportados pelo Flyway oferecem **DDL transacional** no próprio motor de banco de dados: enquanto o PostgreSQL, o SQL Server e o SQLite permitem fazer rollback automático de um `CREATE TABLE` ou `ALTER TABLE` caso o script falhe na metade, bancos como MySQL, MariaDB e Oracle executam commits implícitos em instruções DDL; nesses bancos sem DDL transacional, se uma migração com 5 instruções DDL falhar na 3ª instrução, a migração ficará com status de falha e exigirá limpeza manual das 2 primeiras estruturas antes de rodar `flyway repair`.

## Como verificar
Consulte a documentação de suporte do banco específico no portal do Flyway e verifique se o módulo correspondente (`flyway-database-*`) está presente no classpath ou diretório `drivers/` da CLI.

## Conexões
- [[flyway-modos-execucao-cli-docker-java-api-maven-gradle]] — Veja também: Redgate Flyway: 5 formas de execução (Command-line, Docker, Java API, Maven e Gradle).
- [[flyway-captura-estado-schema-model-disco-diff]] — Veja também: Redgate Flyway: captura de estado do esquema em disco (schema model) além de scripts de migração.
- [[flyway-migracoes-banco-dados-schema-history-versionamento]] — Referência cruzada direta com flyway-migracoes-banco-dados-schema-history-versionamento.
- [[atlasdb-schema-as-code-declarativo-versionado-multibanco]] — Referência cruzada direta com atlasdb-schema-as-code-declarativo-versionado-multibanco.

## Fontes
- [Redgate Flyway GitHub — README.md (How Flyway Works, 5 Execution Modes, Schema Model & 50+ Supported Databases)](https://raw.githubusercontent.com/flyway/flyway/main/README.md) — README oficial do Flyway (Apache-2.0) explicando o funcionamento da tabela flyway_schema_history, migrações SQL e Java, captura de schema model em disco e matriz de mais de 50 bancos suportados; consultado em 2026-10-03.
- [Redgate Flyway Official Documentation — Getting Started with Flyway](https://documentation.red-gate.com/flyway/getting-started-with-flyway) — Documentação oficial da Redgate para configuração, convenções de nomenclatura (V, R, U) e comandos de ciclo de vida do Flyway; consultado em 2026-10-03.
- [Redgate Flyway — Official GitHub Repository](https://github.com/flyway/flyway) — Repositório oficial Apache-2.0 do Redgate Flyway; consultado em 2026-10-03.
