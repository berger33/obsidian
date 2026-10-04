---
id: software.testes.tranche12.000560
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-12.md"
fontes: ["https://hypothesis.readthedocs.io/en/latest/reference/strategies.html", "https://hypothesis.readthedocs.io/en/latest/reference/api.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Hypothesis: map, flatmap e filter em estratégias

## Em uma frase
Combinadores transformam ou encadeiam estratégias sem precisar reescrever o gerador e sua lógica de redução.

## Por que importa
Escolher o combinador que representa a relação entre valores deixa claro quais entradas são possíveis e quais transformações preservam o domínio do teste.

## Como funciona
Use `map` para converter cada valor gerado, `flatmap` quando a segunda estratégia depender do primeiro resultado e `filter` apenas para predicados que rejeitam poucos exemplos.

## Exemplo
Uma estratégia de texto pode ser mapeada para um objeto de domínio; outra pode escolher um limite e então gerar números válidos em função desse limite.

## Limites e trade-offs
Filtros que rejeitam quase todos os valores desperdiçam tentativas e podem disparar um health check. Prefira construir diretamente uma estratégia que represente os dados válidos.

## Como verificar
Leia a estratégia resultante como uma descrição do domínio, rode o teste com exemplos pequenos e observe se a rejeição excessiva indica um filtro que deveria ser removido.

## Conexões
- [[hyp-composite-dependent-strategies]] — Veja também: Hypothesis: estratégias próprias com `@composite`.

## Fontes
- [Hypothesis — Strategies Reference](https://hypothesis.readthedocs.io/en/latest/reference/strategies.html) — estratégias primitivas, compositores, builds, coleções, exemplos e filtros; consultado em 2026-10-02.
- [Hypothesis — API Reference](https://hypothesis.readthedocs.io/en/latest/reference/api.html) — @given, exemplos, inferência, settings, HealthCheck e configuração pública; consultado em 2026-10-02.
