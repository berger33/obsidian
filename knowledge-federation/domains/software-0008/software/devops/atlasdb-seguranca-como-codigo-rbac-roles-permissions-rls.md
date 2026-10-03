---
id: software.devops.tranche08.000768
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

# Ariga Atlas: Security-as-Code para bancos de dados (roles, users, permissions e Row-Level Security em HCL)

## Em uma frase
O Atlas estende o conceito de Schema-as-Code para **Security-as-Code**, permitindo declarar `role`, `user`, `permission` (`GRANT`/`REVOKE`) e `policy` de Row-Level Security (`RLS`) diretamente em HCL com suporte a diff, lint e apply.

## Por que importa
Na maioria das empresas, mesmo quando as tabelas são criadas por migrações automatizadas, a criação de roles de banco de dados, concessão de permissões (`GRANT SELECT, INSERT ON ...`) e políticas de segurança em nível de linha (`Row-Level Security` no PostgreSQL) ainda são feitas manualmente por DBAs via console SQL, gerando permissões excessivas e desvios de auditoria. A seção `Database Security-as-Code` do README oficial do Atlas mostra como codificar essa camada.

## Como funciona
Na definição HCL do esquema do Atlas, além de `table` e `schema`, o engenheiro pode declarar: (1) blocos **`role`** e **`user`**; (2) blocos **`permission`** especificando `for = table.users`, `to = role.app_Team` e `grant = [SELECT, INSERT, UPDATE]`; e (3) blocos **`policy`** (Row-Level Security) dentro da definição da tabela, especificando `for = "ALL"`, `to = [role.app_team]`, a expressão `using = "tenant_id = current_setting('app.current_tenant')::integer"` e `with_check`. O motor do Atlas inspeciona as permissões e políticas RLS atuais do banco e gera automaticamente os comandos `CREATE ROLE`, `GRANT`, `ENABLE ROW LEVEL SECURITY` e `CREATE POLICY`.

## Exemplo
```hcl
# Exemplo declarativo de Security-as-Code no Atlas (Role, Permission e Row-Level Security Policy)
role "app_team" {}

permission "users_perms" {
  for   = table.users
  to    = role.app_team
  grant = [SELECT, INSERT, UPDATE]
}
```

## Limites e trade-offs
Como gerenciar roles e `GRANT`s no nível do banco de dados exige que a conexão usada pelo Atlas possua privilégios administrativos (`CREATEROLE` / `SUPERUSER` ou owner dos objetos), em ambientes onde o pipeline de CI/CD da aplicação possui privilégios restritos apenas ao schema de negócio, as declarações globais de roles/usuários podem precisar ser aplicadas por um pipeline de plataforma separado com credenciais de administração.

## Como verificar
Declare uma `policy` de RLS ou `permission` no seu arquivo `.hcl` e execute `atlas schema diff` contra o banco de desenvolvimento para inspecionar os comandos `GRANT` e `CREATE POLICY` gerados no plano.

## Conexões
- [[atlasdb-testes-unitarios-esquema-migracoes-test-hcl]] — Veja também: Ariga Atlas: testes automatizados de esquemas e migrações (atlas schema test e atlas migrate test) com .test.hcl.
- [[atlasdb-integracao-cloud-native-terraform-kubernetes-operator-cicd]] — Veja também: Ariga Atlas: integrações cloud-native com Terraform Provider, Kubernetes Operator e GitHub Actions/GitLab CI.
- [[atlasdb-schema-as-code-declarativo-versionado-multibanco]] — Referência cruzada direta com atlasdb-schema-as-code-declarativo-versionado-multibanco.
- [[atlasdb-fluxo-declarativo-schema-apply-diff-plan]] — Referência cruzada direta com atlasdb-fluxo-declarativo-schema-apply-diff-plan.
- [[bytebase-controle-acesso-rbac-jit-dynamic-data-masking]] — Referência cruzada direta com bytebase-controle-acesso-rbac-jit-dynamic-data-masking.

## Fontes
- [Ariga Atlas GitHub — README.md (Declarative & Versioned Workflows, 50+ Lint Analyzers, 16 ORMs, Schema Test & Security-as-Code)](https://raw.githubusercontent.com/ariga/atlas/master/README.md) — README oficial do Ariga Atlas documentando schema inspect (HCL, SQL, JSON, Mermaid ERD), schema apply/diff, migrate diff/lint/apply, 16 ORMs, testes unitários .test.hcl, Security-as-Code (RLS/RBAC), Terraform Provider e Kubernetes Operator; consultado em 2026-10-03.
- [Ariga Atlas Official Documentation — Getting Started with Atlas](https://atlasgo.io/getting-started) — Guia oficial do Atlas (atlasgo.io) sobre uso de dev-url, inspeção e migrações declarativas e versionadas; consultado em 2026-10-03.
- [Ariga Atlas — Official GitHub Repository](https://github.com/ariga/atlas) — Repositório oficial do Ariga Atlas; consultado em 2026-10-03.
