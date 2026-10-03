---
id: software.devops.tranche08.000762
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

# Ariga Atlas: inspeção de esquemas (atlas schema inspect) em HCL, SQL dividido por arquivo, JSON e diagramas ERD Mermaid

## Em uma frase
O comando `atlas schema inspect` conecta-se a bancos de dados existentes ou lê definições locais e exporta o esquema completo em formato Atlas HCL (padrão), DDL SQL (único ou um arquivo por objeto com `sql . | split`), JSON ou diagramas Entidade-Relacionamento (`Mermaid ERD`).

## Por que importa
Antes de automatizar migrações em um banco de dados existente ou documentar a arquitetura de dados de um sistema, a equipe precisa extrair com precisão todas as tabelas, colunas, índices, chaves estrangeiras, views e funções existentes. A seção `Inspecting schemas` do README oficial do Atlas demonstra os múltiplos formatos de saída suportados por `atlas schema inspect`.

## Como funciona
Ao executar `atlas schema inspect -u "mysql://root:pass@localhost:3306/example" > schema.hcl`, o Atlas inspeciona o catálogo do banco de dados e gera a representação declarativa na linguagem de configuração do Atlas (HCL). Usando a flag `--format`, o mesmo comando pode emitir: (1) **SQL puro** (`--format '{{ sql . }}' > schema.sql`); (2) **SQL dividido em múltiplos arquivos** por tipo e nome de objeto (`--format '{{ sql . | split }}'`, gravando `tables/users.sql`, `views/...`, etc.); (3) **JSON estruturado** (`--format '{{ json . }}' | jq`) para consumo por scripts e ferramentas de governança; ou (4) **Diagramas Mermaid ERD** (`--format '{{ mermaid . }}'`) prontos para renderizar diagramas visuais em Markdown/GitHub/Obsidian.

## Exemplo
```bash
# Inspecionar um banco PostgreSQL exportando em HCL, SQL e diagrama Entidade-Relacionamento Mermaid
atlas schema inspect -u "postgres://postgres:pass@localhost:5432/appdb?sslmode=disable" > schema.hcl
atlas schema inspect -u "postgres://postgres:pass@localhost:5432/appdb?sslmode=disable" --format '{{ sql . }}' > schema.sql
atlas schema inspect -u "postgres://postgres:pass@localhost:5432/appdb?sslmode=disable" --format '{{ mermaid . }}' > erd.mmd
```

## Limites e trade-offs
Quando se inspeciona um servidor de banco de dados inteiro sem especificar o nome do banco/schema na URL de conexão (ex.: `mysql://root:pass@localhost:3306/`), o Atlas inspeciona **todos** os schemas não-sistema do servidor (modo multi-schema realm); se o seu aplicativo gerencia apenas um schema específico, inclua sempre o nome do banco/schema na URL (ou flag `--schema`) para evitar exportar objetos de outros microsserviços.

## Como verificar
Execute `atlas schema inspect -u "sqlite://file.db" --format '{{ mermaid . }}'` e cole o bloco resultante em um documento Markdown para verificar a geração automática do diagrama ERD com tabelas e chaves estrangeiras.

## Conexões
- [[atlasdb-schema-as-code-declarativo-versionado-multibanco]] — Veja também: Ariga Atlas: ferramenta Schema-as-Code agnóstica de linguagem para gerenciamento declarativo e versionado de bancos de dados.
- [[atlasdb-fluxo-declarativo-schema-apply-diff-plan]] — Veja também: Ariga Atlas: fluxo declarativo (atlas schema diff e atlas schema apply) com dev-url para normalização.
- [[flyway-captura-estado-schema-model-disco-diff]] — Referência cruzada direta com flyway-captura-estado-schema-model-disco-diff.

## Fontes
- [Ariga Atlas GitHub — README.md (Declarative & Versioned Workflows, 50+ Lint Analyzers, 16 ORMs, Schema Test & Security-as-Code)](https://raw.githubusercontent.com/ariga/atlas/master/README.md) — README oficial do Ariga Atlas documentando schema inspect (HCL, SQL, JSON, Mermaid ERD), schema apply/diff, migrate diff/lint/apply, 16 ORMs, testes unitários .test.hcl, Security-as-Code (RLS/RBAC), Terraform Provider e Kubernetes Operator; consultado em 2026-10-03.
- [Ariga Atlas Official Documentation — Getting Started with Atlas](https://atlasgo.io/getting-started) — Guia oficial do Atlas (atlasgo.io) sobre uso de dev-url, inspeção e migrações declarativas e versionadas; consultado em 2026-10-03.
- [Ariga Atlas — Official GitHub Repository](https://github.com/ariga/atlas) — Repositório oficial do Ariga Atlas; consultado em 2026-10-03.
