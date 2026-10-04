---
id: software.testes.tranche26.001983
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

# A abstração Checker, o combinador lógico Not(checker) e CheckerInfo

## Em uma frase
Na seção Index / Types de pkg.go.dev/gopkg.in/check.v1, os matchers do gocheck são modelados pelo tipo Checker, acompanhado da função combinadora func Not(checker Checker) Checker e da estrutura de metadados CheckerInfo (com o método func (info *CheckerInfo) Info() *CheckerInfo).

## Por que importa
Representar cada regra de comparação como um objeto Checker com metadados próprios (CheckerInfo, que informa o nome do checker e os nomes dos parâmetros esperados) permite compor negações genéricas com check.Not(checker) e gerar mensagens de falha que nomeiam claramente o que era obtido versus esperado.

## Como funciona
Passe o Checker adequado como segundo argumento de c.Assert ou c.Check, envolva qualquer checker existente em check.Not(...) quando quiser afirmar a condição inversa (como check.Not(check.IsNil)) e implemente a interface Checker retornando um *CheckerInfo quando precisar de um matcher de domínio próprio.

## Exemplo
Em vez de manter pares duplicados de funções para cada comparação no pacote, check.Not(qualquerChecker) inverte o resultado lógico de qualquer Checker compatível.

## Limites e trade-offs
Quando um checker unário (como IsNil) ou binário é usado com número incorreto de argumentos em args, os metadados de CheckerInfo permitem ao gocheck diagnosticar a assinatura esperada pelo matcher.

## Como verificar
Conferi os tipos Checker, func Not(checker Checker) Checker e CheckerInfo no índice da documentação em pkg.go.dev/gopkg.in/check.v1.

## Conexões
- [[gocheck-assert-vs-check-methods]] — Veja também: A diferença crucial em *check.C: Assert interrompe o teste, Check continua a execução.
- [[gocheck-commentinterface-and-commentf]] — Veja também: Contexto rico em falhas de asserção com CommentInterface e Commentf.

## Fontes
- [Pacote check (gopkg.in/check.v1) no pkg.go.dev](https://pkg.go.dev/gopkg.in/check.v1) — Referência oficial da API de gopkg.in/check.v1 no pkg.go.dev com funções Suite, TestingT, Run, RunAll, List e ListAll, tipo C (Assert, Check, ExpectFailure, MkDir, Skip, timers de benchmark), Checker, Not, CheckerInfo e Commentf.; consultado em 2026-10-03.
- [gocheck — README oficial (branch v1)](https://raw.githubusercontent.com/go-check/check/v1/README.md) — README oficial do gocheck (gopkg.in/check.v1) com instruções de instalação go get gopkg.in/check.v1, importação como pacote check e links oficiais.; consultado em 2026-10-03.
