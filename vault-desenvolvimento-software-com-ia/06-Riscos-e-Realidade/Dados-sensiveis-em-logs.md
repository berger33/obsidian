---
tipo: conceito
dominio: riscos
nivel: intermediario
confianca: media
ultima_verificacao: 2026-09-30
validade: volatil
fontes: ["https://owasp.org/www-project-top-10-for-large-language-model-applications/", "https://owasp.org/www-project-application-security-verification-standard/", "https://www.gov.br/anpd/pt-br", "https://spdx.org/licenses/"]
tags: ["dominio/riscos", "nivel/intermediario", "tipo/conceito"]
aliases: ["Dados sensiveis em logs"]
---

# Dados sensiveis em logs

> [!warning] Informação volátil
> Preços, planos, limites de modelos e disponibilidade mudam rapidamente. Revise as fontes oficiais antes de decidir.

## Em uma frase
Risco prático a controlar ao orquestrar ia em desenvolvimento: dados sensiveis em logs. Esta nota é tratada como fato operacional dentro do vault.

## Por que importa
Para um orquestrador de IA, Dados sensiveis em logs importa porque ajuda a decidir **o que pedir**, **qual ferramenta usar**, **quais riscos revisar** e **como verificar se a entrega é confiável**. O objetivo não é decorar APIs, mas criar julgamento: saber quando delegar, quando limitar autonomia e quando exigir evidência.

## Como funciona
Na prática, comece definindo o resultado observável, o contexto mínimo e os critérios de aceite. Depois escolha a ferramenta ou stack compatível com o escopo. Em tarefas com IA, transforme a ideia em contrato de tarefa: objetivo, restrições, arquivos relevantes, testes esperados e formato de entrega. Em seguida revise o diff, rode validações e registre decisões.

Exemplo: em vez de pedir "faça um sistema", peça "implemente um protótipo pequeno que demonstre Dados sensiveis em logs, com README, testes mínimos e lista de limitações".

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
Você é meu agente de desenvolvimento. Explique e aplique 'Dados sensiveis em logs' no meu projeto. Primeiro leia a documentação/repositório relevante, proponha um plano, liste riscos, gere apenas mudanças pequenas e verificáveis, rode testes/comandos de validação e devolva um resumo com arquivos alterados, critérios de aceite e dúvidas.
```
Como verificar: Verifique comparando com a documentação oficial, lendo diffs, executando testes, procurando APIs inexistentes e pedindo evidência de cada decisão técnica.

## Conexões
- [[MOC-Riscos-e-Realidade]] — mapa do domínio para voltar ao panorama.
- [[Home]] — entrada do vault e navegação geral.
- [[Limites-do-vibe-coding]] — conexão conceitual/prática para aprofundar ou comparar.
- [[Alucinacoes-em-APIs]] — conexão conceitual/prática para aprofundar ou comparar.
- [[Vulnerabilidades-em-codigo-gerado]] — conexão conceitual/prática para aprofundar ou comparar.
- [[Divida-tecnica-invisivel]] — conexão conceitual/prática para aprofundar ou comparar.
- [[Dependencia-de-ferramenta]] — conexão conceitual/prática para aprofundar ou comparar.
- [[Lock-in-de-fornecedor-IA]] — conexão conceitual/prática para aprofundar ou comparar.

## Fontes
- https://owasp.org/www-project-top-10-for-large-language-model-applications/ — fonte registrada, acesso em 2026-09-30.
- https://owasp.org/www-project-application-security-verification-standard/ — fonte registrada, acesso em 2026-09-30.
- https://www.gov.br/anpd/pt-br — fonte registrada, acesso em 2026-09-30.
- https://spdx.org/licenses/ — fonte registrada, acesso em 2026-09-30.
