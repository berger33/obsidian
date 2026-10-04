---
id: software.devops.tranche19.001843
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
fontes: ["https://raw.githubusercontent.com/hashicorp/boundary/main/README.md", "https://developer.hashicorp.com/boundary/docs/what-is-boundary", "https://github.com/hashicorp/boundary"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# HashiCorp Boundary KMS: arquitetura de chaves (`root`, `worker-auth`, `recovery`, `config`) com Cloud KMS ou Vault Transit

## Em uma frase
O Boundary exige pelo menos um provedor **KMS** para operar em produção, utilizando derivação extensiva de chaves (*Key Derivation*) a partir de chaves mestras de propósito específico (`root`, `worker-auth`, `recovery` e opcionalmente `config` e `audit`) para cifrar todos os segredos no banco PostgreSQL e autenticar Workers.

## Por que importa
Se as credenciais de catálogos de nuvem, tokens do Vault ou chaves de sessão fossem gravadas em texto puro no PostgreSQL, qualquer DBA ou backup vazado do banco comprometeria toda a infraestrutura acessada pelo Boundary.

## Como funciona
Na configuração HCL do Controller, blocos `kms` apontam para **AWS KMS**, **GCP Cloud KMS**, **Azure Key Vault** ou para o **Transit Secrets Engine do HashiCorp Vault**: 1) a chave `root` protege as chaves de dados de cada escopo no banco; 2) a chave `worker-auth` autentica o registro entre Workers e Controllers; e 3) a chave `recovery` permite executar operações administrativas de emergência quando o método de login normal falha.

## Exemplo
```hcl
kms "transit" {
  purpose            = "root"
  address            = "https://vault.corp.internal:8200"
  token              = "s.xxxxxxxxxxxx"
  disable_renewal    = "false"
  key_name           = "boundary-root"
  mount_path         = "transit/"
}
```

## Limites e trade-offs
Nunca utilize chaves `aead` estáticas fixas em arquivo de texto para ambientes de produção; utilize sempre um KMS externo (Vault Transit ou Cloud KMS) e nunca perca a chave `root` do KMS, pois sem ela os segredos cifrados no PostgreSQL tornam-se irrecuperáveis.

## Como verificar
Inicialize o banco do Boundary com `boundary database init -config controller.hcl` e valide a conexão com o provedor KMS configurado.

## Conexões
- [[boundary-hierarquia-scopes-global-org-project-iam-roles-grants]] — Veja também: HashiCorp Boundary: modelagem hierárquica de `Scopes` (`global`, `org`, `project`), `Roles` e `Grants`.
- [[boundary-host-catalogs-static-dynamic-aws-azure-host-sets-targets]] — Veja também: HashiCorp Boundary: descoberta automatizada de endpoints com `Host Catalogs` dinâmicos, `Host Sets` e `Targets`.

## Fontes
- [HashiCorp Boundary GitHub — README.md (Identity-Aware Proxy, Controller & Workers, PostgreSQL & KMS Requirements, Dev Mode & CLI)](https://raw.githubusercontent.com/hashicorp/boundary/main/README.md) — README oficial do hashicorp/boundary detalhando os componentes Controller e Worker, requisitos de banco SQL e KMS, hierarquia de Scopes e boundary connect; consultado em 2026-10-03.
- [HashiCorp Developer — What is Boundary? (Core Workflow, OIDC Authentication, Vault Credential Brokering/Injection, Multi-Hop & Session Recording)](https://developer.hashicorp.com/boundary/docs/what-is-boundary) — Documentação oficial do HashiCorp Boundary cobrindo acesso just-in-time sem agente, credenciais dinâmicas via Vault, sessões transparentes e gravação BSR; consultado em 2026-10-03.
- [HashiCorp Boundary — Official GitHub Repository](https://github.com/hashicorp/boundary) — Repositório oficial do HashiCorp Boundary; consultado em 2026-10-03.
