---
id: software.testes.tranche25.001905
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

# As quatro heurísticas principais de busca e as seis variantes de NURS

## Em uma frase
A seção Search Heuristics explica que o KLEE oferece quatro famílias principais de busca selecionáveis via --search: (1) Depth-First Search (dfs), (2) Random State Search (random-state), (3) Random Path Selection (random-path, descrita no artigo do KLEE no OSDI'08) e (4) Non Uniform Random Search (NURS), que escolhe um estado aleatoriamente segundo uma distribuição ponderada — com seis variantes listadas no klee --help: nurs:covnew (Coverage-New), nurs:md2u (Min-Dist-to-Uncovered), nurs:depth (2^depth), nurs:icnt (Instr-Count), nurs:cpicnt (CallPath-Instr-Count) e nurs:qc (Query-Cost).

## Por que importa
Em programas com laços profundos, a busca em profundidade pura (dfs) pode ficar presa desenrolando um único caminho indefinidamente; já random-path e NURS (como md2u ou covnew) priorizam ramos rasos ou estados próximos a instruções ainda não cobertas.

## Como funciona
Escolha a heurística com --search=<opção> (por exemplo, klee --search=dfs demo.o ou klee --search=random-path demo.o) de acordo com o objetivo: alcançar rapidamente código novo (nurs:covnew, nurs:md2u) ou explorar exaustivamente uma subárvore pequena (dfs).

## Exemplo
Se uma campanha estacionar na cobertura por causa de um laço profundo ou consultas caras ao solver, trocar para --search=nurs:md2u ou --search=nurs:qc muda a distribuição de seleção de estados sem alterar o bitcode.

## Limites e trade-offs
Nenhuma heurística única domina todos os programas; exatamente por isso o próprio KLEE combina duas heurísticas por padrão em vez de usar apenas uma.

## Como verificar
Conferi a subseção Main search heuristics e a saída de klee --help em klee-se.org/docs/options/.

## Conexões
- [[klee-symbolic-files-writes-and-failures]] — Veja também: Arquivos simbólicos e injeção de falhas de I/O: -sym-files, -save-all-writes, -max-fail e -fd-fail.
- [[klee-default-interleaving-and-batching-search]] — Veja também: Heurística padrão interleaved (random-path + nurs:covnew) e busca em lote (-use-batching-search).

## Fontes
- [KLEE — Overview of main command-line options](https://klee-se.org/docs/options/) — Documentação oficial das opções de linha de comando do KLEE: sintaxe, -fsanitize para integer overflow, ambiente simbólico, heurísticas de busca DFS/random-path/NURS, batching, --external-calls e startup.; consultado em 2026-10-03.
- [KLEE — README oficial](https://raw.githubusercontent.com/klee/klee/master/README.md) — README oficial do KLEE com descrição da máquina virtual simbólica sobre LLVM, camada de emulação POSIX/Linux com uClibc e infraestruturas de replay em código nativo.; consultado em 2026-10-03.
