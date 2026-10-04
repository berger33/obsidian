---
id: software.seguranca.tranche01.000083
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

# Cerbos `Derived Roles`: evolução limpa de RBAC estático para ABAC contextual usando expressões CEL

## Em uma frase
As **`derivedRoles`** são o mecanismo central do Cerbos para evoluir um sistema RBAC tradicional (onde o provedor de identidade OIDC/Keycloak emite apenas papéis amplos como `user`, `manager` ou `moderator`) para **ABAC contextual** sem precisar criar centenas de grupos no IdP.

## Por que importa
Se uma empresa tem 200 filiais, criar 200 grupos no Active Directory (`manager_filial_001` ... `manager_filial_200`) é ingovernável; com um **Derived Role**, o usuário tem apenas o papel `manager` e o Cerbos deriva dinamicamente o papel `branch_manager` se `request.principal.attr.branch_id == request.resource.attr.branch_id`!

## Como funciona
Uma definição de `derivedRoles` especifica `parentRoles` (os papéis base exigidos no principal) e uma `condition` (`match.expr` escrita em Google CEL) que avalia atributos de `request.principal.attr`, `request.resource.attr` e `request.auxData` (como claims de um JWT).

## Exemplo
```yaml
apiVersion: "api.cerbos.dev/v1"
derivedRoles:
  name: common_roles
  definitions:
    - name: owner
      parentRoles: ["user"]
      condition:
        match:
          expr: request.resource.attr.owner == request.principal.id

    - name: branch_manager
      parentRoles: ["manager"]
      condition:
        match:
          expr: request.resource.attr.branch_id == request.principal.attr.branch_id
```

## Limites e trade-offs
Um `derivedRole` só é ativado durante a avaliação de uma `resourcePolicy` que o importe explicitamente em `importDerivedRoles` e se o principal possuir ao menos um dos `parentRoles` listados.

## Como verificar
Teste a ativação dos seus `derivedRoles` com `cerbos compile --tests ./tests ./policies` habilitando traces de avaliação.

## Conexões
- [[cerbos-seis-tipos-politicas-resource-derived-roles-principal-role-export]] — Veja também: Cerbos Taxonomia das 6 Políticas: `Resource Policies`, `Derived Roles`, `Principal Policies`, `Role Policies`, `Exported Variables` e `Constants`.
- [[cerbos-api-checkresources-batch-avaliacao-multiplos-recursos-acoes]] — Veja também: Cerbos API `CheckResources`: avaliação em lote de múltiplos recursos e múltiplas ações em uma única requisição.

## Fontes
- [Cerbos GitHub — README.md (Stateless Policy Decision Point, CheckResources & PlanResources APIs, Derived Roles, Deployment Topologies & cerbos compile)](https://raw.githubusercontent.com/cerbos/cerbos/main/README.md) — README oficial do cerbos/cerbos documentando a arquitetura stateless do PDP, exemplos de políticas YAML, avaliação em lote, geração de Query Plan e execução via container/sidecar; consultado em 2026-10-03.
- [Cerbos Official Documentation — Policies Overview (Resource, Derived Roles, Principal, Role Policies, Exported Variables/Constants & Scoped Policies)](https://docs.cerbos.dev/cerbos/latest/policies/index.html) — Documentação oficial de políticas do Cerbos detalhando os 6 tipos de política YAML, escopos hierárquicos multi-tenant, condições CEL, schemas e auditoria de decisões; consultado em 2026-10-03.
- [Cerbos — Official GitHub Repository](https://github.com/cerbos/cerbos) — Repositório oficial Apache-2.0 do Cerbos PDP; consultado em 2026-10-03.
