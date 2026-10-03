---
id: software.testes.tranche26.001966
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

# Instalação oficial: PPA para Ubuntu 22.04/24.04, Homebrew com Z3/Bitwuzla e binários de release

## Em uma frase
A seção Installing ESBMC apresenta três caminhos prontos: (1) no Ubuntu (22.04 Jammy e 24.04 Noble), o PPA oficial ppa:esbmc/esbmc instalado com sudo add-apt-repository ppa:esbmc/esbmc, sudo apt update e sudo apt install esbmc; (2) no macOS e Linux via Homebrew, com brew install esbmc (que já instala o esbmc junto dos solvers Z3 e Bitwuzla empacotados); e (3) download direto dos binários mais recentes para Ubuntu e Windows na página de GitHub Releases.

## Por que importa
Fornecer PPA oficial para as LTS do Ubuntu e fórmula Homebrew com solvers já embutidos elimina a barreira histórica de compilar LLVM/Clang e múltiplos solvers SMT manualmente antes de rodar o primeiro comando de verificação.

## Como funciona
No Ubuntu 22.04 ou 24.04 prefira o PPA ppa:esbmc/esbmc; no macOS (ou Linux com Brew) rode brew install esbmc; no Windows baixe o artefato da página de releases; e, ao rodar uma versão de release contra programas C no Linux, garanta que o cabeçalho math.h (incluído em build-essential) esteja instalado no sistema.

## Exemplo
Na seção How to use ESBMC, o README lembra especificamente que você precisa ter math.h instalado no sistema ao rodar uma versão de release, recomendando o pacote build-essential.

## Limites e trade-offs
Para quem precisa compilar o verificador a partir do código-fonte com opções customizadas de CMake, a seção Building ESBMC remete ao guia esbmc.github.io/docs/development/building.

## Como verificar
Conferi as seções Installing ESBMC, Building ESBMC e a nota sobre math.h em How to use ESBMC no README oficial.

## Conexões
- [[esbmc-oneshot-backends-bitwuzllob-neurosym]] — Veja também: Backends one-shot externos sobre arquivos SMT-LIB2: --bitwuzllob (Mallob) e --neurosym.
- [[esbmc-editor-web-and-claude-code-integrations]] — Veja também: As três integrações oficiais fora do terminal: VS Code, ESBMC-Web e plugin Claude Code (mais GitHub Action).

## Fontes
- [ESBMC — README oficial](https://raw.githubusercontent.com/esbmc/esbmc/master/README.md) — README oficial do ESBMC com oito linguagens suportadas, cinco frontends (Clang, Soot/Jimple, CPython 3.10, Solidity e ESBMC-PLC), algoritmos incremental BMC e k-induction, erros detectados, sete solvers SMT mais --bitwuzllob e --neurosym, PPA/Homebrew, integrações e trace de contraexemplo.; consultado em 2026-10-03.
- [ESBMC Documentation — Integrations e guias oficiais](https://esbmc.github.io/docs/integrations) — Documentação oficial do ESBMC sobre integrações (VS Code, ESBMC-Web, Claude Code plugin e GitHub Action) e guias de uso.; consultado em 2026-10-03.
