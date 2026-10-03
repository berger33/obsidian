---
id: software.seguranca.tranche01.000066
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

# OpenFGA Testes Automatizados de Modelos (`fga model test`): validação declarativa de `.fga.yaml` em pipelines de CI/CD

## Em uma frase
A CLI oficial do OpenFGA (`openfga/cli`, binário **`fga`**) inclui um executor nativo de testes automatizados (**`fga model test --tests <arquivo.fga.yaml>`**) que valida um modelo de autorização `.fga` em memória contra cenários de tuplas e asserções de `check`, `list_objects` e `list_users` sem precisar subir um servidor ou banco de dados.

## Por que importa
Uma alteração sutil em uma expressão `or` / `but not` do modelo de autorização pode conceder acesso indevido a documentos confidenciais; testar o modelo como código no CI bloqueia regressões de segurança antes do deploy.

## Como funciona
Em um arquivo `.fga.yaml`, você referencia `model_file: ./model.fga`, define um conjunto de `tuples` de cenário e declara múltiplos `tests` com asserções booleanas explícitas (`assertions: { viewer: true, editor: false }`).

## Exemplo
```yaml
name: "Testes do modelo de documentos"
model_file: ./model.fga
tuples:
  - user: user:anne
    relation: editor
    object: document:roadmap
  - user: user:bob
    relation: viewer
    object: document:roadmap
  - user: user:bob
    relation: blocked
    object: document:roadmap
tests:
  - name: "Editor pode editar e visualizar; usuário bloqueado não pode visualizar"
    check:
      - user: user:anne
        object: document:roadmap
        assertions:
          editor: true
          viewer: true
      - user: user:bob
        object: document:roadmap
        assertions:
          viewer: false
```

## Limites e trade-offs
Como `fga model test` executa 100% em memória no processo da CLI em milissegundos, inclua-o como etapa obrigatória em todo Pull Request que modifique arquivos `.fga`.

## Como verificar
Execute `fga model test --tests ./model.fga.yaml` e verifique que todos os testes passam com exit code `0`.

## Conexões
- [[openfga-queries-check-batchcheck-listobjects-listusers-expand]] — Veja também: OpenFGA APIs de Consulta: diferenças e casos de uso entre `Check`, `BatchCheck`, `ListObjects`, `ListUsers` e `Expand`.
- [[openfga-modular-models-fga-mod-divisao-dominios-equipes]] — Veja também: OpenFGA Modular Models (`fga.mod`): divisão de modelos de autorização complexos em módulos por equipe e domínio.

## Fontes
- [OpenFGA GitHub — README.md (CNCF Incubating Zanzibar Engine, Docker/CLI Quickstart, Production Storage, SLSA Level 3 & Official SDKs)](https://raw.githubusercontent.com/openfga/openfga/main/README.md) — README oficial do openfga/openfga detalhando execução via Docker e binário, migrações para PostgreSQL/MySQL, nota sobre Unix Domain Socket em /tmp e ferramentas do ecossistema; consultado em 2026-10-03.
- [OpenFGA Official Documentation — Core Concepts (Stores, Types, Objects, Users/Usersets, Relations, Authorization Models, Tuples & Queries)](https://openfga.dev/docs/concepts) — Documentação oficial de conceitos do OpenFGA explicando modelagem ReBAC/ABAC, imutabilidade de modelos, operadores de conjunto e semântica das APIs Check, ListObjects, ListUsers e Expand; consultado em 2026-10-03.
- [OpenFGA — Official GitHub Repository (CNCF)](https://github.com/openfga/openfga) — Repositório oficial Apache-2.0 do OpenFGA; consultado em 2026-10-03.
