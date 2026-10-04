---
id: software.testes.tranche23.001685
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-23.md"
fontes: ["https://github.com/approvals/ApprovalTests.Java/blob/master/approvaltests/docs/tutorials/GettingStarted.md", "https://github.com/approvals/ApprovalTests.Java/blob/master/README.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# verifyAllCombinations: o produto cartesiano aprovado de uma vez

## Em uma frase
Para ampliar cobertura sem escrever loops, o tutorial apresenta CombinationApprovals.verifyAllCombinations(lambda, arraysDeParametros): você declara um array de valores possíveis por parâmetro — até nove parâmetros — e a biblioteca executa a função em todas as combinações, aprovando a tabela inteira como um único artefato.

## Por que importa
O formato inverte a estratégia de caso de teste: em vez de escolher exemplos, você registra a fronteira completa de entrada e revisa as saídas juntas — no exemplo, comprimentos 4, 5, 10 contra palavras geram exatamente as seis linhas [4, Bookkeeper] => Book etc.

## Como funciona
A chamada recebe a função como lambda e os arrays como varargs; o resultado é um arquivo de aprovação com uma linha por combinação, prontamente revisável, e a página calcula ela mesma o total (3 vezes 2, seis combinações) como expectativa.

## Exemplo
Verifique um parser aceitando (string, índice, flag) com três arrays pequenos e aprove a matriz completa; depois mude um comportamento e conte quantas linhas do diff mudaram — é a sua regressão visível.

## Limites e trade-offs
O produto cresce exponencialmente com o número de valores; a própria nota de "potencialmente centenas ou milhares de combinações" implica que a revisão humana da saída inteira precisa continuar factível — senão o mecanismo vira ruído aprovado às pressas.

## Como verificar
Abra a seção Generate Combinations of Parameter Values do tutorial Getting Started e confirme o limite de nove parâmetros, o exemplo substring e a saída de seis linhas.

## Conexões
- [[approvaltests-awt-image]] — Veja também: Testar Swing e AWT por imagem, com namer específico de SO.
- [[approvaltests-reporters]] — Veja também: Reporters: a diferença é apresentada pela ferramenta certa.

## Fontes
- [ApprovalTests — tutorial Getting Started](https://github.com/approvals/ApprovalTests.Java/blob/master/approvaltests/docs/tutorials/GettingStarted.md) — verify, verifyAll, JSON, AWT, combinações, aprovação e reporters; consultado em 2026-10-03.
- [ApprovalTests.Java — README oficial](https://github.com/approvals/ApprovalTests.Java/blob/master/README.md) — proposta, compatibilidades, exemplo verifyAll, artefatos aprovados e licença; consultado em 2026-10-03.
