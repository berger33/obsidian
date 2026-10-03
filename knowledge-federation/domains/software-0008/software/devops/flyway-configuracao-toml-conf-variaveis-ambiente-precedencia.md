---
id: software.devops.tranche08.000758
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

# Redgate Flyway: configuração declarativa (flyway.toml e flyway.conf), variáveis FLYWAY_* e precedência

## Em uma frase
O Flyway pode ser configurado por arquivos de projeto (`flyway.toml` moderno ou `flyway.conf` clássico), variáveis de ambiente (`FLYWAY_*`), parâmetros de linha de comando (`-key=value`) e configurações de plugins Maven/Gradle.

## Por que importa
Hardcodar URLs de banco de dados, schemas e políticas de validação diretamente em scripts bash dificulta compartilhar configurações padrão da equipe no Git enquanto se injeta credenciais seguras por ambiente no servidor de CI/CD. A documentação oficial `Getting started with Flyway` detalha o sistema hierárquico de configuração.

## Como funciona
O Flyway permite versionar no repositório as opções estruturais do projeto — como `locations` (`filesystem:./sql`), `schemas`, `table` (nome customizado da tabela de histórico caso não se deseje o padrão `flyway_schema_history`), `baselineOnMigrate` e ambientes (`[environments.default]` no `flyway.toml`) — enquanto credenciais sensíveis e URLs específicas do ambiente de destino são fornecidas via variáveis de ambiente (`FLYWAY_URL`, `FLYWAY_USER`, `FLYWAY_PASSWORD`, `FLYWAY_SCHEMAS`) ou flags de linha de comando (`-url=... -user=...`), onde argumentos de linha de comando têm precedência sobre variáveis de ambiente, que por sua vez sobrescrevem os arquivos de configuração em disco.

## Exemplo
```toml
# Exemplo de arquivo flyway.toml versionado no repositório definindo localizações e validação estrita
[flyway]
locations = ["filesystem:./sql"]
validateMigrationNaming = true
cleanDisabled = true

[environments.default]
url = "jdbc:postgresql://localhost:5432/devdb"
schemas = ["public"]
```

## Limites e trade-offs
Habilitar `validateMigrationNaming = true` no `flyway.toml` (ou `flyway.conf`) é altamente recomendado porque faz o Flyway falhar imediatamente caso encontre no diretório `sql/` algum arquivo mal nomeado (por exemplo, `V1_create_table.sql` com um único sublinhado); sem essa flag ativa, arquivos que não casam com o padrão podem ser silenciosamente ignorados durante o scan, fazendo o desenvolvedor acreditar que sua migração rodou quando na verdade foi pulada.

## Como verificar
Execute `flyway info` com `validateMigrationNaming = true` ativo e confirme que todas as configurações do `flyway.toml` e variáveis `FLYWAY_*` foram carregadas sem avisos.

## Conexões
- [[flyway-migracoes-java-jdbc-placeholders-callbacks]] — Veja também: Redgate Flyway: migrações escritas em Java (BaseJavaMigration), substituição de Placeholders e Callbacks.
- [[flyway-concorrencia-locks-transacoes-out-of-order]] — Veja também: Redgate Flyway: controle de concorrência, escopo de transações (group) e migrações fora de ordem (outOfOrder).
- [[flyway-migracoes-banco-dados-schema-history-versionamento]] — Referência cruzada direta com flyway-migracoes-banco-dados-schema-history-versionamento.
- [[flyway-nomenclatura-migracoes-versionadas-repetiveis-undo]] — Referência cruzada direta com flyway-nomenclatura-migracoes-versionadas-repetiveis-undo.
- [[flyway-comandos-ciclo-vida-info-validate-migrate-baseline-repair]] — Referência cruzada direta com flyway-comandos-ciclo-vida-info-validate-migrate-baseline-repair.

## Fontes
- [Redgate Flyway GitHub — README.md (How Flyway Works, 5 Execution Modes, Schema Model & 50+ Supported Databases)](https://raw.githubusercontent.com/flyway/flyway/main/README.md) — README oficial do Flyway (Apache-2.0) explicando o funcionamento da tabela flyway_schema_history, migrações SQL e Java, captura de schema model em disco e matriz de mais de 50 bancos suportados; consultado em 2026-10-03.
- [Redgate Flyway Official Documentation — Getting Started with Flyway](https://documentation.red-gate.com/flyway/getting-started-with-flyway) — Documentação oficial da Redgate para configuração, convenções de nomenclatura (V, R, U) e comandos de ciclo de vida do Flyway; consultado em 2026-10-03.
- [Redgate Flyway — Official GitHub Repository](https://github.com/flyway/flyway) — Repositório oficial Apache-2.0 do Redgate Flyway; consultado em 2026-10-03.
