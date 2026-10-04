---
id: software.criacao_ia.tranche03.000212
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
fontes: ["https://modelcontextprotocol.io/specification/2026-07-28/basic/transports", "https://modelcontextprotocol.io/specification/2026-07-28/changelog"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# MCP Streamable HTTP 2026: requests POST sem sessão implícita

## Em uma frase
Na binding Streamable HTTP 2026-07-28, cada mensagem cliente-servidor é enviada por POST ao endpoint MCP e uma resposta pode ser JSON ou SSE associado ao request.

## Por que importa
Clientes que mantêm `Mcp-Session-Id`, usam GET como canal permanente ou esperam replay de eventos estão implementando a geração anterior do transporte. A nova semântica elimina dependência de sessão por conexão, facilitando servidores sem estado e balanceamento sem afinidade, mas exige que clientes tratem a perda de uma resposta em voo explicitamente.

## Como funciona
Implemente um único endpoint MCP para POSTs e leia a versão, capacidades e identidade nos metadados do corpo JSON-RPC. A resposta do request pode ser um objeto JSON ou um stream SSE vinculado àquele request. A especificação remove GET, sessões de transporte e IDs de evento usados para redelivery; após quebra do stream, o cliente reenvia a operação como novo request com novo ID, avaliando antes se a operação é segura para repetição.

## Exemplo
Um cliente envia `tools/call` por POST e recebe uma resposta SSE de longa duração. Se a conexão cair antes da resposta final, ele cria um novo request ID e repete apenas quando o tool usa uma chave idempotente ou pode confirmar o resultado anterior por consulta. O servidor não depende de sticky sessions para recuperar estado oculto da conexão.

## Limites e trade-offs
Este contrato é específico à revisão 2026-07-28 e quebra compatibilidade com bindings antigas que exigem GET ou `Mcp-Session-Id`. POST repetido pode executar uma ação duas vezes; o protocolo não transforma operações arbitrárias em idempotentes. Controles de `Origin`, TLS e autorização continuam necessários conforme implantação.

## Como verificar
Compare a implementação com o changelog da versão, teste JSON e SSE, corte a conexão antes e depois do efeito externo e confirme o uso de novo ID na repetição. Interopere também com um servidor legado para exercitar a negociação de versão.

## Conexões
- [[mcp-stdio-framing-e-stdout-limpo]] — MCP stdio: framing por linha e stdout exclusivo do protocolo.
- [[mcp-meta-protocolo-capacidades-por-request]] — MCP 2026: carregar versão e capacidades em _meta por request.

## Fontes
- [MCP 2026-07-28 — Transportes](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports) — resume a binding HTTP atual como POST único com resposta JSON ou SSE por request Consulta: 2026-10-04.
- [MCP 2026-07-28 — Changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog) — registra remoção de GET, sessão, `Mcp-Session-Id` e resumibilidade de SSE Consulta: 2026-10-04.
