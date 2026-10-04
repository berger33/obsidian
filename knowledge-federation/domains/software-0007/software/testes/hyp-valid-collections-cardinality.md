---
id: software.testes.tranche12.000564
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

# Hypothesis: gerar coleções válidas sem rejeição excessiva

## Em uma frase
Estratégias de listas, conjuntos e dicionários permitem declarar cardinalidade e tipo dos elementos diretamente no domínio gerado.

## Por que importa
Uma coleção com duplicatas, ordem ou quantidade incorretas pode testar uma condição que o contrato não permite, enquanto filtros amplos escondem custos de geração.

## Como funciona
Defina limites de tamanho na estratégia, escolha conjunto quando unicidade fizer parte do modelo e mantenha lista quando posição ou duplicatas forem observáveis.

## Exemplo
Para uma operação de lote que exige ao menos dois itens, uma estratégia de lista pode impor `min_size=2` e um máximo compatível com o limite do serviço.

## Limites e trade-offs
Conjuntos dependem de valores hashable e não preservam a semântica de ordenação; usar a estrutura errada pode tornar a propriedade válida para um modelo diferente.

## Como verificar
Observe os exemplos gerados no intervalo de cardinalidade, confirme que todas as invariantes de entrada são representadas e evite filtros que descartem a maioria dos sorteios.

## Conexões
- [[hyp-builds-from-type-infer]] — Veja também: Hypothesis: inferir argumentos com `builds()`.
- [[hyp-floats-dominio-na-infinito]] — Veja também: Hypothesis: definir o domínio numérico de floats.

## Fontes
- [Hypothesis — Strategies Reference](https://hypothesis.readthedocs.io/en/latest/reference/strategies.html) — estratégias primitivas, compositores, builds, coleções, exemplos e filtros; consultado em 2026-10-02.
- [Hypothesis — API Reference](https://hypothesis.readthedocs.io/en/latest/reference/api.html) — @given, exemplos, inferência, settings, HealthCheck e configuração pública; consultado em 2026-10-02.
