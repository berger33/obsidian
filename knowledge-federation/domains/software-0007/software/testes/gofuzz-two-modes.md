---
id: software.testes.tranche23.001695
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-23.md"
fontes: ["https://go.dev/doc/security/fuzz/", "https://pkg.go.dev/cmd/go"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Dois modos de execução: go test puro e go test -fuzz

## Em uma frase
A doc separa explicitamente os modos: rodar o fuzz test como teste unitário (padrão do go test, executando as entradas do seed corpus e reportando falhas antes de sair) ou habilitar o fuzzing com go test -fuzz=Regex, onde o regex deve casar exatamente um fuzz test; por padrão, todos os outros testes do pacote rodam antes do fuzzing começar.

## Por que importa
A regra "outros testes primeiro" existe para o fuzzing não reportar o que a suíte normal já pegaria — a doc declara essa intenção ao descrever o default — e mantém o seed corpus como gate de regressão barato no pipeline comum.

## Como funciona
A página avisa que cabe a você decidir quanto tempo rodar: "It is very possible that an execution of fuzzing could run indefinitely" sem erros; o fuzzing termina por falha encontrada ou cancelamento do usuário, por exemplo Ctrl-C.

## Exemplo
Rode go test -v -run=FuzzXxx para ver só as seeds como unit tests e go test -fuzz=FuzzXxx para a campanha; compare as primeiras linhas da saída — gathering baseline coverage só aparece no modo fuzz.

## Limites e trade-offs
A plataforma importa: a doc recomenda rodar onde há instrumentação de cobertura — hoje AMD64 e ARM64 — porque em outras arquiteturas o corpus não cresce significativamente; e a execução contínua em serviços é apontada como trabalho futuro via issue 50192.

## Como verificar
Abra a seção Running fuzz tests da página Go Fuzzing e confirme a descrição dos dois modos, a frase do regex único e a nota de plataforma para coverage instrumentation.

## Conexões
- [[gofuzz-corpus-format]] — Veja também: O formato literal do arquivo de corpus: go test fuzz v1.
- [[gofuzz-output-metrics]] — Veja também: Lendo a saída do motor: execs, new interesting e baseline.

## Fontes
- [Go — Go Fuzzing (documentação oficial)](https://go.dev/doc/security/fuzz/) — requisitos, modos, saída, falhas, minimização, formato do corpus e glossário; consultado em 2026-10-03.
- [Go — docs de cmd/go](https://pkg.go.dev/cmd/go) — flags de fuzzing documentadas no pacote do comando; consultado em 2026-10-03.
