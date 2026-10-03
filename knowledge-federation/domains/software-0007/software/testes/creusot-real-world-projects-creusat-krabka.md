---
id: software.testes.tranche25.001914
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
fontes: ["https://raw.githubusercontent.com/creusot-rs/creusot/master/README.md", "https://github.com/creusot-rs/creusot"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Projetos reais verificados com Creusot: CreuSAT e Krabka

## Em uma frase
A seção Projects built with Creusot destaca dois sistemas de porte construídos e verificados com a ferramenta: o CreuSAT (github.com/sarsko/creusat), um solucionador SAT escrito em Rust e verificado com Creusot que "really pushes the tool to its limits and gives an idea of what 'use in anger' looks like", e o Krabka (github.com/krabka-io/krabka-broker/), um broker Kafka escrito em Rust com algoritmos-chave de segurança verificados com Creusot.

## Por que importa
Exemplos acadêmicos de dez linhas raramente convencem engenheiros de que um verificador aguenta estruturas de dados complexas e otimizações reais; um SAT solver verificado (CreuSAT) e algoritmos de um broker Kafka (Krabka) provam que o fluxo Rust -> Coma -> Why3 escala além de brinquedos.

## Como funciona
Quando precisar estruturar provas em um projeto Rust maior, estude o repositório do CreuSAT como referência de uso intensivo ("use in anger") e o Krabka como exemplo de verificação focada nos algoritmos críticos de segurança de um sistema distribuído.

## Exemplo
No Krabka, a abordagem descrita pelo README não exige provar cada linha de I/O de rede do broker, mas sim isolar e verificar com Creusot os algoritmos-chave de segurança.

## Limites e trade-offs
Ambos são projetos externos mantidos em seus próprios repositórios; eles ilustram o potencial da ferramenta, mas exigem esforço substancial de especificação e prova por parte dos autores.

## Como verificar
Conferi a seção Projects built with Creusot no README oficial.

## Conexões
- [[creusot-canonical-examples-suite]] — Veja também: Os cinco exemplos de entrada na suíte oficial do repositório.
- [[creusot-installation-rustup-opam-install]] — Veja também: Instalação de usuário em cinco passos: rustup, opam, ./INSTALL e cargo creusot --help.

## Fontes
- [Creusot — README oficial](https://raw.githubusercontent.com/creusot-rs/creusot/master/README.md) — README oficial do Creusot com verificação dedutiva para Rust, tradução para Coma na plataforma Why3, exemplos da suíte, projetos CreuSAT e Krabka, instalação via rustup/opam/./INSTALL, upgrade e publicação ICFEM'22.; consultado em 2026-10-03.
- [Repositório oficial creusot-rs/creusot](https://github.com/creusot-rs/creusot) — Repositório oficial do Creusot no GitHub com ARCHITECTURE.md, examples/, tests/should_succeed e CONTRIBUTING.md.; consultado em 2026-10-03.
