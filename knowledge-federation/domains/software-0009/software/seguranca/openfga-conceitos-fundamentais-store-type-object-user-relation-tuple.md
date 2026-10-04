---
id: software.seguranca.tranche01.000062
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
fontes: ["https://openfga.dev/docs/concepts", "https://raw.githubusercontent.com/openfga/openfga/main/README.md", "https://github.com/openfga/openfga"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# OpenFGA Conceitos Fundamentais: `Store`, `Type`, `Object`, `User` (`userset` e wildcard `*`), `Relation` e `Relationship Tuple`

## Em uma frase
Conforme a documentação oficial de conceitos do OpenFGA (`openfga.dev/docs/concepts`), todo o modelo de dados gira em torno de seis conceitos: **Store** (contêiner isolado de modelos e tuplas), **Type** (classe de objetos como `document` ou `folder`), **Object** (`type:id`, ex.: `document:roadmap`), **User** (sujeito que pode ser um usuário `user:anne`, outro objeto, um conjunto **`userset`** `organization:acme#member` ou todo mundo `user:*`), **Relation** e **Relationship Tuple** (`{user, relation, object}`).

## Por que importa
Compreender que um `User` em uma tupla do OpenFGA não precisa ser apenas uma pessoa física — podendo ser um **userset** (`team:secops#member`) ou outro objeto (`folder:root`) — é o que permite modelar hierarquias inteiras de grupos e pastas sem duplicar linhas no banco.

## Como funciona
Uma **Relationship Tuple** é o fato elementar persistido no Store, composto por `{ user: "user:anne", relation: "editor", object: "document:new-roadmap" }`. As tuplas não podem ser compartilhadas entre Stores diferentes; por isso, recomenda-se manter todos os dados que afetam uma decisão de autorização em um mesmo Store por ambiente (`dev`, `prod`).

## Exemplo
```json
{
  "writes": {
    "tuple_keys": [
      {
        "user": "user:anne",
        "relation": "editor",
        "object": "document:new-roadmap"
      },
      {
        "user": "organization:acme#member",
        "relation": "viewer",
        "object": "document:new-roadmap"
      }
    ]
  }
}
```

## Limites e trade-offs
Use a sintaxe de *type-bound public access* (`user:*`) com extrema cautela, restringindo-a nas definições de tipo apenas a relações de leitura (como `viewer: [user, user:*]`).

## Como verificar
Liste as tuplas gravadas em um Store usando a CLI oficial (`fga tuple read`) ou o endpoint `POST /stores/{store_id}/read`.

## Conexões
- [[openfga-arquitetura-cncf-google-zanzibar-rebac-abac-engine]] — Veja também: OpenFGA: arquitetura CNCF Incubating do motor de autorização ReBAC/ABAC de alta performance inspirado no Google Zanzibar.
- [[openfga-configuration-language-dsl-schema-1-1-operadores-or-and-but-not-from]] — Veja também: OpenFGA Configuration Language (DSL `schema 1.1`): relações diretas, herança hierárquica (`from`) e operadores `or`, `and` e `but not`.

## Fontes
- [OpenFGA GitHub — README.md (CNCF Incubating Zanzibar Engine, Docker/CLI Quickstart, Production Storage, SLSA Level 3 & Official SDKs)](https://openfga.dev/docs/concepts) — README oficial do openfga/openfga detalhando execução via Docker e binário, migrações para PostgreSQL/MySQL, nota sobre Unix Domain Socket em /tmp e ferramentas do ecossistema; consultado em 2026-10-03.
- [OpenFGA Official Documentation — Core Concepts (Stores, Types, Objects, Users/Usersets, Relations, Authorization Models, Tuples & Queries)](https://raw.githubusercontent.com/openfga/openfga/main/README.md) — Documentação oficial de conceitos do OpenFGA explicando modelagem ReBAC/ABAC, imutabilidade de modelos, operadores de conjunto e semântica das APIs Check, ListObjects, ListUsers e Expand; consultado em 2026-10-03.
- [OpenFGA — Official GitHub Repository (CNCF)](https://github.com/openfga/openfga) — Repositório oficial Apache-2.0 do OpenFGA; consultado em 2026-10-03.
