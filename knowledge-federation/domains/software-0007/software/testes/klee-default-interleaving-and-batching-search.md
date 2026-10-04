---
id: software.testes.tranche25.001906
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

# Heurística padrão interleaved (random-path + nurs:covnew) e busca em lote (-use-batching-search)

## Em uma frase
As subseções Interleaving, Batching e Default search heuristics documentam que várias heurísticas podem ser intercaladas em round-robin passando --search múltiplas vezes ( sendo o padrão do KLEE --search=random-path intercalado com --search=nurs:covnew), e que, como o loop principal seleciona um novo estado a cada instrução executada, a flag -use-batching-search permite executar um lote de instruções antes de trocar de estado, configurado por número de instruções (-batch-instructions=1000) ou por tempo (-batch-time=5s).

## Por que importa
Selecionar um novo estado a cada instrução única tem custo perceptível quando a árvore de estados cresce; o batching amortiza esse custo mantendo o estado atual por 1000 instruções ou 5 segundos, enquanto o interleaving evita que os pontos cegos de uma única heurística congelem a exploração.

## Como funciona
Mantenha o padrão intercalado (random-path com nurs:covnew) como linha de base, ou combine explicitamente várias flags --search (como klee --search=random-state --search=nurs:md2u demo.o), ativando -use-batching-search com -batch-instructions=1000 ou -batch-time=5s quando a sobrecarga de escalonamento de estados for alta.

## Exemplo
O comando klee --search=random-state --search=nurs:md2u demo.o alterna em round-robin entre sorteio uniforme de estado e distância mínima até instrução descoberta.

## Limites e trade-offs
Um lote muito longo em -batch-time pode reduzir a reatividade do interleaving se o estado atual entrar num trecho pesado; ajuste o tamanho do lote conforme o perfil do programa.

## Como verificar
Conferi as subseções Interleaving, Batching e Default search heuristics em klee-se.org/docs/options/.

## Conexões
- [[klee-four-main-search-heuristics]] — Veja também: As quatro heurísticas principais de busca e as seis variantes de NURS.
- [[klee-external-call-policy]] — Veja também: Política de chamadas a funções externas: none, concrete (padrão) e all.

## Fontes
- [KLEE — Overview of main command-line options](https://klee-se.org/docs/options/) — Documentação oficial das opções de linha de comando do KLEE: sintaxe, -fsanitize para integer overflow, ambiente simbólico, heurísticas de busca DFS/random-path/NURS, batching, --external-calls e startup.; consultado em 2026-10-03.
- [KLEE — README oficial](https://raw.githubusercontent.com/klee/klee/master/README.md) — README oficial do KLEE com descrição da máquina virtual simbólica sobre LLVM, camada de emulação POSIX/Linux com uClibc e infraestruturas de replay em código nativo.; consultado em 2026-10-03.
