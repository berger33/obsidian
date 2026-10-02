---
id: software.testes.metamorphic.000001
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-01
validade: estavel
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001.md"
fontes: ["https://www.cs.hku.hk/data/techreps/document/TR-2017-04.pdf", "https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=920197"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Metamorphic testing, Metamorphic relation, Teste metamórfico]
lote: software-testes-2000-0001
---

# Metamorphic testing e relações entre execuções

## Em uma frase
Metamorphic testing verifica relações necessárias entre entradas e saídas de várias execuções quando o resultado correto de cada entrada isolada é difícil ou caro de determinar.

## Por que importa
Em alguns programas, não há oracle prático para calcular a saída correta de cada caso — por exemplo, um cálculo complexo ou uma busca com resultados extensos. Ainda podem existir propriedades que relacionam uma execução original a uma execução derivada. Verificar essas relações cria um mecanismo de detecção complementar, sem precisar fornecer a resposta exata de cada execução.

## Como funciona
Define-se uma relação metamórfica a partir da especificação ou de uma propriedade necessária do domínio. Uma entrada de origem gera uma ou mais entradas de acompanhamento; o teste executa o sistema em todas e compara as saídas segundo a relação. A relação precisa ser válida para o escopo e as condições escolhidas. A revisão de Chen et al. descreve esse mecanismo e sintetiza desafios da técnica; o artigo do NIST apresenta seu uso, inclusive em software de segurança.

## Exemplo
Para uma implementação de menor caminho em grafo não direcionado, trocar nó inicial e final não deve alterar o comprimento do caminho mínimo, quando ambos são alcançáveis. O teste executa o algoritmo com `(G, a, b)` e `(G, b, a)` e compara os comprimentos. Essa propriedade não determina que cada caminho retornado seja correto em todos os aspectos; outras verificações ainda podem ser necessárias.

## Limites e trade-offs
Uma relação inadequada pode gerar falsos alarmes ou deixar defeitos passar; ela própria precisa ser validada contra requisitos e condições, como arredondamento numérico, estados ou dados externos. A técnica reduz o problema do oracle, não o elimina universalmente. Uma relação que apenas compara saídas pode permitir que duas execuções compartilhem o mesmo erro.

## Como verificar
Documente a propriedade, as pré-condições e como construir casos de acompanhamento. Teste a relação em exemplos cuja resposta se conhece e procure casos em que ela não se aplica. Quando uma violação surgir, preserve ambas as entradas e saídas, investigue a causa e acrescente um teste regressivo claro.

## Conexões
- [[differential-testing-comparacao-implementacoes]] — compara implementações diferentes para o mesmo dado; metamorphic testing compara execuções relacionadas.
- [[property-based-testing-hypothesis]] — propriedades gerativas podem produzir casos de origem para relações metamórficas.
- [[fuzzing-coverage-guided-libfuzzer]] — fuzzing explora entradas, enquanto relações metamórficas verificam consistência entre resultados.

## Fontes
- [Chen et al. — Metamorphic Testing: A Review of Challenges and Opportunities](https://www.cs.hku.hk/data/techreps/document/TR-2017-04.pdf) — relações metamórficas, geração/verificação de casos e desafios; acesso em 2026-10-01.
- [NIST — Metamorphic Testing for Cybersecurity](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=920197) — relações entre execuções, oracle problem e exemplos de segurança; acesso em 2026-10-01.
