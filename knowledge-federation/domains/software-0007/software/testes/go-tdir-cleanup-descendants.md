---
id: software.testes.tranche12.000588
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

# Go testing: temporários isolados com `t.TempDir`

## Em uma frase
`T.TempDir` cria um diretório temporário exclusivo para o teste e o remove quando o teste e seus descendentes terminam.

## Por que importa
Arquivos de fixture deixam de competir por caminhos globais e não exigem que cada caso lembre de apagar manualmente todos os artefatos.

## Como funciona
Crie o diretório por meio de `t.TempDir`, passe o caminho às dependências e mantenha dentro dele cada arquivo que só precisa existir durante aquela árvore de testes.

## Exemplo
Um teste de parser escreve uma configuração em seu diretório temporário e um subteste lê uma variante sem tocar no diretório compartilhado do repositório.

## Limites e trade-offs
Um processo filho pode continuar usando o caminho depois que o teste terminar se não for encerrado; limpeza automática não coordena subprocessos órfãos.

## Como verificar
Rode dois testes paralelos e confirme caminhos diferentes; verifique também que os arquivos temporários desaparecem após a execução completa.

## Conexões
- [[go-testmain-recursos-pacote]] — Veja também: Go testing: centralizar preparação no `TestMain`.
- [[go-b-loop-benchmark-comparacao]] — Veja também: Go testing: estruturar medições com `B.Loop`.

## Fontes
- [Go — package testing](https://pkg.go.dev/testing) — testes, subtests, helpers, cleanup, benchmarks e interfaces do pacote testing; consultado em 2026-10-02.
- [Go — go test flags](https://pkg.go.dev/cmd/go#hdr-Testing_flags) — seleção e execução de testes, fuzzing e benchmarks pela ferramenta go; consultado em 2026-10-02.
