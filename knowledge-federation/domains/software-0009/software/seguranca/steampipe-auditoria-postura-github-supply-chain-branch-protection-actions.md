---
id: software.seguranca.tranche10.000907
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/turbot/steampipe/main/README.md", "https://raw.githubusercontent.com/turbot/powerpipe/main/README.md", "https://steampipe.io/docs/reference/cli/overview"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Steampipe Plugin **`github`**: Auditoria SQL de **Supply Chain, Repositórios Públicos, Branch Protection, Segredos e GitHub Actions**

## Em uma frase
Gerenciar a postura de segurança de centenas de repositórios em uma organização GitHub corporativa clicando na interface web é impossível; com o plugin **`github`** do Steampipe (`steampipe plugin install github`) e o Mod **`github_compliance`** do Powerpipe, toda a organização GitHub vira um banco SQL auditável!

## Por que importa
As tabelas do plugin `github` incluem `github_my_repository`, `github_branch_protection`, `github_workflow`, `github_actions_repository_permission`, `github_organization_member` (com o campo **`two_factor_enabled`**!), `github_repository_dependabot_alert` e `github_repository_code_scanning_alert`.

## Como funciona
Em segundos, uma query SQL identifica quais membros da organização não têm 2FA habilitado, quais repositórios de produção não exigem revisão de Pull Request ou assinatura de commits na branch `main`, ou quais workflows usam permissões excessivas!

## Exemplo
```sql
-- Auditar todos os repositorios da organizacao GitHub em busca de branches padrao sem protecao de Pull Request ou assinatura
SELECT
  r.name_with_owner,
  r.visibility,
  r.default_branch_ref ->> 'name' AS default_branch,
  r.default_branch_ref -> 'branch_protection_rule' ->> 'requires_approving_reviews' AS requires_review,
  r.default_branch_ref -> 'branch_protection_rule' ->> 'requires_commit_signatures' AS requires_signed_commits
FROM
  github_my_repository AS r
WHERE
  NOT r.is_archived;
```

## Limites e trade-offs
Configure o token no arquivo `~/.steampipe/config/github.spc` usando um **Fine-Grained Personal Access Token** ou **GitHub App** com permissões estritamente *Read-Only* (`metadata:read`, `administration:read`, `members:read`) para que o processo de auditoria nunca tenha permissão de escrita sobre o código.

## Como verificar
Complemente a auditoria organizacional do plugin `github` do Steampipe com o **OpenSSF Scorecard** nos repositórios críticos.

## Conexões
- [[steampipe-auditoria-shift-left-iac-plugins-terraform-kubernetes-docker]] — Veja também: Steampipe **Shift-Left IaC**: Auditoria SQL de Arquivos Locais **Terraform (`.tf`, `.tfstate`)**, Manifestos **Kubernetes YAML** e **`Dockerfile`**.
- [[steampipe-modo-servico-steampipe-service-cache-ttl-clientes-externos]] — Veja também: Steampipe **`steampipe service`**: Operação como Daemon PostgreSQL (`:9193`), Controle de **Cache TTL (`--cache-ttl`)** e Conexão via `psql` / Grafana / Metabase.
- [[steampipe-arquitetura-zero-etl-postgres-fdw-plugins-sql-cloud]] — Referência cruzada direta com steampipe-arquitetura-zero-etl-postgres-fdw-plugins-sql-cloud.

## Fontes
- [Turbot Steampipe Official GitHub — Zero-ETL SQL Engine & PostgreSQL FDW Architecture](https://raw.githubusercontent.com/turbot/steampipe/main/README.md) — repositório oficial do Steampipe cobrindo arquitetura Zero-ETL sobre PostgreSQL FDW, plugins multi-cloud e distribuições SQLite/Postgres; consultado em 2026-10-03.
- [Turbot Powerpipe Official GitHub — Dashboards & 5,000+ Compliance Benchmarks as Code in HCL](https://raw.githubusercontent.com/turbot/powerpipe/main/README.md) — repositório oficial do Powerpipe cobrindo execução de benchmarks CIS/NIST/PCI/SOC2/HIPAA e controles customizados em HCL; consultado em 2026-10-03.
- [Steampipe Official CLI & Exit Codes Reference Documentation](https://steampipe.io/docs/reference/cli/overview) — documentação oficial de subcomandos CLI (`query`, `service`, `plugin`), flags globais e códigos de saída do Steampipe; consultado em 2026-10-03.
