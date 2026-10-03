---
id: software.devops.tranche08.000755
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

# Redgate Flyway: convenção de nomenclatura de migrações Versionadas (V), Repetíveis (R) e Undo (U)

## Em uma frase
Seguindo o princípio de convenção sobre configuração, o Flyway classifica e ordena automaticamente os arquivos SQL pelo prefixo do nome: `V<versão>__<descrição>.sql` (Versioned), `R__<descrição>.sql` (Repeatable) e `U<versão>__<descrição>.sql` (Undo).

## Por que importa
Em ferramentas que exigem manter um arquivo manifesto XML ou YAML central listando manualmente a ordem de todos os scripts SQL, duas branches criadas em paralelo sempre geram conflito de merge na última linha do manifesto central. No Flyway, basta adicionar o arquivo `.sql` no diretório seguindo a convenção de prefixo, sem tocar em nenhum manifesto central.

## Como funciona
Ao escanear os diretórios configurados em `locations`, o Flyway identifica o tipo de cada migração pelo padrão `<Prefixo><Versão>__<Descrição>.sql` (com dois sublinhados `__` separando a versão da descrição): (1) **Migrações Versionadas (`V`)**: ex.: `V1__Create_person_table.sql`, `V2.1__Add_email_column.sql` — são aplicadas **exatamente uma única vez** em ordem crescente de versão para evoluir estruturas (`CREATE`/`ALTER`/`DROP` e migração de dados); (2) **Migrações Repetíveis (`R`)**: ex.: `R__Active_users_view.sql` — não possuem número de versão e são **reaplicadas automaticamente toda vez que seu checksum muda**, sendo ideais para manter `CREATE OR REPLACE VIEW`, functions e procedures; e (3) **Migrações Undo (`U`)**: definem o script inverso para desfazer uma migração versionada de mesmo número.

## Exemplo
```bash
# Exemplo de arquivos em sql/ seguindo a convenção oficial de dois sublinhados (__) para V e R
ls -1 sql/
# V1__Create_person_table.sql
# V2__Add_people.sql
# R__Create_person_summary_view.sql
```

## Limites e trade-offs
Um erro clássico de iniciantes no Flyway é usar apenas **um** sublinhado (`V1_init.sql`) em vez de **dois** sublinhados (`V1__init.sql`): o Flyway ignora ou rejeita arquivos que não seguem o separador padrão `__`; além disso, migrações repetíveis (`R__*.sql`) sempre são executadas **depois** de todas as migrações versionadas pendentes (`V`), portanto uma migração versionada nunca deve depender de uma view criada apenas em uma migração repetível.

## Como verificar
Execute `flyway info` e verifique nas colunas `Category` (`Versioned` vs `Repeatable`), `Version` e `Description` que todos os arquivos do diretório `sql/` foram reconhecidos na ordem esperada.

## Conexões
- [[flyway-captura-estado-schema-model-disco-diff]] — Veja também: Redgate Flyway: captura de estado do esquema em disco (schema model) além de scripts de migração.
- [[flyway-comandos-ciclo-vida-info-validate-migrate-baseline-repair]] — Veja também: Redgate Flyway: comandos fundamentais do ciclo de vida (migrate, info, validate, baseline, repair e clean).
- [[flyway-migracoes-banco-dados-schema-history-versionamento]] — Referência cruzada direta com flyway-migracoes-banco-dados-schema-history-versionamento.
- [[liquibase-formatos-changelog-sql-xml-yaml-json-changesets]] — Referência cruzada direta com liquibase-formatos-changelog-sql-xml-yaml-json-changesets.

## Fontes
- [Redgate Flyway GitHub — README.md (How Flyway Works, 5 Execution Modes, Schema Model & 50+ Supported Databases)](https://raw.githubusercontent.com/flyway/flyway/main/README.md) — README oficial do Flyway (Apache-2.0) explicando o funcionamento da tabela flyway_schema_history, migrações SQL e Java, captura de schema model em disco e matriz de mais de 50 bancos suportados; consultado em 2026-10-03.
- [Redgate Flyway Official Documentation — Getting Started with Flyway](https://documentation.red-gate.com/flyway/getting-started-with-flyway) — Documentação oficial da Redgate para configuração, convenções de nomenclatura (V, R, U) e comandos de ciclo de vida do Flyway; consultado em 2026-10-03.
- [Redgate Flyway — Official GitHub Repository](https://github.com/flyway/flyway) — Repositório oficial Apache-2.0 do Redgate Flyway; consultado em 2026-10-03.
