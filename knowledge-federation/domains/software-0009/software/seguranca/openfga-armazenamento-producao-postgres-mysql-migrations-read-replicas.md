---
id: software.seguranca.tranche01.000068
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

# OpenFGA em Produção (`openfga migrate` e Storage Engines): operação com PostgreSQL/MySQL, conexões e Unix Domain Socket

## Em uma frase
Para rodar o OpenFGA em produção com alta disponibilidade e persistência durável, o servidor suporta os motores de banco de dados **`postgres`** e **`mysql`** (além de `sqlite` em beta), exigindo a execução prévia de migrações de schema com o comando **`openfga migrate`** antes de iniciar as réplicas do servidor.

## Por que importa
Rodar o binário `openfga run` sem configurar `--datastore-engine` utiliza o engine `memory`, que perde 100% dos Stores, modelos e tuplas assim que o Pod reinicia.

## Como funciona
Em um cluster Kubernetes (usando o Helm chart oficial no Artifact HUB `openfga/openfga`), um Job `initContainer` ou hook de pre-upgrade executa `openfga migrate --datastore-engine postgres --datastore-uri ...`, e os Pods do Deployment rodam `openfga run` com pool de conexões ajustado (`--datastore-max-open-conns`).

## Exemplo
```bash
# 1. Executando as migrações de banco de dados no PostgreSQL antes de subir o servidor:
openfga migrate \
  --datastore-engine postgres \
  --datastore-uri "postgres://fga_user:secret@pg-primary.internal:5432/openfga?sslmode=require"

# 2. Iniciando o servidor OpenFGA conectado ao PostgreSQL com autenticação Preshared Key:
openfga run \
  --datastore-engine postgres \
  --datastore-uri "postgres://fga_user:secret@pg-primary.internal:5432/openfga?sslmode=require" \
  --authn-method preshared \
  --authn-preshared-keys "${OPENFGA_API_TOKEN}"
```

## Limites e trade-offs
Conforme documentado na nota oficial da seção *Docker* do README do OpenFGA: quando o servidor HTTP está habilitado, ele tenta conectar-se internamente ao servidor gRPC via **Unix Domain Socket (UDS)** em `/tmp`; por isso, se você rodar o container com filesystem raiz somente-leitura (`--read-only` / `readOnlyRootFilesystem: true`), adicione obrigatoriamente um volume `--tmpfs /tmp` (`emptyDir` em `/tmp`)!

## Como verificar
Verifique o status de prontidão do servidor e do datastore consultando a probe gRPC ou HTTP do OpenFGA.

## Conexões
- [[openfga-modular-models-fga-mod-divisao-dominios-equipes]] — Veja também: OpenFGA Modular Models (`fga.mod`): divisão de modelos de autorização complexos em módulos por equipe e domínio.
- [[openfga-performance-caching-consistency-higher-consistency-minimize-latency]] — Veja também: OpenFGA Consistência e Cache (`ConsistencyPreference`): equilíbrio entre `MINIMIZE_LATENCY` e `HIGHER_CONSISTENCY` (*Zookie* / Problema do Novo Inimigo).

## Fontes
- [OpenFGA GitHub — README.md (CNCF Incubating Zanzibar Engine, Docker/CLI Quickstart, Production Storage, SLSA Level 3 & Official SDKs)](https://raw.githubusercontent.com/openfga/openfga/main/README.md) — README oficial do openfga/openfga detalhando execução via Docker e binário, migrações para PostgreSQL/MySQL, nota sobre Unix Domain Socket em /tmp e ferramentas do ecossistema; consultado em 2026-10-03.
- [OpenFGA Official Documentation — Core Concepts (Stores, Types, Objects, Users/Usersets, Relations, Authorization Models, Tuples & Queries)](https://openfga.dev/docs/concepts) — Documentação oficial de conceitos do OpenFGA explicando modelagem ReBAC/ABAC, imutabilidade de modelos, operadores de conjunto e semântica das APIs Check, ListObjects, ListUsers e Expand; consultado em 2026-10-03.
- [OpenFGA — Official GitHub Repository (CNCF)](https://github.com/openfga/openfga) — Repositório oficial Apache-2.0 do OpenFGA; consultado em 2026-10-03.
