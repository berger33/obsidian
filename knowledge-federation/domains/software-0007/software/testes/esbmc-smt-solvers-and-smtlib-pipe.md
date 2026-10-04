---
id: software.testes.tranche26.001964
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

# Sete solvers SMT suportados nativamente e comunicação via pipe SMT-LIB

## Em uma frase
Na seção Features, o README lista os sete solvers SMT atualmente suportados pelo ESBMC: Z3 4.13+, Bitwuzla, Boolector 3.0+, MathSAT, CVC4, CVC5 e Yices 2.2+, acrescentando que o ESBMC também pode ser configurado para usar o formato de texto interativo SMTLIB através de um pipe para se comunicar com um processo de solver arbitrário (embora com sobrecarga não desprezível).

## Por que importa
Fórmulas geradas por programas com arrays, bit-vectors e ponto flutuante IEEE podem ser resolvidas muito mais rápido por um solver (como Bitwuzla ou Boolector) do que por outro (como Z3 ou CVC5); permitir trocar o solver na linha de comando evita ficar refém do desempenho de um único provador.

## Como funciona
Use os solvers embutidos na distribuição oficial (o pacote Homebrew, por exemplo, já instala o esbmc junto com Z3 e Bitwuzla embutidos) e troque o solver por flag quando uma prova demorar, reservando o pipe SMTLIB interativo para experimentar solvers externos novos.

## Exemplo
Ao instalar via brew install esbmc no macOS ou Linux, a documentação informa que Z3 e Bitwuzla já vêm empacotados e prontos para uso imediato.

## Limites e trade-offs
O próprio README avisa que a comunicação via pipe em formato texto interativo SMTLIB com um processo externo acarreta sobrecarga (overheads) relevante em comparação aos solvers integrados diretamente.

## Como verificar
Conferi a lista de solvers SMT e o parágrafo sobre SMTLIB pipe na seção Features do README oficial.

## Conexões
- [[esbmc-concurrent-pthread-verification]] — Veja também: Verificação de software concorrente (pthread): interleavings, deadlock, data races e atomicidade.
- [[esbmc-oneshot-backends-bitwuzllob-neurosym]] — Veja também: Backends one-shot externos sobre arquivos SMT-LIB2: --bitwuzllob (Mallob) e --neurosym.

## Fontes
- [ESBMC — README oficial](https://raw.githubusercontent.com/esbmc/esbmc/master/README.md) — README oficial do ESBMC com oito linguagens suportadas, cinco frontends (Clang, Soot/Jimple, CPython 3.10, Solidity e ESBMC-PLC), algoritmos incremental BMC e k-induction, erros detectados, sete solvers SMT mais --bitwuzllob e --neurosym, PPA/Homebrew, integrações e trace de contraexemplo.; consultado em 2026-10-03.
- [ESBMC Documentation — Integrations e guias oficiais](https://esbmc.github.io/docs/integrations) — Documentação oficial do ESBMC sobre integrações (VS Code, ESBMC-Web, Claude Code plugin e GitHub Action) e guias de uso.; consultado em 2026-10-03.
