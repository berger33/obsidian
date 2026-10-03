---
id: software.testes.tranche23.001675
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

# @Test(expected) passa cedo demais — use com cuidado

## Em uma frase
O parâmetro expected da anotação Test aceita subclasses de Throwable, mas a página oficial crava o problema: o teste passa se qualquer código do método lançar aquela exceção, e não dá para verificar a mensagem nem o estado do objeto depois do lançamento — "The expected parameter should be used with care".

## Por que importa
Esse é o falso-positivo clássico de teste de exceção: a asserção pretendida depois da chamada é pulada quando a exceção chega cedo, e o build verde esconde o comportamento não verificado.

## Como funciona
A página recomenda explicitamente as abordagens anteriores (assertThrows ou try/catch) pelos motivos acima, e documenta que a regra ExpectedException foi deprecada no 4.13 — o motivo citado é que, após a chamada que lança, o restante do teste não executa, o que confundia.

## Exemplo
Converta um @Test(expected = IOException.class) para assertThrows e prove que havia código morto depois da chamada: adicione uma asserção que falha se for alcançada e veja o teste mudar de estado.

## Limites e trade-offs
Para o caso simples — só verificar o tipo, sem estado posterior — o expected continua funcional e onipresente em bases legadas; a ressalva da doc é de escopo de verificação, não pedido de erradicação.

## Como verificar
Abra a página Exception testing do wiki do junit4 e confira o parágrafo "should be used with care", as três limitações citadas e a nota de deprecação da ExpectedException.

## Conexões
- [[junit4-assertthrows]] — Veja também: assertThrows chegou no 4.13 e virou o jeito padrão de testar exceções.
- [[junit4-timeout-two-ways]] — Veja também: Timeout por método com fork e timeout por classe com a regra.

## Fontes
- [JUnit 4 — Exception testing (wiki)](https://github.com/junit-team/junit4/wiki/Exception-testing) — assertThrows no 4.13, perigos do expected e ExpectedException deprecada; consultado em 2026-10-03.
- [JUnit 4 — página oficial About](https://junit.org/junit4/) — modo manutenção, exemplo @Test com Hamcrest e índice de referências; consultado em 2026-10-03.
