---
id: software.criacao_ia.tranche03.000293
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
fontes: ["https://spec.openapis.org/oas/v3.1.1.html#relative-references-in-api-description-uris", "https://spec.openapis.org/oas/v3.1.1.html#parsing-documents"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# OAS 3.1.1: resolver `$ref` relativo usando `$id` e URI-base

## Em uma frase
Dentro de Schema Objects, um `$id` pode mudar a URI-base usada por referências relativas; fora do contexto de schemas, a base vem do documento que contém a referência.

## Por que importa
Dois arquivos idênticos servidos de locais distintos podem resolver a mesma referência relativa para recursos diferentes. O problema é especialmente perigoso quando um loader valida apenas o fragmento referenciado e não enxerga `$id` ou outras palavras-chave que mudam a base.

## Como funciona
A especificação OAS herda a resolução JSON Schema 2020-12: referências em Schema Objects usam o `$id` ancestral mais próximo como base, se existir. Referências URI em outros Objects e schemas sem `$id` ancestral usam a base URI do documento referenciador, normalmente sua retrieval URI ou uma URI esperada configurada. Para JSON/YAML, um fragmento deve ser resolvido pelo mecanismo do documento e geralmente como JSON Pointer.

## Exemplo
Se um schema resource tem `$id: https://schemas.example/v1/order` e contém `$ref: address.json`, o alvo é resolvido em relação àquele id, não necessariamente à pasta de download. Uma referência `externalDocs.url` que não esteja dentro de schema continua usando a base do documento OAS.

## Limites e trade-offs
OAS 3.1.1 declara indefinido o resultado de parsing de fragmentos isolados quando a base correta depende do documento completo. Adotar somente caminho local, sem manter a URI esperada, pode produzir comportamento não interoperável e carregar conteúdo inesperado.

## Como verificar
Crie fixture com dois `$id` diferentes e o mesmo `$ref` relativo; resolva o documento por retrieval URI e por expected URI e confira o alvo. Audite também referências de Reference Object, Schema Object e externalDocs para garantir o escopo correto.

## Conexões
- [[oas311-reference-object-vs-schema-ref]] — OAS 3.1.1: diferenciar Reference Object de `$ref` em Schema Object.
- [[oas311-format-annotation-nao-validacao]] — OAS 3.1.1: `format` não é uma validação garantida.

## Fontes
- [OpenAPI Specification v3.1.1 — Relative References in API Description URIs](https://spec.openapis.org/oas/v3.1.1.html#relative-references-in-api-description-uris) — define `$id` ancestral, base do documento e interpretação dos fragmentos Consulta: 2026-10-04.
- [OpenAPI Specification v3.1.1 — Parsing Documents](https://spec.openapis.org/oas/v3.1.1.html#parsing-documents) — exige considerar documentos completos antes de concluir que uma referência não é resolvível Consulta: 2026-10-04.
