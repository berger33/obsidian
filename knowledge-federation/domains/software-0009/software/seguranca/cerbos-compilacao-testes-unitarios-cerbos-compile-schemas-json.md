---
id: software.seguranca.tranche01.000087
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

# Cerbos `cerbos compile` e Validação de Schemas: testes unitários de políticas e checagem de tipos de atributos (`schemas`)

## Em uma frase
A CLI **`cerbos compile`** valida a sintaxe de todas as políticas, verifica referências de atributos contra **JSON Schemas** declarados na política (`schemas.principalSchema` e `schemas.resourceSchema`) e executa toda a suíte de **testes unitários de políticas** (`*_test.yaml`) em milissegundos.

## Por que importa
Um erro de digitação no nome de um atributo dentro de uma expressão CEL (`request.resource.attr.publci == true` em vez de `public`) passaria despercebido até a produção se não houver validação de schema e testes unitários no CI.

## Como funciona
Anexando `schemas` à sua `resourcePolicy` e mantendo uma matriz de testes `*_test.yaml` que cruza `principals`, `resources` e `actions` esperadas (`EFFECT_ALLOW` / `EFFECT_DENY`), o comando `cerbos compile` barra qualquer erro de tipo ou regressão lógica durante o Pull Request.

## Exemplo
```yaml
name: "Album Policy Test Suite"
description: "Verifica acesso do dono, usuários comuns e moderadores"
principals:
  alicia:
    id: alicia
    roles: ["user"]
resources:
  alicia_private_album:
    id: XX125
    kind: "album:object"
    attr:
      owner: alicia
      public: false
tests:
  - name: "Dona pode visualizar e deletar seu próprio álbum privado"
    input:
      principals: [alicia]
      resources: [alicia_private_album]
      actions: [view, delete]
    expected:
      - principal: alicia
        resource: alicia_private_album
        actions:
          view: EFFECT_ALLOW
          delete: EFFECT_ALLOW
```

## Limites e trade-offs
Execute `cerbos compile --verbose ./policies` na sua pipeline de CI/CD para exigir 100% de aprovação nos testes antes de distribuir as políticas aos PDPs.

## Como verificar
Rode `cerbos compile ./policies` localmente a cada alteração em arquivos YAML de política.

## Conexões
- [[cerbos-scoped-policies-hierarquia-multi-tenant-heranca-escopos]] — Veja também: Cerbos Scoped Policies: herança hierárquica de políticas para SaaS multi-tenant (`acme.corp.uk`) sem duplicar regras.
- [[cerbos-auxdata-jwt-verificacao-claims-contexto-criptografico]] — Veja também: Cerbos `auxData` e Verificação Nativa de JWT: uso de claims autenticadas do token diretamente nas expressões de política.

## Fontes
- [Cerbos GitHub — README.md (Stateless Policy Decision Point, CheckResources & PlanResources APIs, Derived Roles, Deployment Topologies & cerbos compile)](https://raw.githubusercontent.com/cerbos/cerbos/main/README.md) — README oficial do cerbos/cerbos documentando a arquitetura stateless do PDP, exemplos de políticas YAML, avaliação em lote, geração de Query Plan e execução via container/sidecar; consultado em 2026-10-03.
- [Cerbos Official Documentation — Policies Overview (Resource, Derived Roles, Principal, Role Policies, Exported Variables/Constants & Scoped Policies)](https://docs.cerbos.dev/cerbos/latest/policies/index.html) — Documentação oficial de políticas do Cerbos detalhando os 6 tipos de política YAML, escopos hierárquicos multi-tenant, condições CEL, schemas e auditoria de decisões; consultado em 2026-10-03.
- [Cerbos — Official GitHub Repository](https://github.com/cerbos/cerbos) — Repositório oficial Apache-2.0 do Cerbos PDP; consultado em 2026-10-03.
