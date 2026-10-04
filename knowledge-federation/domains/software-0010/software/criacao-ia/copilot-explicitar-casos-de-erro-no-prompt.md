---
id: software.criacao_ia.tranche01.000008
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-01.md"
fontes: ["https://docs.github.com/copilot/concepts/prompt-engineering-for-copilot-chat", "https://docs.github.com/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Copilot: explicitar casos de erro no prompt

## Em uma frase

Descrever falhas previsíveis orienta o assistente a tratar caminhos que exemplos felizes deixam de fora.

## Por que importa

Apps reais recebem entradas ausentes, atrasos, permissões negadas e dependências indisponíveis; ignorá-los cria comportamento frágil.

## Como funciona

Liste condições de erro, resposta da interface, política de repetição e estado que deve ser preservado, sem deixar decisões implícitas.

## Exemplo

Para upload, diga o que mostrar quando o arquivo excede o limite, a rede cai ou o servidor rejeita o formato.

## Limites e trade-offs

Não se deve inventar recuperação automática que possa repetir cobrança, duplicar gravação ou expor detalhes internos.

## Como verificar

Simule cada falha e verifique mensagem segura, estado final consistente, telemetria adequada e possibilidade de retomar sem duplicar efeitos.

## Conexões
- [[copilot-gerar-testes-a-partir-de-comportamento]] — Copilot: gerar testes a partir de comportamento.
- [[copilot-registrar-instrucoes-do-repositorio]] — Copilot: registrar instruções do repositório.

## Fontes
- [GitHub Docs — Prompt engineering para Copilot Chat](https://docs.github.com/copilot/concepts/prompt-engineering-for-copilot-chat) — Orientações oficiais para prompts com contexto, objetivo e detalhes concretos. Consulta: 2026-10-04.
- [GitHub Docs — Fazer perguntas ao Copilot na IDE](https://docs.github.com/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide) — Documenta os modos Ask, Edit, Agent e Plan e o uso no ambiente de desenvolvimento. Consulta: 2026-10-04.
