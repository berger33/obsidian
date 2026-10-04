---
id: software.testes.tdd.000001
tipo: pratica
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
aliases: ["Test-driven development", "TDD dirige a implementação por testes"]
lote: software-testes-2000-0001
---

# TDD dirige a implementação por testes

## Em uma frase
Test-driven development (TDD) usa casos de teste como direção para escrever código e refatorar, dentro de um ciclo curto de desenvolvimento.

## Por que importa
Testes escritos depois do código podem refletir a implementação sem desafiar suas suposições. TDD cria uma expectativa executável antes da mudança, oferecendo feedback próximo da unidade alterada.

## Como funciona
O CTFL caracteriza TDD como abordagem test-first: os testes são escritos primeiro, o código é então produzido para satisfazê-los, e testes e código podem ser refatorados. O teste persiste como evidência para mudanças futuras. A técnica apoia o princípio de teste antecipado; não é, por si só, uma garantia de cobertura adequada ou de que o comportamento desejado foi especificado corretamente.

## Exemplo
Para validar uma regra de desconto, escreva primeiro casos para a faixa permitida e seus limites, observe a falha inicial, implemente o mínimo necessário e refatore mantendo os testes verdes. Depois complemente com testes de integração se o cálculo depender de outras fronteiras.

## Limites e trade-offs
TDD pode exigir disciplina para evitar testes acoplados a detalhes internos. Ele não substitui testes de sistema, aceitação, revisão de requisitos ou testes não funcionais.

## Como verificar
Observe se uma expectativa relevante existe antes da implementação, se falha quando o comportamento falta e se permanece legível após refatoração.

## Conexões
- [[test-first-approaches-tdd-atdd-bdd]] — compara as abordagens test-first.
- [[component-testing-isolation]] — TDD costuma atuar em granularidade de componente.

## Fontes
- [ASTQB — CTFL §2.1.3, Testing as a Driver for Software Development](https://astqb.org/2-1-testing-in-the-context-of-a-software-development-lifecycle-sdlc/) — sequência conceitual do TDD; acesso em 2026-10-01.
- [ISTQB CTFL Syllabus v4.0.1](https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf) — §2.1.3; acesso em 2026-10-01.
