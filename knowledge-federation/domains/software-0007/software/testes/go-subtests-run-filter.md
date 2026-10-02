---
id: software.testes.tranche12.000580
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

# Go testing: hierarquia de subtests com `t.Run`

## Em uma frase
`t.Run` cria um subteste nomeado associado ao teste pai e possibilita executar subconjuntos por expressão de seleção.

## Por que importa
Subtestes organizam casos de tabela em resultados individuais e fornecem caminhos legíveis quando somente uma combinação falha.

## Como funciona
Passe nomes estáveis às chamadas `t.Run`, mantenha a preparação compartilhada no pai e use a opção `-run` para selecionar caminhos quando investigar uma falha específica.

## Exemplo
Uma tabela de formatos pode nomear cada linha como `empty`, `valid` ou `invalid`, deixando no output qual entrada falhou sem transformar a função em três cópias.

## Limites e trade-offs
Nomes derivados de dados podem conter caracteres interpretados pela expressão regular do runner; seleção parcial também pode deixar preparação ou cleanup fora do trecho investigado.

## Como verificar
Execute a suíte completa e depois selecione um único caminho com `go test -run`, conferindo que o output corresponde ao caso esperado.

## Conexões
- [[go-t-cleanup-subtest-scope]] — Veja também: Go testing: escopo de `t.Cleanup` com subtestes.

## Fontes
- [Go — package testing](https://pkg.go.dev/testing) — testes, subtests, helpers, cleanup, benchmarks e interfaces do pacote testing; consultado em 2026-10-02.
- [Go — go test flags](https://pkg.go.dev/cmd/go#hdr-Testing_flags) — seleção e execução de testes, fuzzing e benchmarks pela ferramenta go; consultado em 2026-10-02.
