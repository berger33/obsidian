---
id: software.testes.tranche26.001985
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

# Controle de fluxo e falhas conhecidas em *check.C: ExpectFailure, Skip, FailNow e SucceedNow

## Em uma frase
O índice de métodos de type C em pkg.go.dev/gopkg.in/check.v1 inclui controles refinados sobre o desfecho do teste: func (c *C) ExpectFailure(reason string), func (c *C) Skip(reason string), func (c *C) Fail(), func (c *C) FailNow(), func (c *C) Failed() bool, func (c *C) Succeed() e func (c *C) SucceedNow().

## Por que importa
O método c.ExpectFailure(reason) é um diferencial raro em frameworks de teste Go: ele permite marcar que um teste documenta um bug conhecido ainda não corrigido — se o teste falhar, a falha é registrada como esperada com a razão informada sem quebrar a suíte; e quando alguém corrigir o bug e o teste passar a ter sucesso, o runner alerta que uma falha esperada deixou de falhar.

## Como funciona
Use c.Skip("motivo") quando o ambiente não suportar aquele teste; use c.ExpectFailure("issue #123: descrição") para manter um teste de regressão ativo enquanto a correção definitiva ainda está pendente; e use FailNow() ou SucceedNow() quando precisar encerrar imediatamente a execução do método atual.

## Exemplo
Em conjunto com os métodos tradicionais Error, Errorf, Fatal, Fatalf, Log e Logf em *check.C, a equipe tem paridade completa com *testing.T somada a ExpectFailure e SucceedNow.

## Limites e trade-offs
Não use ExpectFailure como muleta permanente para testes flaky intermitentes: como ele espera que o teste falhe, uma execução em que o teste flaky passe por acaso será reportada como anomalia.

## Como verificar
Conferi a lista de métodos de type C na seção Index de pkg.go.dev/gopkg.in/check.v1.

## Conexões
- [[gocheck-commentinterface-and-commentf]] — Veja também: Contexto rico em falhas de asserção com CommentInterface e Commentf.
- [[gocheck-mkdir-and-gettestlog-helpers]] — Veja também: Diretórios temporários isolados com c.MkDir() e inspeção de log com c.GetTestLog() e c.TestName().

## Fontes
- [Pacote check (gopkg.in/check.v1) no pkg.go.dev](https://pkg.go.dev/gopkg.in/check.v1) — Referência oficial da API de gopkg.in/check.v1 no pkg.go.dev com funções Suite, TestingT, Run, RunAll, List e ListAll, tipo C (Assert, Check, ExpectFailure, MkDir, Skip, timers de benchmark), Checker, Not, CheckerInfo e Commentf.; consultado em 2026-10-03.
- [gocheck — README oficial (branch v1)](https://raw.githubusercontent.com/go-check/check/v1/README.md) — README oficial do gocheck (gopkg.in/check.v1) com instruções de instalação go get gopkg.in/check.v1, importação como pacote check e links oficiais.; consultado em 2026-10-03.
