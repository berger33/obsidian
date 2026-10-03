---
id: software.testes.tranche26.001986
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

# Diretórios temporários isolados com c.MkDir() e inspeção de log com c.GetTestLog() e c.TestName()

## Em uma frase
Entre os métodos utilitários de type C listados em pkg.go.dev/gopkg.in/check.v1 estão func (c *C) MkDir() string, func (c *C) GetTestLog() string, func (c *C) TestName() string e func (c *C) Output(calldepth int, s string) error.

## Por que importa
Criar diretórios temporários em /tmp manualmente e lembrar de removê-los com defer os.RemoveAll em cada teste é repetitivo e propenso a deixar lixo quando um setup falha; c.MkDir() cria um diretório temporário exclusivo para o teste atual que o gocheck limpa automaticamente ao final da suíte, enquanto c.GetTestLog() e c.TestName() permitem inspecionar o próprio log acumulado e o nome qualificado do teste em execução.

## Como funciona
Sempre que um teste precisar gravar arquivos temporários em disco, chame dir := c.MkDir() para obter um caminho limpo; em teardowns ou testes de loggers, use c.GetTestLog() para verificar o que foi registrado no buffer de log do teste e c.TestName() para identificar o método atual.

## Exemplo
Em um teste de configuração que precisa salvar um arquivo YAML temporário, filepath.Join(c.MkDir(), "config.yml") entrega um caminho isolado sem precisar gerenciar limpeza manual.

## Limites e trade-offs
Os diretórios criados por c.MkDir() são removidos ao final da execução dos testes; se você precisar inspecionar os arquivos gerados após uma falha, consulte as opções de execução (RunConf) para preservar o diretório temporário.

## Como verificar
Conferi as assinaturas de MkDir, GetTestLog, TestName e Output no índice de type C em pkg.go.dev/gopkg.in/check.v1.

## Conexões
- [[gocheck-expectfailure-and-skip-control]] — Veja também: Controle de fluxo e falhas conhecidas em *check.C: ExpectFailure, Skip, FailNow e SucceedNow.
- [[gocheck-benchmark-timer-methods-on-c]] — Veja também: Suporte a benchmarks na mesma estrutura *check.C: ResetTimer, StartTimer, StopTimer e SetBytes.

## Fontes
- [Pacote check (gopkg.in/check.v1) no pkg.go.dev](https://pkg.go.dev/gopkg.in/check.v1) — Referência oficial da API de gopkg.in/check.v1 no pkg.go.dev com funções Suite, TestingT, Run, RunAll, List e ListAll, tipo C (Assert, Check, ExpectFailure, MkDir, Skip, timers de benchmark), Checker, Not, CheckerInfo e Commentf.; consultado em 2026-10-03.
- [gocheck — README oficial (branch v1)](https://raw.githubusercontent.com/go-check/check/v1/README.md) — README oficial do gocheck (gopkg.in/check.v1) com instruções de instalação go get gopkg.in/check.v1, importação como pacote check e links oficiais.; consultado em 2026-10-03.
