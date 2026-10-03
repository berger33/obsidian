---
id: software.testes.tranche23.001672
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
fontes: ["https://github.com/junit-team/junit4/wiki/Test-fixtures", "https://junit.org/junit4/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Quatro anotações de fixture e a ordem real de execução

## Em uma frase
O guia oficial de fixtures define o conceito — um estado fixo de objetos como baseline para testes repetíveis — e enumera as quatro anotações: BeforeClass e AfterClass no nível de classe, Before e After no nível de método; as de classe precisam ser métodos estáticos públicos sem argumentos.

## Por que importa
Repetibilidade é o que separa suítes que pegam em CI de suítes que flutuam: fixtures deixam explícito o que é pré-condição de cada teste versus preparação única e cara, como conectar a um banco de teste.

## Como funciona
O exemplo do wiki imprime a ordem completa: BeforeClass uma vez, depois para cada teste um ciclo Before, metodo, After, e por fim AfterClass — inclusive com a ordem de métodos individuais podendo aparecer invertida (test2 antes de test1 no exemplo).

## Exemplo
Adicione as quatro anotações com println à sua classe de teste e confirme no console exatamente o padrão de ciclo descrito na página oficial; use o recurso de comparação para localizar a sequência esperada.

## Limites e trade-offs
A ordem entre métodos de um mesmo classe não é garantida — o exemplo mostra test2 antes de test1 — e a doc encaminha quem precisa de "test execution order" para a página específica do wiki; depender de ordem é o antipadrão que a própria página sinaliza.

## Como verificar
Abra a página Test fixtures do wiki do junit4 e confira a definição, os quatro níveis de anotação e o bloco de saída com BeforeClass/AfterClass emoldurando o loop por método.

## Conexões
- [[junit4-run-without-build]] — Veja também: Rodar um teste JUnit 4 direto com JUnitCore.
- [[junit4-assertthat-hamcrest]] — Veja também: assertThat e Hamcrest: falhas que descrevem a expectativa.

## Fontes
- [JUnit 4 — Test fixtures (wiki)](https://github.com/junit-team/junit4/wiki/Test-fixtures) — BeforeClass/AfterClass e Before/After com ordem de exemplo; consultado em 2026-10-03.
- [JUnit 4 — página oficial About](https://junit.org/junit4/) — modo manutenção, exemplo @Test com Hamcrest e índice de referências; consultado em 2026-10-03.
