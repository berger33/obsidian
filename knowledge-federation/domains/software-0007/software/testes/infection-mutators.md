---
id: software.testes.tranche23.001748
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
fontes: ["https://infection.github.io/guide/mutators.html", "https://infection.github.io/guide/command-line-options.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Mutators: famílias AST, o describe e o --id para matar um de cada vez

## Em uma frase
A página Mutators oficial documenta que os mutadores do Infection são baseados em AST sobre o projeto PHP-Parser de nikic, organizados em famílias com tabelas Original/Mutated: a seção Function Signature cobre PublicVisibility (público vira protected) e ProtectedVisibility (protected vira private) com a tese de encapsulamento (visibilidade redutível é API pública maior que o necessário); a família Unwrap* desfaz centenas de funções de array e string (UnwrapArrayChunk passa a lista sem o chunk); Binary Arithmetic troca operadores (+ vira -, % vira *, &= vira =); e a Round Family troca round, floor e ceil entre si "to make sure there's enough tests to cover the rounding possibilities".

## Por que importa
A consulta offline da doc oficial é o comando infection describe — "get information about mutators, right from the command line" — fechando o loop de descoberta sem abrir a doc, e a execução seletiva de famílias é feita pelo nome de cada tabela (referenciado pela nota da página para a opção --mutators).

## Como funciona
A doc ainda resolve o problema de iteração individual: --id (desde 0.30.0) roda um único mutante pelo seu hash — o guia mostra o ciclo real: rodar --git-diff-lines, copiar o ID do diff de um escape (11) src/SourceClass.php:9 [M] Minus, hash incluso), ajustar o teste, e rerodar a mesma linha de comando com --id=... até o kill; o alerta da página é que mudar o código pode invalidar o ID, então passe todas as outras opções iguais.

## Exemplo
Rode infection describe Minus e depois infection --id=<hash> do seu escape mais barato: o primeiro ensina o mutator, o segundo é o TDD de matar mutante com contexto mínimo.

## Limites e trade-offs
A tabela de famílias na página é ilustrativa e longa (a página inteira é a referência); --id não substitui a suíte completa — a página o posiciona para "focus on just 1 mutant at a time" durante o desenvolvimento, não para o gate de merge.

## Como verificar
Abra a página Mutators oficial e a seção --id da Command line options; confirme a base PHP-Parser, as famílias citadas e o exemplo completo de ciclo com hash.

## Conexões
- [[infection-loggers]] — Veja também: Loggers nativos de PR: GitHub annotations, GitLab code quality, HTML e JSON.
- [[infection-test-framework]] — Veja também: --test-framework: o adaptador que escolhe como o Infection roda seus testes.

## Fontes
- [Infection — Mutators](https://infection.github.io/guide/mutators.html) — famílias de mutadores AST e o comando describe; consultado em 2026-10-03.
- [Infection — Command line options](https://infection.github.io/guide/command-line-options.html) — threads, test-framework, coverage, git-diff e loggers; consultado em 2026-10-03.
