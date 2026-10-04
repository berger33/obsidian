---
id: software.criacao_ia.tranche03.000297
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
fontes: ["https://spec.openapis.org/oas/v3.1.1.html#working-with-binary-data", "https://spec.openapis.org/oas/v3.1.1.html#data-type-format"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# OAS 3.1.1: modelar binário com contentEncoding e contentMediaType

## Em uma frase
Em OAS 3.1.1, `format: binary` não define encoding do payload; os keywords JSON Schema `contentEncoding` e `contentMediaType` expressam conteúdo codificado.

## Por que importa
Descrições migradas de 3.0 podem continuar usando `format: binary` esperando que o gerador produza base64 ou trate a mensagem como arquivo. Isso mistura JSON Schema com o `Content-Encoding` HTTP, que se aplica em outra etapa da serialização.

## Como funciona
Para binário cru como corpo HTTP, o Schema Object pode ser omitido ou representar media type sem impor um tipo JSON. Para bytes codificados dentro de texto, use `type: string`, `contentEncoding` como `base64` ou `base64url` e `contentMediaType` para o conteúdo representado. `contentEncoding` não é o header HTTP `Content-Encoding`; este último trata compressão da mensagem após a serialização do conteúdo.

## Exemplo
Um upload PNG binário pode usar `content: { image/png: {} }`. Um campo JSON contendo uma representação em texto pode usar `type: string`, `contentEncoding: base64url` e `contentMediaType: image/png`; a codificação URL da própria request continua sendo uma etapa adicional se o payload estiver numa query ou form.

## Limites e trade-offs
As keywords de conteúdo são annotations por default em JSON Schema e podem não ser verificadas por validadores. Quando o media type já aparece na chave do Media Type Object, contentMediaType pode ser redundante; se houver conflito com media type/Encoding Object do OAS, a regra de precedência deve ser considerada.

## Como verificar
Inspecione a representação no fio para payload cru, JSON base64 e `application/x-www-form-urlencoded`. Confirme que o HTTP Content-Encoding só muda compressão e que nenhum consumer espera base64 apenas por encontrar `format: binary`.

## Conexões
- [[oas311-discriminator-nao-altera-validacao]] — OAS 3.1.1 discriminator: pista de serialização, não regra de validação.
- [[oas311-webhooks-versus-callbacks]] — OAS 3.1.1: escolher entre webhook top-level e callback de operação.

## Fontes
- [OpenAPI Specification v3.1.1 — Working with Binary Data](https://spec.openapis.org/oas/v3.1.1.html#working-with-binary-data) — distingue binário cru, string codificada, contentEncoding e Content-Encoding HTTP Consulta: 2026-10-04.
- [OpenAPI Specification v3.1.1 — Data Type Format](https://spec.openapis.org/oas/v3.1.1.html#data-type-format) — define que format em 3.1 não carrega semântica de encoding binário Consulta: 2026-10-04.
