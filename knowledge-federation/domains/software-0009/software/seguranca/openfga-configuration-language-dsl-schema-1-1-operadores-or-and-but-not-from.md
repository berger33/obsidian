---
id: software.seguranca.tranche01.000063
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

# OpenFGA Configuration Language (DSL `schema 1.1`): relações diretas, herança hierárquica (`from`) e operadores `or`, `and` e `but not`

## Em uma frase
O OpenFGA oferece uma **DSL declarativa (`model schema 1.1`)** — suportada na extensão VS Code e na CLI `fga` e compilada para o formato JSON da API — onde cada `type` declara suas `relations` usando restrições explícitas de tipo (`[user, team#member]`), operadores de conjunto (**`or`** união, **`and`** interseção, **`but not`** exclusão) e travessia de grafo (**`from`**).

## Por que importa
Imagine precisar expressar duas regras reais de segurança: 1) "quem é `viewer` da pasta pai (`parent`) é automaticamente `viewer` do documento (`viewer from parent`)"; e 2) "um usuário pode ver o documento se for `viewer`, **exceto se** estiver na relação `blocked` (`viewer but not blocked`)".

## Como funciona
Na DSL `schema 1.1` do OpenFGA, essas duas regras escrevem-se em três linhas legíveis por humanos e auditáveis em Pull Requests, sendo versionadas de forma imutável (cada `POST /stores/{store_id}/authorization-models` gera um novo `authorization_model_id` ULID imutável)!

## Exemplo
```text
model
  schema 1.1

type user

type folder
  relations
    define viewer: [user]

type document
  relations
    define parent: [folder]
    define blocked: [user]
    define editor: [user]
    define viewer: ([user] or editor or viewer from parent) but not blocked
```

## Limites e trade-offs
Em produção, fixe sempre o **`authorization_model_id`** explícito nas chamadas da aplicação (`Check`, `ListObjects`), para que a criação de um modelo novo em teste não altere o comportamento das instâncias em execução antes do rollout.

## Como verificar
Valide e converta um arquivo `.fga` para JSON usando a CLI oficial: `fga model transform --file model.fga`.

## Conexões
- [[openfga-conceitos-fundamentais-store-type-object-user-relation-tuple]] — Veja também: OpenFGA Conceitos Fundamentais: `Store`, `Type`, `Object`, `User` (`userset` e wildcard `*`), `Relation` e `Relationship Tuple`.
- [[openfga-abac-conditions-cel-contextual-tuples-atributos-tempo-execucao]] — Veja também: OpenFGA ABAC Híbrido: combinação de grafos ReBAC com `Conditions` (Google CEL) e `Contextual Tuples`.

## Fontes
- [OpenFGA GitHub — README.md (CNCF Incubating Zanzibar Engine, Docker/CLI Quickstart, Production Storage, SLSA Level 3 & Official SDKs)](https://openfga.dev/docs/concepts) — README oficial do openfga/openfga detalhando execução via Docker e binário, migrações para PostgreSQL/MySQL, nota sobre Unix Domain Socket em /tmp e ferramentas do ecossistema; consultado em 2026-10-03.
- [OpenFGA Official Documentation — Core Concepts (Stores, Types, Objects, Users/Usersets, Relations, Authorization Models, Tuples & Queries)](https://raw.githubusercontent.com/openfga/openfga/main/README.md) — Documentação oficial de conceitos do OpenFGA explicando modelagem ReBAC/ABAC, imutabilidade de modelos, operadores de conjunto e semântica das APIs Check, ListObjects, ListUsers e Expand; consultado em 2026-10-03.
- [OpenFGA — Official GitHub Repository (CNCF)](https://github.com/openfga/openfga) — Repositório oficial Apache-2.0 do OpenFGA; consultado em 2026-10-03.
