---
id: software.testes.tranche25.001897
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

# Fluxo de contribuição: branch a partir de develop e CODING_STANDARD.md

## Em uma frase
A seção Contributing to the code base define os seis passos para contribuir com o CBMC: (1) fazer fork do repositório, (2) clonar com git clone, (3) criar uma branch a partir da branch develop (que é a branch padrão), (4) fazer as alterações seguindo as diretrizes em CODING_STANDARD.md, (5) fazer push para a sua branch e (6) abrir o Pull Request apontando para a branch develop — além de indicar a página FEATURE_IDEAS.md com ideias de mini-projetos focados para novos contribuidores.

## Por que importa
Documentar que a branch alvo e base é a develop (e que existe um CODING_STANDARD.md explícito e uma lista de mini-projetos em FEATURE_IDEAS.md) evita PRs abertos contra a branch errada ou rejeitados no review por estilo de código.

## Como funciona
Antes de escrever um patch para o CBMC, crie a sua branch de trabalho a partir de develop, consulte CODING_STANDARD.md e, se estiver procurando por onde começar, escolha um escopo pequeno listado em FEATURE_IDEAS.md.

## Exemplo
Um novo contribuidor clona seu fork, faz checkout de uma branch baseada em develop, implementa uma ideia de FEATURE_IDEAS.md respeitando o CODING_STANDARD.md e abre o PR contra develop.

## Limites e trade-offs
Para quem apenas encontrou um defeito no uso da ferramenta e não vai enviar código, a seção Report bugs logo acima pede simplesmente abrir uma issue em github.com/diffblue/cbmc/issues.

## Como verificar
Conferi as seções Report bugs e Contributing to the code base no README oficial.

## Conexões
- [[cbmc-macos-homebrew-pin-and-tap]] — Veja também: Instalação no macOS com Homebrew: upgrade automático, brew pin e tap histórico.
- [[cbmc-compilers-and-build-from-source]] — Veja também: Compilação a partir do código-fonte via COMPILING.md e qualidade monitorada.

## Fontes
- [CBMC — README oficial](https://raw.githubusercontent.com/diffblue/cbmc/develop/README.md) — README oficial do CBMC com suporte a C89–C23, extensões gcc/Visual Studio, SystemC/Scoot, Verilog, loop unwinding, canais release vs develop, instalação em Windows/Linux/macOS, contribuição e licença 4-clause BSD.; consultado em 2026-10-03.
- [Repositório oficial diffblue/cbmc](https://github.com/diffblue/cbmc) — Repositório oficial do CBMC e da suíte CProver no GitHub com releases, TOOLS_OVERVIEW.md, COMPILING.md, CODING_STANDARD.md e FEATURE_IDEAS.md.; consultado em 2026-10-03.
