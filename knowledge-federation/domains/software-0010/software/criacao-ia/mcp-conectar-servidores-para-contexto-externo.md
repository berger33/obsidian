---
id: software.criacao_ia.tranche02.000105
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-02.md"
fontes: ["https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview", "https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/tutorials"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Model Context Protocol: conectar servidores MCP de contexto

## Em uma frase
O Model Context Protocol (MCP) padroniza a integração entre modelos de IA e fontes externas de dados e ferramentas.

## Por que importa
Uma interface uniforme de protocolo evita a criação de conectores proprietários para cada banco de dados, issue tracker ou ambiente de desenvolvimento.

## Como funciona
Configure servidores MCP em um arquivo de configuração JSON local. O assistente descobre dinamicamente recursos disponíveis, templates de prompt e ferramentas expostas pelo servidor MCP via protocolo JSON-RPC.

## Exemplo
```json
{
  "mcpServers": {
    "git-history": {
      "command": "mcp-server-git",
      "args": ["--repository", "/home/user/meu-projeto"]
    },
    "postgres-dev": {
      "command": "mcp-server-postgres",
      "args": ["postgresql://localhost:5432/game_dev"]
    }
  }
}
```

## Limites e trade-offs
Servidores MCP executam localmente com privilégios do usuário; configurações incorretas podem expor dados sensíveis ou conexões não autorizadas.

## Como verificar
Inicie o assistente apontando para o arquivo de configuração MCP e execute uma consulta exigindo listagem de ferramentas para verificar os endpoints disponíveis.

## Conexões
- [[claude-code-usar-prompt-caching-para-bases-extensas]] — Veja também: Anthropic API: aplicar Prompt Caching em bases extensas.
- [[anthropic-api-estruturar-mensagens-tool-result]] — Veja também: Anthropic API: estruturar mensagens de retorno em tool_result.
- [[function-calling-declarar-contrato-de-ferramenta]] — Conexão temática direta com function-calling-declarar-contrato-de-ferramenta.
- [[claude-code-iniciar-sessao-interativa-cli]] — Conexão temática direta com claude-code-iniciar-sessao-interativa-cli.

## Fontes
- [Anthropic Docs — Claude Code Overview](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview) — Documentação oficial da cli claude code, comandos interativos, claude.md e arquitetura de agentes. Consulta: 2026-10-04.
- [Anthropic Docs — Claude Code Tutorials](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/tutorials) — Tutoriais oficiais de uso prático, permissões no terminal, ferramentas e fluxos de trabalho. Consulta: 2026-10-04.
