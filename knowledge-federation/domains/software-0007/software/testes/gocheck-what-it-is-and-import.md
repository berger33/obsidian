---
id: software.testes.tranche26.001980
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-26.md"
fontes: ["https://raw.githubusercontent.com/go-check/check/v1/README.md", "https://pkg.go.dev/gopkg.in/check.v1"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# gocheck (gopkg.in/check.v1): extensão rica sobre o pacote testing padrão do Go

## Em uma frase
O README oficial e a visão geral em pkg.go.dev/gopkg.in/check.v1 definem o pacote como uma extensão rica de testes ("a rich testing extension for Go's testing package"): instala-se com go get gopkg.in/check.v1, importa-se com import "gopkg.in/check.v1" e utiliza-se check como o nome do pacote dentro do código Go.

## Por que importa
O pacote testing da biblioteca padrão do Go foi desenhado para ser minimalista (sem asserções baseadas em matchers, sem suítes baseadas em structs com estado compartilhado e, historicamente, sem diretórios temporários por teste); o gocheck adiciona suítes, checkers plugáveis e helpers mantendo compatibilidade total com o comando go test.

## Como funciona
Importe "gopkg.in/check.v1", referencie os símbolos pelo identificador de pacote check (como check.C, check.Suite, check.TestingT) e execute a suíte normalmente com o comando go test padrão da toolchain.

## Exemplo
A convenção do pacote em gopkg.in mapeia o caminho "gopkg.in/check.v1" diretamente para o identificador de pacote check no código-fonte, sem precisar de alias manual na cláusula import.

## Limites e trade-offs
Como o gocheck se acopla ao pacote testing por meio de uma função ponte (TestingT), você continua usando todas as flags habituais do go test para rodar o pacote.

## Como verificar
Conferi o README oficial no repositório go-check/check (v1) e a seção Overview em pkg.go.dev/gopkg.in/check.v1.

## Conexões
- [[gocheck-suite-and-testingt-bridge]] — Veja também: Registro de suítes com Suite(suite) e integração ao go test via TestingT(testingT).

## Fontes
- [gocheck — README oficial (branch v1)](https://raw.githubusercontent.com/go-check/check/v1/README.md) — README oficial do gocheck (gopkg.in/check.v1) com instruções de instalação go get gopkg.in/check.v1, importação como pacote check e links oficiais.; consultado em 2026-10-03.
- [Pacote check (gopkg.in/check.v1) no pkg.go.dev](https://pkg.go.dev/gopkg.in/check.v1) — Referência oficial da API de gopkg.in/check.v1 no pkg.go.dev com funções Suite, TestingT, Run, RunAll, List e ListAll, tipo C (Assert, Check, ExpectFailure, MkDir, Skip, timers de benchmark), Checker, Not, CheckerInfo e Commentf.; consultado em 2026-10-03.
