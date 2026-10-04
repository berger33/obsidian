---
id: software.criacao_ia.tranche01.000006
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

# Copilot: pedir explicação de código existente

## Em uma frase

Perguntas sobre fluxo, dependências e contratos ajudam a entender uma base antes de propor alterações nela.

## Por que importa

Compreender a intenção original reduz refatorações que removem compatibilidade ou contornam invariantes desconhecidas.

## Como funciona

Peça que a resposta cite os símbolos e arquivos que sustentam cada conclusão e separe fatos observados de hipóteses.

## Exemplo

Antes de alterar cache, solicite o caminho de leitura e invalidação, incluindo quem chama cada método e quais testes o cobrem.

## Limites e trade-offs

A explicação pode inferir propósito a partir de nomes incompletos; uma resposta segura em tom não é evidência de que o código faz aquilo.

## Como verificar

Abra cada arquivo citado, rastreie as chamadas no projeto e confirme a interpretação com testes ou documentação mantida pela equipe.

## Conexões
- [[copilot-tratar-sugestoes-como-rascunho]] — Copilot: tratar sugestões como rascunho.
- [[copilot-gerar-testes-a-partir-de-comportamento]] — Copilot: gerar testes a partir de comportamento.

## Fontes
- [GitHub Docs — Prompt engineering para Copilot Chat](https://docs.github.com/copilot/concepts/prompt-engineering-for-copilot-chat) — Orientações oficiais para prompts com contexto, objetivo e detalhes concretos. Consulta: 2026-10-04.
- [GitHub Docs — Fazer perguntas ao Copilot na IDE](https://docs.github.com/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide) — Documenta os modos Ask, Edit, Agent e Plan e o uso no ambiente de desenvolvimento. Consulta: 2026-10-04.
