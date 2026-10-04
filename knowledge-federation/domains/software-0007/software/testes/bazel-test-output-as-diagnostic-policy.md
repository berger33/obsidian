---
id: software.testes.tranche14.000754
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

# Bazel: escolher saída de teste adequada ao diagnóstico

## Em uma frase
`--test_output` controla como stdout e stderr dos testes aparecem durante `bazel test`, com modos úteis para resumo, falhas, tudo ou transmissão ao vivo.

## Por que importa
A política de saída afeta legibilidade e volume de logs, não o critério de sucesso do processo de teste.

## Como funciona
Use `summary` para execução rotineira, `errors` para inspecionar falhas, `all` ao investigar comportamento de casos aprovados e `streamed` quando acompanhar um teste em tempo real for necessário.

## Exemplo
Na CI, `bazel test //... --test_output=errors` mantém o log compacto e imprime a saída agregada dos testes que falharam.

## Limites e trade-offs
O modo `streamed` altera a experiência da execução e pode interagir com outras opções; não o use como substituto para coletar relatórios persistentes.

## Como verificar
Force uma falha controlada e confirme qual saída aparece, se há log individual em `bazel-testlogs` e se o resultado final continua identificável.

## Conexões
- [[bazel-test-size-and-timeout]] — Veja também: Bazel: separar tamanho de teste e limite de tempo.
- [[bazel-test-env-declaration]] — Veja também: Bazel: declarar variáveis de ambiente de teste.

## Fontes
- [Bazel — Commands and Options](https://bazel.build/docs/user-manual) — opções de bazel test, seleção de alvos, variáveis, saída e argumentos; consultado em 2026-10-02.
- [Bazel — Test encyclopedia](https://bazel.build/reference/test-encyclopedia) — contrato normativo do ambiente de execução, hermeticidade, runfiles, timeout e shards; consultado em 2026-10-02.
