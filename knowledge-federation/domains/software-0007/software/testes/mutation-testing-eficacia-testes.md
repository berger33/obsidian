---
id: software.testes.mutation-testing.000001
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: aprovada
revisor: usuario-da-sessao
data_revisao_humana: 2026-10-02
fontes: ["https://stryker-mutator.io/docs/mutation-testing-elements/mutant-states-and-metrics/", "https://stryker-mutator.io/docs/General/faq/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Mutation testing, Teste de mutação, Mutation score]
lote: software-testes-2000-0001
---

# Mutation testing para avaliar a eficácia dos testes

## Em uma frase
Mutation testing altera deliberadamente o código em pequenas variações e verifica se a suíte existente detecta essas mudanças.

## Por que importa
Cobertura de linhas mostra que uma execução passou por código, mas não demonstra que as asserções detectam uma saída incorreta. Um mutante sobrevivente indica que o conjunto de testes executado não distinguiu aquela alteração do comportamento original, sinalizando uma possível lacuna. O método avalia força de detecção, não correção do requisito nem qualidade total do sistema.

## Como funciona
Ferramentas como Stryker geram mutantes, executam os testes e classificam resultados. Um mutante `killed` fez pelo menos um teste falhar; `survived` passou; `no coverage` não foi alcançado pelos testes; `timeout` pode indicar que a alteração causou execução excessiva; erros de compilação ou runtime não entram como mutantes válidos no cálculo descrito pela ferramenta. A documentação define mutation score a partir dos mutantes detectados em relação aos mutantes válidos, e também distingue a pontuação sobre código coberto.

## Exemplo
Se um código verifica `idade >= limite` e o mutante troca para `idade > limite`, o teste de fronteira precisa falhar para matar esse mutante. Se todos os testes usam valores bem acima do limite, o mutante pode sobreviver, indicando que o caso de igualdade não foi verificado pela suíte.

## Limites e trade-offs
Mutação pode ser custosa porque executa testes repetidamente e alguns mutantes são equivalentes — alteram o texto do código sem alterar o comportamento observável. Score não é percentual universal de qualidade nem deve virar meta cega; reporte cobertura, mutantes válidos, sobreviventes e erros de execução separadamente. Um timeout não significa necessariamente a mesma coisa para toda ferramenta, então use a semântica da versão adotada.

## Como verificar
Escolha módulos críticos, exclua código gerado e teste uma amostra de mutações representativas. Inspecione cada mutante sobrevivente e pergunte qual comportamento deveria ser afirmado, em vez de adicionar asserts apenas para elevar score. Reexecute a ferramenta depois das melhorias e compare categorias e custo de execução, não apenas o número agregado.

## Conexões
- [[test-doubles-fakes-stubs-spies-mocks]] — interações verificadas por mocks devem corresponder ao contrato, não apenas a detalhes internos.
- [[testes-flaky-determinismo]] — execução instável torna resultados de mutação difíceis de interpretar.
- [[property-based-testing-hypothesis]] — geração de entradas e mutação de código investigam lacunas por métodos diferentes.

## Fontes
- [Stryker — Mutant states and metrics](https://stryker-mutator.io/docs/mutation-testing-elements/mutant-states-and-metrics/) — estados e fórmulas das métricas de mutação; acesso em 2026-10-01.
- [Stryker — FAQ](https://stryker-mutator.io/docs/General/faq/) — cálculo e interpretação do mutation score; acesso em 2026-10-01.
