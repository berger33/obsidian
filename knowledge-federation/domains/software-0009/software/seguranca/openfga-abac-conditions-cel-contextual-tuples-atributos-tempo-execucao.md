---
id: software.seguranca.tranche01.000064
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

# OpenFGA ABAC Híbrido: combinação de grafos ReBAC com `Conditions` (Google CEL) e `Contextual Tuples`

## Em uma frase
Para unir o poder de relacionamentos (**ReBAC**) com regras baseadas em atributos dinâmicos de contexto (**ABAC** — como janelas de horário, endereço IP, departamento ou limite financeiro), o OpenFGA suporta **Conditional Relationship Tuples** escritas em **Google CEL (*Common Expression Language*)** e **Contextual Tuples** enviadas em memória junto com a requisição `Check`.

## Por que importa
Às vezes uma permissão de acesso temporário de suporte (`support_agent`) só deve valer se `current_time < grant_expiration` e se o IP de origem pertencer à VPN corporativa — dados que mudam a cada requisição.

## Como funciona
No modelo `.fga`, você define um bloco `condition non_expired_grant(current_time: timestamp, expires_at: timestamp) { current_time < expires_at }` e declara `define viewer: [user with non_expired_grant]`. Ao gravar a tupla, você anexa o parâmetro `expires_at`, e na chamada `Check` a aplicação passa `context: {"current_time": "2026-10-03T18:00:00Z"}`!

## Exemplo
```text
model
  schema 1.1

type user

type document
  relations
    define viewer: [user with non_expired_grant]

condition non_expired_grant(current_time: timestamp, expires_at: timestamp) {
  current_time < expires_at
}
```

## Limites e trade-offs
Já as **Contextual Tuples** (`contextual_tuples` enviadas dentro do payload do `Check`) não são gravadas no banco: elas permitem enviar fatos já presentes no JWT da requisição (como a organização do usuário) sem precisar sincronizá-los previamente no Store.

## Como verificar
Teste expressões `condition` CEL usando testes declarativos `.fga.yaml` com `fga model test`.

## Conexões
- [[openfga-configuration-language-dsl-schema-1-1-operadores-or-and-but-not-from]] — Veja também: OpenFGA Configuration Language (DSL `schema 1.1`): relações diretas, herança hierárquica (`from`) e operadores `or`, `and` e `but not`.
- [[openfga-queries-check-batchcheck-listobjects-listusers-expand]] — Veja também: OpenFGA APIs de Consulta: diferenças e casos de uso entre `Check`, `BatchCheck`, `ListObjects`, `ListUsers` e `Expand`.

## Fontes
- [OpenFGA GitHub — README.md (CNCF Incubating Zanzibar Engine, Docker/CLI Quickstart, Production Storage, SLSA Level 3 & Official SDKs)](https://openfga.dev/docs/concepts) — README oficial do openfga/openfga detalhando execução via Docker e binário, migrações para PostgreSQL/MySQL, nota sobre Unix Domain Socket em /tmp e ferramentas do ecossistema; consultado em 2026-10-03.
- [OpenFGA Official Documentation — Core Concepts (Stores, Types, Objects, Users/Usersets, Relations, Authorization Models, Tuples & Queries)](https://raw.githubusercontent.com/openfga/openfga/main/README.md) — Documentação oficial de conceitos do OpenFGA explicando modelagem ReBAC/ABAC, imutabilidade de modelos, operadores de conjunto e semântica das APIs Check, ListObjects, ListUsers e Expand; consultado em 2026-10-03.
- [OpenFGA — Official GitHub Repository (CNCF)](https://github.com/openfga/openfga) — Repositório oficial Apache-2.0 do OpenFGA; consultado em 2026-10-03.
