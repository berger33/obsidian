---
id: software.criacao_ia.tranche03.000292
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
fontes: ["https://spec.openapis.org/oas/v3.1.1.html#reference-object", "https://json-schema.org/draft/2020-12/json-schema-core"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# OAS 3.1.1: diferenciar Reference Object de `$ref` em Schema Object

## Em uma frase
Um Reference Object do OAS e um Schema Object que usa `$ref` são construções diferentes, apesar de compartilharem o mesmo nome de keyword.

## Por que importa
Confundir os dois formatos faz geradores descartarem constraints irmãs de schemas ou, inversamente, usarem propriedades não suportadas em uma referência de parâmetro. A diferença afeta validação, substituição de summary/description e o tratamento de campos adicionais.

## Como funciona
Um Reference Object tem `$ref` obrigatório e admite `summary` e `description` como overrides recomendados; outras propriedades adicionadas devem ser ignoradas. Dentro de Schema Object, `$ref` é o applicator de JSON Schema: keywords irmãs continuam compondo o schema e podem impor constraints adicionais ao alvo. Verifique o tipo do ponto onde a referência aparece antes de aplicar as regras.

## Exemplo
Em `schema: { $ref: '#/components/schemas/Name', maxLength: 40 }`, `maxLength` continua restringindo as instâncias referenciadas. Já `parameters: [{ $ref: '#/components/parameters/Limit', description: '...' }]` usa um Reference Object e a descrição pode sobrescrever a descrição do componente; um campo arbitrário não é merge universal.

## Limites e trade-offs
Não generalize comportamento de Reference Object para Path Item `$ref`: OAS 3.1.1 define uma regra especial para propriedades adjacentes do Path Item e deixa conflitos indefinidos. Implementações também podem limitar quais schemas JSON Schema externos suportam.

## Como verificar
Valide uma instância aceita pelo schema referenciado, mas rejeitada pela constraint irmã. Em referência de parâmetro, confira override de descrição e confirme que uma propriedade adicional desconhecida não alterou a definição efetiva.

## Conexões
- [[oas311-jsonschema-dialect-default-override]] — OAS 3.1.1: selecionar o dialect JSON Schema correto.
- [[oas311-id-and-relative-ref-base-uri]] — OAS 3.1.1: resolver `$ref` relativo usando `$id` e URI-base.

## Fontes
- [OpenAPI Specification v3.1.1 — Reference Object](https://spec.openapis.org/oas/v3.1.1.html#reference-object) — define campos e limitações do Reference Object e o diferencia de Schema Object com $ref Consulta: 2026-10-04.
- [JSON Schema Core Draft 2020-12](https://json-schema.org/draft/2020-12/json-schema-core) — define o keyword $ref no modelo de applicators e na resolução de schemas Consulta: 2026-10-04.
