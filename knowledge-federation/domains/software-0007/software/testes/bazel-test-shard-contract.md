---
id: software.testes.tranche14.000752
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
fontes: ["https://bazel.build/reference/test-encyclopedia", "https://bazel.build/reference/be/common-definitions#common-attributes-tests"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Bazel: implementar o contrato de shards no runner

## Em uma frase
`shard_count` solicita shards, mas cabe ao test runner suportar a partição e usar os índices de shard que o Bazel fornece.

## Por que importa
A divisão pode reduzir tempo sem paralelizar cada método de maneira implícita; todos os shards precisam cobrir partições não sobrepostas e coletivamente completas.

## Como funciona
Leia `TEST_TOTAL_SHARDS` e `TEST_SHARD_INDEX`, cujo índice começa em zero, e selecione os casos de forma determinística; um runner compatível também atualiza `TEST_SHARD_STATUS_FILE`.

## Exemplo
Com `shard_count = 4`, o runner pode distribuir identificadores de caso por round-robin usando o índice de cada processo e marcar o arquivo de status ao concluir.

## Limites e trade-offs
Nem todo framework ou runner aceita sharding; se não o implementar, solicitar shards pode fazer a execução ser considerada falha pelo Bazel.

## Como verificar
Execute cada shard isoladamente, confira união e interseção das seleções e confirme que o arquivo de status é atualizado em todas as partições.

## Conexões
- [[bazel-test-runtime-files-through-runfiles]] — Veja também: Bazel: fornecer arquivos de runtime por runfiles.
- [[bazel-test-size-and-timeout]] — Veja também: Bazel: separar tamanho de teste e limite de tempo.

## Fontes
- [Bazel — Test encyclopedia](https://bazel.build/reference/test-encyclopedia) — contrato normativo do ambiente de execução, hermeticidade, runfiles, timeout e shards; consultado em 2026-10-02.
- [Bazel — Common test-rule attributes](https://bazel.build/reference/be/common-definitions#common-attributes-tests) — atributos compartilhados de regras de teste, como size, timeout, flaky e shard_count; consultado em 2026-10-02.
