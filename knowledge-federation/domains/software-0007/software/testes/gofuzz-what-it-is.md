---
id: software.testes.tranche23.001690
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
fontes: ["https://go.dev/doc/security/fuzz/", "https://google.github.io/oss-fuzz/getting-started/new-project-guide/go-lang/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Fuzzing nativo na toolchain do Go desde a 1.18

## Em uma frase
A documentação oficial define: o Go suporta fuzzing na sua toolchain padrão a partir do Go 1.18, e descreve fuzzing como testes automatizados que manipulam continuamente as entradas do programa para achar bugs, usando guidance por cobertura para percorrer o código de forma inteligente — com valor destacado para exploits e vulnerabilidades, "edge cases which humans often miss".

## Por que importa
Antes da 1.18, fuzzar Go exigia ferramentas de terceiros com integração trabalhosa; ter o motor dentro de go test significa corpus, falhas e repro com os mesmos instrumentos de sempre, sem ferramenta externa.

## Como funciona
Os componentes do exemplo oficial são um fuzz test (a função FuzzXxx), fuzz targets registrados via f.Fuzz, entradas seed via f.Add e argumentos de fuzzing recebidos pelo target; a página também nota que fuzz tests nativos são suportados pelo OSS-Fuzz, o serviço contínuo do Google.

## Exemplo
Rode go version, confirme 1.18+, abra a seção Overview da doc de fuzzing e siga o tutorial oficial linkado logo abaixo do primeiro parágrafo.

## Limites e trade-offs
O texto de suíte contínua menciona suporte futuro para rodar fuzz tests ininterruptamente via ferramentas como OSS-Fuzz referenciando a issue 50192 — o motor da linguagem e o serviço de infra são camadas distintas que a doc mantém separadas.

## Como verificar
Confirme na página Go Fuzzing a frase "beginning in Go 1.18", a definição de fuzzing com coverage guidance e o link de suporte nativo do OSS-Fuzz.

## Conexões
- [[gofuzz-test-requirements]] — Veja também: As regras rígidas de um fuzz test: nome, arquivo e alvo único.

## Fontes
- [Go — Go Fuzzing (documentação oficial)](https://go.dev/doc/security/fuzz/) — requisitos, modos, saída, falhas, minimização, formato do corpus e glossário; consultado em 2026-10-03.
- [OSS-Fuzz — guia para Go (native fuzzing)](https://google.github.io/oss-fuzz/getting-started/new-project-guide/go-lang/) — suporte a fuzz tests nativos citado pela doc do Go; consultado em 2026-10-03.
