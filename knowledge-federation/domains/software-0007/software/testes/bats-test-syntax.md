---
id: software.testes.tranche22.001561
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-22.md"
fontes: ["https://bats-core.readthedocs.io/en/latest/writing-tests.html", "https://github.com/bats-core/bats-core/blob/master/README.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# bats-core: a suíte é um script Bash

## Em uma frase
O arquivo .bats é avaliado como script Bash e cada caso é declarado com @test "descrição" { corpo }, que o pré-processador converte em uma função cujo nome é a descrição do teste.

## Por que importa
Manter o teste dentro da sintaxe nativa do shell evita camadas de tradução: você usa pipes, variáveis e funções de Bash sem aprender um DSL novo.

## Como funciona
O pré-processador reescreve cada bloco @test em função; o documento inteiro é executado n+1 vezes — a primeira passada conta os casos e depois cada teste roda em seu próprio processo.

## Exemplo
@test "foo imprime uso" { run foo; [ "$status" -eq 1 ]; } vira uma função de teste com esse título exato no relatório.

## Limites e trade-offs
Como o arquivo é reavaliado a cada caso, código solto fora de @test roda várias vezes; efeitos colaterais no topo do arquivo surpreendem quem espera execução única.

## Como verificar
Escreva um echo fora de @test e conte quantas linhas ele imprime ao rodar o arquivo com dois testes declarados.

## Conexões
- [[bats-what-it-is]] — Veja também: bats-core: testes TAP nativos para Bash.
- [[bats-errexit-assertions]] — Veja também: bats-core: cada linha viva é uma asserção.

## Fontes
- [Bats-core — Writing tests](https://bats-core.readthedocs.io/en/latest/writing-tests.html) — run, tags, setup/teardown, ganchos e armadilhas de escrita; consultado em 2026-10-03.
- [Bats-core — README oficial](https://github.com/bats-core/bats-core/blob/master/README.md) — proposta TAP, história do fork e licença MIT; consultado em 2026-10-03.
