---
id: software.devops.tranche08.000744
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

# Liquibase: execução em containers Docker, variáveis LIQUIBASE_COMMAND_* e distribuição multi-registry

## Em uma frase
As imagens oficiais do Liquibase são publicadas simultaneamente no Docker Hub (`liquibase/liquibase`), GitHub Container Registry (`ghcr.io/liquibase/liquibase`) e Amazon ECR Public (`public.ecr.aws/liquibase/liquibase`), aceitando configuração direta por variáveis `LIQUIBASE_COMMAND_*`.

## Por que importa
Em pipelines cloud-native (Kubernetes Jobs, Argo Workflows, GitHub Actions, AWS CodeBuild), passar senhas de banco de dados como argumentos visíveis na linha de comando ou sofrer com limites de taxa (rate limit) de pull anônimo de um único registry público causa riscos de segurança e falhas de infraestrutura. O documento `docker/README.md` detalha os três registries oficiais e o uso de variáveis de ambiente.

## Como funciona
As imagens de container do Liquibase Community são construídas a partir do diretório `docker/` do repositório principal `liquibase/liquibase` (tendo substituído o antigo repositório depreciado `liquibase/docker`). Ao executar o container, o diretório local contendo os changelogs é montado em `/liquibase/changelog` e os parâmetros de conexão e execução são injetados via variáveis de ambiente `LIQUIBASE_COMMAND_URL` (ex.: `jdbc:postgresql://localhost:5432/mydb`), `LIQUIBASE_COMMAND_USERNAME` e `LIQUIBASE_COMMAND_PASSWORD`, seguidos do subcomando desejado (`validate`, `status`, `update`, `rollback`).

## Exemplo
```bash
# Validar e aplicar um changelog montado via volume usando variáveis de ambiente LIQUIBASE_COMMAND_*
docker run --rm \
  -v /caminho/para/changelog:/liquibase/changelog \
  -e LIQUIBASE_COMMAND_URL="jdbc:postgresql://test-db:5432/testdb" \
  -e LIQUIBASE_COMMAND_USERNAME="dbuser" \
  -e LIQUIBASE_COMMAND_PASSWORD="dbpassword" \
  ghcr.io/liquibase/liquibase:5.0.1 validate
```

## Limites e trade-offs
Lembre-se de que na imagem padrão `liquibase/liquibase:5.0+` os drivers JDBC não vêm pré-instalados; portanto, ao executar o comando `docker run` acima contra o PostgreSQL, você deve usar uma imagem onde `lpm add postgresql --global` já foi executado ou montar o JAR do driver JDBC no classpath do container.

## Como verificar
Execute o container com o subcomando `validate` antes de rodar `update` em não-produção para verificar que a sintaxe do changelog e as variáveis de ambiente foram reconhecidas sem erros.

## Conexões
- [[liquibase-gerenciamento-drivers-lpm-breaking-change-5-0]] — Veja também: Liquibase 5.0+: remoção de drivers embutidos por padrão e instalação via Liquibase Package Manager (LPM).
- [[liquibase-cadencia-releases-trimestrais-nightly-builds]] — Veja também: Liquibase: cadência de releases trimestrais da comunidade (Fev, Mai, Ago, Nov) e Nightly Builds da branch main.
- [[liquibase-gerenciamento-mudancas-esquema-banco-dados]] — Referência cruzada direta com liquibase-gerenciamento-mudancas-esquema-banco-dados.
- [[liquibase-integracoes-maven-gradle-spring-boot-cicd]] — Referência cruzada direta com liquibase-integracoes-maven-gradle-spring-boot-cicd.

## Fontes
- [Liquibase GitHub — README.md (Database Schema Change Management, Quarterly Releases & CI/CD Integrations)](https://raw.githubusercontent.com/liquibase/liquibase/master/README.md) — README oficial do Liquibase cobrindo rastreamento e rollback de mudanças de banco de dados, fluxo com H2, cadência de releases trimestrais/nightly e gate de aprovação Sonatype; consultado em 2026-10-03.
- [Liquibase Docker Documentation — docker/README.md (Liquibase 5.0 FSL vs Secure, LPM Drivers & Migration Guide)](https://raw.githubusercontent.com/liquibase/liquibase/main/docker/README.md) — Documentação oficial de imagens Docker do Liquibase detalhando o licenciamento 5.0+ (Community FSL vs Secure), remoção de drivers embutidos por padrão, uso do Liquibase Package Manager (lpm add --global) e roteiro de migração de 6 etapas; consultado em 2026-10-03.
- [Liquibase — Official GitHub Repository](https://github.com/liquibase/liquibase) — Repositório oficial do Liquibase; consultado em 2026-10-03.
