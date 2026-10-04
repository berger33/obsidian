---
id: software.testes.tranche23.001725
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

# Cada run é um banco SQLite aberto no boofuzz com boo open

## Em uma frase
A persistência documentada no Quickstart: o log de dados de cada run é salvo em um banco SQLite dentro do diretório boofuzz-results no diretório de trabalho atual — e a qualquer momento é possível reabrir a interface web sobre um daqueles arquivos com boo open <run-*.db>.

## Por que importa
Guardar o run como banco consultável em vez de stdout efêmero muda o fluxo de triagem: dois runs podem ser comparados depois, e o crash de ontem continua navegável sem manter o processo vivo.

## Como funciona
A nomenclatura run-*.db no diretório nomeado é o contrato; a ferramenta de linha de comando boo com o subcomando open é a porta de entrada para a UI, que durante o fuzzing já mostra o progresso ao vivo.

## Exemplo
Rode um fuzz curto, confirme a criação de boofuzz-results/run-0.db (ou seqüencial), e abra-o com boo open semanas depois para rever a tabela de testes sem reexecutar nada.

## Limites e trade-offs
A página descreve a existência do banco e do comando, não o esquema das tabelas; consultas SQL ad-hoc dependem de estrutura não estabilizada em doc pública — export CSV (feature listada no README) continua sendo o caminho suportado para análise externa.

## Como verificar
Confirme no Quickstart o parágrafo "The log data of each run..." com o nome do diretório e o snippet boo open; cruze com o bullet de CSV export no README.

## Conexões
- [[boofuzz-fuzz-run]] — Veja também: session.fuzz() — e a honestidade do "basic fuzzer".
- [[boofuzz-callbacks]] — Veja também: post_test_case_callbacks e ProtocolSessionReference: resposta que alimenta a próxima requisição.

## Fontes
- [boofuzz — Quickstart (Read the Docs)](https://boofuzz.readthedocs.io/en/stable/user/quickstart.html) — Session, Target, conexões, Requests, grafo, resultados e exemplos; consultado em 2026-10-03.
- [boofuzz — README.rst oficial](https://github.com/jtpereyda/boofuzz/blob/master/README.rst) — sucessão ao Sulley, features, instalação e comunidade; consultado em 2026-10-03.
