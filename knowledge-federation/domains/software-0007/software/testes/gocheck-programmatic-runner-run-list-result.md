---
id: software.testes.tranche26.001988
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

# Execução e listagem programática de suítes: Run, RunAll, List, ListAll, RunConf e Result

## Em uma frase
Além de TestingT, a documentação em pkg.go.dev/gopkg.in/check.v1 expõe a API programática de execução e introspecção baseada em *RunConf e *Result: func List(suite interface{}, runConf *RunConf) []string retorna os nomes das funções de teste de uma suíte que serão executadas com a configuração dada; func ListAll(runConf *RunConf) []string lista todas as funções das suítes registradas com Suite; func Run(suite interface{}, runConf *RunConf) *Result e func RunAll(runConf *RunConf) *Result executam uma ou todas as suítes devolvendo um *Result (que possui os métodos Add(other *Result), Passed() bool e String() string).

## Por que importa
Expor List, ListAll, Run e RunAll retornando structs *Result (em vez de apenas imprimir na tela e chamar os.Exit) permite construir runners customizados, testar os próprios helpers de teste programaticamente e inspecionar com r.Passed() e r.String() o desfecho de uma suíte em memória.

## Como funciona
Use check.List ou check.ListAll com um *check.RunConf para descobrir quais testes casam com determinada configuração, e use check.Run ou check.RunAll quando precisar executar suítes programaticamente e agregar resultados com r.Add(outroResult).

## Exemplo
Um meta-teste que valida o comportamento de uma suíte auxiliar pode chamar res := check.Run(&SuiteDeExemplo{}, &check.RunConf{}) e afirmar que res.Passed() retorna o booleano esperado.

## Limites e trade-offs
No uso cotidiano com go test, você não precisa chamar RunAll manualmente: como documentado na própria página, func TestingT(testingT *testing.T) já executa todas as suítes registradas com Suite e reporta falhas ao pacote testing.

## Como verificar
Conferi as funções List, ListAll, Run, RunAll e os tipos Result e RunConf em pkg.go.dev/gopkg.in/check.v1.

## Conexões
- [[gocheck-benchmark-timer-methods-on-c]] — Veja também: Suporte a benchmarks na mesma estrutura *check.C: ResetTimer, StartTimer, StopTimer e SetBytes.
- [[gocheck-source-files-and-canonical-urls]] — Veja também: Estrutura enxuta do repositório go-check/check e URLs canônicas do projeto.

## Fontes
- [Pacote check (gopkg.in/check.v1) no pkg.go.dev](https://pkg.go.dev/gopkg.in/check.v1) — Referência oficial da API de gopkg.in/check.v1 no pkg.go.dev com funções Suite, TestingT, Run, RunAll, List e ListAll, tipo C (Assert, Check, ExpectFailure, MkDir, Skip, timers de benchmark), Checker, Not, CheckerInfo e Commentf.; consultado em 2026-10-03.
- [gocheck — README oficial (branch v1)](https://raw.githubusercontent.com/go-check/check/v1/README.md) — README oficial do gocheck (gopkg.in/check.v1) com instruções de instalação go get gopkg.in/check.v1, importação como pacote check e links oficiais.; consultado em 2026-10-03.
