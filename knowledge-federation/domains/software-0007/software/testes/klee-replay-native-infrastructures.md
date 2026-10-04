---
id: software.testes.tranche25.001901
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
fontes: ["https://raw.githubusercontent.com/klee/klee/master/README.md", "https://klee-se.org/docs/options/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Duas infraestruturas de replay em código nativo: biblioteca simples e ambiente POSIX

## Em uma frase
O segundo parágrafo do README oficial descreve os dois mecanismos de replay das entradas calculadas pelo KLEE diretamente sobre o binário nativo: uma biblioteca simples para reproduzir entradas computadas em código nativo (para programas fechados na memória) e uma infraestrutura mais completa para reproduzir entradas geradas para a camada de emulação POSIX/Linux, que executa o programa nativo em um ambiente correspondente ao caso de teste — configurando arquivos, pipes, variáveis de ambiente e argumentos de linha de comando.

## Por que importa
A execução simbólica ocorre dentro da VM do KLEE sobre bitcode, mas o desenvolvedor precisa confirmar e depurar o bug (com gdb, ASan ou gcov) no binário nativo real; o replay reconstrói exatamente os arquivos, pipes e argumentos que levaram àquele caminho simbólico.

## Como funciona
Após gerar os casos de teste no KLEE, use a biblioteca simples de replay quando o alvo só consome buffers em memória via API, ou a infraestrutura de replay POSIX quando o caso de teste envolve -sym-files, -sym-stdin, pipes e argumentos de linha de comando.

## Exemplo
Se o KLEE descobriu um crash que depende de dois argumentos e de um arquivo simbólico 'A' corrompido, o replay POSIX monta esse arquivo, passa os argumentos e roda o executável nativo fora da máquina virtual simbólica.

## Limites e trade-offs
Reproduzir fielmente no binário nativo exige que ele tenha sido compilado a partir do mesmo código-fonte e para o mesmo ambiente emulado durante a sessão simbólica.

## Como verificar
Conferi o parágrafo sobre replay no README oficial do repositório klee/klee.

## Conexões
- [[klee-what-it-is-and-two-components]] — Veja também: KLEE: máquina virtual simbólica sobre LLVM e seus dois componentes centrais.
- [[klee-cli-order-and-integer-overflow-sanitize]] — Veja também: Ordem da linha de comando e detecção de integer overflow via clang -fsanitize.

## Fontes
- [KLEE — README oficial](https://raw.githubusercontent.com/klee/klee/master/README.md) — README oficial do KLEE com descrição da máquina virtual simbólica sobre LLVM, camada de emulação POSIX/Linux com uClibc e infraestruturas de replay em código nativo.; consultado em 2026-10-03.
- [KLEE — Overview of main command-line options](https://klee-se.org/docs/options/) — Documentação oficial das opções de linha de comando do KLEE: sintaxe, -fsanitize para integer overflow, ambiente simbólico, heurísticas de busca DFS/random-path/NURS, batching, --external-calls e startup.; consultado em 2026-10-03.
