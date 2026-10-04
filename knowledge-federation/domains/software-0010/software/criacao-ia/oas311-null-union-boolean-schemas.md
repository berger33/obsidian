---
id: software.criacao_ia.tranche03.000295
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
fontes: ["https://spec.openapis.org/oas/v3.1.1.html#schema-object", "https://json-schema.org/draft/2020-12/json-schema-core"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# OAS 3.1.1: representar null e schemas booleanos com JSON Schema

## Em uma frase
OAS 3.1.1 adota schemas booleanos e uniões de tipo JSON Schema; `nullable` de OAS 3.0 não é a forma normativa de permitir `null`.

## Por que importa
Migração mecânica de schemas 3.0 pode deixar `nullable: true` sem o efeito esperado em validadores 3.1. Além disso, schemas sem objeto não são necessariamente inválidos: os valores booleanos permitem expressar aceitação universal ou rejeição total.

## Como funciona
Use `type: [string, 'null']` para permitir string e null, mantendo os outros constraints que fizerem sentido. `true` é o schema vazio que permite qualquer instância; `false` é o schema que nenhuma instância satisfaz. Aplique `type` explicitamente quando keywords como `pattern` só se destinarem a strings.

## Exemplo
Uma propriedade opcionalmente nula pode usar `schema: { type: [string, 'null'] }`. Para um campo proibido por uma variante específica, `schema: false` expressa rejeição total; para conteúdo sem constraints além de JSON válido, `schema: true` expressa aceitação geral.

## Limites e trade-offs
Ferramentas antigas podem não aceitar schemas booleanos nem arrays no campo `type`. OAS Schema Object permite propriedades não reconhecidas, mas um `nullable` não definido pelo dialect não converte por si só uma string em união com null.

## Como verificar
Valide string, null e número contra a união e confirme que somente os dois primeiros passam. Teste `true` e `false` isoladamente e faça lint para detectar ocorrências herdadas de `nullable` em arquivos migrados.

## Conexões
- [[oas311-format-annotation-nao-validacao]] — OAS 3.1.1: `format` não é uma validação garantida.
- [[oas311-discriminator-nao-altera-validacao]] — OAS 3.1.1 discriminator: pista de serialização, não regra de validação.

## Fontes
- [OpenAPI Specification v3.1.1 — Schema Object](https://spec.openapis.org/oas/v3.1.1.html#schema-object) — declara Schema Object como superset de JSON Schema 2020-12 e permite boolean schemas Consulta: 2026-10-04.
- [JSON Schema Core Draft 2020-12](https://json-schema.org/draft/2020-12/json-schema-core) — define a forma de schemas, tipos JSON e semântica de referência Consulta: 2026-10-04.
