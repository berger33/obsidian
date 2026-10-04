---
id: software.criacao_ia.tranche03.000213
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
fontes: ["https://modelcontextprotocol.io/specification/2026-07-28/basic/index", "https://modelcontextprotocol.io/specification/2026-07-28/basic/transports"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# MCP 2026: carregar versão e capacidades em _meta por request

## Em uma frase
Na revisão MCP 2026-07-28, a versão de protocolo e as capacidades do cliente são metadados obrigatórios em cada request, em vez de estado negociado por handshake.

## Por que importa
A mudança permite processar requests sem uma sessão inicial compartilhada e evita que o servidor dependa de contexto de conexão ao escalar horizontalmente. Também significa que um método isolado só é interpretável com seus metadados: exemplos de documentação que os omitem por concisão não são mensagens completas para wire.

## Como funciona
Inclua no objeto `_meta` os campos `io.modelcontextprotocol/protocolVersion` e `io.modelcontextprotocol/clientCapabilities`; inclua a identidade do cliente quando aplicável. A página Streamable HTTP permite espelhar certos metadados em cabeçalhos para intermediários, mas o corpo continua sendo a fonte de verdade e diferenças precisam ser rejeitadas conforme binding. Servidores podem devolver identidade em `_meta` do resultado.

## Exemplo
Um adaptador que converte chamadas internas em MCP cria um envelope comum para `tools/list`, `prompts/get` e `resources/read`. Testes de contrato removem cada campo obrigatório por vez e esperam o erro de protocolo especificado, em vez de reutilizar silenciosamente capacidades guardadas num objeto de conexão.

## Limites e trade-offs
A forma exata dos metadados é versionada e clientes legados usam `initialize`; não misture os dois modelos sem detecção de compatibilidade. Espelhar dados em cabeçalhos não os torna mais autoritativos que o corpo, e dados de identidade declarados não substituem autenticação.

## Como verificar
Capture requests no limite HTTP e no decoder JSON-RPC, compare corpo e cabeçalhos e teste versão incompatível e ausência de capacidades. Faça uma chamada sem inicialização prévia para confirmar que cada request tem o contexto próprio.

## Conexões
- [[mcp-streamable-http-versao-2026-stateless]] — MCP Streamable HTTP 2026: requests POST sem sessão implícita.
- [[mcp-mrtr-input-required-request-state]] — MCP MRTR: retomar requests com inputResponses e requestState opaco.

## Fontes
- [MCP 2026-07-28 — Protocolo base e _meta](https://modelcontextprotocol.io/specification/2026-07-28/basic/index) — define campos de metadados por request e o modelo stateless Consulta: 2026-10-04.
- [MCP 2026-07-28 — Transportes](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports) — explica metadados inline e espelhamento opcional na binding HTTP Consulta: 2026-10-04.
