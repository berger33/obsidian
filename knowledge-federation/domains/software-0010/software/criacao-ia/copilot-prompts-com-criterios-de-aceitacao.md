---
id: software.criacao_ia.tranche01.000001
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

# Copilot: prompts com critérios de aceitação

## Em uma frase

Um pedido útil descreve o resultado observável, o contexto relevante e os critérios que tornam a alteração aceitável.

## Por que importa

Critérios claros reduzem respostas plausíveis que não resolvem a tarefa e permitem comparar o código gerado com o comportamento desejado.

## Como funciona

Declare comportamento esperado, arquivos ou módulos relevantes, restrições de compatibilidade e como a equipe pretende validar a mudança.

## Exemplo

Para um formulário, peça validação de e-mail, mensagens acessíveis e preservação dos dados já preenchidos; indique também os testes esperados.

## Limites e trade-offs

Um prompt detalhado não prova que a especificação está correta nem substitui decisões de produto, segurança ou arquitetura.

## Como verificar

Compare cada critério solicitado com diff e testes; marque explicitamente o que não foi implementado ou permaneceu ambíguo.

## Conexões
- [[copilot-fornecer-contexto-de-repositorio]] — Copilot: fornecer contexto de repositório.

## Fontes
- [GitHub Docs — Prompt engineering para Copilot Chat](https://docs.github.com/copilot/concepts/prompt-engineering-for-copilot-chat) — Orientações oficiais para prompts com contexto, objetivo e detalhes concretos. Consulta: 2026-10-04.
- [GitHub Docs — Fazer perguntas ao Copilot na IDE](https://docs.github.com/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide) — Documenta os modos Ask, Edit, Agent e Plan e o uso no ambiente de desenvolvimento. Consulta: 2026-10-04.
