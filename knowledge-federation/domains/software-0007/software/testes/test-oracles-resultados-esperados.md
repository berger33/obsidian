---
id: software.testes.test-oracle.000001
tipo: conceito
dominio: software
subdominio: testes
nivel: avancado
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
fontes: ["https://www.gasq.org/files/content/ISTQB2/ISTQB-CTAL-TA-Syllabus-v4.0-EN.pdf", "https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=920197"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Test oracle, Test oracle problem, Oráculo de teste, Problema do oráculo]
lote: software-testes-2000-0001
---

# Test oracle e problema do resultado esperado

## Em uma frase
Um test oracle é um mecanismo ou fonte de conhecimento usado para decidir se o resultado observado de uma execução é correto para o caso avaliado.

## Por que importa
Executar uma função e observar uma resposta não basta para testar: é preciso algum critério para julgar o resultado. Esse critério pode vir de uma especificação, cálculo independente, asserção, sistema de referência ou conhecimento humano. Em certos domínios, calcular a saída correta é caro, incerto ou impraticável; essa dificuldade é conhecida como problema do oráculo.

## Como funciona
O syllabus ISTQB CTAL-TA trata a determinação de test oracles como atividade de análise e distingue fontes possíveis de resultado esperado, incluindo pessoas, documentação e verificações implementadas. O artigo do NIST define oracle como mecanismo para decidir a correção do outcome e discute como relações metamórficas aliviam casos sem oracle convencional. Um oracle precisa ser coerente com a regra do produto e com as pré-condições do teste; comparação simples com uma saída anterior não torna essa saída correta.

## Exemplo
Num parser de certificado, especificações podem determinar validade para casos simples, mas revisar manualmente muitos certificados complexos é custoso. Comparar implementações independentes pode revelar divergências, embora a divergência não aponte por si só qual está correta. Uma relação metamórfica também pode conectar duas execuções, desde que a propriedade usada seja justificada para aquele escopo.

## Limites e trade-offs
Oracles incompletos ou incorretos geram falsos positivos e falsos negativos. Uma maioria de implementações pode compartilhar o mesmo defeito; outputs de referência podem ficar obsoletos; julgamento humano pode ser caro e variar. Técnicas metamórficas ajudam a verificar relações, mas não fornecem necessariamente a resposta completa para cada entrada.

## Como verificar
Para cada assert, documente a regra ou fonte que sustenta o esperado. Separe comportamento definido, tolerâncias numéricas e casos não especificados. Quando não houver oracle total, declare que evidência parcial será usada, valide as relações escolhidas e preserve entradas e resultados para investigação reprodutível.

## Conexões
- [[metamorphic-testing-oracle-relations]] — usa relações entre execuções quando falta um resultado exato.
- [[differential-testing-comparacao-implementacoes]] — encontra discrepâncias, mas precisa de adjudicação independente.
- [[exploratory-testing-aprendizado-design-execucao]] — testers podem usar conhecimento de domínio e observação como oracle humano.

## Fontes
- [ISTQB CTAL-TA Syllabus v4.0, seção 1.3.4](https://www.gasq.org/files/content/ISTQB2/ISTQB-CTAL-TA-Syllabus-v4.0-EN.pdf) — determinação de test oracles e fontes de resultados esperados; acesso em 2026-10-01.
- [NIST — Metamorphic Testing for Cybersecurity](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=920197) — definição de oracle, oracle problem e relações entre execuções; acesso em 2026-10-01.
