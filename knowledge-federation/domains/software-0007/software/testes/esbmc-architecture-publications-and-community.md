---
id: software.testes.tranche26.001969
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

# Documentação de arquitetura, publicações científicas da SSVLab e comunidade no Zulip

## Em uma frase
O README aponta as fontes oficiais para aprofundar na teoria e na engenharia do verificador: a página de publicações e materiais de base em ssvlab.github.io/esbmc/publications.html, o documento de arquitetura interna em ARCHITECTURE.md no repositório, o site principal esbmc.org e o chat comunitário no Zulip (systemsandsoftwaresecurity.zulipchat.com, linkado no badge do topo), junto das métricas públicas do Codacy, Codecov e downloads de releases.

## Por que importa
Como o ESBMC implementa algoritmos formais específicos (como BMC incremental, k-induction e codificação SMT de ponto flutuante e concorrência), ter a lista de artigos científicos da SSVLab e o ARCHITECTURE.md permite auditar exatamente quais garantias teóricas cada flag implementa.

## Como funciona
Consulte ARCHITECTURE.md ao investigar como um frontend traduz o programa para a representação intermediária GOTO/SMT, leia as publicações em ssvlab.github.io/esbmc/publications.html para fundamentação acadêmica e use o Zulip oficial para dúvidas técnicas com os mantenedores.

## Exemplo
Um pesquisador ou engenheiro de segurança que precisa citar ou entender a prova por k-induction no ESBMC encontra os artigos correspondentes catalogados em ssvlab.github.io/esbmc/publications.html.

## Limites e trade-offs
Esta nota consolida os canais de referência, arquitetura e comunidade declarados na abertura do README oficial.

## Como verificar
Conferi os parágrafos introdutórios e a fileira de badges no README oficial do repositório esbmc/esbmc.

## Conexões
- [[esbmc-incremental-bmc-counterexample-trace]] — Veja também: Uso prático com --incremental-bmc e leitura do trace de contraexemplo por estados.

## Fontes
- [ESBMC — README oficial](https://raw.githubusercontent.com/esbmc/esbmc/master/README.md) — README oficial do ESBMC com oito linguagens suportadas, cinco frontends (Clang, Soot/Jimple, CPython 3.10, Solidity e ESBMC-PLC), algoritmos incremental BMC e k-induction, erros detectados, sete solvers SMT mais --bitwuzllob e --neurosym, PPA/Homebrew, integrações e trace de contraexemplo.; consultado em 2026-10-03.
- [ESBMC Documentation — Integrations e guias oficiais](https://esbmc.github.io/docs/integrations) — Documentação oficial do ESBMC sobre integrações (VS Code, ESBMC-Web, Claude Code plugin e GitHub Action) e guias de uso.; consultado em 2026-10-03.
