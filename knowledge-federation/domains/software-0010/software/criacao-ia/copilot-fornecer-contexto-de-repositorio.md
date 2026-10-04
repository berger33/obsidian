---
id: software.criacao_ia.tranche01.000002
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

# Copilot: fornecer contexto de repositório

## Em uma frase

O Copilot produz sugestões melhores quando a pergunta identifica linguagem, estrutura do projeto, APIs usadas e trechos pertinentes.

## Por que importa

Contexto escolhido evita recomendações genéricas ou incompatíveis com padrões e dependências já adotados pelo aplicativo.

## Como funciona

Abra os arquivos relevantes, mencione o caminho e a convenção que deve ser preservada, e inclua somente os trechos necessários à tarefa.

## Exemplo

Ao pedir uma tela em React, aponte o componente existente, o hook de dados e um teste vizinho que mostre o estilo do repositório.

## Limites e trade-offs

Contexto excessivo pode distrair; arquivos privados, credenciais e dados de usuários não devem ser incluídos sem autorização e política apropriada.

## Como verificar

Repita a pergunta em uma cópia mínima do contexto e verifique se a resposta identifica a API e os padrões corretos do projeto.

## Conexões
- [[copilot-prompts-com-criterios-de-aceitacao]] — Copilot: prompts com critérios de aceitação.
- [[copilot-escolher-ask-edit-ou-agent]] — Copilot: escolher Ask, Edit ou Agent.

## Fontes
- [GitHub Docs — Prompt engineering para Copilot Chat](https://docs.github.com/copilot/concepts/prompt-engineering-for-copilot-chat) — Orientações oficiais para prompts com contexto, objetivo e detalhes concretos. Consulta: 2026-10-04.
- [GitHub Docs — Fazer perguntas ao Copilot na IDE](https://docs.github.com/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide) — Documenta os modos Ask, Edit, Agent e Plan e o uso no ambiente de desenvolvimento. Consulta: 2026-10-04.
