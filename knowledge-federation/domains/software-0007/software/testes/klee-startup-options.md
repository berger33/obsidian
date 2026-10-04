---
id: software.testes.tranche25.001908
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

# Cinco opções de inicialização: entry-point, env-file, optimize, output-dir e run-in-dir

## Em uma frase
A seção Startup Options lista cinco flags que controlam como a execução começa: --entry-point=<function_name> inicia a execução a partir da função indicada em vez de main; --env-file=<file_name> inicializa o ambiente a partir de um arquivo no formato env; --optimize (padrão false) roda passes de otimização do compilador sobre o bitcode antes da execução; --output-dir=<dir_name> define o diretório de saída dos resultados (padrão klee-out-N); e --run-in-dir=<dir_name> muda para o diretório informado antes de iniciar a execução (padrão: local do arquivo testado).

## Por que importa
Dois recursos aqui mudam a prática diária: --entry-point permite verificar uma função de biblioteca diretamente sem escrever um arquivo main dedicado quando a assinatura é compatível, e --optimize simplifica o bitcode antes da interpretação simbólica, reduzindo o número de instruções e consultas ao solver.

## Como funciona
Use --optimize em alvos maiores para enxugar o bitcode antes da exploração, fixe --output-dir em scripts de CI que precisam de caminho previsível para os artefatos e use --entry-point=<função> ou --env-file quando quiser isolar o ponto de partida e as variáveis de ambiente.

## Exemplo
Em um job automatizado, passar --optimize --output-dir=/tmp/klee-result evita ter de descobrir qual diretório sequencial klee-out-0, klee-out-1 foi criado e acelera a interpretação do bitcode.

## Limites e trade-offs
Por padrão --optimize vem desligado (default=false) para preservar a correspondência mais direta com o bitcode de entrada durante depurações rápidas; lembre-se de ativá-lo explicitamente em campanhas mais longas.

## Como verificar
Conferi os cinco itens da seção Startup Options em klee-se.org/docs/options/.

## Conexões
- [[klee-external-call-policy]] — Veja também: Política de chamadas a funções externas: none, concrete (padrão) e all.
- [[klee-diagnostic-and-control-sections-map]] — Veja também: Mapa das demais seções de controle: Solver Chain, klee_assume, estatísticas, memória e saída por eventos.

## Fontes
- [KLEE — Overview of main command-line options](https://klee-se.org/docs/options/) — Documentação oficial das opções de linha de comando do KLEE: sintaxe, -fsanitize para integer overflow, ambiente simbólico, heurísticas de busca DFS/random-path/NURS, batching, --external-calls e startup.; consultado em 2026-10-03.
- [KLEE — README oficial](https://raw.githubusercontent.com/klee/klee/master/README.md) — README oficial do KLEE com descrição da máquina virtual simbólica sobre LLVM, camada de emulação POSIX/Linux com uClibc e infraestruturas de replay em código nativo.; consultado em 2026-10-03.
