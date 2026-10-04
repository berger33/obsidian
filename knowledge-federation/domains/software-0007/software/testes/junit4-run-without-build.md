---
id: software.testes.tranche23.001671
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
fontes: ["https://github.com/junit-team/junit4/wiki/Getting-started", "https://junit.org/junit4/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Rodar um teste JUnit 4 direto com JUnitCore

## Em uma frase
O guia oficial de primeiros passos faz o exercício sem build tool: baixe o junit-4.XX.jar da página de releases mais o hamcrest-core-1.3.jar, compile Calculator.java e CalculatorTest.java com javac apontando o classpath para os dois jars e rode java com a classe main org.junit.runner.JUnitCore passando a classe de teste.

## Por que importa
Saber que o JUnit 4 é só biblioteca + runner de linha de comando desmonta a ideia de que testes exigem Maven/Gradle; é também o caminho mínimo para reproduzir um bug isolado em versão específica.

## Como funciona
O exemplo mostra o contrato da saída: um ponto por teste executado, "OK (1 test)" no sucesso e, no fracasso, a numeração "1) metodo(Classe)", a linha java.lang.AssertionError: expected:<6> but was:<-6> e o resumo "Tests run: 1, Failures: 1".

## Exemplo
Repita o ciclo javac/java do wiki com sua própria classe e inverta um operador para ver a saída de falha exatamente no formato descrito acima — o formato esperado/obtido é o que muitos parsers de CI consomem.

## Limites e trade-offs
Os comandos do exemplo usam separador de classpath específico de SO (dois-pontos no Linux/macOS, ponto-e-vírgula no Windows); fora do exemplo controlado, uma build tool continua sendo o caminho recomendado pelo próprio guia.

## Como verificar
Abra a página Getting started do wiki do junit4 e confira os comandos javac/java completos, a dependência do hamcrest-core e o formato da saída de falha.

## Conexões
- [[junit4-maintenance-mode]] — Veja também: JUnit 4 é um xUnit clássico em modo manutenção.
- [[junit4-fixtures]] — Veja também: Quatro anotações de fixture e a ordem real de execução.

## Fontes
- [JUnit 4 — Getting started (wiki)](https://github.com/junit-team/junit4/wiki/Getting-started) — jars, javac/java, JUnitCore e formatos de saída; consultado em 2026-10-03.
- [JUnit 4 — página oficial About](https://junit.org/junit4/) — modo manutenção, exemplo @Test com Hamcrest e índice de referências; consultado em 2026-10-03.
