---
id: software.criacao_ia.tranche03.000219
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
fontes: ["https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization", "https://www.rfc-editor.org/rfc/rfc9728.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# MCP HTTP OAuth: descobrir recurso protegido e registrar cliente

## Em uma frase
A autorização MCP aplica-se a transportes HTTP e usa metadados do recurso protegido para descobrir o servidor de autorização; stdio segue outra fronteira de credenciais.

## Por que importa
Cliente que inicia OAuth a partir de uma URL ad hoc ou reutiliza token emitido por outro issuer pode encaminhar credenciais ao destino incorreto. A revisão 2026-07-28 prioriza Client ID Metadata Documents ou pré-registro e mantém Dynamic Client Registration apenas para compatibilidade.

## Como funciona
O servidor HTTP publica OAuth Protected Resource Metadata com os authorization servers aceitos. O cliente consulta os metadados e a descoberta do servidor de autorização, aplica a seleção exigida e obtém seu client ID por Client ID Metadata Document, pré-registro ou o caminho DCR compatível. Associe credenciais ao issuer que as emitiu e nunca as reapresente a um issuer diferente.

## Exemplo
Um editor conecta um MCP remoto protegido: diante de `401`, lê `resource_metadata`, valida o issuer e inicia a autorização para aquele recurso. Após redirecionamento, verifica o issuer se presente e armazena o token sob a identidade do authorization server, não apenas sob o nome do host exibido na interface.

## Limites e trade-offs
A especificação seleciona partes de OAuth e aponta para drafts e RFCs externos; ela não substitui revisão da configuração do provedor nem tratamento de consentimento de proxy. DCR continua opcional para compatibilidade, não é a primeira escolha declarada na revisão atual.

## Como verificar
Teste descoberta por cabeçalho e well-known URI, issuer alternativo, token expirado, escopos mínimos e troca de provedor. Confirme que stdio não recebe indevidamente fluxo OAuth HTTP e que credenciais persistidas são indexadas por issuer.

## Conexões
- [[mcp-elicitation-form-url-segredos]] — MCP elicitation: reservar URL mode para credenciais e segredos.
- [[mcp-migrar-para-especificacao-2026-07-28]] — MCP 2026-07-28: preparar migração de handshake e notificações.

## Fontes
- [MCP 2026-07-28 — Authorization](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) — define escopo HTTP, metadados de recurso, registro e prioridade entre métodos Consulta: 2026-10-04.
- [RFC 9728 — OAuth 2.0 Protected Resource Metadata](https://www.rfc-editor.org/rfc/rfc9728.html) — define o documento de descoberta do recurso protegido utilizado pelo MCP Consulta: 2026-10-04.
