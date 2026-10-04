---
id: software.criacao_ia.tranche01.000004
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

# Copilot: dividir mudanças em tarefas pequenas

## Em uma frase

Tarefas curtas e independentes tornam mais fácil fornecer contexto, revisar a solução e localizar a origem de regressões.

## Por que importa

Uma alteração de escopo estreito evita que uma resposta combine refatoração, mudança de interface e atualização de dados sem justificativa.

## Como funciona

Separe descoberta, desenho, implementação, testes e documentação quando cada etapa tiver critérios próprios; mantenha interfaces e limites explícitos.

## Exemplo

Para adicionar busca, implemente primeiro o filtro no serviço, valide-o com testes e só depois conecte o campo da tela e sua documentação.

## Limites e trade-offs

Dividir demais também cria custo de integração e pode ocultar requisitos transversais que precisam ser tratados em conjunto.

## Como verificar

Revise cada commit ou diff por uma intenção principal e rode os testes de integração depois de recombinar as partes.

## Conexões
- [[copilot-escolher-ask-edit-ou-agent]] — Copilot: escolher Ask, Edit ou Agent.
- [[copilot-tratar-sugestoes-como-rascunho]] — Copilot: tratar sugestões como rascunho.

## Fontes
- [GitHub Docs — Prompt engineering para Copilot Chat](https://docs.github.com/copilot/concepts/prompt-engineering-for-copilot-chat) — Orientações oficiais para prompts com contexto, objetivo e detalhes concretos. Consulta: 2026-10-04.
- [GitHub Docs — Fazer perguntas ao Copilot na IDE](https://docs.github.com/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide) — Documenta os modos Ask, Edit, Agent e Plan e o uso no ambiente de desenvolvimento. Consulta: 2026-10-04.
