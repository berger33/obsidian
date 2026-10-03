---
id: software.testes.tranche23.001692
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
fontes: ["https://go.dev/doc/security/fuzz/", "https://go.dev/issue/44551"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Tipos permitidos nos argumentos de fuzzing (e por que a lista é curta)

## Em uma frase
A doc oficial restringe os fuzzing arguments a um conjunto fechado: string e slice de byte; os inteiros de 8 a 64 bits com seus aliases rúne e byte; os uint correspondentes; float32 e float64; e bool — nada além disso pode aparecer após o *testing.T no fuzz target.

## Por que importa
A limitação é estrutural: o motor mantém um corpus como texto legível e precisa round-trip entre bytes mutados e valores tipados; tipos de usuário exigiriam gramática, e o desenho da feature delega isso ao próprio código do target.

## Como funciona
O vínculo com o formato do corpus aparece na mesma página: cada linha de um arquivo de corpus é a notação literal do valor Go — int64(572293) etc. — exatamente como seria copiado de volta para código, o que só fecha com tipos escalares nomeados.

## Exemplo
Escreva um target aceitando (string, int64, bool), gere uma falha e abra o arquivo em testdata/fuzz: confira que cada linha recria um valor daqueles tipos, e tente registrar um target com struct — a recusa confirma a fronteira.

## Limites e trade-offs
Para entradas estruturadas, o caminho é o que a doc exemplifica: aceitar string ou bytes e fazer o parsing dentro do target — o que, aliás, é exatamente o tipo de código que mais beneficia de fuzzing, como a própria proposta (issue 44551) enquadra.

## Como verificar
Abra a lista em Requirements e a seção Corpus file format da página Go Fuzzing; confirme os tipos e a notação literal linha a linha.

## Conexões
- [[gofuzz-test-requirements]] — Veja também: As regras rígidas de um fuzz test: nome, arquivo e alvo único.
- [[gofuzz-seed-corpus]] — Veja também: Seed corpus: f.Add e o diretório testdata/fuzz.

## Fontes
- [Go — Go Fuzzing (documentação oficial)](https://go.dev/doc/security/fuzz/) — requisitos, modos, saída, falhas, minimização, formato do corpus e glossário; consultado em 2026-10-03.
- [Go — proposal de fuzzing nativo (issue 44551)](https://go.dev/issue/44551) — proposal referenciada pela doc oficial; consultado em 2026-10-03.
