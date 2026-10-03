---
id: software.devops.tranche08.000766
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

# Ariga Atlas: carregamento automático de esquema a partir de 16 ORMs em Go, TypeScript, Python, Java, C#/.NET e PHP

## Em uma frase
O Atlas integra-se nativamente a 16 ORMs populares em 6 ecossistemas de linguagens (Go, TypeScript/JavaScript, Python, Java/Kotlin, C#/.NET e PHP), extraindo o esquema diretamente dos modelos de código como fonte da verdade para `schema apply` ou `migrate diff`.

## Por que importa
Em equipes que utilizam ORMs (como GORM, Ent, Prisma, TypeORM, Drizzle, Sequelize, SQLAlchemy, Django, Hibernate, Entity Framework ou Doctrine), manter o esquema duplicado tanto nas classes/structs do ORM quanto em arquivos SQL separados gera retrabalho constante; por outro lado, os utilitários `auto-migrate` embutidos nos próprios ORMs são limitados e inseguros para produção. A seção `Supported ORMs` do README oficial do Atlas resolve esse dilema.

## Como funciona
Por meio de provedores `external_schema` configurados no arquivo `atlas.hcl` (ou drivers nativos), o Atlas lê diretamente as definições do ORM da aplicação em: (1) **Go**: Ent, GORM, Beego, SQLBoiler e Bun; (2) **JavaScript/TypeScript**: Prisma, Sequelize, TypeORM, Drizzle e MikroORM; (3) **Python**: SQLAlchemy, Django e PonyORM; (4) **Java/Kotlin**: Hibernate; (5) **C#/.NET**: Entity Framework Core; e (6) **PHP**: Doctrine. O Atlas converte o modelo do ORM em um esquema alvo (`to = data.external_schema.gorm.url`) e usa seu motor de planejamento e seus 50+ analisadores (`atlas migrate diff` / `atlas migrate lint`) para gerar migrações SQL seguras e auditáveis a partir do código do ORM.

## Exemplo
```hcl
# Exemplo de atlas.hcl carregando o esquema diretamente dos modelos SQLAlchemy (Python) ou GORM (Go)
data "external_schema" "app_orm" {
  program = [
    "atlas-provider-sqlalchemy",
    "--path", "./app/models",
    "--dialect", "postgresql"
  ]
}

env "local" {
  src = data.external_schema.app_orm.url
  dev = "docker://postgres/15/dev"
  migration {
    dir = "file://migrations"
  }
}
```

## Limites e trade-offs
Quando o esquema é extraído de um ORM via `external_schema`, recursos específicos do banco de dados que o ORM escolhido não consegue expressar em suas anotações de código (como triggers customizadas, políticas de Row-Level Security ou funções PL/pgSQL complexas) precisam ser compostos usando `composite_schema` no Atlas (combinando o schema do ORM com arquivos `.sql`/`.hcl` complementares) para que o Atlas não tente removê-los ao calcular o diff.

## Como verificar
Com o `atlas.hcl` configurado para o seu ORM, execute `atlas schema inspect --env local --url "env://src"` para imprimir em SQL ou HCL o esquema exato extraído das classes/structs do seu código.

## Conexões
- [[atlasdb-linting-migracoes-50-analisadores-seguranca]] — Veja também: Ariga Atlas: análise estática e linting de migrações (atlas migrate lint) com mais de 50 analisadores de risco.
- [[atlasdb-testes-unitarios-esquema-migracoes-test-hcl]] — Veja também: Ariga Atlas: testes automatizados de esquemas e migrações (atlas schema test e atlas migrate test) com .test.hcl.
- [[atlasdb-schema-as-code-declarativo-versionado-multibanco]] — Referência cruzada direta com atlasdb-schema-as-code-declarativo-versionado-multibanco.
- [[atlasdb-fluxo-versionado-migrate-diff-lint-apply]] — Referência cruzada direta com atlasdb-fluxo-versionado-migrate-diff-lint-apply.

## Fontes
- [Ariga Atlas GitHub — README.md (Declarative & Versioned Workflows, 50+ Lint Analyzers, 16 ORMs, Schema Test & Security-as-Code)](https://raw.githubusercontent.com/ariga/atlas/master/README.md) — README oficial do Ariga Atlas documentando schema inspect (HCL, SQL, JSON, Mermaid ERD), schema apply/diff, migrate diff/lint/apply, 16 ORMs, testes unitários .test.hcl, Security-as-Code (RLS/RBAC), Terraform Provider e Kubernetes Operator; consultado em 2026-10-03.
- [Ariga Atlas Official Documentation — Getting Started with Atlas](https://atlasgo.io/getting-started) — Guia oficial do Atlas (atlasgo.io) sobre uso de dev-url, inspeção e migrações declarativas e versionadas; consultado em 2026-10-03.
- [Ariga Atlas — Official GitHub Repository](https://github.com/ariga/atlas) — Repositório oficial do Ariga Atlas; consultado em 2026-10-03.
