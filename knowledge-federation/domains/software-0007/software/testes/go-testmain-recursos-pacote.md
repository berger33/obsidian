---
id: software.testes.tranche12.000587
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
fontes: ["https://pkg.go.dev/testing", "https://pkg.go.dev/cmd/go#hdr-Testing_flags"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Go testing: centralizar preparação no `TestMain`

## Em uma frase
`TestMain(m *testing.M)` dá ao pacote um ponto único para preparar recursos antes de rodar seus testes e limpar depois.

## Por que importa
Um ciclo explícito de pacote é útil para dependências realmente compartilhadas, mas pode acoplar testes que seriam mais fáceis de executar isoladamente.

## Como funciona
Crie recursos antes de `m.Run()`, guarde o código de saída, faça cleanup antes de retornar ou chamar `os.Exit` e evite depender de `defer` após uma chamada que encerra o processo.

## Exemplo
Um conjunto de testes pode iniciar um processo auxiliar uma vez, executar `m.Run`, finalizar o processo e preservar o status devolvido pelo runner.

## Limites e trade-offs
Falha durante preparação pode impedir descoberta de um teste específico, e estado compartilhado deve ser seguro para todos os testes do pacote.

## Como verificar
Execute um teste isolado e o pacote completo para confirmar que recursos sobem uma vez, encerram depois e deixam o código de saída refletir falhas.

## Conexões
- [[go-testing-synctest-tempo-virtual]] — Veja também: Go testing: coordenar concorrência com `testing/synctest`.
- [[go-tdir-cleanup-descendants]] — Veja também: Go testing: temporários isolados com `t.TempDir`.

## Fontes
- [Go — package testing](https://pkg.go.dev/testing) — testes, subtests, helpers, cleanup, benchmarks e interfaces do pacote testing; consultado em 2026-10-02.
- [Go — go test flags](https://pkg.go.dev/cmd/go#hdr-Testing_flags) — seleção e execução de testes, fuzzing e benchmarks pela ferramenta go; consultado em 2026-10-02.
