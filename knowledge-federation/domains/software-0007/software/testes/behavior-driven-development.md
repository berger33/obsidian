---
id: software.testes.bdd.000001
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
aliases: ["Behavior-driven development", "BDD descreve comportamento em exemplos compartilhados"]
lote: software-testes-2000-0001
---

# BDD descreve comportamento em exemplos compartilhados

## Em uma frase
Behavior-driven development (BDD) expressa comportamento desejado por meio de exemplos em linguagem simples, entendidos por negócio, desenvolvimento e teste.

## Por que importa
Uma regra descrita apenas em termos técnicos pode ser interpretada de forma diferente por quem define o produto. Exemplos concretos ajudam o grupo a discutir condições, ações e resultados antes de implementar.

## Como funciona
O CTFL inclui BDD entre abordagens test-first: exemplos podem ser redigidos em linguagem natural e frequentemente usam a estrutura Given/When/Then. Esses exemplos descrevem contexto inicial, evento e resultado esperado; podem depois ser ligados a testes executáveis. A linguagem precisa expressar comportamento observável, sem transformar detalhes internos em requisito público.

## Exemplo
Given que uma conta tem sessão ativa, when o prazo de inatividade configurado expira, then novas operações exigem autenticação. O grupo pode discutir se a contagem considera qualquer chamada autenticada ou apenas interação visual antes de codificar.

## Limites e trade-offs
Sintaxe Given/When/Then não garante clareza. Cenários duplicados ou muito detalhados como scripts de implementação podem ficar caros de manter e afastar stakeholders.

## Como verificar
Peça a representantes de produto, desenvolvimento e teste que expliquem o mesmo exemplo; procure termos ambíguos e confirme que o resultado é observável.

## Conexões
- [[test-first-approaches-tdd-atdd-bdd]] — compara TDD, ATDD e BDD.
- [[early-frequent-stakeholder-feedback]] — promove feedback precoce sobre entendimento.

## Fontes
- [ASTQB — CTFL §2.1.3, Testing as a Driver for Software Development](https://astqb.org/2-1-testing-in-the-context-of-a-software-development-lifecycle-sdlc/) — BDD e linguagem de exemplos; acesso em 2026-10-01.
- [ISTQB CTFL Syllabus v4.0.1](https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf) — §2.1.3; acesso em 2026-10-01.
