---
id: software.criacao_ia.tranche03.000211
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
fontes: ["https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio", "https://www.jsonrpc.org/specification"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# MCP stdio: framing por linha e stdout exclusivo do protocolo

## Em uma frase
No transporte stdio do MCP, cada mensagem JSON-RPC ocupa uma linha e toda a saída padrão do servidor precisa ser uma mensagem MCP válida.

## Por que importa
Um banner de inicialização, log colorido ou traceback escrito em `stdout` corrompe o framing e pode fazer o cliente interpretar texto como uma resposta JSON-RPC. O defeito frequentemente parece falha de handshake, embora a causa esteja no processo servidor ou numa biblioteca que escreve diretamente na saída padrão.

## Como funciona
O cliente inicia o servidor como subprocesso; o servidor lê requests de `stdin` e escreve respostas e notificações em `stdout`. Cada mensagem termina por newline e não contém newline embutido. Use `stderr` para logs, inclusive informativos, e não suponha que qualquer conteúdo em `stderr` signifique erro. Em MCP 2026-07-28, as interações de servidor para cliente são representadas em resultados de input requerido; o servidor não emite requests JSON-RPC espontâneos em `stdout`.

## Exemplo
Ao iniciar um servidor Python, encaminhe logging para `stderr` e deixe `stdout` reservado ao writer do SDK. Um teste de integração captura a saída bruta do subprocesso, separa por linhas e tenta decodificar cada linha como objeto JSON-RPC, inclusive enquanto logs de diagnóstico são produzidos.

## Limites e trade-offs
A regra descreve o framing do transporte, não a semântica completa de cada método. Bibliotecas de terceiros ainda podem escrever em stdout, e um cliente pode capturar ou ignorar stderr. Versões anteriores podem ainda usar handshake `initialize` e devem ser negociadas separadamente.

## Como verificar
Execute o servidor com logging em níveis debug e error, gere requests simultâneos e valide todas as linhas de stdout contra o schema JSON-RPC. Confirme encerramento ao fechar stdin e verifique que nenhuma dependência imprime banner no canal do protocolo.

## Conexões
- [[mcp-streamable-http-versao-2026-stateless]] — MCP Streamable HTTP 2026: requests POST sem sessão implícita.

## Fontes
- [MCP 2026-07-28 — Transporte stdio](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio) — define a delimitação por newline, canais stdin/stdout/stderr e regras de encerramento Consulta: 2026-10-04.
- [JSON-RPC 2.0](https://www.jsonrpc.org/specification) — define a estrutura de requests, respostas e notificações que o framing carrega Consulta: 2026-10-04.
