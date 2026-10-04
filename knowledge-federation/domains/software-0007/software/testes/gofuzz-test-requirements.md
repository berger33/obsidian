---
id: software.testes.tranche23.001691
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

# As regras rígidas de um fuzz test: nome, arquivo e alvo único

## Em uma frase
A seção Requirements da doc oficial enumera o que um fuzz test deve cumprir: ser uma função com nome no estilo FuzzXxx, aceitar apenas uma testing.F e não retornar valor; viver em arquivos _test.go; conter exatamente um fuzz target, que é a chamada a (*testing.F).Fuzz recebendo *testing.T como primeiro parâmetro, seguido dos argumentos de fuzzing, sem retorno.

## Por que importa
O formato estranho é o que permite ao motor fazer tudo automaticamente: minimizar, persistir falhas como arquivo e reproduzir com go test sem flags — desvios viram erros de compilação ou de execução claros, não comportamento sutil.

## Como funciona
A doc ancora os termos no glossário: "fuzz test" é a função no arquivo de teste; "fuzz target" é a função passada a (*testing.F).Fuzz, executada para cada entrada do corpus; "fuzzing arguments" são os tipos mutados pelo mutator e repassados ao target.

## Exemplo
Escreva FuzzParse que chama f.Fuzz com (t *testing.T, data []byte) e tente registrar um segundo f.Fuzz no mesmo teste: o motor reclama, confirmando a regra do alvo único documentada.

## Limites e trade-offs
As exigências valem para o fuzz test como unidade — nada impede vários fuzz tests distintos no mesmo pacote, cada um com seu target; a restrição de unicidade é por teste, como a doc descreve.

## Como verificar
Abra a seção Writing fuzz tests/Requirements da página Go Fuzzing e confira as cinco regras listadas e as definições correlatas no glossário abaixo.

## Conexões
- [[gofuzz-what-it-is]] — Veja também: Fuzzing nativo na toolchain do Go desde a 1.18.
- [[gofuzz-argument-types]] — Veja também: Tipos permitidos nos argumentos de fuzzing (e por que a lista é curta).

## Fontes
- [Go — Go Fuzzing (documentação oficial)](https://go.dev/doc/security/fuzz/) — requisitos, modos, saída, falhas, minimização, formato do corpus e glossário; consultado em 2026-10-03.
- [Go — docs de cmd/go](https://pkg.go.dev/cmd/go) — flags de fuzzing documentadas no pacote do comando; consultado em 2026-10-03.
