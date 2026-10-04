---
id: software.devops.tranche08.000746
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

# Liquibase: automação e integrações com Maven, Gradle, Ant, Spring Boot, GitHub Actions e Spinnaker

## Em uma frase
O Liquibase integra-se nativamente a ferramentas de build Java (Maven, Gradle, Ant), frameworks de aplicação (Spring Boot) e orquestradores de CI/CD (GitHub Actions, Spinnaker e workflows customizados), além de suportar extensões gratuitas para bancos adicionais.

## Por que importa
Diferentes arquiteturas de software aplicam migrações de banco em momentos distintos: monolitos e microsserviços Spring Boot menores às vezes executam migrações na inicialização da aplicação ou no build Maven/Gradle, enquanto arquiteturas Kubernetes de alta escala executam o Liquibase como um estágio dedicado de CI/CD no GitHub Actions ou Spinnaker antes do deploy dos pods. A seção `Liquibase Automation and Integrations` do README oficial documenta essas opções.

## Como funciona
Quando integrado via **Maven** (`liquibase-maven-plugin`), **Gradle** ou **Ant**, metas como `liquibase:update`, `liquibase:status` e `liquibase:rollback` fazem parte do ciclo de build do projeto. No **Spring Boot**, a presença da dependência `liquibase-core` no classpath aciona automaticamente a avaliação do changelog configurado em `spring.liquibase.change-log` durante o boot do contexto Spring. Em pipelines de entrega contínua, o Liquibase fornece exemplos e plugins oficiais para **GitHub Actions** (`liquibase/liquibase-github-action-example`) e **Spinnaker** (`liquibase/liquibase-spinnaker-plugin`). Para bancos de dados que não fazem parte do núcleo embutido do Liquibase Community, extensões gratuitas podem ser baixadas do diretório oficial de extensões.

## Exemplo
```xml
<!-- Exemplo de declaração de dependência do Liquibase Core no Maven Central -->
<dependency>
    <groupId>org.liquibase</groupId>
    <artifactId>liquibase-core</artifactId>
    <version>5.0.3</version>
</dependency>
```

## Limites e trade-offs
Executar migrações automaticamente dentro da inicialização da aplicação (`Spring Boot` auto-configuration) quando um Deployment Kubernetes sobe 20 réplicas simultaneamente faz com que 20 pods disputem o lock na tabela `DATABASECHANGELOGLOCK` (e uma migração DDL demorada pode fazer o `livenessProbe`/`startupProbe` do Kubernetes matar o pod no meio da alteração de esquema); em produção Kubernetes, é mais seguro desativar a migração no boot da aplicação e executá-la em um step de CI/CD ou Kubernetes Job/initContainer controlado.

## Como verificar
Em projetos Maven/Gradle ou pipelines GitHub Actions, execute o objetivo de validação (`validate` / `status`) para confirmar que o plugin localiza o arquivo de changelog raiz e conecta ao banco alvo.

## Conexões
- [[liquibase-cadencia-releases-trimestrais-nightly-builds]] — Veja também: Liquibase: cadência de releases trimestrais da comunidade (Fev, Mai, Ago, Nov) e Nightly Builds da branch main.
- [[liquibase-formatos-changelog-sql-xml-yaml-json-changesets]] — Veja também: Liquibase: formatos de Changelog (SQL, XML, YAML, JSON), ordenação de Changesets e Checksums.
- [[liquibase-gerenciamento-mudancas-esquema-banco-dados]] — Referência cruzada direta com liquibase-gerenciamento-mudancas-esquema-banco-dados.
- [[liquibase-execucao-docker-variaveis-ambiente-registries]] — Referência cruzada direta com liquibase-execucao-docker-variaveis-ambiente-registries.

## Fontes
- [Liquibase GitHub — README.md (Database Schema Change Management, Quarterly Releases & CI/CD Integrations)](https://raw.githubusercontent.com/liquibase/liquibase/master/README.md) — README oficial do Liquibase cobrindo rastreamento e rollback de mudanças de banco de dados, fluxo com H2, cadência de releases trimestrais/nightly e gate de aprovação Sonatype; consultado em 2026-10-03.
- [Liquibase Docker Documentation — docker/README.md (Liquibase 5.0 FSL vs Secure, LPM Drivers & Migration Guide)](https://raw.githubusercontent.com/liquibase/liquibase/main/docker/README.md) — Documentação oficial de imagens Docker do Liquibase detalhando o licenciamento 5.0+ (Community FSL vs Secure), remoção de drivers embutidos por padrão, uso do Liquibase Package Manager (lpm add --global) e roteiro de migração de 6 etapas; consultado em 2026-10-03.
- [Liquibase — Official GitHub Repository](https://github.com/liquibase/liquibase) — Repositório oficial do Liquibase; consultado em 2026-10-03.
