---
id: software.testes.tranche09.000282
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
fontes: ["https://graphql.org/learn/schema/", "https://graphql.org/learn/execution/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# GraphQL: testar propagação de null em campos non-null

## Em uma frase
Se a execução produz null para um campo non-null, o erro pode propagar até o ancestral anulável mais próximo da resposta.

## Por que importa
GraphQL valida operações contra um schema e pode devolver data parcial junto a errors, por isso assertions precisam refletir a execução por campo. Uma assertion que verifica somente mensagem de erro perde o efeito estrutural sobre outros campos retornados.

## Como funciona
Exercite operações representativas com variáveis, contexto e dados controlados; cubra tanto validação anterior aos resolvers quanto erros que ocorrem durante execução. Crie um caso em que um resolver falha abaixo de campo non-null e verifique erro, path e fronteira de propagação.

## Exemplo
Uma lista nullable contém item cujo nome obrigatório falha; teste se o item ou a lista inteira é anulada conforme schema.

## Limites e trade-offs
Semântica de paginação, autorização e cache depende do servidor e do schema; o protocolo não define sozinho regras de negócio da aplicação. O ponto exato de propagação depende das posições non-null no tipo da lista e nos campos ancestrais.

## Como verificar
Use pelo menos um caminho com nullable e outro com non-null e compare data, errors e path ao schema.

## Conexões
- [[graphql-variable-omitted-null-default]] — Veja também: GraphQL: distinguir variável omitida de null explícito.
- [[graphql-partial-data-errors-path]] — Veja também: GraphQL: aceitar data parcial quando um resolver falha.

## Fontes
- [GraphQL — Schemas and types](https://graphql.org/learn/schema/) — tipos, nullability e contrato de resposta; consultado em 2026-10-02.
- [GraphQL — Execution](https://graphql.org/learn/execution/) — execução de fields, erros e propagação de null; consultado em 2026-10-02.
