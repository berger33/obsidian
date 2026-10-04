---
id: software.testes.tranche25.001916
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
fontes: ["https://raw.githubusercontent.com/creusot-rs/creusot/master/README.md", "https://guide.creusot.rs/installation.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Fluxo de atualização do Creusot: git pull, opam update e ./INSTALL

## Em uma frase
A subseção Upgrading Creusot define os quatro passos para atualizar uma instalação existente: (1) entrar no repositório git do Creusot clonado anteriormente na instalação, (2) atualizar os fontes com git pull, (3) atualizar a lista de pacotes do opam com opam update e (4) reinstalar rodando ./INSTALL.

## Por que importa
Como novas versões do Creusot podem exigir versões atualizadas de bibliotecas OCaml/Why3 distribuídas via opam, rodar apenas git pull e cargo build sem executar opam update antes do ./INSTALL pode falhar por incompatibilidade de dependências no switch do opam.

## Como funciona
Sempre que atualizar o checkout do Creusot com git pull, execute opam update na sequência imediata antes de disparar ./INSTALL novamente.

## Exemplo
Uma rotina de atualização limpa em três comandos dentro do clone existente é: git pull && opam update && ./INSTALL.

## Limites e trade-offs
Se o repositório clonado na instalação original tiver sido apagado, basta refazer o fluxo de clone e ./INSTALL; manter o clone local facilita upgrades incrementais rápidos.

## Como verificar
Conferi a subseção Upgrading Creusot no README oficial.

## Conexões
- [[creusot-installation-rustup-opam-install]] — Veja também: Instalação de usuário em cinco passos: rustup, opam, ./INSTALL e cargo creusot --help.
- [[creusot-icfem22-academic-citation]] — Veja também: Base científica e citação acadêmica: publicação no ICFEM'22.

## Fontes
- [Creusot — README oficial](https://raw.githubusercontent.com/creusot-rs/creusot/master/README.md) — README oficial do Creusot com verificação dedutiva para Rust, tradução para Coma na plataforma Why3, exemplos da suíte, projetos CreuSAT e Krabka, instalação via rustup/opam/./INSTALL, upgrade e publicação ICFEM'22.; consultado em 2026-10-03.
- [Creusot Guide — Installation e documentação oficial](https://guide.creusot.rs/installation.html) — Guia oficial do Creusot sobre instalação, linguagem de especificação e uso com cargo creusot.; consultado em 2026-10-03.
