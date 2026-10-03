---
id: software.devops.tranche08.000741
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

# Liquibase: plataforma de versionamento, rastreamento e implantação de mudanças de esquema de banco de dados

## Em uma frase
O Liquibase permite às equipes rastrear, versionar, ordenar automaticamente, implantar e reverter (rollback) mudanças de esquema de banco de dados usando changelogs declarativos ou SQL integrados a ferramentas de CI/CD.

## Por que importa
Aplicar scripts SQL manualmente em bancos de dados de produção causa erros humanos, atrasos em releases e divergência (drift) entre ambientes de desenvolvimento, homologação e produção, sem registro confiável de quais scripts já rodaram em cada instância. Segundo o README oficial do Liquibase, a ferramenta elimina erros e atrasos ao ordenar scripts automaticamente para implantação e controlar mudanças de esquema para versões específicas.

## Como funciona
O Liquibase organiza as alterações de banco de dados em arquivos chamados **changelogs** (escritos em SQL anotado, XML, YAML ou JSON) compostos por unidades atômicas chamadas **changesets** (identificadas por `author` e `id`). Quando o comando `liquibase update` é executado contra um banco de dados via JDBC, o Liquibase verifica a tabela de rastreamento de histórico no banco (`DATABASECHANGELOG`) e a tabela de controle de concorrência (`DATABASECHANGELOGLOCK`), aplica em ordem estrita apenas os changesets pendentes que ainda não foram executados, registra o checksum e a data de execução de cada um (visível via `liquibase history`) e suporta reversão controlada via comandos de `rollback`.

## Exemplo
```bash
# Fluxo oficial de exemplo do README usando o banco em memória H2 incluído na CLI do Liquibase
liquibase init start-h2
liquibase update
liquibase history
```

## Limites e trade-offs
Como o Liquibase utiliza a tabela `DATABASECHANGELOGLOCK` para garantir que apenas uma instância do Liquibase aplique migrações por vez no mesmo banco de dados, se um processo `liquibase update` for morto abruptamente por queda de rede ou OOMKill em um pod de CI/CD no meio de uma migração, o lock pode permanecer preso (`LOCKED = true`), exigindo verificar o estado e executar `liquibase release-locks` antes da próxima tentativa.

## Como verificar
Execute `liquibase status --verbose` antes do deploy para listar os changesets pendentes e `liquibase history` após o `liquibase update` para confirmar a aplicação bem-sucedida de todas as mudanças.

## Conexões
- [[liquibase-mudancas-versao-5-0-licenca-fsl-community-secure]] — Veja também: Liquibase 5.0+: separação entre Liquibase Community (licença FSL) e Liquibase Secure (comercial).
- [[liquibase-gerenciamento-drivers-lpm-breaking-change-5-0]] — Referência cruzada direta com liquibase-gerenciamento-drivers-lpm-breaking-change-5-0.
- [[flyway-migracoes-banco-dados-schema-history-versionamento]] — Referência cruzada direta com flyway-migracoes-banco-dados-schema-history-versionamento.

## Fontes
- [Liquibase GitHub — README.md (Database Schema Change Management, Quarterly Releases & CI/CD Integrations)](https://raw.githubusercontent.com/liquibase/liquibase/master/README.md) — README oficial do Liquibase cobrindo rastreamento e rollback de mudanças de banco de dados, fluxo com H2, cadência de releases trimestrais/nightly e gate de aprovação Sonatype; consultado em 2026-10-03.
- [Liquibase Docker Documentation — docker/README.md (Liquibase 5.0 FSL vs Secure, LPM Drivers & Migration Guide)](https://raw.githubusercontent.com/liquibase/liquibase/main/docker/README.md) — Documentação oficial de imagens Docker do Liquibase detalhando o licenciamento 5.0+ (Community FSL vs Secure), remoção de drivers embutidos por padrão, uso do Liquibase Package Manager (lpm add --global) e roteiro de migração de 6 etapas; consultado em 2026-10-03.
- [Liquibase — Official GitHub Repository](https://github.com/liquibase/liquibase) — Repositório oficial do Liquibase; consultado em 2026-10-03.
