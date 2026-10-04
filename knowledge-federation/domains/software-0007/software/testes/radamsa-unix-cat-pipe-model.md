---
id: software.testes.tranche25.001883
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-25.md"
fontes: ["https://gitlab.com/akihe/radamsa/-/raw/master/README.md", "https://gitlab.com/akihe/radamsa"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# O modelo mental do cat UNIX que quebra dados no caminho

## Em uma frase
A seção Fuzzing with Radamsa propõe pensar na ferramenta como o utilitário cat do UNIX que consegue quebrar os dados de maneiras interessantes enquanto eles fluem pelo pipe, escrevendo por padrão na saída padrão (stdout) e contando também com suporte para gerar múltiplas saídas e atuar como cliente ou servidor TCP.

## Por que importa
Adotar a convenção de filtro UNIX (stdin para stdout) permite encadear o Radamsa em qualquer pipeline shell existente sem arquivos temporários nem APIs específicas de linguagem.

## Como funciona
Passe o dado de entrada por pipe (echo "aaa" | radamsa) ou informe caminhos de arquivos de amostra como argumentos (radamsa sample.gz) e redirecione a saída padrão para o programa sob teste ou para um arquivo fuzzed.

## Exemplo
Nos exemplos iniciais do README, echo "aaa" | radamsa produz "aaaa" numa execução e "ːaaa" na execução seguinte.

## Limites e trade-offs
Diferentemente do cat tradicional, o README adverte que, quando recebe mais de um arquivo de amostra como argumento, o Radamsa geralmente usa apenas um ou alguns deles para construir cada saída individual, em vez de concatenar todos em ordem.

## Como verificar
Conferi a seção Fuzzing with Radamsa no README oficial.

## Conexões
- [[radamsa-build-single-binary]] — Veja também: Requisitos de SO e build que gera um binário único sem dependências externas.
- [[radamsa-urandom-and-seed-flag]] — Veja também: Entropia de /dev/urandom por padrão e reprodutibilidade com -s / --seed.

## Fontes
- [Radamsa — README oficial (A Crash Course to Radamsa)](https://gitlab.com/akihe/radamsa/-/raw/master/README.md) — README oficial do Radamsa com proposta black-box, origem no Protos Genome Project, build de binário único, uso em pipe como cat, semente -s/--seed, mutador numérico, -n e laço de captura de crash.; consultado em 2026-10-03.
- [Repositório oficial akihe/radamsa no GitLab](https://gitlab.com/akihe/radamsa) — Repositório oficial do Radamsa no GitLab com código-fonte, Makefile, mutadores e documentação.; consultado em 2026-10-03.
