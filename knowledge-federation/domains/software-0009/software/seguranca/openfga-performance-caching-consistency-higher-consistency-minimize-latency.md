---
id: software.seguranca.tranche01.000069
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

# OpenFGA Consistência e Cache (`ConsistencyPreference`): equilíbrio entre `MINIMIZE_LATENCY` e `HIGHER_CONSISTENCY` (*Zookie* / Problema do Novo Inimigo)

## Em uma frase
Nas chamadas de leitura e verificação (`Check`, `ListObjects`, `ListUsers`), o OpenFGA permite habilitar o cache de queries e de iteradores no servidor e controlar por requisição o parâmetro **`consistency`**: **`MINIMIZE_LATENCY`** (usa o cache em memória para máxima velocidade) versus **`HIGHER_CONSISTENCY`** (ignora caches potencialmente obsoletos para ler diretamente do datastore após uma revogação crítica).

## Por que importa
No clássico *New Enemy Problem* descrito no artigo do Google Zanzibar: se Alice remove Bob do grupo de acesso a um documento e, um milissegundo depois, atualiza o documento com um segredo, um cache de permissão com TTL de 10 segundos não pode continuar respondendo que Bob ainda tem acesso.

## Como funciona
Configurando o cache do servidor (`--check-query-cache-enabled=true`) para absorver 95% das leituras repetitivas com `MINIMIZE_LATENCY`, a aplicação pode passar `"consistency": "HIGHER_CONSISTENCY"` seletivamente nas requisições imediatamente posteriores a uma alteração de permissões ou em ações destrutivas.

## Exemplo
```json
{
  "authorization_model_id": "01HV8G...",
  "tuple_key": {
    "user": "user:bob",
    "relation": "viewer",
    "object": "document:confidential-q4"
  },
  "consistency": "HIGHER_CONSISTENCY"
}
```

## Limites e trade-offs
Monitore a taxa de acerto de cache (*cache hit ratio*) e a latência P95/P99 nas métricas Prometheus expostas pelo OpenFGA (`--metrics-enabled=true` na porta `2112`) para calibrar o TTL do cache.

## Como verificar
Consulte `http://localhost:2112/metrics` para inspecionar as métricas internas de avaliação e cache do OpenFGA.

## Conexões
- [[openfga-armazenamento-producao-postgres-mysql-migrations-read-replicas]] — Veja também: OpenFGA em Produção (`openfga migrate` e Storage Engines): operação com PostgreSQL/MySQL, conexões e Unix Domain Socket.
- [[openfga-automacao-terraform-provider-sdks-embedded-go-library]] — Veja também: OpenFGA Ecossistema e Automação: Terraform Provider (`openfga/openfga`), SDKs oficiais e uso embarcado como biblioteca Go.

## Fontes
- [OpenFGA GitHub — README.md (CNCF Incubating Zanzibar Engine, Docker/CLI Quickstart, Production Storage, SLSA Level 3 & Official SDKs)](https://openfga.dev/docs/concepts) — README oficial do openfga/openfga detalhando execução via Docker e binário, migrações para PostgreSQL/MySQL, nota sobre Unix Domain Socket em /tmp e ferramentas do ecossistema; consultado em 2026-10-03.
- [OpenFGA Official Documentation — Core Concepts (Stores, Types, Objects, Users/Usersets, Relations, Authorization Models, Tuples & Queries)](https://raw.githubusercontent.com/openfga/openfga/main/README.md) — Documentação oficial de conceitos do OpenFGA explicando modelagem ReBAC/ABAC, imutabilidade de modelos, operadores de conjunto e semântica das APIs Check, ListObjects, ListUsers e Expand; consultado em 2026-10-03.
- [OpenFGA — Official GitHub Repository (CNCF)](https://github.com/openfga/openfga) — Repositório oficial Apache-2.0 do OpenFGA; consultado em 2026-10-03.
