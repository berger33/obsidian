---
id: software.testes.tranche23.001676
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
fontes: ["https://github.com/junit-team/junit4/wiki/Timeout-for-tests", "https://junit.org/junit4/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Timeout por método com fork e timeout por classe com a regra

## Em uma frase
Há duas formas documentadas: o parâmetro timeout no @Test, que roda o método em uma thread separada e, ao estourar o limite em milissegundos, falha o teste e interrompe a thread; e a regra Timeout, aplicada a todos os métodos da classe, hoje executada adicionalmente ao parâmetro individual.

## Por que importa
Testes que travam (deadlock, await sem fim) transformam o build do CI em espera infinita; o timeout transforma travamento em falha localizável com tempo delimitado.

## Como funciona
A página detalha as arestas: se o método está em loop infinito não responsivo a interrupt, a thread continua rodando enquanto os outros testes seguem; e o timeout da regra cobre o fixture inteiro — Before e After inclusos — com a ressalva de que After pode não ser chamado quando o método não responde ao interrupt.

## Exemplo
Marque um teste com timeout = 1000 que dorme 2000 e confirme a falha por timeout; depois adicione a regra Timeout.seconds(10) como campo @Rule da classe e veja todos os testes dela passarem a ter o mesmo limite por método.

## Limites e trade-offs
Os detalhes de semântica (interrupção, Before/After cobertos) são exatamente o que a página alerta que surpreende; além disso, a página chama o comportamento de "currently" somar regra e parâmetro, linkando issue — sinal de área ainda ajustada.

## Como verificar
Abra a página Timeout for tests do wiki do junit4 e confira o exemplo com thread separada, a regra Timeout.seconds(10) e os dois parágrafos de consequência.

## Conexões
- [[junit4-expected-peril]] — Veja também: @Test(expected) passa cedo demais — use com cuidado.
- [[junit4-temporaryfolder]] — Veja também: TemporaryFolder apaga sozinha — e pode cobrar prova disso.

## Fontes
- [JUnit 4 — Timeout for tests (wiki)](https://github.com/junit-team/junit4/wiki/Timeout-for-tests) — parâmetro timeout, regra Timeout e semântica de interrupt; consultado em 2026-10-03.
- [JUnit 4 — página oficial About](https://junit.org/junit4/) — modo manutenção, exemplo @Test com Hamcrest e índice de referências; consultado em 2026-10-03.
