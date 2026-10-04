---
id: software.testes.tranche13.000720
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-13.md"
fontes: ["https://spockframework.org/spock/docs/2.4/all_in_one.html", "https://spockframework.org/spock/docs/2.4/all_in_one.html#_conditions"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Spock: estruturar feature com given when then

## Em uma frase
Uma feature Spock pode separar preparação, estímulo e resultado nos blocos `given:`, `when:` e `then:`.

## Por que importa
A ordem visual torna explícito o cenário e ajuda diferenciar preparação da ação que dispara o comportamento verificado.

## Como funciona
Prepare apenas o estado necessário em `given`, faça uma ação principal em `when` e concentre expectativas que descrevem consequência em `then`.

## Exemplo
Um pagamento em atraso pode preparar uma fatura, solicitar cobrança e verificar que o saldo passa ao estado pendente.

## Limites e trade-offs
Blocos são guias de leitura, não uma barreira contra helper opaco; lógica complexa colocada na preparação ainda pode esconder a razão da assertion.

## Como verificar
Comente temporariamente o estímulo e confira que a falha identifica exatamente a condição de resultado que deixa de ocorrer.

## Conexões
- [[spock-fixture-lifecycle-order]] — Veja também: Spock: dimensionar métodos de fixture por feature.

## Fontes
- [Spock 2.4 — Reference Documentation](https://spockframework.org/spock/docs/2.4/all_in_one.html) — specifications, feature blocks, fixtures and runner; consultado em 2026-10-02.
- [Spock 2.4 — Conditions](https://spockframework.org/spock/docs/2.4/all_in_one.html#_conditions) — implicit conditions and diagnostic rendering; consultado em 2026-10-02.
