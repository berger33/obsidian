---
id: software.seguranca.tranche01.000061
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
fontes: ["https://raw.githubusercontent.com/openfga/openfga/main/README.md", "https://openfga.dev/docs/concepts", "https://github.com/openfga/openfga"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# OpenFGA: arquitetura CNCF Incubating do motor de autorização ReBAC/ABAC de alta performance inspirado no Google Zanzibar

## Em uma frase
O **OpenFGA** (projeto **CNCF Incubating** criado originalmente pela Auth0/Okta sob licença Apache 2.0 e publicado com proveniência **SLSA Nível 3**) é um motor de autorização e permissões de granularidade fina (*Fine-Grained Authorization — FGA*) inspirado no artigo **Google Zanzibar**, combinando **ReBAC (*Relationship-Based Access Control*)**, **RBAC** e **ABAC** (via *Contextual Tuples* e *Conditions* CEL).

## Por que importa
Sistemas RBAC tradicionais baseados apenas em listas de papéis estáticos no token JWT (`role: editor`) quebram rapidamente quando a aplicação precisa responder se a usuária `anne` pode editar o `document:roadmap` porque ela pertence ao time `engineering`, que tem permissão na pasta `folder:product`, que é pai do documento.

## Como funciona
No OpenFGA, a aplicação consulta APIs HTTP ou gRPC ultra-rápidas (`Check`, `ListObjects`, `ListUsers`, `Expand`) contra um **Store** apoiado por **PostgreSQL**, **MySQL** ou **SQLite** (ou *In-Memory* para testes locais), onde o estado de autorização é determinado pela combinação de um **Authorization Model** imutável com **Relationship Tuples** dinâmicas.

## Exemplo
```bash
# Subindo o OpenFGA localmente em Docker para desenvolvimento e criando um Store via API HTTP:
docker run -d --name openfga -p 8080:8080 -p 3000:3000 openfga/openfga run

curl -sS -X POST 'http://localhost:8080/stores' \
  -H 'Content-Type: application/json' \
  -d '{"name": "openfga-demo"}'
```

## Limites e trade-offs
Conforme alertado no README oficial do OpenFGA, o storage padrão **in-memory** do comando `openfga run` é efêmero e destinado exclusivamente a avaliação local/testes; em produção, configure sempre PostgreSQL ou MySQL com réplicas de leitura.

## Como verificar
Execute `curl -sS http://localhost:8080/healthz` para verificar a saúde do servidor OpenFGA.

## Conexões
- [[openfga-conceitos-fundamentais-store-type-object-user-relation-tuple]] — Veja também: OpenFGA Conceitos Fundamentais: `Store`, `Type`, `Object`, `User` (`userset` e wildcard `*`), `Relation` e `Relationship Tuple`.

## Fontes
- [OpenFGA GitHub — README.md (CNCF Incubating Zanzibar Engine, Docker/CLI Quickstart, Production Storage, SLSA Level 3 & Official SDKs)](https://raw.githubusercontent.com/openfga/openfga/main/README.md) — README oficial do openfga/openfga detalhando execução via Docker e binário, migrações para PostgreSQL/MySQL, nota sobre Unix Domain Socket em /tmp e ferramentas do ecossistema; consultado em 2026-10-03.
- [OpenFGA Official Documentation — Core Concepts (Stores, Types, Objects, Users/Usersets, Relations, Authorization Models, Tuples & Queries)](https://openfga.dev/docs/concepts) — Documentação oficial de conceitos do OpenFGA explicando modelagem ReBAC/ABAC, imutabilidade de modelos, operadores de conjunto e semântica das APIs Check, ListObjects, ListUsers e Expand; consultado em 2026-10-03.
- [OpenFGA — Official GitHub Repository (CNCF)](https://github.com/openfga/openfga) — Repositório oficial Apache-2.0 do OpenFGA; consultado em 2026-10-03.
