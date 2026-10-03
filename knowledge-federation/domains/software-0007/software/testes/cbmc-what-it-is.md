---
id: software.testes.tranche25.001890
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
fontes: ["https://raw.githubusercontent.com/diffblue/cbmc/develop/README.md", "https://github.com/diffblue/cbmc"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# CBMC: Bounded Model Checker para programas C e C++

## Em uma frase
A seção About do README oficial define o CBMC como um Bounded Model Checker para programas C e C++, integrante do ecossistema CProver (com documentação em diffblue.github.io/cbmc/ e cprover.org/cbmc e visão geral das ferramentas em TOOLS_OVERVIEW.md).

## Por que importa
Em código de sistemas escrito em C e C++, testes convencionais amostram apenas uma fração minúscula das entradas possíveis; um model checker limitado explora simbolicamente todas as entradas dentro de um limite de execução para provar ausência de falhas ou exibir um contraexemplo exato.

## Como funciona
O verificador recebe o programa C/C++ e analisa todas as execuções até a profundidade configurada, reportando se as propriedades de segurança e as asserções do usuário se mantêm válidas.

## Exemplo
Para conhecer o papel do CBMC ao lado dos demais utilitários da suíte CProver, o README aponta diretamente para o arquivo TOOLS_OVERVIEW.md do repositório.

## Limites e trade-offs
A garantia de um bounded model checker é relativa ao limite de desenrolamento configurado e ao modelo de ambiente; caminhos que exigiriam mais iterações do que o limite precisam de configuração adequada de unwinding.

## Como verificar
Conferi a seção About e os links do cabeçalho no README oficial do repositório diffblue/cbmc.

## Conexões
- [[cbmc-language-standards-and-extensions]] — Veja também: Cobertura de padrões C89 a C23, extensões de compilador, SystemC e Verilog.

## Fontes
- [CBMC — README oficial](https://raw.githubusercontent.com/diffblue/cbmc/develop/README.md) — README oficial do CBMC com suporte a C89–C23, extensões gcc/Visual Studio, SystemC/Scoot, Verilog, loop unwinding, canais release vs develop, instalação em Windows/Linux/macOS, contribuição e licença 4-clause BSD.; consultado em 2026-10-03.
- [Repositório oficial diffblue/cbmc](https://github.com/diffblue/cbmc) — Repositório oficial do CBMC e da suíte CProver no GitHub com releases, TOOLS_OVERVIEW.md, COMPILING.md, CODING_STANDARD.md e FEATURE_IDEAS.md.; consultado em 2026-10-03.
