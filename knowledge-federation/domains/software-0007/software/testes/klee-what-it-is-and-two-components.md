---
id: software.testes.tranche25.001900
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

# KLEE: máquina virtual simbólica sobre LLVM e seus dois componentes centrais

## Em uma frase
O README oficial define o KLEE como uma máquina virtual simbólica construída sobre a infraestrutura de compiladores LLVM, composta atualmente por dois componentes primários: (1) o motor central da máquina virtual simbólica (código em lib/), responsável por executar módulos de bitcode LLVM com suporte a valores simbólicos, e (2) uma camada de emulação POSIX/Linux orientada ao suporte a uClibc, com suporte adicional para tornar partes do ambiente do sistema operacional simbólicas.

## Por que importa
Executar bitcode LLVM simbolicamente permite explorar múltiplos caminhos de execução de um programa C/C++ sem ficar preso a entradas fixas, enquanto a camada POSIX/uClibc impede que a execução simbólica pare na primeira chamada de sistema para ler arquivo ou argumento de linha de comando.

## Como funciona
Compile o programa alvo para bitcode LLVM (.bc) e execute-o no motor do KLEE, habilitando o runtime POSIX quando o programa interagir com arquivos, stdin, stdout ou argumentos de linha de comando.

## Exemplo
O comando geral documentado em klee-se.org/docs/options/ segue a ordem klee [klee-options] <program.bc> [program-options], onde a opção -posix-runtime habilita as opções de ambiente simbólico passadas ao programa.

## Limites e trade-offs
Como o KLEE interpreta módulos de bitcode LLVM, o código sob análise precisa ser compilado para bitcode; chamadas a bibliotecas nativas não compiladas para bitcode caem na política de chamadas externas.

## Como verificar
Conferi o README oficial no repositório klee/klee e a seção KLEE usage em klee-se.org/docs/options/.

## Conexões
- [[klee-replay-native-infrastructures]] — Veja também: Duas infraestruturas de replay em código nativo: biblioteca simples e ambiente POSIX.

## Fontes
- [KLEE — README oficial](https://raw.githubusercontent.com/klee/klee/master/README.md) — README oficial do KLEE com descrição da máquina virtual simbólica sobre LLVM, camada de emulação POSIX/Linux com uClibc e infraestruturas de replay em código nativo.; consultado em 2026-10-03.
- [KLEE — Overview of main command-line options](https://klee-se.org/docs/options/) — Documentação oficial das opções de linha de comando do KLEE: sintaxe, -fsanitize para integer overflow, ambiente simbólico, heurísticas de busca DFS/random-path/NURS, batching, --external-calls e startup.; consultado em 2026-10-03.
