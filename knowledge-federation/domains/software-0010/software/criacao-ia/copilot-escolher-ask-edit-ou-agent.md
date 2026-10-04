---
id: software.criacao_ia.tranche01.000003
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

# Copilot: escolher Ask, Edit ou Agent

## Em uma frase

Os modos da IDE variam entre responder sobre o código, propor edições localizadas e executar uma tarefa com maior autonomia.

## Por que importa

Escolher o modo conforme o risco controla a quantidade de alterações que precisam de revisão e reduz ações fora do escopo.

## Como funciona

Use Ask para entender ou planejar, Edit para mudanças delimitadas e Agent para trabalho em várias etapas que possa ser inspecionado e interrompido.

## Exemplo

Investigue primeiro por que um teste falha em Ask; depois solicite uma edição pequena, reservando Agent para aplicar a correção e executar verificações.

## Limites e trade-offs

Nomes e recursos dos modos podem mudar por produto e versão; autonomia maior não significa que cada ação seja correta ou autorizada.

## Como verificar

Confirme o modo visível na IDE, examine arquivos alterados e valide que nenhuma ação excedeu a tarefa autorizada.

## Conexões
- [[copilot-fornecer-contexto-de-repositorio]] — Copilot: fornecer contexto de repositório.
- [[copilot-dividir-mudancas-em-tarefas-pequenas]] — Copilot: dividir mudanças em tarefas pequenas.

## Fontes
- [GitHub Docs — Prompt engineering para Copilot Chat](https://docs.github.com/copilot/concepts/prompt-engineering-for-copilot-chat) — Orientações oficiais para prompts com contexto, objetivo e detalhes concretos. Consulta: 2026-10-04.
- [GitHub Docs — Fazer perguntas ao Copilot na IDE](https://docs.github.com/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide) — Documenta os modos Ask, Edit, Agent e Plan e o uso no ambiente de desenvolvimento. Consulta: 2026-10-04.
