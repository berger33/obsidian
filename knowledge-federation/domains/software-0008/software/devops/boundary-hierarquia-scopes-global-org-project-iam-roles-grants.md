---
id: software.devops.tranche19.001842
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

# HashiCorp Boundary: modelagem hierárquica de `Scopes` (`global`, `org`, `project`), `Roles` e `Grants`

## Em uma frase
O Boundary organiza todos os recursos, métodos de autenticação e permissões de acesso em uma hierarquia de três níveis de **Scopes**: o escopo raiz **`global`**, um ou mais escopos de **Organização (`org`)** sob `global` e múltiplos escopos de **Projeto (`project`)** dentro de cada organização.

## Por que importa
Em uma empresa com várias unidades de negócio e dezenas de equipes de produto, delegar a administração de catálogos de servidores e targets para cada equipe sem dar permissão global de superusuário requer partição hierárquica.

## Como funciona
Tipicamente, os **Auth Methods** (como OIDC com Okta/Entra ID) e usuários são definidos no escopo `global` ou `org`, enquanto os **Host Catalogs**, **Credential Stores** e **Targets** pertencem a cada `project`. As permissões são atribuídas por objetos `Role` contendo strings concisas de `grants` (ex.: `ids=*;type=target;actions=list,authorize-session`).

## Exemplo
```bash
boundary scopes list
boundary roles create \
  -scope-id p_1234567890 \
  -name "sre-connect-role"
boundary roles add-grants \
  -id r_1234567890 \
  -grant "ids=*;type=target;actions=list,read,authorize-session"
```

## Limites e trade-offs
Por segurança *deny-by-default*, um usuário autenticado no Boundary não enxerga nem pode conectar-se a nenhum `Target` até que sua identidade ou *Managed Group* OIDC seja associado como `principal` a uma `Role` com a ação `authorize-session`.

## Como verificar
Execute `boundary scopes list -recursive` para visualizar a árvore completa de escopos `global` -> `org` -> `project`.

## Conexões
- [[boundary-arquitetura-identity-based-access-controller-worker-postgresql-kms]] — Veja também: HashiCorp Boundary: arquitetura de acesso privilegiado baseado em identidade com `Controller`, `Worker`, PostgreSQL e KMS.
- [[boundary-kms-key-hierarchy-root-worker-auth-recovery-vault-transit]] — Veja também: HashiCorp Boundary KMS: arquitetura de chaves (`root`, `worker-auth`, `recovery`, `config`) com Cloud KMS ou Vault Transit.

## Fontes
- [HashiCorp Boundary GitHub — README.md (Identity-Aware Proxy, Controller & Workers, PostgreSQL & KMS Requirements, Dev Mode & CLI)](https://raw.githubusercontent.com/hashicorp/boundary/main/README.md) — README oficial do hashicorp/boundary detalhando os componentes Controller e Worker, requisitos de banco SQL e KMS, hierarquia de Scopes e boundary connect; consultado em 2026-10-03.
- [HashiCorp Developer — What is Boundary? (Core Workflow, OIDC Authentication, Vault Credential Brokering/Injection, Multi-Hop & Session Recording)](https://developer.hashicorp.com/boundary/docs/what-is-boundary) — Documentação oficial do HashiCorp Boundary cobrindo acesso just-in-time sem agente, credenciais dinâmicas via Vault, sessões transparentes e gravação BSR; consultado em 2026-10-03.
- [HashiCorp Boundary — Official GitHub Repository](https://github.com/hashicorp/boundary) — Repositório oficial do HashiCorp Boundary; consultado em 2026-10-03.
