---
id: software.seguranca.tranche01.000070
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

# OpenFGA Ecossistema e Automação: Terraform Provider (`openfga/openfga`), SDKs oficiais e uso embarcado como biblioteca Go

## Em uma frase
Conforme destacado no README oficial, o OpenFGA oferece um **Terraform Provider oficial (`openfga/terraform-provider-openfga`)** para provisionar Stores, Authorization Models e Relationship Tuples como código, **SDKs oficiais** para Go, Python, Node.js/TypeScript, Java e .NET, e a capacidade de ser **embarcado diretamente como biblioteca Go** (`github.com/openfga/openfga/pkg/server`).

## Por que importa
Gerenciar Stores e publicar novas versões do modelo `.fga` manualmente via `curl` em múltiplos ambientes (`dev`, `staging`, `prod`) causa deriva de configuração entre o código da aplicação e o schema de autorização.

## Como funciona
Com o Terraform Provider do OpenFGA (ou em testes de integração que instanciam `server.NewServerWithOpts` em memória dentro do binário Go), todo o ciclo de vida do modelo de autorização acompanha exatamente o pipeline GitOps da infraestrutura.

## Exemplo
```hcl
resource "openfga_store" "prod" {
  name = "payments-prod"
}

resource "openfga_authorization_model" "prod_model" {
  store_id   = openfga_store.prod.id
  model_json = data.openfga_authorization_model_document.model.result
}
```

## Limites e trade-offs
Ao usar os SDKs oficiais do OpenFGA em microsserviços de alta vazão, prefira reutilizar uma única instância de cliente (`OpenFgaClient`) com pool de conexões HTTP/2 ou gRPC ativo.

## Como verificar
Verifique o estado do modelo aplicado no Store com `fga model get --store-id=${STORE_ID}`.

## Conexões
- [[openfga-performance-caching-consistency-higher-consistency-minimize-latency]] — Veja também: OpenFGA Consistência e Cache (`ConsistencyPreference`): equilíbrio entre `MINIMIZE_LATENCY` e `HIGHER_CONSISTENCY` (*Zookie* / Problema do Novo Inimigo).

## Fontes
- [OpenFGA GitHub — README.md (CNCF Incubating Zanzibar Engine, Docker/CLI Quickstart, Production Storage, SLSA Level 3 & Official SDKs)](https://raw.githubusercontent.com/openfga/openfga/main/README.md) — README oficial do openfga/openfga detalhando execução via Docker e binário, migrações para PostgreSQL/MySQL, nota sobre Unix Domain Socket em /tmp e ferramentas do ecossistema; consultado em 2026-10-03.
- [OpenFGA Official Documentation — Core Concepts (Stores, Types, Objects, Users/Usersets, Relations, Authorization Models, Tuples & Queries)](https://openfga.dev/docs/concepts) — Documentação oficial de conceitos do OpenFGA explicando modelagem ReBAC/ABAC, imutabilidade de modelos, operadores de conjunto e semântica das APIs Check, ListObjects, ListUsers e Expand; consultado em 2026-10-03.
- [OpenFGA — Official GitHub Repository (CNCF)](https://github.com/openfga/openfga) — Repositório oficial Apache-2.0 do OpenFGA; consultado em 2026-10-03.
