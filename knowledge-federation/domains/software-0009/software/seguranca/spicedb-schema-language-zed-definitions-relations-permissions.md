---
id: software.seguranca.tranche01.000072
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
fontes: ["https://authzed.com/docs/spicedb/concepts/schema", "https://raw.githubusercontent.com/authzed/spicedb/main/README.md", "https://github.com/authzed/spicedb"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# SpiceDB Schema Language (`.zed`): separação estrita entre `definition`, `relation` (substantivos) e `permission` (verbos computados)

## Em uma frase
Na linguagem de schema do SpiceDB (arquivos **`.zed`**), há uma distinção fundamental e estrita entre **`relation`** (que define como dois objetos/sujeitos podem se relacionar e onde os dados são efetivamente gravados, nomeada como **substantivo**: `reader`, `writer`, `member`) e **`permission`** (que define um conjunto **computado** de sujeitos que podem realizar uma ação, nomeada como **verbo**: `view`, `edit`, `delete`).

## Por que importa
Conforme documentado na referência oficial do Schema do SpiceDB, **você nunca pode gravar um relacionamento referenciando uma `permission`** — você só grava relacionamentos referenciando uma `relation`. Isso permite alterar a regra de cálculo de uma `permission` a qualquer momento sem precisar migrar milhões de linhas no banco de dados!

## Como funciona
Além disso, as `definitions` suportam prefixos de namespace (ex.: `definition docs/document {}`, `definition iam/user {}`) e relações para conjuntos de sujeitos (*Subject Relations*, ex.: `relation owner: user | group#member`).

## Exemplo
```zed
definition iam/user {}

definition iam/group {
  relation member: iam/user
}

definition docs/document {
  relation writer: iam/user | iam/group#member
  relation reader: iam/user | iam/group#member

  permission edit = writer
  permission view = reader + writer
}
```

## Limites e trade-offs
Ao usar **Wildcards** (`relation viewer: user | user:*`) para conceder acesso público (`document:public#viewer@user:*`), siga o alerta oficial da documentação: **nunca** conceda suporte a wildcard em relações associadas a permissões de escrita!

## Como verificar
Aplique e valide o schema com `zed schema write schema.zed` e `zed schema read`.

## Conexões
- [[spicedb-arquitetura-authzed-google-zanzibar-permissions-database]] — Veja também: SpiceDB: arquitetura do banco de dados de permissões distribuído inspirado no Google Zanzibar (`spicedb` e CLI `zed`).
- [[spicedb-operadores-permissao-union-intersection-exclusion-arrows-precedencia]] — Veja também: SpiceDB Operações de Permissão (`+`, `&`, `-` e `->`): travessia de hierarquias com Arrows e a armadilha de precedência do `+`.

## Fontes
- [AuthZed SpiceDB GitHub — README.md (Distributed Permissions Database, Zanzibar Architecture, Consistency Modes, Datastores & zed CLI)](https://authzed.com/docs/spicedb/concepts/schema) — README oficial do authzed/spicedb detalhando a arquitetura do banco de permissões, garantias de consistência por requisição, motores de armazenamento e execução em Kubernetes; consultado em 2026-10-03.
- [AuthZed SpiceDB Official Documentation — Schema Language Reference (Definitions, Relations vs Permissions, +, &, -, -> Operators, Precedence & Caveats)](https://raw.githubusercontent.com/authzed/spicedb/main/README.md) — Referência oficial da linguagem de schema do SpiceDB cobrindo definitions, subject relations, wildcards, operadores de conjunto, alerta de precedência do operador + e caveats CEL; consultado em 2026-10-03.
- [AuthZed SpiceDB — Official GitHub Repository](https://github.com/authzed/spicedb) — Repositório oficial Apache-2.0 do AuthZed SpiceDB; consultado em 2026-10-03.
