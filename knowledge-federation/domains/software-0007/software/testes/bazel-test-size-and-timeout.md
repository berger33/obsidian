---
id: software.testes.tranche14.000753
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-14.md"
fontes: ["https://bazel.build/reference/be/common-definitions#common-attributes-tests", "https://bazel.build/reference/test-encyclopedia"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Bazel: separar tamanho de teste e limite de tempo

## Em uma frase
`size` informa a demanda de recursos presumida, enquanto `timeout` define a classe de duração; os atributos são relacionados, mas não intercambiáveis.

## Por que importa
Metadados coerentes ajudam o agendador e evitam matar testes lentos por limites implícitos excessivamente curtos ou reservar capacidade incompatível.

## Como funciona
Declare os atributos na regra de teste e escolha a classe mais estreita que comporte a execução; sem timeout explícito, o tamanho determina a classe implícita.

## Exemplo
Um teste que usa poucos recursos mas demora bastante pode ter tamanho pequeno e timeout longo, em vez de declarar artificialmente uma classe enorme.

## Limites e trade-offs
Valores maiores não tornam o teste mais rápido nem mais determinístico, e limites generosos demais podem ocultar regressões de duração.

## Como verificar
Compare distribuição observada de runtime e consumo com os metadados da regra e use warnings de timeout para encontrar estimativas infladas.

## Conexões
- [[bazel-test-shard-contract]] — Veja também: Bazel: implementar o contrato de shards no runner.
- [[bazel-test-output-as-diagnostic-policy]] — Veja também: Bazel: escolher saída de teste adequada ao diagnóstico.

## Fontes
- [Bazel — Common test-rule attributes](https://bazel.build/reference/be/common-definitions#common-attributes-tests) — atributos compartilhados de regras de teste, como size, timeout, flaky e shard_count; consultado em 2026-10-02.
- [Bazel — Test encyclopedia](https://bazel.build/reference/test-encyclopedia) — contrato normativo do ambiente de execução, hermeticidade, runfiles, timeout e shards; consultado em 2026-10-02.
