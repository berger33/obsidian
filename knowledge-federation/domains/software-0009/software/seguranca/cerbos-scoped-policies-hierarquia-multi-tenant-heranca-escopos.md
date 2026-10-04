---
id: software.seguranca.tranche01.000086
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
fontes: ["https://docs.cerbos.dev/cerbos/latest/policies/index.html", "https://raw.githubusercontent.com/cerbos/cerbos/main/README.md", "https://github.com/cerbos/cerbos"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Cerbos Scoped Policies: herança hierárquica de políticas para SaaS multi-tenant (`acme.corp.uk`) sem duplicar regras

## Em uma frase
Para aplicações SaaS multi-tenant onde clientes corporativos ou unidades regionais precisam de customizações específicas sobre as regras padrão, o Cerbos suporta **Scoped Policies (`scope: "acme.europe.uk"`)** com resolução hierárquica ponto-a-ponto.

## Por que importa
Copiar e colar o arquivo inteiro `expense_policy.yaml` para cada um dos 500 clientes SaaS quando apenas 3 clientes têm uma regra especial de aprovação tornaria a manutenção das políticas impossível.

## Como funciona
No Cerbos, quando a requisição informa `scope: "acme.europe.uk"`, o motor avalia a cadeia de escopos (`acme.europe.uk` -> `acme.europe` -> `acme` -> política raiz `""`), permitindo que um escopo filho adicione ou sobrescreva apenas a regra específica daquele tenant enquanto herda o restante da política base.

## Exemplo
```yaml
apiVersion: api.cerbos.dev/v1
resourcePolicy:
  resource: "expense:report"
  version: "default"
  scope: "acme.uk"
  scopePermissions: SCOPE_PERMISSIONS_OVERRIDE_PARENT
  rules:
    - actions: ["approve"]
      effect: EFFECT_ALLOW
      roles: ["finance_director"]
      condition:
        match:
          expr: request.resource.attr.amount <= 50000
```

## Limites e trade-offs
Escolha explicitamente `scopePermissions` entre `SCOPE_PERMISSIONS_OVERRIDE_PARENT` (o escopo filho pode permitir ou negar diretamente, caindo para o pai se nenhuma regra casar) e `SCOPE_PERMISSIONS_REQUIRE_PARENTAL_CONSENT_FOR_ALLOWS` (uma ação só é permitida se tanto o pai quanto o filho permitirem).

## Como verificar
Teste a resolução hierárquica de escopos usando `cerbos compile` com casos de teste para cada `scope`.

## Conexões
- [[cerbos-api-planresources-query-plan-ast-filtros-banco-orm]] — Veja também: Cerbos API `PlanResources` (*Query Plan*): geração de AST de filtros (`CONDITIONAL`) para consultas diretas no banco de dados (Prisma/SQLAlchemy/GORM).
- [[cerbos-compilacao-testes-unitarios-cerbos-compile-schemas-json]] — Veja também: Cerbos `cerbos compile` e Validação de Schemas: testes unitários de políticas e checagem de tipos de atributos (`schemas`).

## Fontes
- [Cerbos GitHub — README.md (Stateless Policy Decision Point, CheckResources & PlanResources APIs, Derived Roles, Deployment Topologies & cerbos compile)](https://docs.cerbos.dev/cerbos/latest/policies/index.html) — README oficial do cerbos/cerbos documentando a arquitetura stateless do PDP, exemplos de políticas YAML, avaliação em lote, geração de Query Plan e execução via container/sidecar; consultado em 2026-10-03.
- [Cerbos Official Documentation — Policies Overview (Resource, Derived Roles, Principal, Role Policies, Exported Variables/Constants & Scoped Policies)](https://raw.githubusercontent.com/cerbos/cerbos/main/README.md) — Documentação oficial de políticas do Cerbos detalhando os 6 tipos de política YAML, escopos hierárquicos multi-tenant, condições CEL, schemas e auditoria de decisões; consultado em 2026-10-03.
- [Cerbos — Official GitHub Repository](https://github.com/cerbos/cerbos) — Repositório oficial Apache-2.0 do Cerbos PDP; consultado em 2026-10-03.
