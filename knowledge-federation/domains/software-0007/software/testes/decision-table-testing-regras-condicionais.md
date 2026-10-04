---
id: software.testes.decision-table.000001
tipo: tecnica
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001.md"
fontes: ["https://astqb.org/4-2-black-box-test-techniques/", "https://www.gasq.org/files/content/gasq/downloads/certification/ISTQB/Glossary/ISTQB_Glossary_v2.2.pdf"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Decision table testing, Teste de tabela de decisão, Teste de regras condicionais]
lote: software-testes-2000-0001
---

# Decision table testing para regras condicionais

## Em uma frase
Teste de tabela de decisão deriva casos de teste das combinações de condições e das ações que a especificação associa a cada combinação viável.

## Por que importa
Regras de negócio frequentemente dependem de várias condições ao mesmo tempo: tipo de cliente, estado da conta e valor da compra, por exemplo. Testar cada condição isoladamente pode não verificar se a combinação aciona a ação correta. Uma tabela torna explícitas regras esquecidas, conflitos e combinações sem resposta definida.

## Como funciona
A tabela registra as condições e ações; cada coluna representa uma regra ou combinação de valores das condições com as ações esperadas. O syllabus ISTQB indica a técnica para requisitos em que combinações diferentes resultam em resultados diferentes. Em tabelas de entrada limitada, condições podem ser booleanas; outras tabelas podem representar valores, intervalos ou partições. Combinações impossíveis ou irrelevantes precisam ser justificadas e tratadas conforme a regra, não removidas silenciosamente.

## Exemplo
Um desconto depende de duas condições: o cliente tem assinatura ativa e o carrinho ultrapassa o mínimo. As quatro combinações booleanas formam quatro regras possíveis. Para cada combinação válida, associe explicitamente a ação esperada — desconto aplicado ou não — e derive um caso de teste que percorra o comportamento e confira o resultado.

## Limites e trade-offs
Com n condições booleanas, a enumeração ingênua pode chegar a 2^n combinações antes de considerar restrições. A tabela pode ficar grande ou difícil de manter quando regras mudam. Reduções como combinar colunas só são seguras se preservarem as condições relevantes e forem justificadas pela especificação; cobertura da tabela não demonstra que os requisitos estejam corretos.

## Como verificar
Conte as condições e regras representadas, confronte cada combinação viável com o requisito e registre combinações impossíveis com a justificativa. Garanta que cada coluna testável tenha pelo menos um caso e que o resultado observado corresponda à ação da regra. Após mudanças, compare a tabela com os casos executados para detectar regras órfãs ou testes duplicados.

## Conexões
- [[particionamento-equivalencia-valores-fronteira]] — ajuda a reduzir domínios de valores para condições da tabela.
- [[combinatorial-testing-pairwise-t-way]] — pode ser considerado para muitas condições, sem confundir cobertura t-way com prova de todas as regras.
- [[testes-stateful-model-based-hypothesis]] — regras podem depender também do estado atual e da sequência de eventos.

## Fontes
- [ASTQB/ISTQB — Black-Box Test Techniques, seção 4.2.3](https://astqb.org/4-2-black-box-test-techniques/) — uso de decision tables para combinar condições e outcomes; acesso em 2026-10-01.
- [ISTQB Glossary v2.2](https://www.gasq.org/files/content/gasq/downloads/certification/ISTQB/Glossary/ISTQB_Glossary_v2.2.pdf) — definição de decision table e decision table testing; acesso em 2026-10-01.
