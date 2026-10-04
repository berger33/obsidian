---
id: software.criacao_ia.tranche03.000296
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
fontes: ["https://spec.openapis.org/oas/v3.1.1.html#discriminator-object", "https://spec.openapis.org/oas/v3.1.1.html#composition-and-inheritance-polymorphism"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# OAS 3.1.1 discriminator: pista de serialização, não regra de validação

## Em uma frase
O `discriminator` do OAS pode orientar seleção e desserialização, mas não pode alterar o resultado da validação JSON Schema.

## Por que importa
Um schema que espera que o discriminator descubra subclasses pode aceitar ou rejeitar instâncias de modo diferente do imaginado. Em particular, um pai `allOf` não varre automaticamente schemas filhos apenas porque há `propertyName` e mapping.

## Como funciona
O objeto requer `propertyName` e pode mapear valores de payload a nomes de componentes ou URI references. É legal junto de `oneOf`, `anyOf` ou `allOf`; se `oneOf`/`anyOf` o acompanha, todas as alternativas devem ser listadas explicitamente. A validação continua dependendo dos constraints JSON Schema; `discriminator` apenas fornece uma pista útil a tooling de serialization/deserialization.

## Exemplo
Em `oneOf: [Cat, Dog]` com `propertyName: petType`, uma tabela de mapping pode direcionar rapidamente `petType: dog` ao schema Dog. Ainda assim, os constraints de Cat e Dog determinam se o objeto é válido; a pista não torna válido um payload que falha no schema selecionado.

## Limites e trade-offs
Com `allOf` em um schema pai, o discriminator é útil para casos não validantes, mas não busca schemas filhos. Mapping ambíguo entre nome de componente e URI relativo pode ser implementation-defined; prefira URI explícita quando houver ambiguidade.

## Como verificar
Crie payload com discriminator válido e propriedades inválidas; confirme que continua falhando. Teste mapping implícito e explícito, e valide que as alternatives oneOf/anyOf estejam listadas em vez de presumidas.

## Conexões
- [[oas311-null-union-boolean-schemas]] — OAS 3.1.1: representar null e schemas booleanos com JSON Schema.
- [[oas311-binary-contentencoding-vs-format]] — OAS 3.1.1: modelar binário com contentEncoding e contentMediaType.

## Fontes
- [OpenAPI Specification v3.1.1 — Discriminator Object](https://spec.openapis.org/oas/v3.1.1.html#discriminator-object) — define que discriminator não muda resultado de validação e restringe seus usos Consulta: 2026-10-04.
- [OpenAPI Specification v3.1.1 — Composition and Inheritance](https://spec.openapis.org/oas/v3.1.1.html#composition-and-inheritance-polymorphism) — explica composição allOf e o papel do discriminator no modelamento Consulta: 2026-10-04.
