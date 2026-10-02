---
id: software.testes.tranche12.000585
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
fontes: ["https://go.dev/doc/articles/race_detector", "https://pkg.go.dev/testing"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Go testing: alcance e limite do detector `-race`

## Em uma frase
O detector de corridas instrumenta o programa e reporta acessos concorrentes incompatíveis que aconteceram durante a execução observada.

## Por que importa
Uma execução limpa fornece evidência útil para caminhos exercitados, mas não certifica que caminhos não visitados ou workloads de produção estejam livres de data races.

## Como funciona
Rode pacotes com `go test -race`, complemente casos raros com testes de estresse e inclua cargas representativas quando um caminho concorrente depender de configuração externa.

## Exemplo
Uma corrida só aparece após duas goroutines alterarem a mesma estrutura; o detector mostra stacks de leitura e escrita quando essa interleaving ocorre durante o teste.

## Limites e trade-offs
Builds com `-race` têm custo de tempo e memória e dependem de plataformas suportadas; códigos excluídos por tags de build podem não participar da execução.

## Como verificar
Registre no pipeline quais pacotes e alvos são cobertos e introduza uma corrida controlada localmente para confirmar que o modo realmente instrumenta o binário testado.

## Conexões
- [[go-fuzz-corpus-regressao]] — Veja também: Go testing: corpus de fuzz como regressão executável.
- [[go-testing-synctest-tempo-virtual]] — Veja também: Go testing: coordenar concorrência com `testing/synctest`.

## Fontes
- [Go — Data Race Detector](https://go.dev/doc/articles/race_detector) — execução instrumentada e limite dinâmico de detecção de corridas; consultado em 2026-10-02.
- [Go — package testing](https://pkg.go.dev/testing) — testes, subtests, helpers, cleanup, benchmarks e interfaces do pacote testing; consultado em 2026-10-02.
