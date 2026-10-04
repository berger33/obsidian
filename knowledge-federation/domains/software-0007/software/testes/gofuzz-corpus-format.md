---
id: software.testes.tranche23.001694
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

# O formato literal do arquivo de corpus: go test fuzz v1

## Em uma frase
A doc especifica a codificação dos arquivos de corpus, idêntica para seed e corpus gerado: a primeira linha informa a versão do formato — go test fuzz v1 — e cada linha seguinte traz um valor no formato de expressão Go, por exemplo []byte com notação de escapes e int64(572293), devendo casar os tipos dos argumentos de fuzzing, em ordem; "can be copied directly into Go code".

## Por que importa
O formato texto-e-linha é o que torna crash reprodutível reviewável: o diff de um arquivo de regressão é legível em code review sem abrir ferramenta binária.

## Como funciona
A página justifica o cabeçalho de versão — nenhuma versão futura do formato é planejada, mas o design "must support this possibility" — e repete que a forma mais fácil de declarar seeds é f.Add, reservando arquivos para payloads que não pertencem ao código-fonte.

## Exemplo
Provogue um comportamento interessante, deixe o fuzzing gerar um arquivo de corpus e leia-o em hexdump e em texto: o conteúdo é a expressão dos valores, e as linhas recriam literalmente a chamada f.Add correspondente.

## Limites e trade-offs
A notação de escapes para []byte preserva bytes não imprimíveis, mas ler corpora binários complexos continua sendo trabalho de diff — a doc não promete legibilidade, promete round-trip determinístico para o motor.

## Como verificar
Abra a seção Corpus file format da página Go Fuzzing e confirme o exemplo de três linhas, a justificativa da versão e a frase de cópia direta para código Go.

## Conexões
- [[gofuzz-seed-corpus]] — Veja também: Seed corpus: f.Add e o diretório testdata/fuzz.
- [[gofuzz-two-modes]] — Veja também: Dois modos de execução: go test puro e go test -fuzz.

## Fontes
- [Go — Go Fuzzing (documentação oficial)](https://go.dev/doc/security/fuzz/) — requisitos, modos, saída, falhas, minimização, formato do corpus e glossário; consultado em 2026-10-03.
- [Go — docs de cmd/go](https://pkg.go.dev/cmd/go) — flags de fuzzing documentadas no pacote do comando; consultado em 2026-10-03.
