---
id: software.seguranca.tranche01.000076
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
fontes: ["https://raw.githubusercontent.com/authzed/spicedb/main/README.md", "https://authzed.com/docs/spicedb/concepts/schema", "https://github.com/authzed/spicedb"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# SpiceDB Índices Reversos (`LookupResources` e `LookupSubjects`): listagem eficiente de recursos acessíveis e auditoria de sujeitos

## Em uma frase
Além de `CheckPermission`, a API do SpiceDB fornece duas consultas de índice reverso em streaming: **`LookupResources`** ("quais recursos do tipo `document` o sujeito `user:anne` tem permissão `view`?") e **`LookupSubjects`** ("quais sujeitos do tipo `user` possuem a permissão `edit` no recurso `document:roadmap`?").

## Por que importa
Para listar os documentos de um usuário ou auditar todos os usuários com acesso administrativo a um projeto, varrer todos os registros do banco da aplicação um por um chamando `CheckPermission` não escala.

## Como funciona
O SpiceDB caminha o grafo de relacionamentos de forma reversa e paralela (distribuída entre os nós do cluster via *dispatching* consistente por hash), emitindo os IDs dos recursos ou sujeitos autorizados via stream gRPC com suporte a cursores de paginação.

## Exemplo
```bash
# Listando todos os documentos que user:anne pode visualizar (LookupResources):
zed permission lookup-resources document view user:anne

# Listando todos os usuários que podem editar o document:roadmap (LookupSubjects):
zed permission lookup-subjects document:roadmap edit user
```

## Limites e trade-offs
Quando um `LookupSubjects` ou `LookupResources` atravessa um relacionamento condicional (`caveat`) cujo contexto não foi resolvido, o item retornado inclui o status condicional (`PERMISSIONSHEP_CONDITIONAL`) indicando a caveat pendente.

## Como verificar
Teste ambas as consultas reversas na CLI com `zed permission lookup-resources` e `zed permission lookup-subjects`.

## Conexões
- [[spicedb-consistencia-zedtoken-zookies-at-least-as-fresh-new-enemy]] — Veja também: SpiceDB Consistência Global e `ZedToken`: prevenção do *New Enemy Problem* com `at_least_as_fresh`, `minimize_latency` e `fully_consistent`.
- [[spicedb-validacao-testes-schema-zed-validate-assertions-ci]] — Veja também: SpiceDB Validação e Testes em CI/CD (`zed validate`): arquivos YAML de schema, relacionamentos de teste, `assertions` e `expected_relations`.

## Fontes
- [AuthZed SpiceDB GitHub — README.md (Distributed Permissions Database, Zanzibar Architecture, Consistency Modes, Datastores & zed CLI)](https://raw.githubusercontent.com/authzed/spicedb/main/README.md) — README oficial do authzed/spicedb detalhando a arquitetura do banco de permissões, garantias de consistência por requisição, motores de armazenamento e execução em Kubernetes; consultado em 2026-10-03.
- [AuthZed SpiceDB Official Documentation — Schema Language Reference (Definitions, Relations vs Permissions, +, &, -, -> Operators, Precedence & Caveats)](https://authzed.com/docs/spicedb/concepts/schema) — Referência oficial da linguagem de schema do SpiceDB cobrindo definitions, subject relations, wildcards, operadores de conjunto, alerta de precedência do operador + e caveats CEL; consultado em 2026-10-03.
- [AuthZed SpiceDB — Official GitHub Repository](https://github.com/authzed/spicedb) — Repositório oficial Apache-2.0 do AuthZed SpiceDB; consultado em 2026-10-03.
