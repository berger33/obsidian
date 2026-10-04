---
id: software.testes.tranche14.000757
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
fontes: ["https://bazel.build/docs/user-manual", "https://bazel.build/reference/be/common-definitions#common-attributes-tests"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Bazel: selecionar alvos de teste por padrões

## Em uma frase
`bazel test` seleciona regras de teste por labels e padrões de targets, não por nomes internos de métodos de qualquer framework.

## Por que importa
Seleção precisa reduz feedback local sem modificar os alvos registrados ou transformar um subconjunto em prova da suite inteira.

## Como funciona
Use uma label explícita para um target, uma expansão de pacote como `//service/...` para escopo maior e os operadores de padrão documentados para compor seleções.

## Exemplo
`bazel test //billing:unit_test` restringe a execução a um target; `bazel test //billing/...` amplia para targets elegíveis nos pacotes sob aquele prefixo.

## Limites e trade-offs
O padrão pode selecionar mais alvos que o esperado, e escolher targets não garante que cada teste interno tenha sido descoberto pelo framework.

## Como verificar
Antes de atribuir significado ao resultado, revise targets selecionados no resumo do build e confira a descoberta interna do runner.

## Conexões
- [[bazel-test-arg-forwarding]] — Veja também: Bazel: encaminhar opções do runner com test_arg.
- [[bazel-build-event-protocol-test-results]] — Veja também: Bazel: consumir resultados de testes via BEP.

## Fontes
- [Bazel — Commands and Options](https://bazel.build/docs/user-manual) — opções de bazel test, seleção de alvos, variáveis, saída e argumentos; consultado em 2026-10-02.
- [Bazel — Common test-rule attributes](https://bazel.build/reference/be/common-definitions#common-attributes-tests) — atributos compartilhados de regras de teste, como size, timeout, flaky e shard_count; consultado em 2026-10-02.
