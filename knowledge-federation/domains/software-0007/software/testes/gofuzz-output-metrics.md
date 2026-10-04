---
id: software.testes.tranche23.001696
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

# Lendo a saída do motor: execs, new interesting e baseline

## Em uma frase
A doc interpreta o log do fuzzing linha a linha: as primeiras linhas mostram o gathering baseline coverage, quando o motor executa os corpora seed e gerado para garantir que não há erros e entender que cobertura o corpus já traz; depois cada linha periódica traz elapsed, execs (com taxa por segundo) e new interesting — entradas que expandiram a cobertura além do corpus gerado.

## Por que importa
Saber que "new interesting" só conta entradas que abrem caminhos novos transforma a métrica em diagnóstico: a curva que desacelera não é o fuzzer cansando, é o corpus convergindo — com bursts ocasionais quando um caminho novo é descoberto.

## Como funciona
A própria página descreve o padrão esperado: crescimento rápido de interesting no início, desaceleração progressiva conforme as linhas cobertas se acumulam, e explosões ocasionais a cada nova branch — além do formato de exemplo com oito workers após o baseline.

## Exemplo
Deixe uma campanha alguns minutos e anote as três métricas em duas janelas de tempo; new interesting crescendo zero com elapsed alto é a confirmação textual do platô que a doc descreve.

## Limites e trade-offs
A taxa execs/sec depende de workers e do alvo — a doc lista o número de processos paralelos como default GOMAXPROCS — então comparar entre máquinas ou alvos pelas métricas cruas exige normalização que a página não fornece.

## Como verificar
Abra a subseção Command line output da página Go Fuzzing e confira a explicação de cada campo e do baseline gathering, com o exemplo de log.

## Conexões
- [[gofuzz-two-modes]] — Veja também: Dois modos de execução: go test puro e go test -fuzz.
- [[gofuzz-failure-causes]] — Veja também: O que conta como falha — inclusive o timeout de um segundo.

## Fontes
- [Go — Go Fuzzing (documentação oficial)](https://go.dev/doc/security/fuzz/) — requisitos, modos, saída, falhas, minimização, formato do corpus e glossário; consultado em 2026-10-03.
- [Go — docs de cmd/go](https://pkg.go.dev/cmd/go) — flags de fuzzing documentadas no pacote do comando; consultado em 2026-10-03.
