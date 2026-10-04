---
id: software.testes.tranche22.001617
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
fontes: ["https://kotest.io/docs/proptest/property-test-seeds.html", "https://kotest.io/docs/proptest/property-test-functions.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Kotest: reexecução automática dos seeds que falharam

## Em uma frase
Por padrão, a semente de uma propriedade que falhou é gravada em ~/.kotest/seeds/<spec>/<testname>; na próxima execução esse seed é detectado e usado no lugar do sorteio aleatório, e o arquivo some quando o teste passa.

## Por que importa
É o mecanismo anti-"sumiu na minha máquina": a suíte persegue sozinha o histórico de falhas até elas serem de fato consertadas, sem CI especial nem plugin.

## Como funciona
O guia crava a precedência: um seed manualmente especificado sempre vence o seed persistido de falha — o override explícito continua sendo ferramenta de debug.

## Exemplo
Desative o comportamento global com PropertyTesting.writeFailedSeed = false quando ~/.kotest não puder viver num cache compartilhado entre jobs.

## Limites e trade-offs
Seed persistida em ~/.kotest é estado fora do repositório: builds em container descartam a perseguição de falhas a menos que montem o diretório.

## Como verificar
Falhe uma propriedade num container, monte ~/.kotest num volume e confirme no run seguinte que o seed gravado reaparece em ~/.kotest/seeds.

## Conexões
- [[kotest-seeds]] — Veja também: Kotest: semente da geração e seed fixa.
- [[kotest-proptest-in-specs]] — Veja também: Kotest: propriedade dentro de spec e versão da doc.

## Fontes
- [Kotest — Property Test Seeds](https://kotest.io/docs/proptest/property-test-seeds.html) — sementes, rerun de falhas e ~/.kotest/seeds; consultado em 2026-10-03.
- [Kotest — Property Test Functions](https://kotest.io/docs/proptest/property-test-functions.html) — forAll, checkAll, iterações e generators; consultado em 2026-10-03.
