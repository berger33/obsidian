---
id: software.testes.tranche26.001967
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

# As três integrações oficiais fora do terminal: VS Code, ESBMC-Web e plugin Claude Code (mais GitHub Action)

## Em uma frase
A seção Editor and tool integration destaca três frontends companheiros que rodam o ESBMC fora da linha de comando tradicional: (1) a extensão para Visual Studio Code (esbmc/vscode-esbmc), que verifica o arquivo em edição e reporta no terminal integrado; (2) a interface web auto-hospedada ESBMC-Web (esbmc/esbmc-web) para C, C++ e Python, com seletor de flags e painel interativo de violações e contraexemplos; e (3) o plugin para Claude Code (esbmc/agent-marketplace), que fornece os comandos /verify e /audit, uma verification skill, documentação de referência e exemplos — além da GitHub Action oficial (esbmc.github.io/docs/github-action) para rodar em CI.

## Por que importa
Levar o model checker para dentro do editor VS Code, para uma GUI web com flag picker e para agentes de codificação via /verify e /audit reduz a distância entre escrever código C/C++/Python e interpretar um contraexemplo formal.

## Como funciona
Instale a extensão vscode-esbmc para feedback imediato durante a edição, suba o ESBMC-Web para sessões visuais de exploração de flags e contraexemplos, use o plugin de agente com /verify e /audit em fluxos assistidos e configure a GitHub Action no pipeline do repositório.

## Exemplo
Em uma revisão automatizada de pull request, a GitHub Action oficial roda no CI enquanto o desenvolvedor reproduz o contraexemplo localmente pela extensão do VS Code ou pelo ESBMC-Web.

## Limites e trade-offs
Os detalhes de configuração de cada integração e dos inputs da Action estão nas páginas esbmc.github.io/docs/integrations e esbmc.github.io/docs/github-action linkadas na seção.

## Como verificar
Conferi a seção Editor and tool integration no README oficial do ESBMC.

## Conexões
- [[esbmc-installation-ppa-homebrew-releases]] — Veja também: Instalação oficial: PPA para Ubuntu 22.04/24.04, Homebrew com Z3/Bitwuzla e binários de release.
- [[esbmc-incremental-bmc-counterexample-trace]] — Veja também: Uso prático com --incremental-bmc e leitura do trace de contraexemplo por estados.

## Fontes
- [ESBMC — README oficial](https://raw.githubusercontent.com/esbmc/esbmc/master/README.md) — README oficial do ESBMC com oito linguagens suportadas, cinco frontends (Clang, Soot/Jimple, CPython 3.10, Solidity e ESBMC-PLC), algoritmos incremental BMC e k-induction, erros detectados, sete solvers SMT mais --bitwuzllob e --neurosym, PPA/Homebrew, integrações e trace de contraexemplo.; consultado em 2026-10-03.
- [ESBMC Documentation — Integrations e guias oficiais](https://esbmc.github.io/docs/integrations) — Documentação oficial do ESBMC sobre integrações (VS Code, ESBMC-Web, Claude Code plugin e GitHub Action) e guias de uso.; consultado em 2026-10-03.
