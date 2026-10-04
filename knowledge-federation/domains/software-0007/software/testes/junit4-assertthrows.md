---
id: software.testes.tranche23.001674
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
fontes: ["https://github.com/junit-team/junit4/wiki/Exception-testing", "https://junit.org/junit4/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# assertThrows chegou no 4.13 e virou o jeito padrão de testar exceções

## Em uma frase
A página oficial de exception testing documenta que o método assertThrows foi adicionado à classe Assert na versão 4.13 e permite afirmar que uma lambda ou referência de método lança um tipo específico de exceção, retornando a exceção para asserts adicionais sobre mensagem e causa.

## Por que importa
Testar exceção é onde o estilo try/catch clássico mais vaza estado: com assertThrows, dá para afirmar a mensagem e o estado do domínio depois do lançamento, no mesmo teste — o exemplo oficial confere thrown.getMessage e assertTrue(list.isEmpty) lado a lado.

## Como funciona
O idiom oficial: capturar o retorno de assertThrows(Tipo.class, () -> lista.add(1, new Object())) e continuar asserções sobre o objeto lançado; para códigos sem lambda ou JUnit antigo, a página mantém o try/catch com fail() como alternativa explícita.

## Exemplo
Pegue um try/catch com fail no seu código e converta para assertThrows, acrescentando uma asserção na mensagem; rode e confirme a falha formatada esperando o tipo da exceção.

## Limites e trade-offs
A página adverte que fail() lança AssertionError, então o idiom try/catch não serve para verificar métodos que deveriam lançar AssertionError — detalhe que easy esquecer ao migrar casos específicos.

## Como verificar
Abra a página Exception testing do wiki do junit4 e confira a frase "added to the Assert class in version 4.13", o exemplo com estado do domínio e o aviso sobre fail.

## Conexões
- [[junit4-assertthat-hamcrest]] — Veja também: assertThat e Hamcrest: falhas que descrevem a expectativa.
- [[junit4-expected-peril]] — Veja também: @Test(expected) passa cedo demais — use com cuidado.

## Fontes
- [JUnit 4 — Exception testing (wiki)](https://github.com/junit-team/junit4/wiki/Exception-testing) — assertThrows no 4.13, perigos do expected e ExpectedException deprecada; consultado em 2026-10-03.
- [JUnit 4 — página oficial About](https://junit.org/junit4/) — modo manutenção, exemplo @Test com Hamcrest e índice de referências; consultado em 2026-10-03.
