---
id: software.testes.black-box.000001
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
fontes: ["https://astqb.org/2-2-test-levels-and-test-types/", "https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Black-box specification-based testing", "Teste black-box deriva casos do comportamento especificado"]
lote: software-testes-2000-0001
---

# Teste black-box deriva casos do comportamento especificado

## Em uma frase
Testes black-box derivam casos da especificação observável do objeto, sem usar sua estrutura interna como base principal.

## Por que importa
Uma verificação pode explorar valores e comportamentos importantes para o usuário sem depender de como o código foi organizado. Isso também ajuda a detectar discrepâncias entre requisito e comportamento implementado.

## Como funciona
O CTFL descreve a técnica como specification-based: casos partem de documentação ou comportamento especificado, não da estrutura interna. Particionamento de equivalência, análise de valores de fronteira, tabelas de decisão e transição de estados são técnicas cobertas no syllabus. Elas podem ser usadas em diferentes níveis, com base de teste e foco adequados.

## Exemplo
Uma API documenta que um campo aceita valores de 1 a 30 dias. Casos black-box exercitam limites, classes válidas/inválidas e combinações de regras sem inspecionar o algoritmo interno.

## Limites e trade-offs
Especificação incompleta ou incorreta restringe os casos derivados. Black-box não garante cobertura de caminhos internos; técnicas white-box e experiência podem complementar a análise.

## Como verificar
Associe cada caso à regra ou condição da base de teste, incluindo limites e resultados esperados. Registre lacunas quando o contrato não define um comportamento observável.

## Conexões
- [[particionamento-equivalencia-valores-fronteira]] — agrupa entradas conforme tratamento esperado.
- [[decision-table-testing-regras-condicionais]] — organiza regras combinatórias.

## Fontes
- [ASTQB — CTFL §2.2.2, Test Types](https://astqb.org/2-2-test-levels-and-test-types/) — definição de black-box testing.
- [ASTQB — CTFL §4.2, Black-Box Test Techniques](https://astqb.org/4-2-black-box-test-techniques/) — técnicas specification-based; acesso em 2026-10-01.
