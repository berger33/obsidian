---
tipo: conceito
dominio: fundamentos
nivel: iniciante
confianca: media
ultima_verificacao: 2026-09-30
validade: estavel
fontes: ["https://docs.github.com/en/copilot", "https://github.com/features/copilot/plans", "https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/", "https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/"]
tags: ["dominio/fundamentos", "nivel/iniciante", "tipo/conceito"]
aliases: [".cursorrules", "Cursor Rules"]
---

# Cursor rules

## Em uma frase
Regras de projeto usadas para orientar o cursor e agentes compatíveis. Esta nota é tratada como fato operacional dentro do vault.

## Por que importa
Para um orquestrador de IA, Cursor rules importa porque ajuda a decidir **o que pedir**, **qual ferramenta usar**, **quais riscos revisar** e **como verificar se a entrega é confiável**. O objetivo não é decorar APIs, mas criar julgamento: saber quando delegar, quando limitar autonomia e quando exigir evidência.

## Como funciona
Na prática, comece definindo o resultado observável, o contexto mínimo e os critérios de aceite. Depois escolha a ferramenta ou stack compatível com o escopo. Em tarefas com IA, transforme a ideia em contrato de tarefa: objetivo, restrições, arquivos relevantes, testes esperados e formato de entrega. Em seguida revise o diff, rode validações e registre decisões.

Exemplo: em vez de pedir "faça um sistema", peça "implemente um protótipo pequeno que demonstre Cursor rules, com README, testes mínimos e lista de limitações".

## Quando usar / quando não usar
Use quando o tema resolver uma decisão real do projeto, reduzir incerteza ou acelerar aprendizado. Não use por moda, se o custo cognitivo for maior que o benefício, se a ferramenta exigir dados sensíveis sem governança, ou se você não conseguir verificar o resultado.

## Ferramentas e alternativas
- [[Claude-Code]]
- [[GitHub-Copilot]]
- [[MCP-Model-Context-Protocol]]
- [[Context-engineering]]
- [[Validacao-de-codigo-gerado-por-IA]]

## Armadilhas e erros comuns
- Aceitar output de IA sem executar testes ou checar documentação.
- Misturar requisito, solução e implementação no mesmo pedido.
- Ignorar custos de tokens, licenças, privacidade e manutenção.
- Criar abstrações antes de ter um caso de uso real.

## Como pedir isso para uma IA
```text
Você é meu agente de desenvolvimento. Explique e aplique 'Cursor rules' no meu projeto. Primeiro leia a documentação/repositório relevante, proponha um plano, liste riscos, gere apenas mudanças pequenas e verificáveis, rode testes/comandos de validação e devolva um resumo com arquivos alterados, critérios de aceite e dúvidas.
```
Como verificar: Verifique comparando com a documentação oficial, lendo diffs, executando testes, procurando APIs inexistentes e pedindo evidência de cada decisão técnica.

## Conexões
- [[MOC-Fundamentos]] — mapa do domínio para voltar ao panorama.
- [[Home]] — entrada do vault e navegação geral.
- [[Vibe-coding]] — conexão conceitual/prática para aprofundar ou comparar.
- [[Desenvolvimento-assistido-por-IA]] — conexão conceitual/prática para aprofundar ou comparar.
- [[Engenharia-agentica]] — conexão conceitual/prática para aprofundar ou comparar.
- [[Programacao-em-linguagem-natural]] — conexão conceitual/prática para aprofundar ou comparar.
- [[Historico-autocomplete-chat-agentes]] — conexão conceitual/prática para aprofundar ou comparar.
- [[Spec-driven-development]] — conexão conceitual/prática para aprofundar ou comparar.

## Fontes
- https://docs.github.com/en/copilot — fonte registrada, acesso em 2026-09-30.
- https://github.com/features/copilot/plans — fonte registrada, acesso em 2026-09-30.
- https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/ — fonte registrada, acesso em 2026-09-30.
- https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ — fonte registrada, acesso em 2026-09-30.
- https://dora.dev/research/ — fonte registrada, acesso em 2026-09-30.
