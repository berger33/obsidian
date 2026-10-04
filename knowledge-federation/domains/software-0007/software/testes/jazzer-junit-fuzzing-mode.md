---
id: software.testes.tranche21.001554
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
fontes: ["https://github.com/CodeIntelligenceTesting/jazzer", "https://github.com/CodeIntelligenceTesting/jazzer/blob/main/docs/arguments-and-configuration-options.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Jazzer: fuzzing a partir de testes normais

## Em uma frase
Sob JUnit com @FuzzTest, habilita-se o modo de fuzzing com a variável JAZZER_FUZZ=1 antes de rodar os testes, fazendo o Jazzer executar um fuzz test por vez e gerar entradas livremente.

## Por que importa
O mesmo teste funciona como unitário no build comum e como alvo do fuzzer quando você liga a variável — sem projeto paralelo nem fonte duplicada.

## Como funciona
Anote os métodos com @FuzzTest, rode a suíte normal para o modo regressão e exporte JAZZER_FUZZ=1 para o modo fuzzing na sessão dedicada.

## Exemplo
A mesma classe que valida entradas fixas no CI vira caçadora de crashes numa janela de night fuzzing com uma variável de ambiente.

## Limites e trade-offs
O modo fuzzing roda um alvo por execução; esperar que a suíte inteira fuzzar de uma vez gera horas ociosas comparando alvos independentes.

## Como verificar
Rode com a variável desligada e ligada e confirme a diferença entre o resumo JUnit e o log do libFuzzer.

## Conexões
- [[jazzer-fuzzertestoneinput]] — Veja também: Jazzer: o método fuzzerTestOneInput.
- [[jazzer-generated-corpus]] — Veja também: Jazzer: o corpus gerado pelo fuzzer.

## Fontes
- [Jazzer — repositório oficial](https://github.com/CodeIntelligenceTesting/jazzer) — modos standalone e JUnit, corpus, inputs e sanitizers; consultado em 2026-10-03.
- [Jazzer — Arguments and configuration options](https://github.com/CodeIntelligenceTesting/jazzer/blob/main/docs/arguments-and-configuration-options.md) — argumentos do agente e hooks desativáveis; consultado em 2026-10-03.
