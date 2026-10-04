---
id: software.devops.tranche08.000757
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

# Redgate Flyway: migrações escritas em Java (BaseJavaMigration), substituição de Placeholders e Callbacks

## Em uma frase
Além de scripts SQL puros, o Flyway suporta migrações escritas em Java (`BaseJavaMigration`) para transformações programáticas complexas de dados, substituição dinâmica de variáveis (`${placeholder}`) nos scripts SQL e Callbacks atrelados a eventos do ciclo de vida.

## Por que importa
Certas migrações de dados exigem ler linhas existentes, descriptografar valores, validar estruturas JSON complexas ou calcular hashes que não são possíveis ou viáveis apenas em SQL puro; além disso, scripts SQL frequentemente precisam parametrizar nomes de tabelas, schemas ou roles por ambiente. O README oficial do Flyway destaca que as migrações podem ser escritas em **SQL ou Java**.

## Como funciona
(1) **Java-based migrations**: classes Java que estendem `BaseJavaMigration` (nomeadas como `V3__Anonymize_customer_emails.java`) recebem o objeto `Context` contendo a `Connection` JDBC ativa dentro da transação da migração, permitindo executar lógica Java arbitrária na ordem exata da versão `V3`; (2) **Placeholders**: o Flyway substitui expressões `${meu_placeholder}` dentro dos arquivos `.sql` pelos valores passados via `-placeholders.meu_placeholder=valor` ou variáveis de ambiente `FLYWAY_PLACEHOLDERS_*` (calculando o checksum sobre o script original antes da substituição ou conforme configurado); e (3) **Callbacks**: scripts SQL ou classes Java nomeados com nomes de eventos do ciclo de vida (como `beforeMigrate.sql`, `afterMigrate.sql` ou `afterEachMigrate.sql`) que rodam automaticamente nos ganchos correspondentes.

## Exemplo
```bash
# Executar flyway migrate injetando placeholders para parametrizar o ambiente dentro dos scripts SQL
flyway -url="jdbc:postgresql://localhost:5432/appdb" \
  -user="postgres" \
  -placeholders.app_readonly_role="bi_reader_prod" \
  migrate
```

## Limites e trade-offs
Migrações escritas em Java (`BaseJavaMigration`) nunca devem instanciar nem usar entidades JPA/Hibernate da aplicação atual para ler ou gravar no banco, pois o modelo de classes Java da aplicação daqui a dois anos terá novas colunas que ainda não existiam na época da migração `V3`, quebrando a execução da `V3` em um banco novo; dentro de `BaseJavaMigration`, use exclusivamente SQL direto via `JdbcTemplate` ou `PreparedStatement` na `context.getConnection()`.

## Como verificar
Teste suas migrações Java e SQL com placeholders executando o ciclo completo do `V1` até a versão atual contra um container de banco de dados limpo em CI.

## Conexões
- [[flyway-comandos-ciclo-vida-info-validate-migrate-baseline-repair]] — Veja também: Redgate Flyway: comandos fundamentais do ciclo de vida (migrate, info, validate, baseline, repair e clean).
- [[flyway-configuracao-toml-conf-variaveis-ambiente-precedencia]] — Veja também: Redgate Flyway: configuração declarativa (flyway.toml e flyway.conf), variáveis FLYWAY_* e precedência.
- [[flyway-migracoes-banco-dados-schema-history-versionamento]] — Referência cruzada direta com flyway-migracoes-banco-dados-schema-history-versionamento.
- [[flyway-modos-execucao-cli-docker-java-api-maven-gradle]] — Referência cruzada direta com flyway-modos-execucao-cli-docker-java-api-maven-gradle.

## Fontes
- [Redgate Flyway GitHub — README.md (How Flyway Works, 5 Execution Modes, Schema Model & 50+ Supported Databases)](https://raw.githubusercontent.com/flyway/flyway/main/README.md) — README oficial do Flyway (Apache-2.0) explicando o funcionamento da tabela flyway_schema_history, migrações SQL e Java, captura de schema model em disco e matriz de mais de 50 bancos suportados; consultado em 2026-10-03.
- [Redgate Flyway Official Documentation — Getting Started with Flyway](https://documentation.red-gate.com/flyway/getting-started-with-flyway) — Documentação oficial da Redgate para configuração, convenções de nomenclatura (V, R, U) e comandos de ciclo de vida do Flyway; consultado em 2026-10-03.
- [Redgate Flyway — Official GitHub Repository](https://github.com/flyway/flyway) — Repositório oficial Apache-2.0 do Redgate Flyway; consultado em 2026-10-03.
