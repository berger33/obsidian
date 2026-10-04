---
id: software.testes.tranche12.000583
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-12.md"
fontes: ["https://pkg.go.dev/testing", "https://go.dev/doc/articles/race_detector"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Go testing: barreira de `t.Parallel` em subtestes

## Em uma frase
Um subteste que chama `t.Parallel` pausa até a função do teste pai retornar, e o pai aguarda a conclusão dos filhos paralelos.

## Por que importa
Entender essa barreira ajuda a definir a duração de fixtures do pai e a evitar mutações concorrentes em valores capturados por casos diferentes.

## Como funciona
Use paralelismo somente para cenários independentes, não altere no pai dados que os filhos ainda leem e mantenha recursos comuns válidos até todos os descendentes terminarem.

## Exemplo
Uma tabela de regras imutável pode alimentar vários subtestes paralelos, enquanto cada filho cria seu próprio objeto mutável para executar a operação.

## Limites e trade-offs
Uma referência compartilhada pode gerar data race ou colisão externa mesmo quando a lista de casos parece somente leitura no código de teste.

## Como verificar
Rode os casos com detector de corridas e varie a ordem ou o número de subtestes para localizar dependências acidentais.

## Conexões
- [[go-testing-helper-error-location]] — Veja também: Go testing: atribuir falhas ao chamador com `t.Helper`.
- [[go-fuzz-corpus-regressao]] — Veja também: Go testing: corpus de fuzz como regressão executável.

## Fontes
- [Go — package testing](https://pkg.go.dev/testing) — testes, subtests, helpers, cleanup, benchmarks e interfaces do pacote testing; consultado em 2026-10-02.
- [Go — Data Race Detector](https://go.dev/doc/articles/race_detector) — execução instrumentada e limite dinâmico de detecção de corridas; consultado em 2026-10-02.
