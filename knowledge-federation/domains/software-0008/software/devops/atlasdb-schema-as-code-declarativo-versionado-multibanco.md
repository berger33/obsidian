---
id: software.devops.tranche08.000761
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
fontes: ["https://raw.githubusercontent.com/ariga/atlas/master/README.md", "https://atlasgo.io/getting-started", "https://github.com/ariga/atlas"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Ariga Atlas: ferramenta Schema-as-Code agnóstica de linguagem para gerenciamento declarativo e versionado de bancos de dados

## Em uma frase
O Ariga Atlas (`ariga/atlas`) é uma ferramenta agnóstica de linguagem para gerenciar e migrar esquemas de banco de dados segundo princípios modernos de DevOps (`Schema-as-Code`), oferecendo fluxos de trabalho tanto declarativos (estilo Terraform) quanto versionados.

## Por que importa
Em ferramentas tradicionais de migração, os desenvolvedores precisam escrever manualmente cada comando `ALTER TABLE` e revisar mudanças de banco no escuro sem saber se uma instrução SQL vai travar uma tabela em produção ou apagar dados acidentalmente. Segundo o README oficial do Atlas, a ferramenta planeja migrações automaticamente comparando o estado atual com o desejado (em HCL, SQL ou ORM) e analisa os riscos antes da aplicação.

## Como funciona
O Atlas suporta dois fluxos complementares sobre Postgres, MySQL, MariaDB, SQLite, SQL Server, ClickHouse, Snowflake, Redshift, CockroachDB, Spanner e Aurora DSQL: (1) **Declarative migrations**: similar ao Terraform, o comando `atlas schema apply` compara o estado atual do banco ativo com o estado desejado definido em HCL, SQL ou no esquema de um ORM e gera/executa um plano de migração para atingir aquele estado; e (2) **Versioned migrations**: diferentemente de outras ferramentas, o comando `atlas migrate diff` planeja automaticamente as migrações de esquema para o desenvolvedor com base no estado desejado, salvando os arquivos SQL versionados e o arquivo de integridade `atlas.sum` para revisão e execução controlada em CI/CD via `atlas migrate lint` e `atlas migrate apply`.

## Exemplo
```bash
# Instalar a CLI do Atlas em Linux/macOS usando o instalador oficial documentado no README
curl -sSf https://atlasgo.sh | sh
atlas version
```

## Limites e trade-offs
O fluxo puramente declarativo (`atlas schema apply`) é excelente para desenvolvimento rápido, ambientes de preview e mudanças diretas, mas quando uma transição de estado é ambígua (por exemplo, renomear uma coluna versus dropar a coluna antiga e criar uma nova vazia) ou exige backfilling customizado de dados em produção crítica, o fluxo **versionado** (`atlas migrate diff` -> revisão/edição do `.sql` -> `atlas migrate lint` -> `atlas migrate apply`) oferece controle determinístico passo a passo.

## Como verificar
Execute `atlas version` após a instalação (via `curl -sSf https://atlasgo.sh | sh`, `brew install ariga/tap/atlas`, Docker `arigaio/atlas` ou `npm i @ariga/atlas`) para validar o binário.

## Conexões
- [[atlasdb-inspecao-esquema-hcl-sql-json-mermaid-erd]] — Veja também: Ariga Atlas: inspeção de esquemas (atlas schema inspect) em HCL, SQL dividido por arquivo, JSON e diagramas ERD Mermaid.
- [[atlasdb-fluxo-declarativo-schema-apply-diff-plan]] — Referência cruzada direta com atlasdb-fluxo-declarativo-schema-apply-diff-plan.
- [[atlasdb-fluxo-versionado-migrate-diff-lint-apply]] — Referência cruzada direta com atlasdb-fluxo-versionado-migrate-diff-lint-apply.

## Fontes
- [Ariga Atlas GitHub — README.md (Declarative & Versioned Workflows, 50+ Lint Analyzers, 16 ORMs, Schema Test & Security-as-Code)](https://raw.githubusercontent.com/ariga/atlas/master/README.md) — README oficial do Ariga Atlas documentando schema inspect (HCL, SQL, JSON, Mermaid ERD), schema apply/diff, migrate diff/lint/apply, 16 ORMs, testes unitários .test.hcl, Security-as-Code (RLS/RBAC), Terraform Provider e Kubernetes Operator; consultado em 2026-10-03.
- [Ariga Atlas Official Documentation — Getting Started with Atlas](https://atlasgo.io/getting-started) — Guia oficial do Atlas (atlasgo.io) sobre uso de dev-url, inspeção e migrações declarativas e versionadas; consultado em 2026-10-03.
- [Ariga Atlas — Official GitHub Repository](https://github.com/ariga/atlas) — Repositório oficial do Ariga Atlas; consultado em 2026-10-03.
