---
id: software.testes.tranche26.001960
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

# ESBMC: model checker limitado por contexto baseado em SMT para oito famílias de linguagens

## Em uma frase
O README oficial define o ESBMC (Efficient SMT-based Context-Bounded Model Checker) como um model checker maduro, de código aberto e licença permissiva que detecta automaticamente — ou prova a ausência de — erros em tempo de execução em programas single-threaded e multi-threaded escritos em C, C++, CUDA, CHERI, Kotlin, Python, Rust e Solidity, implementando algoritmos de BMC incremental e prova por k-induction baseados em solvers SMT e CP.

## Por que importa
Combinar BMC incremental com k-induction sobre fórmulas SMT permite tanto achar contraexemplos rápidos em prefixos finitos de execução quanto provar propriedades indutivamente sem precisar de anotações manuais pesadas em cada laço.

## Como funciona
Submeta o arquivo-fonte na linguagem suportada ao binário esbmc escolhendo a estratégia de verificação (como --incremental-bmc ou --k-induction), a propriedade e o solver SMT desejado.

## Exemplo
No exemplo introdutório do README para C, o comando esbmc file.c --incremental-bmc analisa o programa e imprime o contraexemplo passo a passo por estado e linha quando encontra uma violação.

## Limites e trade-offs
Por simular um prefixo finito da execução do programa (context-bounded e loop-bounded quando sem indução completa), o escopo da prova depende da estratégia selecionada (BMC simples, incremental ou k-induction).

## Como verificar
Conferi os parágrafos de abertura e a seção How to use ESBMC no README oficial do repositório esbmc/esbmc.

## Conexões
- [[esbmc-five-language-frontends]] — Veja também: Os cinco frontends especializados: Clang, Soot/Jimple, CPython 3.10, Solidity e ESBMC-PLC.

## Fontes
- [ESBMC — README oficial](https://raw.githubusercontent.com/esbmc/esbmc/master/README.md) — README oficial do ESBMC com oito linguagens suportadas, cinco frontends (Clang, Soot/Jimple, CPython 3.10, Solidity e ESBMC-PLC), algoritmos incremental BMC e k-induction, erros detectados, sete solvers SMT mais --bitwuzllob e --neurosym, PPA/Homebrew, integrações e trace de contraexemplo.; consultado em 2026-10-03.
- [Repositório oficial esbmc/esbmc](https://github.com/esbmc/esbmc) — Repositório oficial do ESBMC no GitHub com código-fonte, ARCHITECTURE.md, src/python-frontend/README.md e releases.; consultado em 2026-10-03.
