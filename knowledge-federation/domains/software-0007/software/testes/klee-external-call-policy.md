---
id: software.testes.tranche25.001907
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
fontes: ["https://klee-se.org/docs/options/", "https://raw.githubusercontent.com/klee/klee/master/README.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Política de chamadas a funções externas: none, concrete (padrão) e all

## Em uma frase
A seção External Call Policy detalha como o KLEE lida com funções fora do bitcode por meio de --external-calls: (1) none não permite chamadas externas (com a exceção explícita de que o KLEE sempre permite algumas chamadas com argumentos concretos, em particular printf e puts); (2) concrete (o padrão) permite apenas chamadas externas cujos argumentos sejam concretos; e (3) all permite todas as chamadas externas, concretizando quaisquer argumentos simbólicos passados a elas — além de controlar os avisos com --external-call-warnings (none, once-per-function ou all).

## Por que importa
Quando uma função externa nativa recebe um valor simbólico sob --external-calls=all, o KLEE precisa escolher um único valor concreto para realizar a chamada real na máquina hospedeira, perdendo a generalidade simbólica naquele argumento e podendo causar efeitos colaterais no sistema real.

## Como funciona
Mantenha o padrão --external-calls=concrete sempre que possível para ser avisado se dados simbólicos vazarem para fora do bitcode; se precisar usar --external-calls=all para destravar uma biblioteca externa, combine com --external-call-warnings=once-per-function para mapear quais funções estão concretizando estados.

## Exemplo
Mesmo sob --external-calls=none, chamadas de diagnóstico como printf e puts com argumentos concretos continuam passando sem abortar a execução simbólica.

## Limites e trade-offs
Concretizar argumentos simbólicos em --external-calls=all significa que ramos internos da função externa dependentes de outros valores possíveis daquele argumento não serão explorados pelo KLEE.

## Como verificar
Conferi a seção External Call Policy em klee-se.org/docs/options/.

## Conexões
- [[klee-default-interleaving-and-batching-search]] — Veja também: Heurística padrão interleaved (random-path + nurs:covnew) e busca em lote (-use-batching-search).
- [[klee-startup-options]] — Veja também: Cinco opções de inicialização: entry-point, env-file, optimize, output-dir e run-in-dir.

## Fontes
- [KLEE — Overview of main command-line options](https://klee-se.org/docs/options/) — Documentação oficial das opções de linha de comando do KLEE: sintaxe, -fsanitize para integer overflow, ambiente simbólico, heurísticas de busca DFS/random-path/NURS, batching, --external-calls e startup.; consultado em 2026-10-03.
- [KLEE — README oficial](https://raw.githubusercontent.com/klee/klee/master/README.md) — README oficial do KLEE com descrição da máquina virtual simbólica sobre LLVM, camada de emulação POSIX/Linux com uClibc e infraestruturas de replay em código nativo.; consultado em 2026-10-03.
