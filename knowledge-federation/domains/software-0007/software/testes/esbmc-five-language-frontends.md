---
id: software.testes.tranche26.001961
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

# Os cinco frontends especializados: Clang, Soot/Jimple, CPython 3.10, Solidity e ESBMC-PLC

## Em uma frase
O README detalha como o ESBMC analisa linguagens tão distintas por meio de cinco frontends: (1) o compilador Clang como frontend para C/C++/CHERI/CUDA; (2) o framework Soot via representação Jimple para Java/Kotlin; (3) o parser do CPython 3.10 como frontend Python — destacado como o primeiro bounded model checker baseado em SMT para programas Python; (4) regras de produção da gramática Solidity como frontend Solidity; e (5) o frontend ESBMC-PLC para verificar programas Ladder Diagram (IEC 61131-3) de controladores lógicos programáveis (PLCs), além de suportar aritmética de ponto flutuante IEEE em vários solvers SMT.

## Por que importa
Reaproveitar frontends industriais reais (Clang AST, Jimple do Soot, parser do CPython 3.10) preserva a semântica exata de cada linguagem antes de traduzir para a representação intermediária simbólica e para ponto flutuante IEEE.

## Como funciona
Ao verificar código Python, Kotlin, Solidity ou Ladder Diagram de PLC, consulte a documentação específica de cada frontend (como src/python-frontend/README.md ou esbmc.github.io/docs/ld/ linkados no README) para conhecer as construções suportadas.

## Exemplo
Um programa Python analisado pelo frontend baseado no parser do CPython 3.10 passa pelo mesmo motor SMT e gerador de contraexemplos usado para programas C no Clang.

## Limites e trade-offs
Cada frontend tem requisitos próprios de versão ou gramática (por exemplo, o parser CPython 3.10 no frontend Python); consulte a documentação de arquitetura (ARCHITECTURE.md) para detalhes de cobertura de bibliotecas de cada linguagem.

## Como verificar
Conferi a lista de seis itens de suporte de frontends e IEEE floating-point na abertura do README oficial.

## Conexões
- [[esbmc-what-it-is]] — Veja também: ESBMC: model checker limitado por contexto baseado em SMT para oito famílias de linguagens.
- [[esbmc-sequential-safety-properties]] — Veja também: Classes de erros sequenciais detectados automaticamente pelo ESBMC.

## Fontes
- [ESBMC — README oficial](https://raw.githubusercontent.com/esbmc/esbmc/master/README.md) — README oficial do ESBMC com oito linguagens suportadas, cinco frontends (Clang, Soot/Jimple, CPython 3.10, Solidity e ESBMC-PLC), algoritmos incremental BMC e k-induction, erros detectados, sete solvers SMT mais --bitwuzllob e --neurosym, PPA/Homebrew, integrações e trace de contraexemplo.; consultado em 2026-10-03.
- [ESBMC Documentation — Integrations e guias oficiais](https://esbmc.github.io/docs/integrations) — Documentação oficial do ESBMC sobre integrações (VS Code, ESBMC-Web, Claude Code plugin e GitHub Action) e guias de uso.; consultado em 2026-10-03.
