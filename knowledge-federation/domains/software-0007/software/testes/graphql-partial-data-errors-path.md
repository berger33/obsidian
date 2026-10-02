---
id: software.testes.tranche09.000283
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
fontes: ["https://graphql.org/learn/execution/", "https://www.apollographql.com/docs/apollo-server/testing/testing"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# GraphQL: aceitar data parcial quando um resolver falha

## Em uma frase
Erro durante resolução de um campo pode coexistir com outros campos concluídos, produzindo data parcial e uma lista de errors.

## Por que importa
GraphQL valida operações contra um schema e pode devolver data parcial junto a errors, por isso assertions precisam refletir a execução por campo. Exigir somente status HTTP de sucesso ou falha pode apagar a distinção entre falha de protocolo e erro de campo.

## Como funciona
Exercite operações representativas com variáveis, contexto e dados controlados; cubra tanto validação anterior aos resolvers quanto erros que ocorrem durante execução. Valide os campos independentes, a entrada de error e o path que aponta ao campo que falhou.

## Exemplo
Query solicita perfil e recomendação; a recomendação falha, mas perfil continua disponível e o cliente mostra fallback local.

## Limites e trade-offs
Semântica de paginação, autorização e cache depende do servidor e do schema; o protocolo não define sozinho regras de negócio da aplicação. Políticas de status HTTP e mascaramento de detalhes variam por servidor; não exponha informação sensível nos erros.

## Como verificar
Injete falha em um resolver e confira que o resultado parcial e o caminho do erro correspondem ao schema e à operação.

## Conexões
- [[graphql-non-null-null-propagation]] — Veja também: GraphQL: testar propagação de null em campos non-null.
- [[graphql-alias-fragment-response-shape]] — Veja também: GraphQL: testar aliases e fragments pela forma da resposta.

## Fontes
- [GraphQL — Execution](https://graphql.org/learn/execution/) — execução de fields, erros e propagação de null; consultado em 2026-10-02.
- [Apollo Server — Integration testing](https://www.apollographql.com/docs/apollo-server/testing/testing) — executeOperation e testes de integração do pipeline de requisições; consultado em 2026-10-02.
