---
id: software.testes.tranche26.001965
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

# Backends one-shot externos sobre arquivos SMT-LIB2: --bitwuzllob (Mallob) e --neurosym

## Em uma frase
O README documenta dois backends adicionais (compilados por padrão via -DENABLE_BITWUZLLOB=On e -DENABLE_NEUROSYM=On) que acionam processos externos one-shot sobre arquivos SMT-LIB2: --bitwuzllob executa o Bitwuzla sobre a plataforma massivamente paralela Mallob (--bitwuzllob-prog, padrão mallob -mono=%f -mono-app=SMT), e --neurosym executa o NeuroSym, um solver SMT guiado por rede neural onde uma GAN propõe modelos candidatos com fallback para o Z3 preservando corretude e completude no fragmento QF_BV (--neurosym-prog, padrão python main.py %f).

## Por que importa
Esses dois modos conectam o ESBMC a duas fronteiras de pesquisa em resolução SMT — paralelismo massivo via Mallob e busca guiada por aprendizado de máquina com fallback formal no Z3 — sem exigir que os programas externos estejam presentes na hora de compilar o ESBMC (apenas em tempo de execução).

## Como funciona
Use --bitwuzllob ou --neurosym apenas em verificações one-shot; como ambos rejeitam estratégias incrementais (--k-induction, --incremental-bmc), passe um solver local interativo de modelo (--bitwuzllob-model-prog ou --neurosym-model-prog, como "z3 -in") para reconstruir contraexemplos, ou adicione --result-only.

## Exemplo
Para o --neurosym, o README detalha que o ESBMC achata arrays, structs e ponto flutuante em bit-vectors puros (QF_BV), não suportando o modo inteiro/real (--ir).

## Limites e trade-offs
Se você tentar combinar --bitwuzllob ou --neurosym com --incremental-bmc ou --k-induction, a execução é rejeitada porque ambos operam estritamente como backends one-shot sobre arquivos SMT-LIB2.

## Como verificar
Conferi o bloco sobre --bitwuzllob e --neurosym no final da seção Features do README oficial.

## Conexões
- [[esbmc-smt-solvers-and-smtlib-pipe]] — Veja também: Sete solvers SMT suportados nativamente e comunicação via pipe SMT-LIB.
- [[esbmc-installation-ppa-homebrew-releases]] — Veja também: Instalação oficial: PPA para Ubuntu 22.04/24.04, Homebrew com Z3/Bitwuzla e binários de release.

## Fontes
- [ESBMC — README oficial](https://raw.githubusercontent.com/esbmc/esbmc/master/README.md) — README oficial do ESBMC com oito linguagens suportadas, cinco frontends (Clang, Soot/Jimple, CPython 3.10, Solidity e ESBMC-PLC), algoritmos incremental BMC e k-induction, erros detectados, sete solvers SMT mais --bitwuzllob e --neurosym, PPA/Homebrew, integrações e trace de contraexemplo.; consultado em 2026-10-03.
- [Repositório oficial esbmc/esbmc](https://github.com/esbmc/esbmc) — Repositório oficial do ESBMC no GitHub com código-fonte, ARCHITECTURE.md, src/python-frontend/README.md e releases.; consultado em 2026-10-03.
