---
id: software.devops.tranche08.000752
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

# Redgate Flyway: 5 formas de execução (Command-line, Docker, Java API, Maven e Gradle)

## Em uma frase
O Flyway pode ser executado de cinco maneiras oficiais documentadas no README: utilitário de linha de comando (`CLI`), imagem oficial Docker (`redgate/flyway`), Java API embutida na inicialização da aplicação, plugin Maven e plugin Gradle.

## Por que importa
Equipes poliglotas que escrevem microsserviços em Go, Python, Node.js ou C# não possuem Maven ou Gradle em seus projetos e precisam de uma CLI standalone ou imagem Docker leve para pipelines de CI/CD, enquanto equipes Java/Spring/Quarkus/Micronaut frequentemente preferem acionar o Flyway via Java API programática ou plugins de build. A seção `How can you run Flyway?` do README oficial cobre todas as cinco modalidades.

## Como funciona
(1) **Command-line**: pacote autocontido para Windows, macOS e Linux voltado para usuários não-Java e pipelines sem necessidade de instalar JDK separado; (2) **Docker**: imagem oficial no Docker Hub (`redgate/flyway`) pronta para jobs de CI/CD e Kubernetes; (3) **Java API**: biblioteca (`flyway-core`) invocada programaticamente em Java (`Flyway.configure().dataSource(...).load().migrate()`) para migrar o banco na inicialização da aplicação; (4) **Maven plugin**: integração com ciclos de build Maven (`mvn flyway:migrate`, `mvn flyway:info`); e (5) **Gradle plugin**: tarefas Gradle (`gradle flywayMigrate`, `gradle flywayValidate`).

## Exemplo
```bash
# Executar o Flyway via imagem oficial Docker montando o diretório local de scripts SQL em /flyway/sql
docker run --rm \
  -v $(pwd)/sql:/flyway/sql \
  redgate/flyway:latest \
  -url=jdbc:postgresql://host.docker.internal:5432/appdb \
  -user=postgres -password=secret \
  migrate
```

## Limites e trade-offs
Ao usar a **Java API** para rodar `flyway.migrate()` automaticamente no boot de cada réplica de um microsserviço em Kubernetes, embora o Flyway utilize locking no banco de dados para evitar que duas réplicas executem a mesma migração ao mesmo tempo, uma migração demorada atrasará a prontidão (`readinessProbe`) de todos os pods; em implantações de larga escala, executar a imagem Docker `redgate/flyway` em um step de CI/CD anterior ao deploy separa o ciclo de esquema do ciclo de réplicas.

## Como verificar
Execute `docker run --rm redgate/flyway -v` (ou `flyway -v` na CLI) para verificar a versão da ferramenta e confirme a leitura do diretório `/flyway/sql` com o comando `info`.

## Conexões
- [[flyway-migracoes-banco-dados-schema-history-versionamento]] — Veja também: Redgate Flyway: controle de versão para bancos de dados baseado em migrações e tabela flyway_schema_history.
- [[flyway-bancos-suportados-relacionais-cloud-data-warehouses]] — Veja também: Redgate Flyway: ecossistema de mais de 50 bancos de dados relacionais, distribuídos e data warehouses suportados.
- [[liquibase-integracoes-maven-gradle-spring-boot-cicd]] — Referência cruzada direta com liquibase-integracoes-maven-gradle-spring-boot-cicd.

## Fontes
- [Redgate Flyway GitHub — README.md (How Flyway Works, 5 Execution Modes, Schema Model & 50+ Supported Databases)](https://raw.githubusercontent.com/flyway/flyway/main/README.md) — README oficial do Flyway (Apache-2.0) explicando o funcionamento da tabela flyway_schema_history, migrações SQL e Java, captura de schema model em disco e matriz de mais de 50 bancos suportados; consultado em 2026-10-03.
- [Redgate Flyway Official Documentation — Getting Started with Flyway](https://documentation.red-gate.com/flyway/getting-started-with-flyway) — Documentação oficial da Redgate para configuração, convenções de nomenclatura (V, R, U) e comandos de ciclo de vida do Flyway; consultado em 2026-10-03.
- [Redgate Flyway — Official GitHub Repository](https://github.com/flyway/flyway) — Repositório oficial Apache-2.0 do Redgate Flyway; consultado em 2026-10-03.
