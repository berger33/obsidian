---
id: software.criacao_ia.tranche03.000216
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
fontes: ["https://modelcontextprotocol.io/specification/2026-07-28/server/tools", "https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# MCP tools/list: catálogo determinístico e schema de entrada executável

## Em uma frase
`tools/list` descreve ferramentas disponíveis ao request autenticado; `tools/call` executa uma delas e suas respostas seguem o contrato de resultado MCP.

## Por que importa
A descrição de uma ferramenta alimenta seleção do modelo e interface, mas não é uma barreira de permissão. A revisão 2026-07-28 tornou explícito que o catálogo pode variar conforme autorização apresentada em cada request, não por conexão ou efeito colateral de outras chamadas.

## Como funciona
Implemente paginação e `inputSchema` JSON Schema 2020-12 válido. Retorne a lista em ordem determinística quando o conjunto não mudar, para viabilizar cache e estabilidade de prompt. O servidor pode filtrar ferramentas segundo escopos autorizados no request; ao executar, valide novamente argumentos, permissões e estado do recurso. Trate anotações descritivas como não confiáveis, salvo origem confiável.

## Exemplo
Um servidor de assets oferece `preview_asset` a todo usuário e `publish_asset` apenas a um grupo autorizado. Duas chamadas `tools/list` usam credenciais distintas e produzem catálogos diferentes; chamadas diretas a `tools/call` sem permissão ainda são recusadas pelo servidor, mesmo se o cliente reteve uma definição antiga.

## Limites e trade-offs
Schemas de entrada ajudam validação estrutural, mas não verificam autorização de negócio nem corrigem argumentos maliciosos. A lista pode mudar ao longo do tempo e a política de cache precisa respeitar `cacheScope` e autorização.

## Como verificar
Valide schema, paginação, estabilidade de ordenação e resposta a `list_changed`. Teste chamadas diretas com usuário sem escopo e alterações na lista enquanto há cópia cacheada no cliente.

## Conexões
- [[mcp-cache-ttl-scope-e-invalidacao]] — MCP: combinar ttlMs, cacheScope e notificações de invalidação.
- [[mcp-prompts-selecao-controlada-pelo-usuario]] — MCP prompts: distinguir seleção do usuário e autoria do servidor.

## Fontes
- [MCP 2026-07-28 — Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools) — define list/call, JSON Schema, variação por autorização e confiança em annotations Consulta: 2026-10-04.
- [MCP 2026-07-28 — Caching](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching) — especifica cache de catálogos e isolamento de resultados privados Consulta: 2026-10-04.
