---
id: software.criacao_ia.tranche02.000107
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

# Claude Code: orquestrar subagentes especializados

## Em uma frase
Dividir a resolução de problemas entre subagentes de pesquisa, edição e validação organiza tarefas complexas de engenharia.

## Por que importa
Agentes com escopo delimitado evitam poluição de contexto e reduzem o risco de edições em arquivos não relacionados durante refatorações grandes.

## Como funciona
O agente principal planeja as etapas e despacha subagentes para ler documentações específicas ou buscar referências de código. Os resultados consolidados são repassados ao módulo de edição antes do teste final.

## Exemplo
```bash
# Instruir o assistente a delegar tarefas de investigacao antes da edicao
> Subdivida a tarefa: primeiro use um agente de pesquisa para mapear todas as chamadas a calculateDamage() e depois proponha o refactoring.
```

## Limites e trade-offs
A delegação múltipla aumenta a latência total da operação e o consumo acumulado de requisições à API.

## Como verificar
Monitore os logs de atividade do assistente e confirme se as etapas de leitura e análise precedem as ações de escrita no código.

## Conexões
- [[anthropic-api-estruturar-mensagens-tool-result]] — Veja também: Anthropic API: estruturar mensagens de retorno em tool_result.
- [[anthropic-api-controlar-limites-com-max-tokens]] — Veja também: Anthropic API: controlar limites com max_tokens e stop_sequences.
- [[copilot-dividir-mudancas-em-tarefas-pequenas]] — Conexão temática direta com copilot-dividir-mudancas-em-tarefas-pequenas.
- [[claude-code-iniciar-sessao-interativa-cli]] — Conexão temática direta com claude-code-iniciar-sessao-interativa-cli.
- [[cursor-composer-coordenar-edicoes-multi-arquivo]] — Conexão temática direta com cursor-composer-coordenar-edicoes-multi-arquivo.

## Fontes
- [Anthropic Docs — Claude Code Overview](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview) — Documentação oficial da cli claude code, comandos interativos, claude.md e arquitetura de agentes. Consulta: 2026-10-04.
- [Anthropic Docs — Claude Code Tutorials](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/tutorials) — Tutoriais oficiais de uso prático, permissões no terminal, ferramentas e fluxos de trabalho. Consulta: 2026-10-04.
