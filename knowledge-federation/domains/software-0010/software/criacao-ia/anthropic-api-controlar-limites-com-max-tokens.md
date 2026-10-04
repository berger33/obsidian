---
id: software.criacao_ia.tranche02.000108
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

# Anthropic API: controlar limites com max_tokens e stop_sequences

## Em uma frase
O controle de max_tokens e stop_sequences define a extensão e os critérios de término das gerações de código na API.

## Por que importa
Limitar a extensão de resposta evita loops de geração excessiva e previne truncamentos inesperados em blocos de lógica crítica.

## Como funciona
Especifique o valor de `max_tokens` dimensionado para o tamanho esperado do trecho de código e utilize `stop_sequences` para interromper a resposta assim que marcadores como fechamento de classe forem emitidos.

## Exemplo
```json
{
  "model": "claude-3-7-sonnet-20250219",
  "max_tokens": 1500,
  "stop_sequences": ["// END_OF_MODULE"],
  "messages": [
    {"role": "user", "content": "Gere a funcao de ordenacao rapida terminando com // END_OF_MODULE"}
  ]
}
```

## Limites e trade-offs
Valores de `max_tokens` excessivamente baixos provocam respostas incompletas com `stop_reason: "max_tokens"`, gerando sintaxe quebrada.

## Como verificar
Examine o campo `stop_reason` na resposta da API para confirmar se a geração terminou pela sequência de parada esperada.

## Conexões
- [[claude-code-orquestrar-subagentes-especializados]] — Veja também: Claude Code: orquestrar subagentes especializados.
- [[anthropic-api-depurar-layout-com-mensagens-de-visao]] — Veja também: Anthropic API: depurar layouts com mensagens de visão.
- [[responses-api-limitar-o-tamanho-da-saida]] — Conexão temática direta com responses-api-limitar-o-tamanho-da-saida.
- [[claude-code-usar-prompt-caching-para-bases-extensas]] — Conexão temática direta com claude-code-usar-prompt-caching-para-bases-extensas.
- [[anthropic-api-estruturar-mensagens-tool-result]] — Conexão temática direta com anthropic-api-estruturar-mensagens-tool-result.

## Fontes
- [Anthropic Docs — Claude Code Overview](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview) — Documentação oficial da cli claude code, comandos interativos, claude.md e arquitetura de agentes. Consulta: 2026-10-04.
- [Anthropic Docs — Claude Code Tutorials](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/tutorials) — Tutoriais oficiais de uso prático, permissões no terminal, ferramentas e fluxos de trabalho. Consulta: 2026-10-04.
