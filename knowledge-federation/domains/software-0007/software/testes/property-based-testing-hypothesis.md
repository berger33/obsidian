---
id: software.testes.property-based.000001
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: aprovada
revisor: usuario-da-sessao
data_revisao_humana: 2026-10-02
fontes: ["https://hypothesis.readthedocs.io/en/latest/tutorial/introduction.html", "https://hypothesis.readthedocs.io/en/latest/reference/strategies.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Property-based testing, Testes baseados em propriedades, Hypothesis]
lote: software-testes-2000-0001
---

# Testes baseados em propriedades com Hypothesis

## Em uma frase
Em vez de enumerar apenas exemplos escolhidos à mão, um teste baseado em propriedades declara uma relação que deve valer para entradas geradas a partir de estratégias.

## Por que importa
Exemplos fixos cobrem casos conhecidos, mas podem deixar passar combinações ou limites que a pessoa que escreveu o teste não antecipou. Estratégias geradoras ajudam a explorar o domínio de entrada e encontrar contraexemplos. O benefício depende de uma propriedade correta e de um gerador que represente entradas válidas para a interface sob teste.

## Como funciona
No Hypothesis, `@given` transforma uma função de teste comum em um teste que recebe valores gerados por estratégias. Estratégias descrevem domínios, como inteiros, listas ou combinações de valores. O teste afirma uma propriedade que deve se manter, por exemplo que serializar e desserializar preserva um valor, ou que o resultado de uma ordenação é equivalente ao `sorted` para a mesma lista. A documentação chama a técnica de complemento poderoso ao teste unitário, não substituto universal.

## Exemplo
Para uma função que ordena listas de números, uma estratégia pode gerar listas de inteiros e o teste comparar a saída com uma implementação de referência. Para uma API de serialização, uma propriedade de round-trip pode exigir que decodificar o resultado de uma codificação recupere valor equivalente, restringindo os geradores ao domínio que o contrato suporta.

## Limites e trade-offs
Uma propriedade mal especificada pode validar o comportamento errado em muitas entradas. Geradores amplos podem produzir casos inválidos para a API, enquanto filtros excessivos podem tornar a geração ineficiente. Execuções amostram entradas, não provam matematicamente que a propriedade vale para todo o domínio. Mantenha exemplos de regressão importantes junto dos testes gerativos.

## Como verificar
Revise se cada estratégia respeita os pré-requisitos reais e se a propriedade expressa o contrato, incluindo limites e erros esperados. Rode com configurações padrão e aumente exemplos para caminhos críticos após medir o custo. Quando surgir contraexemplo, conserve a falha e transforme a lição em uma propriedade mais clara ou em um exemplo explícito complementar.

## Conexões
- [[shrinking-contraexemplos-hypothesis]] — reduz falhas geradas a exemplos mais fáceis de entender.
- [[testes-stateful-model-based-hypothesis]] — amplia a geração para sequências de operações.
- [[fuzzing-coverage-guided-libfuzzer]] — fuzzing também explora entradas, mas é guiado por cobertura e instrumentação.

## Fontes
- [Hypothesis — Introduction to Hypothesis](https://hypothesis.readthedocs.io/en/latest/tutorial/introduction.html) — `@given`, estratégias e exemplos de propriedades; acesso em 2026-10-01.
- [Hypothesis — Strategies Reference](https://hypothesis.readthedocs.io/en/latest/reference/strategies.html) — composição, domínios e comportamento das estratégias; acesso em 2026-10-01.
