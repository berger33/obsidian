---
id: software.criacao_ia.tranche03.000294
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
fontes: ["https://spec.openapis.org/oas/v3.1.1.html#data-type-format", "https://json-schema.org/draft/2020-12/json-schema-validation"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# OAS 3.1.1: `format` não é uma validação garantida

## Em uma frase
No comportamento padrão de OAS 3.1.1, `format` é annotation não validante; sua presença não substitui `type` nem garante que um payload será rejeitado por formato incorreto.

## Por que importa
Formatos conhecidos como `date-time`, `email` ou `int64` são frequentemente tratados como assertions por ferramentas, mas o padrão não obriga suporte igual a todos. Um cliente que usa `format` como única constraint pode aceitar tipos errados ou divergir do servidor.

## Como funciona
Escreva primeiro o tipo JSON com `type`, depois adicione `format` para a annotation e para validação estendida que a implementação oferecer. OAS 3.1.1 indica que format é annotation por default e o suporte a registros adicionais de formato é opcional; JSON Schema também permite que o vocabulário `format-assertion` seja usado explicitamente em outro dialect.

## Exemplo
`{ type: string, format: date-time }` descreve uma string com formato desejado. Com apenas `format: date-time`, a especificação observa que keywords e formatos aplicáveis a strings consideram instâncias de outros tipos automaticamente válidas; por isso, a constraint de tipo precisa estar explícita.

## Limites e trade-offs
Mesmo com `type: string`, a validade calendárica de um `date-time` pode depender de suporte de formato opcional e da versão da biblioteca. Não confunda o formato de Schema Object com serialização HTTP ou uma validação de runtime que OAS não prescreve.

## Como verificar
Rode o mesmo payload em dois validadores: string válida, string malformada e número. Confirme a constraint de tipo em ambos e registre separadamente se o validador habilitou assertions para o formato.

## Conexões
- [[oas311-id-and-relative-ref-base-uri]] — OAS 3.1.1: resolver `$ref` relativo usando `$id` e URI-base.
- [[oas311-null-union-boolean-schemas]] — OAS 3.1.1: representar null e schemas booleanos com JSON Schema.

## Fontes
- [OpenAPI Specification v3.1.1 — Data Type Format](https://spec.openapis.org/oas/v3.1.1.html#data-type-format) — define formatos como annotations não validantes por default e suporte opcional Consulta: 2026-10-04.
- [JSON Schema Validation Draft 2020-12](https://json-schema.org/draft/2020-12/json-schema-validation) — distingue a annotation format da asserção opcional format-assertion Consulta: 2026-10-04.
