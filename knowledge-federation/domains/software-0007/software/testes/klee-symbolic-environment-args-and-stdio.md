---
id: software.testes.tranche25.001903
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

# Ambiente simbólico: -sym-arg, -sym-args, -sym-stdin e -sym-stdout

## Em uma frase
Com -posix-runtime habilitado, a seção Symbolic Environment documenta as opções para tornar entradas de linha de comando e fluxos padrão simbólicos: -sym-arg <N> substitui por um argumento simbólico de comprimento N; -sym-args <MIN> <MAX> <N> substitui por no mínimo MIN e no máximo MAX argumentos, cada um com comprimento máximo N; -sym-stdin <N> torna a stdin simbólica com tamanho N; e -sym-stdout torna a stdout simbólica.

## Por que importa
Utilitários de sistema (como coreutils ou ferramentas de CLI) leem flags de argv e dados da entrada padrão; essas quatro opções permitem testar simbolicamente um binário com main(int argc, char **argv) sem modificar uma única linha do código-fonte C para chamar intrínsecos do KLEE.

## Como funciona
Passe -posix-runtime antes do arquivo .bc e adicione após o arquivo .bc uma combinação de -sym-arg, -sym-args e -sym-stdin dimensionada para o tamanho mínimo capaz de exercitar o parser de opções e de entrada do programa.

## Exemplo
Para testar um filtro que aceita de 1 a 3 flags curtas e lê até 16 bytes da entrada padrão, os argumentos da aplicação após program.bc podem usar -sym-args 1 3 4 -sym-stdin 16.

## Limites e trade-offs
Aumentar <MAX> ou <N> indiscriminadamente multiplica o espaço de estados de parsing de strings; comece com comprimentos pequenos (2 a 10 bytes) suficientes para cobrir as opções do utilitário.

## Como verificar
Conferi os itens 1, 2, 4 e 5 da seção Symbolic Environment em klee-se.org/docs/options/.

## Conexões
- [[klee-cli-order-and-integer-overflow-sanitize]] — Veja também: Ordem da linha de comando e detecção de integer overflow via clang -fsanitize.
- [[klee-symbolic-files-writes-and-failures]] — Veja também: Arquivos simbólicos e injeção de falhas de I/O: -sym-files, -save-all-writes, -max-fail e -fd-fail.

## Fontes
- [KLEE — Overview of main command-line options](https://klee-se.org/docs/options/) — Documentação oficial das opções de linha de comando do KLEE: sintaxe, -fsanitize para integer overflow, ambiente simbólico, heurísticas de busca DFS/random-path/NURS, batching, --external-calls e startup.; consultado em 2026-10-03.
- [KLEE — README oficial](https://raw.githubusercontent.com/klee/klee/master/README.md) — README oficial do KLEE com descrição da máquina virtual simbólica sobre LLVM, camada de emulação POSIX/Linux com uClibc e infraestruturas de replay em código nativo.; consultado em 2026-10-03.
