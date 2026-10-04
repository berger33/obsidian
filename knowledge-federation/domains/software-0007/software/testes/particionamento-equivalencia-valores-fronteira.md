---
id: software.testes.equivalence-boundary.000001
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
fontes: ["https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf", "https://www.gasq.org/files/content/gasq/downloads/certification/ISTQB/Glossary/ISTQB_Glossary_v2.2.pdf"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Equivalence partitioning, Boundary value analysis, Particionamento de equivalência, Análise de valor limite]
lote: software-testes-2000-0001
---

# Particionamento de equivalência e valores de fronteira

## Em uma frase
Particionamento de equivalência agrupa valores que a especificação espera tratar do mesmo modo; análise de valores de fronteira concentra casos nas bordas entre esses grupos ordenados.

## Por que importa
Testar muitos valores comuns pode repetir a mesma verificação e ainda deixar passar erros de limite, como aceitar idade 17 quando a regra começa em 18. As técnicas ajudam a selecionar casos representativos de forma explícita. A qualidade do conjunto depende de interpretar a especificação e de incluir partições inválidas relevantes, não apenas valores considerados “normais”.

## Como funciona
Na técnica ISTQB, uma partição reúne entradas, saídas, estados ou parâmetros que devem receber tratamento equivalente segundo o test object. Seleciona-se ao menos um valor por partição identificada, incluindo partições inválidas quando fazem parte do contrato. A análise de fronteira aplica-se a partições ordenadas: identifica limites mínimo/máximo e testa os valores prescritos pelo critério escolhido. A syllabus descreve BVA de dois valores e de três valores; estes têm conjuntos de cobertura diferentes.

## Exemplo
Para idade inteira aceita de 18 a 65, podem ser identificadas três partições: abaixo do mínimo, válida e acima do máximo. Um teste representativo de cada partição exercita equivalência. Um critério BVA de três valores pode selecionar 17, 18, 19, 64, 65 e 66 para verificar as bordas e vizinhos; o conjunto exato deve corresponder à regra e ao critério adotados.

## Limites e trade-offs
Partições corretas não são sempre óbvias: campos com regras combinadas podem ter várias classes, e entradas que parecem equivalentes podem produzir tratamento diferente por configuração ou estado. BVA requer uma ordem e não substitui teste de combinações entre parâmetros. As técnicas não garantem defeitos encontrados nem cobertura de todas as interações.

## Como verificar
Documente a regra que separa cada partição, se ela é válida ou inválida e qual valor representa a classe. Para BVA, registre o critério de dois ou três valores e confira cada limite e vizinho. Revise se existem lacunas, sobreposições ou partições vazias e mantenha os casos de fronteira como regressão após defeitos encontrados.

## Conexões
- [[decision-table-testing-regras-condicionais]] — útil quando o resultado depende de combinações de condições.
- [[combinatorial-testing-pairwise-t-way]] — aborda interações entre vários parâmetros em vez de cada partição isolada.
- [[property-based-testing-hypothesis]] — estratégias gerativas podem explorar intervalos e propriedades além dos exemplos selecionados.

## Fontes
- [ISTQB/ASTQB — CTFL Syllabus v4.0.1, seção 4.2](https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf) — equivalence partitioning e versões de boundary value analysis; acesso em 2026-10-01.
- [ISTQB Glossary v2.2](https://www.gasq.org/files/content/gasq/downloads/certification/ISTQB/Glossary/ISTQB_Glossary_v2.2.pdf) — definições de equivalence partition, boundary value e coverage items; acesso em 2026-10-01.
