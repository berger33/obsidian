---
id: software.criacao_ia.tranche03.000215
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
fontes: ["https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching", "https://modelcontextprotocol.io/specification/2026-07-28/server/tools"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# MCP: combinar ttlMs, cacheScope e notificações de invalidação

## Em uma frase
Resultados cacheáveis do MCP carregam um TTL de frescor e um escopo público ou privado, e uma notificação de mudança pode invalidar o cache antes do TTL.

## Por que importa
Cache sem escopo pode vazar dados de um usuário a outro, enquanto um TTL interpretado como garantia de imutabilidade pode deixar ferramentas obsoletas na interface. A combinação das dicas com notificações reduz tráfego sem converter frescor aproximado em verdade permanente.

## Como funciona
Use método e parâmetros relevantes na chave do cache, como URI ou cursor. `ttlMs` indica por quanto tempo o cliente pode considerar a resposta fresca; zero significa imediatamente obsoleta. `cacheScope=public` permite reutilização compartilhada; `private` restringe a reutilização ao mesmo contexto de autorização. Notificações de mudança invalidam a entrada. Respostas intermediárias `input_required` e requests repetidos com `inputResponses` ou `requestState` não devem ser cacheados.

## Exemplo
Um `tools/list` idêntico para todos os chamadores pode ser público e ter TTL de cinco minutos. Uma leitura de recurso personalizada para o token atual usa escopo privado; se chegar `resources/list_changed`, o cliente marca os dados como obsoletos e consulta de novo no próximo acesso, sem esperar o TTL.

## Limites e trade-offs
TTL é dica de frescor, não garantia de que o servidor não alterará os dados. Páginas de lista são cacheadas independentemente e não têm garantia de snapshot consistente entre páginas. Não trate expiração como timer obrigatório de polling.

## Como verificar
Automatize casos com TTL zero e positivo, mudança antes da expiração, tokens distintos, páginas paginadas e repetição MRTR. Verifique que caches compartilhados nunca cruzam contextos de autorização privados.

## Conexões
- [[mcp-mrtr-input-required-request-state]] — MCP MRTR: retomar requests com inputResponses e requestState opaco.
- [[mcp-tools-list-schema-autorizacao]] — MCP tools/list: catálogo determinístico e schema de entrada executável.

## Fontes
- [MCP 2026-07-28 — Caching](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching) — define TTL, escopo, chaves, notificações, paginação e exclusões de cache Consulta: 2026-10-04.
- [MCP 2026-07-28 — Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools) — mostra `ttlMs` e `cacheScope` no resultado de tools/list Consulta: 2026-10-04.
