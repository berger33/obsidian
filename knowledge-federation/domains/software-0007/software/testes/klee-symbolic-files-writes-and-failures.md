---
id: software.testes.tranche25.001904
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

# Arquivos simbólicos e injeção de falhas de I/O: -sym-files, -save-all-writes, -max-fail e -fd-fail

## Em uma frase
Os itens 3, 6, 7 e 8 de Symbolic Environment cobrem o sistema de arquivos simbólico e falhas de sistema: -sym-files <NUM> <N> cria NUM arquivos simbólicos nomeados 'A', 'B', 'C', etc., cada um com tamanho N (excluindo stdin); -save-all-writes (ligado por padrão) permite que escritas executem normalmente mesmo quando excedem o tamanho inicial do arquivo; -max-fail <N> permite até N falhas injetadas; e -fd-fail é um atalho para -max-fail 1.

## Por que importa
Tratamento de erro de I/O (disco cheio, falha de descritor, leitura truncada) é um dos trechos menos testados em programas C; combinar arquivos simbólicos 'A', 'B' com -max-fail ou -fd-fail força o KLEE a explorar os ramos de erro de chamadas de sistema além do conteúdo do arquivo.

## Como funciona
Ao testar um programa que abre arquivos passados na linha de comando, crie os arquivos simbólicos com -sym-files 1 32, passe o nome 'A' ao programa e adicione -fd-fail (ou -max-fail N) para verificar se falhas de I/O causam vazamentos ou dereferências inválidas.

## Exemplo
A documentação destaca uma sutileza importante sobre -save-all-writes: quando desligado (off), todas as escritas que excedem o tamanho inicial do arquivo são descartadas, mas o file offset é sempre incrementado.

## Limites e trade-offs
Os arquivos criados por -sym-files seguem a convenção fixa de nomes 'A', 'B', 'C' em ordem alfabética; o programa sob teste precisa receber esses nomes nos argumentos (ou via argumento simbólico) para abri-los.

## Como verificar
Conferi os itens 3, 6, 7 e 8 da seção Symbolic Environment em klee-se.org/docs/options/.

## Conexões
- [[klee-symbolic-environment-args-and-stdio]] — Veja também: Ambiente simbólico: -sym-arg, -sym-args, -sym-stdin e -sym-stdout.
- [[klee-four-main-search-heuristics]] — Veja também: As quatro heurísticas principais de busca e as seis variantes de NURS.

## Fontes
- [KLEE — Overview of main command-line options](https://klee-se.org/docs/options/) — Documentação oficial das opções de linha de comando do KLEE: sintaxe, -fsanitize para integer overflow, ambiente simbólico, heurísticas de busca DFS/random-path/NURS, batching, --external-calls e startup.; consultado em 2026-10-03.
- [KLEE — README oficial](https://raw.githubusercontent.com/klee/klee/master/README.md) — README oficial do KLEE com descrição da máquina virtual simbólica sobre LLVM, camada de emulação POSIX/Linux com uClibc e infraestruturas de replay em código nativo.; consultado em 2026-10-03.
