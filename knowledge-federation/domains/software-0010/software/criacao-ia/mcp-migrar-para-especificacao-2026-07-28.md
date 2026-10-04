---
id: software.criacao_ia.tranche03.000220
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
fontes: ["https://modelcontextprotocol.io/specification/2026-07-28/changelog", "https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# MCP 2026-07-28: preparar migração de handshake e notificações

## Em uma frase
A revisão MCP 2026-07-28 troca o handshake inicial por descoberta e metadados por request e redesenha notificações de mudança como subscriptions explícitas.

## Por que importa
Um cliente que apenas atualiza o número de versão pode continuar emitindo métodos removidos, mantendo estado de conexão ou aguardando mensagens espontâneas do servidor. A versão é uma mudança estrutural e exige atualizar transporte, negociação, fluxo de entrada adicional e operação de subscriptions como um conjunto.

## Como funciona
Use `server/discover` para consultar versões e capacidades compatíveis quando necessário; cada request moderno carrega seu próprio `_meta`. Migre interações servidor-cliente para MRTR e substitua conexões GET ou notificações de sessão por `subscriptions/listen` opt-in. O changelog também move tasks para uma extensão e remove métodos de logging/ping, então consulte o registro versionado antes de manter compatibilidade.

## Exemplo
Um SDK com suporte a 2025 e 2026 envia `server/discover` antes de escolher a semântica. Para uma resposta moderna, ele não chama `initialize`, associa notificação de lista ao subscription ID e reconstrói subscriptions após reiniciar o processo stdio; para um peer antigo, segue o caminho legado documentado.

## Limites e trade-offs
Não há equivalência automática entre sessões antigas, subscriptions novas e estados guardados em servidores. O changelog registra breaking changes que podem exigir atualização coordenada de cliente e servidor. Métodos listados aqui são específicos à revisão de 2026-07-28; confira uma revisão posterior antes de implementar.

## Como verificar
Mantenha uma matriz de compatibilidade entre SDKs e revisões do protocolo. Teste discovery, request metadata, client antigo, servidor moderno, reconnect de subscription e métodos removidos usando fixtures versionadas.

## Conexões
- [[mcp-oauth-discovery-e-client-registration]] — MCP HTTP OAuth: descobrir recurso protegido e registrar cliente.

## Fontes
- [MCP 2026-07-28 — Changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog) — lista mudanças incompatíveis, remoções e alterações de transporte da revisão Consulta: 2026-10-04.
- [MCP 2026-07-28 — Versioning](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning) — descreve descoberta, compatibilidade e negociação entre eras do protocolo Consulta: 2026-10-04.
