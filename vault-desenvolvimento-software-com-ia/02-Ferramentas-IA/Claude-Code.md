---
tipo: ferramenta
dominio: ferramentas-ia
nivel: iniciante
confianca: media
ultima_verificacao: 2026-09-30
validade: volatil
fontes: ["https://code.claude.com/docs/en/overview"]
tags: ["dominio/ferramentas-ia", "ferramenta/cli-agent", "nivel/iniciante", "tipo/ferramenta"]
aliases: ["Claude Code", "CLI agent"]
---

# Claude Code

> [!warning] Informação volátil
> Preços, planos, limites de modelos e disponibilidade mudam rapidamente. Revise as fontes oficiais antes de decidir.

## Em uma frase
Agente de coding da anthropic para terminal, ide, desktop e web. Esta nota é tratada como fato operacional dentro do vault.

## Por que importa
Para um orquestrador de IA, Claude Code importa porque ajuda a decidir **o que pedir**, **qual ferramenta usar**, **quais riscos revisar** e **como verificar se a entrega é confiável**. O objetivo não é decorar APIs, mas criar julgamento: saber quando delegar, quando limitar autonomia e quando exigir evidência.

## Como funciona
Na prática, comece definindo o resultado observável, o contexto mínimo e os critérios de aceite. Depois escolha a ferramenta ou stack compatível com o escopo. Em tarefas com IA, transforme a ideia em contrato de tarefa: objetivo, restrições, arquivos relevantes, testes esperados e formato de entrega. Em seguida revise o diff, rode validações e registre decisões.

Exemplo: em vez de pedir "faça um sistema", peça "implemente um protótipo pequeno que demonstre Claude Code, com README, testes mínimos e lista de limitações".

## Quando usar / quando não usar
Use quando o tema resolver uma decisão real do projeto, reduzir incerteza ou acelerar aprendizado. Não use por moda, se o custo cognitivo for maior que o benefício, se a ferramenta exigir dados sensíveis sem governança, ou se você não conseguir verificar o resultado.

## Ferramentas e alternativas
- [[Cursor]]
- [[GitHub-Copilot]]
- [[Claude-Code]]
- [[OpenAI-Codex]]
- [[Gemini-CLI]]

## Armadilhas e erros comuns
- Aceitar output de IA sem executar testes ou checar documentação.
- Misturar requisito, solução e implementação no mesmo pedido.
- Ignorar custos de tokens, licenças, privacidade e manutenção.
- Criar abstrações antes de ter um caso de uso real.

## Como pedir isso para uma IA
```text
Você é meu agente de desenvolvimento. Explique e aplique 'Claude Code' no meu projeto. Primeiro leia a documentação/repositório relevante, proponha um plano, liste riscos, gere apenas mudanças pequenas e verificáveis, rode testes/comandos de validação e devolva um resumo com arquivos alterados, critérios de aceite e dúvidas.
```
Como verificar: Verifique comparando com a documentação oficial, lendo diffs, executando testes, procurando APIs inexistentes e pedindo evidência de cada decisão técnica.

## Conexões
- [[MOC-Ferramentas-IA]] — mapa do domínio para voltar ao panorama.
- [[Home]] — entrada do vault e navegação geral.
- [[Cursor]] — conexão conceitual/prática para aprofundar ou comparar.
- [[GitHub-Copilot]] — conexão conceitual/prática para aprofundar ou comparar.
- [[OpenAI-Codex]] — conexão conceitual/prática para aprofundar ou comparar.
- [[Gemini-CLI]] — conexão conceitual/prática para aprofundar ou comparar.
- [[Windsurf]] — conexão conceitual/prática para aprofundar ou comparar.
- [[Devin]] — conexão conceitual/prática para aprofundar ou comparar.

## Fontes
- https://code.claude.com/docs/en/overview — fonte registrada, acesso em 2026-09-30.
