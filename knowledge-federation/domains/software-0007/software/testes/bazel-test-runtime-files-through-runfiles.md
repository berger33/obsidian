---
id: software.testes.tranche14.000751
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

# Bazel: fornecer arquivos de runtime por runfiles

## Em uma frase
Arquivos usados durante a execução devem chegar ao teste como entradas de runtime do alvo, e não por caminhos presumidos na árvore de saída.

## Por que importa
Runfiles tornam dados e executáveis acessíveis segundo o grafo declarado e permitem que o runner altere o local físico sem quebrar consumidores corretos.

## Como funciona
Declare os arquivos no atributo `data` da regra de teste e consulte-os pelo mecanismo de runfiles da linguagem; o sistema pode fornecer uma imagem lógica diferente do checkout.

## Exemplo
Uma fixture YAML compartilhada deve ser dependência de runtime do alvo de teste; o código resolve sua localização com a biblioteca runfiles, em vez de concatenar o caminho do workspace.

## Limites e trade-offs
O mecanismo concreto de resolução varia por linguagem e regra; `data` não corrige uma regra customizada que deixa de propagar runfiles.

## Como verificar
Remova acesso direto ao checkout, execute o alvo com sandboxing e confirme que cada arquivo necessário aparece em runfiles do teste.

## Conexões
- [[bazel-test-hermetic-runtime-boundary]] — Veja também: Bazel: delimitar o contrato hermético do teste.
- [[bazel-test-shard-contract]] — Veja também: Bazel: implementar o contrato de shards no runner.

## Fontes
- [Bazel — Common test-rule attributes](https://bazel.build/reference/be/common-definitions#common-attributes-tests) — atributos compartilhados de regras de teste, como size, timeout, flaky e shard_count; consultado em 2026-10-02.
- [Bazel — Test encyclopedia](https://bazel.build/reference/test-encyclopedia) — contrato normativo do ambiente de execução, hermeticidade, runfiles, timeout e shards; consultado em 2026-10-02.
