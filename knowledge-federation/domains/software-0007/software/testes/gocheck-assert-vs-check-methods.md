---
id: software.testes.tranche26.001982
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
fontes: ["https://pkg.go.dev/gopkg.in/check.v1", "https://raw.githubusercontent.com/go-check/check/v1/README.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# A diferença crucial em *check.C: Assert interrompe o teste, Check continua a execução

## Em uma frase
A documentação dos métodos de type C em pkg.go.dev/gopkg.in/check.v1 contrasta as duas verificações principais: func (c *C) Assert(obtained interface{}, checker Checker, args ...interface{}) garante que o valor obtido case com o esperado segundo o checker fornecido e, se não casar, registra o erro, marca o teste como falho e interrompe a execução do teste; já func (c *C) Check(obtained interface{}, checker Checker, args ...interface{}) bool faz a mesma verificação, registra o erro e marca o teste como falho, mas continua a execução do teste e retorna um booleano indicando o resultado.

## Por que importa
Em muitos testes, a primeira checagem é uma pré-condição estrutural (por exemplo, err == nil ou ponteiro não nulo) sem a qual a linha seguinte causaria panic, enquanto as checagens seguintes inspecionam vários campos independentes de uma struct onde é útil ver todas as divergências de uma só vez; Assert e Check separam exatamente esses dois comportamentos.

## Como funciona
Use c.Assert(obtido, checker, esperado) quando as linhas seguintes do teste dependerem do sucesso daquela verificação (equivalente semântico a t.Fatalf), e use c.Check(obtido, checker, esperado) quando quiser acumular múltiplas falhas no mesmo método de teste (equivalente semântico a t.Errorf), aproveitando o retorno bool de Check se quiser um if condicional.

## Exemplo
A própria documentação de Assert e Check observa que alguns checkers não precisam do argumento esperado (por exemplo, IsNil: c.Assert(err, check.IsNil)).

## Limites e trade-offs
Tantoc.Assert quanto c.Check aceitam no último elemento de args um valor que implemente CommentInterface (criado com check.Commentf) para anexar contexto ao log de falha sem passá-lo ao checker.

## Como verificar
Conferi a documentação de func (*C) Assert e func (*C) Check em pkg.go.dev/gopkg.in/check.v1.

## Conexões
- [[gocheck-suite-and-testingt-bridge]] — Veja também: Registro de suítes com Suite(suite) e integração ao go test via TestingT(testingT).
- [[gocheck-checker-not-and-checkerinfo]] — Veja também: A abstração Checker, o combinador lógico Not(checker) e CheckerInfo.

## Fontes
- [Pacote check (gopkg.in/check.v1) no pkg.go.dev](https://pkg.go.dev/gopkg.in/check.v1) — Referência oficial da API de gopkg.in/check.v1 no pkg.go.dev com funções Suite, TestingT, Run, RunAll, List e ListAll, tipo C (Assert, Check, ExpectFailure, MkDir, Skip, timers de benchmark), Checker, Not, CheckerInfo e Commentf.; consultado em 2026-10-03.
- [gocheck — README oficial (branch v1)](https://raw.githubusercontent.com/go-check/check/v1/README.md) — README oficial do gocheck (gopkg.in/check.v1) com instruções de instalação go get gopkg.in/check.v1, importação como pacote check e links oficiais.; consultado em 2026-10-03.
