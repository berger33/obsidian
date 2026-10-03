---
id: software.devops.tranche08.000747
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
fontes: ["https://raw.githubusercontent.com/liquibase/liquibase/master/README.md", "https://raw.githubusercontent.com/liquibase/liquibase/main/docker/README.md", "https://github.com/liquibase/liquibase"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Liquibase: formatos de Changelog (SQL, XML, YAML, JSON), ordenação de Changesets e Checksums

## Em uma frase
O Liquibase suporta changelogs escritos em SQL, XML, YAML ou JSON (como demonstrado nos diretórios `examples/sql` e `examples/xml` da distribuição), rastreando cada `changeset` individualmente por `id`, `author`, caminho do arquivo e hash MD5/checksum na tabela `DATABASECHANGELOG`.

## Por que importa
Algumas equipes de engenharia preferem escrever DDL diretamente em SQL puro para aproveitar recursos específicos do SGBD, enquanto outras preferem formatos abstratos (XML, YAML, JSON) que geram o SQL adequado para múltiplos bancos e oferecem geração automática de comandos de rollback para operações comuns. O README oficial do Liquibase destaca o uso de `examples/sql` e `examples/xml` no guia prático.

## Como funciona
Independentemente do formato escolhido (SQL formatado com comentários `--liquibase formatted sql` e `--changeset autor:id`, ou estruturas XML/YAML/JSON), o Liquibase lê a lista ordenada de changesets declarados no changelog mestre (que pode incluir diretórios ou sub-arquivos com `include`/`includeAll`). Para cada changeset, o Liquibase calcula um checksum sobre seu conteúdo normalizado: se o par `(id, author, filename)` ainda não consta na tabela `DATABASECHANGELOG`, o changeset é executado dentro de uma transação (sempre que o banco suportar DDL transacional) e registrado; se já consta na tabela, o Liquibase compara o checksum atual com o gravado no banco e aborta com erro de validação caso um changeset já aplicado tenha sido modificado retroativamente.

## Exemplo
```sql
--liquibase formatted sql

--changeset devops:001-create-orders-table
CREATE TABLE orders (
    id BIGINT PRIMARY KEY,
    customer_id BIGINT NOT NULL,
    status VARCHAR(32) NOT NULL
);
--rollback DROP TABLE orders;
```

## Limites e trade-offs
Nunca edite o conteúdo SQL de um `changeset` que já foi aplicado em ambientes compartilhados ou produção, pois a divergência de checksum na tabela `DATABASECHANGELOG` bloqueará os próximos deploys (`Validation Failed: change sets check sum`); para alterar uma tabela existente, adicione sempre um novo `changeset` sequencial ao final do changelog (modelo append-only).

## Como verificar
Execute `liquibase validate` e `liquibase update-sql` (que imprime no terminal o SQL exato que seria executado sem alterar o banco) para revisar os changesets antes de aplicar `liquibase update`.

## Conexões
- [[liquibase-integracoes-maven-gradle-spring-boot-cicd]] — Veja também: Liquibase: automação e integrações com Maven, Gradle, Ant, Spring Boot, GitHub Actions e Spinnaker.
- [[liquibase-estrategias-rollback-reversao-segura-mudancas]] — Veja também: Liquibase: estratégias de reversão de esquema (rollback por tag, contagem ou data) e validação prévia.
- [[liquibase-gerenciamento-mudancas-esquema-banco-dados]] — Referência cruzada direta com liquibase-gerenciamento-mudancas-esquema-banco-dados.
- [[flyway-migracoes-banco-dados-schema-history-versionamento]] — Referência cruzada direta com flyway-migracoes-banco-dados-schema-history-versionamento.

## Fontes
- [Liquibase GitHub — README.md (Database Schema Change Management, Quarterly Releases & CI/CD Integrations)](https://raw.githubusercontent.com/liquibase/liquibase/master/README.md) — README oficial do Liquibase cobrindo rastreamento e rollback de mudanças de banco de dados, fluxo com H2, cadência de releases trimestrais/nightly e gate de aprovação Sonatype; consultado em 2026-10-03.
- [Liquibase Docker Documentation — docker/README.md (Liquibase 5.0 FSL vs Secure, LPM Drivers & Migration Guide)](https://raw.githubusercontent.com/liquibase/liquibase/main/docker/README.md) — Documentação oficial de imagens Docker do Liquibase detalhando o licenciamento 5.0+ (Community FSL vs Secure), remoção de drivers embutidos por padrão, uso do Liquibase Package Manager (lpm add --global) e roteiro de migração de 6 etapas; consultado em 2026-10-03.
- [Liquibase — Official GitHub Repository](https://github.com/liquibase/liquibase) — Repositório oficial do Liquibase; consultado em 2026-10-03.
