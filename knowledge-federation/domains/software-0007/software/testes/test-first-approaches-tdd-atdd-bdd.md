---
id: software.testes.test-first-overview.000001
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
aliases: ["Test-first approaches TDD ATDD BDD", "Abordagens test-first: TDD, ATDD e BDD"]
lote: software-testes-2000-0001
---

# Abordagens test-first: TDD, ATDD e BDD

## Em uma frase
TDD, ATDD e BDD definem testes antes do código para orientar o desenvolvimento, mas enfatizam níveis e formas de colaboração diferentes.

## Por que importa
“Escrever testes antes” pode significar teste de unidade dirigido por código, critérios de aceitação definidos com negócio ou exemplos de comportamento em linguagem compartilhada. Usar os nomes como sinônimos esconde quem participa e qual decisão os testes apoiam.

## Como funciona
O CTFL apresenta as três abordagens como test-first e alinhadas a teste antecipado e shift left. TDD orienta a codificação por casos de teste; ATDD deriva casos de critérios de aceitação com perspectivas como cliente, desenvolvimento e teste; BDD expressa comportamento desejado em exemplos compreensíveis por stakeholders, frequentemente em Given/When/Then. Podem gerar artefatos que permanecem como regressão automatizada, mas a automação não é condição de todo exemplo colaborativo.

## Exemplo
Para uma tarifa, TDD pode dirigir uma função de cálculo; ATDD pode validar critérios de cobrança combinados pelo time; BDD pode descrever cenários de uso e resultado observável em linguagem partilhada.

## Limites e trade-offs
Testes antecipados não substituem exploração, revisão ou níveis de teste posteriores. Um cenário mal especificado continua sendo uma expectativa ruim, mesmo se automatizado.

## Como verificar
Identifique objetivo, participantes, nível de detalhe e momento de cada exemplo; confirme que orienta implementação sem duplicar requisitos ambíguos.

## Conexões
- [[test-driven-development]] — detalha TDD.
- [[acceptance-test-driven-development]] — conecta ATDD a aceitação.
- [[behavior-driven-development]] — enfatiza exemplos compartilhados de comportamento.

## Fontes
- [ASTQB — CTFL §2.1, Testing as a Driver for Software Development](https://astqb.org/2-1-testing-in-the-context-of-a-software-development-lifecycle-sdlc/) — TDD, ATDD e BDD; acesso em 2026-10-01.
- [ISTQB CTFL Syllabus v4.0.1](https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf) — §2.1.3; acesso em 2026-10-01.
