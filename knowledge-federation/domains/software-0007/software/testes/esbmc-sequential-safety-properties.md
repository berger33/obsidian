---
id: software.testes.tranche26.001962
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
fontes: ["https://raw.githubusercontent.com/esbmc/esbmc/master/README.md", "https://github.com/esbmc/esbmc"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Classes de erros sequenciais detectados automaticamente pelo ESBMC

## Em uma frase
Na seção Features, o README enumera os erros de implementação detectados ao simular um prefixo finito da execução com todas as entradas possíveis: falhas em asserções do usuário, acesso fora dos limites de array, dereferências ilegais de ponteiro (ponteiro nulo, fora de limites, double-free de memória alocada com malloc e acesso desalinhado), overflows de inteiros, comportamento indefinido em operações de shift, parâmetros de ponteiro qualificados com restrict que sofrem aliasing, ponto flutuante resultando em NaN, divisão por zero e vazamentos de memória (memory leaks).

## Por que importa
Muitos desses defeitos — como aliasing violando ponteiros restrict, shifts indefinidos, geração de NaN ou acesso desalinhado — passam despercebidos em testes convencionais em arquiteturas x86 tolerantes, mas causam bugs graves sob otimização agressiva do compilador ou em arquiteturas embarcadas.

## Como funciona
Execute o ESBMC sobre módulos críticos de manipulação de memória e aritmética para checar automaticamente toda essa bateria de propriedades predefinidas além das asserções explícitas do programa.

## Exemplo
No código de exemplo do README com malloc para os ponteiros a e b e incremento *b++ = 0 seguido de free(a); free(b);, o ESBMC aponta a violação de propriedade no estado exato da execução.

## Limites e trade-offs
Algumas verificações específicas (como memory leaks ou overflows particulares) podem ser habilitadas ou ajustadas por flags de propriedade; o README observa que o usuário pode escolher o solver SMT, a propriedade e a estratégia de verificação.

## Como verificar
Conferi a primeira lista de itens da seção Features no README oficial do ESBMC.

## Conexões
- [[esbmc-five-language-frontends]] — Veja também: Os cinco frontends especializados: Clang, Soot/Jimple, CPython 3.10, Solidity e ESBMC-PLC.
- [[esbmc-concurrent-pthread-verification]] — Veja também: Verificação de software concorrente (pthread): interleavings, deadlock, data races e atomicidade.

## Fontes
- [ESBMC — README oficial](https://raw.githubusercontent.com/esbmc/esbmc/master/README.md) — README oficial do ESBMC com oito linguagens suportadas, cinco frontends (Clang, Soot/Jimple, CPython 3.10, Solidity e ESBMC-PLC), algoritmos incremental BMC e k-induction, erros detectados, sete solvers SMT mais --bitwuzllob e --neurosym, PPA/Homebrew, integrações e trace de contraexemplo.; consultado em 2026-10-03.
- [Repositório oficial esbmc/esbmc](https://github.com/esbmc/esbmc) — Repositório oficial do ESBMC no GitHub com código-fonte, ARCHITECTURE.md, src/python-frontend/README.md e releases.; consultado em 2026-10-03.
