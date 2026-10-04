---
id: software.seguranca.tranche01.000085
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-01.md"
fontes: ["https://raw.githubusercontent.com/cerbos/cerbos/main/README.md", "https://docs.cerbos.dev/cerbos/latest/policies/index.html", "https://github.com/cerbos/cerbos"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Cerbos API `PlanResources` (*Query Plan*): geração de AST de filtros (`CONDITIONAL`) para consultas diretas no banco de dados (Prisma/SQLAlchemy/GORM)

## Em uma frase
Para responder à pergunta **"quais recursos do tipo X este principal pode acessar?"** sem buscar milhões de linhas do banco de dados da aplicação para a memória, o Cerbos oferece a API **`PlanResources`** (`POST /api/plan/resources`), que realiza avaliação parcial das políticas e retorna um **Query Plan (Árvore Sintática Abstrata — AST de condições)**.

## Por que importa
Em um banco SQL com 5 milhões de pedidos, é impossível ler os 5 milhões de linhas e enviá-los ao `CheckResources`; você precisa empurrar o filtro de autorização diretamente para a cláusula `WHERE` da query SQL/NoSQL.

## Como funciona
Ao chamar `PlanResources` informando apenas o `principal`, o `resource.kind` e a `action: "view"`, o Cerbos retorna um de três tipos de plano (`filter.kind`): 1) **`KIND_ALWAYS_ALLOWED`** (sem filtro extra no `WHERE`); 2) **`KIND_ALWAYS_DENIED`** (nem execute a query no banco); ou 3) **`KIND_CONDITIONAL`**, acompanhado da árvore lógica de condições (ex.: `request.resource.attr.public == true OR request.resource.attr.owner == "alicia"`), que os **Query Plan Adapters** oficiais (Prisma, SQLAlchemy, Drizzle, Mongoose, GORM) convertem automaticamente em cláusulas `WHERE` nativas do ORM!

## Exemplo
```bash
curl -sS "http://localhost:3592/api/plan/resources?pretty" -d '{
  "requestId": "plan-01",
  "action": "view",
  "principal": {
    "id": "alicia",
    "roles": ["user"]
  },
  "resource": {
    "kind": "album:object"
  }
}'
```

## Limites e trade-offs
O `PlanResources` mantém o Cerbos 100% stateless e elimina a necessidade de sincronizar seus dados de negócio para um banco de autorização externo.

## Como verificar
Verifique o campo `filter.kind` e a árvore `filter.condition` retornados pela chamada `POST /api/plan/resources`.

## Conexões
- [[cerbos-api-checkresources-batch-avaliacao-multiplos-recursos-acoes]] — Veja também: Cerbos API `CheckResources`: avaliação em lote de múltiplos recursos e múltiplas ações em uma única requisição.
- [[cerbos-scoped-policies-hierarquia-multi-tenant-heranca-escopos]] — Veja também: Cerbos Scoped Policies: herança hierárquica de políticas para SaaS multi-tenant (`acme.corp.uk`) sem duplicar regras.

## Fontes
- [Cerbos GitHub — README.md (Stateless Policy Decision Point, CheckResources & PlanResources APIs, Derived Roles, Deployment Topologies & cerbos compile)](https://raw.githubusercontent.com/cerbos/cerbos/main/README.md) — README oficial do cerbos/cerbos documentando a arquitetura stateless do PDP, exemplos de políticas YAML, avaliação em lote, geração de Query Plan e execução via container/sidecar; consultado em 2026-10-03.
- [Cerbos Official Documentation — Policies Overview (Resource, Derived Roles, Principal, Role Policies, Exported Variables/Constants & Scoped Policies)](https://docs.cerbos.dev/cerbos/latest/policies/index.html) — Documentação oficial de políticas do Cerbos detalhando os 6 tipos de política YAML, escopos hierárquicos multi-tenant, condições CEL, schemas e auditoria de decisões; consultado em 2026-10-03.
- [Cerbos — Official GitHub Repository](https://github.com/cerbos/cerbos) — Repositório oficial Apache-2.0 do Cerbos PDP; consultado em 2026-10-03.
