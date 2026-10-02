---
id: software.testes.tranche12.000566
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
fontes: ["https://hypothesis.readthedocs.io/en/latest/tutorial/replaying-failures.html", "https://hypothesis.readthedocs.io/en/latest/reference/api.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Hypothesis: adicionar regressões com `@example`

## Em uma frase
`@example` acrescenta uma entrada escolhida manualmente à execução de um teste baseado em propriedades.

## Por que importa
Um exemplo explícito fixa uma regressão conhecida e protege-a mesmo quando a exploração gerada não volta a visitar aquela região do espaço de entradas.

## Como funciona
Anote a função com valores que reproduzem a condição importante e mantenha a mesma propriedade geral para que os casos gerados continuem ampliando a busca.

## Exemplo
Após corrigir um erro com string vazia, um caso decorado pode manter essa entrada como verificação explícita enquanto o teste ainda explora textos de outros tamanhos.

## Limites e trade-offs
O exemplo decorado não é reduzido pelo processo de shrinking; ele pode repetir informações já cobertas por uma estratégia que gera aquele valor com frequência.

## Como verificar
Execute o teste em modo normal e confirme que a regressão explícita aparece junto das amostras geradas sem alterar a regra que a propriedade afirma.

## Conexões
- [[hyp-floats-dominio-na-infinito]] — Veja também: Hypothesis: definir o domínio numérico de floats.
- [[hyp-example-database-replay]] — Veja também: Hypothesis: banco persistente para replay de falhas.

## Fontes
- [Hypothesis — Replaying failures](https://hypothesis.readthedocs.io/en/latest/tutorial/replaying-failures.html) — banco de exemplos, replay, @example e @reproduce_failure; consultado em 2026-10-02.
- [Hypothesis — API Reference](https://hypothesis.readthedocs.io/en/latest/reference/api.html) — @given, exemplos, inferência, settings, HealthCheck e configuração pública; consultado em 2026-10-02.
