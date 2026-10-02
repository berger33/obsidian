---
id: software.testes.tranche09.000281
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-09.md"
fontes: ["https://graphql.org/learn/queries/", "https://graphql.org/learn/schema/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# GraphQL: distinguir variável omitida de null explícito

## Em uma frase
Valores omitidos, defaults e null explícito podem produzir caminhos diferentes conforme definição do argumento e da variável no schema.

## Por que importa
GraphQL valida operações contra um schema e pode devolver data parcial junto a errors, por isso assertions precisam refletir a execução por campo. Um cliente pode inadvertidamente substituir um default por null ou ocultar que uma propriedade não foi enviada.

## Como funciona
Exercite operações representativas com variáveis, contexto e dados controlados; cubra tanto validação anterior aos resolvers quanto erros que ocorrem durante execução. Teste operações com variável ausente, variável definida, null explícito e valor válido nos campos em que a distinção importa.

## Exemplo
A atualização de filtro usa default quando a chave é omitida, mas preserva solicitação explícita de null conforme contrato definido.

## Limites e trade-offs
Semântica de paginação, autorização e cache depende do servidor e do schema; o protocolo não define sozinho regras de negócio da aplicação. O comportamento final é decidido pelo schema e resolver; não assuma que todos os argumentos interpretam null como ausência.

## Como verificar
Compare input recebido no resolver e resposta nos quatro cenários, incluindo erro de coerção quando o tipo exige valor.

## Conexões
- [[graphql-validation-before-resolvers]] — Veja também: GraphQL: validar operações antes de executar resolvers.
- [[graphql-non-null-null-propagation]] — Veja também: GraphQL: testar propagação de null em campos non-null.

## Fontes
- [GraphQL — Queries](https://graphql.org/learn/queries/) — variáveis, aliases, fragments e forma das operações; consultado em 2026-10-02.
- [GraphQL — Schemas and types](https://graphql.org/learn/schema/) — tipos, nullability e contrato de resposta; consultado em 2026-10-02.
