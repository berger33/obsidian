---
id: software.criacao_ia.tranche02.000109
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

# Anthropic API: depurar layouts com mensagens de visão

## Em uma frase
O envio de capturas de tela e mockups como blocos de imagem multimodal auxilia na correção de bugs visuais de interface.

## Por que importa
Erros de renderização de UI e shaders nem sempre são evidentes apenas no código-fonte, exigindo análise de pixels e layout.

## Como funciona
Inclua blocos de imagem em Base64 ou URL no array de conteúdo da mensagem do usuário, solicitando ao modelo a identificação de sobreposições, margens desalinhadas ou artefatos de renderização.

## Exemplo
```json
{
  "role": "user",
  "content": [
    {
      "type": "image",
      "source": {
        "type": "base64",
        "media_type": "image/png",
        "data": "iVBORw0KGgoAAAANSUhEUgAA..."
      }
    },
    {
      "type": "text",
      "text": "Identifique por que o botao de login esta sobrepondo o menu lateral nesta tela."
    }
  ]
}
```

## Limites e trade-offs
Imagens com alta resolução geram custo elevado de tokens de visão e não substituem o teste visual automatizado em navegadores reais.

## Como verificar
Submeta uma captura de interface com um elemento propositalmente deslocado e verifique se o modelo aponta a coordenada e classe CSS correspondente.

## Conexões
- [[anthropic-api-controlar-limites-com-max-tokens]] — Veja também: Anthropic API: controlar limites com max_tokens e stop_sequences.
- [[claude-code-validar-testes-antes-do-commit]] — Veja também: Claude Code: validar testes e diff antes do commit.
- [[documentacao-usar-imagens-acessiveis-e-uteis]] — Conexão temática direta com documentacao-usar-imagens-acessiveis-e-uteis.
- [[claude-code-iniciar-sessao-interativa-cli]] — Conexão temática direta com claude-code-iniciar-sessao-interativa-cli.
- [[cursor-composer-coordenar-edicoes-multi-arquivo]] — Conexão temática direta com cursor-composer-coordenar-edicoes-multi-arquivo.

## Fontes
- [Anthropic Docs — Claude Code Overview](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview) — Documentação oficial da cli claude code, comandos interativos, claude.md e arquitetura de agentes. Consulta: 2026-10-04.
- [Anthropic Docs — Claude Code Tutorials](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/tutorials) — Tutoriais oficiais de uso prático, permissões no terminal, ferramentas e fluxos de trabalho. Consulta: 2026-10-04.
