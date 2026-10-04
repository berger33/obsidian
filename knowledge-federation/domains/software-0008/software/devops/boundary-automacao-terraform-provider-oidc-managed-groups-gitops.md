---
id: software.devops.tranche19.001850
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-19.md"
fontes: ["https://developer.hashicorp.com/boundary/docs/what-is-boundary", "https://raw.githubusercontent.com/hashicorp/boundary/main/README.md", "https://github.com/hashicorp/boundary"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# HashiCorp Boundary como Código: provisionamento declarativo de Scopes, OIDC, Managed Groups e Targets via Terraform Provider

## Em uma frase
Toda a configuração do Boundary (Scopes, Auth Methods OIDC/LDAP, Managed Groups, Roles, Host Catalogs, Credential Stores e Targets) pode ser gerenciada declarativamente por GitOps através do **Terraform Provider oficial `hashicorp/boundary`**.

## Por que importa
Criar dezenas de projetos, roles e targets clicando na interface web ou rodando scripts manuais de CLI dificulta auditorias de revisão por Pull Request e a replicação entre ambientes de staging e produção.

## Como funciona
Com o provider `hashicorp/boundary`, a equipe de segurança define regras de *OIDC Managed Groups* (por exemplo `filter = "\"/token/groups\" contains \"devops-prod\""`) e as vincula a `boundary_role` e `boundary_target` em código HCL versionado.

## Exemplo
```hcl
resource "boundary_target" "prod_postgres" {
  type                     = "tcp"
  name                     = "prod-postgres-ro"
  description              = "Acesso somente-leitura ao PostgreSQL de produção"
  scope_id                 = boundary_scope.prod_project.id
  default_port             = 5432
  session_max_seconds      = 7200
  session_connection_limit = -1
  address                  = "pg-ro.prod.internal"
  brokered_credential_source_ids = [
    boundary_credential_library_vault.pg_ro_creds.id
  ]
}
```

## Limites e trade-offs
Nunca salve senhas ou tokens estáticos no código Terraform do Boundary; referencie o Vault Provider ou variáveis sensíveis injetadas pelo runner de CI.

## Como verificar
Execute `terraform plan` sobre a configuração do provider `hashicorp/boundary` para validar os recursos antes de aplicar na API do Controller.

## Conexões
- [[boundary-session-recording-bsr-storage-buckets-auditoria-ssh]] — Veja também: HashiCorp Boundary Session Recording (BSR): gravação e reprodução criptografada de sessões SSH para conformidade.

## Fontes
- [HashiCorp Boundary GitHub — README.md (Identity-Aware Proxy, Controller & Workers, PostgreSQL & KMS Requirements, Dev Mode & CLI)](https://developer.hashicorp.com/boundary/docs/what-is-boundary) — README oficial do hashicorp/boundary detalhando os componentes Controller e Worker, requisitos de banco SQL e KMS, hierarquia de Scopes e boundary connect; consultado em 2026-10-03.
- [HashiCorp Developer — What is Boundary? (Core Workflow, OIDC Authentication, Vault Credential Brokering/Injection, Multi-Hop & Session Recording)](https://raw.githubusercontent.com/hashicorp/boundary/main/README.md) — Documentação oficial do HashiCorp Boundary cobrindo acesso just-in-time sem agente, credenciais dinâmicas via Vault, sessões transparentes e gravação BSR; consultado em 2026-10-03.
- [HashiCorp Boundary — Official GitHub Repository](https://github.com/hashicorp/boundary) — Repositório oficial do HashiCorp Boundary; consultado em 2026-10-03.
