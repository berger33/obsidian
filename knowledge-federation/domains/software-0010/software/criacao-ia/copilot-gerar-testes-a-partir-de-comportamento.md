---
id: software.criacao_ia.tranche01.000007
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

# Copilot: gerar testes a partir de comportamento

## Em uma frase

Um modelo pode sugerir casos de teste derivados de exemplos, invariantes e condições de erro descritos pelo desenvolvedor.

## Por que importa

Testes com cenários concretos ajudam a revelar lacunas de especificação antes de aceitar uma implementação gerada.

## Como funciona

Forneça entradas, saídas esperadas, estados inválidos e comportamento de borda; peça casos que falhem se o requisito for violado.

## Exemplo

Para um inventário, inclua item inexistente, estoque zero, reserva concorrente e cancelamento, especificando o resultado de cada caso.

## Limites e trade-offs

Testes escritos a partir da mesma suposição incorreta da implementação podem confirmar o bug em vez de encontrá-lo.

## Como verificar

Execute os testes contra implementação anterior e nova quando possível, e acrescente ao menos um caso definido independentemente do código gerado.

## Conexões
- [[copilot-pedir-explicacao-de-codigo-existente]] — Copilot: pedir explicação de código existente.
- [[copilot-explicitar-casos-de-erro-no-prompt]] — Copilot: explicitar casos de erro no prompt.

## Fontes
- [GitHub Docs — Prompt engineering para Copilot Chat](https://docs.github.com/copilot/concepts/prompt-engineering-for-copilot-chat) — Orientações oficiais para prompts com contexto, objetivo e detalhes concretos. Consulta: 2026-10-04.
- [GitHub Docs — Fazer perguntas ao Copilot na IDE](https://docs.github.com/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide) — Documenta os modos Ask, Edit, Agent e Plan e o uso no ambiente de desenvolvimento. Consulta: 2026-10-04.
