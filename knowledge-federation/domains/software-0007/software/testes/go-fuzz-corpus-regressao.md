---
id: software.testes.tranche12.000584
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
fontes: ["https://go.dev/doc/tutorial/fuzz", "https://go.dev/doc/security/fuzz/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Go testing: corpus de fuzz como regressão executável

## Em uma frase
Um fuzz test pode combinar sementes declaradas no código com arquivos de corpus, e entradas que revelam falhas podem ser salvas para reprodução.

## Por que importa
A falha minimizada vira um caso persistente executado também no modo normal, aproximando exploração automatizada e suíte de regressão.

## Como funciona
Implemente `FuzzX` em arquivo `_test.go`, forneça seeds representativas e rode `go test -fuzz` com alvo e duração limitados em um job dedicado.

## Exemplo
Ao encontrar entrada inválida, Go grava um caso reprodutível sob `testdata/fuzz/<nome>`; o próximo `go test` executa essa semente sem continuar a exploração.

## Limites e trade-offs
Corpus enorme pode aumentar o tempo de toda execução normal, e seeds sem relação com formatos aceitos podem testar um contrato que o pacote não promete.

## Como verificar
Reproduza a entrada salva com `go test`, revise-a como fixture versionada e confirme que a função trata bytes arbitrários conforme a propriedade declarada.

## Conexões
- [[go-parallel-subtests-barreira]] — Veja também: Go testing: barreira de `t.Parallel` em subtestes.
- [[go-race-dinamico-limites]] — Veja também: Go testing: alcance e limite do detector `-race`.

## Fontes
- [Go — Getting started with fuzzing](https://go.dev/doc/tutorial/fuzz) — corpus de sementes, falhas minimizadas e execução de fuzz tests; consultado em 2026-10-02.
- [Go — Fuzzing overview](https://go.dev/doc/security/fuzz/) — tipos permitidos, corpus, funções de fuzz e modo de execução; consultado em 2026-10-02.
