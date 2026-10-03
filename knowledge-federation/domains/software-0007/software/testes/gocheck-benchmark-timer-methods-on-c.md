---
id: software.testes.tranche26.001987
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

# Suporte a benchmarks na mesma estrutura *check.C: ResetTimer, StartTimer, StopTimer e SetBytes

## Em uma frase
O tipo *check.C em pkg.go.dev/gopkg.in/check.v1 expõe também os métodos de controle de cronômetro e vazão de benchmarks: func (c *C) ResetTimer(), func (c *C) StartTimer(), func (c *C) StopTimer() e func (c *C) SetBytes(n int64).

## Por que importa
No pacote testing padrão do Go, testes usam *testing.T e benchmarks usam outro tipo (*testing.B), o que dificulta compartilhar o mesmo objeto de contexto e fixtures da suíte; ao unificar os métodos de timer (ResetTimer, StartTimer, StopTimer, SetBytes) dentro do próprio *check.C, o gocheck permite que métodos de benchmark vivam na mesma struct de suíte e usem as mesmas fixtures e asserções c.Assert.

## Como funciona
Após realizar preparações pesadas no início de um benchmark da suíte (ou dentro do setup), chame c.ResetTimer() (ou pause com c.StopTimer() e retome com c.StartTimer()) e informe c.SetBytes(n) quando estiver medindo taxa de processamento em bytes por segundo.

## Exemplo
Um benchmark que prepara um buffer de 1 MB antes do laço chama c.SetBytes(1024 * 1024) e c.ResetTimer() no próprio *check.C recebido pelo método da suíte.

## Limites e trade-offs
Chamar StartTimer/StopTimer dentro de cada iteração de um laço muito curto adiciona custo de medição; prefira fazer o setup antes do laço e chamar c.ResetTimer() uma única vez.

## Como verificar
Conferi os métodos ResetTimer, StartTimer, StopTimer e SetBytes no índice de type C em pkg.go.dev/gopkg.in/check.v1.

## Conexões
- [[gocheck-mkdir-and-gettestlog-helpers]] — Veja também: Diretórios temporários isolados com c.MkDir() e inspeção de log com c.GetTestLog() e c.TestName().
- [[gocheck-programmatic-runner-run-list-result]] — Veja também: Execução e listagem programática de suítes: Run, RunAll, List, ListAll, RunConf e Result.

## Fontes
- [Pacote check (gopkg.in/check.v1) no pkg.go.dev](https://pkg.go.dev/gopkg.in/check.v1) — Referência oficial da API de gopkg.in/check.v1 no pkg.go.dev com funções Suite, TestingT, Run, RunAll, List e ListAll, tipo C (Assert, Check, ExpectFailure, MkDir, Skip, timers de benchmark), Checker, Not, CheckerInfo e Commentf.; consultado em 2026-10-03.
- [gocheck — README oficial (branch v1)](https://raw.githubusercontent.com/go-check/check/v1/README.md) — README oficial do gocheck (gopkg.in/check.v1) com instruções de instalação go get gopkg.in/check.v1, importação como pacote check e links oficiais.; consultado em 2026-10-03.
