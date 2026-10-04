---
id: software.testes.tranche23.001724
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
fontes: ["https://boofuzz.readthedocs.io/en/stable/user/quickstart.html", "https://github.com/jtpereyda/boofuzz/blob/master/README.rst"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# session.fuzz() — e a honestidade do "basic fuzzer"

## Em uma frase
Depois de conexão e grafo, o gatilho é literalmente session.fuzz(); e a página tem o cuidado raro de avisar logo abaixo: "at this point you have only a very basic fuzzer. Making it kick butt is up to you", apontando para os dois diretórios do repositório que servem de curriculum: examples/ e request_definitions/.

## Por que importa
O aviso define a linha entre scaffold e campanha real: o fuzz() default gera mutações sobre o grafo com gravação; os extras que separam um run útil (monitores, callbacks, vocabulário de mutação) são trabalho de script, como o modelo "biblioteca para construir fuzzers" promete.

## Como funciona
A página ainda entrega dois laboratórios reproduzíveis: ftp_simple.py roda contra o servidor FTP de Siim com porta default 8021 (a doc manda garantir a porta) e, para HTTP, http_simple.py e http_with_body.py rodam contra um servidor qualquer — o exemplo usa python3 -m http.server na mão.

## Exemplo
Suba python3 -m http.server e rode o http_simple.py do repo apontado para ele; abra o web UI do run e confirme cada requisição mutada com seu resultado gravado — o loop completo do aviso "basic".

## Limites e trade-offs
Os exemplos são do repositório, evoluem entre versões, e dependência de ambiente do servidor de terceiros não é suportada pela doc — a página só garante que o caminho existe, não que roda na sua versão específica do boofuzz.

## Como verificar
Abra a seção final do Quickstart e confirme o trecho do basic fuzzer, os dois diretórios apontados e as instruções dos exemplos FTP e HTTP.

## Conexões
- [[boofuzz-state-graph]] — Veja também: O grafo de Requests decide a ordem do fuzzing.
- [[boofuzz-results-sqlite]] — Veja também: Cada run é um banco SQLite aberto no boofuzz com boo open.

## Fontes
- [boofuzz — Quickstart (Read the Docs)](https://boofuzz.readthedocs.io/en/stable/user/quickstart.html) — Session, Target, conexões, Requests, grafo, resultados e exemplos; consultado em 2026-10-03.
- [boofuzz — README.rst oficial](https://github.com/jtpereyda/boofuzz/blob/master/README.rst) — sucessão ao Sulley, features, instalação e comunidade; consultado em 2026-10-03.
