---
id: software.testes.tranche26.001968
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-26.md"
fontes: ["https://raw.githubusercontent.com/esbmc/esbmc/master/README.md", "https://github.com/esbmc/esbmc"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Uso prático com --incremental-bmc e leitura do trace de contraexemplo por estados

## Em uma frase
Na seção How to use ESBMC (Verifying C Programs), o README apresenta um programa C com dois ponteiros globais int *a, *b alocados via malloc, onde o código faz *b++ = 0 antes de chamar foo() e ao final tenta dar free(a); free(b); — ao executar esbmc file.c --incremental-bmc, o verificador imprime o bloco [Counterexample] numerando State 1, State 2, State 3 com arquivo, linha, coluna, função, thread e a propriedade violada (Violated property).

## Por que importa
Como o ponteiro b foi incrementado (*b++ = 0), passar b depois para free(b) entrega um endereço deslocado em vez do ponteiro base retornado pelo malloc, além de malloc poder retornar NULL se não verificado; o trace de contraexemplo do ESBMC reconstrói cada atribuição de estado (incluindo o retorno 0 de malloc no State 2 e a dereferência no State 3) com linha, coluna e thread exatas.

## Como funciona
Invoque esbmc arquivo.c --incremental-bmc para procurar violações aumentando gradualmente o limite de desenrolamento e leia a sequência de blocos State N no [Counterexample] de cima para baixo para identificar em qual linha e com quais valores concretos a propriedade quebrou.

## Exemplo
No trace reproduzido pelo README, State 1 mostra a = (signed int *)(&dynamic_1_array[0]), State 2 mostra b = (signed int *)0 na linha 15 e State 3 aponta a propriedade violada na linha 16 ao desreferenciar *b++.

## Limites e trade-offs
O contraexemplo exibido pelo ESBMC inclui o identificador da thread (thread 0 no exemplo sequencial), o que se torna fundamental ao depurar traces intercalados de programas multi-threaded.

## Como verificar
Conferi a seção How to use ESBMC / Verifying C Programs e a saída [Counterexample] no README oficial.

## Conexões
- [[esbmc-editor-web-and-claude-code-integrations]] — Veja também: As três integrações oficiais fora do terminal: VS Code, ESBMC-Web e plugin Claude Code (mais GitHub Action).
- [[esbmc-architecture-publications-and-community]] — Veja também: Documentação de arquitetura, publicações científicas da SSVLab e comunidade no Zulip.

## Fontes
- [ESBMC — README oficial](https://raw.githubusercontent.com/esbmc/esbmc/master/README.md) — README oficial do ESBMC com oito linguagens suportadas, cinco frontends (Clang, Soot/Jimple, CPython 3.10, Solidity e ESBMC-PLC), algoritmos incremental BMC e k-induction, erros detectados, sete solvers SMT mais --bitwuzllob e --neurosym, PPA/Homebrew, integrações e trace de contraexemplo.; consultado em 2026-10-03.
- [Repositório oficial esbmc/esbmc](https://github.com/esbmc/esbmc) — Repositório oficial do ESBMC no GitHub com código-fonte, ARCHITECTURE.md, src/python-frontend/README.md e releases.; consultado em 2026-10-03.
