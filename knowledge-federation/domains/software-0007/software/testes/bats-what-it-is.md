---
id: software.testes.tranche22.001560
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
fontes: ["https://github.com/bats-core/bats-core/blob/master/README.md", "https://bats-core.readthedocs.io/en/latest/index.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# bats-core: testes TAP nativos para Bash

## Em uma frase
O Bats (Bash Automated Testing System) é um framework de testes aderente ao TAP para Bash 3.2 ou superior, feito para verificar que os programas UNIX que você escreve se comportam como esperado.

## Por que importa
Scripts de shell, wrappers de CLI e utilitários de infraestrutura raramente recebem suítes de teste; o Bats traz o teste automatizado para o mesmo idioma do código, sem depender de bindings de outra linguagem.

## Como funciona
Cada arquivo de teste é um script Bash comum com blocos @test; o executável bats roda os arquivos .bats e emite resultados no formato TAP, que qualquer relatório CI já sabe interpretar.

## Exemplo
bats teste.bats imprime ✓ em cada caso que passa e, na última linha, "2 tests, 0 failures" — sem terminal, a saída vira TAP puro.

## Limites e trade-offs
Serve para testar qualquer programa UNIX, mas é onde o software escrito em Bash que ele brilha; lógicas complexas demais merecem migração para outra linguagem.

## Como verificar
Rode bats contra um comando qualquer e confirme que a saída sem terminal começa com "ok 1 ..." no padrão testanything.org.

## Conexões
- [[bats-test-syntax]] — Veja também: bats-core: a suíte é um script Bash.

## Fontes
- [Bats-core — README oficial](https://github.com/bats-core/bats-core/blob/master/README.md) — proposta TAP, história do fork e licença MIT; consultado em 2026-10-03.
- [Bats-core — Documentação oficial (página inicial)](https://bats-core.readthedocs.io/en/latest/index.html) — índice: tutorial, instalação, usage, gotchas e FAQ; consultado em 2026-10-03.
