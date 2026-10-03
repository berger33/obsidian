---
id: software.testes.tranche25.001902
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

# Ordem da linha de comando e detecção de integer overflow via clang -fsanitize

## Em uma frase
A seção KLEE usage da documentação oficial define a forma geral klee [klee-options] <program.bc> [program-options] — primeiro as opções do próprio KLEE, depois o arquivo de bitcode LLVM program.bc e por fim os argumentos passados à aplicação — e destaca que, para habilitar a detecção de overflow de inteiros, program.bc precisa ter sido compilado pelo clang com -fsanitize=signed-integer-overflow (para inteiros com sinal) e -fsanitize=unsigned-integer-overflow (para inteiros sem sinal).

## Por que importa
No bitcode LLVM padrão, operações aritméticas inteiras não geram armadilhas explícitas de overflow por conta própria; usar as flags -fsanitize do clang injeta as checagens de estouro no bitcode que o KLEE então passa a tratar como alvos de verificação simbólica.

## Como funciona
Ao compilar o código C para bitcode com clang, adicione -fsanitize=signed-integer-overflow e -fsanitize=unsigned-integer-overflow se quiser que o KLEE gere casos de teste para estouros aritméticos, e passe sempre as flags do KLEE antes do nome do arquivo .bc.

## Exemplo
Inverter a ordem na linha de comando — colocando uma flag do KLEE depois de program.bc — faz com que ela seja entregue como argumento da aplicação em vez de configurar o verificador.

## Limites e trade-offs
Na seção KLEE Output logo abaixo, a documentação também informa que avisos saem por padrão na tela e em klee-last/warnings.txt, podendo ser restritos apenas ao arquivo com a flag --warnings-only-to-file.

## Como verificar
Conferi as seções KLEE usage e KLEE Output em klee-se.org/docs/options/.

## Conexões
- [[klee-replay-native-infrastructures]] — Veja também: Duas infraestruturas de replay em código nativo: biblioteca simples e ambiente POSIX.
- [[klee-symbolic-environment-args-and-stdio]] — Veja também: Ambiente simbólico: -sym-arg, -sym-args, -sym-stdin e -sym-stdout.

## Fontes
- [KLEE — Overview of main command-line options](https://klee-se.org/docs/options/) — Documentação oficial das opções de linha de comando do KLEE: sintaxe, -fsanitize para integer overflow, ambiente simbólico, heurísticas de busca DFS/random-path/NURS, batching, --external-calls e startup.; consultado em 2026-10-03.
- [KLEE — README oficial](https://raw.githubusercontent.com/klee/klee/master/README.md) — README oficial do KLEE com descrição da máquina virtual simbólica sobre LLVM, camada de emulação POSIX/Linux com uClibc e infraestruturas de replay em código nativo.; consultado em 2026-10-03.
