---
id: software.testes.tranche23.001699
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
fontes: ["https://go.dev/doc/security/fuzz/", "https://google.github.io/oss-fuzz/getting-started/new-project-guide/go-lang/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Corpus gerado na GOCACHE, campanha contínua no OSS-Fuzz

## Em uma frase
A doc separa os dois corpora com nomes e endereços: o seed corpus — f.Add mais testdata/fuzz — é versionado e roda sempre; o generated corpus, mantido pelo motor durante a campanha para registrar progresso, fica em $GOCACHE/fuzz e "só é usado durante o fuzzing" — nada em que o pipeline normal deva depender.

## Por que importa
Entender os dois repositórios evita os dois erros clássicos: commitar inputs descartáveis gerados pela campanha e, no oposto, achar que limpar o cache perde alguma regressão.

## Como funciona
A página ancora o caminho contínuo fora da máquina local: fuzz tests nativos são suportados pelo OSS-Fuzz, que mantém as corporas em escala, com guia específica para Go (seção native Go fuzzing da new-project-guide) — e a doc lista no glossário o papel de cada peça: mutator manipula entradas, engine mantém corpus, identifica cobertura nova e reporta falhas.

## Exemplo
Limpe o cache com go clean -cache e veja a campanha recomeçar sem os interesting acumulados; em seguida consulte o guia do OSS-Fuzz para Go para comparar com sua campanha local.

## Limites e trade-offs
O guia externo de integração OSS-Fuzz é maintained pelo projeto OSS-Fuzz, não pela documentação de fuzzing do Go — a página do Go apenas aponta para ele; e os termos do glossário definem papéis de motor, não APIs estáveis.

## Como verificar
Abra o Glossário da página Go Fuzzing e confirme as entradas generated corpus, seed corpus, mutator, fuzzing engine e a linha do suporte OSS-Fuzz na abertura do documento.

## Conexões
- [[gofuzz-minimization-regression]] — Veja também: Minimização automática e a falha que vira teste permanente.

## Fontes
- [Go — Go Fuzzing (documentação oficial)](https://go.dev/doc/security/fuzz/) — requisitos, modos, saída, falhas, minimização, formato do corpus e glossário; consultado em 2026-10-03.
- [OSS-Fuzz — guia para Go (native fuzzing)](https://google.github.io/oss-fuzz/getting-started/new-project-guide/go-lang/) — suporte a fuzz tests nativos citado pela doc do Go; consultado em 2026-10-03.
