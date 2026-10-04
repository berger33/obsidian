---
id: software.testes.sdlc-impact.000001
tipo: conceito
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: estavel
status: candidata
revisao_humana: nao_solicitada
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-06.md"
revisor: ""
fontes: ["https://astqb.org/2-1-testing-in-the-context-of-a-software-development-lifecycle-sdlc/", "https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Impact of SDLC on testing", "Como o SDLC muda o escopo e o momento dos testes"]
lote: software-testes-2000-0001
---

# Como o SDLC muda o escopo e o momento dos testes

## Em uma frase
O ciclo de vida de desenvolvimento influencia quando e quais atividades de teste ocorrem, a documentação, as técnicas, a automação e as responsabilidades.

## Por que importa
Uma estratégia copiada de outro projeto pode chegar tarde demais para detectar defeitos de requisitos ou exigir evidências incompatíveis com a cadência de entrega. O CTFL não define um modelo único; pede que o teste seja adaptado ao SDLC escolhido.

## Como funciona
Modelos sequenciais, iterativos e incrementais organizam fases e atividades de formas distintas. Essa escolha afeta o escopo e o momento de níveis e tipos de teste, o detalhe do testware, as técnicas, o grau de automação e o papel dos testers. A resposta adequada é integrar análise, desenho, execução e comunicação ao fluxo real, e não esperar por uma “fase de testes” universal.

## Exemplo
Uma equipe que publica um incremento a cada duas semanas pode revisar histórias antes da implementação e executar regressão em CI. Um programa sequencial pode planejar revisões de especificação e ciclos formais por nível. Ambos ainda precisam decidir que risco será coberto.

## Limites e trade-offs
Iterativo não significa ausência de planejamento; sequencial não impede feedback antecipado. O nome do modelo sozinho não determina o teste necessário.

## Como verificar
Compare a abordagem de teste com fases, entregas, critérios e riscos do SDLC; revise-a quando a cadência ou o produto mudar.

## Conexões
- [[test-process-context-tailoring]] — adapta o processo à situação.
- [[fundamental-test-activities]] — apresenta grupos de atividades que precisam ser planejados.

## Fontes
- [ASTQB — CTFL §2.1, Testing in the Context of an SDLC](https://astqb.org/2-1-testing-in-the-context-of-a-software-development-lifecycle-sdlc/) — fatores do SDLC que afetam teste; acesso em 2026-10-01.
- [ISTQB CTFL Syllabus v4.0.1](https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf) — §§2.1.1–2.1.2; acesso em 2026-10-01.
