---
id: software.testes.tranche23.001693
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
fontes: ["https://go.dev/doc/security/fuzz/", "https://go.dev/doc/tutorial/fuzz"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Seed corpus: f.Add e o diretório testdata/fuzz

## Em uma frase
O seed corpus de um fuzz test é definido pela doc oficial como a composição das entradas passadas a (*testing.F).Add dentro do próprio teste com os arquivos do diretório testdata/fuzz/{NomeDoFuzzTest} do pacote — e a regra dura: os tipos de toda entrada seed devem ser idênticos aos argumentos do fuzzing, na mesma ordem, nos dois canais.

## Por que importa
Seeds não são decoração: o corpus de entrada é o que ancora a cobertura inicial, e os seeds versionados viram testes de regressão permanentes — a doc nota que entradas do seed corpus rodam por padrão com go test, com ou sem fuzzing ativo.

## Como funciona
A página mostra f.Add com os valores tipados, explica que arquivos individuais servem para binaries grandes "que você preferiria não copiar como código" e indica o tool go install golang.org/x/tools/cmd/file2fuzz@latest para converter arquivos binários ao formato de corpus de []byte.

## Exemplo
Adicione um seed mínimo via f.Add e um arquivo manual em testdata/fuzz/FuzzXxx, rode go test -run=^FuzzXxx$ e confirme que ambos executam como testes unitários antes de qualquer flag -fuzz.

## Limites e trade-offs
O -run citado serve para o filtro unitário; a doc apresenta o seed corpus como o mecanismo único dos dois modos, e o file2fuzz é um comando separado mantido no golang.org/x/tools — fora da toolchain principal do go test.

## Como verificar
Abra as seções Requirements, Corpus file format e Resources da página Go Fuzzing e confirme a definição de seed corpus, a regra de tipos e o bloco de instalação do file2fuzz.

## Conexões
- [[gofuzz-argument-types]] — Veja também: Tipos permitidos nos argumentos de fuzzing (e por que a lista é curta).
- [[gofuzz-corpus-format]] — Veja também: O formato literal do arquivo de corpus: go test fuzz v1.

## Fontes
- [Go — Go Fuzzing (documentação oficial)](https://go.dev/doc/security/fuzz/) — requisitos, modos, saída, falhas, minimização, formato do corpus e glossário; consultado em 2026-10-03.
- [Go — Tutorial: Fuzzing with Go](https://go.dev/doc/tutorial/fuzz) — tutorial profundo indicado na seção Resources da doc oficial; consultado em 2026-10-03.
