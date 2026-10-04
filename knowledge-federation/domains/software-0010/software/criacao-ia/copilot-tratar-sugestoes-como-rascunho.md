---
id: software.criacao_ia.tranche01.000005
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

# Copilot: tratar sugestões como rascunho

## Em uma frase

Código sugerido por um modelo é uma hipótese de implementação que exige leitura, teste e conformidade com as regras do projeto.

## Por que importa

Fluência do texto e aparência idiomática podem esconder defeitos lógicos, incompatibilidades ou dependências inadequadas.

## Como funciona

Leia a alteração linha a linha, compare com o contrato da função e confirme que tratamento de erros e efeitos colaterais permanecem aceitáveis.

## Exemplo

Se o copiloto propõe substituir um parser, compare o comportamento em entradas vazias, Unicode, formatos antigos e conteúdo malformado.

## Limites e trade-offs

A revisão humana também pode falhar; controles automáticos não cobrem todos os riscos de produto e de segurança.

## Como verificar

Peça uma revisão independente do diff, execute análise estática e testes representativos, e registre os casos que continuam sem cobertura.

## Conexões
- [[copilot-dividir-mudancas-em-tarefas-pequenas]] — Copilot: dividir mudanças em tarefas pequenas.
- [[copilot-pedir-explicacao-de-codigo-existente]] — Copilot: pedir explicação de código existente.

## Fontes
- [GitHub Docs — Prompt engineering para Copilot Chat](https://docs.github.com/copilot/concepts/prompt-engineering-for-copilot-chat) — Orientações oficiais para prompts com contexto, objetivo e detalhes concretos. Consulta: 2026-10-04.
- [GitHub Docs — Fazer perguntas ao Copilot na IDE](https://docs.github.com/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide) — Documenta os modos Ask, Edit, Agent e Plan e o uso no ambiente de desenvolvimento. Consulta: 2026-10-04.
