---
id: software.seguranca.tranche01.000065
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

# OpenFGA APIs de Consulta: diferenças e casos de uso entre `Check`, `BatchCheck`, `ListObjects`, `ListUsers` e `Expand`

## Em uma frase
O OpenFGA expõe cinco operações principais de consulta sobre o grafo de autorização: **`Check`** ("o usuário U tem a relação R com o objeto O?"), **`BatchCheck`** (avalia múltiplas checagens em uma única chamada de rede com deduplicação de subgrafos), **`ListObjects`** ("quais objetos do tipo T o usuário U pode acessar?"), **`ListUsers`** ("quais usuários têm a relação R no objeto O?") e **`Expand`** (retorna a árvore de resolução).

## Por que importa
Para renderizar uma página de listagem com 50 itens filtrados por permissão ou mostrar ícones de ações habilitadas, fazer 50 chamadas `Check` sequenciais criaria latência de rede; usar `BatchCheck` ou `ListObjects` resolve isso em uma única chamada.

## Como funciona
Cada API responde a uma pergunta arquitetural distinta: use **`Check`** no middleware de autorização de um endpoint específico; use **`BatchCheck`** para verificar permissões em uma lista paginada já buscada do banco; use **`ListObjects`** quando o conjunto de objetos acessíveis pelo usuário for pequeno/médio; e use **`ListUsers`** para auditorias de governança ("quem tem acesso a este cofre?").

## Exemplo
```bash
# Executando uma verificação Check na API HTTP do OpenFGA:
curl -sS -X POST "http://localhost:8080/stores/${STORE_ID}/check" \
  -H "Content-Type: application/json" \
  -d '{
    "authorization_model_id": "'"${MODEL_ID}"'",
    "tuple_key": {
      "user": "user:anne",
      "relation": "viewer",
      "object": "document:new-roadmap"
    }
  }'
```

## Limites e trade-offs
A resposta `{"allowed": true}` do `Check` pode ser cacheada em memória no próprio servidor OpenFGA configurando `--check-query-cache-enabled=true` e `--check-query-cache-ttl`.

## Como verificar
Execute `fga query check --store-id=${STORE_ID} user:anne viewer document:new-roadmap` para validar a decisão pela CLI.

## Conexões
- [[openfga-abac-conditions-cel-contextual-tuples-atributos-tempo-execucao]] — Veja também: OpenFGA ABAC Híbrido: combinação de grafos ReBAC com `Conditions` (Google CEL) e `Contextual Tuples`.
- [[openfga-testes-unitarios-modelos-fga-model-test-ci-cd]] — Veja também: OpenFGA Testes Automatizados de Modelos (`fga model test`): validação declarativa de `.fga.yaml` em pipelines de CI/CD.

## Fontes
- [OpenFGA GitHub — README.md (CNCF Incubating Zanzibar Engine, Docker/CLI Quickstart, Production Storage, SLSA Level 3 & Official SDKs)](https://openfga.dev/docs/concepts) — README oficial do openfga/openfga detalhando execução via Docker e binário, migrações para PostgreSQL/MySQL, nota sobre Unix Domain Socket em /tmp e ferramentas do ecossistema; consultado em 2026-10-03.
- [OpenFGA Official Documentation — Core Concepts (Stores, Types, Objects, Users/Usersets, Relations, Authorization Models, Tuples & Queries)](https://raw.githubusercontent.com/openfga/openfga/main/README.md) — Documentação oficial de conceitos do OpenFGA explicando modelagem ReBAC/ABAC, imutabilidade de modelos, operadores de conjunto e semântica das APIs Check, ListObjects, ListUsers e Expand; consultado em 2026-10-03.
- [OpenFGA — Official GitHub Repository (CNCF)](https://github.com/openfga/openfga) — Repositório oficial Apache-2.0 do OpenFGA; consultado em 2026-10-03.
