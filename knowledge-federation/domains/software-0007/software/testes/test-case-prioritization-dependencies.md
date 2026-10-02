---
id: software.testes.test-case-prioritization.000001
tipo: pratica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-04.md"
fontes: ["https://astqb.org/5-1-test-planning/", "https://astqb.org/assets/documents/CTFL-4.0-Sample-Exam3-2-Answers.pdf"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Test case prioritization, Test execution schedule, Priorização de casos de teste]
lote: software-testes-2000-0001
---

# Priorização e ordenação de casos de teste

## Em uma frase
Priorização define a ordem de execução de casos para obter feedback útil mais cedo, equilibrando risco, cobertura, requisitos, dependências e recursos disponíveis.

## Por que importa
Quando não há tempo para executar tudo imediatamente, a sequência afeta quais defeitos ou bloqueios serão descobertos primeiro. Priorizar apenas por uma etiqueta estática pode atrasar feedback de alto valor se casos dependerem de outros ou de um ambiente que só está disponível em uma janela específica.

## Como funciona
O ISTQB descreve estratégias baseadas em risco, cobertura e prioridade de requisitos. Uma variante de cobertura adicional escolhe o teste com maior cobertura ainda não obtida, em vez de somar repetidamente a cobertura total. Idealmente, a agenda segue as prioridades definidas, mas dependências podem obrigar a executar antes um caso nominalmente menos prioritário. A disponibilidade de ferramentas, pessoas e ambientes também altera a ordem prática. A agenda deve tornar explícitas essas decisões, sem confundir prioridade com severidade ou com probabilidade de aprovação.

## Exemplo
Suponha que o teste `T5` seja de prioridade alta porque valida liquidação, mas só possa rodar depois de `T2`, que cria a conta; `T2` depende de `T1`, que cadastra o cliente. A ordem executável começa `T1 → T2 → T5`, mesmo que `T5` tenha prioridade nominal mais alta. Se `T3` executa rapidamente e cobre um risco urgente sem dependências, pode ser inserido antes para dar feedback rápido.

## Limites e trade-offs
Cobertura incremental depende da métrica e do conjunto de testes disponíveis; cobertura maior não significa sempre maior redução de risco. Priorização pode deixar casos de baixa prioridade sem execução e deve registrar essa lacuna. Dependências mal modeladas e ambientes compartilhados podem invalidar o cronograma.

## Como verificar
Mantenha as prioridades com justificativa, dependências e recursos explícitos. Gere uma ordem executável, verifique pré-condições e confirme se os primeiros casos reduzem riscos ou desbloqueiam trabalho importante. Compare a agenda prevista com a execução real e reordene quando evidências mudarem.

## Conexões
- [[regression-test-prioritization-risco-impacto]] — aplica priorização ao subconjunto de regressão após mudança.
- [[risk-based-testing-priorizacao-risco]] — fornece avaliação de risco para ordenar casos.
- [[combinatorial-testing-pairwise-t-way]] — ajuda a selecionar interações; não determina sozinha a ordem de execução.

## Fontes
- [ASTQB — ISTQB CTFL §5.1: Test Planning](https://astqb.org/5-1-test-planning/) — estratégias de prioridade por risco, cobertura e requisitos; acesso em 2026-10-01.
- [ASTQB — CTFL v4.0 Sample Exam #3 Answers](https://astqb.org/assets/documents/CTFL-4.0-Sample-Exam3-2-Answers.pdf) — exemplo de dependências e ordem executável; acesso em 2026-10-01.
