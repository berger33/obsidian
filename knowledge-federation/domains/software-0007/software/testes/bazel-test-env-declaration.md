---
id: software.testes.tranche14.000755
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

# Bazel: declarar variáveis de ambiente de teste

## Em uma frase
`--test_env` injeta uma variável no ambiente do teste; especificar valor fixa esse valor, enquanto omiti-lo herda o valor do shell que iniciou Bazel.

## Por que importa
Ambiente não controlado pode tornar um teste dependente da máquina e comprometer resultados em sandbox ou execução remota.

## Como funciona
Prefira valores explícitos e mínimos em configuração reproduzível; use a forma sem valor somente quando herdar do processo chamador for parte deliberada do contrato.

## Exemplo
Um teste que precisa de locale previsível pode receber `--test_env=LANG=C.UTF-8`, em vez de depender do locale configurado no agente de CI.

## Limites e trade-offs
Injetar uma variável não a torna segura nem hermética se seu valor variar entre executores; segredos também não devem ser impressos nos logs.

## Como verificar
Rode o mesmo alvo com shell limpo e com valores ambientais diferentes e confirme que apenas entradas explicitamente contratadas alteram o comportamento.

## Conexões
- [[bazel-test-output-as-diagnostic-policy]] — Veja também: Bazel: escolher saída de teste adequada ao diagnóstico.
- [[bazel-test-arg-forwarding]] — Veja também: Bazel: encaminhar opções do runner com test_arg.

## Fontes
- [Bazel — Commands and Options](https://bazel.build/docs/user-manual) — opções de bazel test, seleção de alvos, variáveis, saída e argumentos; consultado em 2026-10-02.
- [Bazel — Test encyclopedia](https://bazel.build/reference/test-encyclopedia) — contrato normativo do ambiente de execução, hermeticidade, runfiles, timeout e shards; consultado em 2026-10-02.
