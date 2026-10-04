---
id: software.seguranca.tranche01.000077
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

# SpiceDB Validação e Testes em CI/CD (`zed validate`): arquivos YAML de schema, relacionamentos de teste, `assertions` e `expected_relations`

## Em uma frase
O comando **`zed validate`** permite validar estaticamente o schema `.zed` e executar uma suíte completa de testes unitários de autorização declarados em um arquivo YAML de validação (contendo `schema`, `relationships`, `assertions` de `assertTrue`/`assertFalse` e `validation` exaustiva de sujeitos esperados) sem precisar de servidor externo.

## Por que importa
Refatorar um schema `.zed` grande sem testes automatizados de `assertTrue` **e** `assertFalse` pode abrir brechas silenciosas onde um papel de leitor passa a herdar permissão de exclusão.

## Como funciona
No arquivo YAML passado para `zed validate`, a seção `assertions` verifica que permissões positivas (`assertTrue`) e negativas (`assertFalse`) sejam respeitadas, enquanto a seção `validation` garante a lista exata e completa de todos os sujeitos que possuem determinada permissão e como chegaram até ela.

## Exemplo
```yaml
schema: |
  definition user {}
  definition document {
    relation writer: user
    relation reader: user
    permission edit = writer
    permission view = reader + writer
  }
relationships: |
  document:doc1#writer@user:alice
  document:doc1#reader@user:bob
assertions:
  assertTrue:
    - "document:doc1#edit@user:alice"
    - "document:doc1#view@user:alice"
    - "document:doc1#view@user:bob"
  assertFalse:
    - "document:doc1#edit@user:bob"
```

## Limites e trade-offs
Inclua sempre casos explícitos em **`assertFalse`** nos seus arquivos de validação para testar limites de isolamento multi-tenant e usuários banidos.

## Como verificar
Execute `zed validate ./authz-tests.yaml` na sua pipeline de CI/CD a cada commit.

## Conexões
- [[spicedb-reverse-indexes-lookupresources-lookupsubjects-paginacao]] — Veja também: SpiceDB Índices Reversos (`LookupResources` e `LookupSubjects`): listagem eficiente de recursos acessíveis e auditoria de sujeitos.
- [[spicedb-datastores-postgres-cockroachdb-spanner-mysql-migrate]] — Veja também: SpiceDB Datastores de Produção e `spicedb migrate`: escolha entre `postgres`, `cockroachdb`, `spanner` e `mysql`.

## Fontes
- [AuthZed SpiceDB GitHub — README.md (Distributed Permissions Database, Zanzibar Architecture, Consistency Modes, Datastores & zed CLI)](https://raw.githubusercontent.com/authzed/spicedb/main/README.md) — README oficial do authzed/spicedb detalhando a arquitetura do banco de permissões, garantias de consistência por requisição, motores de armazenamento e execução em Kubernetes; consultado em 2026-10-03.
- [AuthZed SpiceDB Official Documentation — Schema Language Reference (Definitions, Relations vs Permissions, +, &, -, -> Operators, Precedence & Caveats)](https://authzed.com/docs/spicedb/concepts/schema) — Referência oficial da linguagem de schema do SpiceDB cobrindo definitions, subject relations, wildcards, operadores de conjunto, alerta de precedência do operador + e caveats CEL; consultado em 2026-10-03.
- [AuthZed SpiceDB — Official GitHub Repository](https://github.com/authzed/spicedb) — Repositório oficial Apache-2.0 do AuthZed SpiceDB; consultado em 2026-10-03.
