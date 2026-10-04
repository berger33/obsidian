---
id: software.testes.tranche22.001613
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
fontes: ["https://kotest.io/docs/proptest/property-test-functions.html", "https://kotest.io/docs/proptest/property-test-generators.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Kotest: generators automáticos e Arb explícitos

## Em uma frase
Sem especificação, o Kotest resolve um generator por tipo de parâmetro — o de Int cobre negativos, positivos, zeros e infinitos; quando o espaço precisa de recorte, passa-se o gerador explicitamente no lugar dos tipos.

## Por que importa
A sorte de um property test está na amostragem: generators automáticos encontram bugs de fronteira, mas só o recorte explícito concentra a força bruta no domínio real da função.

## Como funciona
forAll(Arb.int(21..150)) e forAll(Arb.int(18..150)) demonstram o padrão na própria página, com o argumento idiomático de idade mínima para beber em Chicago e Londres.

## Exemplo
A página encaminha para o catálogo de generators embutidos (property-test-generators) quando o tipo precisa de um Arb dedicado, por exemplo listas de estruturas próprias.

## Limites e trade-offs
Recortar o espaço também esconde bugs fora dele: a suíte verde com Arb.int(21..150) não diz nada sobre o que acontece em 20.

## Como verificar
Injete um valor de borda fora do range escolhido via generator customizado e veja a propriedade pegar o que o recorte automático não cobre.

## Conexões
- [[kotest-iterations]] — Veja também: Kotest: mil iterações por padrão, ajustáveis por argumento.
- [[kotest-config-maxfailure]] — Veja também: Kotest: PropTestConfig e a tolerância a falhas.

## Fontes
- [Kotest — Property Test Functions](https://kotest.io/docs/proptest/property-test-functions.html) — forAll, checkAll, iterações e generators; consultado em 2026-10-03.
- [Kotest — Property Test Generators](https://kotest.io/docs/proptest/property-test-generators.html) — catálogo de generators embutidos citado pela página de funções; consultado em 2026-10-03.
