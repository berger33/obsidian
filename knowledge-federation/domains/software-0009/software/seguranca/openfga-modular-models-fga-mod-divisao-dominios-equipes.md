---
id: software.seguranca.tranche01.000067
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

# OpenFGA Modular Models (`fga.mod`): divisão de modelos de autorização complexos em módulos por equipe e domínio

## Em uma frase
Em organizações grandes onde múltiplas equipes de produto compartilham o mesmo Store do OpenFGA, o recurso **Modular Models (`fga.mod`)** (suportado a partir do `schema 1.2`) permite dividir um modelo de autorização monolítico em múltiplos arquivos `.fga` por domínio (`core.fga`, `billing.fga`, `projects.fga`) e usar `extend type` para adicionar relações de forma segura.

## Por que importa
Se 10 equipes editarem um único arquivo `model.fga` de 1.500 linhas simultaneamente, conflitos de merge serão constantes e ficará difícil aplicar regras de `CODEOWNERS` no GitHub por área de negócio.

## Como funciona
Com um arquivo manifesto `fga.mod` listando os módulos (`contents: [core.fga, billing.fga, wiki.fga]`), cada equipe mantém seu próprio arquivo `.fga` e pode estender tipos compartilhados (como `extend type organization`) sem tocar nos arquivos das demais equipes.

## Exemplo
```yaml
# Arquivo fga.mod declarando os módulos que compõem o modelo unificado:
schema: '1.2'
contents:
  - core.fga
  - billing.fga
  - documents.fga
```

## Limites e trade-offs
Use o comando `fga model validate --file fga.mod` e `fga model test --tests tests.fga.yaml` para compilar e testar todos os módulos integrados antes de publicar a nova versão do modelo no Store.

## Como verificar
Execute `fga model transform --file fga.mod` para inspecionar o JSON consolidado resultante da compilação dos módulos.

## Conexões
- [[openfga-testes-unitarios-modelos-fga-model-test-ci-cd]] — Veja também: OpenFGA Testes Automatizados de Modelos (`fga model test`): validação declarativa de `.fga.yaml` em pipelines de CI/CD.
- [[openfga-armazenamento-producao-postgres-mysql-migrations-read-replicas]] — Veja também: OpenFGA em Produção (`openfga migrate` e Storage Engines): operação com PostgreSQL/MySQL, conexões e Unix Domain Socket.

## Fontes
- [OpenFGA GitHub — README.md (CNCF Incubating Zanzibar Engine, Docker/CLI Quickstart, Production Storage, SLSA Level 3 & Official SDKs)](https://openfga.dev/docs/concepts) — README oficial do openfga/openfga detalhando execução via Docker e binário, migrações para PostgreSQL/MySQL, nota sobre Unix Domain Socket em /tmp e ferramentas do ecossistema; consultado em 2026-10-03.
- [OpenFGA Official Documentation — Core Concepts (Stores, Types, Objects, Users/Usersets, Relations, Authorization Models, Tuples & Queries)](https://raw.githubusercontent.com/openfga/openfga/main/README.md) — Documentação oficial de conceitos do OpenFGA explicando modelagem ReBAC/ABAC, imutabilidade de modelos, operadores de conjunto e semântica das APIs Check, ListObjects, ListUsers e Expand; consultado em 2026-10-03.
- [OpenFGA — Official GitHub Repository (CNCF)](https://github.com/openfga/openfga) — Repositório oficial Apache-2.0 do OpenFGA; consultado em 2026-10-03.
