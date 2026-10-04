---
id: software.criacao_ia.tranche02.000110
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

# Claude Code: validar testes e diff antes do commit

## Em uma frase
A execução automatizada da suíte de testes antes da conclusão de uma tarefa assegura que regressões sejam barradas no terminal.

## Por que importa
Aceitar sugestões de código sem validação determinística introduz quebras em funcionalidades existentes do projeto.

## Como funciona
Configure o fluxo de trabalho para que o assistente execute o comando de teste configurado após aplicar edições em arquivos e verifique o código de saída do processo antes de finalizar a sessão.

## Exemplo
```bash
# Solicitar ao assistente a aplicacao da alteracao e validacao imediata
> Aplique a correcao no parser de inventario e execute npm test. Nao conclua sem que todos os testes passem.
```

## Limites e trade-offs
Testes lentos ou com mocks ausentes podem travar a sessão interativa ou mascarar falhas de integração em ambientes reais.

## Como verificar
Provoque uma falha intencional em um teste unitário e confira se o assistente identifica a quebra no terminal e propõe a retificação necessária.

## Conexões
- [[anthropic-api-depurar-layout-com-mensagens-de-visao]] — Veja também: Anthropic API: depurar layouts com mensagens de visão.
- [[copilot-inspecionar-o-diff-antes-de-aceitar]] — Conexão temática direta com copilot-inspecionar-o-diff-antes-de-aceitar.
- [[claude-code-definir-instrucoes-claudemd]] — Conexão temática direta com claude-code-definir-instrucoes-claudemd.
- [[qa-jogos-executar-playtests-headless-em-ci]] — Conexão temática direta com qa-jogos-executar-playtests-headless-em-ci.

## Fontes
- [Anthropic Docs — Claude Code Overview](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview) — Documentação oficial da cli claude code, comandos interativos, claude.md e arquitetura de agentes. Consulta: 2026-10-04.
- [Anthropic Docs — Claude Code Tutorials](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/tutorials) — Tutoriais oficiais de uso prático, permissões no terminal, ferramentas e fluxos de trabalho. Consulta: 2026-10-04.
