---
id: software.testes.tranche09.000288
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
fontes: ["https://www.apollographql.com/docs/apollo-server/performance/caching", "https://www.apollographql.com/docs/apollo-server/security/authentication"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# GraphQL: testar cache em respostas autenticadas

## Em uma frase
Cache control precisa refletir se a resposta é pública ou depende da identidade e dos dados consultados.

## Por que importa
GraphQL valida operações contra um schema e pode devolver data parcial junto a errors, por isso assertions precisam refletir a execução por campo. Resposta compartilhada por chave insuficiente pode servir dados privados a outra sessão mesmo quando ambos usam a mesma operação GraphQL.

## Como funciona
Exercite operações representativas com variáveis, contexto e dados controlados; cubra tanto validação anterior aos resolvers quanto erros que ocorrem durante execução. Inspecione política de cache por field e execute requests com identidades diferentes contra o mesmo caminho e parâmetros.

## Exemplo
O perfil retorna informação privada sem cache compartilhado, enquanto um catálogo público pode usar política pública explicitamente aprovada.

## Limites e trade-offs
Semântica de paginação, autorização e cache depende do servidor e do schema; o protocolo não define sozinho regras de negócio da aplicação. A política efetiva depende do cache HTTP e de plugins do servidor; hints não configuram todos os intermediários automaticamente.

## Como verificar
Compare headers e corpo depois de autenticação variável e confirme que proxies/CDN respeitam as regras definidas.

## Conexões
- [[graphql-authorization-resolver-context]] — Veja também: GraphQL: verificar autorização no caminho de execução.
- [[graphql-schema-change-compatibility]] — Veja também: GraphQL: revisar mudanças de schema com operações consumidoras.

## Fontes
- [Apollo Server — Caching](https://www.apollographql.com/docs/apollo-server/performance/caching) — políticas de cache e comportamento de resposta; consultado em 2026-10-02.
- [Apollo Server — Authentication and authorization](https://www.apollographql.com/docs/apollo-server/security/authentication) — autenticação, contexto da requisição e autorização em resolvers; consultado em 2026-10-02.
