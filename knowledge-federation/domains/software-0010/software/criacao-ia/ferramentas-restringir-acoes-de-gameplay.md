---
id: software.criacao_ia.tranche01.000027
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
fontes: ["https://platform.openai.com/docs/guides/function-calling", "https://platform.openai.com/docs/guides/structured-outputs"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Ferramentas: restringir ações de gameplay

## Em uma frase

Uma ferramenta de jogo deve expor ações de domínio delimitadas em vez de aceitar comandos arbitrários do modelo.

## Por que importa

Allowlist reduz o impacto de geração incorreta e facilita revisar o que o agente pode controlar na partida.

## Como funciona

Mapeie operações para ações permitidas, verifique fase da partida e estado do jogador, e mantenha decisão competitiva no servidor.

## Exemplo

Um NPC pode pedir diálogo de uma lista aprovada, mas não alterar saldo, inventário ou resultado da partida sem regra explícita.

## Limites e trade-offs

Um modelo pode chamar a opção válida no momento errado, repetir uma ação ou tentar influenciar o estado além de seu papel.

## Como verificar

Teste todas as transições legais e ilegais da partida e registre qual regra bloqueou cada tentativa.

## Conexões
- [[validacao-de-argumentos-de-ferramentas]] — Validação de argumentos de ferramentas.
- [[ferramentas-pedir-confirmacao-antes-de-efeitos-externos]] — Ferramentas: pedir confirmação antes de efeitos externos.

## Fontes
- [OpenAI API — Function calling](https://platform.openai.com/docs/guides/function-calling) — Define o ciclo de chamada de ferramenta entre modelo, aplicativo e resultado de ferramenta. Consulta: 2026-10-04.
- [OpenAI API — Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs) — Documenta respostas compatíveis com esquemas JSON e suas limitações. Consulta: 2026-10-04.
