---
id: software.testes.tranche12.000581
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

# Go testing: escopo de `t.Cleanup` com subtestes

## Em uma frase
`T.Cleanup` registra uma função que roda quando o teste e seus subtestes concluírem, respeitando ordem inversa de registro.

## Por que importa
Limpeza associada ao escopo correto evita encerrar um recurso enquanto um subteste descendente ainda o utiliza e reduz vazamentos entre casos.

## Como funciona
Registre a remoção junto da criação do recurso; use `defer` quando a duração deve terminar ao retornar daquela função e `t.Cleanup` quando precisa durar até a árvore de testes terminar.

## Exemplo
Um teste pai inicia servidor efêmero, registra `server.Close` em `t.Cleanup` e cria filhos que enviam requests antes do encerramento.

## Limites e trade-offs
Registrar limpeza depois de uma criação parcialmente concluída pode deixar um recurso órfão se a preparação falhar no meio.

## Como verificar
Force a falha de um filho e confira que a limpeza ocorre uma vez, após os descendentes, sem interferir em outros testes.

## Conexões
- [[go-subtests-run-filter]] — Veja também: Go testing: hierarquia de subtests com `t.Run`.
- [[go-testing-helper-error-location]] — Veja também: Go testing: atribuir falhas ao chamador com `t.Helper`.

## Fontes
- [Go — package testing](https://pkg.go.dev/testing) — testes, subtests, helpers, cleanup, benchmarks e interfaces do pacote testing; consultado em 2026-10-02.
- [Go — go test flags](https://pkg.go.dev/cmd/go#hdr-Testing_flags) — seleção e execução de testes, fuzzing e benchmarks pela ferramenta go; consultado em 2026-10-02.
