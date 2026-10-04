---
id: software.criacao_ia.tranche02.000106
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

# Anthropic API: estruturar mensagens de retorno em tool_result

## Em uma frase
O bloco tool_result devolve os dados de execução de uma ferramenta para que o modelo continue o raciocínio na API Anthropic.

## Por que importa
Retornos estruturados com identificação precisa permitem que o modelo interprete saídas de sucesso e mensagens de erro para corrigir seu plano de ação.

## Como funciona
Quando o modelo emite um bloco `tool_use`, a aplicação executa a função localmente e responde com uma mensagem de papel `user` contendo um bloco de tipo `tool_result` com o respectivo `tool_use_id` e o conteúdo textual do resultado.

## Exemplo
```json
{
  "role": "user",
  "content": [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01A098bcde",
      "content": "Arquivo src/utils/math.ts atualizado com sucesso. 0 erros de compilacao."
    }
  ]
}
```

## Limites e trade-offs
Omitir o campo `tool_use_id` correspondente ou enviar formatos de mensagem inválidos invalida a conversa e gera exceção de schema na API.

## Como verificar
Capture uma chamada de ferramenta, execute a rotina e valide se o payload `tool_result` retornado fecha o turno sem erros de requisição.

## Conexões
- [[mcp-conectar-servidores-para-contexto-externo]] — Veja também: Model Context Protocol: conectar servidores MCP de contexto.
- [[claude-code-orquestrar-subagentes-especializados]] — Veja também: Claude Code: orquestrar subagentes especializados.
- [[function-calling-correlacionar-chamadas-pelo-identificador]] — Conexão temática direta com function-calling-correlacionar-chamadas-pelo-identificador.
- [[function-calling-executar-no-aplicativo-nao-no-modelo]] — Conexão temática direta com function-calling-executar-no-aplicativo-nao-no-modelo.

## Fontes
- [Anthropic Docs — Claude Code Overview](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview) — Documentação oficial da cli claude code, comandos interativos, claude.md e arquitetura de agentes. Consulta: 2026-10-04.
- [Anthropic Docs — Claude Code Tutorials](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/tutorials) — Tutoriais oficiais de uso prático, permissões no terminal, ferramentas e fluxos de trabalho. Consulta: 2026-10-04.
