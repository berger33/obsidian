---
id: software.testes.tranche21.001553
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

# Jazzer: o método fuzzerTestOneInput

## Em uma frase
No modo sem JUnit, o fuzz test é uma classe pública com um método estático fuzzerTestOneInput que declara os parâmetros que o fuzzer vai gerar e variar.

## Por que importa
Deixar a assinatura do método como contrato de entrada permite usar tipos ricos em vez de ler um byte[] bruto e parsear na mão.

## Como funciona
Defina public static void fuzzerTestOneInput(String par1, int par2, int[] par3, ...) com exatamente os tipos que o analisador aceita e chame o código real ali dentro.

## Exemplo
Um parser de datas recebe a String crua e o ano de referência, e lança em qualquer resultado inconsistente.

## Limites e trade-offs
Cada tipo de parâmetro precisa de suporte de mutação do Jazzer; tipos de domínio complexos viram melhor um parser próprio dentro do teste a partir de primitivas.

## Como verificar
Rode contra uma implementação com exceção explícita em argumento inválido e confirme o registro do input reprodutor.

## Conexões
- [[jazzer-main-class-invocation]] — Veja também: Jazzer: chamar a classe main diretamente.
- [[jazzer-junit-fuzzing-mode]] — Veja também: Jazzer: fuzzing a partir de testes normais.

## Fontes
- [Jazzer — repositório oficial](https://github.com/CodeIntelligenceTesting/jazzer) — modos standalone e JUnit, corpus, inputs e sanitizers; consultado em 2026-10-03.
- [Jazzer — Arguments and configuration options](https://github.com/CodeIntelligenceTesting/jazzer/blob/main/docs/arguments-and-configuration-options.md) — argumentos do agente e hooks desativáveis; consultado em 2026-10-03.
