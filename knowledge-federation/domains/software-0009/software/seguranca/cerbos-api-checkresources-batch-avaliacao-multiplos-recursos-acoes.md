---
id: software.seguranca.tranche01.000084
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

# Cerbos API `CheckResources`: avaliação em lote de múltiplos recursos e múltiplas ações em uma única requisição

## Em uma frase
A API primária de decisão do Cerbos PDP — **`CheckResources`** (`POST /api/check/resources` ou método gRPC equivalente) — recebe um `principal`, um conjunto de até dezenas de objetos em `resources[]` e a lista de `actions[]` desejadas para cada recurso, retornando um mapa determinístico de decisões (`EFFECT_ALLOW` ou `EFFECT_DENY`) para cada par `(resource, action)`.

## Por que importa
Sem suporte nativo a lotes na API de autorização, renderizar uma tabela com 25 faturas mostrando os botões `view`, `edit`, `approve` e `delete` exigiria 100 requisições HTTP separadas ao PDP.

## Como funciona
Com `CheckResources`, a aplicação envia os 25 objetos (apenas com o `id`, `kind` e o dicionário enxuto `attr` relevante para a política, como `owner`, `status` e `amount`) em um único payload e recebe a matriz completa de permissões em poucos milissegundos.

## Exemplo
```bash
curl -sS "http://localhost:3592/api/check/resources?pretty" -d '{
  "requestId": "req-01",
  "principal": {
    "id": "alicia",
    "roles": ["user"],
    "attr": { "department": "finance" }
  },
  "resources": [
    {
      "actions": ["view", "delete"],
      "resource": {
        "id": "XX125",
        "kind": "album:object",
        "attr": { "owner": "alicia", "public": false, "flagged": false }
      }
    }
  ]
}'
```

## Limites e trade-offs
Adicione `"includeMeta": true` no payload do `CheckResources` durante o desenvolvimento ou auditoria para que a resposta informe exatamente qual regra e qual política (`matchedPolicy`, `matchedScope`) produziu cada decisão.

## Como verificar
Inspecione o campo `results[].actions` na resposta JSON confirmando `"EFFECT_ALLOW"` ou `"EFFECT_DENY"`.

## Conexões
- [[cerbos-derived-roles-evolucao-rbac-para-abac-condicoes-cel]] — Veja também: Cerbos `Derived Roles`: evolução limpa de RBAC estático para ABAC contextual usando expressões CEL.
- [[cerbos-api-planresources-query-plan-ast-filtros-banco-orm]] — Veja também: Cerbos API `PlanResources` (*Query Plan*): geração de AST de filtros (`CONDITIONAL`) para consultas diretas no banco de dados (Prisma/SQLAlchemy/GORM).

## Fontes
- [Cerbos GitHub — README.md (Stateless Policy Decision Point, CheckResources & PlanResources APIs, Derived Roles, Deployment Topologies & cerbos compile)](https://raw.githubusercontent.com/cerbos/cerbos/main/README.md) — README oficial do cerbos/cerbos documentando a arquitetura stateless do PDP, exemplos de políticas YAML, avaliação em lote, geração de Query Plan e execução via container/sidecar; consultado em 2026-10-03.
- [Cerbos Official Documentation — Policies Overview (Resource, Derived Roles, Principal, Role Policies, Exported Variables/Constants & Scoped Policies)](https://docs.cerbos.dev/cerbos/latest/policies/index.html) — Documentação oficial de políticas do Cerbos detalhando os 6 tipos de política YAML, escopos hierárquicos multi-tenant, condições CEL, schemas e auditoria de decisões; consultado em 2026-10-03.
- [Cerbos — Official GitHub Repository](https://github.com/cerbos/cerbos) — Repositório oficial Apache-2.0 do Cerbos PDP; consultado em 2026-10-03.
