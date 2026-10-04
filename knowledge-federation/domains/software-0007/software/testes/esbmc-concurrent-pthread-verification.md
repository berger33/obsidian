---
id: software.testes.tranche26.001963
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-26.md"
fontes: ["https://raw.githubusercontent.com/esbmc/esbmc/master/README.md", "https://esbmc.github.io/docs/integrations"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Verificação de software concorrente (pthread): interleavings, deadlock, data races e atomicidade

## Em uma frase
O segundo bloco da seção Features explica que programas concorrentes que usam a API pthread são verificados explorando explicitamente os entrelaçamentos (interleavings), produzindo uma execução simbólica por interleaving: por padrão são checados pointer-safety, array-out-of-bounds, division-by-zero e asserções do usuário, podendo-se ativar opções adicionais para verificar deadlock (em mutexes e variáveis de condição pthread), data races (escritas concorrentes conflitantes), violações de atomicidade em atribuições visíveis e ordem de aquisição de locks.

## Por que importa
Bugs de concorrência em pthreads dependem de escalonamentos raríssimos que testes de estresse podem rodar milhões de vezes sem atingir; explorar sistematicamente os interleavings (por busca lazy em profundidade por padrão, ou codificando todos os interleavings numa única fórmula SMT) transforma a caça a deadlocks e data races num problema formal.

## Como funciona
Ao verificar código multi-threaded com pthread, adicione as opções de checagem de deadlock, data races, violação de atomicidade ou lock acquisition ordering conforme o risco do módulo, mantendo a busca lazy DFS padrão ou testando a codificação em fórmula SMT única.

## Exemplo
O README destaca especificamente que a verificação de deadlock aplica-se a mutexes e variáveis de condição pthread, enquanto data races detectam escritas concorrentes conflitantes.

## Limites e trade-offs
Explorar interleavings aumenta rapidamente o espaço de estados conforme o número de threads e trocas de contexto cresce; exatamente por isso o ESBMC é um verificador context-bounded.

## Como verificar
Conferi os parágrafos sobre software concorrente e pthread na seção Features do README oficial.

## Conexões
- [[esbmc-sequential-safety-properties]] — Veja também: Classes de erros sequenciais detectados automaticamente pelo ESBMC.
- [[esbmc-smt-solvers-and-smtlib-pipe]] — Veja também: Sete solvers SMT suportados nativamente e comunicação via pipe SMT-LIB.

## Fontes
- [ESBMC — README oficial](https://raw.githubusercontent.com/esbmc/esbmc/master/README.md) — README oficial do ESBMC com oito linguagens suportadas, cinco frontends (Clang, Soot/Jimple, CPython 3.10, Solidity e ESBMC-PLC), algoritmos incremental BMC e k-induction, erros detectados, sete solvers SMT mais --bitwuzllob e --neurosym, PPA/Homebrew, integrações e trace de contraexemplo.; consultado em 2026-10-03.
- [ESBMC Documentation — Integrations e guias oficiais](https://esbmc.github.io/docs/integrations) — Documentação oficial do ESBMC sobre integrações (VS Code, ESBMC-Web, Claude Code plugin e GitHub Action) e guias de uso.; consultado em 2026-10-03.
