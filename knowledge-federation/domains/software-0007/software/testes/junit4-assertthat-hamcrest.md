---
id: software.testes.tranche23.001673
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
fontes: ["https://github.com/junit-team/junit4/wiki/Matchers-and-assertthat", "https://junit.org/junit4/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# assertThat e Hamcrest: falhas que descrevem a expectativa

## Em uma frase
A página Matcher and assertThat conta a origem: Joe Walnes construiu assertThat sobre o JMock 1, e o time decidiu embuti-lo no JUnit ("We have decided to include this API directly in JUnit"), trazendo pela primeira vez classes de terceiros — as hamcrest-core — para a distribuição.

## Por que importa
O benefício prático demonstrado na página é a mensagem de falha: assertTrue com ou lógico não imprime nada útil, enquanto assertThat com anyOf imprime Expected: (a string containing "color" or a string containing "colour") got: "Please choose a font" — diagnóstico sem depurador.

## Como funciona
A forma geral é assertThat(valor, matcher); os matchers entram por import estático de org.hamcrest.CoreMatchers (is, not, either().or(), hasItem, each), combináveis, e o JUnit também expõe matchers próprios na classe org.junit.matchers.JUnitMatchers.

## Exemplo
Reescreva um assertTrue composto como assertThat com anyOf e provoque a falha: compare as duas mensagens lado a lado e confirme que a versão Hamcrest contém expectativa e valor atual.

## Limites e trade-offs
A página anota limitações históricas: a comparação especial de strings e arrays com diff detalhado existia nos métodos assert clássicos e "not yet available" para assertThat na época da escrita; além disso, a página lista JUnitMatchers sem dizer que hoje é caminho legado.

## Como verificar
Abra a página Matchers and assertThat do wiki do junit4 e confira a origem JMock, a citação da decisão de inclusão, o exemplo de mensagem e as duas classes de matchers citadas.

## Conexões
- [[junit4-fixtures]] — Veja também: Quatro anotações de fixture e a ordem real de execução.
- [[junit4-assertthrows]] — Veja também: assertThrows chegou no 4.13 e virou o jeito padrão de testar exceções.

## Fontes
- [JUnit 4 — Matchers and assertThat (wiki)](https://github.com/junit-team/junit4/wiki/Matchers-and-assertthat) — origem JMock, importações estáticas de Hamcrest e mensagens de falha; consultado em 2026-10-03.
- [JUnit 4 — página oficial About](https://junit.org/junit4/) — modo manutenção, exemplo @Test com Hamcrest e índice de referências; consultado em 2026-10-03.
