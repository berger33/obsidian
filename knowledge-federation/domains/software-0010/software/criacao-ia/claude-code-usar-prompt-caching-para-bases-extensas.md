---
id: software.criacao_ia.tranche02.000104
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

# Anthropic API: aplicar Prompt Caching em bases extensas

## Em uma frase
O Prompt Caching armazena prefixos de contexto repetidos para reduzir a latência de inferência e os custos em repositórios grandes.

## Por que importa
Bases de código com centenas de arquivos consomem grande volume de tokens se retransmitidas a cada turno de conversa com o modelo de linguagem.

## Como funciona
Ao estruturar chamadas à API da Anthropic, marque blocos estáticos de contexto como esquemas de sistema e resumos do repositório com o parâmetro `cache_control: {"type": "ephemeral"}`. As requisições subsequentes aproveitam o cache na memória da infraestrutura.

## Exemplo
```json
{
  "model": "claude-3-7-sonnet-20250219",
  "max_tokens": 1024,
  "system": [
    {
      "type": "text",
      "text": "Voce e o assistente de engenharia do projeto. Abaixo esta a arquitetura completa...",
      "cache_control": {"type": "ephemeral"}
    }
  ],
  "messages": [{"role": "user", "content": "Adicione validacao de email no modulo auth."}]
}
```

## Limites e trade-offs
O cache possui tempo de vida efêmero (tipicamente 5 minutos) e requer que os blocos de prefixo sejam idênticos em ordem e conteúdo para produzir cache hits.

## Como verificar
Inspecione os metadados de resposta da API (`usage.cache_creation_input_tokens` e `usage.cache_read_input_tokens`) para confirmar o reaproveitamento efetivo de tokens.

## Conexões
- [[claude-code-gerenciar-permissoes-de-execucao-de-comandos]] — Veja também: Claude Code: gerenciar permissões de execução de comandos.
- [[mcp-conectar-servidores-para-contexto-externo]] — Veja também: Model Context Protocol: conectar servidores MCP de contexto.
- [[responses-api-separar-instrucoes-e-entrada]] — Conexão temática direta com responses-api-separar-instrucoes-e-entrada.
- [[anthropic-api-controlar-limites-com-max-tokens]] — Conexão temática direta com anthropic-api-controlar-limites-com-max-tokens.
- [[cursor-priorizar-janela-de-contexto-essencial]] — Conexão temática direta com cursor-priorizar-janela-de-contexto-essencial.

## Fontes
- [Anthropic Docs — Claude Code Overview](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview) — Documentação oficial da cli claude code, comandos interativos, claude.md e arquitetura de agentes. Consulta: 2026-10-04.
- [Anthropic Docs — Claude Code Tutorials](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/tutorials) — Tutoriais oficiais de uso prático, permissões no terminal, ferramentas e fluxos de trabalho. Consulta: 2026-10-04.
