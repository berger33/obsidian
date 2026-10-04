---
id: software.testes.tranche21.001552
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-21.md"
fontes: ["https://github.com/CodeIntelligenceTesting/jazzer", "https://llvm.org/docs/LibFuzzer.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Jazzer: chamar a classe main diretamente

## Em uma frase
Também é possível invocar com o seu próprio java o classpath do projeto mais jazzer.jar e jazzer-junit.jar e a classe com.code_intelligence.jazzer.Jazzer, passando --target_class com a classe do fuzz test.

## Por que importa
Executar dentro da JVM e do launcher da sua build system preserva módulos, argumentos e variáveis que a suíte do projeto já usa.

## Como funciona
Monte java -cp <classpath>;<jazzer.jar>;<jazzer-junit.jar> com.code_intelligence.jazzer.Jazzer --target_class=<classe> e anote flags do Jazzer com duas barras.

## Exemplo
Um build Maven já configurado pode disparar o mesmo alvo sem depender do plugin, só adicionando os dois jars ao classpath.

## Limites e trade-offs
Flags com barra simples pertencem ao libFuzzer, não ao Jazzer: trocá-las de lugar produz argumento desconhecido em vez de comportamento errado.

## Como verificar
Adicione um único flag da documentação libFuzzer e confirme que a corrida o aceita e altera o parâmetro prometido.

## Conexões
- [[jazzer-standalone-binary]] — Veja também: Jazzer: binário standalone da página de releases.
- [[jazzer-fuzzertestoneinput]] — Veja também: Jazzer: o método fuzzerTestOneInput.

## Fontes
- [Jazzer — repositório oficial](https://github.com/CodeIntelligenceTesting/jazzer) — modos standalone e JUnit, corpus, inputs e sanitizers; consultado em 2026-10-03.
- [LLVM — documentação do libFuzzer](https://llvm.org/docs/LibFuzzer.html) — flags de um traço aceitos pelo Jazzer; consultado em 2026-10-03.
