---
id: software.testes.tranche14.000756
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
fontes: ["https://bazel.build/docs/user-manual", "https://bazel.build/reference/test-encyclopedia"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Bazel: encaminhar opções do runner com test_arg

## Em uma frase
`--test_arg` encaminha argumentos ao programa de teste, permitindo usar filtros próprios sem confundir opções do framework com flags de Bazel.

## Por que importa
Separar opções do build das opções do runner deixa a linha de comando auditável e facilita reproduzir um subconjunto localmente.

## Como funciona
Passe cada argumento como opção `--test_arg` e confirme na documentação do framework como o executável interpreta e combina esses valores.

## Exemplo
Para um runner que aceita `--filter=checkout`, use `bazel test //payments:unit_tests --test_arg=--filter=checkout` e registre a mesma seleção no comando reproduzível.

## Limites e trade-offs
O significado, a repetição e o parsing dos argumentos são definidos pelo executável de teste; Bazel não valida que o filtro tenha selecionado casos.

## Como verificar
Inspecione a linha de comando recebida pelo runner ou use um filtro conhecido e confira no relatório quais casos foram realmente executados.

## Conexões
- [[bazel-test-env-declaration]] — Veja também: Bazel: declarar variáveis de ambiente de teste.
- [[bazel-test-target-selection-patterns]] — Veja também: Bazel: selecionar alvos de teste por padrões.

## Fontes
- [Bazel — Commands and Options](https://bazel.build/docs/user-manual) — opções de bazel test, seleção de alvos, variáveis, saída e argumentos; consultado em 2026-10-02.
- [Bazel — Test encyclopedia](https://bazel.build/reference/test-encyclopedia) — contrato normativo do ambiente de execução, hermeticidade, runfiles, timeout e shards; consultado em 2026-10-02.
