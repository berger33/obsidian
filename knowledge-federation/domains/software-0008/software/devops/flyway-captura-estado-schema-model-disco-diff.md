---
id: software.devops.tranche08.000754
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

# Redgate Flyway: captura de estado do esquema em disco (schema model) além de scripts de migração

## Em uma frase
Além de scripts de migração sequenciais, o Flyway suporta capturar o estado de objetos individuais do banco de dados em disco como um **schema model** para MySQL, Oracle, PostgreSQL e SQL Server, facilitando revisões de diff no Git.

## Por que importa
Quando um projeto acumula centenas de arquivos de migração (`V1__...sql` até `V450__...sql`), descobrir qual é a definição atual de uma tabela ou view apenas lendo o repositório Git torna-se difícil, pois uma tabela criada na `V1` pode ter sido alterada nas versões `V42`, `V118` e `V390`. Conforme destaca o parágrafo de abertura do README oficial do Flyway, a captura de estado como um `schema model` em disco resolve exatamente essa visibilidade.

## Como funciona
Para os quatro grandes motores empresariais (**MySQL**, **Oracle**, **PostgreSQL** e **SQL Server**), o fluxo moderno do Flyway permite manter, ao lado da pasta de migrações versionadas, uma representação em nível de objeto do esquema no sistema de arquivos (`schema model`). Quando um desenvolvedor altera uma tabela, view ou stored procedure no seu banco de dados de desenvolvimento, a captura do schema model grava o estado de cada objeto em arquivos individuais versionáveis no Git, permitindo visualizar exatamente o que mudou em cada objeto durante um Pull Request e gerar o script de migração versionada correspondente para o pipeline de produção.

## Exemplo
```bash
# Inspecionar a estrutura de um projeto Flyway combinando diretório de migrações SQL e configurações TOML
ls -la flyway.toml sql/ schema-model/
```

## Limites e trade-offs
O suporte nativo à captura de estado de esquema em disco (`schema model`) concentra-se nos quatro motores principais (MySQL, Oracle, PostgreSQL e SQL Server) e integra recursos avançados das edições comerciais/Redgate; para os demais motores entre os 50+ bancos suportados na edição Apache 2.0, o controle de versão baseia-se nas migrações versionadas (`V`), repetíveis (`R`) e callbacks.

## Como verificar
Verifique no repositório Git se as alterações no `schema-model/` correspondem exatamente ao efeito líquido das migrações versionadas pendentes em `sql/`.

## Conexões
- [[flyway-bancos-suportados-relacionais-cloud-data-warehouses]] — Veja também: Redgate Flyway: ecossistema de mais de 50 bancos de dados relacionais, distribuídos e data warehouses suportados.
- [[flyway-nomenclatura-migracoes-versionadas-repetiveis-undo]] — Veja também: Redgate Flyway: convenção de nomenclatura de migrações Versionadas (V), Repetíveis (R) e Undo (U).
- [[flyway-migracoes-banco-dados-schema-history-versionamento]] — Referência cruzada direta com flyway-migracoes-banco-dados-schema-history-versionamento.
- [[atlasdb-inspecao-esquema-hcl-sql-json-mermaid-erd]] — Referência cruzada direta com atlasdb-inspecao-esquema-hcl-sql-json-mermaid-erd.

## Fontes
- [Redgate Flyway GitHub — README.md (How Flyway Works, 5 Execution Modes, Schema Model & 50+ Supported Databases)](https://raw.githubusercontent.com/flyway/flyway/main/README.md) — README oficial do Flyway (Apache-2.0) explicando o funcionamento da tabela flyway_schema_history, migrações SQL e Java, captura de schema model em disco e matriz de mais de 50 bancos suportados; consultado em 2026-10-03.
- [Redgate Flyway Official Documentation — Getting Started with Flyway](https://documentation.red-gate.com/flyway/getting-started-with-flyway) — Documentação oficial da Redgate para configuração, convenções de nomenclatura (V, R, U) e comandos de ciclo de vida do Flyway; consultado em 2026-10-03.
- [Redgate Flyway — Official GitHub Repository](https://github.com/flyway/flyway) — Repositório oficial Apache-2.0 do Redgate Flyway; consultado em 2026-10-03.
