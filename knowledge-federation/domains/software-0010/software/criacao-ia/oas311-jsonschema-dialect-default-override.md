---
id: software.criacao_ia.tranche03.000291
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-03.md"
fontes: ["https://spec.openapis.org/oas/v3.1.1.html#specifying-schema-dialects", "https://spec.openapis.org/oas/3.1/dialect/base"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# OAS 3.1.1: selecionar o dialect JSON Schema correto

## Em uma frase
OAS 3.1.1 usa um dialect JSON Schema baseado em Draft 2020-12 e permite configurar um default por documento sem substituir `$schema` na raiz de cada recurso-schema.

## Por que importa
Um validador que assume sempre JSON Schema puro pode ignorar vocabulário OAS, enquanto outro pode processar `$schema` de forma inconsistente entre documentos. Em descrições multi-documento, essa divergência muda referências, annotations e até a interpretação dos mesmos keywords.

## Como funciona
O dialect OAS para esta especificação é identificado por `https://spec.openapis.org/oas/3.1/dialect/base`. `jsonSchemaDialect` no OpenAPI Object define o default para Schema Objects do documento; se ausente, aplica-se o dialect OAS. Um `$schema` presente na raiz de um schema resource prevalece sobre o default. Tooling OAS deve suportar o OAS dialect id e pode suportar outros dialects.

## Exemplo
Uma API que usa o dialect padrão deixa `jsonSchemaDialect` ausente. Um schema externo que declara explicitamente `$schema: https://json-schema.org/draft/2020-12/schema` seleciona aquele dialect para seu recurso, enquanto schemas sem override continuam a usar o default do documento OAS.

## Limites e trade-offs
`$schema` não é um indicador arbitrário em qualquer subobjeto: a especificação o descreve em raiz de schema resource. Um parser que só carrega o fragmento referenciado pode perder a informação de dialect e de base URI presente no documento completo.

## Como verificar
Teste documento sem default, documento com `jsonSchemaDialect` customizado e schema resource com `$schema` explícito. Registre qual dialect o validador escolheu para cada recurso, inclusive após resolver referências externas.

## Conexões
- [[oas311-reference-object-vs-schema-ref]] — OAS 3.1.1: diferenciar Reference Object de `$ref` em Schema Object.

## Fontes
- [OpenAPI Specification v3.1.1 — Specifying Schema Dialects](https://spec.openapis.org/oas/v3.1.1.html#specifying-schema-dialects) — define precedência de $schema, jsonSchemaDialect e OAS dialect schema id Consulta: 2026-10-04.
- [OpenAPI 3.1 Schema Object Dialect](https://spec.openapis.org/oas/3.1/dialect/base) — publica o meta-schema do dialect base e os vocabulários JSON Schema incluídos Consulta: 2026-10-04.
