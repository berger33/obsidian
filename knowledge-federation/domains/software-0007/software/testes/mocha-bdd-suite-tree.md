---
id: software.testes.tranche13.000650
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-13.md"
fontes: ["https://mochajs.org/features/interfaces/", "https://mochajs.org/features/hooks/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Mocha: organizar suites BDD com describe e it

## Em uma frase
A interface BDD registra grupos com `describe()` e exemplos individuais com `it()`.

## Por que importa
A hierarquia dá nomes ao comportamento e limita hooks ao grupo onde foram declarados, em vez de esconder preparação dentro do corpo de cada verificação.

## Como funciona
Separe cenários por capacidade ou estado observável, mantenha descrições que expliquem a expectativa e use hooks do grupo apenas para recursos realmente compartilhados por seus testes. A interface pode ser escolhida pela configuração do runner.

## Exemplo
Uma suite `Carrinho` pode conter exemplos para item ausente e total atualizado, enquanto um `beforeEach` recria o carrinho para cada exemplo.

## Limites e trade-offs
A árvore é construída enquanto o arquivo de teste é carregado; não tente esperar uma chamada de rede dentro de `describe()` para descobrir os casos antes de registrá-los.

## Como verificar
Rode somente o arquivo e leia o relatório hierárquico: deve ficar claro qual comportamento falhou sem depender do nome da função de produção.

## Conexões
- [[mocha-hooks-nested-order]] — Veja também: Mocha: controlar ordem e escopo de hooks aninhados.

## Fontes
- [Mocha — Interfaces](https://mochajs.org/features/interfaces/) — BDD, TDD and other suite-definition interfaces; consultado em 2026-10-02.
- [Mocha — Hooks](https://mochajs.org/features/hooks/) — nested setup/teardown hooks and async hook behavior; consultado em 2026-10-02.
