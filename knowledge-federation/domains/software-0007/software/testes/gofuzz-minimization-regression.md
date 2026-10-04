---
id: software.testes.tranche23.001698
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

# Minimização automática e a falha que vira teste permanente

## Em uma frase
Quando um input falha, a doc descreve o fluxo: o motor tenta minimizar para o menor valor ainda reprodutível e mais legível a humanos, loga o erro e grava a entrada em testdata/fuzz/{FuzzTestName}/{hash} — a partir daí, aquele input roda pelo go test padrão, "serving as a regression test once the bug has been fixed", e a doc formula o próximo passo: diagnosticar, corrigir e submeter o patch com o arquivo novo como teste de regressão.

## Por que importa
O fuzzing encerra o ciclo achar-provar-registrar sozinho: o hash do arquivo é também o seletor de reprodução (go test -run=FuzzFoo/hash), então cada crash que sai da campanha chega ao code review já como caso permanente da suíte.

## Como funciona
Os knobs documentados na seção Custom settings controlam essa fase: -fuzzminimizetime limita tempo ou iterações de cada tentativa de minimização (default 60s) e aceitar 0 desativa a minimização; -fuzztime limita o total da campanha; -parallel define o número de processos.

## Exemplo
Encontre um crash com -fuzztime 30s, abra o arquivo escrito em testdata/fuzz, rode go test sem flags e veja a regressão falhar por si — depois minimize manualmente o conteúdo mantendo a falha para conferir o que o motor tentou fazer.

## Limites e trade-offs
A minimização heurística pode não chegar ao mínimo semântico — a doc fala em "attempt" — e, com minimização desligada, a falha persiste como foi encontrada: maiores e menos legíveis, mas ainda reproduzíveis.

## Como verificar
Abra a subseção Failing input e a seção Custom settings da página Go Fuzzing e confirme a frase da escrita em testdata, o formato do comando To re-run e o default de 60 segundos.

## Conexões
- [[gofuzz-failure-causes]] — Veja também: O que conta como falha — inclusive o timeout de um segundo.
- [[gofuzz-cache-and-ossfuzz]] — Veja também: Corpus gerado na GOCACHE, campanha contínua no OSS-Fuzz.

## Fontes
- [Go — Go Fuzzing (documentação oficial)](https://go.dev/doc/security/fuzz/) — requisitos, modos, saída, falhas, minimização, formato do corpus e glossário; consultado em 2026-10-03.
- [Go — docs de cmd/go](https://pkg.go.dev/cmd/go) — flags de fuzzing documentadas no pacote do comando; consultado em 2026-10-03.
