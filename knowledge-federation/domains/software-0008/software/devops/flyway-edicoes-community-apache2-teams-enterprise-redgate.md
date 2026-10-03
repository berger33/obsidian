---
id: software.devops.tranche08.000760
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

# Redgate Flyway: código aberto Apache-2.0 no repositório flyway/flyway e ecossistema Redgate

## Em uma frase
O núcleo do Flyway é mantido como software livre sob licença Apache-2.0 no repositório `flyway/flyway` (com artefatos publicados no Maven Central sob `org.flywaydb`), integrando-se à documentação e aos recursos avançados da Redgate.

## Por que importa
Ao selecionar uma ferramenta de migração de banco de dados para padronização corporativa, arquitetos precisam conhecer o licenciamento do código-fonte aberto, onde reportar issues, como consultar as notas de versão e quais recursos pertencem ao núcleo Apache-2.0 versus capacidades estendidas da plataforma Redgate Flyway. O README oficial do repositório `flyway/flyway` documenta essa estrutura.

## Como funciona
Todo o código-fonte aberto do Flyway no repositório `github.com/flyway/flyway` é licenciado sob a **Apache License 2.0** (`LICENSE.md`), publicado no Maven Central (`org.flywaydb:flyway-core`) e no Docker Hub (`redgate/flyway`). O projeto mantém documentação centralizada em `documentation.red-gate.com/flyway`, notas de release detalhadas (`Release Notes`) a cada versão, fórum comunitário oficial da Redgate e rastreamento público de bugs e sugestões de melhoria via GitHub Issues (com política dedicada de divulgação responsável de vulnerabilidades em `SECURITY.md`).

## Exemplo
```bash
# Verificar a edição, versão e licença reportadas pelo binário da CLI ou container do Flyway
flyway -v
```

## Limites e trade-offs
Ao consultar a documentação oficial em `documentation.red-gate.com/flyway`, observe as marcações de disponibilidade de recursos por tier (Community Apache-2.0 vs Teams/Enterprise), pois determinadas capacidades avançadas de governança corporativa (como geração automatizada de migrações a partir do schema model, drift checks automatizados ou conectores legados específicos em versões antigas) podem exigir licenciamento comercial Redgate.

## Como verificar
Verifique as coordenadas Maven `org.flywaydb:flyway-core` no `pom.xml` ou `build.gradle` e consulte as Release Notes oficiais antes de atualizar entre versões principais do Flyway.

## Conexões
- [[flyway-concorrencia-locks-transacoes-out-of-order]] — Veja também: Redgate Flyway: controle de concorrência, escopo de transações (group) e migrações fora de ordem (outOfOrder).
- [[flyway-migracoes-banco-dados-schema-history-versionamento]] — Referência cruzada direta com flyway-migracoes-banco-dados-schema-history-versionamento.
- [[flyway-modos-execucao-cli-docker-java-api-maven-gradle]] — Referência cruzada direta com flyway-modos-execucao-cli-docker-java-api-maven-gradle.
- [[liquibase-mudancas-versao-5-0-licenca-fsl-community-secure]] — Referência cruzada direta com liquibase-mudancas-versao-5-0-licenca-fsl-community-secure.

## Fontes
- [Redgate Flyway GitHub — README.md (How Flyway Works, 5 Execution Modes, Schema Model & 50+ Supported Databases)](https://raw.githubusercontent.com/flyway/flyway/main/README.md) — README oficial do Flyway (Apache-2.0) explicando o funcionamento da tabela flyway_schema_history, migrações SQL e Java, captura de schema model em disco e matriz de mais de 50 bancos suportados; consultado em 2026-10-03.
- [Redgate Flyway Official Documentation — Getting Started with Flyway](https://documentation.red-gate.com/flyway/getting-started-with-flyway) — Documentação oficial da Redgate para configuração, convenções de nomenclatura (V, R, U) e comandos de ciclo de vida do Flyway; consultado em 2026-10-03.
- [Redgate Flyway — Official GitHub Repository](https://github.com/flyway/flyway) — Repositório oficial Apache-2.0 do Redgate Flyway; consultado em 2026-10-03.
