---
id: software.testes.tranche22.001614
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-22.md"
fontes: ["https://kotest.io/docs/proptest/property-test-config.html", "https://kotest.io/docs/proptest/property-test-functions.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Kotest: PropTestConfig e a tolerância a falhas

## Em uma frase
Toda a afinação do property test passa por PropTestConfig, o objeto de configuração aceito por ambas as funções; maxFailure = 3, por exemplo, tolera até três amostras reprovadas antes de considerar o teste fracassado.

## Por que importa
Testes sobre código não determinístico (threads, aleatoriedade interna) são falsos alarmes em massa; a cota de falhas dá folga sem desligar a propriedade.

## Como funciona
Passa-se o config junto da chamada: forAll<String, String>(PropTestConfig(maxFailure = 3)) { a, b -> ... }, com default documentado de tolerância zero.

## Exemplo
"Talvez você queira rodar um teste não determinístico várias vezes e aceitar um pequeno número de falhas" — a página descreve exatamente esse caso de uso para maxFailure.

## Limites e trade-offs
Tolerar falha esconde regressões reais atrás de instabilidade; combine com seed fixa (nota própria) antes de aceitar flake como normal.

## Como verificar
Suba maxFailure para 1 e introduza um bug com taxa de disparo baixa para ver a propriedade deixar de pegar o erro imediatamente.

## Conexões
- [[kotest-generators]] — Veja também: Kotest: generators automáticos e Arb explícitos.
- [[kotest-config-listeners-hex]] — Veja também: Kotest: listeners por iteração e hex para não imprimíveis.

## Fontes
- [Kotest — Property Test Configuration](https://kotest.io/docs/proptest/property-test-config.html) — PropTestConfig: maxFailure, listeners e saída hex; consultado em 2026-10-03.
- [Kotest — Property Test Functions](https://kotest.io/docs/proptest/property-test-functions.html) — forAll, checkAll, iterações e generators; consultado em 2026-10-03.
